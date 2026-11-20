# Workspace data guide

This workspace holds sales evidence and findings for handoff. It persists between the four workflow stages and between conversations. Read progress.json first.

## Files

- raw/: unchanged source exports and captures. Keep private.
- working/: progress, normalized tables, exact extracts and draft reports. Keep private.
- handoff/: selected, reviewed copies only. Portable folder layout mirrors working.
- tools/context_tools.py: standard-library validation, review-manifest preview and ZIP packaging. Python 3.10+; no network or packages required.

Setup creates structure; collection fills records; analysis writes reports; handoff makes reviewed copies. Preserve old records and user edits on resume. If the user changes scope, record the change and reconcile the affected rows rather than blindly appending.

All files above live in the verified local project workspace. Save and read back each batch's artifacts there before marking progress. Keep any additional working tables in working/ with evidence references. Chat links should open files already saved in the project; users should not need to download or reattach intermediate results. If only temporary/session storage is available, restore project access before continuing artifact-producing work.

Use this guide as a shared reference for the current milestone. Setup needs Files and Progress; collection needs Progress, Record contract, Extract format and validation; analysis needs Reports and citations and validation; handoff needs the shareable-copy rules and review/package commands. Instructions for later milestones are not tasks to execute early.

## Progress

Complete scope with business, supplied website URL, selected offers as a list, rep/team scope and exact ISO dates. Retain product when present in an older workspace; confirm its meaning before using it to fill offers. A website is optional; supplied documents or a user explanation can establish the offer scope.

Older workspaces may contain recipient metadata. Leave it intact on resume, but do not request, require or use it to select a report variant. Prepare the common handoff without resetting existing evidence or progress.

All four milestones use not_started, partial or complete. Sources are objects with:

```json
{
  "source_id": "crm-a",
  "kind": "crm",
  "label": "Selected sales CRM",
  "status": "ready",
  "scope": "Selected team and dates",
  "coverage": "",
  "completed_keys": [],
  "next_action": ""
}
```

Kinds: crm, spreadsheet, email, transcript, linkedin, sales_navigator, document, user.
Status: ready, partial, awaiting_export, inaccessible, skipped.

Record source coverage honestly. completed_keys records processed source records/threads, not guessed completeness of an entire account. For an interrupted batch, write last_batch.status as partial and a concrete next_action. Save rows/extracts before marking completion. Inspect saved rows on restart even if the manifest lagged behind the last write.

Use gaps as short objects: subject, state (missing/unqueried/inaccessible/contradictory), impact and next_input. Record sampling choices and period extensions in selection_notes. Preserve the initial defaults unless the user changes scope explicitly.

## Record contract

UTF-8 CSV with headers, quoted multiline cells where needed. Leave unavailable values empty. Never use zero, "N/A" or a guessed value to mean missing.

Identifiers are stable workspace keys: a-0001 for accounts, d-0001 for deals, o-0001 for outreach and ev-0001 for evidence. They are not row numbers. Allocate once, retain on resume, and never reassign after an omission.

| Table | Required meaning |
|---|---|
| accounts.csv | One identifiable company per row. Store only observed firmographics and supporting evidence IDs. Domain is optional; do not infer it from a company name. |
| deals.csv | One opportunity per row; account_id links the company. Preserve original_stage. outcome is won, lost, no_decision, disqualified, open or blank. origin can record outbound, inbound, referral, expansion or the source's own wording. fit_note is attributed, never assumed from outcome. |
| outreach.csv | One sequence/example per row. deal_id is optional. channel is the source channel. outcome is reply, meeting, associated_closed_won, no_reply or blank. additional_success is true only for one of the up to 10 reply/meeting examples outside the selected deal sample; otherwise false. extract_path identifies the preserved sequence. |
| evidence.csv | One captured evidence item per row. source_id points to progress sources. source_key identifies the original record. source_locator is a URL returned by the source, record ID, file/sheet/row, or transcript timestamp; never invent a URL. |

Required nonempty fields:
- accounts: account_id, company, evidence_ids.
- deals: deal_id, account_id, source_keys, selection_reason, evidence_ids.
- outreach: outreach_id, account_id, source_keys, channel, additional_success, extract_path, evidence_ids.
- evidence: evidence_id, source_id, source_key, source_locator, observed_at, kind, coverage, extract_path.

Join multiple evidence_ids or source_keys with a pipe, with no empty entries. Source keys include the source namespace and object type. Do not merge similarly named companies or distinct opportunities. Only add source aliases when evidence establishes identity.

Evidence kinds: recorded_fact, buyer_statement, seller_explanation, user_clarification. A user_clarification is an explanation from the person running the analysis, attributed to them. Interpretations and hypotheses belong in reports, not fabricated evidence rows. Coverage is complete, partial or excerpt; complete means the stated item was fully captured, not that the whole source was searched.

extract_path is relative to working/ (or handoff/ in the shareable copy), e.g. extracts/ev-0001.md. Use one Markdown extract per evidence ID. Exact sequences can include several message passages in chronological order; evidence rows can cite different original sources for outcome verification. Use local references for everything needed by a recipient, even if source systems require login.

## Extract format

Start with evidence ID and a neutral description. Include source, exact locator, event date if known, observation date, speaker/role if known and capture coverage. Quote the exact relevant content. Add [OMITTED: ...] or [REDACTED: ...] markers where needed. Distinguish collector notes from quotations.

When a table row contains values from several sources, explain which source supports which value in the extracts. Preserve conflicting values there; leave the disputed normalized cell empty. A user clarification can settle a working interpretation, but it does not rewrite a raw record.

## Reports and citations

During analysis, write sales-context.md, findings.md, outreach-examples.md and gaps.md inside working/reports/. Cite evidence with a relative link, e.g. [ev-0001](../extracts/ev-0001.md). Keep linked evidence in a handoff when its finding is included. Hypotheses must be labeled and supported by cited observations. The helper checks structure and references; it cannot establish that a claim is true.

During handoff, copy only selected rows/extracts/reports. Maintain account/deal/evidence referential integrity. Remove private raw paths, unrelated personal data and unneeded source details from shareable copies; retain source mappings in working. An evidence source_locator can become a neutral record label plus its local extract reference if the original locator is sensitive.

## Review and helper commands

Run these commands from the workspace root. `python` stands for an available Python 3.10+ interpreter; check its version and substitute the appropriate launcher, such as `python3` or `py -3`. Adapt shell commands and filesystem paths to the current environment.

Collection and analysis use `validate .`. The handoff milestone uses `validate . --area handoff`, `manifest` and `package` after preparing the shareable copies. Setup only copies the helper; it does not run these commands.

```text
python tools/context_tools.py validate .
python tools/context_tools.py validate . --area handoff
python tools/context_tools.py manifest .
python tools/context_tools.py package . sales-context-handoff.zip
```

manifest prints JSON to standard output; it does not approve anything. After user review, save the relevant file list as handoff/review.json with status "reviewed" and reviewed_at set to the actual ISO date. Each file entry contains path and sha256. Regenerate hashes and review changed contents after any edits.

Only README.md, the four CSV tables, reports/*.md and extracts/*.md can be packaged. All four table files are required; an empty header-only table is valid when there are no selected records. Reports can be omitted if the user excludes them and remaining references still resolve. review.json is private packaging metadata and is not included. Unlisted files are never added.

Packaging refuses missing/changed files, broken references, unsafe paths and an existing output archive. This does not replace human review of redactions. The user shares the resulting ZIP manually.
