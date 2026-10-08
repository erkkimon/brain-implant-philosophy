---
type: article
about: concept
title: "Parrondo's paradox"
description: "Can two games of chance, each losing when played on its own, combine into a winning game when they are alternated or mixed at random? Harmer and Abbott (Nature 1999) reported that they can, in coin-tossing games devised by Juan Parrondo after the flashing Brownian ratchet; the page sets out the games and an exact check of the arithmetic, the convexity and dependence explanations, and the dispute over whether the result deserves the name paradox (Philips & Feldman 2004 against Abbott), each with its owner."
tags: [problem, paradox, decision-theory, probability, game-theory, physics]
timestamp: 2026-10-08T21:37:56Z
---

# Parrondo's paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
sources graded as in [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md). Admitted from Wikipedia's
[List of paradoxes, rev. 1376699902](https://en.wikipedia.org/w/index.php?title=List_of_paradoxes&oldid=1376699902),
section "Decision theory", which gives it as "Parrondo's paradox: It is possible to play two losing games alternately to eventually win."
The Wikipedia article [rev. 1373822103](https://en.wikipedia.org/w/index.php?title=Parrondo%27s_paradox&oldid=1373822103)
is used as a pointer to sources (excerpt: `raw/wikipedia-parrondos-paradox-rev-1373822103-and-list-entry.md`).
Primary text: Harmer & Abbott, "Losing strategies can win by Parrondo's paradox", *Nature* 402, 1999, p. 864
([doi:10.1038/47220](https://doi.org/10.1038/47220); only the public opening paragraph read; excerpt: `raw/harmer-abbott-1999-losing-strategies-can-win-nature.md`).
Other sources read: Derek Abbott's FAQ on [The Official Parrondo's Paradox Page](https://web.archive.org/web/20180621224639/http://www.eleceng.adelaide.edu.au/Groups/parrondo/faq.html)
(2018 snapshot; excerpt: `raw/abbott-parrondos-paradox-faq-answers-2018-snapshot.md`);
Philips & Feldman, [SSRN 581521](https://doi.org/10.2139/ssrn.581521), abstract
(excerpt: `raw/philips-feldman-2004-parrondos-paradox-is-not-paradoxical.md`);
Shu & Wang, "Beyond Parrondo's Paradox", *Scientific Reports* 4, 2014
([doi:10.1038/srep04244](https://doi.org/10.1038/srep04244); excerpt: `raw/shu-wang-2014-beyond-parrondos-paradox.md`).
Abstracts and works verified bibliographically only: `raw/parrondos-paradox-crossref-and-arxiv-records.md`.

## The question

Harmer and Abbott (1999) put it as: "But can two losing gambling games be set up such that, when they are played one after the other, they becoming winning? The answer is yes."
("they becoming" as printed.) Abbott's FAQ (Q1): "Parrondo's paradox is the counterintuitive result where individual losing games can be combined to give rise to a winning expectation. Random or periodic switching between losing games can surprisingly win."

**The games, in the sources' wording.** The Harmer–Abbott review abstract
(*Fluctuation and Noise Letters* 2, 2002, R71–R107,
[doi:10.1142/S0219477502000701](https://doi.org/10.1142/S0219477502000701)):
"Game A uses a single biased coin while game B uses two biased coins and has a state dependent rule based on the player's current capital. Playing each of the games individually causes the player to lose. However, a winning expectation is produced when randomly mixing games A and B."
Game B, from the 1999 note: "The rule is that we play coin 2 if our capital is a multiple of an integer M and play coin 3 if it is not."
and "If we assign a poor probability of winning to coin 2, such as p 2 =1/10−ε, then this would outweigh the better coin 3 with p 3 =3/4−ε, making game B a losing game overall."
The Wikipedia article (rev. 1373822103) gives game A's coin as winning with probability 1/2 − ε, and reports: "Harmer and Abbott show via simulation that if M=3 and ε = 0.005, Game B is an almost surely losing game as well."
Shu and Wang (2014) use the same setting: "by setting the value of biasing parameter ε = 0.005 and predefined integer M = 3".
They distinguish two families: "There are totally two versions of the Parrondo's paradox, which is referred to as capital- and history-dependent."

**Arithmetic check (this implant, 2026-10-09; mathematics, not a position).**
Take the rules above with M = 3 and ε = 0, and track the capital modulo 3
as a three-state Markov chain (state 0: capital a multiple of 3).

1. Game B alone: coin 2 (win 1/10) in state 0, coin 3 (win 3/4) in states 1 and 2. Solving the stationary equations exactly gives state probabilities 5/13, 2/13, 6/13; the long-run chance of winning a round is (5/13)(1/10) + (8/13)(3/4) = 1/26 + 6/13 = 13/26 = 1/2. Game B is then fair, and game A (win 1/2) is fair.
2. Random mixing, a fair coin choosing A or B each round: the win probabilities average to 3/10 in state 0 and 5/8 in states 1 and 2. The exact stationary probabilities are 245/709, 180/709, 284/709, and the long-run chance of winning a round is 727/1418, which exceeds 1/2 by 4/1418.
3. With ε = 0.005 (computed numerically): game A wins with probability 0.495; in game B the stationary probability of coin 2 is 0.3836 (the figure the Wikipedia article gives) and the expected gain per round is about −0.0087; the random mixture's is about +0.0157.

Step 3 reproduces, for these parameters, the claim quoted from the sources; it
does not adjudicate whether the result should be called a paradox.

**Is it a paradox?** The label is contested (Positions, below). Wikipedia's
article: "In the early literature on Parrondo's paradox, it was debated whether the word 'paradox' is an appropriate description given that the Parrondo effect can be understood in mathematical terms."
See [paradox](../vocabulary/paradox.md) for this implant's normative sense.

## Why it matters

- **Physics: the Brownian ratchet.** Shu and Wang (2014): "The initial purpose of the Parrondo's paradox was to simulate a counterintuitive physical phenomenon generated by the flashing Brownian ratchet 1 in terms of two gambling games 2 ."
  Abbott (FAQ Q3): "Inspired by a version called the flashing ratchet , in 1996, Parrondo devised the games as a pedagogical illustration of the Brownian ratchet."
  and "it turns out that Parrondo's games are a discrete-time and discrete-space version of the continuous flashing ratchet."
  Harmer and Abbott (1999): "Here we model this behaviour as a flashing ratchet".
- **Game theory.** Harmer and Abbott (1999) present it as "a striking new result in game theory" ("This is a striking new result in game theory called Parrondo's paradox, after its discoverer, Juan Parrondo").
  Abbott's FAQ (Q11) takes up the objection that the original games involve no decisions between players and answers: "In the Blackwell sense, game theory includes simple coin tossing games."
- **Applications claimed and disputed.** Shu and Wang (2014): "The concept has been scrutinized 8 9 since its first appearance and extended into other potential applications 10 11 12 13 ."
  The Wikipedia article: "Parrondo's games are of little practical use such as for investing in stock markets as the original games require the payoff from at least one of the interacting games to depend on the player's capital."
  — cited there to Iyengar & Kohli, "Why Parrondo's paradox is irrelevant for utility theory, stock buying, and the emergence of life", *Complexity* 9(1), 2003, 23–27 ([doi:10.1002/cplx.10112](https://doi.org/10.1002/cplx.10112); not read, so their argument is reported only through that title and the Wikipedia sentence).
  Abbott (FAQ Q2), on casinos: "Parrondo's games rely on exploiting convex linear combinations in a non-linear parameter space. Casino games have a linear parameter space (as far as we know)."

## Positions taken

Each line names its owner; none is ranked. The sources group the responses
by how the result is explained and by whether the name fits.

**How the effect arises.**

- **Convexity.** Abbott (FAQ Q2): "The importance of convexity in the Parrondo effect was first pointed out by Moraal in 1999 and then independently by Costa, Fackrell & Taylor in 2000."
  Shu and Wang (2014): "The compound game is formed as a convex linear combination of two games, game A and game B, by introducing one additional parameter, namely, mixing parameter, denoted by γ ."
  They state the mechanism as: "The Parrondo's paradox is caused by manipulating the probability distribution of individual losing games to form a winning compound game 17 18 ."
- **Dependence on capital (elementary probability).** Philips and Feldman (2004, abstract): "This paradox has aroused a great deal of interest in recent years, and a number of sophisticated resolutions of it have been published. It is the purpose of this article to show that the paradox is not paradoxical at all, and is easily resolved using elementary probability."
  The Wikipedia article summarises the dependence reading and points to them: "In summary, Parrondo's paradox is an example of how dependence can wreak havoc with probabilistic computations made under a naive assumption of independence. A more detailed exposition of this point, along with several related examples, can be found in Philips and Feldman."
  The full paper was not read.
- **Random walks in periodic environments.** Key, Klosek and Abbott (arXiv:math/0206151, 2002, abstract): "We observe that all of the games in question are random walks in periodic environments (RWPE) when viewed on the proper time scale. Consequently, we use RWPE techniques to derive conditions under which Parrondo's paradox occurs."
- **Discretised Fokker–Planck equation.** Allison and Abbott (arXiv:cond-mat/0208470, 2002, abstract): "Parrondo's games, are in effect, a particular way of sampling a Fokker-Planck equation."
  They state the prior gap: "Several authors have implied that the original inspiration for Parrondo's games was a physical system called a ``flashing Brownian ratchet''. The relationship seems to be intuitively clear but, surprisingly, has not yet been established with rigor."
  Abbott (FAQ Q3): "This link was first mathematically established by Allison & Abbott (2002) and then independantly by Toral, Amengual & Mangioni (2003)." (spelling as on the page).

**Whether the name fits, side by side.**

- **Not paradoxical.** Philips and Feldman (2004), title and abstract, quoted above.
- **A name for an apparent paradox.** Abbott (FAQ Q12): "This question is sometimes asked by mathematicians, whereas physicists usually don't worry about such things. The first thing to point out is that "Parrondo's paradox" is just a name, just like the "Braess paradox" or "Simpson's paradox." Secondly, as is the case with most of these named paradoxes they are all really apparent paradoxes."
  and "So no one claims these are paradoxes in the strict sense. In the wide sense, a paradox is simply something that is counterintuitive."
- **Not reducible to a simpler game.** Shu and Wang (2014) test a simple capital-dependent game proposed by Philips and Feldman and report that in it "game B is a winning game instead of a losing game"; they conclude: "Therefore, the paradoxical effect cannot be simply created by replacing the original game with a primitive version. Unfortunately, the proposed simple capital-dependent game 14 is failed to reproduce the analogous paradoxical effect."
  The Philips–Feldman paper, and any reply to this, were not read.

**Whether it is interesting if a single game does as well.** Abbott (FAQ Q13)
states the objection — "The implication of this question is that Parrondo's paradox is not really interesting, because you can replace games A & B, with a single game—call it C—that can perform equally as well." —
and answers by analogy with Penrose tiles: "Similarly with Parrondo's games what is of interest is the richness in the dynamics produced by switching A and B."

## Arguments in play

(none recorded as separate argument pages yet). The arithmetic check above
shows, for ε = 0, two fair games whose random mixture has a winning chance
of 727/1418 per round; the explanations on record (convexity, dependence,
periodic random walks, discretised ratchet) are listed under Positions taken.

## Thinkers who addressed it

- **Juan Parrondo** (J. M. R. Parrondo) — devised the games in 1996 (Abbott FAQ Q3; the Wikipedia article's lead gives the same year); with Español (1996) criticised Feynman's ratchet analysis (Shu & Wang ref. 2; FAQ Q4).
- **Gregory P. Harmer and Derek Abbott** — the 1999 *Nature* note, a 1999 *Statistical Science* paper ([doi:10.1214/ss/1009212247](https://doi.org/10.1214/ss/1009212247); not read) and the 2002 review; Abbott's FAQ defends the name.
- **Ajdari and Prost** — the flashing-ratchet work that, per Abbott (FAQ Q4), "influenced Parrondo to devise his now famous games" (he dates it 1992; Shu & Wang cite Prost, Chauwin, Peliti & Ajdari 1994).
- **Moraal** (1999); **Costa, Fackrell and Taylor** (2000) — convexity (FAQ Q2).
- **Andrew Allison and Derek Abbott** (2002); **Toral, Amengual and Mangioni** (2003) — the ratchet–game link (FAQ Q3; arXiv:cond-mat/0208470).
- **Thomas K. Philips and Andrew B. Feldman** (2004) — "not paradoxical". **R. Iyengar and R. Kohli** (2003) — irrelevance for utility theory and stock buying (title; not read).
- **Jian-Jun Shu and Qi-Wen Wang** (2014) — probability-space analysis and reply to Philips & Feldman.

## Framings and reframings

- **A ratchet in discrete form.** Allison and Abbott's abstract and Abbott's FAQ (Q3), quoted above.
- **A convex combination.** Abbott (FAQ Q2) and Shu and Wang (2014), quoted above.
- **A dependence effect.** Philips and Feldman (2004), as pointed to by the Wikipedia article.
- **A named apparent paradox.** Abbott (FAQ Q12) places it beside "Braess paradox" and "Simpson's paradox"; see [Simpson's paradox](simpsons-paradox.md).
- **Two versions.** Capital-dependent and history-dependent (Shu & Wang 2014).

Left out: the history-dependent and cooperative games beyond their naming, quantum and chaotic variants, biological and financial applications listed in the Wikipedia article (sources not read), and the content of the 2002 review beyond its abstract.

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — see The question, last paragraph, and the naming dispute.
- Markov chain, stationary distribution, expectation, convex linear combination, Brownian ratchet — open work in [vocabulary](../vocabulary/index.md).

Related problems: [Simpson's paradox](simpsons-paradox.md) (named beside it
by Abbott, FAQ Q12). Branch: [Problems](./index.md).
