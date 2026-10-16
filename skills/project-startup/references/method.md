# Agentic Project Startup

You are initializing, organizing, or onboarding into a project.

Establish a project structure that is:

- predictable
- human-readable
- agent-readable
- easy to navigate
- resistant to stale context
- useful without any particular AI tool or conversation history

The repository should teach a competent newcomer how to understand and work inside it.

A capable autonomous agent dropped into the project should be able to find the **good, current context**, understand what is authoritative, and behave like a respectable worker rather than reconstructing project intent from scattered files and source code.

At the same time, a human browsing the repository directly should find an organized, recognizable project rather than an agent-specific knowledge dump.

This is not an AI coding workflow. It is **repository legibility under autonomous labor**. If agents disappeared tomorrow, it would still describe a clean, pleasantly organized engineering style.

---

# Structural Philosophy

Use **strong conventions for the core structure** and allow personality inside it.

The foundational structure should be highly consistent between projects. Someone familiar with one project should be able to predict the important locations in another.

Prefer boring and obvious names for foundational files.

The bar is approximately:

> An autistic person who likes predictable systems should be pleased.

Individual briefs, references, subsystem names, and project-specific material can be much more expressive.

Standardize the **organizational language**, not the substance.

The structure should answer:

> What kind of information am I looking for, and where would information like that normally live?

It should not force every project to describe itself using identical categories.

---

# Root

## `README.md`

The user-facing face of the project.

It should help someone understand things such as:

- what the project is
- why it exists
- what it does
- what is notable about it
- how to install, run, or use it where relevant
- what environments it supports where relevant
- where someone should look next

README is the project's front door.

It may summarize deeper design or technical information, but it does not need to become the canonical home for it.

---

## `AGENTS.md`

The onboarding layer for:

- autonomous agents
- coding agents
- maintainers
- contributors
- technical explorers

It should help answer:

> What am I standing inside, where is everything, how do I work here, and what should I know before touching it?

Useful contents may include:

- concise project identity
- repository map
- important systems and directories
- development commands
- build/test/verification instructions
- terminology
- important conventions
- important invariants
- documentation map
- where deeper or canonical knowledge lives
- practical guidance for working responsibly in the repository

`AGENTS.md` should primarily **orient and route**.

Think of it as the map handed to a competent worker when they enter the project.

It should make deeper information easy to find rather than attempting to reproduce all of it.

---

# `docs/`

`docs/` contains deeper internal project knowledge.

Keep its root conceptually clean.

Durable, important project documents live directly inside it, while narrower or supporting material can live in predictable subfolders.

A common shape is:

```text
PROJECT/
├── README.md
├── AGENTS.md
│
├── docs/
│   ├── TDD.md / equivalent
│   ├── GDD.md / PDD.md / equivalent
│   ├── STATUS.md / equivalent
│   ├── briefs/
│   └── reference/
│
└── ...
```

The filenames above illustrate **information roles**, not mandatory forms.

A project's exact core documents should reflect what the project actually needs to understand itself.

`docs/` may also grow project-specific semantic spaces such as `media/`, `captures/`, `benchmarks/`, `external/`, or whatever else gives a meaningful body of project knowledge an obvious home.

These are natural extensions of the structure, not exceptions to it.

---

# Core Project Documents

Most projects benefit from a **small number of primary documents** that partition durable project knowledge into understandable domains.

Often this is roughly two design documents, with a lightweight current-state surface when useful.

The goal is not to fill out predefined templates.

The goal is to give the project's important kinds of knowledge obvious canonical homes.

A useful core document should answer a question that is important enough to deserve a durable answer.

---

## Technical Design — `TDD.md` / equivalent

A technical-design document is the durable home for the project's **technical model of itself**.

Its job is not to contain a mandatory list of technical topics.

Its job is to help a technically capable worker understand how the project is built, what technical decisions matter, and what constraints shape future implementation.

Depending on the project, relevant material might include:

- architecture
- runtime model
- important subsystem relationships
- platforms and compatibility
- data or protocol design
- performance expectations
- dependencies and build strategy
- important implementation patterns
- testing or verification strategy
- distribution or deployment
- technical workflows
- technical tradeoffs
- technical taste

A project may call this:

- `TDD.md`
- `ARCHITECTURE.md`
- `SYSTEM_DESIGN.md`
- `TECHNICAL_DESIGN.md`
- something project-specific

The exact name matters less than having a **predictable technical-design home**.

For new projects, prefer the common convention unless another name genuinely communicates the role better.

Technical decisions are allowed to be opinionated.

Choices such as native versus web, Linux support, architectural primitives, compatibility philosophy, or an asset pipeline are part of a project's technical identity when they meaningfully shape the system.

---

## Experience / Domain Design — `GDD.md`, `PDD.md`, or equivalent

Many projects need a second durable document concerned less with *how the system is built* and more with **what the system is trying to be** in its relevant domain.

The appropriate shape depends heavily on the project.

