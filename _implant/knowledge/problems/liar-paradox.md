---
type: article
about: concept
title: "The liar paradox: is 'This sentence is false' true or false?"
description: "The sentence that says of itself that it is false — true if false, false if true — from the Megarians and Epimenides through the medieval insolubilia to Tarski, Kripke and Priest, with the families of solution (deny bivalence, paracomplete, paraconsistent, substructural, Tarski's hierarchy, contextualism) and who holds each."
tags: [problem, logic, philosophy-of-language, truth, paradox]
timestamp: 2026-09-26T12:00:19Z
---

# The liar paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md).
Source for the map: Beall, Glanzberg & Ripley,
[SEP Fall 2024 "Liar Paradox"](https://plato.stanford.edu/archives/fall2024/entries/liar-paradox/)
(excerpt: `raw/sep-sorites-and-liar-fall-2024-paradox-formulations-and-responses.md`).

## The question

"Consider a sentence named ‘FLiar’, which says of itself (i.e., says of
FLiar) that it is false. FLiar: FLiar is false." The SEP authors derive
"FLiar is false if and only if FLiar is true", and then: "if every sentence
is true or false, FLiar itself is either true or false, in which case [...]
it is both true and false. This is a contradiction. Contradictions,
according to many logical theories (e.g., classical logic, intuitionistic
logic, and many others) imply triviality, that is, that every sentence is
true" (§1.1).

**Logic check (this implant, 2026-09-26).** Writing T for "FLiar is true"
and taking "false" as "not true", the biconditional is `T <-> ~T`.
`logic.py` reports that this premise alone is "jointly inconsistent", so
both `T & ~T` and an unrelated `Q` follow "vacuously" — the triviality
the SEP describes, in classical propositional logic. What the tool cannot
check is the step *to* `T <-> ~T`, which rests on principles of truth
(the T-schema, §2), not on propositional logic; that step is where many
solutions intervene.

**History.** "It was discussed in classical times, notably by the
Megarians, but it was also mentioned by Aristotle and by Cicero. As one of
the insolubilia, it was the subject of extensive investigation by medieval
logicians such as Buridan" (preamble). The name "‘Epimenides paradox’"
comes from the tradition that Epimenides of Crete "said that all Cretans
are always liars" (preamble).

## Why it matters

- The SEP authors: "the Liar seems to allow us to reach such conclusions on the basis of logic, plus some very obvious principles that have sometimes been counted as principles of logic"
  — "perhaps the most virulent strain of paradox" (preamble).
- It has been used in "arguments against classical logic" (§2), and in
  Tarski's conclusion about truth predicates (§4.3.1).
- Cantini places the semantic paradoxes at the origin of type theory and of
  incompleteness results ([SEP "Paradoxes and Contemporary Logic"](https://plato.stanford.edu/archives/fall2024/entries/paradoxes-contemporary-logic/),
  contents §§2.3, 6.4).

## Positions taken

Families as the SEP entry groups them (§4), each with the proponents it
names. None is ranked.

- **Deny bivalence.** "An obvious response is to deny that every sentence is
  true or false, i.e., to deny the principle of bivalence" (§1.1).
- **Paracomplete logics** — "(e.g., Kripke 1975; Field 2008)" (§2, §4.1.1).
- **Paraconsistent logics** — "(e.g., Asenjo 1966; Priest 1984, 2006)";
  "the basic idea is to allow the contradiction [...] but alter the logic by
  rejecting EFQ" (ex falso quodlibet) (§2, §4.1.2).
- **Substructural logics** — noncontractive, nontransitive, nonreflexive
  (§4.2; proponents not yet excerpted).
- **Keep classical logic: Tarski's hierarchy.** "Tarski concluded from the
  paradox that no language could contain its own truth predicate" (§4.3.1);
  also Kripke's closed-off construction and other classical approaches
  (§§4.3.2–4.3.4); Ripley (2013b) "argues that classical logic can be
  maintained while shedding the features in question" (§2).
- **Contextualist approaches** (§4.4; not yet excerpted).

No survey figure is recorded.

## Arguments in play

(none recorded as separate argument pages yet).

## Thinkers who addressed it

- **Eubulides / the Megarians** (4th c. BCE) — Cantini credits "the
  arguments entangling the notions of truth and vagueness" to "the Megarian
  School, and Eubulides of Miletus" (preamble).
- **Aristotle, Cicero** — mention it (Beall et al., preamble).
- **Jean Buridan** (14th c.) — the insolubilia (preamble).
- **Alfred Tarski** (1935) — the hierarchy of languages (§4.3.1).
- **F. G. Asenjo** (1966), **Saul Kripke** (1975), **Graham Priest** (1984,
  2006), **Hartry Field** (2008), **David Ripley** (2013) — positions as
  above.

## Framings and reframings

- **A family, not one sentence.** "The puzzle is usually named ‘the Liar
  paradox’, though this really names a family of paradoxes" — simple-falsity
  and simple-untruth liars, liar cycles, Boolean compounds, infinite
  sequences (preamble; §1).
- **Not about lying.** "what’s puzzling about sentences like the first one of
  this essay isn’t essentially tied to intentions, social norms, or anything
  like that. Rather, it seems to have something to do with truth" (preamble).

## Vocabulary

- [Paradox](../vocabulary/paradox.md).
- [Validity](../vocabulary/validity.md) — the triviality step is valid in
  classical logic.
- [Classical logic](../methods/classical-logic.md) — the logic several
  solutions revise.
