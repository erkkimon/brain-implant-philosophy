---
type: article
about: concept
title: "Ellsberg paradox"
description: "An urn holds 30 red balls and 60 black and yellow in unknown proportion: many people prefer a bet on red to a bet on black, yet a bet on black-or-yellow to a bet on red-or-yellow — a pattern no single probability assignment fits, which Ellsberg (1961) set against Savage's Sure-thing Principle and called a response to 'ambiguity'. Savage-style defence, ambiguity models (Gilboa & Schmeidler 1989; Schmeidler 1989), re-description, and the Al-Najjar & Weinstein (2009) critique with Siniscalchi's reply."
tags: [problem, paradox, decision-theory, rationality, uncertainty]
timestamp: 2026-10-08T20:29:06Z
---

# Ellsberg paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md); sources graded as in [How claims are graded](../../conventions/how-claims-are-graded.md). One of the [problems](./index.md). Primary text: Daniel Ellsberg, "Risk, Ambiguity, and the Savage Axioms", *Quarterly Journal of Economics* 75(4), 1961, pp. 643–669 ([doi:10.2307/1884324](https://doi.org/10.2307/1884324); excerpt: `raw/ellsberg-1961-risk-ambiguity-savage-axioms.md`). Map: Briggs, [SEP Fall 2024 "Normative Theories of Rational Choice: Expected Utility"](https://plato.stanford.edu/archives/fall2024/entries/rationality-normative-utility/) §3.2.2 (excerpt: `raw/sep-rationality-normative-utility-fall-2024-ellsberg-independence.md`); Steele & Stefánsson, [SEP Fall 2024 "Decision Theory"](https://plato.stanford.edu/archives/fall2024/entries/decision-theory/) (excerpt: `raw/sep-decision-theory-fall-2024-sure-thing-maxmin-al-najjar.md`). Admitted from Wikipedia's List of paradoxes, revision 1376699902, "Decision theory" (excerpt: `raw/wikipedia-ellsberg-paradox-rev-1374491127-and-list-entry.md`).

## The question

Ellsberg's three-colour case: "Imagine an urn known to contain 30 red balls and 60 black and yellow balls, the latter in unknown proportion." (1961, p. 653). One ball is drawn. Action I pays $100 on red, II pays $100 on black; III pays $100 on red or yellow, IV pays $100 on black or yellow (p. 654):

|     | Red (30) | Black | Yellow |
|-----|----------|-------|--------|
| I   | $100     | $0    | $0     |
| II  | $0       | $100  | $0     |
| III | $100     | $0    | $100   |
| IV  | $0       | $100  | $100   |

Ellsberg reports: "A very frequent pattern of response is: action I preferred to II, and IV preferred to III. Less frequent is: II preferred to I, and III preferred to IV. Both of these, of course, violate the Sure-thing Principle, which requires the ordering of I to II to be preserved in III and IV (since the two pairs differ only in their third column, constant for each pair)." (p. 654). He adds that "for any values of the pay-offs, it is impossible to find probability numbers in terms of which these choices could be described -even roughly or approximately - as maximizing the mathematical expectation of utility." (p. 655).

The principle at stake is Savage's Postulate 2, which "he calls the "Sure-thing Principle" and which bears great weight in the analysis." (Ellsberg, p. 649). Steele & Stefánsson give its idea: "since we should be able to evaluate each outcome independently of other possible outcomes, we can safely ignore states of the world where two acts that we are comparing result in the same outcome." (SEP §3.1). Briggs states the case with win/lose $100 payoffs and white for black, and concludes: "Because they violate independence, the Ellsberg preferences are incompatible with expected utility theory. Again, this incompatibility does not require any assumptions about the relative utilities of winning $100 and losing $100." (SEP §3.2.2).

**Logic check (this implant, 2026-10-08; logic, not a position).** With utility increasing in money and a single probability *P*, I over II requires *P*(red) > *P*(black); IV over III requires *P*(black) + *P*(yellow) > *P*(red) + *P*(yellow), i.e. *P*(black) > *P*(red) — the same derivation Al-Najjar & Weinstein give (2009, p. 256). The propositional core, checked with `skills/tools/logic.py`:

```
P1: I_over_II -> RedMoreLikely
P2: IV_over_III -> BlackMoreLikely
P3: ~(RedMoreLikely & BlackMoreLikely)
C:  ~(I_over_II & IV_over_III)
VALID
```

Structural note (this implant): the pair of choices and a single probability-weighted ranking cannot both hold; the positions below differ on which of these to give up.

