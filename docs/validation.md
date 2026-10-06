# Validation evidence

Release: 0.1.0. Date: 2026-10-06.

This document separates repository checks from behavioral evidence. The software and research examples are synthetic illustrations.

## Repository checks

Observed on Python 3.14.5:

- `python3 scripts/check.py`: passed; generated entrypoint matches the canonical skill and simple local links resolve across 18 Markdown files.
- `python3 -m unittest discover -s tests -v`: six tests passed. They cover a clean checkout, repeated regeneration without rewriting an unchanged file, stale entrypoint detection/repair, broken local references, out-of-repository links, excluded URL/fragment/code examples, and invalid skill metadata.
- The skill-creator `quick_validate.py` check: passed with PyYAML 6.0.3 in an isolated validation environment. That external validator is not a runtime dependency of this repository.

The checker does not fetch external URLs or validate anchor fragments, arbitrary Markdown, instruction-loading behavior, or semantic project portability. Python 3.10 is the intended minimum, but this release was executed on Python 3.14.5 only. Repeated generation tests validate the distribution script, not real agents' repeated adoption behavior.

## Behavior and compatibility

The adoption procedure has been reviewed against the scenarios in [handoff-trial.md](handoff-trial.md), including repeated adoption, existing instructions, unavailable context, deliberate vendor dependencies, chat-only environments, uncertain scheduled work, and contribution authorization. This is author review, not an executed independent agent trial.

Cross-vendor adoption and fresh-session continuation: **untested**. Automatic loading by each named host: **untested**. See [integration notes](integrations.md) for documentation reviewed on this date.

No score, badge, or check output in this repository certifies that a consuming project is portable. Record actual handoff evidence before making narrower compatibility claims.
