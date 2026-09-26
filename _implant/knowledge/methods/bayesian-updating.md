---
type: article
about: process
title: "Bayesian updating with the case against"
description: "The method of revising credences by conditionalising on new evidence, presented here alongside its objections (the problem of the priors, frequentist and likelihoodist alternatives, computational intractability) so that the implant's use of Bayesian tools is transparent about what it assumes and what it does not."
tags: [method, epistemology, probability]
timestamp: 2026-09-26T09:54:50Z
---

# Bayesian updating with the case against

## What it does

Bayesian updating is the rule for revising degrees of belief (credences) in
light of new evidence. Given a prior credence P(H) in hypothesis H and new
evidence E, the posterior credence is:

    P(H|E) = P(E|H) × P(H) / P(E)

where P(E|H) is the likelihood of E given H, and P(E) is the marginal
likelihood (summed or integrated over all hypotheses). The rule is a theorem
of probability theory; its philosophical significance lies in treating it as
a normative model for rational belief revision.

This implant uses Bayesian updating via the companion
[cognitive-tools implant](https://github.com/erkkimon/brain-implant-cognitive-tools),
specifically the [estimate-a-credence](https://github.com/erkkimon/brain-implant-cognitive-tools/blob/main/_implant/skills/estimate-a-credence.md) skill. The
skill decomposes a gut feeling into factors, priors, and likelihood ratios,
runs a Monte Carlo range, and reports whether evidence or prior is carrying
the result. The decomposition is the contribution; the numbers are inputs
the user can change.

## Origins

- **Bayes 1763:** "An Essay towards Solving a Problem in the Doctrine of
  Chances" — the theorem, published posthumously by Price. Bayes did not
  propose it as a general epistemology.
- **Laplace 1812:** *Théorie analytique des probabilités* — extended Bayes'
  theorem to scientific inference; called it "probability of causes".
- **Ramsey 1926 / de Finetti 1937:** subjective probability as degree of
  belief, defined by betting dispositions. The Dutch book argument shows
  that incoherent credences expose the agent to guaranteed loss.
- **Savage 1954:** *Foundations of Statistics* — axiomatised subjective
  expected utility; Bayesian decision theory.
- **Jaynes 2003:** *Probability Theory: The Logic of Science* — Bayesianism
  as an extension of logic; maximum entropy as the principle for setting
  priors.
- **Howson & Urbach 2006:** *Scientific Reasoning: The Bayesian Approach*
  (3rd ed.) — the standard philosophical defence of Bayesian confirmation
  theory.

## Presuppositions

- **Credences are probabilities.** Degrees of belief satisfy the probability
  axioms. The Dutch book argument supports this; critics note that real
  agents are not idealised bettors and that the axioms may be too strong
  for bounded agents.
- **Conditionalisation is the update rule.** New evidence is incorporated by
  conditionalising on it. This assumes the evidence is certain (P(E) = 1);
  Jeffrey conditionalisation relaxes this for uncertain evidence. Both
  assume the evidence partition is fixed; framing effects challenge this.
- **Priors are permissible.** Bayesianism allows any probabilistically
  coherent prior. Objective Bayesians demand constraints (principle of
  indifference, maximum entropy); subjective Bayesians deny this. The
  choice between them is contested.
- **Compute, never guess.** The cognitive-tools implant's convention
  ([compute-never-guess](https://github.com/erkkimon/brain-implant-cognitive-tools/blob/main/_implant/conventions/compute-never-guess.md))
  requires that every number in a credence model come from a deterministic
  tool, not from a language model's head. This is a methodological choice,
  not a theorem.

## The case for

- **Coherence.** The Dutch book argument shows that non-probabilistic
  credences expose the agent to guaranteed loss. Coherence is a minimal
  rationality constraint.
- **Learning from evidence.** Conditionalisation guarantees that credences
  converge on the truth as evidence accumulates (under mild conditions;
  Gaifman & Snir 1982). Frequentist methods lack this guarantee for
  individual hypotheses.
- **Handles uncertainty gracefully.** Bayesian methods assign degrees of
  belief to all hypotheses, not just accept/reject decisions. This matches
  the epistemic situation in philosophy, where certainty is rare.
- **Unifies confirmation and disconfirmation.** Evidence that raises P(H)
  confirms; evidence that lowers it disconfirms. The same formula handles
  both. Popperian falsificationism cannot confirm; Bayesianism can.
- **Practical success.** Bayesian methods dominate machine learning, signal
  processing, medical diagnosis, and forensic science. Their practical
  success is evidence of their normative adequacy (proponents argue).

## The case against

- **The problem of the priors.** Subjective priors allow any starting point;
  two rational agents with different priors may never converge in finite
  time. Objective priors require principles (indifference, maximum entropy)
  whose own justification is contested. Keynes criticised the principle of
  indifference (*A Treatise on Probability*, 1921); Bertrand's paradox
  shows it can yield contradictory results depending on parameterisation.
- **Frequentist alternatives.** Neyman-Pearson hypothesis testing controls
  error rates without requiring priors. Fisher's significance testing
  assesses evidence against a null without assigning probabilities to
  hypotheses. Frequentists argue that science needs error control, not
  belief revision. Mayo, *Statistical Inference as Severe Testing* (2018).
- **Likelihoodism.** Royall argues that evidence should be measured by
  likelihood ratios alone, without priors or posteriors; the question
  "what does the evidence say?" is distinct from "what should I believe?"
  (*Statistical Evidence: A Likelihood Paradigm*, 1997).
- **Computational intractability.** Exact Bayesian updating is intractable
  for complex hypothesis spaces. Approximate methods (MCMC, variational
  inference) introduce their own assumptions and errors. The gap between
  normative ideal and feasible practice is wide.
- **Old evidence problem.** Glymour (1980) noted that Bayesianism cannot
  explain how already-known evidence confirms a new theory (P(E) = 1 makes
  P(H|E) = P(H)). Various solutions have been proposed (Garber 1983,
  Earman 1992); none is universally accepted.
- **Framing and partition dependence.** The posterior depends on how the
  hypothesis space is partitioned. Different partitions yield different
  posteriors from the same evidence. This challenges the claim that
  Bayesian updating is uniquely rational.
- **Bounded rationality.** Real agents cannot maintain probabilistically
  coherent credence functions over large hypothesis spaces. Gigerenzer
  argues that fast-and-frugal heuristics outperform Bayesian methods in
  many ecological contexts (*Simple Heuristics That Make Us Smart*, 1999).

## Where it is used in this implant

- [Estimate-a-credence](https://github.com/erkkimon/brain-implant-cognitive-tools/blob/main/_implant/skills/estimate-a-credence.md) — the cognitive-tools skill
  that implements Bayesian decomposition for this implant's users.
- [Biases](../biases/index.md) pages cite Bayesian norms when discussing
  deviations (base-rate neglect, confirmation bias).
- [Persuasion](../persuasion/index.md) pages cite Bayesian reanalyses of
  traditionally classified fallacies (appeal to authority, argument from
  ignorance).
- The implant itself does not assign credences; it provides the factors,
  base rates, and bias pages that make a user's credence model educated.
  The decision stays with the user.
