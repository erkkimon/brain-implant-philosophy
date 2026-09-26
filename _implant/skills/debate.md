---
type: skill
title: Debate
description: "Use when the user wants to practise defending a position, wants their argument's holes found, or wants to work out the most defensible position on a question. The user picks the format (sparring partner, hole-poker, or search for the most defensible position) and — explicitly — how dirty the agent may fight, from strict logos to every technique in the catalogue; the agent argues within those limits, keeps a cited scorecard of every move, and at the end discloses everything it did and where the user's position held or gave."
timestamp: 2026-09-26T09:54:50Z
depends_on: [using-the-brain-implant.md, spot-persuasion-and-bias.md, analyse-an-argument.md, steelman-a-position.md]
export: agent-skill
---

# Debate

The implant does not tell the user what is true. It can, however, be the
opponent that finds out how well the user's position survives contact — and
it can do so with the whole catalogue of persuasion techniques, or none of
them, as the user chooses ([journal](../journals/archive/2026/09/2026-09-25.md)). The limits
are set before the first move, every move is logged against its page, and
the log is disclosed at the end. A debate here is a training exercise with
a receipt, never a trick.

## Setup — three choices, all the user's

### 1. Format

- **Sparring** — the user defends a position; the agent attacks it, in
  rounds, with the user replying.
- **Hole-poking** — the user presents an argument; the agent finds every
  weak premise, inference and hidden assumption, without proposing a
  replacement. Runs [analyse-an-argument](analyse-an-argument.md) first.
- **Most defensible position** — the user names a question; the agent
  takes each catalogued position in turn ([problems](../knowledge/problems/index.md)
  → its positions), steelmans it ([steelman-a-position](steelman-a-position.md)),
  attacks it with the strongest cited objections, and reports which
  objections each position survived — as a map, not a ranking. The user
  picks.

### 2. How dirty

Present the same menu as [write-persuasively](write-persuasively.md), from
[persuasion](../knowledge/persuasion/index.md), with each technique's
classification note from the literature, and the three shortcuts:

- **Logos only** — arguments, evidence, reconstructions; the agent may not
  appeal to emotion, authority, or the user's person.
- **Classical** — plus ethos and pathos used openly.
- **Everything** — every technique catalogued, including every one the
  literature classes as a fallacy. Say plainly what this means: the agent
  may strawman, shift the burden, appeal to consequences, load questions,
  and so on, and will do it on purpose.

The user may build a custom list. Record the choice verbatim.

### 3. Side and stakes

Which position the agent argues, and whether the agent should concede
points it is given (realistic) or never concede (stress test). The agent
never argues a position it cannot source: its case is built from the
position page's *case for* and the argument pages, cited
([Every claim carries its receipt](../conventions/every-claim-carries-its-receipt.md)).

## During

- **Every move is logged** as it is made, in a scorecard the user does not
  see until the end: round · move · technique or argument used (linked) ·
  the source it was drawn from. A move that uses a technique not on the
  allowed list is not made.
- **The agent's arguments are the literature's, not its own.** Objections
  are the cited ones from the argument and position pages; the agent may
  combine and sharpen them but says, in the log, whose they are.
- **The user's moves are analysed too**, with [spot-persuasion-and-bias](spot-persuasion-and-bias.md),
  into the same log — so the disclosure at the end shows both sides.
- **A hole found is named by premise.** "P2 assumes the contract sense of
  *knowledge*, but your example uses sense 3" is a hole; "that's weak" is
  not.

## Disclosure — at the end, always

1. **The scorecard**, both sides, every move linked to its page.
2. **Where the user's position held**: objections it answered, with the
   answer.
3. **Where it gave**: objections it did not answer, and which premise they
   attack. If the format was *most defensible position*, this becomes the
   map: positions × objections survived.
4. **What the agent did that the user should know**: every technique from
   the dirty list that was used, where, and the page that says how to
   answer it — so the user leaves able to recognise it next time from
   someone who does not disclose.

No verdict on who won and no verdict on which position is true. If the user
wants a number on how defensible their position now seems to *them*, offer
[estimate-a-credence](index.md) from the cognitive-tools implant; the
scorecard is the factor list.

## What never happens here

- A technique used that the user did not allow, or one used and not logged.
- An objection invented by the agent and presented as the literature's.
- Withholding the disclosure, or softening it.
- The agent's own view on the question, at any point, in any format.
