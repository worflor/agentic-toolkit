# Agentic Toolkit

**Reusable, opinionated methods for agents working with real projects.**

This is a small collection of independent [Agent Skills](https://agentskills.io/specification) for helping an agent understand a repository, give its knowledge good places to live, keep its representation honest as it evolves, and criticize what it actually feels like to use.

Not an orchestration platform, daemon, monitoring service, or mega-prompt. Each skill has a distinct job. Use one when it earns its place.

## Skills

| Skill | Reach for it when… | What it does |
| --- | --- | --- |
| **[Superfan](skills/superfan/SKILL.md)** | You want an obsessively detailed, opinionated reading of a repository, feature, gameplay loop, user fantasy, design arc, or conceptual inconsistency. | Reconstructs the project's identity and history, traces interactions, and develops evidence-grounded taste. **Analysis-only by default.** |
| **[Project Startup](skills/project-startup/SKILL.md)** | You're starting, adopting, or reorganizing a project, and workers need to find trustworthy context without guesswork. | Establishes predictable information architecture and appropriately scoped canonical documents without templating away the project's identity. |
| **[Project Shaping](skills/project-shaping/SKILL.md)** | A project has learned things through development and its docs, conventions, assumptions, or structure need to catch up. | Reconciles intended direction, implementation reality, living context, archaeology, and residue while preserving project taste. |

**These are not phases of a mandatory pipeline.** Superfan can critique something without reorganizing it. Shaping can repair documentation without performing a superfan review. Startup can organize a mature codebase without redesigning it.

## Install

Use the [skills CLI](https://github.com/vercel-labs/skills) to install an individual skill:

```bash
npx skills add worflor/agentic-toolkit --skill superfan
```

Or install the whole collection:

```bash
npx skills add worflor/agentic-toolkit --all
```

To make Superfan available globally to Claude Code, for example:

```bash
npx skills add worflor/agentic-toolkit --skill superfan -g -a claude-code -y
```

**Repository access:** This repository is currently private. The installer requires authentication with an account that can read it. The skills CLI supports existing Git credentials, authenticated GitHub CLI, and SSH. Alternatively, clone the repo using your normal Git authentication and run `npx skills add . --skill superfan` from the checkout. Installation does not require making this repository public.

You can also use these skills without the installer: copy the complete desired `skills/<name>/` directory into a location your agent recognizes (for example `.claude/skills/` or `.agents/skills/`). **Copy the directory, not just `SKILL.md`,** for Startup and Shaping: their full reference documents are part of the skill.

## Invoke

Tell a compatible coding agent what to examine and which skill to use. For example:

> Use **superfan** on this repo. Trace the core experience, the intended fantasy, and the actual implementation. Go looking for tiny pieces of awkwardness and deeper cohesion problems. Read-only.

> Use **superfan** on the Fate system. Trace only the other systems that meaningfully shape its user-facing experience. Distinguish implemented behavior from design intentions.

> Use **project-startup** to give this existing repo a sensible knowledge structure while preserving its conventions and personality.

> Use **project-shaping** to reconcile the project's design documents, status, implementation, history, and emerging direction. Do not touch the code.

The user sets the scope and whether changes are authorized. A skill isn't permission to silently edit a repository.

## Why these three belong together

A project needs its own identity and an understandable representation of that identity:

- **Startup** asks: *Where should important knowledge live?*
- **Shaping** asks: *Does the knowledge still match what the project has become?*
- **Superfan** asks: *What kind of experience or system does all this actually add up to, and where does it feel wrong or unusually right?*

The organizing principle is **predictability at the center; emergence around it**. Give workers solid landmarks while letting each project remain recognizably itself.

## Repository layout

```text
skills/
  superfan/
    SKILL.md                  # Complete, standalone critic
  project-startup/
    SKILL.md                  # Skill entry point
    references/method.md      # Complete, canonical Startup methodology
  project-shaping/
    SKILL.md                  # Skill entry point
    references/method.md      # Complete, canonical Shaping methodology
AGENTS.md                     # Contributor/agent orientation
Agentic Project Startup.md    # Compatibility pointer to Startup
Project Shaping.md            # Compatibility pointer to Shaping
```

The original Startup and Shaping text has been preserved in the reference files rather than abbreviated or regenerated. Each skill is independently installable. The former root documents are now links to their canonical locations.

## Contributing and evolution

Add a skill when it describes a **distinct, reusable practice** with a clear invocation boundary; do not add a separate prompt for every project preference or make this a warehouse of unrelated roleplay. Keep project-specific truths in their own repositories.

Prefer small `SKILL.md` entry points with deeper resources loaded only when relevant. Don't maintain parallel, diverging copies of canonical material. See [AGENTS.md](AGENTS.md) for repository-editing guidance.
