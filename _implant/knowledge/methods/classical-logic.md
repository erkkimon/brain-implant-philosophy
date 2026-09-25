---
type: article
about: process
title: "Classical logic"
description: "The working logic of this implant — classical propositional and first-order logic with bivalence, excluded middle, and non-contradiction — adopted as a given (G1) because any defence of it would already use it, and documented here so that its presuppositions and its limits are visible."
tags: [method, logic]
timestamp: 2026-09-25T23:58:00Z
---

# Classical logic

## What it does

Classical logic is the system of valid inference that this implant uses to
evaluate arguments. It comprises classical propositional logic (truth tables,
named forms such as modus ponens, modus tollens, hypothetical syllogism,
disjunctive syllogism) and classical first-order predicate logic (quantifiers,
identity, validity defined over models). Its key principles are:

- **Bivalence:** every proposition is either true or false.
- **Law of excluded middle:** for every proposition P, P ∨ ¬P.
- **Law of non-contradiction:** ¬(P ∧ ¬P).
- **Truth-preservation:** a valid argument guarantees that if all premises
  are true, the conclusion is true.

`logic.py` implements propositional validity
checking via truth tables and named-form recognition. First-order validity
is not currently implemented; arguments requiring it are flagged.

## Origins

- **Aristotle:** *Prior Analytics* (c. 350 BCE) — the syllogistic, the first
  formal system of valid inference. Standard edition Bekker 24a–70b.
- **Stoics:** Chrysippus developed propositional logic (conditionals,
  disjunctions); fragments in Diogenes Laertius VII.76–81 and Sextus
  Empiricus, *Against the Logicians*.
- **Frege 1879:** *Begriffsschrift* — modern quantificational logic.
- **Russell & Whitehead 1910–1913:** *Principia Mathematica* — the
  axiomatisation that became the standard reference.
- **Tarski 1933:** model-theoretic semantics for first-order logic; the
  definition of validity used by `logic.py`.

## Presuppositions

Classical logic assumes:

- **Bivalence.** Intuitionistic logic rejects excluded middle; paraconsistent
  logic rejects explosion from contradiction. These are documented as
  subject matter, not adopted.
- **Extensionality.** The truth value of a compound depends only on the
  truth values of its parts. Intensional contexts (belief, necessity)
  require modal extensions not currently implemented.
- **G1 ([manifest](../../vision/manifest.md)).** Logic is trusted as a
  given; any defence of it would already use it. This is unavoidable, not
  a choice.

Pages whose arguments depend on non-classical logic say so explicitly.

## The case for

- **Unavoidability.** Any attempt to argue against classical logic must use
  inference; the attempt presupposes what it denies. This is not a proof
  but a structural observation recorded in G1.
- **Simplicity and computability.** Truth-table checking is decidable for
  propositional logic; first-order validity is semi-decidable. Non-classical
  logics are typically harder to compute.
- **Standardisation.** Classical logic is the lingua franca of analytic
  philosophy, mathematics, and computer science. Using it maximises
  interoperability with external sources.
- **Empirical adequacy (proponents).** Classical logic captures the
  inferential practices of mathematics and science; deviations are special
  cases, not replacements. Williamson, "Deviance and Viciousness" (*Philosophy
  of Logic*, ed. Burgess, 2023).

## The case against

- **Intuitionism.** Brouwer rejected excluded middle for infinite domains;
  mathematical truth requires construction, not mere consistency. Heyting
  formalised intuitionistic logic (1930). Dummett extended the challenge
  to natural language (*Elements of Intuitionism*, 1977).
- **Paraconsistency.** Priest argues that some contradictions are true
  (dialetheism); classical logic's explosion principle makes inconsistent
  theories trivial. *In Contradiction* (1987/2006).
- **Relevance logic.** Anderson & Belnap argue that classical implication
  allows irrelevant conclusions (A → (B → A)); relevance logic requires
  premise-conclusion connection. *Entailment* (1975).
- **Quantum logic.** Birkhoff & von Neumann (1936) proposed a non-distributive
  logic for quantum mechanics; the status of this proposal is contested.
- **Feminist / postcolonial critiques.** Some scholars argue that classical
  logic encodes Western, masculinist assumptions about rationality
  (Plumwood, "Feminism and the Mastery of Nature", 1993; Nisbett et al.,
  "Culture and Systems of Thought", *Psychological Review* 2001). These
  critiques target the cultural hegemony of classical logic, not its
  formal properties.
- **Empirical psychology.** Johnson-Laird's mental-models theory suggests
  human reasoning does not follow classical rules; Wason selection task
  results show systematic deviations. Whether this counts against classical
  logic as a normative standard or against humans as reasoners is contested.

## Where it is used in this implant

- [Analyse-an-argument](../../skills/analyse-an-argument.md) — reconstructs
  arguments and checks validity via `logic.py`.
- [Validity](../vocabulary/validity.md) — defined classically.
- [Argument](../vocabulary/argument.md) — the unit evaluated.
- All [arguments](../arguments/index.md) pages include a `logic.py`
  reconstruction where the form is propositional.
- [Bayesian updating](bayesian-updating.md) — an alternative to classical
  logic for reasoning under uncertainty; documented with its case against.
