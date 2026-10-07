# Project Shaping

Project Shaping helps a repository clearly represent **what the project is, what it is becoming, and how someone should work inside it**.

It is useful:

- when an idea is becoming a project
- during fast-moving development
- after a productive but messy sprint
- before release
- during long-term maintenance
- when adopting an established repository
- when making an existing project easier for humans and autonomous agents to inherit

The purpose is not standardization for its own sake.

The purpose is to make the project **legible, coherent, navigable, current, and recognizably itself**.

A successful shaping pass should leave a project feeling **more like itself, only easier to understand and continue**.

---

# The Shaping Posture

Enter the project like a thoughtful maintainer joining an existing body of work.

The repository has already learned things.

Your job is to understand those things, help important knowledge find the right home, reduce avoidable ambiguity, and preserve what gives the project its identity.

This is not an AI coding workflow. It describes **sensible stewardship under velocity and autonomous labor**: enter like a thoughtful maintainer, understand what the project has learned, and help its representation catch up without flattening it.

A useful shaping posture is:

### Observe before interpreting

Read enough of the project to understand its existing grammar before deciding what should change.

### Preserve useful identity

Project-specific weirdness, unconventional architecture, historical scars, and informal working practices may exist for good reasons.

Understand them before normalizing them.

### Prefer trustworthy context

Useful, current context is more valuable than exhaustive context.

A repository should make it reasonably clear which information represents current reality, intended direction, active exploration, and history.

### Clarify uncertainty

When evidence disagrees, identify the disagreement clearly.

Use evidence to narrow uncertainty and involve the project owner when resolving it would require intent rather than observation.

### Improve proportionally

Prefer interventions whose value exceeds their disruption.

A shaping pass should make ordinary work easier, not create a second project devoted to organizing the first one.

### Leave the next worker better equipped

Useful discoveries should survive the current conversation or agent session.

The next competent worker should benefit from what was learned without requiring private context.

---

# Shaping Across a Project's Life

The same philosophy applies throughout a project's life, but the emphasis changes.

## Early Projects

When little implementation exists, shaping is primarily about **discovering latent shape**.

Work with the user to understand:

- what the project is
- why it should exist
- what experience it should create
- major conceptual systems
- technical direction
- constraints
- unusual quality priorities
- non-goals
- unknowns
- project taste
- what could be technically correct while still feeling wrong for this project

Do not reduce this to feature collection.

Examples often reveal principles.

Follow them.

Distinguish:

- an example from a rule
- a preference from a constraint
- a current idea from project identity
- genuine uncertainty from a decision that simply has not been made yet

The aim is to capture enough of the user's model that future workers can make coherent decisions in situations nobody explicitly specified.

---

## Active Projects

During rapid development, shaping becomes partly archaeological.

Ask:

> What has this project learned by being built?

Look for:

- architecture that evolved naturally
- temporary systems that proved useful enough to stay
- repeated primitives appearing across unrelated features
- terminology that no longer describes the implementation well
- workflows that became normal without being documented
- briefs whose conclusions quietly became reality
- project taste visible in repeated choices
- assumptions that are still written down but no longer obviously true

Fast development naturally creates sediment.

That is not a failure.

Shaping periodically lets the repository catch up with what the work has discovered.

---

## Release and Maintenance

As a project matures, shaping increasingly protects **legibility and durability**.

A capable newcomer should be able to discover:

- what the project currently supports
- what remains experimental
- how to build, run, test, debug, package, and release it where relevant
- which systems are foundational
- where canonical knowledge lives
- what can safely change
- what assumptions deserve extra care
- what old material remains valuable history
- what no longer represents the project

A mature project should be able to stand on its own feet without constantly summoning its original developer.

---

## Adopted or Established Projects

When entering a repository you did not create, learn its existing organizational grammar first.

If its conventions are understandable, useful, and actively maintained, work with them.

The broader project structure framework is an organizing language and fallback—not a reason to remodel a functioning repository into a preferred template.

Sometimes the best shaping pass is small.

---

# Read the Repository as Evidence

A repository contains different kinds of evidence:

- source code
- runtime behavior
- tests
- configuration
- scripts
- README
- AGENTS
- design documents
- briefs
- comments
- TODOs
- naming
- folder structure
- build and release workflows
- historical implementation artifacts

Different artifacts tell you different things.

Current implementation is strong evidence of **current implementation reality**.

It is not automatically proof of **intended direction**.

