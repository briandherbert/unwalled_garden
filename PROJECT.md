# Project context

## Goal

Help people make software and non-software projects easier to continue with another AI agent, using a public instruction URL and project-local records.

## Scope

Initial release: a standalone adoption procedure, an optional standard skill, minimal templates, integration notes, two synthetic examples, contribution guidance, and maintenance checks. Account migration, an agent runtime, a hosted service, and universal compatibility certification are outside scope.

## Decisions

| Decision | Rationale |
| --- | --- |
| Reuse existing AGENTS.md and Agent Skills conventions | Avoid requiring another proprietary format |
| Use ordinary project files with optional adapters | Keep context accessible without a particular agent or hosting service |
| Canonical SKILL.md; generated UNWALL.md | Support one-prompt adoption and skill installation without divergent procedures |
| Preserve useful vendor-specific features; document dependencies | Portability should not remove capabilities or trigger unrelated migrations |
| Invite connecting agents to submit MRs/PRs | Keep platform guidance current through real usage, within user authorization |
| Separate structural validation from actual handoff trials | Prevent unsupported claims about compatibility |
| MIT license | Allow reuse and adaptation of the toolkit |

The project concept, name, public distribution, and contribution invitation were requested by the project owner. File organization and maintenance tooling are initial implementation choices.

## Artifact map

Start at [README.md](README.md). The canonical procedure is [SKILL.md](skills/unwalled-garden/SKILL.md), distributed as [UNWALL.md](UNWALL.md). Optional [templates](templates/README.md) and [trial instructions](docs/handoff-trial.md) support adoption. Current work is in [HANDOFF.md](HANDOFF.md).
