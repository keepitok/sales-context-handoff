# 03. Analyze

Adapted on 2026-11-20 from the upstream sources identified in [NOTICE.md](../NOTICE.md).

Interpret the collected sales evidence into supported findings and open questions for handoff. Draft reports from available evidence before asking clarification questions about the findings.

## Read the workspace

Read `working/progress.json`, tables, relevant extracts and existing draft reports. Use the Reports and citations section and validation guidance in `working/data-guide.md`; consult record definitions only when needed. If the workspace is missing, direct the user to the setup stage. If no evidence has been collected, direct them to the collection stage. If collection is partial, use what exists and state its limits. Reuse the recorded scope and coverage; do not reconnect sources, repeat sampling or initiate new collection or enrichment. Preserve user corrections when updating drafts.

Use [the report guide](report-guide.md) for output structure. Read [win/loss interpretation](evidence/win-loss.md), [buyer roles](evidence/buyers.md), [working ICP and signals](evidence/hypotheses.md) and [the deal walkthrough](evidence/deal-walkthrough.md) for the corresponding sections.

Assess [outcome coverage and readiness](evidence/coverage.md). With partial evidence, label the reports preliminary and state which comparisons cannot be supported. Interpret noncommercial outcomes using the saved definitions rather than treating replies or registrations as won deals.

## Evidence rules

- Do not turn an aspiration into a customer fact.
- Keep contradictory evidence visible. Repetition does not verify an explanation.
- Treat frameworks as optional language, not evidence.
- Label unsupported process definitions and proposed targeting criteria as hypotheses.
- Do not invent customer attributes, outcomes, stakeholders, scoring weights, thresholds, tiers or market sizes.

## Draft the findings

Produce the seven reports listed in [the report guide](report-guide.md) under `working/reports/`. Include buyer roles within icp, signals/triggers within customer-context, and the documented journey plus outreach sequences within examples. Refine the existing offer and ICP drafts using [their lifecycle guidance](evidence/offer-and-icp.md); if missing, build them from already collected context and evidence, noting any missing initial material. Keep the structured tables alongside them.

Use the report guide to cover business context, observed patterns, conversation examples and gaps. Keep drafts in working.

Reconcile the offer and explicit working ICP/audience definition against the collected sample. Preserve the initial source-based understanding, explain evidence-backed revisions and retain uncertainties. Include observed buying roles, influence and decision involvement in icp, distinguishing job titles from demonstrated roles. In sales-context, describe the seller's sales motion and stages, existing qualification rules and operational constraints. Link to the offer and ICP files instead of repeating their full contents. Distinguish current practice from a recommended change.

Explain supported patterns with counts, counterexamples and limits in outcome-analysis. Put one best-documented deal or noncommercial journey walkthrough alongside selected outreach sequences in examples. Assess ICP/audience-fit evidence explicitly; include hypotheses only when supported and name missing inputs needed to evaluate them. Preserve existing scoring rules as current practice without endorsing or recalibrating them.

Use [customer context, signals and triggers guidance](evidence/customer-context-and-signals.md) for the corresponding sections in customer-context. Distinguish observed needs and situations from candidate predictors. For signals/triggers, preserve chronology, whether each fact was available before outreach or only later/private, supporting and contradictory cases, and the evidence needed to test its future usefulness.

Outreach examples must identify the contact/account and show observed profile/record links, exact source wording, conversation evidence and separately verified response/conversion outcomes. Put these links beside the named example, not only inside a distant extract. If a profile link is unavailable, say so and retain the exact source-record link. Do not rewrite examples into improved copy or imply the initial outreach caused a later sale.

Omit empty narrative sections. For a missing deliverable, write one clear sentence explaining which evidence was unavailable. Keep important questions and enrichment requests together in gaps.

## Finish

Run the workspace helper's validate command and resolve structural errors. If a compatible runtime is unavailable, use the guide to check identifiers and references and state that the helper was not run. Manually check that each material finding's cited extract supports the claim; the script cannot judge this.

Save draft reports with analysis partial and findings_review pending. Present the current offer and working ICP/audience definition, strongest findings, outcome comparison and material limitations for substantive review. Saving the reports is not analysis completion. If readiness is needs_collection, propose targeted additional collection or ask whether the user accepts a limited handoff; do not present packaging as the default next step.

After the user reviews the findings and readiness is ready or accepted_limited, record their decision and mark analysis complete. Only then offer the separate review/share stage: selecting contents, redacting and packaging. This may be combined with an explicit user request to proceed after review, without a redundant confirmation. Keep the later review of exact shareable contents intact.