Likewise, a design document may strongly express intended direction without proving that a divergent implementation is mistaken.

If a TDD specifies WebSockets while the implementation now uses SSE, several explanations are possible:

- SSE intentionally won
- SSE is experimental
- the TDD is stale
- implementation drifted from intended architecture
- a temporary compromise became permanent
- both approaches remain valid in different contexts

The discrepancy itself is useful information.

Treat the repository as evidence to understand, not an argument where one artifact must automatically defeat another.

---

# Understand What Kind of Knowledge You Are Looking At

A useful shaping pass distinguishes several kinds of project knowledge.

## Current Truth

What is factually true of the project now.

Examples:

- the application currently uses Tauri
- these tests run in CI
- Linux builds currently succeed

## Intent

What the project is trying to preserve or become.

Examples:

- Linux is a first-class platform
- interactions should feel instantaneous
- compatibility matters more than framework purity

## Working Context

Information useful to active or exploratory work.

Examples:

- three rendering strategies are currently being compared
- this subsystem is undergoing a rewrite

This often belongs in `docs/briefs/`.

## Archaeology

Historical information that is no longer current but still explains something important about the project.

An old comment explaining an ugly compatibility workaround may prevent a future worker from confidently "fixing" deliberate behavior.

Useful history deserves to remain understandable as history.

## Residue

Information that no longer helps someone correctly understand or maintain the project.

Examples:

- TODOs for removed systems
- setup instructions for tooling that no longer exists
- comments confidently describing behavior that changed long ago

Good shaping distinguishes archaeology from residue rather than treating age itself as a problem.

---

# Trajectory Cleanup

Trajectory Cleanup reconciles the project's accumulated representation with what the project has actually become.

It may reveal:

- stale or conflicting comments
- outdated documentation
- old terminology
- obsolete assumptions
- duplicated project knowledge
- dead references
- temporary names that became permanent
- architectural drift
- undocumented evolution
- working practices that never reached documentation
- important conclusions trapped in old briefs

The interesting question is not merely:

> What is outdated?

It is:

> What changed, what did the project learn, and what should now represent that knowledge?

A divergence can represent stale documentation, implementation drift, deliberate evolution, a local exception, or an unresolved design decision.

Shaping makes that distinction visible.

---

# Look for Emerging Structure

A shaping pass should look for discoveries as actively as it looks for mess.

Projects often invent useful structure before anyone names it.

Examples:

- several features independently use the same mathematical primitive
- multiple interfaces converge on the same interaction rule
- a local helper quietly becomes infrastructure
- several briefs imply the same UX principle
- one compatibility technique becomes a general strategy
- repeated implementation choices reveal a technical preference

These may represent **emergent project knowledge**.

Surface them when useful.

Not every repeated pattern deserves promotion.

The question is whether the project has learned something durable enough to make explicit.

---

# Preserve Project Taste

Project taste should normally live beside the domain it influences.

For example:

- technical taste → TDD or technical-design equivalent
- product and UX taste → PDD or product-design equivalent
- game/player taste → GDD or game-design equivalent
- research taste → research-design document
- agent behavior taste → agent-design document

A good design document explains enough reasoning that future workers can understand not only:

> What was chosen?

but also:

> What kinds of decisions feel native to this project?

This matters increasingly as implementation becomes autonomous.

The goal is not to specify every future decision.

It is to preserve enough project identity that unfamiliar decisions can still be made coherently.

---

# Use the Existing Documentation Structure

Use the project's established documentation structure; where this framework established it, see *Agentic Project Startup*.

When following this framework, a common shape is:

```text
README.md
AGENTS.md

docs/
├── TDD.md / equivalent
├── GDD.md / PDD.md / equivalent
├── STATUS.md / equivalent
├── briefs/
└── reference/
```

These names represent **roles**, not mandatory filenames.

Consistency is valuable, especially across projects that share an ecosystem or maintainer, but the underlying information architecture matters more than mechanically reproducing a template.

Project-specific documentation spaces are welcome when they make a meaningful body of knowledge easier to discover. Shape them around the project rather than trying to fit every kind of information into `reference/`.

## Technical Design

`TDD.md` or its equivalent is the durable home for the project's technical shape.

Depending on the project, another name may fit better:

- `ARCHITECTURE.md`
- `SYSTEM_DESIGN.md`
- `TECHNICAL_DESIGN.md`
- a research-oriented technical document
- an established project-specific equivalent

