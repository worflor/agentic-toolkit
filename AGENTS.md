# Agentic Toolkit — Agent and contributor guidance

This repository hosts reusable agentic skills, methodologies, and supporting resources. The catalogue may grow: **do not describe it as a fixed number of skills, a mandatory sequence, or a permanently closed set of tool types.**

Orient using `README.md`, then inspect only the entry or supporting material relevant to the task. A tool or skill should stand on its own unless an explicit dependency is documented.

## Where knowledge lives

- `README.md`: public introduction, current catalogue, installation, and usage.
- `skills/<name>/SKILL.md`: a skill's canonical, discoverable entry point, including its name, purpose, and operating boundaries.
- `skills/<name>/references/`: optional deeper material that the skill can load when relevant.
- `skills/<name>/scripts/` or other resources: optional tooling and examples, with documented requirements when present.
- `Agentic Project Startup.md` and `Project Shaping.md`: compatibility pointers for existing links. Their canonical full methods live at `skills/project-startup/references/method.md` and `skills/project-shaping/references/method.md`.

Don't maintain competing versions of canonical instructions. When adding an entry, give it a clear home and update the catalogue; don't rewrite unrelated skills to accommodate it.

## Working principles

1. **Preserve scope.** Carry out the requested work, not an imagined larger campaign. Inspecting or critiquing a repository does not implicitly authorize edits, PRs, issues, or monitoring.
2. **Keep capabilities composable.** Avoid global prerequisites, automatic cross-skill handoffs, or a mandatory end-to-end pipeline. State genuine dependencies explicitly.
3. **Protect voice and substance.** Each method can be distinctive and opinionated. In particular, Startup is about good homes for knowledge, Shaping is about keeping that knowledge truthful over time, and Superfan is about deep, evidence-grounded criticism. Don't flatten their differences.
4. **Prefer progressive disclosure.** Frontmatter explains when to invoke a skill; `SKILL.md` gives the working instructions; references carry deeper material when warranted.
5. **Use evidence responsibly.** Separate intent, current implementation, runtime verification, historical artifacts, and inferred user experience. Never claim to have inspected, tested, or observed something you haven't.
6. **Keep interventions proportionate.** Prefer a focused, useful capability over extra infrastructure, ritual, or documentation for its own sake. Supporting tools are welcome when they demonstrably serve the method.
7. **Respect project identity.** A toolkit should help people understand a project's taste and constraints, not impose one aesthetic or architecture everywhere.
8. **Preserve continuity.** Protect existing links, references, and history when reorganizing content. Make semantic changes intentionally, not as an accidental result of packaging.

## Before finishing a change

- Confirm affected links, file paths, and README examples actually resolve.
- For each new or modified Agent Skill, verify that `SKILL.md` has valid YAML frontmatter with a matching `name` and clear `description`.
- Ensure referenced files and required utilities ship with the entry or are explicitly documented dependencies.
- Keep the catalogue accurate without describing today's inventory as a permanent limit.
- Verify changed behavior where possible; distinguish checks you ran from checks you did not.
- Preserve the Startup and Shaping compatibility paths and their canonical reference documents.
