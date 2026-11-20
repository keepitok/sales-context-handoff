# Selected-source setup

Use these routes only for sources the user selected. Prefer available connectors over browser interaction when their read capability is sufficient. Avoid a universal integration checklist.

## Choose the practical access route

Aim for usable evidence with the least manual effort from the user. Inspect available tools and connection options before requesting exports or copied conversations. A source that is not connected yet calls for setup guidance, not an immediate manual collection assignment.

- Reuse selected files and working connections. With a suitable connector, the agent searches and extracts relevant records during collection.
- For an unconnected source, discover the supported connection option, explain the user-only authorization steps and verify a small relevant read afterward.
- If a connector is unavailable or unsuitable, compare a native export with a bounded browser read. Choose based on coverage, exact wording, setup effort, waiting time and user preference. For LinkedIn, use the route guidance below.
- Suggest manual extracts when automated access is blocked, the user prefers not to connect, or a small one-off extract is more practical than setting up access. Briefly explain why and request only the specific missing material. Manual copying is not the default merely because setup has not happened yet.

For a native export, guide the user only through steps the agent cannot perform; the agent handles filtering and extraction from the supplied file. Optional business documents can be located in a selected connected folder as well as supplied directly.

| Source | Small access check | Fallback |
|---|---|---|
| CRM | One opportunity in scope; inspect actual outcome/stage definitions | Native CSV/XLSX opportunity export with account and contact identifiers |
| Spreadsheets | Read sheets, headers and a few relevant rows | User-provided CSV; preserve sheet/row locators |
| Email | One scoped search by known account/person or deal reference | Selected thread export, EML, copied text or PDF |
| Transcripts | One existing call transcript within the selected business scope | Existing text, document or meeting notes; distinguish notes from verbatim transcript |
| LinkedIn | One scoped browser read or readable export; see [route and export guidance](linkedin-export.md) | Switch between browser and export according to coverage and delay; manual extracts when practical |
| Sales Navigator | Check its own inbox and known thread independently | Relevant browser read or manual extract |
| Website and business documents | One selected page or file; verify readable content and available date/version | Selected file upload, document export, pasted excerpt or user's short explanation, explicitly attributed |

Record the selected route and why any manual input is needed in source coverage/next_action. Record a coverage gap only when evidence remains unavailable. Do not require the user to adopt a different service. Never ask the user to paste credentials into chat or files.

## LinkedIn access

When LinkedIn is selected, read [LinkedIn routes, export capabilities and setup](linkedin-export.md). It explains when to browse or export, documented waiting times, categories for invitation text versus private notes, and what to verify and save. Collection uses [LinkedIn collection guidance](linkedin.md) for either route.

## Workspace and source access

When browser access is needed, prefer the AI app's built-in browser. Discover the browser surfaces the session actually exposes and check that route first. If sign-in is needed, let the user sign in there, then continue the scoped read. An existing Chrome session alone is not a reason to choose Chrome over the built-in browser.

Use an external browser such as Chrome when the user explicitly prefers it, or when the built-in route is unavailable or cannot perform the required read. Explain the observed limitation before proposing that fallback; do not default to asking the user to open or control Chrome. Save any expressed browser preference with the source's access notes so it persists on resume. This browser preference does not replace suitable connectors or a ready export that covers the scope.

ChatGPT Work: verify write/read access in the selected workspace. Enable connectors or browser access only as needed for the selected sources.

Claude Cowork: verify file access to the selected folder and enable missing file/code capabilities if needed. Verify that a task-written file can be read back from that folder. Later milestones check access to saved progress when resuming.

Current Cowork sessions can run in the cloud and reach local folders through the open desktop app. A connected project reference may not be writable in every mode; test actual access. If only session files are writable, explicitly arrange download into the user folder and reattachment on resume, or resolve folder access before calling setup complete.

Browser extraction is unverified until a relevant signed-in conversation has been read and its capture checked. Availability may depend on account settings. No authentication bypass, hidden API extraction or delay scheme intended to avoid restrictions.

## Official references

Checked 2026-11-20; refresh app-specific steps if the UI differs.
- [ChatGPT browser](https://learn.chatgpt.com/docs/browser)
- [Cowork local access and execution](https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile)
- [Cowork browser](https://support.claude.com/en/articles/16607400-use-the-built-in-browser-in-claude-cowork)
- [LinkedIn data download](https://www.linkedin.com/help/sales-navigator/answer/a1339364)
