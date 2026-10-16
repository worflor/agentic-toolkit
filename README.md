# Agentic Toolkit

**Reusable skills, methods, and tools for working thoughtfully with AI agents.**

Agentic Toolkit is a home for portable, opinionated ways of understanding, building, examining, and maintaining projects. Each capability should solve a recognizable problem, explain when to use it, and respect the context of the project it enters.

Use what is relevant. Nothing requires adopting the rest of the collection, following a prescribed pipeline, or giving an agent more authority than the task calls for.

## Skills

Skills are packaged using the [Agent Skills](https://agentskills.io/specification) format. Each has its own entry point and can be installed independently.

| Skill | Use it for | Focus |
| --- | --- | --- |
| **[Superfan](skills/superfan/SKILL.md)** | A deeply opinionated examination of a repository, feature, workflow, experience, or design trajectory. | Reconstruct intent and history, inspect how parts interact, and find cohesion gaps, awkwardness, and overlooked potential. Read-only by default. |
| **[Project Startup](skills/project-startup/SKILL.md)** | Starting, adopting, or reorganizing a project so its important knowledge is easy to find. | Establish predictable information architecture without imposing a rigid template. |
| **[Project Shaping](skills/project-shaping/SKILL.md)** | Reconciling what a project has become with its documentation, conventions, and accumulated decisions. | Preserve project identity while resolving outdated context, hidden assumptions, and emerging structure. |

Skills are **independent practices, not stages in a required workflow**. Their boundaries matter more than their order.

## Installation

Install a selected skill with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add worflor/agentic-toolkit --skill superfan
```

Or install every skill available in the repository:

```bash
npx skills add worflor/agentic-toolkit --all
```

For example, to install Superfan globally for Claude Code:

```bash
npx skills add worflor/agentic-toolkit --skill superfan -g -a claude-code -y
```

If this repository is private, access requires GitHub authentication with permission to read it. You can also clone it using your existing Git credentials and run `npx skills add . --skill superfan` from the checkout.

Manual installation works too: copy the complete `skills/<name>/` directory into a location supported by your agent, such as `.claude/skills/` or `.agents/skills/`. Include bundled references and other resources, not just `SKILL.md`, when a skill depends on them.

## Usage

Invoke a skill with a clear subject and scope. For example:

> Use **superfan** to investigate this repository's core experience. Trace its history, inspect the actual implementation, and be painfully specific about design friction. Read-only.

> Use **superfan** on this feature. Follow its dependencies only where they materially shape the user experience, and distinguish design intentions from observable behavior.

> Use **project-startup** to make the repository's context and responsibilities easy for future workers to navigate.

> Use **project-shaping** to reconcile what the codebase has learned with its documentation and current direction. Don't edit code.

A skill supplies a method, **not blanket permission to change things**. The task defines the scope and the user authorizes any changes.

## Philosophy

**Predictability at the center; emergence around it.**

Good agentic work needs trustworthy context, clear boundaries, and room for a project's own character to survive. The recurring ideas behind this toolkit are:

- **Understand before intervening.** Read the code, documents, history, and behavior relevant to the question.
- **Distinguish evidence from interpretation.** A specification, an implementation, a passing test, and a lived experience are not interchangeable.
- **Protect useful weirdness.** Avoid sanding off deliberate design choices merely because they are unconventional.
- **Prefer proportionate methods.** A valuable skill should help with the task, not create another maintenance project.
- **Keep context local.** Project-specific truths belong with their projects; reusable methodology belongs here.

These are guiding principles, not a required checklist or a claim that every future tool must behave identically.

## Repository conventions

```text
skills/
  <skill-name>/
    SKILL.md             # discoverable entry point
    references/          # deeper source material, when needed
    scripts/             # optional supporting utilities
README.md                # catalogue and usage
AGENTS.md                # contributor/agent guidance
```

Individual entries can be self-contained or include additional reference material, examples, and utilities. Keep dependencies explicit and avoid loading unrelated skills just to use one.

The full Project Startup and Project Shaping methods live in their respective `references/method.md` files. The [former Startup path](Agentic%20Project%20Startup.md) and [former Shaping path](Project%20Shaping.md) remain available for existing links.

## Contributing

A new entry should provide a distinct, reusable capability with a clear purpose, invocation boundary, and honest limitations. Preserve each method's individual voice and substance rather than standardizing every skill into the same personality.

Add supporting files only when they improve understanding or execution. Keep canonical knowledge in one place, update the catalogue when capabilities change, and document any required tooling or cross-skill dependencies.

See [AGENTS.md](AGENTS.md) for practical repository guidance.
