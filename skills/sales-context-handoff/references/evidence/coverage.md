# Outcome coverage and readiness

Use this review after collection and before presenting analysis as complete. File creation and structural validation do not establish evidence sufficiency. The agent assesses coverage; the helper only checks recorded states and references.

## Define the comparison

Use the scope and outcome definitions saved during setup. Commercial opportunities retain won/lost and their original stages. For noncommercial outreach, use the actual conversion journey rather than inventing deals. For example, an event can have replies, registrations, attendance, explicit declines, cancellations and verified no-shows. Registration is not attendance, and no reply or an unsuccessful name search leaves conversion unknown. A no-show requires a matched registration and sufficiently complete attendance evidence after the event.

Keep engagement in outreach.csv and separately sourced conversion/status observations in outcomes.csv. Each observation links an identifiable contact or account to a specific event/campaign/offer instance through scope_key. Preserve multiple stages and their dates instead of overwriting a registration with attendance. Count distinct people/cases at each stage, not outcome rows. Do not add intermediate and final stages as if they were different successes.

## Assess the handoff

Review the evidence for each question and record a concise summary, counts and consequential gaps:

| Area | What should be available |
| --- | --- |
| Context | Offer, problem, intended audience, motion, existing qualification rules and explicit outcome definitions |
| Identity | Named accounts or contacts, observed profile/record links and stable IDs; missing links flagged |
| Outcome comparison | Confirmed positive and negative cases where available, unknowns kept separate, reasons and source coverage stated |
| Conversation evidence | Exact openings, follow-ups, replies, relevant objections and observed outcomes, with omissions visible |
| ICP/audience fit | Existing targeting definitions distinguished from observed attributes and tentative hypotheses, with named examples and counterexamples |
| Traceability | Every material finding resolves to evidence; the complete sample lives in standard tables, including people with no known company |

A missing optional attribute is not automatically a material gap. Missing final outcomes for most cases, an absent comparison group, unresolved identity matches or insufficient attributes to examine fit usually limit the intended analysis. Explain which conclusion cannot yet be supported. Do not demand a fixed success rate or invent a calibrated score.

## Next action

- Set readiness.status to needs_collection when material gaps remain. List them in readiness.material_gaps and state the smallest useful next collection step. Offer to return to collection or proceed with explicitly limited preliminary findings; do not silently resume collection.
- Set ready only when the agreed scope has sufficient evidence for the intended comparisons, with no unresolved material gaps. This does not mean a validated ICP or complete source population.
- If the user explicitly chooses a limited handoff after seeing the gaps, set accepted_limited and record their decision in readiness.user_decision. Keep the limitations in the reports and index. A generic earlier instruction to prepare a handoff is not acceptance of newly discovered gaps.
- Keep actual milestone progress honest: a finished browser batch or draft report can still leave collection/analysis partial. Never mark a stage complete merely because its files exist.

Present the draft findings for review before proposing packaging. Save findings_review.status as reviewed and its user_decision only after the user has reviewed the substance or explicitly accepted its stated limits. If evidence or conclusions materially change, reset that review to pending and reassess readiness. Review of findings is distinct from the later choice of shareable files and redactions.
