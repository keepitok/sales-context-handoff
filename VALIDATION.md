# Validation and live checks

This document is for maintainers and coding agents changing or verifying the workflow. Validation covers synthetic evidence handling, workspace persistence, skill portability and handoff contents. Live app checks are tracked separately below.

## Repository layout

```text
skills/sales-context-handoff/  Skill entry point, references, notices and starter workspace
tests/              Synthetic evidence, handoff and skill portability tests
VALIDATION.md       Tested behavior and live-app verification steps
upstream.json       Pinned upstream revisions and original file hashes
adaptation-map.json Mapping from borrowed sources to adapted files
```

[Upstream records](upstream.json) and the [adaptation map](adaptation-map.json) document the sources and changes. Preserve the original source identifiers and bundled licenses when adapting skills.

## Automated checks

The workspace helper and tests require Python 3.10 or later and use only the standard library, with no additional packages. Run the following from the repository root. Substitute the available Python launcher, such as `python3` or `py -3`, after checking its version.

```sh
python -m unittest discover -s tests -v
```

The synthetic tests exercise actual CSV files, saved state, separate helper-process invocation and ZIP contents:

- Spreadsheet-only and mixed spreadsheet/email/transcript evidence.
- Sparse samples, missing attributes, conflicting outcomes, identical company names and separate opportunities at one company.
- Inbound win without invented outreach, additional meeting success without a closed deal and unanswered comparison outreach.
- Contacts without companies, same-name contacts, duplicate profile identities, and separate registration/attendance observations without fabricated deals.
- Defined noncommercial outcomes, distinct-case limits, unrelated contact links and missing evidence.
- Partial LinkedIn coverage, inaccessible Sales Navigator and preserved restart state. These test recorded coverage and resumption invariants, not live browser automation.
- Duplicate source-key detection, evidence references, wrong citation targets and sample limits.
- Exact Unicode/multiline message preservation, redaction of shareable copies with unchanged originals, and exclusion of unselected/private files.
- Rejection of unreviewed or changed files, incomplete allowlists, escaping paths, unrelated extract references and overwriting an existing archive.
- Readiness and findings-review checks before packaging, explicit acceptance of limited coverage, and contact redaction that preserves private originals and stable outcome links.
- Rejection of populated contact email fields in handoff copies, with private addresses preserved. Email addresses embedded elsewhere still require manual cross-file redaction review.

The skill entry point is checked with the skill-creator validator. Portability checks copy the skill and starter workspace into a temporary folder, follow links from the index through numbered stages and supporting references, verify metadata and licenses, and run the copied helper in a new process. The skill baseline was copied from pinned upstream checkouts before adaptation.

The common index loads one stage at a time: `01-setup.md`, `02-collect.md`, `03-analyze.md` and `04-handoff.md` under `references/`. Source and evidence references are loaded only when needed by the current stage. The progress keys remain `setup`, `collect`, `analyze` and `handoff`.

The helper checks structure, counts, references and reviewed bytes. It does not determine whether an agent chose a representative sample, whether an inference follows from a quotation, or whether every sensitive fact has been redacted. Those require a real workflow review.

During development, keep one current workspace contract in the runtime helper. If an existing test workspace needs migration after a model change, prepare a one-off helper under ignored `tmp/`, preview and test it on a copy, and preserve a backup before applying it. Do not add compatibility branches to the distributed skill or commit temporary migration helpers and data.

## Live app status

| Capability | Status |
|---|---|
| Single skill folder, numbered stage references and OpenAI metadata | Validated on disk |
| New-process workspace/helper access | Tested with synthetic saved files |
| Project-only skill installation, discovery and natural-language routing in a fresh ChatGPT Work project | User-reported attempt chose a personal folder and desktop check; instructions revised, behavioral retest pending |
| Installation-to-setup transition | User-reported run requested manual threads before source discovery; instructions revised, behavioral retest pending |
| Claude Cowork project-local instructions, discovery and folder persistence | Not yet tested in a signed-in Cowork session; no account-level upload fallback |
| Live CRM/email/transcript connectors | Not exercised |
| LinkedIn/Sales Navigator browser extraction | Unverified until tested in an authorized account |

No customer accounts were accessed or private conversations collected during implementation.

## First run in your workspace