For a game, this may be a `GDD.md`.

For an application, it may be a `PDD.md`.

For a research project, it may be a research-design document.

For an agent system, it may be an agent-design document.

For something stranger, another category may fit better.

This document may capture things such as:

- intended experience
- behavior
- interaction philosophy
- mechanics
- workflows
- product principles
- research methodology
- agent behavior
- aesthetic direction
- quality priorities
- constraints
- project-specific taste
- what technically valid implementations could still get wrong

The role is:

> Preserve the durable non-technical or domain-specific intent that future implementation should continue to understand.

Do not force unrelated projects into GDD/PDD semantics merely because those names are common.

---

## Research Design — possible equivalent

When research itself is a major project domain, its core design knowledge may deserve a dedicated home.

That document might contain whatever is necessary to understand the research direction, such as:

- questions
- hypotheses
- theory
- mathematical framing
- methodology
- experiments
- evaluation
- observations
- uncertainties
- open directions

The important distinction is that **research reasoning itself is part of the project's design**, rather than merely supporting technical implementation.

---

## Agent Design — possible equivalent

When autonomous or intelligent agents are part of the thing being built, agent behavior may deserve its own core design home.

Relevant knowledge might include:

- roles
- capabilities
- boundaries
- tools
- state and memory
- trust
- planning/execution behavior
- escalation
- evaluation
- agent-to-agent relationships

Do not create an agent-design document merely because agents are being used to develop the project.

Use one when agent behavior is itself part of the project's design.

---

# Choosing Core Documents

Choose the smallest set of documents that gives the project's important durable knowledge clear homes.

Common shapes might include:

```text
Game / Mod
TDD.md / equivalent
GDD.md / equivalent
```

```text
Application
TDD.md / equivalent
PDD.md / equivalent
```

```text
Agentic Product
TECHNICAL_DESIGN.md
AGENT_DESIGN.md
```

```text
Research System
RESEARCH_DESIGN.md
TDD.md / equivalent
```

But these are examples, not templates.

Another project may have one unusually rich design document.

Another may genuinely need three.

What matters is that the partition makes conceptual sense.

Core documents are **categories of durable project understanding**, not forms that need to be completed.

---

# Taste Belongs With Its Domain

Do not create a separate taste document by default.

The project's taste, values, constraints, and characteristic decisions should live beside the systems they govern.

For example:

- technical taste → technical-design document
- player/game taste → game-design document
- product/UX taste → product-design document
- research taste → research-design document
- agent behavior taste → agent-design document

These are mappings of **intent**, not filenames.

This is especially important in agentic development.

The core documents should preserve enough project reasoning that an autonomous worker does not merely produce technically valid work—it can make decisions that still feel native to the project.

Do not reduce durable project documents to dry specification sheets if important reasoning or taste would be lost.

---

# Workflows That Span Domains

Place information according to **what part of the project it helps someone understand**.

A single real-world workflow may therefore appear from different perspectives in different documents.

For example, an asset system may have:

**Experience or creative intent**

> Assets should use restrained animation, chunky silhouettes, and avoid photorealistic materials.

This belongs with the project's relevant experience or creative design knowledge.

**Technical implementation**

> Assets are authored in Blender, exported as glTF, processed through the conversion pipeline, and validated during the build.

This belongs with technical design.

The goal is not to force every fact into exactly one semantic bucket.

The goal is to give each important idea a clear canonical context and avoid maintaining conflicting copies of the same instruction.

Cross-reference when that improves understanding.

---

# Current-State Board — `STATUS.md` / equivalent

Some projects benefit from an obvious place to glance at **known work, loose ends, and things worth keeping visible**.

`STATUS.md` is a useful default name for this role.

Think of it as the repository's **wooden tavern board**: a place where useful work, warnings, and unfinished business can be pinned up so the next person wandering through knows what is around.

It might contain things such as:

- known issues
- unfinished systems
- maintenance work worth returning to
- regressions
- useful warnings
- unresolved items
- follow-ups
- areas currently receiving attention
- ideas concrete enough to remember
- bits of work someone may want to pick up later

The board reflects **known work**, not the complete universe of possible work.

A developer might notice an idea, implement it, test it, and commit it without the task ever appearing on the board.

An autonomous worker might discover useful work through the code, a user request, a brief, testing, or ordinary exploration.

That is normal.

`STATUS.md` simply gives things worth remembering somewhere predictable to remain visible.

It can be sparse.

It can contain work someone intends to get to eventually.

It can coexist with spontaneous development, active experimentation, issue trackers, roadmaps, or other project workflows without needing to represent all of them.

Its role is primarily **orientation and memory**.

It may resemble a lightweight maintenance board, but it does not need to become an exhaustive tracker, queue, changelog, roadmap, or copy of the design documents.

Some projects may already express this role through another established mechanism.

Others may not need a dedicated status surface at all.

For new projects where this role is useful, `docs/STATUS.md` is a predictable default.

---

# `docs/briefs/` — Briefs / Artifacts / Working Memory

