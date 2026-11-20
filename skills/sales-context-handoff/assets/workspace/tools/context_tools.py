"""Validate a sales-context workspace and package an explicitly reviewed allowlist.

Python 3.10+, standard library only. No network access or source mutations.
"""
from __future__ import annotations

import argparse
import csv
from datetime import date
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import sys
from urllib.parse import unquote, urlsplit
import zipfile

HEADERS = {
    "accounts.csv": "account_id,company,domain,industry,employee_band,revenue_band,geography,evidence_ids".split(","),
    "deals.csv": "deal_id,account_id,source_keys,outcome,original_stage,closed_date,amount,currency,origin,fit_note,selection_reason,evidence_ids".split(","),
    "outreach.csv": "outreach_id,account_id,deal_id,source_keys,channel,outcome,additional_success,extract_path,evidence_ids".split(","),
    "evidence.csv": "evidence_id,source_id,source_key,source_locator,event_date,observed_at,kind,coverage,extract_path".split(","),
}
REQUIRED = {
    "accounts.csv": "account_id company evidence_ids".split(),
    "deals.csv": "deal_id account_id source_keys selection_reason evidence_ids".split(),
    "outreach.csv": "outreach_id account_id source_keys channel additional_success extract_path evidence_ids".split(),
    "evidence.csv": "evidence_id source_id source_key source_locator observed_at kind coverage extract_path".split(),
}
ID_FIELDS = {"accounts.csv": ("account_id", "a"), "deals.csv": ("deal_id", "d"),
             "outreach.csv": ("outreach_id", "o"), "evidence.csv": ("evidence_id", "ev")}
LINK = re.compile(r"\[([^\]]*)\]\(([^\s)]+)\)")
EVIDENCE_ID = re.compile(r"\bev-\d{4,}\b")


def safe_path(root: Path, relative: str, *, links: bool = False) -> Path:
    """Resolve within root, rejecting traversal (except in validated report links)."""
    if not isinstance(relative, str) or not relative or "\\" in relative or ":" in relative:
        raise ValueError(f"Invalid relative path: {relative!r}")
    parts = PurePosixPath(relative)
    if parts.is_absolute() or (not links and ".." in parts.parts):
        raise ValueError(f"Unsafe path: {relative}")
    candidate = root / relative
    resolved = candidate.resolve()
    if not resolved.is_relative_to(root.resolve()):
        raise ValueError(f"Path escapes workspace area: {relative}")
    for p in (candidate, *candidate.parents):
        if p == root.parent:
            break
        if p.is_symlink() or (hasattr(p, "is_junction") and p.is_junction()):
            raise ValueError(f"Linked path is not allowed: {relative}")
    return candidate


def allowed(relative: str) -> bool:
    path = PurePosixPath(relative)
    return relative == "README.md" or relative in HEADERS or (
        len(path.parts) == 2 and path.parts[0] in {"reports", "extracts"}
        and path.suffix == ".md" and not path.name.startswith(".")
    )


def split_ids(value: str) -> list[str]:
    return value.split("|") if value else []


def read_progress(workspace: Path) -> dict:
    value = json.loads(safe_path(workspace, "working/progress.json").read_text(encoding="utf-8-sig"))
    if not isinstance(value, dict) or value.get("version") != 1:
        raise ValueError("Unsupported progress manifest; expected version 1")
    return value


