# Contributing

Humans and connecting agents: feel free to submit merge requests or pull requests to keep Unwalled Garden current. GitHub calls them pull requests; contributions from any agent ecosystem are welcome.

Finish the user's task first. Submit only when the user has authorized upstream contributions under your host's rules. This invitation does not itself grant permission to publish private material. Without submission authorization, provide a sanitized local proposal when useful.

## Useful contributions

- An agent changed how it discovers or loads project instructions.
- A real transfer exposed missing context or an undocumented dependency.
- An adoption duplicated, overwrote, or misplaced existing project guidance.
- A smaller example or better verification method makes handoffs easier.

Search existing issues/PRs before submitting. Keep changes focused; explain the problem, resulting behavior, and verification. Include official documentation and its checked date for claims about platform behavior. For a handoff result, record host/model versions, setup, supplied artifacts, task, outcome, and limitations. Distinguish documentation review, same-agent rehearsal, and an independent cross-agent trial.

Use synthetic or explicitly approved examples. Do not include credentials, private paths, project content, customer data, or conversation histories. Redacting a name alone may not make a real example safe to publish.

## Editing

`skills/unwalled-garden/SKILL.md` is the authoritative adoption procedure. `UNWALL.md` is generated from its body. Keep the procedure self-contained so downloaded files and installed skills work offline. Templates illustrate it; they must not introduce contradictory requirements.

1. Branch or fork using your existing workflow.
2. Edit the relevant files, preserving the small footprint and existing standards.
3. Run `python3 scripts/check.py --sync` if the skill body changed.
4. Run `python3 scripts/check.py`, `python3 -m unittest discover -s tests`, and relevant scenarios in [the handoff trial](docs/handoff-trial.md).
5. Open a PR explaining what you actually verified and what remains untested.

Do not claim universal support, turn optional dependencies into mandatory infrastructure, or add an auto-update service. A vendor-specific adapter is appropriate when it makes shared context discoverable without duplicating its substance.

Contributions are provided under the repository's [MIT license](LICENSE).
