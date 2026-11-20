# 02. Collect

Collect scoped deal records, conversations and business context. Save traceable tables, exact extracts and coverage notes for analysis.

## Resume before querying

Locate the user's workspace and read `working/progress.json`. Use the Progress, Record contract, Extract format and validation guidance in `working/data-guide.md`. If the workspace or scope is missing, direct the user to the setup stage rather than inventing setup choices. Reuse the saved scope and source access; repair only an actual access failure or pending connection. Read existing tables and completed source keys; reuse identifiers and continue the saved sample instead of selecting it again. An interrupted batch is partial, not complete.

Read [record collection](evidence/records.md) for CRM, files, email and transcripts, [outreach evidence](evidence/outreach.md) for message selection, and [LinkedIn collection](sources/linkedin.md) only when those sources were selected.

Use [outcome coverage and readiness](evidence/coverage.md) to apply the saved outcome definitions and decide whether the collected sample is sufficient or preliminary.

Use the saved access routes to find and extract the sample yourself. Do not turn collection into a request for the user to assemble threads that selected sources can supply. If a route fails, use [connection guidance](sources/connections.md) to choose a practical alternative and record the reason for any manual request.

Read the stated business concerns and competing explanations in selection_notes or supplied context. Use them to guide searches for both supporting and challenging evidence within the selected sources and sample budget. Preserve the original statements as attributed evidence, including their dates or periods when known; do not assume the user's explanation is the finding.

## Start with the offer and intended audience

Before selecting deal or outreach examples, follow [the offer and ICP draft guidance](evidence/offer-and-icp.md). Read the selected website/offer material and supplied business documents, capture evidence and create `working/reports/offer.md` and `working/reports/icp.md`. These are initial source-based drafts, not verified conclusions. If resuming, read and refine the existing drafts rather than restarting them. Use the initial understanding to guide relevant searches while including counterexamples rather than collecting only cases that fit it.

## Select a useful bounded sample

Use the chosen business, rep/team and dates:
1. Find up to 10 won and 10 lost opportunities, preferring recent records. Include user-identified best-fit and poor-fit wins when available. Record selection reasons rather than interpreting a win as good fit.
2. If short, ask once whether to extend the period or continue with a shortfall. Do not block the workflow on unavailable history.
3. Offer expansion only when useful; never exceed 50 sampled deals without a new scope. Include up to 10 additional reply/meeting outreach successes outside the closed-deal sample.
4. Use connector filters or export rows to identify candidates before opening conversations. Do not enumerate an entire mailbox. If a source cannot support scoped searching, check the other selected access routes before requesting a narrower export or specific user-picked threads.

Keep different opportunities at one company distinct. Preserve original stages and loss reasons alongside normalized outcomes. Silence, a declined meeting, and an unanswered InMail do not establish a lost deal. Conflicting outcome sources remain unresolved until clarified.

For noncommercial work, replace the won/lost sample with up to 10 confirmed positive and 10 confirmed negative cases under the agreed definitions, where available, within a 50-case collection budget. Keep unknown cases separate and report shortfalls. Use outcome-bearing sources to find examples on both sides, then link conversations; do not select solely by replies or successful-link searches. Save the selection rule and denominators. Do not create fictional commercial deals for registrations or attendance.

## Capture evidence

Read the relevant records and conversations. Keep raw source captures in `raw/`; create concise, exact extracts in `working/extracts/` with source locators and dates. Do not invent message text or expand ellipses.

Populate accounts, contacts, deals, outreach, outcomes and evidence tables according to the workspace guide. Each example must have an identifiable account or contact. Capture observed profile/CRM record links, role and organization from the selected sources; keep source conversation and outcome-record links as well. Do not omit a contact because their company is unknown. Report missing identity links as gaps, never manufacture URLs. Preserve known attributes as supplied; leave unknown fields empty. Do not research missing firmographics or start enrichment.

Capture any further relevant passages from business documents, including qualification/scoring rules, sales stages, selling guidance and constraints. Preserve document dates/versions and current or historical status when known. For multiple offers, identify the associated offer in deal extracts when known; leave unclear associations unresolved.

For sampled commercial cases, capture available sales-handling history and customer-value evidence using the corresponding section of [record collection guidance](evidence/records.md). Store details in linked extracts using existing record/evidence IDs; no new required CSV fields or separate report is needed. These inputs are best-effort within selected sources, not prerequisites for collection or a reason to add enrichment.

Use [customer context, signals and triggers guidance](evidence/customer-context-and-signals.md) to capture the situation behind each case: needs, current workflow, alternatives, constraints, decision criteria and dated changes relevant to timing. Record when a fact became knowable and whether it was public or private. Preserve counterexamples as well as successes; do not invent predictive signals or enrich missing context.

Capture exact opening messages, follow-ups and relevant replies when available. Label reply, meeting and associated-closed-won outcomes with their actual evidence. A reply can be negative; label sentiment only when the wording supports it. Keep unanswered comparison examples distinct from additional successes.

After each small batch, save rows and extracts in the local project workspace and read them back, then mark its source keys complete in progress. Record partial threads, failed searches, unavailable sources and the next cursor/action. Stop browser work at login challenges, restrictions or unavailable pages; keep collected evidence and offer manual extracts.

Refine `offer.md` and `icp.md` with the batch's supporting and contradictory evidence, following the linked draft guidance. Keep the initial source-based descriptions visible and record material changes with citations. These two living drafts are part of collection; the remaining reports and overall synthesis belong to Analyze.

## Check and finish

Run `python tools/context_tools.py validate .` from the workspace when Python is available. Otherwise perform the same identifier, duplicate and reference checks using the data guide and state that the helper was not run. Inspect plausible duplicate warnings; never merge on company name alone.

Show distinct case counts by confirmed outcome and unknown status, coverage, missing identity links and two or three named, linked examples. Briefly show how the offer and ICP drafts changed or remain uncertain. Assess readiness using the coverage reference. Point to the saved project files and briefly identify what each contains and which sources it draws from. Additional task-specific tables, if useful, also belong in `working/` and must retain evidence references; they do not replace the standard tables or source mapping. Do not offer intermediate files as downloads. Mark collection complete or partial honestly. Do not start the Analyze stage automatically.

If coverage is sufficient, offer analysis and explain its purpose. If material gaps remain, propose the specific additional collection needed and let the user choose further collection or preliminary analysis with those limits. Wait for their answer; a completed batch alone is not a reason to advance.
