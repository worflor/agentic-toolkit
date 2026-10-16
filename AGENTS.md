# AGENTS.md — Agentic Toolkit

This repository is a collection of independent, installable methodologies for agents working with projects. It is **not** an agent runner or universal workflow. Read the README first, then only the skill relevant to the requested work.

## Map and authority

- `README.md`: public front door, catalogue, installation, and boundaries.
- `skills/superfan/SKILL.md`: canonical, standalone Superfan skill; intensely opinionated, evidence-grounded analysis. Invocation is read-only by default.
- `skills/project-startup/SKILL.md`: onboarding and invocation contract for Startup.
- `skills/project-startup/references/method.md`: **canonical full Startup methodology**, moved verbatim from the original root document.
- `skills/project-shaping/SKILL.md`: onboarding and invocation contract for Shaping.
- `skills/project-shaping/references/method.md`: **canonical full Shaping methodology**, moved verbatim from the original root document.
- `Agentic Project Startup.md` and `Project Shaping.md`: old-path compatibility pointers; do not add competing full copies.

## Editing principles

1. **Keep skills independent.** Do not force Startup, Shaping, and Superfan into a mandatory pipeline. Each should make sense when installed in isolation.
2. **Preserve the original methods' voice and substance.** Startup establishes predictable homes for knowledge; Shaping reconciles that knowledge with what a project becomes. Both value legibility, proportionality, and identity over documentation theater.
3. **No silent semantic rewrites.** Improving an entry point or reorganizing paths is not a license to flatten an opinionated methodology. Edit canonical references only when intentionally changing their meaning.
4. **Progressive disclosure.** A skill's YAML frontmatter says when to use it, `SKILL.md` provides essential instructions, and `references/` stores the long-form method if it needs one.
5. **Read-only means read-only.** A project being inspected through Superfan should not receive unsolicited code changes, PRs, issues, or monitoring.
6. **Evidence over invention.** Do not assert that a test was run, a UX was observed, or a repository was fully read when it wasn't. Distinguish specification, implementation, verification, and inferred experience.
7. **Keep the toolkit lightweight.** Do not add required runtimes, telemetry, trackers, or deployment infrastructure to solve a prompt/skills problem.

## Verification after editing

- Each `skills/<name>/SKILL.md` starts with valid YAML frontmatter containing matching `name` and an informative `description`.
- References are relative to the skill folder and are bundled with that skill.
- Old root paths still lead readers to the canonical documents.
- The README's examples and install commands match the actual directory structure.
- Preserve project history; don't delete original work or present moved texts as newly authored work.
