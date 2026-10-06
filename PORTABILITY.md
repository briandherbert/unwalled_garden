# Portability notes

This repository implements and adopts Unwalled Garden 0.1.0. Source: https://github.com/briandherbert/unwalled_garden. Initial adoption: 2026-10-06. Resolve the published commit for immutable provenance; the version metadata does not imply that a release tag exists.

## Dependencies

| Capability | Current choice | Access/setup | Exit path or limitation |
| --- | --- | --- | --- |
| Read and adopt instructions | UTF-8 Markdown files | Any file reader; manual attachment is possible | Copy/download files; no service or model required |
| Versioned distribution and contributions | GitHub public repository | Public read; authenticated write or fork/PR | Standard Git clone, mirror, or archive; update upstream links if moved |
| Maintenance checks | Python 3.10+ standard library | `python3 scripts/check.py` | Plain source; adopters do not need Python |
| Skill discovery | Host's Agent Skills support | Install the skill directory using host documentation | Use standalone UNWALL.md when skills are unsupported |
| Continuing guidance | AGENTS.md or host-specific adapter | Verify loading in the actual host | Manual starting prompt and file attachment |

No credentials, runtime service, scheduled job, or production deployment is part of this toolkit. User projects retain their own access controls. No automatic self-update mechanism exists.

## Evidence and limits

See [validation](docs/validation.md) for checks actually performed and [integration notes](docs/integrations.md) for documentation-based routes. No universal compatibility claim is made. Independent cross-vendor handoff trials remain untested at initial release.

## Updating

Review upstream or contributor changes against the current skill, templates, examples, and local customization. Regenerate UNWALL.md from its source and rerun checks. A release tag is a convenient version reference; users needing immutable provenance should record the resolved commit SHA as well.
