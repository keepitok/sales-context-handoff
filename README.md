# Sales Context Handoff

**Turn your sales history into a clear, evidence-backed handoff.**

Sales Context Handoff helps sales leaders prepare a reviewed handoff for a new sales hire, a GTM engineer or another recipient who needs to understand the business's sales context.

Use the data you already have: CRM records or spreadsheets, email, existing call transcripts, LinkedIn messages and Sales Navigator conversations. No particular CRM or enrichment subscription is required.

## Start here

Start a new project in **ChatGPT Work** (desktop app) or **Claude Cowork**, then paste this prompt:

```text
Read the README at <PUBLIC_REPOSITORY_URL>, install sales-context-handoff in this project only, and tell me the next step.
```

Replace `<PUBLIC_REPOSITORY_URL>` with this repository's public URL once published.

> **For agents:** Before installing, check that the user is in ChatGPT Work or Claude Cowork, in a dedicated project with skill support and persistent file access. Ask if the app or project is unclear. If needed, guide the user to the appropriate app and help them start a project, then ask them to paste the prompt there. Reuse an existing Sales Context Handoff project when resuming.

> Use project file tools for installation and the app's built-in browser when browsing is needed; do not use full computer control. Guide the user through any action they need to perform themselves.

> Install only inside the selected project. For Codex, copy the complete `skills/sales-context-handoff/` folder to `<project>/.agents/skills/sales-context-handoff/` using file tools; see the [documented repository scope](https://learn.chatgpt.com/docs/build-skills). Do not use personal/account-wide skill folders or account-level uploads. Check an installer helper's destination before using it; its default must not override project scope. For other hosts, verify their project-local mechanism rather than assuming the Codex path is automatically discovered. If automatic discovery is unavailable, keep the complete folder in the project and explicitly read its `SKILL.md` as project instructions, reporting that discovery is unverified.

> Verify the copied entrypoint and supporting files through file reads or available skill metadata. Do not open desktop settings, inspect the screen or request computer-control access to check installation or the picker. If project write access is unavailable, explain the specific folder-access issue and guide the user through connecting the project folder or copying the skill there; do not switch to a personal install or a desktop-control workaround. Distinguish files saved, instructions loaded and automatic discovery verified. Repository development tests are not an end-user setup step.

> Once the project copy is readable, load the skill, report its actual availability and introduce setup: it confirms scope, connects selected sources and verifies access. Show the skill's short privacy note prominently in chat, then immediately ask the first unanswered setup question, usually the business website and offer in scope. Do not ask "Ready to begin?" or require another prompt. Reuse supplied context; if the activity is already clear, ask where its records and conversations live. Follow the setup instructions as answers arrive, without asking the user to assemble a sample of threads or exports. Respect an explicit request to install only and stop.

## The workflow

One skill guides you through four stages at your own pace. After installation, it starts with the setup questions. Between later stages, it explains the next step and waits for you to proceed. Each stage saves its results so you can review them or resume in a new conversation.

Use these prompts to start or resume a stage:

| Stage | Prompt |
| --- | --- |
| **Set up** | Help me set up a sales-context handoff: confirm my business, offers and data sources. |
| **Collect** | Collect my deal evidence and successful outreach examples from my selected sources. |
| **Analyze** | Analyze my sales context and prepare findings for handoff. |
| **Review and hand off** | Help me review and redact my sales-context handoff, then package the results I choose to share. |

If the skill appears in ChatGPT Work's `@` picker, you can select it there. Otherwise, ask the assistant to read the project's `sales-context-handoff/SKILL.md` at the saved installation path and follow it. The skill uses your request and saved progress to choose the current stage.

To resume, point the assistant to your workspace and say: “Resume my sales-context analysis from the saved progress.”

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

Setup asks for your business website, the offers in scope and where relevant evidence lives.

The workflow explains existing evidence; it does not run enrichment, create campaigns or implement a GTM engine. A reply, a booked meeting and an outreach sequence associated with a won deal remain distinct outcomes; association is not treated as proof of causation.

## Project-only installation

The starting prompt keeps the skill inside your selected project. If you prefer to copy files yourself, copy the complete `skills/sales-context-handoff/` folder into that project's skill location and tell the assistant where it is. For Codex, this is `.agents/skills/sales-context-handoff/` inside the project. If your app does not discover project skills, the assistant can read the saved instructions directly; this does not register an account-wide skill.

Installation uses project file access. For web sources, the workflow uses suitable connections or the app's built-in browser by default. It does not require full computer control. If a user-only action is needed, the assistant explains the steps for you to perform.

Once the instructions are available, the assistant starts the setup questions. Setup creates the shared workspace and checks that results can be saved there.

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
