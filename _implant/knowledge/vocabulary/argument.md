---
type: article
about: concept
title: "Argument"
description: "A set of sentences (premises) offered as reasons for another sentence (the conclusion), distinguished here from explanation, assertion, and persuasion — the unit that logic evaluates and that the analyse-an-argument skill reconstructs."
tags: [vocabulary, logic]
timestamp: 2026-09-26T09:54:50Z
---

# Argument

## Normative definition (this implant)

An **argument** is a finite set of declarative sentences, one designated the
*conclusion* and the rest the *premises*, where the premises are offered as
reasons for accepting the conclusion. The relation between premises and
conclusion is what [logic](../methods/classical-logic.md) evaluates; whether
anyone is persuaded by it is a separate question handled under
[persuasion](persuasion-rhetoric-dialectic.md).

Why this definition: the implant's core skill
[analyse-an-argument](../../skills/analyse-an-argument.md) reconstructs prose
into numbered premises and a conclusion so that
`logic.py` can check validity mechanically. A
definition that conflates argument with persuasion would make validity
depend on audience response; a definition that conflates it with explanation
would make every causal account an argument. This sense is the one standard
in formal logic and in the reconstruction literature this implant follows.

Fixed 2026-09-25 ([journal](../../journals/archive/2026/09/2026-09-25.md)). The normative
choice is recorded as a decision, not a claim that other uses are wrong.

## Descriptive definitions

- **Formal logic (standard):** "a series of statements, called premises,
  together with a final statement, called the conclusion, where the premises
  are intended to provide support for the conclusion" (Copi, Cohen &
  Flage, *Introduction to Logic*, 14th ed., 2018, p. 5). This is the sense
  `logic.py` implements.
- **Informal logic / argumentation theory:** a broader unit that may include
  implicit premises, dialogical context, and pragmatic force. Van Eemeren
  and Grootendorst define an argument as "a verbal, social, and rational
  activity aimed at convincing a reasonable critic of the acceptability of a
  standpoint by putting forward a constellation of propositions justifying
  or refuting the proposition expressed in the standpoint" (*A Systematic
  Theory of Argumentation*, 2004, p. 1). This implant records such
  definitions when citing argumentation-theory sources but does not use them
  as the reconstruction target.
- **Ordinary usage:** often any disagreement or quarrel. This sense is
  excluded; when a source uses "argument" this way, the implant reports the
  ordinary sense explicitly.
- **Computer science / programming:** a value passed to a function. Excluded;
  no collision risk in philosophical context.

## Collisions

- **Argument vs. explanation.** An explanation offers reasons why something
  *is* the case; an argument offers reasons why something *should be
  believed*. Hempel distinguishes them by direction of fit: explanations
  assume the explanandum and seek causes; arguments assume the premises and
  seek to establish the conclusion (*Aspects of Scientific Explanation*,
  1965, pp. 335–336). Pages in [arguments](../arguments/index.md) are
  arguments in the normative sense; causal accounts cited on problem pages
  are explanations unless reconstructed as arguments.
- **Argument vs. persuasion.** A persuasive text may contain no argument
  (pure emotional appeal) and an argument may persuade no one. The
  distinction matters because [spot-persuasion-and-bias](../../skills/spot-persuasion-and-bias.md)
  inventories persuasion techniques separately from argument structure.
- **Argument vs. assertion.** A bare claim without premises is an assertion,
  not an argument. The implant's admission rule
  ([every claim carries its receipt](../../conventions/every-claim-carries-its-receipt.md))
  requires that knowledge pages ground claims; ungrounded assertions do not
  enter.

## Related terms

- [Validity](validity.md) — the property of an argument whose form guarantees
  that if the premises are true, the conclusion is true.
- [*Fallacy*](fallacy.md) — a pattern of reasoning classified as defective by # lint: allow
  some authority, cited with the classifier and the classification.
- [Knowledge](knowledge.md) — the epistemic state that arguments aim to
  produce or undermine; defined separately because justified true belief
  and its challengers are substantive positions, not logical ones.
- [Persuasion / rhetoric / dialectic / argumentation](persuasion-rhetoric-dialectic.md) —
  the spectrum of communicative practices in which arguments may or may not
  appear.
