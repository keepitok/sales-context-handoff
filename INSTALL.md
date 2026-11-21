# Installation instructions for agents

Read this file when asked to install Sales Context Handoff. The [README](README.md) is the user-facing introduction; the [skill entry point](skills/sales-context-handoff/SKILL.md) contains the workflow to follow after installation.

## Confirm the project

Before installing, check that the user is in ChatGPT Work or Claude Cowork, in a dedicated project with skill support and persistent file access. Ask if the app or project is unclear. If needed, guide the user to the appropriate app and help them start a project, then ask them to paste the prompt there. Reuse an existing Sales Context Handoff project when resuming.

## Use project tools

Use project file tools for installation and the app's built-in browser when browsing is needed; do not use full computer control. Guide the user through any action they need to perform themselves.

## Install within the project

Install only inside the selected project. For Codex, copy the complete `skills/sales-context-handoff/` folder to `<project>/.agents/skills/sales-context-handoff/` using file tools; see the [documented repository scope](https://learn.chatgpt.com/docs/build-skills). Do not use personal/account-wide skill folders or account-level uploads. Check an installer helper's destination before using it; its default must not override project scope. For other hosts, verify their project-local mechanism rather than assuming the Codex path is automatically discovered. If automatic discovery is unavailable, keep the complete folder in the project and explicitly read its `SKILL.md` as project instructions, reporting that discovery is unverified.

## Verify availability

Verify the copied entrypoint and supporting files through file reads or available skill metadata. Do not open desktop settings, inspect the screen or request computer-control access to check installation or the picker. If project write access is unavailable, explain the specific folder-access issue and guide the user through connecting the project folder, then retry installation with project file tools; do not switch to a personal install or a desktop-control workaround. Distinguish files saved, instructions loaded and automatic discovery verified. Repository development tests are not an end-user setup step.

## Start setup

Once the project copy is readable, load the skill, report its actual availability and introduce setup: it confirms scope, connects selected sources and verifies access. Show the skill's short privacy note prominently in chat, then immediately use the two numbered question groups in the installed skill's `references/01-setup.md`: business context and example accounts; data sources and existing documents. Ask both groups together, omitting answered items. Do not ask "Ready to begin?" or require another prompt. Reuse supplied context and adapt the questions to the activity. Follow the setup instructions as answers arrive, without asking the user to assemble a sample of threads or exports. Respect an explicit request to install only and stop.
