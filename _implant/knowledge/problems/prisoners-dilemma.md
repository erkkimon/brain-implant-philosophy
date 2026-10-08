---
type: article
about: concept
title: "The prisoner's dilemma"
description: "Two players each do better by defecting whatever the other does, yet both do worse if both defect than if both cooperate — Flood and Dresher's 1950 RAND game, Tucker's prison story; what rationality requires in the one-shot, replica and iterated games (dominance, cooperation with a twin, Gauthier's constrained maximization, team reasoning, Axelrod's Tit for Tat), and the game as a reading of Hobbes's state of nature."
tags: [problem, dilemma, ethics, decision-theory, game-theory, political-philosophy]
timestamp: 2026-10-08T20:29:06Z
---

# The prisoner's dilemma

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
sources graded as in [How claims are graded](../../conventions/how-claims-are-graded.md).
The map follows Kuhn,
[SEP Fall 2024 "Prisoner’s Dilemma"](https://plato.stanford.edu/archives/fall2024/entries/prisoner-dilemma/)
(rev. 2019-04-02; excerpts:
`raw/sep-prisoner-dilemma-fall-2024-origins-structure-iteration-and-morality.md`,
`raw/sep-prisoner-dilemma-fall-2024-newcomb-and-replicas.md`), with Ross,
[SEP "Game Theory"](https://plato.stanford.edu/archives/fall2024/entries/game-theory/)
(excerpt: `raw/sep-game-theory-fall-2024-prisoners-dilemma-rationality-and-experiments.md`),
Cudd & Eftekhari,
[SEP "Contractarianism"](https://plato.stanford.edu/archives/fall2024/entries/contractarianism/),
and Lloyd & Sreedhar,
[SEP "Hobbes's Moral and Political Philosophy"](https://plato.stanford.edu/archives/fall2024/entries/hobbes-moral/)
(excerpt: `raw/sep-contractarianism-and-hobbes-moral-fall-2024-prisoners-dilemma.md`).
Where an entry's author assesses, the assessment is attributed to that author.

## The question

Kuhn's statement of the story's point: "The “dilemma” faced by the prisoners here is that, whatever the other does, each is better off confessing than remaining silent. But the outcome obtained when both confess is worse for each than the outcome they would have obtained had both remained silent." (preamble).
With cooperation (C, silence) and defection (D, confession), a symmetric
two-player PD requires "(PD1) \(T \gt R \gt P \gt S\)" (§1): *R* "reward"
for mutual cooperation, *P* "punishment" for mutual defection, *T*
"temptation" for the sole defector, *S* "sucker" for the sole cooperator.
Axelrod's values are *T* = 5, *R* = 3, *P* = 1, *S* = 0 (Kuhn §18;
Axelrod,
[1988 chapter adapted from the 1984 book](https://ee.stanford.edu/~hellman/Breakthrough/book/pdfs/axelrod.pdf),
p. 2; excerpt: `raw/axelrod-1988-evolution-of-cooperation-breakthrough-chapter.md`).

| Row \ Column | C      | D      |
|--------------|--------|--------|
| C            | 3, 3   | 0, 5   |
| D            | 5, 0   | 1, 1   |

**Check (this implant, 2026-09-27; mathematics, not a position).** A
Python enumeration of the table (script in `_temp/`, deleted) printed:
`D strictly dominates C for Row: True | for Column: True`;
`pure-strategy Nash equilibria: [('D', 'D')]`;
`outcome ('D', 'D') (1, 1) Pareto-dominated by: [('C', 'C')]`, with no
other outcome Pareto-dominated; and, over every integer assignment on
0–6 with *T* > *R* > *P* > *S*,
`all 35 integer orderings T>R>P>S on 0..6: D dominant, (C,C) better for both than (D,D), (D,D) unique pure NE: True`.
This matches Kuhn: D is "said to strictly dominate" C (§1), (D, D) is "the game's only strict nash equilibrium" (§1), and "every outcome except universal defecton is pareto optimal" (§5, spelling his).
The dominance step as a propositional form — *ColumnCooperates →
DefectBetter*, *ColumnDefects → DefectBetter*, *ColumnCooperates ∨
ColumnDefects* ⊢ *DefectBetter* — `logic.py check` reports `VALID`
(2026-09-27); without the disjunctive premise it reports `INVALID`. What
the dispute below turns on is whether dominance fixes the rational
choice when the other's move is correlated with one's own, not the form.

**Origin.** "Puzzles with the structure of the prisoner's dilemma were discussed by Merrill Flood and Melvin Dresher in 1950, as part of the Rand Corporation's investigations into game theory (which Rand pursued because of possible applications to global nuclear strategy)." (Kuhn, preamble).
"The title “prisoner's dilemma” and the version with prison sentences as payoffs are due to Albert Tucker, who wanted to make Flood and Dresher's ideas more accessible to an audience of Stanford psychologists." (ibid.).
Kuhn reports Peterson's (2015, p. 1) suggestion that Tucker "may have been
discussing the work of his famous graduate student John Nash", whose 1950
dissertation (p. 291) contains a game of this structure (preamble;
[Nash 1951](https://doi.org/10.2307/1969529)). Flood and Dresher's interest "seems to have stemmed from their view that it provided a counterexample to the claim that the nash equilibria of a game constitute its natural “solutions”." (Kuhn §1).
The Flood–Dresher RAND memorandum itself was not fetched (the RAND site
refused the request).

**Which "dilemma".** *Structural note (this implant).* In the terms of
[Dilemma](../vocabulary/dilemma.md) the name uses the loose sense — Kuhn
puts "dilemma" in quotation marks (preamble) — not the moral sense of
[Can there be genuine moral dilemmas?](moral-dilemmas.md).

## Why it matters

- **Individual vs. group rationality.** "A common view is that the puzzle illustrates a conflict between individual and group rationality." (Kuhn, preamble).
- **Selfishness vs. altruism, and morality.** "A slightly different interpretation takes the game to represent a choice between selfish behavior and socially desirable altruism." — an observation that "has led David Gauthier and others to take the prisoner's dilemma to say something important about the nature of morality." (Kuhn, preamble).
- **Collective action.** Kuhn: "A common view is that a multi-player PD structure is reflected in what Garrett Hardin popularized as “the tragedy of the commons.”" (§5; [Hardin 1968](https://doi.org/10.1126/science.162.3859.1243)).
- **Decision theory.** A PD between replicas is, for Lewis (1979), a
  Newcomb problem; Kuhn reports that "Lewis argues that the link to the PD suggests that situations where the two decisions diverge are not so unusual" (§7) — see [Newcomb's problem](newcombs-problem.md).
- **Political philosophy.** Ross: the PD "gives the logic of the problem faced by Cortez’s and Henry V’s soldiers" and "by Hobbes’s agents before they empower the tyrant" (§2.4; see Framings).
- **Scale.** Kuhn reports Donninger's count of "more than a thousand articles" in the sixties and seventies, and 49,600 Google Scholar results in 2018 (preamble).

## Positions taken

Grouped by the question each answers; the grouping is this implant's
(structural note), the positions and their owners are the sources'. No
position is ranked here.

**One-shot game: defect.** Kuhn §1: "Thus two “rational” players will defect and receive a payoff of \(P\), while two “irrational” players can cooperate and receive greater payoff \(R\)." (scare quotes his). Ross: "What makes a game an instance of the PD is strictly and only its payoff structure." (§2.7).
- *Case for:* the dominance argument above (Kuhn §1; Axelrod: "no matter what the other player does, defection yields a higher payoff", 1988, p. 2). Ross: "It is the logic of the prisoners’ situation, not their psychology, that traps them in the inefficient outcome" (§2.7). Binmore (1994), as Ross reports, holds that players who cooperate because they value the team are in a different game: "Rather, we should say that the PD was the wrong model of their situation." (§5).
- *Case against:* the "common view" of a conflict with group rationality (Kuhn, preamble); an objection Ross reports, that players "might be able to just see" the cooperative outcome is "socially and morally superior", which "applies the distinctive idea of rationality urged by Immanuel Kant" (§2.7). Ross's reply: "the defender of the possibility of Kantian rationality is really proposing that they try to dig themselves out of such games by turning themselves into different agents." (§2.7).

**Cooperate with a replica (the "PD with twins").** Kuhn's words for it: "One controversial argument that it is rational to cooperate in a PD relies on the observation that my partner in crime is likely to think and act very much like I do." (§7).
- *Case for:* "When the correlation between our behaviors is sufficiently strong or the differences in payoffs is sufficiently great, my expected payoff (as that term is usually understood) is higher if I cooperate than if I defect." (§7); Davis (1977, 1985) gives "a sympathetic presentation" (§7).
- *Case against:* "my action is causally independent of my replica's. Since I can't affect what my accomplice does and since, whatever he does, my payoff is greater if I defect, I should defect." (§7); Binmore (1994, chs. 3.4–3.5) gives "a reformulation and extended rebuttal" (§7). The split mirrors evidential against causal decision theory; Kuhn: "there remain people committed to each view" (§7).

**Constrained maximization (Gauthier).** As Cudd & Eftekhari summarise Gauthier's *Morals by Agreement* (1986): "But by disposing themselves to act according to the requirements of morality whenever others are also so disposed, they can gain each others’ trust and cooperate successfully." (§3).
Kuhn: "a player \(j\) should cooperate if the other would cooperate if \(j\) did, and defect otherwise." (§10); Kuhn discusses it among strategies for players with the property "that David Gauthier has labeled transparency" (§10). Danielson (1992) favours the related "reciprocal cooperation" (Kuhn §9).
- *Case for:* the choice between being a "constrained (self-interest) maximizer" and a "straightforward" one, where agents "keep their agreements, provided that they find themselves in an environment of like-minded individuals (Gauthier 1986, 160–166)" (Cudd & Eftekhari §4); Danielson's program "does move and score well against familiar strategies" (Kuhn §10).
- *Case against:* Cudd & Eftekhari: "this solution has been found dubitable by many commentators (see Vallentyne 1991)" (§4); Kuhn: such programs "cannot be coherently paired with everything" and "The lesson of all this for rational action is not clear." (§10).
- *Later view:* Gauthier (2013), as Cudd & Eftekhari report, no longer treats the parties "as (constrained) rational maximizers; instead, he conceives of them as Pareto-optimizers." (§3).

**Team reasoning.** "Sugden (1993) seems to have been the first to suggest that even non-altruistic players in the one-shot PD might jointly see that they could reason as a team, that is, arrive at their choices of strategies by asking ‘What is best for us?’ instead of ’What is best for me?’." (Ross §5); Bacharach (2006, completed by Sugden and Gold) develops it (ibid.).
- *Case for:* "The critic of individualism can acknowledge Binmore’s logical point but accommodate it by arguing that changing the game is exactly what people should try to do" (Ross §5).
- *Case against:* "Binmore (1994) forcefully argues that this line of criticism confuses game theory as mathematics with questions about which game theoretic models are most typically applicable to situations in which people find themselves." (Ross §5).

**Finitely repeated game: defect throughout (backward induction).** "In games of the first kind, one can prove by an argument known as backward induction that \(\bDu\), \(\bDu\) is the only subgame perfect equilibrium." (Kuhn §11; "first kind" is IPDs "of fixed, finite length"). Axelrod: players "have no incentive to cooperate on the last move, nor on the next-to-last move" (1988, p. 4).
- *Case for:* the induction itself; an observation "apparently originating in Kavka 1983" applies it whenever "an upper bound to the length of the game is common knowledge" (Kuhn §14).
- *Case against:* Kuhn: "In practice, there is not a great difference between how people behave in long fixed-length IPDs (except in the final few rounds) and those of indeterminate length." (§11); "Some have used these kinds of observation to argue that the backward induction argument shows that standard assumptions about rationality (with other plausible assumptions) are inconsistent or self-defeating." (§11, citing Skyrms 1990 and Bicchieri 1989).

**Indefinitely repeated game: reciprocity (Tit for Tat).** Axelrod: "For cooperation to prove stable, the future must have a sufficiently large shadow." (1988, p. 4). His tournament winner "cooperates on the first move and then does whatever the other player did on the previous move" (p. 2).
- *Case for:* TFT is "The strategy that scored highest in Axelrod's initial tournament", and "it won Axelrod's second tournament, whose sixty three entrants were all given the results of the first tournament" (Kuhn §14); Axelrod's four properties — "avoidance of unnecessary conflict", "provocability", "forgiveness" and "clarity of behavior" (1988, pp. 2–3; Kuhn §14: nice, retaliatory, forgiving, clear).
- *Case against:* Kuhn: "Suggestive as Axelrod's discussion is, it is worth noting that the ideas are not formulated precisely enough to permit a rigorous demonstration of the supremacy of TFT." (§14); by a "folk theorem", "for any \(p\), \(0 \le p \le 1\) there is a nash equilibrium in which \(p\) is the fraction of times that mutual cooperation occurs" (§14); Rapoport et al. (2015), re-running the first tournament's strategies in groups followed by a championship round, find the strategies ranked two and six in the first tournament "both perform considerably better than top-ranked TFT" (§14); in the one of the 2004–2005 anniversary tournaments (Kendall et al. 2007) that "most closely replicated Axelrod's tournaments", "TFT finished only fourteenth out of the fifty strategies submitted" (§14).

**Empirical record (as the sources report it; no cooperation rates are
given in them).** Twins: "It turns out that twins are more likely to cooperate in a PD than strangers, but there seems to be no suggestion that the reasoning that leads them to do so follows the controversial arguments presented above." (Kuhn §7; [Segal & Hershberger 1999](https://doi.org/10.1016/s1090-5138(98)00039-7)).
Ross: "in experiments in which subjects play sequences of one-shot PDs (not repeated PDs, since opponents in the experiments change from round to round), majorities of subjects begin by cooperating but learn to defect as the experiments progress." (§5); in repeated PDs with known end-points subjects "tend to cooperate for awhile, but learn to defect earlier as they gain experience" (§4).

## Arguments in play

(none recorded as separate argument pages yet). The dominance argument
(checked above), the replica argument and its causal counter-argument
(Kuhn §7), and backward induction (Kuhn §11) are quoted in Positions.

## Thinkers who addressed it

- **Thomas Hobbes** (*Leviathan*, 1651, as dated by Lloyd & Sreedhar §1) — the state of nature, read as a
  PD by some later interpreters (Framings); not read here.
- **David Hume** (*Treatise* 3.2.5, 1739–40) — the two farmers: "Your corn is ripe to-day; mine will be so tomorrow." ([Gutenberg #4705](https://www.gutenberg.org/ebooks/4705); excerpt: `raw/hume-1739-40-treatise-3-2-5-farmers-dilemma.md`); Kuhn reports Skyrms (1998) and Vanderschraaf reading it as an asynchronous PD, "the farmer's dilemma" (§9).
- **Merrill Flood & Melvin Dresher** (RAND, 1950) — the game (Kuhn, preamble).
- **Albert Tucker** — the name and the prison story (ibid.).
- **John Nash** (1950/[1951](https://doi.org/10.2307/1969529)) — a game of PD structure as an example (ibid.).
- **Garrett Hardin** ([1968](https://doi.org/10.1126/science.162.3859.1243)) — the tragedy of the commons (Kuhn §5).
- **Laurence Davis** (1977, 1985) — cooperation with a replica (Kuhn §7).
- **David Lewis** (1979) — "Prisoner's Dilemma Is a Newcomb Problem" ([1985 reprint](https://doi.org/10.59962/9780774857154-015); Kuhn §7).
- **Robert Axelrod** (1981, [with Hamilton 1981](https://doi.org/10.1126/science.7466396), 1984) — tournaments, Tit for Tat.
- **Gregory Kavka** ([1983](https://doi.org/10.1086/292435); 1991) — backward induction with an upper bound (§14); intrapersonal PD (§6).
- **David Gauthier** ([1986](https://doi.org/10.1093/0198249926.001.0001); 2013) — constrained maximization; later Pareto-optimizers.
- **Jean Hampton** ([1986](https://doi.org/10.1017/cbo9780511625060)) — the passions/rationality dilemma for Hobbes (Framings).
- **S. L. Hurley** ([1991](https://doi.org/10.1007/bf00485806)), **Bermúdez** (2015) — the PD and Newcomb's problem "are significantly different" (Kuhn §7).
- **Peter Danielson** (1992) — reciprocal cooperation (Kuhn §§9–10).
- **Robert Sugden** (1993), **Michael Bacharach** (2006) — team reasoning; **Kenneth Binmore** (1994) — the reply (Ross §5).
- **Brian Skyrms** (1998), **Peter Vanderschraaf** (1998) — Hobbes and Hume as PD theorists (Kuhn §§9, 16).
- **Steven Kuhn** (SEP 1997, rev. 2019) — the survey this page follows.

## Framings and reframings

- **Hobbes's state of nature as a PD.** Lloyd & Sreedhar give it as one of three readings: people "fully rational, but ... trapped in a situation that makes it individually rational for each to act in a way that is sub-optimal for all, perhaps finding themselves in the familiar ‘prisoner’s dilemma’ of game theory" (§5), the others being shortsightedness and passions; "Which, if any, of these accounts adequately answers to Hobbes’s text is a matter of continuing debate among Hobbes scholars." (§5).
  Ross reconstructs Hobbes so that agents "can repeatedly fail to derive the benefits of cooperation" (§1), and "Hobbes’s proposed solution to this problem was tyranny." (§1).
  Hampton (1986), as Cudd & Eftekhari report, argues that if the war comes from "prisoner’s dilemma reasoning", then "rational actors will not comply with the social contract any more than they will cooperate with each other before it is made." (§4).
  Kuhn reports that "According to Skyrms (1998) and Vanderschraaf, both Hobbes and Hume identified it as the strategy that underlies our cooperative behavior in important PD-like situations." (§16; "it" is GRIM, cooperating until the other defects once).
- **Not a PD after all.** Binmore's reframing (Ross §5, above): where players cooperate for the team's sake, "the PD was the wrong model of their situation". Kuhn §8 reports critics (Sugden; Binmore 2005) who contend that, since cooperation is not an equilibrium in a true PD, any such "problem" "would be an unsolvable one"; Kuhn says the stag hunt "might provide a better model for situations where cooperation is difficult, but still possible" (§8).
- **One player, not two.** Kuhn §6 reports readings of the PD inside one person: Parfit's and Quinn's temporal stages, and Kavka's (1991) "subagents".
- **Moves players do not need to reason about.** Axelrod: "the individuals involved do not have to be rational: The evolutionary process allows successful strategies to thrive, even if the players do not know why or how." (1988, p. 4).

## Vocabulary

- [Dilemma](../vocabulary/dilemma.md) — the loose sense; see The question.
- [Validity](../vocabulary/validity.md) — the dominance form is valid; the
  dispute is over whether its premises describe the choice.
- [Paradox](../vocabulary/paradox.md) — Kuhn calls the PD a "puzzle" (preamble).
- Dominance, Nash equilibrium, Pareto optimality, backward induction,
  subgame perfection — open work in [vocabulary](../vocabulary/index.md).

Related problems: [chainstore paradox](chainstore-paradox.md) (Selten 1978; Kreps & Wilson 1982), [Kavka's toxin puzzle](kavkas-toxin-puzzle.md) (Mintoff 1996), [Newcomb's problem](newcombs-problem.md),
[Can there be genuine moral dilemmas?](moral-dilemmas.md),
[the St Petersburg paradox](st-petersburg-paradox.md) (decision theory).
Branch: [Problems](./index.md).
