---
type: article
about: concept
title: "Dilemma"
description: "Three senses kept apart — the logical argument form with two horns (constructive/destructive dilemma), the loose everyday 'choice between two bad options', and the moral dilemma of ethics, where an agent is required to do each of two acts but cannot do both and neither requirement is overridden."
tags: [vocabulary, logic, ethics, dilemma]
timestamp: 2026-09-26T12:00:19Z
---

# Dilemma

## Normative definition (this implant)

"Dilemma" is used here in two technical senses, always with its qualifier:

1. **Dilemma (argument form).** An argument whose disjunctive premise has
   two "horns", each leading to a conclusion. *Constructive dilemma*: from
   *P → Q*, *R → S* and *P ∨ R*, infer *Q ∨ S*. `logic.py` reports this
   form as "VALID" and names it "constructive dilemma". *Destructive
   dilemma*: from *P → Q*, *R → S* and *¬Q ∨ ¬S*, infer *¬P ∨ ¬R*;
   `logic.py` reports it "VALID" (checked 2026-09-26). The validity is a
   matter of form, per [validity](validity.md); whether the horns exhaust
   the options is a separate, factual question.
2. **Moral dilemma.** A situation in which "the agent is required to do each
   of two (or more) actions; the agent can do each of the actions; but the
   agent cannot do both (or all) of the actions", and "neither of the
   conflicting requirements is overridden" (McConnell,
   [SEP Fall 2024 "Moral Dilemmas"](https://plato.stanford.edu/archives/fall2024/entries/moral-dilemmas/),
   §2, citing Sinnott-Armstrong 1988 ch. 1; excerpt:
   `raw/sep-moral-dilemmas-fall-2024-concept-and-consistency-arguments.md`).
   Whether any situation meets this definition is the open question of
   [Can there be genuine moral dilemmas?](../problems/moral-dilemmas.md);
   the definition does not presuppose an answer.

Why these: the loose sense (a hard choice) and the moral sense (a choice in
which every option is wrong) come apart, and much of the literature is about
whether the second ever occurs. A page that says "dilemma" without the
qualifier would silently take sides. Fixed 2026-09-26
([journal](../../journals/2026-09-26.md)).

## Descriptive definitions

- **Rhetoric and logic (the older sense).** Etymonline, citing the *Century
  Dictionary*: "A form of argument in which it is shown that whoever
  maintains a certain proposition must accept one or other of two
  alternative conclusions, and that each of these involves the denial of
  the proposition in question"; English from the 1520s, from Greek
  *dilemma* "double proposition" ([Etymonline](https://www.etymonline.com/word/dilemma);
  excerpt:
  `raw/oxymoron-and-dilemma-definitions-silva-rhetoricae-wiktionary-etymonline.md`).
- **Loose everyday sense.** "Loosely, "choice between two undesirable
  alternatives," from 1580s" (Etymonline). A usage note there says it
  "should be used only of situations where someone is forced to choose
  between two alternatives, both unfavorable to him"; the note is
  Etymonline's recommendation, recorded here as such.
- **Moral dilemma (ethics).** McConnell's definition above. He reports that
  on it Plato's case (returning a weapon to a friend "not in his right
  mind", *Republic* I) "strikes many as too easy to be characterized as a
  genuine moral dilemma", whereas Sartre's student, torn between staying with
  his mother and going to fight, is the harder case (§§1–2).
- **Symmetrical dilemma.** A moral dilemma in which "the same precept
  generates the conflicting requirements" — McConnell's example is
  *Sophie’s Choice* (§5).

## Collisions

- **Dilemma vs. false dilemma.** A *false dilemma* (a label in the
  [fallacy](fallacy.md) literature) is the charge that the disjunctive # lint: allow
  premise leaves out an option. It is a charge against a premise's truth,
  not against the form, which stays valid. The charge is always attributed
  to whoever makes it.
- **Hard choice vs. moral dilemma.** Uncertainty about what to do does not by
  itself make a situation a moral dilemma: McConnell reports opponents'
  point that "the mere fact that one does not know which of two (or more)
  conflicting obligations prevails does not show that none does" (§5).
- **Trolley "dilemma".** The [trolley problem](../problems/trolley-problem.md)
  is often called a dilemma in the loose sense. Whether it is a moral
  dilemma in sense 2 depends on the answer one gives, so pages here call it
  a problem or a case.

## Related terms

- [Paradox](paradox.md) — a dilemma-form argument can be one step of a
  paradox; neither is a kind of the other.
- [Validity](validity.md) — what makes the argument-form sense mechanical.
- [Oxymoron](oxymoron.md) — unrelated beyond the two-part structure.