def validate(workspace: Path, area: str = "working", selected: set[str] | None = None) -> dict:
    workspace = Path(workspace).resolve()
    if area not in {"working", "handoff"}:
        raise ValueError("Area must be working or handoff")
    root = safe_path(workspace, area)
    errors, warnings, tables = [], [], {}
    progress = read_progress(workspace)
    sources = progress.get("sources", [])
    if not isinstance(sources, list) or any(not isinstance(s, dict) for s in sources):
        raise ValueError("progress.sources must be a list of source objects")
    source_ids = [s.get("source_id") for s in sources]
    if any(not isinstance(s, str) or not s for s in source_ids) or len(set(source_ids)) != len(source_ids):
        errors.append("Source IDs must be nonempty and unique")
    for source in sources:
        if source.get("status") not in {"ready", "partial", "awaiting_export", "inaccessible", "skipped"}:
            errors.append(f"Invalid source status: {source.get('source_id')}")
        if source.get("status") != "ready":
            warnings.append(f"Source {source.get('source_id')}: {source.get('status')}")
        keys = source.get("completed_keys", [])
        if not isinstance(keys, list) or any(not isinstance(k, str) for k in keys) or len(set(keys)) != len(keys):
            errors.append(f"Invalid or duplicate completed keys: {source.get('source_id')}")
    scope = progress.get("scope", {})
    for field in ("start_date", "end_date"):
        if scope.get(field):
            try:
                date.fromisoformat(scope[field])
            except (ValueError, TypeError):
                errors.append(f"Invalid scope date: {field}")
    if scope.get("start_date") and scope.get("end_date") and scope["start_date"] > scope["end_date"]:
        errors.append("Scope start_date is after end_date")

    def check_file(relative: str) -> Path | None:
        try:
            target = safe_path(root, relative)
            if not target.is_file():
                raise ValueError(f"Missing file: {relative}")
            if selected is not None and relative not in selected:
                raise ValueError(f"Referenced file is not in reviewed allowlist: {relative}")
            return target
        except ValueError as exc:
            errors.append(str(exc))
            return None

    for name, headers in HEADERS.items():
        file = check_file(name)
        rows = []
        if file:
            with file.open(encoding="utf-8-sig", newline="") as stream:
                reader = csv.DictReader(stream)
                if reader.fieldnames != headers:
                    errors.append(f"{name}: headers do not match the workspace contract")
                for number, row in enumerate(reader, 2):
                    if None in row or any(v is None for v in row.values()):
                        errors.append(f"{name}:{number}: malformed CSV row")
                        continue
                    if set(row) != set(headers):
                        continue
                    for field in REQUIRED[name]:
                        if not row[field].strip():
                            errors.append(f"{name}:{number}: missing {field}")
                    rows.append(row)
        tables[name] = rows
        id_field, prefix = ID_FIELDS[name]
        ids, source_keys = set(), set()
        for row in rows:
            identity = row[id_field]
            if not re.fullmatch(prefix + r"-\d{4,}", identity):
                errors.append(f"Invalid {id_field}: {identity}")
            if identity in ids:
                errors.append(f"Duplicate {id_field}: {identity}")
            ids.add(identity)
            for key in split_ids(row.get("source_keys", "")):
                if not key or key in source_keys:
                    errors.append(f"{name}: duplicate or empty source key: {key}")
                source_keys.add(key)

    accounts = {r["account_id"]: r for r in tables["accounts.csv"]}
    deals = {r["deal_id"]: r for r in tables["deals.csv"]}
    evidence = {r["evidence_id"]: r for r in tables["evidence.csv"]}
    for row in tables["accounts.csv"]:
        for key in ("domain", "company"):
            value = row[key].strip().casefold()
            if value and sum(r[key].strip().casefold() == value for r in accounts.values()) > 1:
                warnings.append(f"Possible duplicate account {key}: {row[key]}; inspect, do not auto-merge")
    for name in ("accounts.csv", "deals.csv", "outreach.csv"):
        for row in tables[name]:
            refs = split_ids(row["evidence_ids"])
            if len(refs) != len(set(refs)):
                errors.append(f"{name}: repeated evidence ID")
            for ref in refs:
                if ref not in evidence:
                    errors.append(f"{name}: unknown evidence ID {ref}")
            if name != "accounts.csv" and row["account_id"] not in accounts:
                errors.append(f"{name}: unknown account {row['account_id']}")
    for row in deals.values():
        if row["outcome"] not in {"", "won", "lost", "no_decision", "disqualified", "open"}:
            errors.append(f"{row['deal_id']}: invalid outcome")
        if row["closed_date"]:
            try:
                date.fromisoformat(row["closed_date"])
            except ValueError:
                errors.append(f"{row['deal_id']}: invalid closed_date")
    for row in tables["outreach.csv"]:
        deal = deals.get(row["deal_id"])
        if row["deal_id"] and not deal:
            errors.append(f"{row['outreach_id']}: unknown deal")
        if deal and deal["account_id"] != row["account_id"]:
            errors.append(f"{row['outreach_id']}: deal/account mismatch")
        if row["outcome"] not in {"", "reply", "meeting", "associated_closed_won", "no_reply"}:
            errors.append(f"{row['outreach_id']}: invalid outreach outcome")
        if row["outcome"] == "associated_closed_won" and (not deal or deal["outcome"] != "won"):
            errors.append(f"{row['outreach_id']}: closed-won association requires a won deal")
        if row["additional_success"] not in {"true", "false"}:
            errors.append(f"{row['outreach_id']}: additional_success must be true or false")
        if row["additional_success"] == "true" and (row["deal_id"] or row["outcome"] not in {"reply", "meeting"}):
            errors.append(f"{row['outreach_id']}: additional success requires reply/meeting outside sampled deals")
        cited_extracts = {evidence[ref]["extract_path"] for ref in split_ids(row["evidence_ids"]) if ref in evidence}
        if row["extract_path"] not in cited_extracts:
            errors.append(f"{row['outreach_id']}: sequence extract must be backed by its evidence IDs")
        check_file(row["extract_path"])
    for row in evidence.values():
        if row["source_id"] not in source_ids:
            errors.append(f"{row['evidence_id']}: unknown source")
        # Retain the earlier identifier for already-saved evidence; new rows use user_clarification.
        if row["kind"] not in {"recorded_fact", "buyer_statement", "seller_explanation", "user_clarification", "client_clarification"}:
            errors.append(f"{row['evidence_id']}: invalid evidence kind")
        if row["coverage"] not in {"complete", "partial", "excerpt"}:
            errors.append(f"{row['evidence_id']}: invalid coverage")
        extract = PurePosixPath(row["extract_path"])
        if len(extract.parts) != 2 or extract.parts[0] != "extracts" or extract.suffix != ".md":
            errors.append(f"{row['evidence_id']}: extract_path must identify an extracts/*.md file")
        for field in ("event_date", "observed_at"):
            if row[field]:
                try:
                    date.fromisoformat(row[field].split("T")[0])
                except ValueError:
                    errors.append(f"{row['evidence_id']}: invalid {field}")
        check_file(row["extract_path"])

    counts = {"accounts": len(accounts), "deals": len(deals), "won": sum(r["outcome"] == "won" for r in deals.values()),
              "lost": sum(r["outcome"] == "lost" for r in deals.values()), "outreach": len(tables["outreach.csv"]),
              "additional_successes": sum(r["additional_success"] == "true" for r in tables["outreach.csv"]), "evidence": len(evidence)}
    limits = progress.get("limits", {})
    if counts["deals"] > limits.get("deal_cap", 50):
        errors.append("Deal sample exceeds configured cap")
    if counts["additional_successes"] > limits.get("additional_success_cap", 10):
        errors.append("Additional outreach successes exceed configured cap")
    for outcome in ("won", "lost"):
        if counts[outcome] < limits.get(outcome + "_target", 10):
            warnings.append(f"Sample shortfall: {counts[outcome]} {outcome}; report the limitation")

    markdown = [p for p in root.rglob("*.md") if p.relative_to(root).as_posix() != "data-guide.md"]
    for file in markdown:
        relative = file.relative_to(root).as_posix()
        if selected is not None and relative not in selected:
            continue
        if not check_file(relative):
            continue
        content = file.read_text(encoding="utf-8-sig")
        for label, url in LINK.findall(content):
            parts = urlsplit(url)
            if parts.scheme in {"http", "https", "mailto"}:
                continue
            if not parts.path:
                continue
            try:
                combined = (PurePosixPath(relative).parent / unquote(parts.path)).as_posix()
                target = safe_path(root, combined, links=True)
                target_relative = target.resolve().relative_to(root.resolve()).as_posix()
                check_file(target_relative)
                if EVIDENCE_ID.fullmatch(label) and label in evidence and target_relative != evidence[label]["extract_path"]:
                    errors.append(f"{relative}: {label} links to the wrong extract")
            except ValueError as exc:
                errors.append(f"{relative}: {exc}")
        # Check citation labels, not evidence-like text inside exact quoted messages.
        for label, _ in LINK.findall(content):
            if EVIDENCE_ID.fullmatch(label) and label not in evidence:
                errors.append(f"{relative}: unknown evidence citation {label}")
    if area == "handoff":
        check_file("README.md")
    return {"errors": sorted(set(errors)), "warnings": sorted(set(warnings)), "counts": counts}


