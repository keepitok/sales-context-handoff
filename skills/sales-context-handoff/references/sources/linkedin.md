# LinkedIn and Sales Navigator collection

## Export first

Use [the documented export categories](linkedin-export.md) to interpret the archive. Invitation messages and private connection notes are different evidence; do not treat private notes as messages sent to a prospect.

Use the export location or pending request saved during setup. Do not request another export if the existing one covers the scope. While an export is pending, collect from other ready sources. Inspect actual filenames/columns rather than assuming an export schema. Filter to selected companies, people and the approved period. Preserve relevant original captures in raw without copying unrelated archive categories into the workspace. Preserve participant identifiers, dates and thread identifiers when supplied.

Check each requested category separately: present/readable, relevant date coverage, available text and participant identifiers, and any truncation or missing fields. Check a known relevant invitation and follow-up thread when available. A Messages file alone does not establish invitation coverage. An absent file means that category is unavailable in this archive, not proof that no such activity happened. Record consequential gaps and distinguish an unqueried source from a failed or incomplete read.

Match invitation text to later messages using profile identifiers and supporting dates/context; names alone are insufficient. Keep uncertain matches separate and deduplicate overlapping text without losing its source references. Preserve exact invitation wording as the opening message when linkage is supported. A sent invitation or connection acceptance does not establish a reply, meeting, registration, attendance or won deal; those need their own evidence. Keep private notes attributed as seller context.

If Sales Navigator is selected, independently check a known Sales Navigator thread. Record the result for each source; the personal export does not establish complete Sales Navigator coverage.

## Browser gaps

Use browser access only for missing relevant threads, following the built-in-browser preference and fallback guidance in [connection guidance](connections.md):
1. Reuse the selected account's signed-in session. If it is unavailable, save the access issue for the user to resolve before continuing this source.
2. Open the correct inbox and search a known person/company or selected conversation.
3. Read and expand enough messages to capture the relevant sequence. Wait for the UI to load; do not use stealth, randomized delay or restriction-evasion schemes.
4. Save exact visible content with source locator, dates, capture method and coverage.
5. Save the completed source key and next action after each thread. Reuse existing evidence IDs when resuming.

Do not claim that an unloaded beginning or truncated message was read. Deduplicate overlapping export/browser captures by source identifiers and message dates/text, retaining source provenance.

If login expires, a challenge or restriction appears, or the tool cannot read the content, save progress, stop this source and offer manual copied text/export. Continue independently available sources. Never send messages, mark conversations resolved, invite people or alter account settings.

## Coverage

Track LinkedIn and Sales Navigator separately as ready, partial, awaiting_export, inaccessible or skipped. Include a short reason such as "opening messages unavailable" or "Sales Navigator export coverage not verified." Opening a thread can affect the site's read state; use existing exports where that matters to the user.

The built-in browser route remains unverified until tested in the user's account.

References checked 2026-11-20:
- [Message export](https://www.linkedin.com/help/sales-navigator/answer/a1339364)
- [Separate LinkedIn and Sales Navigator inboxes](https://www.linkedin.com/help/sales-navigator/answer/a107018/compose-an-inmail-message-in-sales-navigator?lang=en)
