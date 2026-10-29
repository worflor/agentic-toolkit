# Agentic Toolkit

**Reusable skills for developers working with coding agents.**

Coding agents can produce a lot of work quickly. Understanding a project, respecting its intent, spotting weak assumptions, and keeping the result maintainable are different challenges.

Agentic Toolkit collects practical ways to approach those challenges. Use them on a side project, an established application, a library, a game, a research tool, or something in between. Each skill has its own job and point of view, and none requires the others.

The skills follow the [Agent Skills specification](https://agentskills.io/specification). They're instructions and supporting resources for compatible agents, not an agent runner, a required development process, or a dependency your software needs. The methods are plain Markdown, so you can also read or adapt them yourself.

## Find the right skill

| Skill | When to use it | What it does |
| --- | --- | --- |
| **[Superfan](skills/superfan/SKILL.md)** | You want more than a surface-level review of a feature, API, design, or research question. | Investigates the details, follows connections, and develops evidence-grounded opinions about what works and what doesn't. |
| **[Project Startup](skills/project-startup/SKILL.md)** | You're starting a repository or inheriting one that's hard to navigate. | Gives documentation, decisions, and working context sensible places to live without forcing a project template. |
| **[Project Shaping](skills/project-shaping/SKILL.md)** | Code, documentation, and earlier decisions have drifted apart as a project evolves. | Traces what changed and reconciles the project's understanding of itself without inventing its direction. |
| **[Anti-Slop](skills/anti-slop/SKILL.md)** | Docs, comments, or agent instructions have become repetitive, outdated, or difficult to maintain. | Removes unnecessary noise while protecting useful reasoning, local conventions, and personality. |

Each skill can handle its own task. You can also bring its perspective into another job, such as using Superfan to sharpen research or Anti-Slop to keep documentation tidy during implementation. There's no required order or automatic handoff between skills.

## Get started

Install an individual skill with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add worflor/agentic-toolkit --skill superfan
```

Or install all available skills:

```bash
npx skills add worflor/agentic-toolkit --all
```

For agent-specific installation options, see the skills CLI documentation. You can also copy a complete `skills/<name>/` directory, including its references, into your agent's supported skills location.

If you're accessing this repository privately, you'll need GitHub read access. You can also clone it and run `npx skills add . --skill superfan` from the checkout.

## Give a skill a job

Once installed, talk to your agent like you normally would. You don't need to explain the skill back to it:

> I'm pretty sure this API makes sense only to me. **Superfan** it before I call it stable.

> This started as a weekend project, and now people actually want to contribute. Can **Project Startup** help me sort out the repo?

> We've rebuilt the backend twice, and half the docs still describe the old version. Give it a **Project Shaping** pass.

> These docs read like five agents took turns summarising each other. Please **Anti-Slop** them.

You can also bring a skill into another task:

> We're torn between building our own plugin system and adopting an existing one. Research the options **with Superfan**. I want to know what we'll regret later.

The task sets the scope and permissions. A review isn't permission to edit. Cleanup isn't permission to redesign a product. Using more than one skill doesn't expand either.

## What the skills have in common

**Predictable foundations, room for character.** The methods differ, but they share a few habits:

- **Understand before changing.** Look at the actual project, not just its introduction or the latest conversation.
- **Distinguish evidence.** Intended behaviour, documented behaviour, implementation, tests, and likely user experience aren't interchangeable.
- **Respect the project's identity.** Existing conventions, decisions, and deliberate weirdness deserve understanding before they're replaced.
- **Prefer proportionate work.** Keep useful context easy to find, changes focused, and process lighter than the value it provides.
- **Be clear about uncertainty.** Say what was inspected or verified, what was inferred, and what still needs a decision.

## Explore and contribute

Each skill lives in `skills/<name>/SKILL.md`, with deeper guidance under `references/` where needed. The longer [Project Startup method](skills/project-startup/references/method.md) and [Project Shaping method](skills/project-shaping/references/method.md) are available for readers who want the full approach.

See [AGENTS.md](AGENTS.md) for repository-specific contribution guidance. A new skill should solve a recognisable, reusable problem, have a useful standalone default, and keep its own character.

To validate skill metadata, local links, and the validator's tests:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

These checks cover structure, not whether an agent demonstrates good judgement. That needs evaluation on real tasks.

## Licence

MIT. See [LICENSE](LICENSE).
