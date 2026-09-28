# SEP "Prisoner's Dilemma" (Kuhn) — origins, payoff structure, conditional strategies, iteration, Axelrod, twins

Source: Steven Kuhn, "Prisoner’s Dilemma", The Stanford Encyclopedia of
  Philosophy (Fall 2024 Edition), Edward N. Zalta & Uri Nodelman (eds.);
  first published 1997-09-04, substantive revision 2019-04-02 (copyright
  line: "Copyright © 2019 by Steven Kuhn"). Preamble, §§1, 5, 7, 9, 10,
  11, 14 ("Axelrod and Tit for Tat", "Post-Axelrod"), 16, 18.
Original: https://plato.stanford.edu/archives/fall2024/entries/prisoner-dilemma/
  (copyrighted; excerpts only)
Retrieved: 2026-09-27 (archived page fetched with curl, HTML stripped,
  read; each quotation below checked by script against the stripped text.)
Companion excerpt (§7 Newcomb passages, written earlier by another page):
  `sep-prisoner-dilemma-fall-2024-newcomb-and-replicas.md`.

## Preamble — the story, the readings, the history

> "The “dilemma” faced by the prisoners here is that, whatever the other does, each is better off confessing than remaining silent. But the outcome obtained when both confess is worse for each than the outcome they would have obtained had both remained silent."  (preamble)

> "A common view is that the puzzle illustrates a conflict between individual and group rationality."  (preamble)

> "A slightly different interpretation takes the game to represent a choice between selfish behavior and socially desirable altruism."  (preamble)

> "This observation has led David Gauthier and others to take the prisoner's dilemma to say something important about the nature of morality."  (preamble)

> "Puzzles with the structure of the prisoner's dilemma were discussed by Merrill Flood and Melvin Dresher in 1950, as part of the Rand Corporation's investigations into game theory (which Rand pursued because of possible applications to global nuclear strategy)."  (preamble)

> "The title “prisoner's dilemma” and the version with prison sentences as payoffs are due to Albert Tucker, who wanted to make Flood and Dresher's ideas more accessible to an audience of Stanford psychologists."  (preamble)

> "More recently, it has been suggested (Peterson, p1) that Tucker may have been discussing the work of his famous graduate student John Nash, and Nash 1950 (p. 291) does indeed contain a game with the structure of the prisoner's dilemma as the second in a series of six examples illustrating his technical ideas."  (preamble)

> "Donninger reports that “more than a thousand articles” about it were published in the sixties and seventies. A Google Scholar search for “prisoner's dilemma” in 2018 returns 49,600 results."  (preamble)

## §1 Symmetric 2×2 PD with ordinal payoffs

