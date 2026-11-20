# Selected-source setup

Use these routes only for sources the user selected. Prefer available connectors over browser interaction when their read capability is sufficient. Avoid a universal integration checklist.

| Source | Small access check | Fallback |
|---|---|---|
| CRM | One opportunity in scope; inspect actual outcome/stage definitions | Native CSV/XLSX opportunity export with account and contact identifiers |
| Spreadsheets | Read sheets, headers and a few relevant rows | User-provided CSV; preserve sheet/row locators |
| Email | One scoped search by known account/person or deal reference | Selected thread export, EML, copied text or PDF |
| Transcripts | One existing call transcript within the selected business scope | Existing text, document or meeting notes; distinguish notes from verbatim transcript |
| LinkedIn | Export availability and request/download status | User-supplied thread text; browser for relevant gaps during collection |
| Sales Navigator | Check its own inbox and known thread independently | Relevant browser read or manual extract |
| Website and business documents | One selected page or file; verify readable content and available date/version | Selected file upload, document export, pasted excerpt or user's short explanation, explicitly attributed |

Use the sources the user chooses. If a selected source is not connected, guide the user through the available connection setup and verify access with a small relevant read. If connection is unavailable or the user prefers not to connect, offer an export or manual extract. Record a coverage gap only when the evidence remains unavailable. Do not require the user to adopt a different service. Never ask the user to paste credentials into chat or files.

## LinkedIn export

Guide the user to Settings & Privacy → Data Privacy → Download your data, select messages where offered and request the archive. Let the user handle authentication and download. If an export is already supplied or requested, reuse it or its saved status. Continue setting up other selected sources while it is pending.

Record the supplied export location or pending request in progress. Collection handles filtering, source captures and exact extracts; do not populate evidence tables during setup.

A personal LinkedIn export does not establish complete Sales Navigator coverage. Record the two as separate sources; collection compares relevant threads against the export.

## Workspace and source access

ChatGPT Work: verify write/read access in the selected workspace. Enable connectors or browser access only as needed for the selected sources. Use the browser tool the session actually exposes.

Claude Cowork: verify file access to the selected folder and enable missing file/code capabilities if needed. Verify that a task-written file can be read back from that folder. Later milestones check access to saved progress when resuming. The built-in browser or Claude in Chrome can be used where available for selected sources.

Current Cowork sessions can run in the cloud and reach local folders through the open desktop app. A connected project reference may not be writable in every mode; test actual access. If only session files are writable, explicitly arrange download into the user folder and reattachment on resume, or resolve folder access before calling setup complete.

Browser extraction is unverified until a relevant signed-in conversation has been read and its capture checked. Availability may depend on account settings. No authentication bypass, hidden API extraction or delay scheme intended to avoid restrictions.

## Official references

Checked 2026-11-20; refresh app-specific steps if the UI differs.
- [ChatGPT browser](https://learn.chatgpt.com/docs/browser)
- [Cowork local access and execution](https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile)
- [Cowork browser](https://support.claude.com/en/articles/16607400-use-the-built-in-browser-in-claude-cowork)
- [LinkedIn data download](https://www.linkedin.com/help/sales-navigator/answer/a1339364)
