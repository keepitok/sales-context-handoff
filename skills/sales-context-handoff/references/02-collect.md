# 02. Collect

Collect scoped deal records, conversations and business context. Save traceable tables, exact extracts and coverage notes for analysis.

## Resume before querying

Locate the user's workspace and read `working/progress.json`. Use the Progress, Record contract, Extract format and validation guidance in `working/data-guide.md`. If the workspace or scope is missing, direct the user to the setup stage rather than inventing setup choices. Reuse the saved scope and source access; repair only an actual access failure or pending connection. Read existing tables and completed source keys; reuse identifiers and continue the saved sample instead of selecting it again. An interrupted batch is partial, not complete.

Read [record collection](evidence/records.md) for CRM, files, email and transcripts, [outreach evidence](evidence/outreach.md) for message selection, and [LinkedIn collection](sources/linkedin.md) only when those sources were selected.

Use the saved access routes to find and extract the sample yourself. Do not turn collection into a request for the user to assemble threads that selected sources can supply. If a route fails, use [connection guidance](sources/connections.md) to choose a practical alternative and record the reason for any manual request.

## Select a useful bounded sample

Use the chosen business, rep/team and dates:
1. Find up to 10 won and 10 lost opportunities, preferring recent records. Include user-identified best-fit and poor-fit wins when available. Record selection reasons rather than interpreting a win as good fit.
2. If short, ask once whether to extend the period or continue with a shortfall. Do not block the workflow on unavailable history.
3. Offer expansion only when useful; never exceed 50 sampled deals without a new scope. Include up to 10 additional reply/meeting outreach successes outside the closed-deal sample.
4. Use connector filters or export rows to identify candidates before opening conversations. Do not enumerate an entire mailbox. If a source cannot support scoped searching, check the other selected access routes before requesting a narrower export or specific user-picked threads.

Keep different opportunities at one company distinct. Preserve original stages and loss reasons alongside normalized outcomes. Silence, a declined meeting, and an unanswered InMail do not establish a lost deal. Conflicting outcome sources remain unresolved until clarified.

## Capture evidence

Read the relevant records and conversations. Keep raw source captures in `raw/`; create concise, exact extracts in `working/extracts/` with source locators and dates. Do not invent message text or expand ellipses.

Populate accounts, deals, outreach and evidence tables according to the workspace guide. Preserve known attributes as supplied; leave unknown fields empty. Do not research missing firmographics or start enrichment.

Also capture relevant passages from the selected website/offer pages and supplied business documents: offer, existing ICP/personas, qualification or scoring rules, sales stages, selling guidance and commercial constraints. Preserve document dates/versions and current or historical status when known. Treat documented strategy and published claims as attributed context, not proof of actual buyer behavior or sales effectiveness; retain discrepancies with deal evidence for analysis. For multiple offers, identify the associated offer in deal extracts when known; leave unclear associations unresolved. Save evidence for analysis rather than drafting reports here.

Capture exact opening messages, follow-ups and relevant replies when available. Label reply, meeting and associated-closed-won outcomes with their actual evidence. A reply can be negative; label sentiment only when the wording supports it. Keep unanswered comparison examples distinct from additional successes.

After each small batch, save rows and extracts first, then mark its source keys complete in progress. Record partial threads, failed searches, unavailable sources and the next cursor/action. Stop browser work at login challenges, restrictions or unavailable pages; keep collected evidence and offer manual extracts.

## Check and finish

Run `python tools/context_tools.py validate .` from the workspace when Python is available. Otherwise perform the same identifier, duplicate and reference checks using the data guide and state that the helper was not run. Inspect plausible duplicate warnings; never merge on company name alone.

Show deal and outreach counts, coverage, missing inputs and two or three evidence examples. Mark collection complete or partial honestly. Do not run synthesis automatically.

Next prompt: "Analyze my sales context and prepare findings for my chosen recipient."
