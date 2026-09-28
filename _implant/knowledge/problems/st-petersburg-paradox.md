---
type: article
about: concept
title: "The St Petersburg paradox"
description: "A fair coin is tossed until it lands heads and the prize doubles with every toss, so the expected payoff is infinite, yet few would pay much to play: Nicolaus Bernoulli's 1713 problem, Cramer's 1728 and Daniel Bernoulli's 1738 utility answers, Menger's restoration, and the later responses — bounded utility, unrealistic assumptions, negligible probabilities, relative expectations — with the Pasadena game as sequel, each with its owner."
tags: [problem, paradox, decision-theory, probability, rationality]
timestamp: 2026-09-28T07:01:48Z
---

# The St Petersburg paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
claim grades as in [How claims are graded](../../conventions/how-claims-are-graded.md).
Part of the [problems](./index.md) branch. Map: Martin Peterson,
[SEP Fall 2024 "The St. Petersburg Paradox"](https://plato.stanford.edu/archives/fall2024/entries/paradox-stpetersburg/)
(first published 2019-07-30, revised 2023-08-01; excerpt:
`raw/sep-paradox-stpetersburg-fall-2024-history-and-responses.md`). Primary
texts: the 1713–1732 letters in Pulskamp's translation
([PDF, Internet Archive](https://web.archive.org/web/20200725100737/http://cerebro.xu.edu/math/Sources/NBernoulli/correspondence_petersburg_game.pdf);
excerpt: `raw/bernoulli-n-cramer-1713-1732-correspondence-st-petersburg-pulskamp.md`)
and Daniel Bernoulli 1738 in Sommer's translation
([Econometrica 1954, doi:10.2307/1909829](https://doi.org/10.2307/1909829);
excerpt: `raw/bernoulli-d-1738-specimen-measurement-of-risk-sommer.md`).

## The question

Peterson's standard version: "A fair coin is flipped until it comes up heads the first time. At that point the player wins \(\$2^n,\) where n is the number of times the coin was flipped. How much should one be willing to pay for playing this game?" (SEP, preamble).
Expected value multiplies each prize by its probability and adds the terms;
here every term is 1.

**Mathematics (this implant, 2026-09-27; a computation, not a position).**
Heads first on toss *n* has probability (1/2)^*n* and pays 2^*n*, so the
*n*-th term is (1/2)^*n* · 2^*n* = 1 and the partial sum to *N* is *N*.
Computed with exact fractions in Python:

```
partial sum to N=1: 1
partial sum to N=10: 10
partial sum to N=100: 100
partial sum to N=1000: 1000
```

For any bound *B*, the partial sum exceeds *B* once *N* > *B*; the series
Σ_{n≥1} (1/2)^n 2^n diverges. Peterson's display sets the sum equal to ∞ and adds: "(Some would say that the sum approaches infinity, not that it is infinite. We will discuss this distinction in Section 2.)" (preamble).

Peterson's statement of the puzzle: "The “paradox” consists in the fact that our best theory of rational choice seems to entail that it would be rational to pay any finite fee for a single opportunity to play the St. Petersburg game, even though it is almost certain that the player will win a very modest amount." (preamble).
On the word: "In a strict logical sense, the St. Petersburg paradox is not a paradox because no formal contradiction is derived. However, to claim that a rational agent should pay millions, or even billions, for playing this game seems absurd." (Peterson, preamble; compare this implant's sense of [paradox](../vocabulary/paradox.md)).

**A stronger version (Peterson §2).** Peterson turns it into "three incompatible claims": (1) "The amount of utility it is rational to pay for playing (or selling the right to play) the St. Petersburg game is higher than every finite amount of utility."
(2) "The buyer knows that the actual amount of utility he or she will actually receive is finite." (3) "It is not rational to knowingly pay more for something than one will receive."
*Logic check (this implant).* With a bridge premise added here, not
Peterson's wording — *k*: if (1) and (2), it is rational to knowingly pay
more than one will receive — the set {(1), (2), (1)&(2)→*k*, (3) = ¬*k*}
was run through `skills/tools/logic.py`:

```
  P1: a    [a]
  P2: b    [b]
  P3: (a & b) -> k    [((a & b) -> k)]
  P4: ~k    [~k]
  C:  q & ~q    [(q & ~q)]

VALID
premises are jointly inconsistent — argument is vacuously valid
```

So at least one of the four must go; the responses below differ over which.

**Origin.** Nicolaus Bernoulli's "Fifth Problem" (letter to Montmort,
9 September 1713, printed in Montmort's *Essay d'analyse*, p. 402) uses a
die, not a coin: "One asks the same thing if A promises to B to give him some coins in this progression 1, 2, 4, 8, 16 etc. or 1, 3, 9, 27 etc. or 1, 4, 9, 16, 25 etc. or 1, 8, 27, 64 instead of 1, 2, 3, 4, 5 etc. as beforehand. Although for the most part these problems are not difficult, you will find however something most curious."
Montmort replied that they "have no difficulty, the only concern is to find the sum of the series" (15 November 1713). Nicolaus (20 February 1714): "But it would follow thence that B must give to A an infinite sum and even more than infinity (if it is permitted to speak thus)".
Gabriel Cramer (21 May 1728) gave the coin form and the word: "The paradox consists in this that the calculation gives for the equivalent that A must give to B an infinite sum, which would seem absurd, since there is no person of good sense, who would wish to give 20 coins." (Pulskamp tr.).
The name: Peterson reports that it "is named after one of the leading scientific journals of the eighteenth century, Commentarii Academiae Scientiarum Imperialis Petropolitanae" (§1), where Daniel Bernoulli's paper appeared in 1738. Peterson's assessments of the early exchange: "It seems that Montmort did not immediately get Nicolaus’ point." and Nicolaus's argument "was also a bit sketchy and would not impress contemporary mathematicians." (§1).

## Why it matters

- **The expected-value rule.** Daniel Bernoulli's paper opens with the rule on which "Expected values are computed by multiplying each possible gain by the number of ways in which it can occur, and then dividing the sum of these products by the total number of possible cases" (§1, p. 23) and argues "The rule established in §1 must, therefore, be discarded" in favour of utility (§3, p. 24).
- **Utility theory.** Peterson: Cramer's proposal "revolutionized the emerging field of decision theory" and gives "the first clear statement of what contemporary decision theorists and economists refer to as decreasing marginal utility" (§1).
- **Decision theory now.** Peterson: it "continues to be a reliable source for new puzzles and insights in decision theory" (preamble). His closing assessment: "For hundreds of years, decision theorists have agreed that rational agents should maximize expected utility." — and "The rich and growing literature on the many puzzles inspired by the St. Petersburg paradox indicate that this might have been a mistake. Perhaps the principle of maximizing expected utility should be replaced by some entirely different principle?" (§7).
- **Contagion.** "Hájek and Smithson (2012) point out that the St Petersburg paradox is contagious in the following sense: As long as you assign some nonzero probability to the hypothesis that the bank’s promise is credible, the expected utility will be infinite no matter how low your credence in the hypothesis is." (Peterson §3; [doi:10.1007/s11229-011-0033-3](https://doi.org/10.1007/s11229-011-0033-3)).

## Positions taken

Grouped as Peterson's entry groups them (§§1–7). None is ranked here.
Peterson's own assessments are marked as his.

- **Diminishing marginal utility of money (Cramer 1728; Daniel Bernoulli 1738).**
  Cramer: "the mathematicians value money in proportion to its quantity, and men of good sense in proportion to the usage that they may make of it."
  Capping prizes at 2^24 coins, "my expectation is reduced to 13 coins"; in a postscript, "If one wishes to suppose that the moral value of goods was as the square root of the mathematical quantities", the equivalent comes out "less than 3" (Letter 8, 1728). Daniel Bernoulli: value "must not be based on its price, but rather on the utility it yields" (§3, p. 24), and "any increase in wealth, no matter how insignificant, will always result in an increase in utility which is inversely proportionate to the quantity of goods already possessed" (§5, p. 25), giving a "logarithmic curve" (§10, p. 28).
  For a player who "owned nothing at all" the game is worth "two ducats, precisely", "approximately three ducats" with ten, "four" with a hundred and "six" with a thousand (§19, p. 32). He acknowledges Cramer: "Indeed I have found his theory so similar to mine that it seems miraculous that we independently reached such close agreement on this sort of subject." (p. 33).
  *Arithmetic check (this implant, Python).* Cramer's cap (his schedule pays
  2^(n−1)): Σ (1/2)^n · min(2^(n−1), 2^24) = 13.0. Square root: the
  equivalent (Σ (1/2)^n √2^(n−1))² = 1/(6 − 4√2) ≈ 2.914. Bernoulli's
  schedule with Menger's formula (footnote 10), D = Π(a + 2^(n−1))^(1/2^n) − a:
  fortune 0 → 2.000, 10 → 3.043, 100 → 4.389, 1000 → 5.972 ducats.
  - *Against — the prizes can be raised (Menger 1934).* Peterson: "The paradox can be restored by increasing the values of the outcomes up to the point at which the agent is fully compensated for her decreasing marginal utility of money (see Menger 1934 [1979])." ([doi:10.1007/BF01311578](https://doi.org/10.1007/BF01311578); tr. [doi:10.1007/978-94-009-9347-1_25](https://doi.org/10.1007/978-94-009-9347-1_25)). Peterson reports that "modern decision theorists agree that this solution is too narrow" (§2), and restates the game with prizes of "\(2^n\) units of utility" (§2).
  - *Against — the question is the fair price, not personal utility (Nicolaus Bernoulli).* To Cramer, the answer "does not demonstrate the true reason for the difference that there is between the mathematical expectation and common estimate" (Letter 9, 1728); to Daniel, "it does not solve the knot of the problem in question", since "the concern is to find how much a player is obliged according to justice or according to equity to give to another" (Letter 18, 1732). Daniel's report of the same objection: "the case is different if a third person, somewhat in the position of a judge, is to evaluate the prospects" (1738, p. 33).
- **Bounded utility (Arrow 1970; Bassett 1987).** "Arrow (1970: 92) suggests that the utility function of a rational agent should be “taken to be a bounded function.… since such an assumption is needed to avoid [the St. Petersburg] paradox”. Basset (1987) makes a similar point; see also Samuelson (1977) and McClennen (1994)." (Peterson §4; [Bassett doi:10.1215/00182702-19-4-517](https://doi.org/10.1215/00182702-19-4-517)).
  Peterson reports that the axiomatisations of Ramsey, von Neumann & Morgenstern and Savage "all entail that the decision maker’s utility function is bounded", and that "The crucial assumption is that rationally permissible preferences over lotteries are continuous." (§4).
  - *Against:* "A possible view is that anyone who is offered to play the St. Petersburg game has reason to reject the continuity axiom." (Peterson §4); alternatives he names: utility not defined by lottery preferences (Luce 1959) or with continuity "explicitly rejected" (Skala 1975) (§4).
- **The game is unrealistic (Buffon, Fontaine, Jeffrey 1983, Brito 1975).** "For instance, Jeffrey (1983: 154) argues that “anyone who offers to let the agent play the St. Petersburg gamble is a liar, for he is pretending to have an indefinitely large bank”. Similar objections were raised in the eighteenth century by Buffon and Fontaine (see Dutka 1988)." (Peterson §3; [Dutka doi:10.1007/BF00329984](https://doi.org/10.1007/BF00329984)). "Brito (1975) claims that the coin flipping may simply take too long time." (§3; [doi:10.1016/0022-0531(75)90067-8](https://doi.org/10.1016/0022-0531(75)90067-8)).
  An earlier form of the bank point is in the letters: Nicolaus wrote to Daniel, "As for the last 2 of the 5 problems I do not agree with you that one is able to resolve them in valuing the riches of the one with whom one is able to play." (Letter 15, 1730); Daniel replied: "The last two problems are so vague that I have no more to say to you, if you do not believe that it is necessary to know the sum that the other is in position to pay." (Letter 16, 1731).
  - *Against:* the contagion point above (Hájek & Smithson 2012); Aumann: "The payoffs need not be expressible in terms of a fixed finite number of commodities, or in terms of commodities at all" (1977: 444, via Peterson §3; [doi:10.1016/0022-0531(77)90143-0](https://doi.org/10.1016/0022-0531(77)90143-0)). Peterson (§3) argues the bank need only make a "credible promise" and offers supertask and dart constructions; he reports that "In the contemporary literature on the St. Petersburg paradox practical worries are often ignored".
- **Neglect small probabilities (Nicolaus Bernoulli 1714; Buffon 1777; Smith 2014).** Nicolaus, 1714: "the cases which have a very small probability must be neglected and counted for nulls, although they can give a very great expectation." (Letter 3); and to Cramer, the player "regards the event of the first case as impossible" (Letter 9). "Buffon argued in 1777 that a rational decision maker should disregard the possibility of winning lots of money in the St. Petersburg game because the probability of doing so is very low." — Dutka's summary: "Buffon thus takes a probability of 1/10,000 or less for an event as a probability which may be disregarded." (Peterson §5).
  "Nicholas J. J. Smith (2014) defends a modern version of Buffon’s solution" with "Rationally negligible probabilities (RNP)" (Peterson §5; [doi:10.1093/mind/fzu072](https://doi.org/10.1093/mind/fzu072)).
  - *Against:* Nicolaus himself: "the limits of these small probabilities are not precise" (Letter 9); Cramer: "I will be able never to fix to what point a probability becomes zero or certitude" (Letter 11). Peterson (§5): "Buffon can thus be accused of attempting to derive an “ought” from an “is”."; "if we ignore small probabilities, then we will sometimes have to ignore all possible outcomes of an event" (the 52! card orderings); Smith "would have to defend the stronger claim that decision makers are rationally required to ignore small probabilities". Hájek (2014) critiques RNP; "Yoaav Isaacs (2016)" shows RNP with Weak Consistency implies "arbitrarily much risk for arbitrarily little reward" (§5; [doi:10.1093/mind/fzv151](https://doi.org/10.1093/mind/fzv151)).
- **Risk-weighted expected utility (Buchak 2013).** "Her suggestion is that we should assign exponentially less weight to small probabilities as we calculate an option’s value." Peterson reports that "Buchak notes that this move does not by itself solve the St. Petersburg paradox" and that she is "also committed to RNP" (§5; [doi:10.1093/acprof:oso/9780199672165.001.0001](https://doi.org/10.1093/acprof:oso/9780199672165.001.0001)); Briggs (2015) discusses objections.
- **Accept an infinite value (Hájek & Nover 2006).** "A rare exception is Hájek and Nover", who argue from truncated games: "Thus we have a principled reason for accepting that it is worth paying any finite amount to play the St Petersburg game." (2006: 706, via Peterson §2; [doi:10.1093/mind/fzl703](https://doi.org/10.1093/mind/fzl703)). Peterson's reading: "Although they do not explicitly say so, Hájek and Nover would probably reject (3)." Joyce (1999: 37) and Russell & Isaacs (2021: 179) analyse what is troubling about an infinite value (§2).
- **Relative expectations (Colyvan 2008; Bartha 2007, 2016).** Colyvan's Petrograd game pays one unit more than St Petersburg on every outcome; "Both games have infinite expected utility, so the expected utility principle gives the wrong answer." (Peterson §6). "According to Colyvan, it is rational to choose \(A_k\) over \(A_l\) if and only if \(\reu(A_k,A_l) \gt 0\)." ([doi:10.5840/jphil200810519](https://doi.org/10.5840/jphil200810519)). Bartha's relative utilities compare an outcome with another and a basepoint ([2016, doi:10.1093/mind/fzv152](https://doi.org/10.1093/mind/fzv152)).
  - *Against:* "Peterson (2013) notes that REUT cannot explain why the Leningradskij game is worth more than the Leningrad game", since "“\(\infty - \infty\)” is undefined in standard analysis" (§6). On Bartha, Peterson: "An odd feature of Bartha’s theory is that two lotteries can have the same relative utility even if one is strictly preferred to the other" (§6).
  - *Peterson's own variant (2015: 87):* the Moscow game, a coin landing heads "with probability 0.4"; he states the task: "The challenge is to explain why in a robust and non-arbitrary way." (§6). The entry records no solution of his own.

No survey figure is recorded.

## Arguments in play

(none recorded as separate argument pages yet). The divergent sum and
Peterson's three claims are shown above.

**Sequel: the Pasadena game (Nover & Hájek 2004).** "If n is odd the player wins \((2^n)/n\) units of utility; however, if n is even the player has to pay \((2^n)/n\) units." (Peterson §7; [doi:10.1093/mind/113.450.237](https://doi.org/10.1093/mind/113.450.237)).
Summed in toss order the terms form 1 − 1/2 + 1/3 − …; "This infinite sum converges to ln 2 (about 0.69 units of utility). However, Nover and Hájek point out that we would obtain a very different result if we were to rearrange the order in which the very same numbers are summed up." (*Mathematics:* the first 10^6 terms sum to 0.693147 in Python; ln 2 = 0.693147.)
Responses as Peterson reports them (§7): Easwaran's (2008) weak expectation, on which "the fair price to pay is ln 2" ([doi:10.1093/mind/fzn053](https://doi.org/10.1093/mind/fzn053)); Bartha's Arroyo game with "no expected value" (2016: 805); Colyvan (2006) would "bite the bullet" and accept no expected utility ([doi:10.1093/mind/fzl695](https://doi.org/10.1093/mind/fzl695)); Peterson (2013) on non-probabilistic versions ([doi:10.1111/1746-8361.12046](https://doi.org/10.1111/1746-8361.12046)).

## Thinkers who addressed it

- **Nicolaus Bernoulli** (1687–1759) — posed it (1713); infinite equivalent,
  neglect of small probabilities (1714); objected to Cramer (1728) and to
  Daniel (1730, 1732).
- **Pierre Rémond de Montmort** — printed it (*Essay d'analyse*, p. 402);
  "I am not able to resolve myself to abandon our lemma" (Letter 4, 1714).
- **Gabriel Cramer** (1704–1752, per Sommer's note 12) — coin version,
  "usage", cap and square-root (1728).
- **Daniel Bernoulli** (1700–1782) — logarithmic utility, *Specimen* (1738).
- **Buffon** (1777) — moral impossibility, bank limits; **Fontaine** — bank
  limits (via Peterson §§3, 5, Dutka 1988).
- **d'Alembert** — Peterson notes only that the ratio test "was discovered by d’Alembert in 1768" (§1).
- **Karl Menger** (1934) — restoration; footnotes to Sommer's translation.
- **Kenneth Arrow** (1970), **Gilbert Bassett** (1987), **Paul Samuelson**
  (1977), **Edward McClennen** (1994) — bounded utility.
- **Robert Aumann** (1977), **D. L. Brito** (1975), **Richard Jeffrey**
  (1983), **James Joyce** (1999) — as above.
- **Harris Nover & Alan Hájek** (2004, 2006), **Mark Colyvan** (2006, 2008),
  **Paul Bartha** (2007, 2016), **Kenny Easwaran** (2008), **Alan Hájek &
  Michael Smithson** (2012), **Lara Buchak** (2013), **Martin Peterson**
  (2013, 2015, SEP 2019/2023), **Nicholas J. J. Smith** (2014), **Alan
  Hájek** (2014), **Rachael Briggs** (2015), **Yoaav Isaacs** (2016),
  **Jeffrey Sanford Russell & Yoaav Isaacs** (2021) — as above.

## Framings and reframings

- **A slight paradox from small probabilities (Daniel Bernoulli, 1728).** "The 4th and the 5th problems are easy, although their solutions are a slight paradox. In the case of the geometric progression 1, 2, 4, etc. the paradox is found on the small probability that there is that the game will last more than 20 or 30 throws." (Letter 12).
- **Fairness versus personal value.** Nicolaus Bernoulli's 1732 reframing
  (above) separates the price "according to justice or according to equity"
  from what the game is worth to one player.
- **Potential, not actual, infinity.** Peterson: "No actual infinities are required for constructing the paradox, only potential ones." (§2).
- **Not a logical paradox.** Peterson's preamble remark (see The question).
- **Related problems:** [Newcomb's problem](newcombs-problem.md) (another
  case against a principle of choice), [Zeno's paradoxes](zenos-paradoxes.md)
  (infinite series; Peterson §3 uses a supertask),
  [the lottery and preface paradoxes](lottery-and-preface-paradoxes.md)
  (another paradox built on improbable outcomes; structural note of this
  implant).

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — see The question and Peterson's
  "strict logical sense" remark.
- [Validity](../vocabulary/validity.md) — the logic check above;
  [classical logic](../methods/classical-logic.md).
- [Bayesian updating](../methods/bayesian-updating.md) — neighbouring use
  of probability.
- *Expected value, expected utility, marginal utility, bounded utility,
  continuity axiom, dominance, conditionally convergent series* — open work
  in [vocabulary](../vocabulary/index.md).
