---
type: article
about: concept
title: "Newcomb's problem: one box or two?"
description: "A reliable predictor has filled an opaque box with a million dollars only if it predicted you would take that box alone; a transparent box holds a thousand. Dominance says take both, conditional expected utility says take one — the case, from William Newcomb via Nozick (1969), that split causal from evidential decision theory."
tags: [problem, paradox, decision-theory, rationality]
timestamp: 2026-10-08T20:29:06Z
---

# Newcomb's problem

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
sources graded as in [How claims are graded](../../conventions/how-claims-are-graded.md).
Sources for the map: Nozick,
[1969](https://doi.org/10.1007/978-94-017-1466-2_7)
(excerpt: `raw/nozick-1969-newcombs-problem-two-principles-of-choice.md`);
Weirich,
[SEP Fall 2024 "Causal Decision Theory"](https://plato.stanford.edu/archives/fall2024/entries/decision-causal/)
(excerpt: `raw/sep-decision-causal-fall-2024-newcombs-problem.md`).

## The question

Nozick's statement: "There are two boxes, (B1) and (B2). (B1) contains $1000. (B2) contains either $1 000 000 ($ M), or nothing." (1969, p. 114). A being whose predictions you trust has already acted on this rule:
"(I) If the being predicts you will take what is in both boxes, he does not put the $ M in the second box. (II) If the being predicts you will take only what is in the second box, he does put the $ M in the second box." (p. 115).
You may take both boxes or only the second. If the being predicts that you
will randomise, it leaves the second box empty (p. 143, note 1).

Nozick: "There are two plausible looking and highly intuitive arguments which require different decisions. The problem is to explain why one of them is not legitimately applied to this choice situation." (p. 115).
The first argument ends "Therefore I should take only what is in the
second box" (p. 115); the second, from the fact that the contents are
"already fixed and determined", ends "So I should take what is in both
boxes" (p. 115).

Weirich's decision-theoretic form (SEP, §2.1): "Because the outcome of two-boxing is better by $T than the outcome of one-boxing given each prediction, two-boxing dominates one-boxing. Two-boxing is the rational choice according to the principle of dominance."
And: "Hence, using conditional probabilities to compute expected utilities, one-boxing’s expected utility exceeds two-boxing’s expected utility. One-boxing is the rational choice according to the principle of expected-utility maximization."

|                | predicted: one box | predicted: two boxes |
|----------------|--------------------|----------------------|
| take one box   | $M                 | $0                   |
| take two boxes | $M + $T            | $T                   |

(Weirich's Figure 1, §2.1; $M = $1,000,000, $T = $1,000.)

**Arithmetic check (this implant, 2026-09-27; mathematics, not a
position).** Let *p* be the probability that the prediction matches the
choice, conditional on each choice, and take utility as linear in dollars.
Then EU(one) = *p*·1,000,000 and EU(two) = 1,000 + (1 − *p*)·1,000,000;
EU(one) > EU(two) exactly when *p* > 1,001,000 / 2,000,000 = 0.5005.
Nozick makes the related observation that at *p* = .6 the conditional
expected utility still favours one box, yet "if the probability of the beings predicting correctly were only .6, each of us would choose to take what is in both boxes" (p. 140),
and concludes "It is crucial that the predictor is almost certain to be correct." (p. 140).
Whether *p* here should be a conditional probability at all is the point
in dispute (see Positions).

**Origin.** Nozick: "It was constructed by a physicist, Dr. William Newcomb, of the Livermore Radiation Laboratories in California. I first heard the problem, in 1963, from his friend Professor Martin David Kruskal of the Princeton University Department of Astrophysical Sciences." (p. 143, note *).
He adds: "It is a beautiful problem. I wish it were mine." (ibid.). Weirich
reports the same attribution (§2.1). Kuhn calls it "a puzzle popularized among philosophers in Nozick" ([SEP Fall 2024 "Prisoner’s Dilemma"](https://plato.stanford.edu/archives/fall2024/entries/prisoner-dilemma/), §7; excerpt: `raw/sep-prisoner-dilemma-fall-2024-newcomb-and-replicas.md`).

Whether it is a [paradox](../vocabulary/paradox.md) in this implant's
normative sense depends on the reading: Nozick presents two arguments from
acceptable-looking premises to incompatible conclusions (p. 115), and
Weirich calls it "a dilemma for decision theory" (§2.1).

## Why it matters

- **Two principles of choice collide.** Nozick states the Expected Utility
  Principle and the Dominance Principle (p. 118) and asks which to follow
  when they conflict; Weirich: "He constructed an example in which the standard principle of dominance conflicts with the standard principle of expected-utility maximization." (§2.1).
- **It divides decision theory.** Gibbard and Harper "distinguished causal decision theory, which uses probabilities of subjunctive conditionals, from evidential decision theory, which uses conditional probabilities." (Weirich §2.2).
- **Realistic versions.** Weirich: "The essential feature of Newcomb’s problem is an inferior act’s correlation with a good state that it does not causally promote." (§2.1), with "medical Newcomb problems" as instances.
- **Game theory.** "Also, Allan Gibbard and William Harper (1978: Sec. 12) and David Lewis (1979) observe that a Prisoner’s Dilemma with psychological twins poses a Newcomb problem for each player." (Weirich §2.1). Kuhn reports that "Lewis argues that the link to the PD suggests that situations where the two decisions diverge are not so unusual" (SEP "Prisoner’s Dilemma", §7).

## Positions taken

Grouped as Weirich's entry groups them (§§2.2–2.5, 3.6, 4). No position is
ranked here. The entry's author, Weirich, also gives assessments of his own
(for example §2.5, below); each is marked as his.

- **Two-boxing by causal decision theory (CDT).** Stalnaker's 1972 letter
  to Lewis proposed "probabilities of conditionals in place of conditional
  probabilities" ([Stalnaker 1972, printed 1981](https://doi.org/10.1007/978-94-009-9117-0_7);
  Weirich §2.2); Gibbard & Harper
  ([1978](https://doi.org/10.1007/978-94-009-9789-9_5)) "elaborated and made
  public Stalnaker’s resolution" (§2.2). Skyrms
  ([1980; 1982](https://doi.org/10.2307/2026547)) and Lewis
  ([1981](https://doi.org/10.1080/00048408112340011)) gave versions without
  subjunctive conditionals that "yield the same recommendations" in
  Newcomb's problem (§2.3). Nozick himself: "I believe that one should take what is in both boxes. I fear that the considerations I have adduced thus far will not convince those proponents of taking only what is in the second box." (1969, p. 135).
  Lewis: "Others, and I for one, think it rational to take both boxes." ([1981, Noûs](https://doi.org/10.2307/2215439), p. 377; excerpt: `raw/lewis-1981-why-aincha-rich.md`).
  - *Case for:* the dominance argument (Nozick's Second Argument,
    p. 115); Lewis: "If I took only one box, I would be poorer by a thousand than I will be after taking both." (p. 377); Sobel (1994: Chap. 5) argues "Efficacy still trumps auspiciousness" (Weirich §2.5).
  - *Case against:* "The most common objection to causal decision theory is that it yields the wrong choice in Newcomb’s problem." (Weirich §2.5, reporting the objection).
- **One-boxing.** "Terry Horgan (1981 [1985]), Paul Horwich (1987: Chap. 11), and Caspar Hare and Brian Hedden (2016) for example, promote one-boxing." (Weirich §2.5; [Horgan 1981](https://doi.org/10.2307/2026128)).
  Lewis ties one-boxing to Jeffrey's theory: "Their decision theory is that
  of Jeffrey" (1981, p. 377).
  - *Case for:* "The main rationale for one-boxing is that one-boxers fare better than do two-boxers." (Weirich §2.5); the one-boxers' taunt as Lewis reports it: "if you're so smart, why ain'cha rich?" (1981, p. 377); Nozick's First Argument (p. 115).
  - *Case against:* "Causal decision theorists respond that Newcomb’s problem is an unusual case that rewards irrationality. One-boxing is irrational even if one-boxers prosper." (Weirich §2.5).
    Lewis: "The reason why we are not rich is that the riches were reserved for the irrational." (p. 377).
  - *Variant:* "Some theorists hold that one-boxing is plainly rational if the prediction is completely reliable." Weirich (§2.5) judges that "This view oversimplifies."
- **Evidential decision theory (EDT) that yields two-boxing.** Jeffrey
  ([1965] 1983, 2004) "formulates decision principles that do not rely on causal relations" (§2.5). Eells ([1981](https://doi.org/10.1007/BF01063891), 1982) "contends that evidential decision theory yields causal decision theory’s recommendations but, more economically, without reliance on causal apparatus" (§2.5); Horgan (1981) and Price ([1986](https://doi.org/10.1007/BF00540068)) "make similar points" (§2.5).
  This is the **tickle defence**: "it assumes that an introspected condition screens off the correlation between choice and prediction." (§2.5).
  - *Case against:* Lewis (1981: 10–11) and Pollock (2010) argue that EDT
    "may not do that correctly" for agents without such self-knowledge
    (§2.5); "Horwich (1987: Chap. 11) rejects Eells’s argument" (§2.5).
    Eells ([1984a](https://doi.org/10.1007/BF00141675)) replied with "a
    dynamic version of the tickle defense"; Sobel (1994: Chap. 2) "concludes that even in cases where evidential decision theory yields the right recommendation, it does not yield it for the right reasons." (§2.5).
- **Ratification.** "Jeffrey used ratification as a means of making evidential decision theory yield the same recommendations as causal decision theory. In Newcomb’s problem, for instance, two-boxing is the only self-ratifying option." (§3.6).
  Jeffrey (2004: 113n) "concedes" it does not secure agreement in all
  cases, and Joyce (2007) argues its motivation "appeals to causal
  relations" (§3.6).
- **Evidential decision theory against CDT.** "Ahmed (2014a) champions evidential decision theory and advances several objections to causal decision theory." Weirich (§2.5) adds that "His objections assume some controversial points about rational choice".
- **Two-boxing without causation.** An objection that "concedes that two-boxing is the rational choice in Newcomb’s problem but rejects causal principles of choice that yield two-boxing" (§2.5).
- **Rational disposition, rational act.** "A way of reconciling the two sides of the debate about Newcomb’s problem acknowledges that a rational person should prepare for the problem by cultivating a disposition to one-box." CDT "may conclude that cultivating a disposition to one-box is rational although one-boxing itself is irrational." (§2.5).
- **CDT that one-boxes.** "Wolfgang Spohn (2012) constructs for Newcomb’s problem a causal model that distinguishes a decision and its execution and argues that given the model causal decision theory recommends one-boxing." (§4; [Spohn 2012](https://doi.org/10.1007/s11229-011-0023-5)).
- **A blend.** "Price (2012) proposes a blend of evidential and causal decision theory" (§2.5).

**Distribution, as reported.** Nozick's informal report: "To almost everyone it is perfectly clear and obvious what should be done. The difficulty is that these people seem to divide almost evenly on the problem, with large numbers thinking that the opposing half is just being silly." (1969, p. 117).
Weirich (§4): "Causal decision theory is the prevailing form of decision theory among those who distinguish causal and evidential decision theory."
Kuhn (§7): "there remain people committed to each view". Survey data
(opinion data, not a verdict; excerpt:
`raw/philpapers-2009-2020-surveys-newcombs-problem.md`):

| Survey | Population | Two boxes | One box | Other / undecided |
|--------|-----------|-----------|---------|-------------------|
| PhilPapers 2009 | target faculty, N = 931 | 31.4 % | 21.3 % | Other 47.4 % |
| PhilPapers 2020 | all respondents, N = 1071 | 39.03 % | 31.19 % | agnostic/undecided 22.41 %; other rows as in the excerpt |

2009: [results page](https://philpapers.org/surveys/results.pl); paper
[Bourget & Chalmers 2014](https://doi.org/10.1007/s11098-013-0259-7).
2020: [results page](https://survey2020.philpeople.org/survey/results/4886)
(read in an Internet Archive copy); paper
[Bourget & Chalmers 2023](https://doi.org/10.3998/phimp.2109). The 2020
page itself says: "These results should not be used for comparison to 2009 results due to different populations and parameters."

## Arguments in play

(none recorded as separate argument pages yet). Nozick's First and Second
Arguments (p. 115) and Lewis's "why ain'cha rich?" exchange
(p. 377) are quoted above.

## Thinkers who addressed it

- **William Newcomb** (physicist, Livermore) — constructed it; heard by
  Nozick in 1963 via **Martin David Kruskal** (Nozick 1969, p. 143).
- **Richard Jeffrey** (1965) — evidential decision theory; later
  ratification (Weirich §§2.4, 3.6).
- **Robert Nozick** (1969) — published it; two boxes, tentatively (p. 135).
- **Robert Stalnaker** (1972 letter) — probabilities of conditionals (§2.2).
- **Allan Gibbard & William Harper** (1978) — causal vs. evidential; V and
  U (§2.2).
- **Brian Skyrms** (1980, 1982), **David Lewis** (1979, 1981) — CDT
  variants; Lewis on the PD and "why ain'cha rich?".
- **Terry Horgan** (1981), **Ellery Eells** (1981, 1982, 1984),
  **Huw Price** (1986, 2012), **Paul Horwich** (1987), **Jordan Howard
  Sobel** (1994), **James Joyce** (2007), **Wolfgang Spohn** (2012),
  **Arif Ahmed** (2014, 2018), **Caspar Hare & Brian Hedden** (2016),
  **Kenny Easwaran** — positions as above (Weirich §§2.1–4).

## Framings and reframings

- **Not about expected utility alone.** Nozick: "it is not the expected
  utility principle which leads some people to choose only what is in the
  second box" (p. 140), citing the .6 case above.
- **Dominance restricted.** Nozick's proposal that where states are "already fixed and determined, where the actions do not affect whether or not the states obtain, then it seems that it is legitimate to use the dominance principle" (p. 127).
- **A standoff.** Lewis on the "why ain'cha rich?" exchange: "I regret to say that alternative (1) appears to be correct. At any rate, the obvious way to argue for alternative (2) is a failure. So it's a standoff." (1981, p. 378). Alternative (1) is that the moral is "one more piece of two-boxist doctrine that one-boxers may consistently deny".
- **A family of problems.** Easwaran ([doi](https://doi.org/10.1007/s11229-019-02272-z)) "distinguishes Newcomb-like problems according to opportunities for causal intervention" (Weirich §2.1); Hurley (1991) and Bermúdez (2015) argue the PD and Newcomb's problem "are significantly different" (Kuhn §7).

Not in the excerpts held: "functional decision theory" and other proposals
from outside academic philosophy journals; they are left out until a source
is fetched.

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — see The question.
- [Validity](../vocabulary/validity.md) — both of Nozick's arguments are
  presented as valid; the dispute is over premises and principles.
- Dominance, expected utility, conditional probability, causal and
  evidential decision theory, ratification, screening off — open work in
  [vocabulary](../vocabulary/index.md).

Related problems: [Ellsberg paradox](ellsberg-paradox.md) (Briggs §§1.1, 3.2.2), [the argument from free will](argument-from-free-will.md) (foreknowledge), [the sorites paradox](sorites-paradox.md),
[the liar paradox](liar-paradox.md),
[the surprise examination paradox](surprise-examination-paradox.md) (also
about prediction). Branch: [Problems](./index.md).

Related thinkers: [Nozick](../thinkers/nozick.md).
