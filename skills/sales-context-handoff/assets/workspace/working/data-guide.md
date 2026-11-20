# Workspace data guide

This workspace holds sales evidence and findings for handoff. It persists between the four workflow stages and between conversations. Read progress.json first.

## Files

- raw/: unchanged source exports and captures. Keep private.
- working/: progress, normalized tables, exact extracts and draft reports. Keep private.
- handoff/: selected, reviewed copies only. Portable folder layout mirrors working.
- tools/context_tools.py: standard-library validation, review-manifest preview and ZIP packaging. Python 3.10+; no network or packages required.

Setup creates structure; collection starts offer/ICP drafts and refines them while filling records; analysis reconciles those drafts and writes the remaining reports; handoff makes reviewed copies. Preserve old records and user edits on resume. If the user changes scope, record the change and reconcile the affected rows rather than blindly appending.

All files above live in the verified local project workspace. Save and read back each batch's artifacts there before marking progress. Keep any additional working tables in working/ with evidence references. Chat links should open files already saved in the project; users should not need to download or reattach intermediate results. If only temporary/session storage is available, restore project access before continuing artifact-producing work.

Use this guide as a shared reference for the current milestone. Setup needs Files and Progress; collection needs Progress, Record contract, Extract format and validation; analysis needs Reports and citations and validation; handoff needs the shareable-copy rules and review/package commands. Instructions for later milestones are not tasks to execute early.

## Progress

Complete scope with business, supplied website URL, selected offers as a list, motion (commercial/noncommercial), rep/team scope and exact ISO dates. A website is optional; supplied documents or a user explanation can establish the offer scope. Do not ask who receives the handoff.

For noncommercial conversions, outcome_definitions contains objects with key, meaning, category (positive/negative/intermediate/unknown) and evidence_required. Define these from the stated goal and actual source statuses, not a scoring model. Example: an attendance goal can define registered as intermediate, attended as positive, cancelled as negative and unknown as unknown. Do not map no reply to a negative final outcome. All populated outcomes.csv outcome values must reference a defined key; leave conflicting values blank and explain them in the cited extracts.

readiness contains status (not_reviewed/needs_collection/ready/accepted_limited), summary, material_gaps and user_decision. It records the agent's evidence-coverage assessment; accepted_limited requires the user's actual decision after reviewing the listed gaps. findings_review contains status (pending/reviewed) and user_decision. Drafts remain partial until the findings are reviewed and coverage is ready or its limits accepted. Reset findings review after material changes; keep user decisions attributable. These records do not replace the later review of exact files and redactions in handoff/review.json.

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

Identifiers are stable workspace keys: a-0001 for accounts, c-0001 for contacts, d-0001 for deals, o-0001 for outreach, r-0001 for outcome observations and ev-0001 for evidence. They are not row numbers. Allocate once, retain on resume, and never reassign after an omission.

| Table | Required meaning |
|---|---|
| accounts.csv | One identifiable company per row. Store observed attributes, profile_url (company profile or CRM record URL) and evidence IDs. Domain is optional; do not infer it from a company name. |
| contacts.csv | One identifiable person per row, independent of company. Preserve name, observed profile/CRM URL, role, source_keys and evidence_ids. Email is optional private matching data: retain it in working only and leave the column empty in handoff. account_id is optional. Never omit a person because their company is unknown. |
| deals.csv | One commercial opportunity per row, linked to an account or contact. Preserve original_stage. outcome is won, lost, no_decision, disqualified, open or blank. origin can record outbound, inbound, referral, expansion or the source's own wording. fit_note is attributed, never assumed from outcome. Leave this table empty for noncommercial cases. |
| outreach.csv | One sequence/example per row. deal_id is optional. channel is the source channel. outcome is reply, meeting, associated_closed_won, no_reply or blank. additional_success is true only for one of the up to 10 reply/meeting examples outside the selected deal sample; otherwise false. extract_path identifies the preserved sequence. |
| outcomes.csv | One sourced status observation per subject and event/campaign instance. scope_key identifies that instance, not a person. outcome references outcome_definitions. Preserve multiple stages as separate dated observations (e.g. registration then attendance). Link the account/contact and any verified outreach/deal association; association does not establish causation. Record unresolved status as unknown if defined, or blank if conflicting, with evidence of what was checked. |
| evidence.csv | One captured evidence item per row. source_id points to progress sources. source_key identifies the original record. source_locator is a URL returned by the source, record ID, file/sheet/row, or transcript timestamp; never invent a URL. |