1. Install `sales-context-handoff` in the chosen app. Confirm it is available; use setup to verify a write/read in the selected folder. Check that it asks only for missing business/offer scope, dates and source choices, without asking who receives the handoff. Confirm that the agent loads only setup and its relevant references, then pauses before collection. Check the same stage routing and pause on subsequent prompts.
2. Start with a small supplied spreadsheet. Run collection, open the tables/extracts and confirm exact values and locators. Continue in a new conversation and verify no duplicate records.
3. Add one authorized relevant email/transcript source if available. Check linkage to the same opportunity and attribution of buyer versus seller statements.
4. If LinkedIn is selected, compare one exported thread with its visible original. Independently check Sales Navigator. Test a missing thread through the available browser; verify exact text and partial-coverage handling. Record success only for capabilities actually demonstrated.
5. Run analysis and inspect every material finding against its extract. Check that the common reports need no recipient information. Confirm the seven reports in the report guide: offer, icp, customer-context, sales-context, outcome-analysis, examples and gaps. Check that ICP covers buyer roles, customer context covers signals/triggers, and examples covers both a documented journey and outreach sequences. Check named linked examples and limitations. Confirm no enrichment, invented scoring or causal claim about an outreach message.
6. Review a concrete handoff, request one redaction, package it, and inspect the archive. Confirm originals remain private and the redaction appears everywhere needed.

Keep any remaining failures in your coverage/gap record; do not label untested integrations as verified.

## Setup behavior regression checks

These require an agent run; repository unit tests do not establish conversational behavior.

- Request installation in a fresh project with a writable project folder and an inaccessible personal skills directory. Expect the full skill copied only inside the project, file-based verification and no personal-directory writes, account upload, desktop check or computer-control request. When automatic discovery is unknown, expect an explicit distinction between saved/readable instructions and verified discovery, with direct project-file invocation offered. Repeat with project write access unavailable: expect folder-access guidance or project-local manual-copy steps, never an account-wide or desktop-control workaround.

- Supply a document mixing actual cases with illustrative results and proposed ICP criteria, plus younger and older opportunity groups, different offers and a separately sourced aggregate report. Expect passage-level evidence labels, no hypothetical cases in observed tables/counts, and comparisons qualified by available context and observation time. Population figures retain their own denominator and do not merge with sampled-case rates. Repeat without dates or report definitions: expect descriptive findings and stated limits, not invented cutoffs, compulsory new sources or a blocked workflow solely for these missing details. Behavioral validation of this scenario is pending.

- Supply conflicting seller explanations for a sales problem, a loss with delayed follow-up, a high-value win with documented delivery burden, a retained/expanded customer and a recent win without renewal history. Expect attributed concerns preserved from setup, handling/value evidence linked to the original cases, and analysis that does not equate losses with poor fit or wins with customer value. The recent win's retention remains unknown; conflicting causes remain unresolved unless evidence separates them. Repeat with a general handoff and none of these optional records: expect no invented problem, mandatory additional source or blocked completion, with only relevant limitations stated. Behavioral validation of this scenario is pending.

- Give the agent a writable local project folder. After a collection batch, verify tables, extracts and progress exist there and can be read in a new conversation without attachments. Expect a project-path summary, not a download link. Repeat with only session storage available: expect folder-access resolution before collection, not a download-and-reattach workaround. Check any task-specific CSV retains evidence references in working/.

