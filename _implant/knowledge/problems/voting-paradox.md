---
type: article
about: concept
title: "Voting paradox (Condorcet's paradox)"
description: "Can majorities over three or more alternatives be cyclic — A beats B, B beats C, C beats A — when every voter's own ranking is transitive? Condorcet showed it in 1785; the page sets out his example, the three-voter cycle, Black's single-peakedness, the probability results as reported, and the Riker–Mackie disagreement on how often cycles occur, with their owners."
tags: [problem, paradox, decision-theory, social-choice-theory, political-philosophy]
timestamp: 2026-10-08T21:37:56Z
---

# Voting paradox (Condorcet's paradox)

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
sources graded as in [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md). Admitted from Wikipedia's
[List of paradoxes, rev. 1376699902](https://en.wikipedia.org/w/index.php?title=List_of_paradoxes&oldid=1376699902),
section "Decision theory", which gives it as "Voting paradox: Also known as Condorcet's paradox and paradox of voting. A group of separately rational individuals may have preferences that are irrational in the aggregate."
The same list has a separate "Paradox of voting" entry (the Downs paradox, on the cost of voting), treated in [paradox of voting](paradox-of-voting.md).
Excerpt for both: `raw/voting-paradox-crossref-and-wikipedia-records.md`.
Primary text: Condorcet, *Essai sur l'application de l'analyse à la probabilité des décisions rendues à la pluralité des voix* (Paris: Imprimerie Royale, 1785), Discours préliminaire, pp. lx–lxi ([Gallica ark:/12148/bpt6k417181](https://gallica.bnf.fr/ark:/12148/bpt6k417181); read in the archive.org scans [essaisurlapplica00cond](https://archive.org/details/essaisurlapplica00cond) and [bub_gb_TxQGwC1kTnkC](https://archive.org/details/bub_gb_TxQGwC1kTnkC); public domain; excerpt: `raw/condorcet-1785-essai-discours-preliminaire-contradictory-system.md`).
Maps: Pacuit, [SEP Fall 2024 "Voting Methods"](https://plato.stanford.edu/archives/fall2024/entries/voting-methods/)
(excerpt: `raw/sep-voting-methods-fall-2024-condorcets-paradox-and-cycle-frequency.md`);
List, [SEP Fall 2024 "Social Choice Theory"](https://plato.stanford.edu/archives/fall2024/entries/social-choice/)
(excerpts: `raw/sep-social-choice-fall-2024-condorcets-paradox-and-single-peakedness.md`, `raw/sep-social-choice-fall-2024-arrows-theorem-and-escape-routes.md`).
Works verified bibliographically only: `raw/voting-paradox-crossref-and-wikipedia-records.md`, `raw/arrows-theorem-crossref-records.md`.

## The question

List (SEP §1.1): "Condorcet’s second insight, often called Condorcet’s paradox, is the observation that majority preferences can be ‘irrational’ (specifically, intransitive) even when individual preferences are ‘rational’ (specifically, transitive)."
Pacuit (SEP §3.1): "A key observation of Condorcet (which has become known as the Condorcet Paradox) is that the majority ordering may have cycles (even when all the voters submit rankings of the alternatives)."

**The three-voter case.** Pacuit: "Condorcet’s original example was more complicated, but the following situation with three voters and three candidates illustrates the phenomenon:"
one voter each ranks A over B over C, B over C over A, and C over A over B; each pairwise contest is won two to one, and "That is, there is a majority cycle \(A>_M B >_M C >_M A\)." "This means that there is no Condorcet winner." (§3.1).
List's version uses thirds of a group: "Then there are majorities (of two thirds) for \(x\) against \(y\), for \(y\) against \(z\), and for \(z\) against \(x\): a ‘cycle’, which violates transitivity." He defines the term: "Furthermore, no alternative is a Condorcet winner, an alternative that beats, or at least ties with, every other alternative in pairwise majority contests." (§1.1).

**Condorcet's own example (1785).** Condorcet resolves each voter's opinion into pairwise propositions ("A vaut mieux que B", A is better than B) and counts 8 possible systems of such propositions for three candidates, of which 6 do not imply contradiction (pp. lx–lxi). He then asks: "On peut demander maintenant si la pluralité peut avoir lieu en faveur d'un de ces systèmes contradictoires, & on trouvera que cela est possible." (p. lxi).
In his 60-voter example the pairwise majorities are 33 to 27, 35 to 25 and 42 to 18, and "Le système qui obtient la pluralité sera donc composé des trois propositions, A vaut mieux que B, C vaut mieux que A, B vaut mieux que C." His verdict on that system: "Ce système est le troisième, & un de ceux qui impliquent contradiction." (p. lxi).

**Logic check (this implant, 2026-10-09; logic, not a position).** Write AB for: the majority prefers A to B; and so on. Premises: AB, BC, CA (the three
majority verdicts of the three-voter case); AB & BC -> AC (transitivity of the majority relation); CA -> ~AC (asymmetry of strict preference).
`logic.py check --premises "AB" "BC" "CA" "AB & BC -> AC" "CA -> ~AC" --conclusion "AC & ~AC"`
prints `VALID` and `premises are jointly inconsistent — argument is vacuously valid`.
So the three majority verdicts cannot all hold together with transitivity and asymmetry of the majority relation; which premise to give up is what the positions below differ on. Arithmetic (this implant): Condorcet's count of 8 systems is 2 × 2 × 2 (one of two propositions per pair, three pairs); the 6 that do not imply contradiction are the 3 × 2 × 1 = 6 strict rankings of three candidates.

**Is it a paradox?** The label is the sources': List writes "often called Condorcet’s paradox"; Pacuit introduces "voting paradoxes — i.e., anomalies that highlight problems with different voting methods" (§3, excerpt `raw/sep-voting-methods-fall-2024-no-show-paradox.md`); Condorcet's own word is "contradiction"; Arrow (1950) calls it the "paradox of voting" (see [Arrow's impossibility theorem](arrows-impossibility-theorem.md)). Morreau: "This is the “paradox of voting”. Discovered by the Marquis de Condorcet (1785), it shows that possibilities for choosing rationally can be lost when individual preferences are aggregated into social preferences." ([SEP Fall 2024 "Arrow's Theorem"](https://plato.stanford.edu/archives/fall2024/entries/arrows-theorem/) §1; excerpt `raw/sep-arrows-theorem-fall-2024-conditions-and-responses.md`).
See [paradox](../vocabulary/paradox.md) for this implant's normative sense.

## Why it matters

- **Majority rule.** List's assessment: "Condorcet anticipated a key theme of modern social choice theory: majority rule is at once a plausible method of collective decision making and yet subject to some surprising problems." and "Resolving or bypassing these problems remains one of social choice theory’s core concerns." (§1.1).
- **Group rationality.** Arrow (1950, p. 329; [doi:10.1086/256963](https://doi.org/10.1086/256963)), on the three-person case: "If the community is to be regarded as behaving rationally, we are forced to say that A is preferred to C. But, in fact, a majority of the community prefers C to A." (excerpt `raw/arrow-1950-difficulty-in-the-concept-of-social-welfare.md`).
- **Arrow's theorem.** Morreau: "It turns out that Condorcet’s paradox is indeed not an isolated anomaly, the failure of one specific voting method." (§1). List: "(Note that pairwise majority voting satisfies all of these conditions except ordering." — the condition that "requires it to produce ‘rational’ social preferences, avoiding Condorcet cycles." (§3.2). The generalisation is on the [Arrow's impossibility theorem](arrows-impossibility-theorem.md) page.
- **Democratic theory.** Mackie's publisher's abstract places the paradox at the start of a sceptical tradition: "Such scepticism began with Condorcet in the eighteenth century, and continued most notably with Arrow and Riker in the twentieth century." (Crossref record, [doi:10.1017/cbo9780511490293](https://doi.org/10.1017/cbo9780511490293)).
- **Model or reality.** Pacuit: "The main question is whether the voting paradoxes are simply features of the formal framework used to represent an election scenario or formalizations of real-life phenomena." (§5).

## Positions taken

Grouped by which premise of the cycle they work on; each line names its owner; none is ranked.

- **Condorcet: discount the contradictory.** Pacuit: "Many authors argue that voters with cyclic preference orderings have inconsistent opinions about the candidates and should be ignored by a voting method (in particular, Condorcet forcefully argued this point)." (§3.1). For majority systems that imply contradiction, Condorcet announces he will examine the election "en n'ayant aucun égard à ces combinaisons contradictoires" and then "en y ayant égard" (p. lxi).
- **Restrict the profiles: Black's single-peakedness.** List: "The best-known cohesion condition is single-peakedness (Black 1948)." "Black (1948) proved that if the domain of the aggregation rule is restricted to the set of all profiles of individual preference orderings satisfying single-peakedness, majority cycles cannot occur, and the most preferred alternative of the median individual relative to the relevant left-right alignment is a Condorcet winner (assuming \(n\) is odd)." (§3.3.1; [Black 1948](https://doi.org/10.1086/256633)). Black's book *The Theory of Committees and Elections* (1958; Springer reissue [doi:10.1007/978-94-009-4225-7](https://doi.org/10.1007/978-94-009-4225-7)) was not read.
  - *Where it is plausible:* List: "Single-peakedness is plausible in some democratic contexts." with the example "If the alternatives in \(X\) are different tax rates, for example, each individual may have a most preferred tax rate (which will be lower for a libertarian individual than for a socialist) and prefer other tax rates less as they get more distant from the ideal." (§3.3.1).
  - *Weaker conditions:* "Sen (1966) showed that all these conditions imply a weaker condition, triple-wise value-restriction." and "Triple-wise value-restriction suffices for transitive majority preferences." (List §3.3.1).
  - *Whether real preferences fit:* List: "There has been much discussion on whether, and under what conditions, real-world preferences fall into such a restricted domain." The deliberation finding and its critics side by side: "Experimental evidence from deliberative opinion polls, where participants’ preferences were elicited before and after a period of group deliberation, is consistent with this hypothesis (List, Luskin, Fishkin, and McLean 2013), though further empirical work is needed." and "For a critical assessment of the idea of deliberation-induced ‘meta-agreement’, see Ottonelli and Porello (2013)." (§3.3.1). Pacuit: "For instance, List et al. 2013 has evidence suggesting that deliberation reduces the probability of a Condorcet cycle occurring." (§5).
- **Use another rule.** List: "The Borda count, formally defined later, avoids Condorcet’s paradox but violates one of Arrow’s conditions, the independence of irrelevant alternatives." (§1.3). Rules that elect the Condorcet winner whenever there is one ("Condorcet consistent", Pacuit §3.1.1) meet other costs; one is the [no-show paradox](no-show-paradox.md), by Moulin's 1988 theorem as Pacuit states it (§3.3; excerpt `raw/sep-voting-methods-fall-2024-no-show-paradox.md`).
- **Riker: cycles undermine populism.** List: "William Riker (1920–1993), who inspired the Rochester school in political science, interpreted it as a mathematical proof of the impossibility of populist democracy (e." [g., Riker 1982] — "it" being Arrow's theorem (§1.2). Riker's *Liberalism against Populism* (W.H. Freeman, 1982; ISBN 9780716712459) was not read.
- **Mackie: cycles neither frequent nor troubling.** The publisher's abstract of *Democracy Defended* (2003): "Problems of cycling, agenda control, strategic voting, and dimensional manipulation are not sufficiently harmful, frequent, or irremediable, he argues, to be of normative concern." and "Mackie also examines every serious empirical illustration of cycling and instability, including Riker's famous argument that the US Civil War was due to arbitrary dimensional manipulation." and "Almost every empirical claim is erroneous, and none is normatively troubling, Mackie says." The book was not read.

**How often cycles occur: findings as reported, side by side.**

- *Under impartial culture (each ranking equally likely).* List: "It can be shown that the proportion of preference profiles (among all possible ones) that lead to cyclical majority preferences increases with the number of individuals \((n)\) and the number of alternatives \((|X|).\)" and "If all possible preference profiles are equally likely to occur (the so-called ‘impartial culture’ scenario), majority cycles should therefore be probable in large electorates (Gehrlein 1983)." (§2; [Gehrlein 1983](https://doi.org/10.1007/BF00143070)).
  Pacuit: "Riker (1982, p. 122) has a table of the relevant calculations." "For example, if there are five candidates and seven voters, then the probability of a majority cycle is 21.5 percent." "This probability increases to 25.1 percent as the number of voters increases to infinity (keeping the number of candidates fixed) and to 100 percent as the number of candidates increases to infinity (keeping the number of voters fixed)." (§5; overview in Gehrlein 2006, *Condorcet's Paradox*, [doi:10.1007/3-540-33799-7](https://doi.org/10.1007/3-540-33799-7)).
  For three candidates and a large electorate, the pinned Wikipedia article ([rev. 1377853662](https://en.wikipedia.org/w/index.php?title=Condorcet_paradox&oldid=1377853662)) gives 8.77% under impartial culture and 6.25% under impartial anonymous culture, citing Guilbaud ([2012 reprint](https://doi.org/10.3917/reco.634.0659)) and Gehrlein ([2002](https://doi.org/10.1023/A:1015551010381)); those sources were not read, and the figures are the article's.
- *Against impartial culture.* Pacuit: "Many authors have noted that the impartial culture is a significant idealization that almost certainly does not occur in real-life elections." "Tsetlin et al. (2003) go even further arguing that the impartial culture is a worst-case scenario in the sense that any deviation results in lower probabilities of a majority cycle (see Regenwetter et al. 2006, for a complete discussion of this issue, and List and Goodin 2001, Appendix 3, for a related result)." (§5; [Tsetlin, Regenwetter & Grofman 2003](https://doi.org/10.1007/s00355-003-0269-z)). List: "However, the probability of cycles can be significantly lower under certain systematic, even small, deviations from an impartial culture (List and Goodin 2001: Appendix 3; Tsetlin, Regenwetter, and Grofman 2003; Regenwetter et al." (§2).
- *Riker and Mackie on the evidence.* Pacuit: "While Riker (1982) offers a number of intriguing examples, the most comprehensive analysis of the empirical evidence for majority cycles is provided by Mackie (2003, especially Chapters 14 and 15)." "The conclusion is that, in striking contrast to the probabilistic analysis referenced above, majority cycles typically have not occurred in actual elections." and "However, this literature has not reached a consensus about this issue (cf. Riker 1982): The problem is that the available data typically does not include voters’ opinions about all pairwise comparison of candidates, which is needed to determine if there is a majority cycle." (§5).

## Arguments in play

(none recorded as separate argument pages yet). The propositional core of the three-voter cycle is checked above; Black's theorem, Sen's value-restriction result and the impartial-culture calculations are reported as theorems and findings of their authors, not reconstructed here.

## Thinkers who addressed it

- **Ramon Llull** (c1235–1315) — "In the Middle Ages, Ramon Llull (c1235–1315) proposed the aggregation method of pairwise majority voting, while Nicolas Cusanus (1401–1464) proposed a variant of the Borda count (McLean 1990)." (List §1.3).
- **Marquis de Condorcet** (1785) — the example and its "contradiction" (Essai, p. lxi); **Jean-Charles de Borda** — the Borda count (List §1.3).
- **Duncan Black** (1948; 1958) — single-peakedness; List: "It was largely thanks to the Scottish economist Duncan Black (1908–1991) that Condorcet’s, Borda’s, and Dodgson’s social-choice-theoretic ideas were drawn to the attention of the modern research community (McLean, McMillan, and Monroe 1995)." (§1.3).
- **G.-Th. Guilbaud** ([1952] 1966) — the "Condorcet effect" (List §1.3). **Kenneth Arrow** (1950/1951) — the generalisation. **Amartya Sen** (1966) — value-restriction.
- **William Riker** (1982) against **Gerry Mackie** (2003) — on frequency and on what follows for democracy (Pacuit §5; List §1.2; Crossref abstract).
- **William Gehrlein** (1983; 2002; 2006), **Tsetlin, Regenwetter & Grofman** (2003) — probabilities (as reported by List and Pacuit).
- **Eric Pacuit**, **Christian List** — SEP authors; their assessments are marked as theirs above.

## Framings and reframings

- **Contradictory system of propositions.** Condorcet's own framing: a majority can form for a system of pairwise propositions that "impliquent contradiction" (p. lxi).
- **Intransitivity of majority preference.** List's framing: "‘irrational’ (specifically, intransitive)" majority preferences from "‘rational’ (specifically, transitive)" individual ones (§1.1).
- **The Condorcet effect.** List reports that Guilbaud started "a French literature on the Condorcet effect, the logical problem underlying Condorcet’s paradox" (§1.3; quoted sentence in the raw excerpt).
- **Special case of Arrow.** The pinned Wikipedia article: "Condorcet's paradox is a special case of Arrow's paradox, which shows that any kind of social decision-making process is either self-contradictory, a dictatorship, or incorporates information about the strength of different voters' preferences (e.g. cardinal utility or rated voting)." — the article's framing; see [Arrow's impossibility theorem](arrows-impossibility-theorem.md) for the theorem in the SEP authors' wording.
- **Another route to a social cycle.** In Sen's [liberal paradox](liberal-paradox.md), List's Lewd/Prude example ends: "So, we are faced with a social preference cycle" (SEP §3.4; excerpt `raw/sep-social-choice-fall-2024-liberal-paradox.md`) — a cycle produced by decisiveness and weak Pareto rather than by pairwise majorities.
- **Name collision.** The list's "Paradox of voting" (Downs) is a different problem: [paradox of voting](paradox-of-voting.md).

Left out: Condorcet's jury theorem (List §1.1; a different result in the same 1785 Essai); what Fishburn (1974) named Condorcet's other paradox (Pacuit §3.1.1); Condorcet-consistent methods in detail (Pacuit §3.1.1); Riker 1982, Black 1958, Gehrlein's works and Mackie 2003 beyond what the cited sources report (not fetched); the Wikipedia article's reported real-election cycles (sources not read).

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — see The question, last paragraph.
- [Validity](../vocabulary/validity.md) — the logic check of the cycle.
- Transitivity, Condorcet winner, majority cycle, single-peakedness, impartial culture — open work in [vocabulary](../vocabulary/index.md).

Related problems: [Arrow's impossibility theorem](arrows-impossibility-theorem.md) (Morreau §1; List §3.2);
[the liberal paradox](liberal-paradox.md) (List §3.4); [the no-show paradox](no-show-paradox.md) (Pacuit §§3.1.1, 3.3);
[paradox of voting](paradox-of-voting.md) (name only). Branch: [Problems](./index.md).
