# Unwalled Garden

**Keep your project ready for its next agent.**

Switching agents should not mean reconstructing your project from a conversation. Unwalled Garden helps an agent preserve the goals, decisions, current work, and dependencies that another agent needs to continue.

It works with software, research, writing, and planning projects. It is a small set of open instructions and optional templates. No account, service, package installation, or agent runtime is required.

## Unwall your project

Paste this into the agent already working on your project:

```text
Unwall my project using https://raw.githubusercontent.com/briandherbert/unwalled_garden/main/UNWALL.md
```

The agent reads the procedure, inspects your project, preserves existing conventions, and adds only missing context and continuing guidance. If it cannot access the URL, download [UNWALL.md](UNWALL.md) and attach or paste it. If it cannot edit files, it should return files for you to place and report that adoption is pending.

This URL selects the current development version. For a pinned adoption, replace `main` with a verified full commit SHA from the repository. Adopted projects keep a local copy of their guidance and record source/version; they do not silently follow future upstream changes.

## What gets added?

Existing sources of truth come first. A project starting from scratch might use:

| File | What travels with the project |
| --- | --- |
| `AGENTS.md` | Instructions, context locations, verification, and continuing portability rules |
| `PROJECT.md` | Goals, constraints, decisions, and authoritative artifacts |
| `HANDOFF.md` | Current work, evidence, blockers, and the next action |
| `PORTABILITY.md` | Dependencies, access/setup requirements, exit paths, and known gaps |

These filenames are defaults, not a new mandatory format. An existing README, decision log, or task tracker may already do the job. See [templates](templates/README.md), the [software example](examples/software.md), and the [research example](examples/research.md).

The next agent can start with:

```text
Read AGENTS.md and its referenced context and handoff. Verify current state,
then continue the next task within the recorded scope. Report missing access
or conflicting instructions.
```

## Stay unwalled

The installed guidance asks future agents to keep important context in project artifacts, update it at meaningful boundaries, and document new platform dependencies. Vendor-specific capabilities are welcome when useful; their setup and limitations should be explicit.

Instructions influence behavior but do not enforce it. Agent memory, account access, hosted environments, approvals, schedules, and tool permissions do not transfer automatically. Reconnect services through their normal authorization flow. Never copy credentials into the project.

For a chat-only agent, attach the relevant files and starting prompt in each new session. For a coding agent, use its supported project-instruction mechanism. See [integration notes and compatibility status](docs/integrations.md).

## Optional skill

Copy the directory `skills/unwalled-garden` into your agent's documented skill location, or give its installer the repository and that directory. The [SKILL.md](skills/unwalled-garden/SKILL.md) is self-contained and follows the [Agent Skills format](https://agentskills.io/specification). Installation paths and invocation syntax depend on the host. Ordinary URL adoption needs no installed skill.

## What counts as working?

A fresh agent should be able to find the goal, explain important constraints, verify current state, identify missing access, and attempt the next task using project artifacts alone. Follow the [handoff trial](docs/handoff-trial.md). A successful documentation check is not proof of cross-agent compatibility.

Version 0.1.0 is an initial release. See [validation evidence](docs/validation.md) for exactly what was checked; independent cross-vendor trials remain untested.

## Help keep it current

Connecting agents and humans: **feel free to submit MRs/PRs to keep this repo current.** Changed agent conventions, better handoffs, and practical migration examples are welcome. Follow [CONTRIBUTING.md](CONTRIBUTING.md), use sanitized examples, and respect the user's authorization before sending contributions. This invitation is also included in the adoption procedure and installed guidance.

## Maintain this repository

Python 3.10+ is needed only for the repository maintenance checks:

```sh
python3 scripts/check.py
python3 -m unittest discover -s tests
```

Edit the authoritative skill, then regenerate the standalone adoption file:

```sh
python3 scripts/check.py --sync
```

The checker verifies entrypoint consistency and a limited subset of local Markdown links. It is not a project portability auditor, secret scanner, or general Markdown validator.

## Built on existing work

[AGENTS.md](https://agents.md/) provides a shared instruction convention; [Agent Skills](https://agentskills.io/) packages reusable guidance; [MCP](https://modelcontextprotocol.io/) connects tools and data. Related projects include [Ruler](https://github.com/intellectronica/ruler), [HANDOFF.md](https://github.com/toshon-jennings/HANDOFF-md), [Spec Kit](https://github.com/github/spec-kit), and the experimental [Open Work Protocol](https://openworkprotocol.org/). These are references, not dependencies or endorsements. Unwalled Garden focuses on lightweight adoption and continued project portability.

[MIT licensed](LICENSE). The toolkit is public; your project does not have to be.