> "(PD1) \(T \gt R \gt P \gt S\)"  (§1; the chain of inequalities, in the entry's LaTeX)

> "\(R\) is the “reward” payoff that each player receives if both cooperate. \(P\) is the “punishment” that each receives if both defect. \(T\) is the “temptation” that each receives as sole defector and \(S\) is the “sucker” payoff that each receives as sole cooperator."  (§1)

> "The move \(\bD\) for Row is said to strictly dominate the move \(\bC\): whatever Column does, Row is better off choosing \(\bD\) than \(\bC\)."  (§1)

> "Thus two “rational” players will defect and receive a payoff of \(P\), while two “irrational” players can cooperate and receive greater payoff \(R\)."  (§1)

> "It is also worth noting that the outcome \((\bD, \bD)\) of both players defecting is the game's only strict nash equilibrium, i.e., it is the only outcome from which each player could only do worse by unilaterally changing its move."  (§1)

> "Flood and Dresher's interest in their dilemma seems to have stemmed from their view that it provided a counterexample to the claim that the nash equilibria of a game constitute its natural “solutions”."  (§1)

## §5 Many players

> "A common view is that a multi-player PD structure is reflected in what Garrett Hardin popularized as “the tragedy of the commons.”"  (§5)

> "Finally, in the orginal PD, every outcome except universal defecton is pareto optimal--i.e., as long as at least one of the players cooperates, there is no outcome in which in which each player is at least as well off and one is better off."  (§5; spelling as in the entry)

## §6 Single-person interpretations

> "One such interpretation, elucidated in Quinn, derives from an example of Parfit's."  (§6)

> "We can view the situation here as a multi-player PD in which each “player” is the temporal stage of a single person."  (§6)

> "On Kavka's interpretation, the prisoners are not temporal stages, but rather “subagents” reflecting different desiderata that I might bring to bear on a decision."  (§6)

## §7 Replicas / twins (beyond the companion file)

> "One controversial argument that it is rational to cooperate in a PD relies on the observation that my partner in crime is likely to think and act very much like I do. (See, for example, Davis 1977 and 1985 for a sympathetic presentation of one such argument and Binmore 1994, chapters 3.4 and 3.5, for a reformulation and extended rebuttal.)"  (§7)

> "When the correlation between our behaviors is sufficiently strong or the differences in payoffs is sufficiently great, my expected payoff (as that term is usually understood) is higher if I cooperate than if I defect. The counter argument, of course, is that my action is causally independent of my replica's. Since I can't affect what my accomplice does and since, whatever he does, my payoff is greater if I defect, I should defect."  (§7)

> "It might be noted that what is here called “PD between replicas” is usually called “PD with twins” in the literature."  (§7)

> "It turns out that twins are more likely to cooperate in a PD than strangers, but there seems to be no suggestion that the reasoning that leads them to do so follows the controversial arguments presented above."  (§7, citing Segal and Hershberger 1999)

## §8 Stag hunt

> "The idea mentioned in the introduction that the PD models a problem of cooperation among rational agents is sometimes criticized because, in a true PD, the cooperative outcome is not a nash equilibrium. Any “problem” of this nature, the critics contend, would be an unsolvable one. (See for example, Sugden or Binmore 2005, chapter 4.5.)"  (§8)

> "It might provide a better model for situations where cooperation is difficult, but still possible, and it may also be a better fit for other roles sometimes assigned to the PD."  (§8; "It" is the stag hunt)

## §§9–10 Conditional strategies, Hume, Gauthier, Danielson

> "Peter Danielson, for example, favors a strategy of reciprocal cooperation: if the other player would cooperate if you cooperate and would defect if you don't, then cooperate, but otherwise defect."  (§9)

> "Careful discussion of an asynchronous PD example, as Skyrms (1998) and Vanderschraaf recently note, occurs in the writings of David Hume, well before Flood and Dresher's formulation of the ordinary PD."  (§9; Hume's text: `hume-1739-40-treatise-3-2-5-farmers-dilemma.md`)

> "Another way that conditional moves can be introduced into the PD is by assuming that players have the property that David Gauthier has labeled transparency. A fully transparent player is one whose intentions are completely visible to others."  (§10)

> "One is a version of the strategy that Gauthier has advocated as constrained maximization. The idea is that a player \(j\) should cooperate if the other would cooperate if \(j\) did, and defect otherwise."  (§10)

> "Danielson's program (and other implementations of constrained maximization) cannot be coherently paired with everything. Nevertheless it does move and score well against familiar strategies. It cooperates with \(\bCu\) and itself and it defects against \(\bDu\)."  (§10)

> "The lesson of all this for rational action is not clear."  (§10)

## §11 Finite iteration and backward induction

> "There is a significant theoretical difference on this matter between IPDs of fixed, finite length, like the one pictured above, and those of infinite or indefinitely finite length."  (§11)

> "In games of the first kind, one can prove by an argument known as backward induction that \(\bDu\), \(\bDu\) is the only subgame perfect equilibrium."  (§11)

> "In practice, there is not a great difference between how people behave in long fixed-length IPDs (except in the final few rounds) and those of indeterminate length. This suggests that some of the rationality and common knowledge assumptions used in the backward induction argument (and elsewhere in game theory) are unrealistic."  (§11)

> "Some have used these kinds of observation to argue that the backward induction argument shows that standard assumptions about rationality (with other plausible assumptions) are inconsistent or self-defeating."  (§11, citing Skyrms 1990, pp. 125–139 and Bicchieri 1989)

## §14 Indefinite iteration, Axelrod and Tit for Tat

> "There is an observation, apparently originating in Kavka 1983, and given more mathematical form in Carroll, that the backward induction argument applies as long as an upper bound to the length of the game is common knowledge."  (§14)

> "The iterated version of the PD was discussed from the time the game was devised, but interest accelerated after influential publications of Robert Axelrod in the early eighties. Axelrod invited professional game theorists to submit computer programs for playing IPDs."  (§14)

> "The strategy that scored highest in Axelrod's initial tournament, Tit for Tat (henceforth TFT), simply cooperates on the first round and imitates its opponent's previous move thereafter. More significant than TFT's initial victory, perhaps, is the fact that it won Axelrod's second tournament, whose sixty three entrants were all given the results of the first tournament."  (§14)

> "Axelrod attributed the success of TFT to four properties. It is nice, meaning that it is never the first to defect."  (§14; the other three: retaliatory, forgiving, clear)

> "Suggestive as Axelrod's discussion is, it is worth noting that the ideas are not formulated precisely enough to permit a rigorous demonstration of the supremacy of TFT."  (§14)

> "Indeed, a “folk theorem” of iterated game theory (now widely published — see, for example, Binmore 1992, pp. 373–377) implies that, for any \(p\), \(0 \le p \le 1\) there is a nash equilibrium in which \(p\) is the fraction of times that mutual cooperation occurs."  (§14)

> "In more recent years enthusiasm about TFT has been tempered by increasing skepticism.(See, for example, Binmore 2015 (p. 30) and Northcott and Alexandrova (pp. 71-78)."  (§14)

> "They find that, with the same initial population of strategies present in Axelrod's first tournament, the strategies ranked two and six in that tournament both perform considerably better than top-ranked TFT."  (§14, reporting Rapoport et al 2015)

> "In the one that most closely replicated Axelrod's tournaments. however, TFT finished only fourteenth out of the fifty strategies submitted."  (§14, reporting the 2004–2005 tournaments in Kendall et al 2007; punctuation as in the entry)

## §§16, 18 Evolution; Hobbes and Hume as Skyrms and Vanderschraaf read them

> "According to Skyrms (1998) and Vanderschraaf, both Hobbes and Hume identified it as the strategy that underlies our cooperative behavior in important PD-like situations."  (§16; "it" is GRIM/TRIGGER, which "cooperates until its opponent has defected once, and then defects for the rest of the game")

> "Axelrod's payoffs of 5, 3, 1 and 0 for \(T\), \(R\), \(P\), and \(S\), do meet this condition."  (§18)

DOI-verified records of works Kuhn cites (DOI content negotiation /
Crossref, 2026-09-27; not read): Nash 1951, "Non-Cooperative Games",
Annals of Mathematics 54: 286–295, doi:10.2307/1969529; Hardin 1968,
"The Tragedy of the Commons", Science 162: 1243–1248,
doi:10.1126/science.162.3859.1243; Kavka 1983, "Hobbes's War of All
Against All", Ethics 93: 291–310, doi:10.1086/292435; Hurley 1991,
"Newcomb's Problem, Prisoners' Dilemma, and Collective Action",
Synthese 86: 173–196, doi:10.1007/bf00485806; Segal & Hershberger 1999,
"Cooperation and Competition Between Twins", Evolution and Human
Behavior 20: 29–51, doi:10.1016/s1090-5138(98)00039-7; Lewis 1979, "Prisoner's Dilemma Is a Newcomb Problem" (title as in
Kuhn's bibliography; Crossref: "Prisoners' Dilemma ..."), as
reprinted in Campbell & Sowden (eds.), Paradoxes of Rationality and
Cooperation, UBC Press 1985, pp. 251–255, doi:10.59962/9780774857154-015
(no DOI found for the 1979 Philosophy & Public Affairs 8: 235–240
original); Davis 1977 as reprinted there, pp. 45–59,
doi:10.59962/9780774857154-003; Gauthier, Morals by Agreement,
doi:10.1093/0198249926.001.0001, chapter "Compliance: Maximization
Constrained", pp. 157–189, doi:10.1093/0198249926.003.0006; Hampton,
Hobbes and the Social Contract Tradition, doi:10.1017/cbo9780511625060.

Relied on for: the origin (Flood and Dresher 1950 at RAND; Tucker's
name and prison story; the Peterson/Nash suggestion); the PD1 ordering
and payoff names; dominance, the unique strict Nash equilibrium and
Pareto-optimality of every outcome but mutual defection; the two
standard readings (individual vs. group rationality; selfishness vs.
altruism) and Gauthier's moral reading; the replica argument, its
sympathisers and critics, the twin experiments; Danielson and
constrained maximization; backward induction and its critics;
Axelrod's tournaments, TFT's four properties, Kuhn's assessments and
the later skepticism; the Hobbes/Hume GRIM reading by Skyrms and
Vanderschraaf; Axelrod's payoff values.
Context: Kuhn opens with the Tanya-and-Cinque bank-robbery story and a
cap-exchange story, then characterises PDs from narrowest (§1) to
iterated and evolutionary versions (§§11–21). The scare quotes around
"rational" and "irrational" in §1 are Kuhn's. Axelrod 1984, Gauthier
1986, Danielson 1992, Davis 1977/1985, Binmore 1994, Segal and
Hershberger 1999, Kavka 1983, Skyrms 1998 and Vanderschraaf 1998 were
not read; they are reported only as Kuhn reports them.
