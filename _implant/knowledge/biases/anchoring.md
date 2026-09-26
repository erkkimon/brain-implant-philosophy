---
type: article
about: concept
title: Anchoring
description: "The effect, first named by Tversky and Kahneman in 1974, in which numerical estimates are pulled toward a starting value the estimator was exposed to — even an arbitrary one produced by a wheel of fortune — with the replication record, the boundary conditions, the two competing mechanism accounts, the ecological-rationality critique of calling it a bias, the markers by which to spot it, and the one debiasing intervention with published support."
tags: [bias, judgement, heuristics-and-biases, anchoring, numerical-estimation, replicated]
timestamp: 2026-09-26T09:54:50Z
---

# Anchoring

Family: judgement under uncertainty. Grades follow
[How claims are graded](../../conventions/how-claims-are-graded.md); the
sources are excerpted in `raw/` under the names given in each section.

## Also known as

*Anchoring-and-adjustment*: Tversky and Kahneman's own heading for the
section that introduces the effect is "Adjustment and Anchoring", and they
write, of adjustment away from a starting point, that "adjustments are
typically insufficient"
([Tversky & Kahneman 1974](https://doi.org/10.1126/science.185.4157.1124),
p. 1128; excerpt: `raw/tversky-kahneman-1974-anchoring.md`).
*Anchoring effect*, *anchoring bias* and *anchoring heuristic* are used in
the later literature for the effect, the error, and the process
respectively; the review by
[Furnham & Boo 2011](https://doi.org/10.1016/j.socec.2010.10.008) uses
"anchoring effect" throughout.

## The effect as claimed

The original description (textual claim, verbatim):

> "That is, different starting points yield different estimates, which are
> biased toward the initial values. We call this phenomenon anchoring."
> — [Tversky & Kahneman 1974](https://doi.org/10.1126/science.185.4157.1124), p. 1128

The demonstration they report: subjects estimated quantities stated as
percentages, such as the percentage of African countries in the United
Nations, after a number between 0 and 100 was produced by spinning a wheel
of fortune in their presence; they first said whether the true value was
higher or lower than the number, then estimated by moving away from it.
"The median estimates of the percentage of African countries in the United
Nations were 25 and 45 for groups that received 10 and 65, respectively,
as starting points. Payoffs for accuracy did not reduce the anchoring
effect" (same page). The paper treats anchoring as one of three heuristics
— beside representativeness and availability — of which its summary
says: "These heuristics are highly economical and usually effective, but
they lead to systematic and predictable errors" (p. 1131).

The quantitative paradigm most later studies use is
[Jacowitz & Kahneman 1995](https://doi.org/10.1177/01461672952111004): a
calibration group estimates the quantities first, anchors are set at the
15th and 85th percentiles of those estimates, and the anchored estimates
are converted into calibration-group percentiles so that results can be
pooled across problems.

## Evidence

**Grade: strong** (large effect, direct multi-site replication, consistent
direction across 36 samples).

- The 1974 paper reports medians without effect sizes or sample sizes for
  the wheel-of-fortune demonstration (empirical claim, from the excerpt).
- Many Labs 1 ([Klein et al. 2014](https://doi.org/10.1027/1864-9335/a000178);
  excerpt: `raw/klein-2014-many-labs-anchoring.md`) replicated four
  anchoring items adapted from Jacowitz & Kahneman 1995 across 36 samples
  (6,344 participants total, 13 effects tested). All four items reached
  p < .05 in the expected direction in every one of the 36 samples;
  weighted replication effect sizes (Cohen's d, 99 % CI) were 2.42
  (2.33–2.51) for babies born per day, 2.23 (2.14–2.32) for the height of
  Mt Everest, 1.79 (1.71–1.87) for the population of Chicago, and 1.17
  (1.09–1.25) for the distance from San Francisco to New York. The authors
  note that the original 1995 design (test–retest, point-biserial r across
  15 items) does not yield effect sizes comparable item-by-item with their
  between-subjects design.
- The same paper reports that "heterogeneity of effect sizes was largely
  observed among the very large effects – anchoring, allowed-forbidden, and
  relations between implicit and explicit attitudes": the effect is
  reliably present but its size varies by site and item.
- [Furnham & Boo 2011](https://doi.org/10.1016/j.socec.2010.10.008)
  review the literature to that date and describe the effect as robust
  across paradigms; their review is narrative rather than meta-analytic.

A reader who wants a credence on "anchoring is a real effect" has, in the
above, a strong-grade base; the cognitive-tools implant's
[estimate-a-credence](https://github.com/erkkimon/brain-implant-cognitive-tools/blob/main/_implant/skills/estimate-a-credence.md) skill takes such a record as
one input, never as the answer.

## Boundary conditions

Reported in the literature, each attributed:

- **Expertise does not remove it.** [Englich, Mussweiler & Strack 2006](https://doi.org/10.1177/0146167205282152)
  report that experienced legal professionals anchored their sentencing
  decisions on a demand even when it was randomly determined by throwing
  dice, and that "expertise and experience did not reduce this effect".
  [Northcraft & Neale 1987](https://doi.org/10.1016/0749-5978(87)90046-X)
  report the same pattern for real-estate agents pricing a property from a
  manipulated listing price.
- **Incentives do not remove it**, according to the 1974 paper ("payoffs for
  accuracy did not reduce the anchoring effect").
- **Self-generated versus provided anchors behave differently.**
  [Epley & Gilovich 2006](https://doi.org/10.1111/j.1467-9280.2006.01704.x)
  report that adjustment from anchors people generate themselves "tend[s]
  to be insufficient because [adjustments] terminate once a plausible
  value is reached", whereas provided anchors, on their account, work
  through a different route (see the next section).
- **Negotiation.** [Galinsky & Mussweiler 2001](https://doi.org/10.1037/0022-3514.81.4.657)
  report that first offers anchor negotiated outcomes and that the effect
  is reduced when the receiving negotiator focuses on their own target or
  on the opponent's alternatives.

## Interpretations and critique

Two mechanism accounts compete in the literature, and a third voice
disputes whether the phenomenon is a *bias* at all.

1. **Insufficient adjustment** — the original account: the estimator
   starts at the anchor and adjusts too little
   ([Tversky & Kahneman 1974](https://doi.org/10.1126/science.185.4157.1124), p. 1128).
   [Epley & Gilovich 2006](https://doi.org/10.1111/j.1467-9280.2006.01704.x)
   argue that "evidence for adjustment-based anchoring biases has only
   recently been provided" and that the account holds for self-generated
   anchors.
2. **Selective accessibility** — [Strack & Mussweiler 1997](https://doi.org/10.1037/0022-3514.73.3.437)
   propose that comparing the target with the anchor selectively activates
   anchor-consistent knowledge, which then shapes the estimate; on this
   account no adjustment need occur. The Englich et al. 2006 sentencing
   study reports, in support, that "the accessibility of incriminating
   arguments was higher" after a high anchor.
3. **The ecological-rationality critique** — [Gigerenzer 1996](https://doi.org/10.1037/0033-295X.103.3.592)
   (excerpt: `raw/gigerenzer-1996-narrow-norms.md`) argues, of the
   heuristics-and-biases programme as a whole, that "at issue is the
   imposition of unnecessarily narrow norms of sound reasoning that are
   used to diagnose so-called cognitive illusions and the continuing
   reliance on vague heuristics that explain everything and nothing", and
   that the named heuristics "are labels with the virtue of Rorschach
   inkblots: a researcher can read into them what he or she wishes".
   [Kahneman & Tversky 1996](https://doi.org/10.1037/0033-295X.103.3.582)
   is the paper this replies to; they defend the reality of the illusions
   and the explanatory use of the heuristics. The exchange is the locus
   for the question whether a robust *effect* is thereby a *bias*: that
   depends on the norm one measures against, which is what the two sides
   dispute.

The implant records the three; which is right is not a question it
answers ([Reporting, not endorsing](../../conventions/reporting-not-endorsing.md)).

## How to spot it

Markers, from the sources that give them:

- A numerical estimate made after a number was mentioned — a list price,
  an opening offer, a sentencing demand, a "would you say more or less
  than N?" question — and lying closer to that number than an unanchored
  estimate would ([Jacowitz & Kahneman 1995](https://doi.org/10.1177/01461672952111004)
  for the comparative-question paradigm;
  [Galinsky & Mussweiler 2001](https://doi.org/10.1037/0022-3514.81.4.657)
  for offers; [Englich et al. 2006](https://doi.org/10.1177/0146167205282152)
  for demands).
- The anchor need not be relevant, plausible, or believed by the
  estimator: the 2006 sentencing study used anchors the participants
  themselves produced by dice.
- In text, a figure introduced before the question ("Experts have
  suggested as much as 40 %; what do you think?") is the structural form
  of the comparative-question paradigm; the
  [spot-persuasion-and-bias](../../skills/spot-persuasion-and-bias.md)
  skill lists it under this page.

## Debiasing

- **Consider the opposite.** [Mussweiler, Strack & Pfeiffer 2000](https://doi.org/10.1177/01461672002611010)
  report that "listing arguments that speak against a provided anchor
  value reduces the effect", in two studies including one with expert
  participants in a real-world setting; the intervention is derived from
  the selective-accessibility account. Grade: moderate (two studies, one
  group, no independent multi-site replication located).
- **Incentives and expertise** are reported *not* to work (see Boundary
  conditions).
- **Perspective-taking in negotiation.** [Galinsky & Mussweiler 2001](https://doi.org/10.1037/0022-3514.81.4.657)
  report that focusing on one's own target or on the counterpart's
  alternatives reduces the first-offer effect. Grade: moderate.

## Exploited by

- [Appeal to authority](../persuasion/appeal-to-authority.md) — an
  authority's stated figure is a provided anchor; the connection is the
  implant's structural observation, not a claim of any cited source.
- First offers in negotiation, per
  [Galinsky & Mussweiler 2001](https://doi.org/10.1037/0022-3514.81.4.657);
  list prices, per
  [Northcraft & Neale 1987](https://doi.org/10.1016/0749-5978(87)90046-X).
  Pages for those techniques are open work
  ([todo](../../todo/open.md)).

## See also

- [Biases index](index.md) — the branch template and its grading rule.
- [Persuasion index](../persuasion/index.md).