def draft_manifest(workspace: Path) -> dict:
    root = safe_path(Path(workspace).resolve(), "handoff")
    files = []
    for file in sorted(root.rglob("*")):
        relative = file.relative_to(root).as_posix()
        if file.is_file() and allowed(relative):
            checked = safe_path(root, relative)
            files.append({"path": relative, "sha256": hashlib.sha256(checked.read_bytes()).hexdigest()})
    return {"status": "draft", "reviewed_at": "", "files": files}


def package(workspace: Path, output: Path) -> dict:
    workspace = Path(workspace).resolve()
    root = safe_path(workspace, "handoff")
    review = json.loads(safe_path(root, "review.json").read_text(encoding="utf-8-sig"))
    if review.get("status") != "reviewed" or not review.get("reviewed_at"):
        raise ValueError("Review is incomplete; a draft manifest does not record your approval")
    date.fromisoformat(review["reviewed_at"])
    entries = review.get("files")
    if not isinstance(entries, list) or not entries:
        raise ValueError("Reviewed allowlist is empty")
    payload = {}
    for item in entries:
        relative = item["path"]
        if not allowed(relative) or relative in payload:
            raise ValueError(f"Not an allowed unique handoff path: {relative}")
        file = safe_path(root, relative)
        data = file.read_bytes()
        if hashlib.sha256(data).hexdigest() != item["sha256"]:
            raise ValueError(f"Content changed since review: {relative}")
        payload[relative] = data
    result = validate(workspace, "handoff", set(payload))
    if result["errors"]:
        raise ValueError("Handoff validation failed: " + "; ".join(result["errors"]))
    # Use the already hashed bytes so later filesystem changes cannot enter the ZIP.
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for relative, data in sorted(payload.items()):
            archive.writestr(relative, data)
    output = Path(output)
    if output.suffix.lower() != ".zip":
        raise ValueError("Output must have a .zip extension")
    with output.open("xb") as stream:
        stream.write(buffer.getvalue())
    with zipfile.ZipFile(output) as archive:
        if archive.testzip() is not None or set(archive.namelist()) != set(payload):
            raise ValueError("Archive verification failed")
    return {"archive": str(output.resolve()), "files": sorted(payload), "warnings": result["warnings"]}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest="command", required=True)
    check = subs.add_parser("validate")
    check.add_argument("workspace", type=Path)
    check.add_argument("--area", choices=("working", "handoff"), default="working")
    manifest = subs.add_parser("manifest")
    manifest.add_argument("workspace", type=Path)
    bundle = subs.add_parser("package")
    bundle.add_argument("workspace", type=Path)
    bundle.add_argument("output", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "validate":
            result = validate(args.workspace, args.area)
        elif args.command == "manifest":
            result = draft_manifest(args.workspace)
        else:
            result = package(args.workspace, args.output)
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 1 if result.get("errors") else 0
    except (OSError, ValueError, KeyError, TypeError, csv.Error) as exc:
        print(json.dumps({"errors": [str(exc)]}, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    sys.exit(main())