Required nonempty fields:
- accounts: account_id, company, evidence_ids.
- contacts: contact_id, name, source_keys, evidence_ids.
- deals: deal_id, source_keys, selection_reason, evidence_ids, and at least one of account_id/contact_id.
- outreach: outreach_id, source_keys, channel, additional_success, extract_path, evidence_ids, and at least one of account_id/contact_id.
- outcomes: outcome_id, scope_key, source_keys, evidence_ids, and at least one of account_id/contact_id. deal_id, outreach_id and event_date are optional when unavailable.
- evidence: evidence_id, source_id, source_key, source_locator, observed_at, kind, coverage, extract_path.

Join multiple evidence_ids or source_keys with a pipe, with no empty entries. Source keys include the source namespace and object type. Do not merge similarly named companies or distinct opportunities. Only add source aliases when evidence establishes identity.

Capture profile_url from the selected source rather than guessing it. For named examples, put the account/contact link alongside conversation and outcome source links in reports. Missing profile links remain blank in tables and explicit in coverage notes. A source thread/record URL can identify an example when a profile URL is unavailable. Existing source attributes are collection; researching missing attributes elsewhere is enrichment and remains out of scope. Profile links and names may be redacted in shareable copies at the user's request.

Evidence kinds: recorded_fact, buyer_statement, seller_explanation, user_clarification. A user_clarification is an explanation from the person running the analysis, attributed to them. Interpretations and hypotheses belong in reports, not fabricated evidence rows. Coverage is complete, partial or excerpt; complete means the stated item was fully captured, not that the whole source was searched.

extract_path is relative to working/ (or handoff/ in the shareable copy), e.g. extracts/ev-0001.md. Use one Markdown extract per evidence ID. Exact sequences can include several message passages in chronological order; evidence rows can cite different original sources for outcome verification. Use local references for everything needed by a recipient, even if source systems require login.

## Extract format

Start with evidence ID and a neutral description. Include source, exact locator, event date if known, observation date, speaker/role if known and capture coverage. Quote the exact relevant content. Add [OMITTED: ...] or [REDACTED: ...] markers where needed. Distinguish collector notes from quotations.

When a table row contains values from several sources, explain which source supports which value in the extracts. Preserve conflicting values there; leave the disputed normalized cell empty. A user clarification can settle a working interpretation, but it does not rewrite a raw record.

## Reports and citations

At the start of collection, create offer.md and icp.md inside working/reports/ from selected website/offer material, supplied documents or attributed user context. Preserve the initial source-based drafts and refine current working definitions as evidence arrives. During analysis, reconcile these two files and write sales-context.md, findings.md, outreach-examples.md and gaps.md in the same folder. Cite evidence with a relative link, e.g. [ev-0001](../extracts/ev-0001.md). Keep linked evidence in a handoff when its finding is included. Hypotheses must be labeled and supported by cited observations. The helper checks structure and references; it cannot establish that a claim is true.

During handoff, copy only selected rows/extracts/reports. Maintain account/contact/deal/outreach/outcome/evidence referential integrity. Remove private raw paths, unrelated personal data and unneeded source details from shareable copies; retain source mappings in working. An evidence source_locator can become a neutral record label plus its local extract reference if the original locator is sensitive.

Exclude email addresses from all handoff contents, including quoted text, source identifiers and links. Blank contacts.csv email cells and visibly mark redactions in excerpts. Keep names, websites and LinkedIn profiles unless the user excludes them separately. Private originals retain addresses for source matching.

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

Only README.md, the six CSV tables, reports/*.md and extracts/*.md can be packaged. All six table files are required; an empty header-only table is valid when there are no selected records. Put custom-table information needed by the handoff into the standard tables or reports instead of linking to excluded working files. Reports can be omitted if the user excludes them and remaining references still resolve. review.json is private packaging metadata and is not included. Unlisted files are never added.

Packaging refuses unresolved readiness, missing findings review, missing/changed files, broken references, unsafe paths and an existing output archive. The helper validates the recorded decisions, not the truth of the readiness assessment or whether a user actually reviewed the findings. The user shares the resulting ZIP manually.
