---
type: skill
title: Compare thinkers
description: "Use when asked how two or more thinkers — any era, any tradition — relate on a question: what Hume and Parfit each say about personal identity, where Nāgārjuna and Wittgenstein meet on the limits of language. Walks the graph problem-first so classical and modern thinkers meet on the problem page rather than in the agent's memory, tabulates their positions with locators, names the exact points of agreement and divergence as logical observations, and reports any published comparison rather than inventing one."
timestamp: 2026-09-25T18:30:00Z
depends_on: [using-the-brain-implant.md, steelman-a-position.md]
export: agent-skill
---

# Compare thinkers

A language model will happily compare any two thinkers from memory, and the
comparison will be fluent, roughly right, and unsourced. The graph exists so
that the comparison can instead be *read off*: the
[problem](../knowledge/problems/index.md) page is the room in which every
thinker who addressed the question is already listed with the position they
took and the locator ([knowledge](../knowledge/index.md), *problem-centric*).
The skill is to use the room.

## Steps

### 1. Find the shared problem(s)

From each thinker's page (*Problems addressed*), intersect the lists. If the
user named a topic rather than a problem, `brain_search` the problems
branch for it. If the thinkers share no problem page, say so — the honest
answer is often "they did not address the same question, and here is the
nearest each came" — and do not force a comparison.

### 2. Tabulate

For each shared problem: thinker · position (linked) · the work and locator
where they take it · the century. One row per thinker. If a thinker changed
position, two rows with dates. Everything in the table is attributive and
carries its receipt ([How claims are graded](../conventions/how-claims-are-graded.md)).

### 3. Steelman each cell

Run [steelman-a-position](steelman-a-position.md) at the depth the user
needs — a paragraph per thinker for a quick comparison, the full skill for a
serious one — so that each thinker's view is stated as they would state it,
in their sense of the terms. Mark every place where two thinkers use the
same word in different contract senses; that is where most apparent
disagreements and most apparent agreements dissolve.

### 4. Name agreement and divergence as logic

For each pair: do their positions entail the same answer, incompatible
answers, or answers to slightly different questions? Where incompatible,
which premise or which term sense makes them so. This is a logical
observation on cited claims and may be stated in the implant's voice
([manifest](../vision/manifest.md), G4). "Hume's bundle and Parfit's
reductionism both deny a further fact of identity; they diverge on whether
what matters survives without it" is such an observation, given the
locators.

### 5. Report published comparisons

Check each thinker's *In dialogue with* and *Reception* sections and the
problem page for scholars who have compared these thinkers already. Report
their comparisons, attributed. Where a later thinker explicitly responded to
an earlier one, the citation that establishes the response goes in the
table.

### 6. Deliver

The table, the divergence map, the published comparisons, and — if the
thinkers share no page yet or a thinker lacks a page — a line to
`todo/open.md`. No ranking, no "who was right", no "who was more
influential" unless a cited source says so and is named.
