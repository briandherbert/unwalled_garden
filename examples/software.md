# Worked example: a small web app

Synthetic illustration, not a reported cross-agent trial.

## Before

A project already has a README with setup commands, `docs/decisions/` with architectural decisions, and `CLAUDE.md` containing useful coding conventions. A chat contains the important detail that the CSV export must preserve leading zeroes in postal codes. The UI export screen is unfinished.

## Adoption

- Keep setup commands in the README and decisions in `docs/decisions/`.
- Add the confirmed postal-code requirement to the existing feature specification, with its user-decision provenance.
- Add an `AGENTS.md` context map and the continuing guidance from Unwalled Garden.
- Preserve `CLAUDE.md` conventions; use its documented `@AGENTS.md` import if needed by the current environment.
- Create a short `HANDOFF.md` because no current-work record exists.
- Record that production deployment uses a chosen hosting service. Local development remains possible without that service; deployment requires separate access. Do not migrate hosting merely to adopt the toolkit.

## Example handoff content

> Goal: finish CSV export without altering postal-code strings.
>
> Current state: export UI is incomplete. The existing specification and decision records are authoritative. No validation has yet been run for the unfinished screen.
>
> Next action: implement the export path and use a fixture containing postal code `00123`. Acceptance: exported CSV preserves `00123` and existing export tests pass.
>
> Setup and verification: use the commands in the README; report any unavailable dependencies. Production deployment is outside this task.

## Repeat adoption

Reuse the same documents. Preserve the postal-code requirement, existing Claude conventions, and project-specific changes to the installed guidance. Do not create another decision log or managed section.

## Destination prompt

“Read AGENTS.md and the referenced context and handoff. Finish the CSV export task and verify that postal-code strings are preserved. Report missing access; do not deploy.”

The meaningful test is whether a fresh agent preserves the requirement without seeing the original conversation.
