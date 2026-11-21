# 01. Setup

Prepare the workspace and connect the user's selected data sources so collection can retrieve relevant evidence with minimal manual work from the user. Save the business and offer scope, history period and verified access for collection.

## Start from what exists

Start with the context already supplied in chat. On a fresh setup, ask for the missing inputs in one message with the two numbered groups below. Do not split business scope, account examples and source locations into separate interview steps. Omit answered items and reuse supplied links. If resuming, read `working/progress.json` only when needed to recover saved answers. Do not repeat installation checks, run the helper or inventory connections before this opening. If the inputs are already sufficient, proceed to the next concrete setup action.

Use this opening, adapted to the user's context:

1. **Your business:** What's your website, and which offers should we focus on? Name a few best-fit accounts you've won, poor-fit accounts you've won, and accounts you've lost. Links and brief reasons help. Skip any group you cannot name.
2. **Your data sources:** Where do you keep the relevant records and conversations? For example: CRM, spreadsheets, email, transcripts, LinkedIn or Sales Navigator. Include any existing ICP, qualification or sales documents. Point me to the sources you'd like to use or connect.

Names are enough to start. Websites, LinkedIn profiles or CRM links help identify the right accounts. Offer pages, decks or a short explanation can substitute for a website. Account examples and existing documents are optional. Do not ask for a quota, copied threads or attachments that the agent can retrieve. Ask follow-up questions only when a missing or ambiguous answer affects scope, access or collection. Do not re-ask skipped optional inputs.

Adapt both groups to the activity. For event invitations or other noncommercial outreach, ask for useful contact or organization examples and known outcomes instead of closed accounts. Use a project/event name and dates as search anchors. Do not invent won/lost deals. If the activity is already clear, omit its answered business questions while retaining any useful unanswered inputs.

Save supplied account/contact identities in `progress.selection_notes`. Preserve the user's group, reason, links and any known offer or deal dates. Attribute fit judgments and reported outcomes to the user; they are not yet verified findings. Keep best-fit and poor-fit wins distinct from losses. A lost account is not automatically poor fit. Resolve ambiguous account or opportunity matches from selected sources during collection; ask only if ambiguity remains material.

Read the supplied website's relevant offer pages or supplied documents only far enough to confirm the selected offers. Summarize that understanding for correction before collection; record the URLs or file locations for later evidence capture. Ask about sales-team scope if needed. Propose the last 12 calendar months ending on the user's current date, showing exact dates, and offer a different period for historical exports. Save the agreed dates; do not silently shift them to fit an old file.

Establish what counts as the outcome before selecting examples. Use recorded stages and the user's stated goal first. If unclear, ask a plain-language question such as "Does success here mean registration or actual attendance?" Save scope.motion as commercial or noncommercial. For noncommercial work, save outcome_definitions with the observed stages, meanings, positive/negative/intermediate/unknown categories and evidence needed to verify them. Explain the proposed mapping for correction; the user need not design a schema. Preserve intermediate engagement separately from final outcomes, and leave unresolved results unknown.

Don't require the user to define an ICP or know qualification terminology. Capture any existing definitions or frameworks they use; otherwise, ask plain-language questions about their customers and sales process.

Reuse any stated reason for this work. Capture reported symptoms and explanations with attribution in `progress.selection_notes`. Treat them as claims to examine, not established causes. Ask about the purpose only if it materially changes the scope. A general handoff needs no extra diagnostic interview.

The source group already invites existing documents. Do not ask for them again as a separate step. Relevant material includes ICP definitions, qualification models, sales playbooks, offer decks, pricing and past win/loss reviews. Save supplied locations as sources, with dates or versions and current/historical status when known. Do not ask the user to create missing documents.

## Prepare the workspace

Read the Files and Progress sections of [the workspace data guide](../assets/workspace/working/data-guide.md) and [connection guidance](sources/connections.md).

Choose file operations and paths for the user's actual operating system and available tools. The user need not choose a development stack.

Use a dedicated `sales-context-workspace` folder inside the selected location unless a workspace already exists. Copy the contents of `assets/workspace/` into it, including hidden files, and rename `gitignore.template` to `.gitignore` in the new workspace. Never overwrite an existing workspace with the starter. Preserve the data guide and helper so later stages and new conversations can use them. Create a temporary probe file in `working/`, read it back, then remove that probe to verify persistence. If write access fails, resolve the folder permission before claiming setup is complete.

Confirm the actual local project path with the user in the setup summary. The persistence probe must target that folder, not a temporary execution directory or chat attachment store. If the app exposes only session storage, help connect the local project folder and verify it before collection; do not substitute a download-and-reattach workflow.

Fill `working/progress.json` with scope, website, selected offers, dates, source choices, access status and the current milestone. Keep credentials and session cookies out of files. In a new workspace, leave collection tables empty for the collection milestone. Preserve existing records and milestone progress when repairing setup.

## Connect the selected sources

Inspect available connection metadata for the selected sources and reuse existing access where appropriate. A connected source is a candidate, not proof it belongs to this business. Do not search unrelated folders or read unrelated accounts.

Choose access routes using [connection guidance](sources/connections.md), balancing coverage, fidelity, setup effort and user preference. Guide connection setup for selected sources, then perform the small access check yourself. Leave authentication and user-only permission actions to the user. Save the chosen route and any remaining action so collection can retrieve the evidence without asking for it again. Do not install a custom scraper or require paid enrichment.
- Verify new or changed connections with one relevant record or file. Reuse a saved successful access check unless access has failed or the account changed.
- For files, inspect actual sheets and columns rather than assuming a CRM schema.
- For browser access, the user signs in themselves. Check both LinkedIn and Sales Navigator if selected.
- Record source states: ready, partial, skipped, inaccessible or awaiting_export. Use partial with a next action while connection setup is pending; an unconnected source is not automatically inaccessible. Proceed with usable sources; do not repeatedly ask for a skipped source.
- If a LinkedIn export is pending, record its status and whether a bounded browser route is usable in the meantime; collection need not wait for the archive.

## Finish

Save setup as complete, or partial with the actual blocker. Show the selected offers, workspace location, ready/skipped/pending sources and agreed dates in a few lines. Do not begin collecting the full sample automatically.

Offer collection: "Next is collection: I'll draft your offer and intended audience from the website or supplied material, then refine them with evidence from your selected sources. Shall we proceed?" Wait for the user's answer.
