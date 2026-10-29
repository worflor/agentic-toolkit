# Agentic Toolkit

**Reusable skills for developers working with coding agents.**

Coding agents can produce a lot of work quickly. Understanding a project, respecting its intent, spotting weak assumptions, and keeping the result maintainable are different challenges.

Agentic Toolkit collects a few practical ways to handle those challenges. Whether you're working on a side project, an established app, a library, a game, or a research tool, pick the skill that fits the job.

The skills follow the [Agent Skills specification](https://agentskills.io/specification). Install them in a supported coding agent, or read through the methods yourself.

## Find the right skill

| Skill | When it helps | What it does |
| --- | --- | --- |
| **[Superfan](skills/superfan/SKILL.md)** | You want someone to look closely at an idea, experience, or project and challenge what you might have stopped noticing. | Gets unreasonably invested in the details, follows the interesting connections, and gives you a considered opinion. |
| **[Project Startup](skills/project-startup/SKILL.md)** | You're starting something new, taking over an existing project, or losing track of where its knowledge lives. | Gives important context and decisions sensible places to live, without making every project look the same. |
| **[Project Shaping](skills/project-shaping/SKILL.md)** | The project has evolved, but its plans, assumptions, or documentation haven't quite caught up. | Works out what has changed, what the project has learned, and what needs to be brought up to date. |
| **[Anti-Slop](skills/anti-slop/SKILL.md)** | Explanations, notes, or instructions are piling up and making the work harder to follow. | Clears away repetition and stale clutter while keeping useful reasoning and personality intact. |

Use a skill on its own, or bring its perspective into another task. Superfan can make research more revealing; Anti-Slop can help keep a long stretch of work from leaving a mess.

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

Working from a local clone? Run `npx skills add . --skill superfan` from the checkout.

## Give a skill a job

Once installed, talk to your agent like you normally would. You don't need to explain the skill back to it:

> I'm pretty sure this API makes sense only to me. **Superfan** it before I call it stable.

> This started as a weekend project, and now people actually want to contribute. Can **Project Startup** help me sort out the repo?

> We've rebuilt the backend twice, and half the docs still describe the old version. Give it a **Project Shaping** pass.

> These docs read like five agents took turns summarising each other. Please **Anti-Slop** them.

You can also bring a skill into another task:

> We're torn between building our own plugin system and adopting an existing one. Research the options **with Superfan**. I want to know what we'll regret later.

## What the skills have in common

The skills have different personalities, but a few things matter to all of them:

- **Understand before changing.** Look at the actual project, not just its introduction or the latest conversation.
- **Know what the evidence shows.** Plans, code, tests, and actual user experience can tell different stories.
- **Keep what makes a project itself.** A strange convention or bit of personality might be there for a good reason.
- **Prefer proportionate work.** Keep useful context easy to find, changes focused, and process lighter than the value it provides.
- **Be clear about uncertainty.** Say what was inspected or verified, what was inferred, and what still needs a decision.

## Explore and contribute

Each skill lives in `skills/<name>/SKILL.md`, with deeper guidance under `references/` where needed. The longer [Project Startup method](skills/project-startup/references/method.md) and [Project Shaping method](skills/project-shaping/references/method.md) are available for readers who want the full approach.

See [AGENTS.md](AGENTS.md) for contribution guidance. If you're adding a skill, give it a clear job and a character of its own.

To validate skill metadata, local links, and the validator's tests:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

These catch packaging and link mistakes. To see how a skill actually performs, try it on real work.

## Licence

MIT. See [LICENSE](LICENSE).
