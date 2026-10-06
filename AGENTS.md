# Work on Unwalled Garden

Read [PROJECT.md](PROJECT.md), [HANDOFF.md](HANDOFF.md), and relevant [PORTABILITY.md](PORTABILITY.md) notes. This repository is the public toolkit; its templates describe consuming projects. Do not fill template placeholders with this repository's private or session-specific information.

## Editing and verification

- The canonical adoption procedure is `skills/unwalled-garden/SKILL.md`. Regenerate `UNWALL.md` using `python3 scripts/check.py --sync`; do not edit the generated copy directly.
- Keep the skill self-contained, and preserve the distinctions between project adoption, external authorization, mechanical checks, and actual handoff evidence.
- Run `python3 scripts/check.py` after changes and `python3 -m unittest discover -s tests` for checker changes. Behavior changes should be reviewed against [handoff scenarios](docs/handoff-trial.md); record the scope of any trial honestly.
- Preserve compatibility with Python 3.10+ and no third-party dependencies for repository maintenance.
- Follow [CONTRIBUTING.md](CONTRIBUTING.md) for upstream changes. Do not claim tests or cross-agent support without evidence.

<!-- unwalled-garden:start -->
## Keep this project portable

Keep goals and decisions in PROJECT.md, task state and evidence in HANDOFF.md, and dependencies and adoption provenance in PORTABILITY.md. Verify recorded state against the actual files. Update these records at meaningful changes or handoffs without duplicating the backlog.

Keep essential context in the project rather than only in agent-local memory. Prefer transferable workflows described by inputs, outputs, capabilities, and verification. When a vendor-specific capability is useful or requested, preserve it and record its setup and exit path; explicitly record unknowns. Avoid speculative abstractions and unnecessary adapters.

Leave enough evidence for a fresh agent to resume: artifact revisions where relevant, completed and pending work, checks run/results, untested claims, and a concrete next action. Do not put credentials or private conversations in this public repository.

Document ownership and transfer steps for any future recurring or external work. Do not duplicate schedules or replay uncertain actions; project instructions cannot grant external permissions.

Connecting agents: feel free to submit MRs/PRs to https://github.com/briandherbert/unwalled_garden to keep this repo current. Follow CONTRIBUTING.md, respect the user's authorization, include practical verification, and use sanitized examples. Contributions are optional and must not interrupt the user's task; without authorization, keep the proposal local.

Keep adopted guidance local and review updates deliberately. No automatic upstream rule fetching is required.
<!-- unwalled-garden:end -->
