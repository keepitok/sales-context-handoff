# 01. Setup

Prepare the workspace and connect the user's selected data sources so collection can retrieve relevant evidence with minimal manual work from the user. Save the business and offer scope, history period and verified access for collection.

## Start from what exists

Inspect the user-selected project folder and available connection metadata. Read an existing `working/progress.json` before asking anything. Reuse saved scope and verified connections; ask only about missing or changed choices. Do not search unrelated folders or read unrelated accounts. A connected source is a candidate, not proof it belongs to this business.

When the user has already described their activity, begin by asking where its records and conversations live. Do not ask them to select, copy or attach a quota of example threads to begin setup. Ask for a source location and a useful search anchor, such as a project/event name and dates, rather than material the agent could retrieve. Adapt questions to the stated activity; do not assume outreach concerns closed deals.

Inspect supplied context first. Ask only what is missing, at most three short questions at a time, using choices when the app supports them:

- What is your business website, and which offer or offers should this handoff cover? Offer pages, sales decks or a short explanation can substitute for a website.
- Where do you keep the relevant sales records and conversations: CRM or spreadsheets, email, existing transcripts, LinkedIn, Sales Navigator? Each source can be skipped.

Read the supplied website's relevant offer pages or supplied documents only far enough to confirm the selected offers. Summarize that understanding for correction before collection; record the URLs or file locations for later evidence capture. Ask about sales-team scope if needed. Propose the last 12 calendar months ending on the user's current date, showing exact dates, and offer a different period for historical exports. Save the agreed dates; do not silently shift them to fit an old file.

Don't require the user to define an ICP or know qualification terminology. Capture any existing definitions or frameworks they use; otherwise, ask plain-language questions about their customers and sales process.

Also offer an optional document input: "Do you have existing documents that explain who you sell to, how you qualify deals or how your team sells? You can share files or links, point me to a connected folder, or skip this." Give a few relevant examples if useful: ICP or buyer-persona definitions; qualification/scoring models and pipeline-stage criteria; sales playbooks or objection guides; offer decks and pricing; positioning or competitor notes; previous customer research or win/loss reviews. Reuse documents already supplied. Do not ask the user to create missing documents or complete a checklist. Save selected file/link locations as sources for collection; note known dates or versions and whether the user considers them current.

## Prepare the workspace

Read the Files and Progress sections of [the workspace data guide](../assets/workspace/working/data-guide.md) and [connection guidance](sources/connections.md).

Choose file operations and paths for the user's actual operating system and available tools. The user need not choose a development stack.

Use a dedicated `sales-context-workspace` folder inside the selected location unless a workspace already exists. Copy the contents of `assets/workspace/` into it, including hidden files, and rename `gitignore.template` to `.gitignore` in the new workspace. Never overwrite an existing workspace with the starter. Preserve the data guide and helper so later stages and new conversations can use them. Create a temporary probe file in `working/`, read it back, then remove that probe to verify persistence. If write access fails, resolve the folder permission before claiming setup is complete.

Fill `working/progress.json` with scope, website, selected offers, dates, source choices, access status and the current milestone. Keep credentials and session cookies out of files. In a new workspace, leave collection tables empty for the collection milestone. Preserve existing records and milestone progress when repairing setup.

## Connect the selected sources

Choose access routes using [connection guidance](sources/connections.md), balancing coverage, fidelity, setup effort and user preference. Guide connection setup for selected sources, then perform the small access check yourself. Leave authentication and user-only permission actions to the user. Save the chosen route and any remaining action so collection can retrieve the evidence without asking for it again. Do not install a custom scraper or require paid enrichment.
- Verify new or changed connections with one relevant record or file. Reuse a saved successful access check unless access has failed or the account changed.
- For files, inspect actual sheets and columns rather than assuming a CRM schema.
- For browser access, the user signs in themselves. Check both LinkedIn and Sales Navigator if selected.
- Record source states: ready, partial, skipped, inaccessible or awaiting_export. Use partial with a next action while connection setup is pending; an unconnected source is not automatically inaccessible. Proceed with usable sources; do not repeatedly ask for a skipped source.
- If a LinkedIn export is pending, record its status and whether a bounded browser route is usable in the meantime; collection need not wait for the archive.

## Finish

Save setup as complete, or partial with the actual blocker. Show the selected offers, workspace location, ready/skipped/pending sources and agreed dates in a few lines. Do not begin collecting the full sample automatically.

Offer collection: "Next is collection: I'll retrieve the agreed evidence from your selected sources and save traceable records and exact messages. Shall we proceed?" Wait for the user's answer.
