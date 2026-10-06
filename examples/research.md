# Worked example: a research brief

Synthetic illustration, not a reported cross-agent trial.

## Before

A team is preparing a transit accessibility brief. It has an editable report, CSV survey data, source URLs, and a recurring dashboard refresh owned by a personal agent. Scope and caveats were agreed in chat. There is no software repository requirement.

## Adoption

- Keep the report and data in their existing user-controlled folder.
- Add shared project context: audience, research question, timeframe, confirmed scope, and the decision to separate survey responses from population estimates.
- Index source URLs with access dates and the dataset revision. Record unavailable sources rather than fabricating summaries.
- Add a handoff with completed sections, open claims, and the next analysis task.
- Document the spreadsheet/dashboard dependency, editable data export, and what the export omits. Preserve formulas or calculation instructions when necessary to reproduce results.
- Inventory the refresh job: its actual owner, trigger/timezone, last confirmed output, and transfer procedure. If the old job's state cannot be checked, record it as unknown and leave replacement inactive.

## Example next task

> Check whether the claim in section 3 is supported by the survey CSV. Record the dataset revision, calculation, and caveats. Update the report and handoff. Do not refresh external dashboards or publish the brief.

## Verification

The next agent should trace the claim to data, reproduce the calculation, and preserve the distinction between sample responses and population estimates. If it lacks the data or calculation environment, it should identify that gap and leave the claim unverified.

## Chat-only transfer

Attach the shared instructions, context, handoff, editable report, and authorized data. Explicitly ask the next session to read them. An instruction file named `AGENTS.md` does not automatically give a chat-only product persistent memory or access to the files.

Updating a local context file does not stop the old agent's refresh job. Transfer operational ownership explicitly through the relevant service when authorized.
