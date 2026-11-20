# 04. Handoff

Prepare a portable copy of the results the user chooses to share, apply corrections and redactions, and package the reviewed contents while preserving private originals.

Read `working/progress.json`, the handoff and helper guidance in `working/data-guide.md`, and [review guidance](review.md).

Check [outcome coverage and readiness](evidence/coverage.md) before preparing the package. Require readiness ready or accepted_limited and a recorded findings review. If unresolved, return to the findings/coverage discussion instead of offering packaging. An explicitly requested evidence-only handoff still requires the user to review and accept its stated limits.

Use the existing evidence and draft reports. If reports are missing, offer the analysis milestone or an evidence-only handoff, making omissions clear. If no evidence exists, direct the user to collection, or setup if the workspace is missing. Do not repeat source setup, collection or analysis here. On resume, preserve reviewed copies and redactions; apply only requested corrections and relevant source updates, then review changed contents again.

## Prepare a concrete review copy

Copy selected draft reports, filtered CSV tables and relevant extracts into `handoff/`. Preserve the parallel reports/extracts layout so relative citations work. Never copy `raw/`, the progress manifest, credentials, the helper or a full user folder into the handoff.

Create `handoff/README.md` titled "Sales context handoff: [business]," with a short reading order, offer/date scope, coverage limitations and a list of included files. Start with offer and ICP, then customer context, sales context, outcome analysis and examples, followed by gaps and the supporting tables/extracts. Adjust to the selected contents and keep links between included reports intact. Explain that original source links may require account access; the included extracts should still allow evidence review.

Retain stable identifiers and account/contact/outcome links. Include the six standard tables, with headers only for those containing no selected records. If an example is omitted, prune unused evidence and unneeded personal data from the shareable tables. Preserve the full mapping in working files. Keep identifiable example links unless the user requests their redaction; check redactions across reports, tables and extracts.

Remove email addresses from the proposed handoff before review. Keep the contacts.csv email column empty; redact addresses in excerpts, reports, source keys, locators, links and filenames with visible markers where appropriate. Preserve names, company websites and LinkedIn profiles unless separately excluded. Keep original addresses in private working/raw evidence for matching; do not remove the email conversations themselves.

Show the actual proposed contents and sensitive excerpts needing attention. Ask for corrections, exclusions or redactions, unless the user has already supplied explicit review instructions sufficient for these exact contents. Do not treat silence or a generic earlier request to package as completed review.

## Apply review

Apply corrections and redactions only to handoff copies, with visible markers such as [REDACTED: person name]. Keep exact wording around redactions and omissions. Recheck the same details in CSV cells, filenames, source locators, excerpts and report prose. For a factual correction, preserve its attribution to the user's clarification in working evidence; do not silently change raw sources.

Run `python tools/context_tools.py validate . --area handoff`.
Run `python tools/context_tools.py manifest .` to obtain a draft list of paths and hashes. Save it as `handoff/review.json`, recording the user's actual review date and setting status to reviewed only after the corresponding review has happened. If contents change afterward, repeat review for the changes and regenerate hashes.

## Package

Run `python tools/context_tools.py package . <output.zip>`. The helper validates the allowlist and hashes and excludes raw/working material. Never replace this with a recursive archive of the workspace.

If a compatible Python interpreter is unavailable locally, check whether the app's code execution provides Python 3.10+ and can read the reviewed files and save the resulting ZIP back to the local project workspace. Verify the saved ZIP there. If neither environment can do this, leave the reviewed folder ready and report that ZIP packaging is incomplete; do not substitute a session-only download.

Verify the ZIP member list and report its local path. Save handoff completion in progress. The user shares the package themselves; do not email, upload or publish it.