**The two-urn case.** "Urn I contains 100 red and black balls, but in a ratio entirely unknown to you; there may be from 0 to 100 red balls. In Urn II, you confirm that there are exactly 50 red and 50 black balls." (p. 650). "But if you are in the majority, you will report that you prefer to bet on RedII rather than RedI, and BlackII rather than BlackI." (p. 651), so that "it is impossible to infer probabilities from your choices" (p. 651). Ellsberg says these responses were gathered "under absolutely nonexperimental conditions" (p. 651).

**Name and label.** Ellsberg's paper does not use the word "paradox" (searched in the text read). Briggs (SEP §3.2.2) and Siniscalchi (2009, §1) call it "the Ellsberg paradox"; Wikipedia's list gives "People exhibit ambiguity aversion (as distinct from risk aversion), in contradiction with expected utility theory." (rev. 1376699902). Al-Najjar & Weinstein put "paradox" in scare quotes and explain: "Referring to choices in Ellsberg’s thought experiment as “paradoxical” implicitly confers on them an aura of rationality. Since we question the rationality of these choices, we prefer the more neutral term anomaly, which refers to “a deviation, irregularity, or an unexpected result”." (2009, p. 251, n. 2).

**Antecedent.** Wikipedia's article: "John Maynard Keynes published a version of the paradox in 1921." (rev. 1374491127, citing *A Treatise on Probability* pp. 75–76). In the 1921 Macmillan edition read here, Keynes compares two urns, one with equal proportions and one unknown: "It is evident that in either case the probability of drawing a white ball is 1/2 but that the weight of the argument in favour of this conclusion is greater in the first case." (ch. VI §6, p. 83; excerpt: `raw/keynes-1921-treatise-probability-weight-two-urns.md`). That passage poses no bet; pp. 75–76 were searched and contain no two-urn comparison. Ellsberg's own paper opens from Frank Knight's distinction between "measurable uncertainty" or "risk" and "unmeasurable uncertainty" (p. 643).

## Why it matters

