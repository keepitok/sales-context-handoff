"""Synthetic behavior tests. No real client data or live connections."""
import copy
import csv
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
STARTER = ROOT / "skills/sales-context-handoff/assets/workspace"
spec = importlib.util.spec_from_file_location("context_tools", STARTER / "tools/context_tools.py")
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)


def write_rows(root, name, rows):
    with (root / name).open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=helper.HEADERS[name])
        writer.writeheader()
        writer.writerows(rows)


def read_rows(root, name):
    with (root / name).open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def record(name, **values):
    return dict.fromkeys(helper.HEADERS[name], "") | values


def fixture(workspace, mixed=True):
    """Creative-services business: inbound win, loss, expansion, conflicted deal."""
    shutil.copytree(STARTER, workspace)
    working = workspace / "working"
    progress = json.loads((working / "progress.json").read_text())
    progress["scope"] = {"business": "Synthetic creative subscription", "website": "https://example.invalid", "offers": ["Design support", "Launch assets"], "product": "Design support", "people": "Owner", "start_date": "2025-11-20", "end_date": "2026-11-20"}
    progress["recipient"] = {"role": "new sales hire", "needs": "Understand our offers, objections and qualification practices"}
    progress["sources"] = [{"source_id": "sheet-a", "kind": "spreadsheet", "label": "Synthetic deal export", "status": "ready", "completed_keys": [], "coverage": "Selected rows"}]
    if mixed:
        progress["sources"] += [{"source_id": "mail-a", "kind": "email", "status": "ready", "completed_keys": []}, {"source_id": "calls-a", "kind": "transcript", "status": "ready", "completed_keys": []}]
    progress["milestones"] = {"setup": "complete", "collect": "partial", "analyze": "partial", "handoff": "not_started"}
    progress["last_batch"] = {"status": "partial", "source_id": "sheet-a", "next_action": "Resume after saved rows"}
    (working / "progress.json").write_text(json.dumps(progress), encoding="utf-8")
    message = 'Subject: A design backlog?\n\nHi Rowan,\nCould we help with your launch assets?\n\nReply: "Yes, let’s meet Tuesday."'
    extracts = {
        "ev-0001": "Sheet row 2: Cedar Studio, inbound referral, closed won. Revenue band blank.",
        "ev-0002": "Sheet row 3: Cedar Studio (different business), closed lost. Seller reason: timing.",
        "ev-0003": "Sheet row 4: First Cedar Studio, separate expansion opportunity, closed won.",
        "ev-0004": "Sheet row 5 says won; attached seller note says still open. Outcome unresolved.",
        "ev-0005": message,
        "ev-0006": "Sent: Can we discuss your design backlog? No response visible in the supplied capture.",
        "ev-0007": "Buyer call: Procurement handles the signature; I own the creative budget.",
    }
    evidence = []
    for i, (identity, content) in enumerate(extracts.items(), 1):
        source = "mail-a" if mixed and i in {5, 6} else "calls-a" if mixed and i == 7 else "sheet-a"
        relative = f"extracts/{identity}.md"
        (working / relative).write_text(f"# {identity}\n\nSource: {source}, record {i}; observed 2026-11-20; excerpt.\n\n{content}\n", encoding="utf-8")
        evidence.append(record("evidence.csv", evidence_id=identity, source_id=source, source_key=f"{source}:record:{i}", source_locator=f"Synthetic record {i}", observed_at="2026-11-20", kind="buyer_statement" if i in {5, 7} else "recorded_fact", coverage="excerpt", extract_path=relative))
    write_rows(working, "evidence.csv", evidence)
    write_rows(working, "accounts.csv", [
        record("accounts.csv", account_id="a-0001", company="Cedar Studio", domain="cedar-one.example", evidence_ids="ev-0001"),
        record("accounts.csv", account_id="a-0002", company="Cedar Studio", domain="cedar-two.example", evidence_ids="ev-0002"),
        record("accounts.csv", account_id="a-0003", company="Juniper Studio", evidence_ids="ev-0005"),
    ])
    write_rows(working, "deals.csv", [
        record("deals.csv", deal_id="d-0001", account_id="a-0001", source_keys="sheet-a:opportunity:1", outcome="won", original_stage="Signed", origin="inbound", selection_reason="Recent win", evidence_ids="ev-0001"),
        record("deals.csv", deal_id="d-0002", account_id="a-0002", source_keys="sheet-a:opportunity:2", outcome="lost", original_stage="Closed lost", selection_reason="Recent loss", evidence_ids="ev-0002"),
        record("deals.csv", deal_id="d-0003", account_id="a-0001", source_keys="sheet-a:opportunity:3", outcome="won", original_stage="Signed", origin="expansion", selection_reason="Distinct expansion", evidence_ids="ev-0003|ev-0007"),
        record("deals.csv", deal_id="d-0004", account_id="a-0002", source_keys="sheet-a:opportunity:4", original_stage="Conflicting records", selection_reason="Outcome clarification needed", evidence_ids="ev-0004"),
    ])
    write_rows(working, "outreach.csv", [
        record("outreach.csv", outreach_id="o-0001", account_id="a-0003", source_keys="mail-a:thread:5" if mixed else "sheet-a:thread:5", channel="email", outcome="meeting", additional_success="true", extract_path="extracts/ev-0005.md", evidence_ids="ev-0005"),
        record("outreach.csv", outreach_id="o-0002", account_id="a-0002", deal_id="d-0004", source_keys="mail-a:thread:6" if mixed else "sheet-a:thread:6", channel="email", outcome="no_reply", additional_success="false", extract_path="extracts/ev-0006.md", evidence_ids="ev-0006"),
    ])
    (working / "reports/findings.md").write_text("# Findings\n\nTwo sampled wins are separate opportunities at one company, not two companies. [ev-0001](../extracts/ev-0001.md) [ev-0003](../extracts/ev-0003.md)\n\nOne outcome is contradictory. [ev-0004](../extracts/ev-0004.md)\n\nHypothesis: repeat design demand may matter; delivery quality and retention are unknown. [ev-0003](../extracts/ev-0003.md)\n", encoding="utf-8")
    (workspace / "raw/private.txt").write_text("PRIVATE ORIGINAL Rowan", encoding="utf-8")
    return message


