---
type: article
about: concept
title: "Goodman's new riddle of induction (grue)"
description: "Why do green emeralds confirm 'all emeralds are green' but not 'all emeralds are grue', when the same observations fit both? Goodman's 1955 riddle in Fact, Fiction, and Forecast, the grue/bleen symmetry, projectibility and entrenchment, and the responses on record (positional predicates, Quine's natural kinds, Bayesian priors, no-rules material induction, formal learning theory) with their owners."
tags: [problem, paradox, epistemology, philosophy-of-science, induction]
timestamp: 2026-10-01T19:53:21Z
---

# Goodman's new riddle of induction (grue)

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
claim grades as in [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Primary text: Nelson Goodman, *Fact, Fiction, and Forecast*, Harvard UP, 1955, ch. III "The New Riddle of Induction" and ch. IV §2
([1955 scan](https://archive.org/details/fact-fiction-and-forecast); excerpts:
`raw/goodman-1955-fact-fiction-forecast-new-riddle-entrenchment.md`, `raw/goodman-1955-fact-fiction-forecast-ravens-and-grue.md`;
page numbers below are the printed ones at the foot of each scanned page, which the first file explains).
Maps: Leah Henderson, [SEP Fall 2024 "The Problem of Induction"](https://plato.stanford.edu/archives/fall2024/entries/induction-problem/) §§4.2, 5.4
(excerpt: `raw/sep-induction-problem-fall-2024-new-riddle.md`); Daniel Cohnitz & Marcus Rossberg,
[SEP Fall 2024 "Nelson Goodman"](https://plato.stanford.edu/archives/fall2024/entries/goodman/) §5 (excerpt: `raw/sep-goodman-fall-2024-new-riddle-and-solution.md`);
Alexander Bird & Emma Tobin, [SEP Fall 2024 "Natural Kinds"](https://plato.stanford.edu/archives/fall2024/entries/natural-kinds/) §1.2
(excerpt: `raw/sep-natural-kinds-fall-2024-quine-grue.md`); Vincenzo Crupi, [SEP Fall 2024 "Confirmation"](https://plato.stanford.edu/archives/fall2024/entries/confirmation/)
§§1.2, 2.2, 3.6 (excerpts: `raw/sep-confirmation-fall-2024-blite-bayesian.md`, `raw/sep-confirmation-fall-2024-ravens-paradox.md`).
Cohnitz & Rossberg list their own 2006 book among the rule-following references (§5.4); that is marked where it appears.

## The question

Goodman's predicate: "It is the predicate “grue” and it applies to all things examined before t just in case they are green but to other things just in case they are blue." (1955, p. 74).
All emeralds examined before *t* are green, hence also grue; each evidence statement confirms, by the instance definition Goodman is testing, both *all emeralds are green* and *all emeralds are grue*:
"Thus according to our definition, the prediction that all emeralds subsequently examined will be green and the prediction that all will be grue are alike confirmed by evidence statements describing the same observations." (p. 74).
"Thus although we are well aware which of the two incompatible predictions is genuinely confirmed, they are equally well confirmed according to our present definition." (p. 75).
Henderson's restatement: "Thus the two predictions are incompatible. Goodman claims that what Hume omitted to do was to give any explanation for why we project predicates like “green”, but not predicates like “grue”." (SEP §4.2).
Goodman's general form: "the new riddle of induction, which is more broadly the problem of distinguishing between projectible and non-projectible hypotheses" (p. 82).
The question therefore turns on *lawlike* versus *accidental* generalisations: "Only a statement that is lawlike—regardless of its truth or falsity or its scientific importance —is capable of receiving confirmation from an instance of it; accidental statements are not." (p. 74).
Cohnitz & Rossberg: "We could obviously define infinitely many grue-like predicates that would all lead to new, similarly incompatible predictions." (§5.3).
Crupi's variant "blite" (from "Blite (Goodman 1955)") runs the same construction on the ravens: "an object is blite just in case (i) it is black if examined at some moment t up to some future time T (say, the next expected appearance of Halley’s comet, in 2061) and (ii) it is white if examined afterwards." (§1.2).

**Propositional check (this implant, 2026-10-01; logic, not a position).**
For one object, let *e* = examined before *t*, *g* = green, *b* = blue, *u* = grue, *n* = bleen, with Goodman's definitions as
*u* ↔ ((*e* & *g*) | (~*e* & *b*)) and *n* ↔ ((*e* & *b*) | (~*e* & *g*)) (p. 79 gives bleen).
(1) `logic.py check --premises "u <-> ((e & g) | (~e & b))" "e & g" --conclusion "u"` outputs `VALID`: an examined green object is grue.
(2) With `~(g & b)` and `~e & u` added as premises, conclusion `~g`: `VALID` — an unexamined grue object is not green, Goodman's "it is blue and hence not green" (p. 75).
(3) From both definitions, conclusion `g <-> ((e & u) | (~e & n))`: `VALID` — green is definable from grue, bleen and the same temporal atom.
Step (3) is the logical core of Goodman's symmetry remark quoted under *Positions*; the tool covers it only as a single-object propositional scheme and says nothing about which predicates are projectible.

## Why it matters

- **Hume's problem.** Henderson: "This is the “new riddle”, which is often taken to be a further problem of induction that Hume did not address." (§4.2); Goodman: "Hume overlooks the fact that some regularities do and some do not establish such habits; that predictions based on some regularities are valid while predictions based on other regularities are not." (p. 81).
- **Confirmation theory.** Goodman: "We are left once again with the intolerable result that anything confirms anything." (p. 75). Crupi reports that hypothetico-deductive (HD) confirmation has the same difficulty: "So, all in all, HD-confirmation can not tell black from blite any more than Hempel-confirmation can." (§2.2).
- **Choice of predicates.** Cohnitz & Rossberg: "For valid inductive inferences the choice of predicates matters." (§5.3); they call the "grue-paradox" "Perhaps his most famous contribution" (preamble).
- **The ravens.** Goodman sets the riddle beside Hempel's paradox: "Sometimes, for example, the problem is thought to be much like the paradox of the ravens." (p. 75), then denies that the ravens diagnosis carries over: "But while it is true that such information is being smuggled in, this does not by itself settle the matter as it settles the matter of the ravens." (p. 76). See [the raven paradox](raven-paradox.md).
- **Rule-following.** Cohnitz & Rossberg point to the literature relating "the grue-paradox to Kripke’s Wittgenstein’s rule following puzzle (1982)" (§5.4); see the [rule-following paradox](rule-following-paradox.md).

## Positions taken

No survey grouping of answers was found in the sources read; the order below is the order in which the sources present them (Cohnitz & Rossberg §§5.3–5.4, then Bird & Tobin, Crupi, Henderson). None is ranked here.

- **Positional versus qualitative predicates (Carnap 1947, as Cohnitz & Rossberg report it).**
  *For:* "An immediate reply is that the illegitimate generalization L4 involves a temporal restriction, just as L2 was restricted spatially (see e.g., Carnap 1947)." (§5.3; L4 is "all emeralds are grue").
  *Against:* Goodman: "True enough, if we start with “blue” and “green”, then “grue” and “bleen” will be explained in terms of “blue” and “green” and a temporal term. But equally truly, if we start with “grue” and “bleen”, then “blue” and “green” will be explained in terms of “grue” and “bleen” and a temporal term" (p. 79), and "Thus qualitativeness is an entirely relative matter and does not by itself establish any dichotomy of predicates" (p. 79). Cohnitz & Rossberg: "The trouble is that this reply makes it relative to a language whether or not a predicate is projectible." (§5.3).
- **Entrenchment (Goodman 1955, ch. IV).** "The answer, I think, is that we must consult the record of past projections of the two predicates." (p. 95); "The predicate “green”, we may say, is much better entrenched than the predicate “grue”." (p. 95); "One principle for eliminating unprojectible projections, then, is that a projection is to be ruled out if it conflicts with the projection of a much better entrenched predicate." (p. 96). The definition as Cohnitz & Rossberg give it from "FFF, 108": "A hypothesis is projectible iff it is supported, unviolated, and unexhausted, and all hypotheses conflicting with it are overridden." (§5.4).
  *For:* Cohnitz & Rossberg describe the account as descriptive: "Instead of providing a theory that would ultimately justify our choice of predicates for induction, he develops a theory that provides an account of how we in fact choose predicates for induction and projection." (§5.4). Goodman separates it from familiarity: "In the first place, entrenchment and familiarity are not the same." (p. 97).
  *Against:* the objection Goodman states himself: "And in fact wasn’t it projected so often because its projection was so often obviously legitimate, so that our proposal begs the question? I think not." (p. 98), with his reply "I submit that the judgment of projectibility has derived from the habitual projection, rather than the habitual projection from the judgment of projectibility." (p. 98). Cohnitz & Rossberg: "Goodman’s solution makes projectibility essentially a matter of what language we use and have used to describe and predict the behaviour of our world." (§5.4).
- **Natural kinds and similarity (Quine 1969, "Natural Kinds", [doi:10.1007/978-94-017-1466-2_2](https://doi.org/10.1007/978-94-017-1466-2_2), not read here).**
  *For:* Bird & Tobin: "With Goodman’s new riddle of induction and Hempel’s paradox of confirmation in mind, Quine answers that it is the similarity or sameness of kinds between instances that permits an induction: two green emeralds are more similar than two grue emeralds when one of them is green and the other blue." (§1.2); on their report Quine adds "And the force of Darwinian processes gives us some reason to think that we have evolved an innate similarity space that corresponds to some natural similarities." (§1.2).
  *Against:* Quine's own worry, as Bird & Tobin quote it: the "dubious scientific standing of a general notion of similarity, or of kind" (1969, 116). Crupi's assessment: "Then one could restrict confirmation theory accordingly, i.e., to “natural kinds” only (see, e.g., Quine 1970). Yet this point turns out be very difficult to pursue coherently and it has not borne much fruit in this discussion (Rinard 2014 is a recent exception)." (§1.2), with Howson's water case: "So why should the time threshold T in blite or blurple be a reason to dismiss those predicates?" (§1.2; "(The water example comes from Howson 2000, 31–32.").
- **Bayesian priors (Gaifman 1979, Sober 1994, Fitelson 2008, as Crupi reports them).**
  *For:* "So, as long as the black hypothesis is perceived as initially more credible than its blite counterpart, the former will be more strongly confirmed than the latter." (Crupi §3.6, crediting "Gaifman 1979, 127–128; Sober 1994, 229–230; and Fitelson 2008, 131"). Records: Gaifman, *Erkenntnis* 14 ([doi:10.1007/bf00196729](https://doi.org/10.1007/bf00196729)); Fitelson, "Goodman's “New Riddle”", *J. Philos. Logic* 37, 613–643 ([doi:10.1007/s10992-008-9083-5](https://doi.org/10.1007/s10992-008-9083-5)); texts not read (`raw/new-riddle-of-induction-bibliographic-records.md`).
  *Against:* Crupi's assessment: "Lacking some interesting, non-question-begging story as to why that inequality should obtain, no solution of the paradox seems to emerge." (§3.6). He proposes minimal requirements instead: "Without a doubt, (i) and (ii) fall far short of a satisfactory solution of the blite paradox. Yet it seems at least a legitimate minimal requirement for a compelling solution (if any exists) that it implies both." (§3.6). For the updating rule see [Bayesian updating](../methods/bayesian-updating.md).
- **No general rule; material induction (Sober 1988, Norton 2003, Okasha 2001, 2005, as Henderson reports them).**
  *For:* "One moral that could be taken from Goodman is that there is not one general Uniformity Principle that all probable arguments rely upon (Sober 1988; Norton 2003; Okasha 2001, 2005a,b, Jackson 2019)." and "There is no circularity. Rather there is a regress of inductive justifications, each relying on their own empirical presuppositions (Sober 1988; Norton 2003; Okasha 2001, 2005a,b)." (§4.2).
  *Against:* no objection to this reading is stated in the passages read (Henderson §4.2 reports it without one); left open here rather than supplied.
- **Formal learning theory (Schulte 1999, 2017, as Henderson reports it).**
  *For* and *against* are reported together by Henderson, who names a party on each side without stating their arguments: "There is a similar dispute over formal learning theory’s treatment of Goodman’s riddle (Chart 2000, Schulte 2017)." (§5.4). Chart, "Schulte and Goodman's Riddle", *BJPS* 51, 147–149 ([doi:10.1093/bjps/51.1.147](https://doi.org/10.1093/bjps/51.1.147)), not read.

## Arguments in play

- The **instance-confirmation argument**: green emeralds are positive instances of both hypotheses, so a purely syntactic definition confirms both (Goodman pp. 74–75; Crupi §1.2 for blite under Hempel's theory).
- The **symmetry argument** against a qualitativeness criterion (Goodman p. 79; propositional core checked above).
- The **question-begging objection** to entrenchment and Goodman's reply (p. 98).
- The **prior-probability argument** and the objection that it needs a non-question-begging story (Crupi §3.6).
- The ravens argument, a sibling case in the same chapter: [raven paradox](raven-paradox.md).

## Thinkers who addressed it

- **David Hume** (1739–40) — the old problem Goodman starts from; Goodman: "Predictions, of course, pertain to what has not yet been observed. And they cannot be logically inferred from what has been observed; for what has happened imposes no logical restrictions on what will happen." (p. 63).
- **Rudolf Carnap** (1947) — the positional/qualitative reply (Cohnitz & Rossberg §5.3).
- **Nelson Goodman** (1955; London printing 1954, per Cohnitz & Rossberg's bibliography) — the riddle, grue and bleen, entrenchment, projectibility (*FFF* chs. III–IV).
- **W. V. Quine** (1969) — similarity and natural kinds (Bird & Tobin §1.2).
- **H. Gaifman** (1979), **Elliott Sober** (1994), **Branden Fitelson** (2008) — the prior-probability result (Crupi §3.6).
- **Saul Kripke** (1982), **Crispin Wright** (1984), **Ian Hacking** (1993; "On Kripke's and Goodman's Uses of ‘Grue’", *Philosophy* 68, 269–295, [doi:10.1017/s003181910004122x](https://doi.org/10.1017/s003181910004122x), not read) — grue and rule-following (Cohnitz & Rossberg §5.4, who also list their own 2006 book and Kowalenko 2022).
- **Colin Howson** (2000) — the water example against a natural-kinds restriction (Crupi §1.2).
- **David Chart** (2000), **Oliver Schulte** (1999, 2017) — the learning-theory dispute (Henderson §5.4).
- **John Norton**, **Samir Okasha** (2001–2005) — the no-rules reading (Henderson §4.2).
- Collections: Cohnitz & Rossberg point to "Stalker 1994 and Elgin 1997c for selections of important essays on the topic" (§5.4).

## Framings and reframings

- **The old problem dissolved.** Goodman: "What is commonly thought of as the Problem of Induction has been solved, or dissolved; and we face new problems that are not as yet very widely understood." (p. 63). His route is the "virtuous" circle between rules and inferences: "The point is that rules and particular inferences alike are justified by being brought into agreement with each other." (p. 67) — "All this applies equally well to induction." (p. 67); see [reflective equilibrium](../methods/reflective-equilibrium.md). Cohnitz & Rossberg's summary of his view: "Accordingly, the old problem of induction, which requires such a justification of induction, is a pseudo-problem." (§5.1).
- **From justification to projection.** Goodman: "Regularities are where you find them, and you can find them anywhere." (p. 82). Henderson places the riddle under the complaint that "The future only resembles the past in some respects, but not others." (§4.2).
- **A riddle about predicates, not about emeralds.** Cohnitz & Rossberg: the grue-paradox "points to the problem that in order to learn by induction, we need to make a distinction between projectible and non-projectible predicates." (preamble).

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — the filing term.
- [Validity](../vocabulary/validity.md) — the deductive sense, used for the propositional check; Goodman's "valid" in "predictions based on some regularities are valid" (p. 81) is said of inductive predictions, a departure from that contract.
- [Knowledge](../vocabulary/knowledge.md); [Classical logic](../methods/classical-logic.md) — the propositional check above.
- *Projectible*, *entrenchment*, *lawlike*, *grue/bleen*, *natural kind* — open work in [vocabulary](../vocabulary/index.md).