What matters is that deeper technical truth and technical intent have a predictable canonical home.

## Product, Game, Research, or Experience Design

`GDD.md`, `PDD.md`, or their equivalent captures the non-technical design domain that matters to the project.

This may instead be:

- a research design document
- agent design document
- interaction design document
- protocol design
- creative direction document
- another project-native category

Choose the smallest set of core documents that cleanly represents the project.

## Project Status

`STATUS.md` or its equivalent is a lightweight current-state / known-work surface.

Think of it as the wooden tavern board near the entrance: useful issues, loose ends, warnings, maintenance work, or things somebody wanted to keep visible.

It reflects known work, not the complete universe of possible work. Work may begin, happen, and finish without ever appearing there.

Its role is orientation and memory, not process enforcement.

## Briefs / Artifacts

`docs/briefs/` is working memory. “Brief” and “artifact” refer to the same general class here: bounded, usually one-off documents worth preserving outside the current conversation or work session.

Implementation plans, investigations, research dumps, design explorations, reviews, handoffs, and other “make an `.md` with this” outputs can live here.

It is allowed to become somewhat messy. That is part of its job.

## Reference

`docs/reference/` holds durable supporting material that benefits from being independently addressable without becoming another primary design document.

Do not create documents simply to complete the pattern.

Documentation earns its place by improving understanding.

---

# Let Knowledge Earn Permanence

Information does not need to become permanent merely because it was discovered.

A healthy project lets repeated usefulness reveal where knowledge belongs.

## A finding happens once

Keep it local, report it, or place it in a brief.

## It becomes durable understanding

Promote it into the appropriate core document or reference material.

## It becomes a stable invariant

Where practical, encode it mechanically through:

- tests
- types
- schemas
- lint rules
- validation
- architectural checks
- build tooling

## A procedure becomes repeatedly useful

Make it reproducible through:

- a script
- task
- command
- tool
- reusable agent workflow

## Something stops being true

Let its representation evolve too.

Update, demote, archive, or remove it according to its remaining value.

The project should accumulate **useful structure**, not layers explaining why previous layers are wrong.

---

# Prefer Executable Knowledge Where It Fits

Some conventions are better expressed through the system than through reminders.

Formatting can live in formatting configuration.

Dependency reality can live in lockfiles.

Verification belongs in tests and CI.

Repeatable workflows may deserve scripts or task runners.

Architectural boundaries may sometimes be checked mechanically.

Documentation is most valuable for:

- intent
- reasoning
- tradeoffs
- exceptions
- taste
- non-obvious constraints
- navigation

When a failure repeats, ask where the durable improvement belongs.

Sometimes the right answer is documentation.

Sometimes it is tooling.

Sometimes it is code.

Sometimes the project simply needed one correction rather than a new permanent rule.

---

# Agent Instructions Are Part of the Environment

Files such as:

- `AGENTS.md`
- tool-specific project instructions
- repository rules
- reusable agent skills
- workflow prompts

shape worker behavior.

Treat them with the same care as other project infrastructure.

Good agent instructions are:

- current
- high-value
- appropriately scoped
- easy to navigate
- complementary to mechanical enforcement
- concise enough to remain useful

A useful instruction file often acts as a map toward deeper context rather than trying to contain the entire project.

Because agents may follow instructions confidently, trustworthy instructions are more valuable than exhaustive ones.

---

# Prefer Freshness and Trust

A repository benefits when workers can trust what presents itself as current.

Missing information can be investigated.

Misleading authoritative-looking information may quietly steer work in the wrong direction.

This does not mean erasing history.

It means helping readers distinguish:

- current reality
- intended direction
- active exploration
- useful archaeology
- residue

Keep authority aligned with relevance.

---

# Shape With Proportion

Shaping should improve the project without becoming the project.

Before a significant intervention, consider:

- implementation blast radius
- import and build consequences
- external links
- tooling assumptions
- contributor expectations
- release risk
- historical value
- whether the increased clarity justifies disruption

A good shaping diff is usually **boring, understandable, and proportionate to the confusion it resolves**.

Structural elegance is useful when it makes work easier.

Symmetry by itself is not a feature.

---

# Findings During a Shaping Pass

A useful shaping pass can organize findings into three broad categories.

## Safe Normalization

Low-risk improvements whose intended outcome is clear.

Examples:

- broken internal links
- obvious dead references
- missing navigation
- clearly misplaced documentation
- unambiguous factual drift