- Install and ask for the next step in a fresh project. Expect availability confirmation, a one-sentence setup purpose, the privacy note and two numbered input groups in the same response: business website/offers and optional account examples; source locations/connections and optional existing documents, without "Ready to begin?" or another prompt. Repeat with partial answers: expect answered items omitted and the remaining inputs asked together. A known event activity should get relevant contact/outcome wording, no fictional closed deals, no recipient question and no assignment to attach sample threads. Explicitly request installation only and a stop: expect no setup questions. Behavioral retest is pending.
- Interrupt the setup conversation, then say "continue". Expect the current stage and next unanswered question, without reinstalling, asking whether to start or stopping at a generic project-status announcement. On a new-conversation resume, allow a narrow progress read to reuse saved answers; when scope and sources are already sufficient, expect the next concrete setup action instead of redundant questions. Tool permissions remain separate from workflow continuation. Behavioral retest is pending.
- Install while describing a test scenario and supplying a URL or source names. Expect those details reused in setup rather than requested again. Follow setup's scoped connection checks as answers arrive; installation and setup answers must not start sample collection. An explicit request to start setup should also proceed without another confirmation.
- Finish each of setup, collection and analysis. Expect saved results and a coverage/findings review where required before offering the next stage, with no next-stage execution until the user agrees. Test "yes" as acceptance and a clarification question as continued discussion. Resume a completed stage in a new conversation and check that the next stage is offered, not silently started.
- Start collection with website/offer material that names one audience, then supply deal or conversation evidence supporting some criteria and contradicting another. Expect offer.md and icp.md before deal sampling, cited refinements after batches, preserved initial source-based descriptions and explicit uncertainty. Analyze should reconcile those same files without inventing criteria or duplicating them in other analysis reports. Repeat without an accessible website: supplied documents or attributed user context should establish a limited draft without blocking collection.
- Supply a buyer-stated operational problem, a dated pre-outreach event, a seller's trigger theory and a fact learned only after the outcome. Include a negative case sharing the event. Expect customer-context to preserve needs and alternatives and its signals/triggers section to distinguish observations from theories and public availability from private/post-outcome knowledge, with no claim of validated prediction. Supply a senior title without authority evidence and a contact demonstrating advocacy; expect the buyer-roles section of icp to distinguish title from demonstrated role. Check that every topic in the merged reports receives a substantive synthesis or an explicit evidence shortfall.
- Supply an event sample with replies but mostly unknown registrations/attendance. Expect preliminary reports, explicit missing comparison and audience-fit evidence, then a targeted collection proposal or a question about accepting limited coverage. Saved reports must not trigger an immediate packaging invitation. Accept limited coverage, review findings and then verify that handoff can proceed.
- Include contacts with no company and two people with the same name. Expect all sampled people in standard tables, observed profile/source-record links beside named examples, unresolved name matches left unknown, and no guessed attributes. Include registered/attended/cancelled examples and check that outcome timelines do not inflate distinct-case counts or imply outreach caused conversion.
- Start setup with email as the selected source but no connection. Expect discovery of available connection options and guidance through authorization, then a small scoped read. Full collection waits until setup is reviewed.
- Use an already connected source. Expect reuse and scoped retrieval during collection, without asking the user to copy messages or export them unnecessarily.
- Make automated access unavailable, decline connection, or prefer a small one-off extract. Expect a brief explanation of the practical alternative and a bounded request for only necessary material.
- Select LinkedIn without a ready archive. Expect a relevant export request and a small browser access check during setup. After the user starts collection, expect a few browser examples while the export prepares, then work on other sources rather than an inbox sweep. Reuse existing requests. If export is declined or unavailable, expect a bounded browser alternative. No third-party extraction service or custom browser-tool installation should be proposed. Sales Navigator coverage remains separate.
- Deliver an export notification during collection. Expect actual archive inspection before claiming readiness, local filtering for broader collection, deduplication against browser samples and browser use only for remaining gaps. The skill must not promise delivery within ten minutes or treat a notification for Invitations as proof that Messages are available.
- Mention invitation notes and later messages. If exporting, expect Invitations plus Messages, with clarification only if private notes are ambiguous. Setup should use the documented categories rather than researching them anew. A pending archive must not block usable browser collection or other sources; later archive overlaps must be deduplicated.
- Supply an archive containing Messages but no Invitations, plus a private connection note and two people sharing a name. Expect explicit invitation-coverage gaps, private notes attributed as seller context and no unsupported thread linkage. Connection acceptance alone must not become a reply or another success. These are behavioral scenarios awaiting an agent run, not claims of automated test coverage.
- Make both built-in and external browser surfaces available. Expect the built-in route without desktop inspection unless the user explicitly chooses another browser. If it is unavailable or insufficient, expect connector/export/manual options rather than automatic Chrome or full-computer control. An explicit external-browser choice permits that browser, not native desktop settings/control. Check that a saved preference is reused on resume and that sign-in or folder-connection steps are explained for the user to perform.

- Provide setup examples from all three account groups, including duplicate company names, multiple opportunities, an out-of-period case and a fit judgment contradicted by source evidence. Expect saved attributed search anchors, scoped identity resolution and targeted collection within the sample budget. Add source-selected cases and counterexamples. Expect ICP analysis to distinguish supported, challenged and unresolved fit judgments from deal outcomes. Repeat with all optional examples/documents skipped and resume in a new conversation: no repeated requests, blocked collection or duplicate records. Behavioral validation is pending.
