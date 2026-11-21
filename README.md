# Sales Context Handoff

**Turn your sales history into a clear, evidence-backed handoff.**

Sales Context Handoff helps sales leaders document their business's sales context. Prepare a reviewed handoff for a new sales hire, a GTM engineer or another recipient.

Use the data you already have: CRM records, spreadsheets, email, call transcripts and LinkedIn conversations.

> **Privacy:** Collected files stay in your project workspace. You choose what to share at handoff. Your AI provider may process their contents.

## Start here

Start a new project in **ChatGPT Work** (desktop app) or **Claude Cowork**. Then paste this prompt:

```text
Read the README at https://github.com/keepitok/sales-context-handoff.
Install the sales-context-handoff skill in this project. Tell me the next step.
```

Your AI assistant should follow the [installation instructions](INSTALL.md).

## The workflow

| Stage | What happens |
| --- | --- |
| **1. Set up** | Confirm your business and offers. Choose data sources and verify access. |
| **2. Collect** | Gather deal records and exact outreach conversations. Refine offer and ICP drafts as evidence accumulates. |
| **3. Analyze** | Compare outcomes and refine your sales context. Review supported findings and gaps. |
| **4. Review and hand off** | Choose what to share. Review corrections and redactions. Package the selected results. |

One skill guides you through four stages at your own pace. Setup questions start after installation. Before each later stage, the assistant waits for you to proceed. Saved results let you review or resume in a new conversation.

Setup asks about your business and data sources together. You can name best-fit wins, poor-fit wins and lost accounts to guide collection. The assistant helps connect those sources to reduce manual collection.

See what your recent wins, losses and successful outreach have in common. The assistant usually starts with the last 12 months. You can adjust the period and sample size.

You can also use it for event invitations and other outreach. See who replied, registered or attended, based on the available evidence. Unconfirmed outcomes remain unknown.

## What you get

By the end of analysis, you have these files:

| File | What it contains |
| --- | --- |
| `working/reports/offer.md` | Your offer's problem, promise, delivery, terms and observed buyer value. |
| `working/reports/icp.md` | Customer fit, buyer roles and available evidence of value beyond the sale. Includes examples, counterexamples and unknowns. For noncommercial outreach, an audience profile. |
| `working/reports/sales-context.md` | Sales process, qualification rules and constraints. Business concerns and possible explanations to examine. |
| `working/reports/customer-context.md` | Customer and prospect situations, needs, workflows, alternatives and constraints. Signals and triggers that may reveal fit or timing. |
| `working/reports/outcome-analysis.md` | Outcome comparisons, objections and counterexamples. Considers fit, sales follow-up and timing where evidence permits. |
| `working/reports/examples.md` | One documented journey and exact outreach sequences. Includes identifiable accounts or contacts, replies and verified outcomes. |
| `working/reports/gaps.md` | Missing information, contradictions and next inputs. |
| `working/extracts/*.md` | Source excerpts and exact conversations supporting the reports. |

Supporting CSV files in `working/` hold accounts, contacts, deals, outreach, outcomes and source references.

`working/progress.json` saves scope, coverage and review status. Reports remain preliminary where evidence is insufficient.

The workflow explains existing evidence. It does not enrich companies, create campaigns or implement a GTM engine. Replies, meetings and associated won deals remain distinct outcomes. A message associated with a win did not necessarily cause it.

## Your data and review

Your workspace keeps originals in `raw/` and analysis in `working/`. Selected shareable copies go in `handoff/`. Review and redaction apply to those copies. The ZIP contains only selected, reviewed files and a reading-order index. Nothing is sent automatically.

Email addresses may be kept privately to match records. They are removed from the handoff. Names, company websites and LinkedIn profiles remain unless you redact them.

The assistant links to your saved files for review. You do not need to download or reattach them between stages.

The workflow checks for duplicates and missing evidence links. You review findings before packaging. Important gaps lead to targeted collection or your acceptance of a limited handoff.

Check your AI app's settings for its current privacy options.

## Status

The workflow has been tested with synthetic sales data. App installation and live source connections still need verification. LinkedIn and Sales Navigator browser collection also needs verification. See [validation notes](VALIDATION.md).

## License and acknowledgments

Original contributions use the [MIT license](LICENSE). Third-party material keeps its own licenses. Notices and license files are included with the skill.

Adapted from skills by [Zarif](https://github.com/zarif3624/gtm-skills), [Anthropic](https://github.com/anthropics/knowledge-work-plugins) and [Checkpoint GTM](https://github.com/noahatcheckpoint/gtm-skills). Their license texts and attribution notices are preserved.
