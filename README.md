# Sales Context Handoff

**Turn your sales history into a clear, evidence-backed handoff.**

Sales Context Handoff helps sales leaders prepare a reviewed handoff for a new sales hire, a GTM engineer or another recipient who needs to understand the business's sales context.

Use the data you already have: CRM records or spreadsheets, email, existing call transcripts, LinkedIn messages and Sales Navigator conversations. No particular CRM or enrichment subscription is required.

## Start here

Start a new project in **ChatGPT Work** (desktop app) or **Claude Cowork**, then paste this prompt:

```text
Install the sales-context-handoff skill from <PUBLIC_REPOSITORY_URL> and tell me the next step. If installation requires an action from me, guide me through it.
```

Replace `<PUBLIC_REPOSITORY_URL>` with this repository's public URL once published.

> **For agents:** Before installing, check that the user is in ChatGPT Work or Claude Cowork, in a dedicated project with skill support and persistent file access. Ask if the app or project is unclear. If needed, guide the user to the appropriate app and help them start a project, then ask them to paste the prompt there. Reuse an existing Sales Context Handoff project when resuming.

> After installation, load the skill, confirm it is installed and introduce setup: it confirms scope, connects selected sources and verifies access. Show the skill's short privacy note prominently in chat, then ask whether to begin and wait before setup questions or source access. An installation request mentioning a test scenario does not start setup. Do not ask the user to assemble a sample of threads or exports before source discovery. Installation checks should establish that the skill is available; repository development tests are not an end-user setup step.

## The workflow

One skill guides you through four stages at your own pace. It explains each next stage and waits for you to proceed. Each saves its results so you can review them or resume in a new conversation.

Use these prompts after installation:

| Stage | Prompt |
| --- | --- |
| **Set up** | Help me set up a sales-context handoff: confirm my business, offers and data sources. |
| **Collect** | Collect my deal evidence and successful outreach examples from my selected sources. |
| **Analyze** | Analyze my sales context and prepare findings for handoff. |
| **Review and hand off** | Help me review and redact my sales-context handoff, then package the results I choose to share. |

In ChatGPT Work, type `@` and select `sales-context-handoff`. The skill uses your request and saved progress to choose the current stage.

To resume, point the assistant to your workspace and say: “Resume my sales-context analysis from the saved progress.”

The default starting point is the last 12 months, aiming for 10 wins and 10 losses where available. You can expand the sample to 50 deals and include up to 10 additional outreach examples that led to a reply or meeting. Missing history stays visible as a gap.

For noncommercial outreach, such as event invitations, setup establishes what success means. Collection compares confirmed positive and negative cases where available, keeping replies, registrations, attendance and unknown outcomes distinct.

## What you get

Collection starts with your website and offer material, saving separate offer and ICP drafts. As records and conversations are collected, those drafts are refined with supporting evidence and counterexamples. Analyze reconciles the working definitions and prepares these files:

| File | What it contains |
| --- | --- |
| `working/reports/offer.md` | Initial offer description and evidence-backed refinements: problem, promise, delivery, terms and observed buyer value. |
| `working/reports/icp.md` | Initial intended audience and working ICP, with supported fit criteria, examples, counterexamples and unknowns. For noncommercial outreach, an audience profile. |
| `working/reports/sales-context.md` | Your sales process, qualification rules and operational constraints. |
| `working/reports/customer-context.md` | Customers' and prospects' goals, problems, workflows, alternatives and decision criteria. |
| `working/reports/outcome-analysis.md` | Outcome comparisons, patterns, objections and counterexamples. |
| `working/reports/buyer-roles.md` | Observed buyer or participant roles, influence and decision involvement. |
| `working/reports/signals-and-triggers.md` | Conditions and events that may help identify similar future opportunities, with timing, evidence and limits. |
| `working/reports/case-study.md` | One documented deal or contact journey, from initial context to observed outcome. |
| `working/reports/outreach-examples.md` | Exact openings, follow-ups and replies, with identifiable examples and observed outcomes. |
| `working/reports/gaps.md` | Missing information, contradictions and the next inputs needed. |
| `working/accounts.csv` | Company names, available websites/profile links and attributes already present in the evidence. |
| `working/contacts.csv` | Contact names, available LinkedIn/profile links, roles and company associations. |
| `working/deals.csv` | Commercial opportunities, outcomes and sampling reasons; empty for noncommercial work. |
| `working/outreach.csv` | Outreach sequences linked to contacts/accounts, conversations and response outcomes. |
| `working/outcomes.csv` | Separately verified status observations, such as registration or attendance, with unknowns preserved. |
| `working/evidence.csv` | Source locations, dates and identifiers connecting records to extracts. |
| `working/extracts/*.md` | Source excerpts and exact conversations supporting the reports and tables. |

`working/progress.json` saves scope, coverage and review status so you can resume. Reports remain preliminary where evidence is insufficient. The later handoff stage creates selected, redacted copies, a reading-order index and a reviewed ZIP.

Setup asks for your business website, the offers in scope and where relevant evidence lives.

The workflow explains existing evidence; it does not run enrichment, create campaigns or implement a GTM engine. A reply, a booked meeting and an outreach sequence associated with a won deal remain distinct outcomes; association is not treated as proof of causation.

## Manual installation

If you prefer to install the skill yourself, follow the steps for your app.

### ChatGPT Work

1. Open the ChatGPT desktop app, switch to Work and start a dedicated project.
2. Use the starting prompt above to install the `skills/sales-context-handoff/` folder, following the [current skill installation guidance](https://learn.chatgpt.com/docs/build-skills).
3. Confirm `sales-context-handoff` is available in the skill picker.

### Claude Cowork

1. Give Claude this repository's URL using the starting prompt above.
2. Ask it to guide you through the [current skill installation steps](https://support.claude.com/en/articles/12512180-use-skills-in-claude), preparing any required upload from `skills/sales-context-handoff/`.
3. Enable file/code capabilities and connect a dedicated folder for your sales context.

Once installed, run the setup prompt above. It creates the shared workspace and checks that results can be saved there.

Setup helps connect your selected sources so the assistant can find and collect relevant evidence with as little manual work from you as practical. It can also use existing files, native exports and browser access. Manual extracts are an option when they are the most practical route or you prefer them. For LinkedIn, it requests an export and collects a few browser examples while the archive prepares, then uses the archive for broader collection. Sales Navigator coverage is checked separately.

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