When shaping work is authorized, these are good candidates for direct improvement.

## Proposed Reconciliation

Places where choosing an interpretation requires project intent.

Examples:

- implementation and design documents disagree on architecture
- a supported platform appears to have become ceremonial
- two canonical documents describe different behavior
- a temporary system appears to have become permanent

Present the evidence clearly and let the relevant owner resolve the uncertainty.

## Interesting Emergence

Patterns that may represent newly discovered project structure.

Examples:

- repeated abstractions
- consistent undocumented taste
- organically converged workflows
- newly important primitives
- formerly separate systems becoming one conceptual domain

Surface these as opportunities rather than defects.

The best shaping passes discover useful things the project did not yet know how to say about itself.

---

# Scope and Authority

Risk and authority are different questions.

A change can be safe without being relevant to the current task.

When shaping itself is the task, improve what falls naturally within that scope.

During an unrelated implementation task, noticing a shaping opportunity does not automatically turn the session into repository cleanup.

Record or surface useful observations when appropriate and keep the assigned work coherent.

This lets shaping remain available without becoming ambient churn.

---

# When Working With the User

**Inspect before asking when there is something to inspect.**

Recover ordinary repository facts from the repository.

Questions are most valuable for things the project cannot reliably tell you:

- intent
- taste
- priorities
- tradeoffs
- ambiguity
- non-goals
- whether an observed divergence was deliberate

If the reason for the shaping pass is already stated, use it.

If the project is empty or the trigger is genuinely unclear, one useful opening question may be:

> What made you want to shape this project now?

Do not turn shaping into a fixed interview.

Follow useful threads.

When an example seems important, ask what makes it feel right.

When something feels wrong to the user, investigate what broader principle that reaction exposes.

One particularly useful question is:

> What could be technically correct here and still feel wrong for this project?

Hunt for **latent taste**, not merely requirements.

---

# Context Density

More information is not automatically better information.

Aim for context that is:

- trustworthy
- well placed
- easy to navigate
- appropriately scoped
- dense with useful signal

Consider both:

> What would I wish existed if I inherited this project six months from now with no conversation history?

and:

> What would become annoying if every worker had to consume it repeatedly?

Prefer maps toward deeper context over giant mandatory context bundles.

**Good context beats maximum context.**

---

# Completion Standard

A shaping pass does not need to make the repository perfect.

It should leave the project meaningfully easier to understand and continue.

A competent newcomer should be increasingly able to answer:

- What is this?
- What matters here?
- Where is deeper project truth?
- What state is the project currently in?
- What conventions already exist?
- What is temporary or exploratory?
- What assumptions deserve care?
- How is work verified?
- Where does project-specific taste live?
- What remains uncertain?
- When should I investigate, and when should I ask?

Most importantly:

> The next worker should not need the shaping agent's private context in order to benefit from what the shaping agent learned.

Leave useful knowledge in the project or clearly surface what still requires human direction.

---

# Voices from the Field

These are distilled perspectives commonly expressed by people building, maintaining, and increasingly delegating software work.

They are not laws, and they do not necessarily agree.

Treat them as experienced voices in the room.

> “A repository becomes easier to trust when you know where the current truth lives.”
>
> — Experienced maintainers

> “Give the worker a map, not the entire library every time it walks through the door.”
>
> — Developers working with large agentic repositories

> “The first patterns you establish matter disproportionately. Agents tend to reproduce the shape they inherit.”
>
> — Agent-heavy developers

> “If a convention genuinely matters, making it deterministic is often kinder than asking every future worker to remember it.”
>
> — Tooling-minded developers

> “Good documentation is a handoff between stages of thinking, not only a record of what happened.”
>
> — Developers using agents across research, design, and implementation

> “The best autonomous work has good boundaries and some way for the worker to discover whether it succeeded.”
>
> — Experienced developers delegating to agents

> “Moving quickly creates sediment. The useful question is which parts became geology.”
>
> — Fast-moving developers

> “Sometimes you should tell the model what you want and let it cook.”
>
> — Vibe coders

> “Not every imperfection needs a framework. A project should cost less to understand after the framework than before it.”
>
> — Developers who have lived through too many methodologies

> “A repository can work perfectly and still become much nicer to inherit.”
>
> — Maintainers everywhere

These perspectives can inform the work.

**This project, however, needs its own direction.**

Let its evidence, intent, people, and emerging identity have the final word.