- **A counterexample to expected utility as a standard of rationality.** Briggs: "Allais (1953) and Ellsberg (1961) propose examples of preferences that cannot be represented by an expected utility function, but that nonetheless seem rational." (SEP §3.2.2); such examples "suggest that maximizing expected utility is not necessary for rationality." (§3.2).
- **The most-discussed axiom.** "The axiom in Savage’s theory that has received most attention is the Sure Thing Principle." (Steele & Stefánsson, SEP §3.1).
- **A literature built on it.** Al-Najjar & Weinstein: "The all-consuming concern of the ambiguity aversion literature is the Ellsberg “paradox”." (2009, p. 251); "The seminal works of Schmeidler (1989) and Gilboa and Schmeidler (1989) laid a formal foundation for this enterprise by modifying Savage’s (1954) subjective expected utility model." (pp. 249–250).
- **Kin cases, as the sources pair them.** Briggs treats the [Allais paradox](https://plato.stanford.edu/archives/fall2024/entries/rationality-normative-utility/) beside it as a second violation of Independence, and lists the same three responses for both (§3.2.2). On Jeffrey's definition, Briggs says, "expected utility theory entails Independence in the presence of the assumption that the states are probabilistically independent of the acts." (§3.2.2) — "the condition that is violated in the Newcomb problem" (§1.1; see [Newcomb's problem](newcombs-problem.md)). Briggs treats [the St. Petersburg game](st-petersburg-paradox.md) in a separate section (§3.2.4, unbounded utility) and does not link the two.

## Positions taken

Grouped first as Briggs groups the responses to "the Allais and Ellsberg paradoxes" (SEP §3.2.2), then the ambiguity models and the dispute over them. No position is ranked here.

- **The preferences are irrational; keep expected utility.** "First, one might follow Savage (101 ff) and Raiffa (1968, 80–86), and defend expected utility theory on the grounds that the Allais and Ellsberg preferences are irrational." (Briggs §3.2.2). Ellsberg reports respondents who "do not violate the axioms, or say they won't, even in these situations (e.g., G. Debreu, R. Schlaiffer, P. Samuelson)" (p. 655), and gives the Savage advocate's objection to his own rule: "Why are you double-counting the "worst" possibilities?" (p. 662).
- **The preferences are permissible; expected utility fails as a norm.** "Second, one might follow Buchak (2013) and claim that that the Allais and Ellsberg preferences are rationally permissible, so that expected utility theory fails as a normative theory of rationality." (Briggs §3.2.2). Ellsberg's own stance: "Are they foolish? It is not the object of this paper to judge that." (p. 669), and "Indeed, it seems out of the question summarily to judge their behavior as irrational: I am included among them." (p. 669).
- **Re-describe the outcomes.** "Third, one might follow Loomes and Sugden (1986), Weirich (1986), and Pope (1995) and argue that the outcomes in the Allais and Ellsberg paradoxes can be re-described to accommodate the Allais and Ellsberg preferences." (Briggs §3.2.2).
  - *Objection and constraint:* "Broome (1991, Ch. 5) raises a worry about this re-description solution. Any preferences can be justified by re-describing the space of outcomes, thus rendering the axioms of expected utility theory devoid of content." Broome's added constraint lets an expected-utility theorist count the preferences as rational "if, and only if, there is a non-monetary difference that justifies placing outcomes of equal monetary value at different spots in one’s preference ordering." (Briggs §3.2.2).
- **Ambiguity is a third dimension of choice (Ellsberg 1961).** "What is at issue might be called the ambiguity of this information, a quality depending on the amount, type, reliability and "unanimity" of information, and giving rise to one's degree of "confidence" in an estimate of relative likelihoods." (p. 657). His rule weighs a best-estimate distribution against the worst expectation over a set of "reasonable" distributions; such a criterion "may appeal to a conservative person as deserving some weight" (p. 662).
- **Maxmin expected utility (Gilboa & Schmeidler 1989).** Gilboa & Schmeidler, *Maxmin expected utility with non-unique prior*, *Journal of Mathematical Economics* 18(2), 141–153 ([doi:10.1016/0304-4068(89)90018-9](https://doi.org/10.1016/0304-4068(89)90018-9); bibliographic data verified, paper not read). As Al-Najjar & Weinstein state it, value is the minimum expected utility over a set *C* of priors; "When C is a singleton, this reduces to standard expected utility." (2009, p. 257), and the three-colour choices fit a set with *P*(black) fixed and the other two colours free (Example 1, p. 257). Steele & Stefánsson: "The Maxmin-EU rule, for instance, recommends picking the action with greatest minimum expected utility (see Gilboa and Schmeidler 1989; Walley 1991). The rule is simple to use, but arguably much too cautious, paying no attention at all to the full spread of expected utilities." (SEP §5.2) — their assessment; they report α-Maxmin and the confidence-weighted rule of Klibanoff et al. (2005) as alternatives.
- **Non-additive probability, Choquet expected utility (Schmeidler 1989).** Schmeidler, *Subjective Probability and Expected Utility without Additivity*, *Econometrica* 57(3), 571–587 ([doi:10.2307/1911053](https://doi.org/10.2307/1911053); bibliographic data verified, paper not read). Al-Najjar & Weinstein list "capacities" among the belief-objects of this literature (p. 250); Wikipedia's article lists "Choquet expected utility" as a modification of expected utility (rev. 1374491127).
- **Not rational, an anomaly from misapplied heuristics (Al-Najjar & Weinstein 2009).** ([doi:10.1017/S026626710999023X](https://doi.org/10.1017/S026626710999023X); excerpt: `raw/al-najjar-weinstein-2009-ambiguity-aversion-critical-assessment.md`). "First, admitting Ellsberg choices as rational leads to behaviour, such as sensitivity to irrelevant sunk cost, or aversion to information, which most economists would consider absurd or irrational." (p. 249). "These choices can arise when decision makers form heuristics that serve them well in real-life situations where odds are manipulable, and misapply them to experimental settings." (p. 249); they credit the point to "Myerson (1991) and others" (p. 255). Steele & Stefánsson: "the costs of any departure from EU theory are well highlighted by Al-Najjar and Weinstein (2009)" (SEP §6.2) — their assessment; they point to Buchak (2010, 2013) on the other side.
  - *Reply (Siniscalchi 2009,* [doi:10.1017/S0266267109990277](https://doi.org/10.1017/S0266267109990277); *excerpt:* `raw/siniscalchi-2009-two-out-of-three-reply-al-najjar-weinstein.md`*):* "perhaps NW themselves would be embarassed by these choices, but there is no fundamental canon of rationality according to which every DM should feel similarly uncomfortable." (§1); rejecting free information "simply reflects a trade-off between the intrinsic value of information, which is positive even in the presence of ambiguity, and the value of commitment." (abstract); on the heuristic account, "some recent experiments actually attempt to control for possible misapplied heuristics: see for instance Hey, Lotito, and Maffioletti (2008)." (§5).
- **Prior knowledge as the source (competence; comparative ignorance).** Wikipedia's article reports these hypotheses (Heath & Tversky 1991, [doi:10.1007/bf00057884](https://doi.org/10.1007/bf00057884); Fox & Tversky 1995, [doi:10.2307/2946693](https://doi.org/10.2307/2946693)): "Both theories attribute the source of the ambiguity aversion to the participant's pre-existing knowledge." (rev. 1374491127). The papers were not read here.

**The evidence, as reported.** Ellsberg's observations were "nonexperimental" (p. 655, n. 6). Siniscalchi: "As an empirical matter, the amount of experimental evidence confirming Ellsberg’s observations is, by now, rather substantial." (2009, §5). Al-Najjar & Weinstein argue the same findings "are equally consistent with other explanations" (2009, p. 276). Neither side's experimental papers were read here.

## Arguments in play

(none recorded as separate argument pages yet). The incompatibility derivation is under The question; the Sure-thing rationale as Ellsberg gives it: "So, since he would not prefer IV to III "in either event," he should not prefer IV when he does not know whether or not the third column will obtain." (p. 649).

## Thinkers who addressed it

- **Frank Knight** (1921) — risk versus unmeasurable uncertainty, the frame Ellsberg starts from (Ellsberg p. 643).
- **John Maynard Keynes** (1921) — two urns, equal probability, unequal "weight" (*Treatise* ch. VI §6, p. 83); credited with "a version" by Wikipedia (rev. 1374491127).
- **Leonard J. Savage** (1954) — the Sure-thing Principle (P2); per Ellsberg, among those who wished to persist in violating it "when last tested by me" (p. 656); Briggs lists him with the defence of expected utility (§3.2.2).
- **Daniel Ellsberg** (1961) — the cases, "ambiguity", the conservative rule.
- **Kenneth Arrow** — a related four-event example (Ellsberg p. 654, n. 4).
- **Paul Samuelson, Gérard Debreu, Robert Schlaifer** (as "Schlaiffer"), **Jacob Marschak, Norman Dalkey, Howard Raiffa** — respondents as Ellsberg reports them (pp. 655–656); **Raiffa** (1968) with the defence (Briggs).
- **Itzhak Gilboa & David Schmeidler** (1989), **Schmeidler** (1989) — maxmin expected utility; non-additive probability.
- **Graham Loomes & Robert Sugden** (1986), **Paul Weirich** (1986), **Robert Pope** (1995), **John Broome** (1991), **Lara Buchak** (2013) — as Briggs reports (§3.2.2).
- **Peter Klibanoff, Massimo Marinacci & Sujoy Mukerji** (2005) — smooth, confidence-weighted model (Steele & Stefánsson §5.2).
- **Nabil Al-Najjar & Jonathan Weinstein** (2009), **Marciano Siniscalchi** (2009) — the critique and a reply, in a symposium of *Economics and Philosophy* 25(3) that also carried comments by Gilboa, Postlewaite & Schmeidler, Mukerji and Nehring (titles verified via Crossref, not read).

## Framings and reframings

- **Anomaly, not paradox.** Al-Najjar & Weinstein's relabelling (2009, p. 251, n. 2), quoted under The question.
- **A game against the experimenter.** Al-Najjar & Weinstein: "ambiguity-sensitive behaviour is observationally indistinguishable from the behaviour of a player in a game." (2009, p. 276) — read by them as support for the heuristic account.
- **Taste or belief.** Al-Najjar & Weinstein define the literature by the view that "the decision maker’s attitude towards ambiguity is a matter of taste" (p. 250); Siniscalchi accepts the description: attitudes toward ambiguity "are viewed as a matter of taste, just like her attitudes toward risk." (§1).
- **Imprecise probabilities.** Steele & Stefánsson place maxmin-type rules under sets of probability functions representing belief (SEP §5.2), without naming Ellsberg.
- **Ellsberg's own question.** The paper ends: "Are they clearly mistaken?" (p. 669).

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — the label is disputed (see The question).
- [Validity](../vocabulary/validity.md) — the incompatibility derivation.
- Sure-thing principle, Independence, ambiguity, ambiguity aversion, Knightian uncertainty, maxmin expected utility, capacity, Choquet integral — open work in [vocabulary](../vocabulary/index.md).

Related problems: [Newcomb's problem](newcombs-problem.md) (act–state independence, Briggs §1.1), [the St. Petersburg paradox](st-petersburg-paradox.md) (both counterexamples in Briggs §3.2). Branch: [Problems](./index.md).
