# Sales Context Handoff

**Turn your sales history into a clear, evidence-backed handoff.**

Sales Context Handoff helps sales leaders prepare a reviewed handoff for a new sales hire, a GTM engineer or another recipient who needs to understand the business's sales context.

Use the data you already have: CRM records or spreadsheets, email, existing call transcripts, LinkedIn messages and Sales Navigator conversations. No particular CRM or enrichment subscription is required.

## Start here

Start a new project in **ChatGPT Work** (desktop app) or **Claude Cowork**, then paste this prompt:

```text
Read the README at https://github.com/keepitok/sales-context-handoff, install sales-context-handoff in this project, and tell me the next step.
```

Your assistant should follow the [installation instructions](INSTALL.md). You do not need to work through them yourself.

## The workflow

One skill guides you through four stages at your own pace. After installation, it starts with the setup questions. Between later stages, it explains the next step and waits for you to proceed. Each stage saves its results so you can review them or resume in a new conversation.

Setup asks for your business website, the offers in scope and where relevant evidence lives. It helps you connect selected sources so the assistant can collect evidence with as little manual work from you as practical.

| Stage | What happens |
| --- | --- |
| **1. Set up** | Confirm your business and offers, choose data sources and verify access. |
| **2. Collect** | Gather deal records and exact outreach conversations, refining offer and ICP drafts as evidence accumulates. |
| **3. Analyze** | Compare outcomes, refine your sales context and review supported findings and gaps. |
| **4. Review and hand off** | Choose what to share, review corrections and redactions, and package the selected results. |

The default starting point is the last 12 months, aiming for 10 wins and 10 losses where available. You can expand the sample to 50 deals and include up to 10 additional outreach examples that led to a reply or meeting. Missing history stays visible as a gap.

For noncommercial outreach, such as event invitations, setup establishes what success means. Collection compares confirmed positive and negative cases where available, keeping replies, registrations, attendance and unknown outcomes distinct.

## What you get

Collection starts with your website and offer material, saving separate offer and ICP drafts. As records and conversations are collected, those drafts are refined with supporting evidence and counterexamples. Analyze reconciles the working definitions and prepares these files:

| File | What it contains |
| --- | --- |
| `working/reports/offer.md` | Evidence-backed offer description, refined throughout collection and analysis: problem, promise, delivery, terms and observed buyer value. |
| `working/reports/icp.md` | Evidence-backed working ICP with customer fit, buyer roles and available evidence of customer value beyond the sale, plus examples, counterexamples and unknowns. For noncommercial outreach, an audience profile. |
| `working/reports/sales-context.md` | Your sales process, qualification rules, operational constraints and any business concerns and explanations to examine. |
| `working/reports/customer-context.md` | Customers' and prospects' situations, needs, workflows, alternatives and constraints, plus signals and triggers that may reveal fit or timing. |
| `working/reports/outcome-analysis.md` | Outcome comparisons, objections and counterexamples, considering fit, sales follow-up and timing where evidence permits. |
| `working/reports/examples.md` | One documented journey plus exact outreach sequences and replies, with identifiable accounts/contacts and verified outcomes. |
| `working/reports/gaps.md` | Missing information, contradictions and the next inputs needed. |
| `working/extracts/*.md` | Source excerpts and exact conversations supporting the reports and tables. |

Supporting CSV evidence in `working/` preserves accounts, contacts, deals, outreach, outcomes and source references behind the reports.

`working/progress.json` saves scope, coverage and review status so you can resume. Reports remain preliminary where evidence is insufficient. The later handoff stage creates selected, redacted copies, a reading-order index and a reviewed ZIP.

The workflow explains existing evidence; it does not run enrichment, create campaigns or implement a GTM engine. A reply, a booked meeting and an outreach sequence associated with a won deal remain distinct outcomes; association is not treated as proof of causation.

## Your data and review

Your workspace separates original captures (`raw/`), analysis and source mappings (`working/`), and selected shareable copies (`handoff/`). Review and redaction apply to the handoff copies. The ZIP includes only selected, reviewed files; the workflow does not send it automatically.

Email addresses can be kept privately for matching records and are removed from the handoff. Names, company websites and LinkedIn profiles remain unless you choose to redact them.

Intermediate tables, extracts and drafts are saved directly in your local project folder. The assistant points you to those files for review; you do not need to download or reattach them between stages.

The workflow checks for duplicate records and missing evidence links. You review the findings before moving to packaging. If important outcomes, comparisons or audience attributes are missing, it proposes targeted collection or asks whether you want a limited handoff with those gaps stated. You then choose what to include or redact.

Your data may be shared with your AI provider (OpenAI or Anthropic). Check your AI app's settings for your current privacy options.

## Status

The workflow has been tested with synthetic sales data. Installation in the target apps, live source connections and LinkedIn/Sales Navigator browser collection still need verification. See [validation notes](VALIDATION.md) for details.

## License and acknowledgments

Original contributions are licensed under [MIT](LICENSE). Third-party material remains subject to its respective licenses; see the notices and license files included with the skill.

Adapted from selected skills by [Zarif](https://github.com/zarif3624/gtm-skills), [Anthropic](https://github.com/anthropics/knowledge-work-plugins) and [Checkpoint GTM](https://github.com/noahatcheckpoint/gtm-skills). Their license texts and attribution notices are preserved alongside the adapted material.
