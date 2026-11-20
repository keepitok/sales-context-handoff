# LinkedIn export: capabilities and setup

Read this when LinkedIn is selected during setup, or when interpreting a supplied archive. Use these documented capabilities to guide the user; verify account access and actual coverage instead of researching export options from scratch on every run. Refresh the official guidance if the interface, available categories or returned files differ.

## Documented categories

Checked 2026-11-20 against [LinkedIn's data-download documentation](https://www.linkedin.com/help/sales-navigator/answer/a1339364).

| Category | Documented contents | Use in this workflow |
| --- | --- | --- |
| Invitations | Sent/received invitations, participants' names and URLs, sent date and message | Opening text attached to a connection request |
| Messages | Sent, received and archived messages, with dates, subject, content and profile URL | Follow-ups and replies |
| Connections | First-degree connections, profile URL, company, position and connection date; email only where permitted | Optional identity matching; not outreach text or proof of a reply |
| Premium Connection Notes | Notes written about connections, creation/edit dates and associated identities | Optional seller context, not a message delivered to the connection |

LinkedIn says returned categories depend on account activity. Category availability does not guarantee a particular thread, field or historical period is complete. Inspect the actual files.

If "connection notes" means text sent with connection requests, use Invitations. Ask a brief clarification only when it could instead mean private notes. When exporting invitation-led outreach followed by messages, select both Invitations and Messages; a Messages-only export may omit the opening evidence needed here. Add Connections or private notes only when useful to the agreed scope.

## Request the export, sample while it prepares

The same LinkedIn help page lists Invitations within 10 minutes and Messages, Connections and Premium Connection Notes within 48 hours. Its general instructions say specific categories arrive within minutes and a larger archive within 24 hours. These estimates are inconsistent; use the account's displayed estimate/status and never promise a delivery time.

Use a hybrid route by default:

- Reuse a readable archive that already covers the scope, or an existing pending request. Otherwise request the relevant export categories during setup.
- Explain the next step plainly: "While LinkedIn prepares the export, I can collect a few relevant examples in the built-in browser. Once the archive is ready, I'll use it for the broader collection." The agent does the browser extraction; this is not an assignment for the user to copy messages.
- During setup, verify access with a small read only. After the user proceeds to collection, gather a few relevant threads while the archive prepares, then work on other selected sources. Do not turn the preview into a contact-by-contact inbox sweep.
- When the archive arrives, filter it locally and reconcile overlapping browser captures without duplication. Use the browser afterward for specific gaps.
- If the user declines export or it is unavailable, use bounded browser collection with an explicit coverage limit. Do not wait idly, repeatedly request archives or silently expand the sample.

Use native exports and the app's available browser for this workflow. Third-party extraction services and custom Playwright/MCP installations are out of scope.

Browser access is not guaranteed to reveal old invitation text or complete threads. Save actual coverage and use an export or a specific manual extract for unresolved gaps. Keep authentication and restriction stopping rules in [collection guidance](linkedin.md).

## Setup: arrange access

1. Reuse an existing archive or pending request. Otherwise explain which categories are relevant and guide the user to Settings & Privacy → Data Privacy → Download your data. Select the relevant categories where offered. If a larger archive is needed, explain why; retain only relevant categories in the workspace.
2. Use the built-in-browser preference in [connection guidance](connections.md). Perform available navigation yourself; let the user handle authentication and any request/download steps the agent cannot perform. Do not ask them to copy individual invitations or assemble a sample while an export is practical.
3. Verify a small browser read, available export selections or readability of a supplied archive as appropriate. Save the route, any requested categories, request status, file location when available and next action in the source's coverage/next_action fields. Use awaiting_export only when waiting is the only usable route; if the browser is usable, mark ready or partial based on its verified coverage and record the pending archive separately in those notes.
4. Continue other selected-source setup while an archive is pending. Collection, after the user proceeds, handles filtering, coverage checks and evidence capture; setup does not populate the full sample.

## Sales Navigator boundary

LinkedIn and Sales Navigator have separate inbox surfaces; see [Sales Navigator Inbox](https://www.linkedin.com/help/sales-navigator/answer/a110660). Do not infer that an ordinary LinkedIn export covers Sales Navigator InMail. If selected, save it as a separate source and verify a relevant known conversation independently during collection. Do not claim either inclusion or exclusion of all Sales Navigator messages without inspecting the actual archive.