`docs/briefs/` is the project's working-memory space.

**Briefs and artifacts mean the same thing here.** Different tools and agent harnesses may use either term for bounded, usually one-off documents created to preserve useful work outside the current conversation or session.

This includes things such as:

- implementation plans
- feature briefs
- research notes
- investigations
- architecture reviews
- optimization plans
- experiments
- red-team passes
- migration notes
- handoffs
- temporary agent documents
- exploratory design work
- essentially any “make an `.md` file with this” output worth keeping

The folder does not need to remain pristine.

A project may have a handful of briefs/artifacts or dozens. They may be organized carefully or somewhat free-range.

That is acceptable.

The important distinction is:

> Briefs / artifacts are working context, not automatically canonical project truth.

If something inside one becomes durable project understanding, that knowledge can later find its appropriate canonical home.

---

# `docs/reference/` — Durable Supporting Knowledge

`docs/reference/` contains useful supporting material that benefits from being independently addressable without becoming one of the project's primary design documents.

Examples might include:

- compatibility information
- protocols
- mathematical derivations
- benchmark methodology
- reverse-engineering notes
- file formats
- hardware information
- terminology
- external API behavior
- detailed subsystem references

The exact contents depend on the project.

The role is:

> Preserve durable supporting knowledge that someone may intentionally look up.

Do not use reference material simply to avoid organizing the core documents.

For an established project with another coherent reference convention, preserve that convention rather than creating a duplicate hierarchy.

---

# Canonicality

Important information should normally have one clear authoritative context.

Other documents may summarize it, link to it, or explain why it matters from another perspective.

For example:

- README presents the project publicly.
- AGENTS routes a worker through the repository.
- a technical-design document contains deeper technical intent.
- an experience/domain-design document preserves what the project is trying to be.
- a status surface preserves useful currently-relevant loose ends when the project benefits from one.
- a brief explores one bounded piece of work.
- reference material supports deeper lookup.

These are **roles**, not rigid ownership laws.

The important property is that someone can reasonably determine:

> Where should I look for the best version of this information?

Prefer references and concise summaries over independently maintained competing truths.

---

# Documentation vs Reality

Source code and documentation can disagree.

Neither automatically wins.

A mismatch may mean:

- documentation is stale
- implementation is incomplete
- implementation accidentally violated design intent
- a broad principle was intended more narrowly
- a previous change was incorrect
- the project deliberately evolved
- a temporary compromise became permanent
- the difference is valid in context

The discrepancy itself is useful information.

When a meaningful conflict is discovered:

1. identify the discrepancy
2. gather enough evidence to explain it
3. determine whether the current task can proceed safely
4. raise questions of project intent when needed

Current implementation is evidence of current implementation reality.

Design documentation is evidence of intended direction.

Use both to understand the project rather than automatically forcing one to conform to the other.

---

# Editing Core Documentation

Treat core documents as relatively stable project knowledge.

A worker should approach them as **shared project understanding**, not disposable scratchpads.

When work reveals:

- possible documentation drift
- a new architectural implication
- a design contradiction
- an emerging project principle
- a decision requiring owner intent

use the amount of authority appropriate to the task.

That may mean:

- updating an obviously stale factual statement
- improving organization without changing meaning
- flagging a discrepancy
- recording investigation in a brief
- proposing a core-document change
- asking the user to resolve a meaningful ambiguity

Core documents may naturally evolve when documentation maintenance is part of the task or implementation has intentionally changed the project.

The important goal is that changes to durable project understanding should be **deliberate and legible**.

---

# Information Placement

When new information appears, first ask:

> What kind of understanding does this give someone?

A useful default map is:

- public project understanding → `README.md`
- worker/repository orientation → `AGENTS.md`
- durable technical understanding → technical-design document
- durable game/product/research/agent/domain intent → appropriate core design document
- known work or loose ends worth keeping visible → `STATUS.md` or equivalent, when useful
- bounded or exploratory work → `briefs/`
- durable independently useful supporting information → `reference/`

These are default destinations, not semantic laws.

An established project may already have an obvious equivalent.

A piece of information may also touch multiple domains; keep one canonical explanation and cross-reference where useful.

Not every active task needs to be recorded in documentation before work begins.

If nothing fits naturally, first ask whether the information needs permanent documentation at all.

Do not create another Markdown file merely because information exists.

---

# General Standard

Prefer:

**few canonical documents, strong responsibilities, predictable locations, useful working memory, current context, and visible project intent.**

The core structure should be familiar enough that moving between projects feels easy.

The contents should remain flexible enough that each project can express what it actually is.

The structure should support work rather than requiring work to perform the structure.

The repository should remain coherent if every AI tool disappeared tomorrow.

It should also be structured well enough that, if the human disappeared for a day and a competent autonomous worker was given a bounded task, that worker could enter the repository, understand the environment, find the right context, respect the project's taste, notice uncertainty, and do respectable work without requiring constant supervision.