def prepare_handoff(workspace):
    working, handoff = workspace / "working", workspace / "handoff"
    for name in helper.HEADERS:
        shutil.copyfile(working / name, handoff / name)
    shutil.copytree(working / "extracts", handoff / "extracts", dirs_exist_ok=True)
    shutil.copytree(working / "reports", handoff / "reports", dirs_exist_ok=True)
    (handoff / "README.md").write_text("# Reviewed handoff\n\nStart with [findings](reports/findings.md). Tables contain the sampled records; source extracts support them.\n", encoding="utf-8")


def approve_fixture(workspace):
    # Synthetic review only. Production skill must obtain actual client review.
    review = helper.draft_manifest(workspace)
    review.update(status="reviewed", reviewed_at="2026-11-20")
    (workspace / "handoff/review.json").write_text(json.dumps(review), encoding="utf-8")
    return review


class ContextTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.workspace = Path(self.temp.name) / "workspace"
        self.message = fixture(self.workspace)

    def tearDown(self):
        self.temp.cleanup()

    def test_mixed_sources_sparse_sample_missing_attributes_and_distinct_deals(self):
        result = helper.validate(self.workspace)
        self.assertEqual([], result["errors"])
        self.assertEqual(4, result["counts"]["deals"])
        self.assertEqual(2, result["counts"]["won"])
        self.assertTrue(any("shortfall" in w for w in result["warnings"]))
        self.assertTrue(any("duplicate account company" in w for w in result["warnings"]))
        self.assertEqual("", read_rows(self.workspace / "working", "accounts.csv")[0]["revenue_band"])
        self.assertEqual("", read_rows(self.workspace / "working", "deals.csv")[3]["outcome"])

    def test_spreadsheet_only_is_complete_input(self):
        workspace = Path(self.temp.name) / "files-only"
        fixture(workspace, mixed=False)
        self.assertFalse(helper.validate(workspace)["errors"])

    def test_restart_preserves_existing_ids_and_duplicate_source_key_is_detected(self):
        before = (self.workspace / "working/deals.csv").read_bytes()
        progress_before = (self.workspace / "working/progress.json").read_bytes()
        result = subprocess.run([sys.executable, str(self.workspace / "tools/context_tools.py"), "validate", str(self.workspace)], capture_output=True, text=True)
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertEqual(before, (self.workspace / "working/deals.csv").read_bytes())
        self.assertEqual(progress_before, (self.workspace / "working/progress.json").read_bytes())
        rows = read_rows(self.workspace / "working", "deals.csv")
        duplicate = copy.deepcopy(rows[0])
        duplicate["deal_id"] = "d-0005"
        write_rows(self.workspace / "working", "deals.csv", rows + [duplicate])
        self.assertTrue(any("source key" in e for e in helper.validate(self.workspace)["errors"]))

    def test_no_reply_is_not_success_and_closed_won_needs_deal_evidence(self):
        rows = read_rows(self.workspace / "working", "outreach.csv")
        rows[1]["additional_success"] = "true"
        rows[0]["outcome"] = "associated_closed_won"
        write_rows(self.workspace / "working", "outreach.csv", rows)
        errors = helper.validate(self.workspace)["errors"]
        self.assertTrue(any("additional success" in e for e in errors))
        self.assertTrue(any("requires a won deal" in e for e in errors))

    def test_inbound_win_does_not_require_fabricated_outreach(self):
        rows = read_rows(self.workspace / "working", "outreach.csv")
        self.assertFalse(any(row["deal_id"] == "d-0001" for row in rows))
        self.assertFalse(helper.validate(self.workspace)["errors"])

    def test_partial_linkedin_and_missing_navigator_are_coverage_warnings(self):
        path = self.workspace / "working/progress.json"
        progress = json.loads(path.read_text())
        progress["sources"] += [
            {"source_id": "linkedin-a", "kind": "linkedin", "status": "partial", "coverage": "Export lacks opening messages", "completed_keys": ["linkedin-a:thread:1"], "next_action": "Manual extract after login challenge"},
            {"source_id": "navigator-a", "kind": "sales_navigator", "status": "inaccessible", "completed_keys": [], "coverage": "Not verified"},
        ]
        path.write_text(json.dumps(progress))
        result = helper.validate(self.workspace)
        self.assertFalse(result["errors"])
        self.assertIn("Source navigator-a: inaccessible", result["warnings"])
        self.assertIn("Source linkedin-a: partial", result["warnings"])

    def test_unknown_evidence_and_wrong_citation_target_fail(self):
        report = self.workspace / "working/reports/findings.md"
        report.write_text("[ev-9999](../extracts/ev-0001.md) [ev-0001](../extracts/ev-0002.md)")
        errors = helper.validate(self.workspace)["errors"]
        self.assertTrue(any("unknown evidence citation" in e for e in errors))
        self.assertTrue(any("wrong extract" in e for e in errors))

    def test_exact_unicode_and_multiline_message_is_preserved(self):
        prepare_handoff(self.workspace)
        approve_fixture(self.workspace)
        output = Path(self.temp.name) / "messages.zip"
        helper.package(self.workspace, output)
        with zipfile.ZipFile(output) as archive:
            data = archive.read("extracts/ev-0005.md")
            self.assertEqual((self.workspace / "handoff/extracts/ev-0005.md").read_bytes(), data)
            self.assertIn(self.message, data.decode("utf-8").replace("\r\n", "\n"))

    def test_redaction_preserves_original_and_excludes_raw_unselected_and_metadata(self):
        prepare_handoff(self.workspace)
        extract = self.workspace / "handoff/extracts/ev-0005.md"
        extract.write_text(extract.read_text(encoding="utf-8").replace("Rowan", "[REDACTED: person name]"), encoding="utf-8")
        (self.workspace / "handoff/private.txt").write_text("DO NOT SHARE")
        (self.workspace / "handoff/reports/unselected.md").write_text("Not selected by client")
        review = approve_fixture(self.workspace)
        review["files"] = [f for f in review["files"] if f["path"] != "reports/unselected.md"]
        (self.workspace / "handoff/review.json").write_text(json.dumps(review))
        original = (self.workspace / "raw/private.txt").read_bytes()
        output = Path(self.temp.name) / "redacted.zip"
        result = helper.package(self.workspace, output)
        with zipfile.ZipFile(output) as archive:
            self.assertEqual(set(result["files"]), set(archive.namelist()))
            self.assertNotIn("review.json", archive.namelist())
            self.assertNotIn("private.txt", archive.namelist())
            self.assertNotIn("reports/unselected.md", archive.namelist())
            self.assertNotIn(b"Rowan", archive.read("extracts/ev-0005.md"))
        self.assertEqual(original, (self.workspace / "raw/private.txt").read_bytes())
        self.assertIn("Rowan", (self.workspace / "working/extracts/ev-0005.md").read_text(encoding="utf-8"))

    def test_draft_review_cannot_package(self):
        prepare_handoff(self.workspace)
        (self.workspace / "handoff/review.json").write_text(json.dumps(helper.draft_manifest(self.workspace)))
        with self.assertRaisesRegex(ValueError, "Review is incomplete"):
            helper.package(self.workspace, Path(self.temp.name) / "draft.zip")

    def test_changed_reviewed_file_fails_without_archive(self):
        prepare_handoff(self.workspace)
        approve_fixture(self.workspace)
        (self.workspace / "handoff/accounts.csv").write_text("changed")
        output = Path(self.temp.name) / "changed.zip"
        with self.assertRaisesRegex(ValueError, "changed since review"):
            helper.package(self.workspace, output)
        self.assertFalse(output.exists())

    def test_allowlist_must_include_referenced_extracts(self):
        prepare_handoff(self.workspace)
        review = approve_fixture(self.workspace)
        review["files"] = [f for f in review["files"] if f["path"] != "extracts/ev-0001.md"]
        (self.workspace / "handoff/review.json").write_text(json.dumps(review))
        with self.assertRaisesRegex(ValueError, "not in reviewed allowlist"):
            helper.package(self.workspace, Path(self.temp.name) / "missing.zip")

    def test_traversal_absolute_paths_and_raw_are_rejected(self):
        prepare_handoff(self.workspace)
        for path in ("../raw/private.txt", "raw/private.txt", "C:/secret.txt", "/secret.txt"):
            with self.subTest(path=path):
                review = approve_fixture(self.workspace)
                review["files"].append({"path": path, "sha256": "0" * 64})
                (self.workspace / "handoff/review.json").write_text(json.dumps(review))
                with self.assertRaises(ValueError):
                    helper.package(self.workspace, Path(self.temp.name) / "unsafe.zip")

    def test_report_link_cannot_escape_handoff(self):
        prepare_handoff(self.workspace)
        (self.workspace / "handoff/reports/findings.md").write_text("[private](../../raw/private.txt)")
        approve_fixture(self.workspace)
        with self.assertRaisesRegex(ValueError, "escapes"):
            helper.package(self.workspace, Path(self.temp.name) / "escape.zip")

    def test_existing_archive_is_not_overwritten(self):
        prepare_handoff(self.workspace)
        approve_fixture(self.workspace)
        output = Path(self.temp.name) / "existing.zip"
        output.write_bytes(b"original")
        with self.assertRaises(FileExistsError):
            helper.package(self.workspace, output)
        self.assertEqual(b"original", output.read_bytes())

    def test_sample_caps(self):
        path = self.workspace / "working/progress.json"
        progress = json.loads(path.read_text())
        progress["limits"]["deal_cap"] = 3
        progress["limits"]["additional_success_cap"] = 0
        path.write_text(json.dumps(progress))
        errors = helper.validate(self.workspace)["errors"]
        self.assertIn("Deal sample exceeds configured cap", errors)
        self.assertIn("Additional outreach successes exceed configured cap", errors)

    def test_outreach_cannot_point_to_unrelated_extract(self):
        rows = read_rows(self.workspace / "working", "outreach.csv")
        rows[0]["extract_path"] = "extracts/ev-0002.md"
        write_rows(self.workspace / "working", "outreach.csv", rows)
        self.assertTrue(any("backed by its evidence" in error for error in helper.validate(self.workspace)["errors"]))

    def test_evidence_cannot_reference_progress_or_other_non_extract_file(self):
        rows = read_rows(self.workspace / "working", "evidence.csv")
        rows[0]["extract_path"] = "progress.json"
        write_rows(self.workspace / "working", "evidence.csv", rows)
        self.assertTrue(any("extracts/*.md" in error for error in helper.validate(self.workspace)["errors"]))


if __name__ == "__main__":
    unittest.main()
