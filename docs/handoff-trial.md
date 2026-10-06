# Test a real handoff

Use a synthetic or authorized project with a bounded next task. No new paid agent, account connection, or publication is required by this procedure. If a second host is unavailable, label the trial untested and keep the structural checks separate.

## Trial

1. Adopt Unwalled Garden in the source environment. Record changed files, preserved conventions, unknowns, and the host/model/version where available.
2. Run adoption again with no new facts. Confirm that it does not create competing records, duplicate managed sections, replace unrelated instructions, or reset user customizations. Timestamps alone should not force edits.
3. Start a fresh destination session with the project artifacts and one bounded task. Do not give it the original conversation or explain the expected implementation.
4. Have it locate the goal and constraints, verify current state, identify missing capabilities, and attempt the task. For external actions, use a dry run or synthetic substitute rather than sending or deploying merely to prove portability.
5. Inspect both the outcome and the updated shared records. Record misunderstandings, lost requirements, unexpected dependencies, and any human hints needed.

## Observable acceptance criteria

- The destination identifies the actual next task and preserves prior decisions.
- It finds or reports unavailable inputs without inventing their contents.
- It uses the documented verification method and distinguishes checked from unchecked claims.
- It does not need a private source chat to understand an essential requirement.
- It leaves a useful updated handoff without duplicating the project's task system.
- A repeat adoption preserves unrelated instructions and customization.

Passing one task on one pair of hosts is evidence for that configuration, not universal certification.

## Scenarios to exercise

| Scenario | Expected behavior |
| --- | --- |
| Existing README, decisions directory, and issue tracker | Reuse them; add a context map and only missing state |
| Existing Claude-specific rules | Preserve them; add a supported bridge to shared guidance if needed |
| Conflicting project requirements | Surface the material conflict; do not silently choose or overwrite |
| Browser-only artifact with no export permission | Record the location, access dependency, and gap; do not claim it transferred |
| User explicitly requires a vendor API | Retain it and document setup and migration limits |
| Agent cannot edit project files | Produce proposed files; mark adoption pending |
| A recurring job may still be running elsewhere | Record ownership uncertainty; do not start a duplicate |
| No permission to submit an upstream contribution | Keep any finding local; do not submit based on the invitation alone |

## Result record

Record date, source and destination hosts/versions, task, artifacts supplied, exact verification steps/results, human assistance, unresolved gaps, and outcome (`passed`, `partial`, `failed`, or `untested`). Sanitize material before publishing. A same-agent rehearsal must be labeled as such.
