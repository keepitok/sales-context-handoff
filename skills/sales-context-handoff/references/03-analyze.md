# 03. Analyze

Adapted on 2026-11-20 from the upstream sources identified in [NOTICE.md](../NOTICE.md).

Interpret the collected sales evidence into supported findings and open questions for the saved recipient and purpose. Draft reports from available evidence before asking clarification questions about the findings.

## Read the workspace

Read `working/progress.json`, tables, relevant extracts and existing draft reports. Use the Reports and citations section and validation guidance in `working/data-guide.md`; consult record definitions only when needed. If the workspace is missing, direct the user to the setup stage. If no evidence has been collected, direct them to the collection stage. If collection is partial, use what exists and state its limits. Reuse the recorded scope and coverage; do not reconnect sources, repeat sampling or initiate new collection or enrichment. Preserve user corrections when updating drafts.

Use [the report guide](report-guide.md) for output structure. Read [win/loss interpretation](evidence/win-loss.md), [buyer roles](evidence/buyers.md), [lightweight hypotheses](evidence/hypotheses.md) and [the deal walkthrough](evidence/deal-walkthrough.md) for the corresponding sections.

## Evidence rules

- Do not turn an aspiration into a customer fact.
- Keep contradictory evidence visible. Repetition does not verify an explanation.
- Treat frameworks as optional language, not evidence.
- Label unsupported process definitions and proposed targeting criteria as hypotheses.
- Do not invent customer attributes, outcomes, stakeholders, scoring weights, thresholds, tiers or market sizes.

## Draft the findings

Write four concise reports in `working/reports/`: sales-context, findings, outreach-examples and gaps. Keep the structured tables alongside them.

Use the recipient guidance in the report guide to choose the emphasis. A new sales hire needs usable business and sales-process context; a GTM engineer needs patterns and gaps that inform design decisions. For another role, follow its saved needs. Keep drafts in working. If the recipient changed, revise the reports' emphasis using existing evidence and flag any newly relevant gaps.

Capture what is sold, the buyer's problem, sales motion and stages, existing qualification rules, constraints and recorded buying roles. Distinguish current practice from a recommended change.

Explain supported patterns with counts, counterexamples and limits. Include one best-documented deal walkthrough in findings. Include lightweight ICP/signal hypotheses when relevant to the recipient's needs and supported by collected evidence; name missing inputs needed to evaluate them. Preserve existing scoring rules as current practice without endorsing or recalibrating them.

Outreach examples must show exact source wording and the observed response/outcome. Do not rewrite examples into improved copy or imply the initial outreach caused a later sale.

Omit empty narrative sections. For a missing deliverable, write one clear sentence explaining which evidence was unavailable. Keep important questions and enrichment requests together in gaps.

## Finish

Run the workspace helper's validate command and resolve structural errors. If a compatible runtime is unavailable, use the guide to check identifiers and references and state that the helper was not run. Manually check that each material finding's cited extract supports the claim; the script cannot judge this.

Save the milestone state. Summarize the strongest findings, limitations and only material clarification questions. Do not block the handoff because evidence is incomplete.

Next prompt: "Help me review and redact my sales-context handoff, then package the results I choose to share."
