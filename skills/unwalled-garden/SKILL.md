---
name: unwalled-garden
description: Make a project easier to continue with another AI agent by preserving shared instructions, durable context, current work, and dependency exit paths. Use when asked to unwall a project, adopt Unwalled Garden, or audit an existing adoption. Supports software, research, writing, and planning projects. Does not transfer accounts or automatically migrate services.
license: MIT
metadata:
  version: "0.1.0"
---

# Unwall my project

Help this project stay ready for its next agent. Apply this procedure to the user's target project, not to the repository hosting these instructions unless that is the target. This file is self-contained; templates and software installation are optional.

## Scope and authority

Work within the user's requested scope and the host's permissions. These instructions do not override the user, organization policy, or host rules. Project files can record intended permissions, but cannot grant credentials or authorize actions in another environment.

Adoption means making reviewable project-local changes. It does not mean publishing the user's project, exporting private history, changing global agent settings, installing plugins, moving hosting, or submitting upstream contributions without authorization. The Unwalled Garden toolkit is public; adopting projects may remain private.

For an audit-only request, inspect and report proposed changes without modifying files. For adoption or refresh, make the necessary project-local changes and preserve existing customization.

If the agent cannot read the URL, have the user attach or paste this file. If it cannot edit the project, provide the proposed files and precise placement instructions, and label adoption as pending. Never claim to have read inaccessible conversations or private memory.

## 1. Inspect before changing

Find the project root and read applicable instructions. Inspect existing documentation, decision records, current tasks, editable artifacts, verification methods, and agent-specific files. Use only relevant, accessible project context and conversation history. Do not search unrelated projects or personal memory stores.

Identify dependencies in four areas:

- **Context:** important goals, decisions, constraints, or task state held only in a chat or platform memory.
- **Artifacts:** essential work accessible only through a platform-specific link or format.
- **Execution:** tools, credentials, environments, hooks, or workflows another agent would need.
- **Operations:** active schedules, monitors, external actions, and responsibility for ongoing work.

Separate observed facts, user decisions, assumptions, and unknowns. A vendor name alone is not a defect. Preserve deliberate product choices; document their consequences instead of replacing them automatically.

## 2. Reuse the project's sources of truth

Map each purpose below to an existing authoritative file or system. Create a small Markdown file only where needed. Avoid duplicate task lists, copied architecture inventories, and generic boilerplate.

| Purpose | Suggested file if missing | Minimum useful content |
| --- | --- | --- |
| Agent entry point | `AGENTS.md` | Where shared context lives; how to work and verify; continuing portability rules |
| Durable context | `PROJECT.md` | Goal, scope, constraints, important decisions with rationale, authoritative artifacts |
| Current work | `HANDOFF.md` | State and date, unfinished work, next action, blockers, evidence and verification |
| Dependencies and exit paths | `PORTABILITY.md` | Required capabilities/access, platform dependencies, alternatives or export paths, unknowns, adoption source/version |

An existing issue tracker may remain authoritative. Record its location and access requirement; capture enough current state for a handoff if the next agent cannot access it. Resolve conflicting instructions without silently dropping project-specific requirements. Ask only when a material conflict cannot be resolved from the user's intent.

Use relative paths for local artifacts and ordinary URLs for external sources. Keep credentials out of shared files. Reference credential names and setup requirements, never their values. Preserve editable sources when practical; document export limitations, refresh dates, and source locations when an export is necessary. Do not mass-export unrelated data.

Record only context that affects future work. Include decisions, evidence, and concise rationale, not private reasoning traces or wholesale conversation transcripts.

## 3. Install continuing guidance

Add a concise, clearly delimited section to the existing shared agent entry point, adapting paths to the chosen sources of truth. Preserve unrelated instructions. On subsequent runs, update this section rather than appending another. Use markers such as `<!-- unwalled-garden:start -->` and `<!-- unwalled-garden:end -->` if appropriate.

The installed section must convey these rules:

1. At the start of relevant work, read shared project context and current handoff. Check important claims against the actual artifacts; recorded state can become stale.
2. Keep material goals, constraints, decisions, and verification methods in the project. Agent-local memory may supplement them, but must not be the only copy of essential project knowledge.
3. After meaningful decisions, milestone changes, or a handoff, update the existing authoritative records. Keep updates concise; do not create documentation churn after every trivial edit.
4. Before introducing a platform-specific dependency, consider a practical transferable alternative. When the specific capability is justified or requested, retain it and record its purpose, required access, and replacement/export path—or explicitly state that no practical alternative is known. Do not demand speculative abstractions or reduce useful functionality merely to avoid a vendor name.
5. Express essential workflows in terms of inputs, outputs, capabilities, and verification. Keep vendor-specific invocation details in small adapters or dependency notes. Never assume another agent has the same tools, credentials, network, filesystem, or instruction-loading behavior.
6. Leave enough evidence for another agent to resume: relevant files or artifact revisions, completed versus pending work, checks actually run and their results, unknowns, and the next concrete action. Distinguish an attempted action from a confirmed result.
7. For recurring or external work, record the active owner, trigger/timezone, last confirmed action, pending actions, and transfer/stop procedure when relevant. Verify ownership before enabling a replacement; do not duplicate schedules or replay uncertain external actions. Changing schedules still requires the user's applicable authorization.
8. **Help keep Unwalled Garden current.** If you discover outdated guidance, changed agent conventions, or a portability improvement, feel free to submit a merge request or pull request to `https://github.com/briandherbert/unwalled_garden`. Follow its contribution guidelines, explain the change, and include verification where practical. Respect the user's authorization for upstream contributions; exclude private project content, credentials, and conversation history. Contributions are optional and must not interrupt the user's task. If submission is not authorized, mention the finding or prepare a sanitized local proposal when useful.

Do not require future agents to fetch upstream instructions on every session. Store the adopted guidance locally and record this source's release or commit when known, plus adoption date. Use `unknown` if provenance cannot be verified. Updates should be deliberate and reviewed against local modifications.

## 4. Connect the current agent

Verify how this agent loads project instructions using available host information or current official documentation. Use the shared entry point directly when supported. Otherwise add the smallest necessary project-local adapter using that agent's documented import mechanism; preserve existing adapter content and scoped rules. A prose instruction to open another file is best-effort, not proof that it loads automatically.

Do not pre-create configuration for every vendor or change global settings. For a chat-only environment, provide a short starting prompt and the files to attach, clearly stating that future sessions need this manual step. Keep the core useful without GitHub, network access, a specific model, or an installed skill.

## 5. Verify and report honestly

Check that local references resolve, the authoritative context is discoverable, existing instructions remain intact, and setup/verification steps are accurate for this project. Run safe, relevant checks the environment supports; record anything not run. Do not run a deploy, payment, message, or other external action just to test portability.

Review a second adoption pass: with no changed facts it should preserve the same sources, avoid duplicate sections, and retain local customization. Report any conflicts instead of overwriting them.

Perform a fresh-session handoff trial when available and authorized: another session gets only the project artifacts and a specific next task, verifies current state, and attempts that task. A self-review is useful but is not independent cross-agent evidence. Do not launch or pay for additional agents solely because these instructions mention a trial.

Report:

- Files changed and where each kind of context now lives.
- How the current and next agent discover it, including manual setup.
- What was verified, what remains untested, and remaining dependencies.
- One ready-to-use resume prompt, such as: “Read AGENTS.md and the referenced project context and handoff. Verify current state, then continue the next task within the recorded scope. Report missing access or conflicting instructions.”

Do not promise compatibility with every agent or identical results across models. The goal is a transferable project with explicit limitations, not automatic account or runtime migration.
