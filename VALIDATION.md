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
- Partial LinkedIn coverage, inaccessible Sales Navigator and preserved restart state. These test recorded coverage and resumption invariants, not live browser automation.
- Duplicate source-key detection, evidence references, wrong citation targets and sample limits.
- Exact Unicode/multiline message preservation, redaction of shareable copies with unchanged originals, and exclusion of unselected/private files.
- Rejection of unreviewed or changed files, incomplete allowlists, escaping paths, unrelated extract references and overwriting an existing archive.

The skill entry point is checked with the skill-creator validator. Portability checks copy the skill and starter workspace into a temporary folder, follow links from the index through numbered stages and supporting references, verify metadata and licenses, and run the copied helper in a new process. The skill baseline was copied from pinned upstream checkouts before adaptation.

The common index loads one stage at a time: `01-setup.md`, `02-collect.md`, `03-analyze.md` and `04-handoff.md` under `references/`. Source and evidence references are loaded only when needed by the current stage. The progress keys remain `setup`, `collect`, `analyze` and `handoff`.

The helper checks structure, counts, references and reviewed bytes. It does not determine whether an agent chose a representative sample, whether an inference follows from a quotation, or whether every sensitive fact has been redacted. Those require a real workflow review.

## Live app status

| Capability | Status |
|---|---|
| Single skill folder, numbered stage references and OpenAI metadata | Validated on disk |
| New-process workspace/helper access | Tested with synthetic saved files |
| Recipient-specific analysis for a new sales hire, GTM engineer or another role | Instructions reviewed; live agent behavior not yet tested |
| Skill installation, discovery and natural-language routing in a fresh ChatGPT Work project | Not yet tested |
| Claude Cowork installation from repository contents, discovery and folder persistence | Not yet tested in a signed-in Cowork session |
| Live CRM/email/transcript connectors | Not exercised |
| LinkedIn/Sales Navigator browser extraction | Unverified until tested in an authorized account |

No customer accounts were accessed or private conversations collected during implementation.

## First run in your workspace

1. Install `sales-context-handoff` in the chosen app. Confirm it is available; use setup to verify a write/read in the selected folder. Check that it asks only for missing website/offer scope and recipient needs. Confirm that the agent loads only setup and its relevant references, then pauses before collection. Check the same stage routing and pause on subsequent prompts.
2. Start with a small supplied spreadsheet. Run collection, open the tables/extracts and confirm exact values and locators. Continue in a new conversation and verify no duplicate records.
3. Add one authorized relevant email/transcript source if available. Check linkage to the same opportunity and attribution of buyer versus seller statements.
4. If LinkedIn is selected, compare one exported thread with its visible original. Independently check Sales Navigator. Test a missing thread through the available browser; verify exact text and partial-coverage handling. Record success only for capabilities actually demonstrated.
5. Run analysis and inspect every material finding against its extract. Try the same evidence for a new sales hire and a GTM engineer: check that emphasis changes while facts remain unchanged and no evidence is recollected unnecessarily. Also test a custom recipient and resuming an older progress file without recipient fields. Confirm no enrichment, invented scoring or causal claim about an outreach message.
6. Review a concrete handoff, request one redaction, package it, and inspect the archive. Confirm originals remain private and the redaction appears everywhere needed.

Keep any remaining failures in your coverage/gap record; do not label untested integrations as verified.
