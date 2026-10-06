# Integration notes

Documentation checked: 2026-10-06. These are documented routes, not executed compatibility tests. Behavior can vary by version, settings, organization policy, and product surface. Verify the current host before changing configuration.

| Environment | Documented or manual route | Status in this release |
| --- | --- | --- |
| Codex | Project `AGENTS.md`; scoped instructions and overrides may also apply | Documentation reviewed; independent handoff untested |
| Claude Code | `AGENTS.md` support depends on version/settings and existing Claude files; `@AGENTS.md` in `CLAUDE.md` is a documented import route | Documentation reviewed; independent handoff untested |
| Gemini CLI | `GEMINI.md` by default; configurable context filenames | Documentation reviewed; independent handoff untested |
| Other file-capable agents | Consult their documented project-instruction mechanism; use a minimal adapter when needed | Manual setup required; untested |
| Chat-only agents | Attach project files and explicitly request the shared entry point in each fresh session | Manual setup required; untested |
| Muse, Dots, and other persistent personal agents | Verify available file access and instruction discovery; separately inventory ongoing actions and schedules | Untested; no automatic discovery claim |

## Keep adapters small

When an existing `CLAUDE.md` should load shared guidance, the documented import is:

```markdown
@AGENTS.md
```

Preserve other applicable content. Do not replace existing files blindly. A prose pointer such as “read AGENTS.md” relies on the agent choosing to open it; it is not equivalent to a host-supported import. Avoid symlinks as the universal distribution mechanism because archives, operating systems, and hosts handle them differently.

Gemini CLI documents configurable context filenames. Verify the scope and behavior of configuration in the installed host before choosing a project-local route; don't rewrite a person's global settings to make a project portable. If shared-file loading cannot be established, use an explicit starting prompt and label discovery as manual.

Core shared instructions should use ordinary Markdown and relative links. Host-specific import syntax belongs in the adapter. Account permissions, hooks, approvals, and background jobs require separate setup; instruction files do not transfer them.

## Sources

- [AGENTS.md convention](https://agents.md/)
- [Codex instruction discovery](https://developers.openai.com/codex/guides/agents-md/)
- [Claude Code memory and instruction files](https://code.claude.com/docs/en/memory)
- [Gemini CLI context files](https://geminicli.com/docs/cli/gemini-md/)
- [Agent Skills specification](https://agentskills.io/specification)

When submitting an integration update, include the host/version, checked date, official source, and whether you actually verified loading. Use the [trial procedure](handoff-trial.md) for stronger compatibility evidence.
