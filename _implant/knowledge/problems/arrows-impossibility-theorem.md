---
type: article
about: concept
title: "Arrow's impossibility theorem (Arrow's paradox)"
description: "Is there any procedure that turns every possible combination of individual preference orderings over three or more alternatives into a social ordering while respecting unanimity, independence of irrelevant alternatives and non-dictatorship? Arrow's 1950/1951 theorem says no; the page sets out the conditions in the sources' wording and the responses on record side by side — Riker's reading against Mackie's, domain restriction after Black's single-peakedness, Sen's cardinal and interpersonally comparable information, grading — with their owners."
tags: [problem, paradox, decision-theory, social-choice-theory, political-philosophy, welfare-economics]
timestamp: 2026-10-08T21:37:56Z
---

# Arrow's impossibility theorem (Arrow's paradox)

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
sources graded as in [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md). Admitted from Wikipedia's
[List of paradoxes, rev. 1376699902](https://en.wikipedia.org/w/index.php?title=List_of_paradoxes&oldid=1376699902),
section "Decision theory", which gives it as "Arrow's paradox: Given more than two choices, no system can have all the attributes of an ideal voting system at once."
(excerpt: `raw/wikipedia-list-of-paradoxes-arrows-paradox-entry.md`).
Primary text: Arrow, "A Difficulty in the Concept of Social Welfare", *Journal of Political Economy* 58(4), 1950, pp. 328–346 ([doi:10.1086/256963](https://doi.org/10.1086/256963); excerpt: `raw/arrow-1950-difficulty-in-the-concept-of-social-welfare.md`), the article version of *Social Choice and Individual Values* (Wiley 1951; 2nd ed. 1963), not fetched and cited only as quoted in the SEP.
Maps: Morreau, [SEP Fall 2024 "Arrow's Theorem"](https://plato.stanford.edu/archives/fall2024/entries/arrows-theorem/)
(excerpt: `raw/sep-arrows-theorem-fall-2024-conditions-and-responses.md`);
List, [SEP Fall 2024 "Social Choice Theory"](https://plato.stanford.edu/archives/fall2024/entries/social-choice/)
(excerpt: `raw/sep-social-choice-fall-2024-arrows-theorem-and-escape-routes.md`).
Works verified bibliographically only: `raw/arrows-theorem-crossref-records.md`.

## The question

Morreau: "Kenneth Arrow’s “impossibility” theorem—or “general possibility” theorem, as he called it—answers a very basic question in the theory of collective decision-making."
The question, in his preamble: which procedures derive "a collective or
“social” ordering" of alternatives from people's preferences; and
"Arrow’s theorem says there are no such procedures whatsoever—none, anyway, that satisfy certain apparently quite reasonable assumptions concerning the autonomy of the people and the rationality of their preferences."
Arrow put the question in 1950 as: "Can such consistency be attributed to collective modes of choice, where the wills of many people are involved?" (p. 328).

**The precursor case.** Arrow opens with the "paradox of voting": three
individuals rank A, B, C cyclically, majorities prefer A to B and B to C,
and "If the community is to be regarded as behaving rationally, we are forced to say that A is preferred to C. But, in fact, a majority of the community prefers C to A." (1950, p. 329).
Morreau: "This is the “paradox of voting”. Discovered by the Marquis de Condorcet (1785), it shows that possibilities for choosing rationally can be lost when individual preferences are aggregated into social preferences." (§1).

**Logic check (this implant, 2026-10-08; logic, not a position).** Write
AB for: society prefers A to B; and so on. Premises: AB, BC, CA (the three
majority verdicts); AB & BC -> AC (transitivity); CA -> ~AC (asymmetry of
strict preference). `logic.py check --premises "AB" "BC" "CA" "AB & BC -> AC" "CA -> ~AC" --conclusion "AC & ~AC"`
prints `VALID` and `premises are jointly inconsistent — argument is vacuously valid`.
That is the propositional core of the cycle only; the theorem quantifies over all profiles.

**The conditions, in the sources' wording.** Morreau states them "in the
canonical form into which they have settled since" Arrow's 1963 restatement
(§3: "Arrow restated the conditions in the second edition of Social Choice and Individual Values (Arrow 1963).").
List's glosses (§3.2):

- *Unrestricted (universal) domain.* "Universal domain requires the aggregation rule to cope with any level of ‘pluralism’ in its inputs." Morreau: "Unrestricted Domain (U): The domain of \(f\) includes every list \(\langle R_{1}, \ldots, R_{n}\rangle\) of \(n\) weak orderings of \(X\)." (§3.1).
- *Ordering.* "Ordering requires it to produce ‘rational’ social preferences, avoiding Condorcet cycles."
- *Weak Pareto.* "The weak Pareto principle requires that when all individuals strictly prefer alternative \(x\) to alternative \(y\), so does society."
- *Independence of irrelevant alternatives.* "Independence of irrelevant alternatives requires that the social preference between any two alternatives \(x\) and \(y\) depend only on the individual preferences between \(x\) and \(y\), not on individuals’ preferences over other alternatives."
- *Non-dictatorship.* "Non-dictatorship requires that there be no ‘dictator’, who always determines the social preference, regardless of other individuals’ preferences."

The theorem, in List's statement: "Theorem (Arrow 1951/1963): If \(|X| \gt 2\), there exists no preference aggregation rule satisfying universal domain, ordering, the weak Pareto principle, independence of irrelevant alternatives, and non-dictatorship."
List adds: "(Note that pairwise majority voting satisfies all of these conditions except ordering."
Morreau: "Arrow (1951) has the original proof of this “impossibility” theorem." (§3.2).

**The 1950 form.** Arrow's article lists five conditions of its own,
including a condition of "citizens' sovereignty" (non-imposition) and a
condition that the function not reflect individuals' desires negatively, and
concludes that a social welfare function meeting them "must be either imposed or dictatorial" (p. 342).
He calls it the "Possibility Theorem" and reads it thus: "If consumers' values can be represented by a wide range of individual orderings, the doctrine of voters' sovereignty is incompatible with that of collective rationality." (pp. 342–343).
Structural note (this implant): the five-condition list above is Morreau's "canonical form" after the 1963 restatement; its difference from the 1950 list is read off the two texts, not from the 1963 edition, which was not fetched.

**Is it a paradox?** Both SEP entries present it as a theorem with a proof. The label "Arrow's paradox" is the Wikipedia list's; Morreau uses "paradox" for Condorcet's case and writes that "It turns out that Condorcet’s paradox is indeed not an isolated anomaly, the failure of one specific voting method." (§1).
On whether the conditions look harmless, two encyclopedia assessments:
Morreau, "Taken separately, the conditions of Arrow’s theorem do not seem severe." and "Taken together, though, these conditions exclude all possibility of deriving social preferences." (§4);
List, "He proved that, surprisingly, there exists no method for aggregating the preferences of two or more individuals over three or more alternatives into collective preferences, where this method satisfies five seemingly plausible axioms, discussed below." (§1.2).
Arrow himself, in 1950: "These conditions are of course value judgments and could be called into question; taken together, they express the doctrines of citizens' sovereignty and rationality in a very general form, with the citizens being allowed to have a wide range of values." (p. 339).
See [paradox](../vocabulary/paradox.md) for this implant's normative sense.

## Why it matters

- **Voting and markets.** Arrow framed the problem around both: "In a capitalist democracy there are essentially two methods by which social choices can be made: voting, typically used to make "political" decisions, and the market mechanism, typically used to make "economic" decisions." (1950, p. 328).
  He drew from the theorem that "the Possibility Theorem shows that, if no prior assumptions are made about the nature of individual orderings, there is no method of voting which will remove the paradox of voting discussed in Part I, neither plurality voting nor any scheme of proportional representation, no matter how complicated." (p. 342).
- **A field's agenda.** Morreau: "The impossibility theorem itself set much of the agenda for contemporary social choice theory." List judges that "In contemporary social choice theory, it is perhaps fair to say, Arrow’s axiomatic method is more influential than his impossibility theorem itself (on the axiomatic method, see Thomson 2000)." (§1.2).
- **Democratic theory.** Morreau's assessment: "The tenor of Arrow’s theorem is deeply antithetical to the political ideals of the Enlightenment." (§1). The readings of what follows for democracy diverge (Positions, below).
- **Welfare economics and ordinalism.** List quotes Arrow's view "‘that interpersonal comparison of utilities has no meaning and … that there is no meaning relevant to welfare comparisons in the measurability of individual utility.’ (1951/1963: 9)" and assesses that "Arrow’s theorem demonstrates the stark implications of the ‘ordinalist’ assumptions of neoclassical thought." (§1.2).
- **Other aggregation problems.** List lists applications to intrapersonal aggregation, theory choice, evidence amalgamation, similarity and normative uncertainty, and adds: "In each case, the plausibility of Arrow’s theorem depends on the case-specific plausibility of Arrow’s ordinalist framework and the theorem’s conditions." (§3.2).

## Positions taken

Grouped as the two entries group them: readings of what the theorem shows, then escape routes by relaxed condition or richer information (Morreau §§4–5; List §§1.2, 3.3, 4.1). Each line names its owner; none is ranked.
List's framing: "Generally, if we consider Arrow’s framework appropriate and his conditions indispensable, Arrow’s theorem raises a serious challenge." (§3.2).

**Readings of the theorem, side by side.**

- **Riker: against populist democracy.** List: "William Riker (1920–1993), who inspired the Rochester school in political science, interpreted it as a mathematical proof of the impossibility of populist democracy (e." [g., Riker 1982]. Morreau: "There are some who, following Riker (1982), take Arrow’s theorem to show that democracy, conceived as government by the will of the people, is an incoherent illusion." (§1). Riker's *Liberalism against Populism* (1982) was not read.
- **Mackie: democracy defended.** The publisher's abstract of Gerry Mackie, *Democracy Defended* ([2003](https://doi.org/10.1017/cbo9780511490293)), reports the opposing view as "A prevalent view in political science is that democracy is unavoidably chaotic, arbitrary, meaningless, and impossible." and traces it: "Such scepticism began with Condorcet in the eighteenth century, and continued most notably with Arrow and Riker in the twentieth century."
  Mackie's thesis as the abstract states it: "Problems of cycling, agenda control, strategic voting, and dimensional manipulation are not sufficiently harmful, frequent, or irremediable, he argues, to be of normative concern." It adds: "Mackie also examines every serious empirical illustration of cycling and instability, including Riker's famous argument that the US Civil War was due to arbitrary dimensional manipulation." On the conditions, Morreau reports: "Gerry Mackie (2003) argues that there has been equivocation on the notion of irrelevance." (§4.5). The book itself was not read.
- **Some conditions unreasonable.** Morreau: "Others argue that some conditions of the theorem are unreasonable, and from their point of view the prospects for collective choice look much brighter." (§1). List: "Commentators also questioned whether Arrow’s desiderata on an aggregation method are as innocuous as claimed or whether they should be relaxed." (§1.2).
- **Sen: a richer informational basis.** List: "Others, most prominently Amartya Sen (born 1933), who won the 1998 Nobel Memorial Prize, took it to show that ordinal preferences are insufficient for making satisfactory social choices and that social decisions require a richer informational basis." (§1.2). List reports that Sen promoted a "‘possibilist’ interpretation" (his 1998 Nobel lecture, printed as ["The Possibility of Social Choice"](https://doi.org/10.1257/aer.89.3.349), not read here) and assesses: "Nowadays most social choice theorists have moved beyond the negative interpretations of Arrow’s theorem and are interested in the trade-offs involved in finding satisfactory decision procedures and the possibilities opened up by relaxing certain restrictive assumptions." (§1.2).

**Escape routes, condition by condition.**

- **Restrict the domain (Black's single-peakedness).** List: "Black (1948) proved that if the domain of the aggregation rule is restricted to the set of all profiles of individual preference orderings satisfying single-peakedness, majority cycles cannot occur, and the most preferred alternative of the median individual relative to the relevant left-right alignment is a Condorcet winner (assuming \(n\) is odd)." (§3.3.1; [Black 1948](https://doi.org/10.1086/256633)). Morreau calls such domains "Arrow consistent": "Such domains are said to be Arrow consistent." (§5.1). "Sen (1966) showed that all these conditions imply a weaker condition, triple-wise value-restriction." (List §3.3.1).
  - *For U as stated:* Arrow, as quoted by Morreau: "If we do not wish to require any prior knowledge of the tastes of individuals before specifying our social welfare function, that function will have to be defined for every logically possible set of individual orderings." (§4.1).
  - *Against U in some cases:* Morreau: "Whether it is sensible to impose U or any other domain condition on a social welfare function depends very much on the particulars of the choice problem being studied." (§4.1).
  - *Does it happen?* List: "There has been much discussion on whether, and under what conditions, real-world preferences fall into such a restricted domain." Miller (1992) proposes deliberation as a route (Morreau §5.1). The empirical finding and its critics side by side (List §3.3.1): "Experimental evidence from deliberative opinion polls, where participants’ preferences were elicited before and after a period of group deliberation, is consistent with this hypothesis (List, Luskin, Fishkin, and McLean 2013), though further empirical work is needed." and "For a critical assessment of the idea of deliberation-induced ‘meta-agreement’, see Ottonelli and Porello (2013)."
- **Relax ordering.** Requiring only quasi-transitivity: Sen (1969: Theorem V) showed compatibility with the other conditions (Morreau §4.2); "Allan Gibbard showed that the only social welfare functions made available by allowing intransitivity of social indifference, while keeping Arrow’s other requirements in place, are what he called liberum veto oligarchies (Gibbard 1969, 2014)." (§4.2). On Arrow's rationale for ordering, "Criticized by Buchanan (1954) for transferring properties of individual choice to collective choice, Arrow in the second edition of Social Choice and Individual Values gave a different rationale." (§4.2; [Buchanan 1954](https://doi.org/10.1086/257496)).
- **Relax weak Pareto.** List's assessment: "The weak Pareto principle is arguably hard to give up." (§3.3.3). Sen's critique of it is the [liberal paradox](liberal-paradox.md): "Although the weak Pareto principle is arguably one of the least contentious ones of Arrow’s conditions, Sen (1970a) offered a critique of it that applies when the aggregation rule is interpreted not as a voting method, but as a social evaluation method which a social planner can use to rank social alternatives in an order of social desirability." (List). Morreau: "Sen argued that even these limited demands might be found excessive on moral grounds (Sen 1979: Section IV)." (§4.3).
- **Relax or reinterpret non-dictatorship.** Morreau's assessments: "This apparently straightforward condition has attracted very little attention in the literature." and, from his Zelig example, "Even pairwise majority voting, that paradigm of a democratic procedure, is in Arrow’s sense sometimes a dictatorship." and "Sometimes there is nothing undemocratic about having a “dictator”, in Arrow’s technical sense." (§4.4).
- **Relax independence.** *Against:* the Mackie equivocation argument (above), with Morreau's example: "But I also requires that the ranking of Gore with respect to Bush should be independent of voters’ preferences for Nader, and this does not seem right because he was on the ballot and, in the ordinary sense, he was a relevant alternative to them." (§4.5). On Arrow's dead-candidate motivation (1950, p. 337), Morreau judges "Apparently, then, Arrow’s example misses its mark." and reports "Hansson (1973) argues that Arrow confused his independence condition for another; compare Bordes and Tideman (1991) for a contrary view." *For:* "Proofs of the Gibbard-Sattherthwaite theorem (Gibbard 1973, Sattherthwaite 1975) associate vulnerability to strategic voting systematically with violation of I, and Iain McLean argues on this ground that voting methods ought to satisfy this condition: “Take out [I] and you have gross manipulability” (McLean 2003: 16)." (§4.5).
- **Cardinal, interpersonally comparable utility (Sen).** "Sen (1970b) generalized Arrow’s framework to incorporate such richer information." (List §4.1; *Collective Choice and Social Welfare*). Morreau: "One important finding was that having cardinal utilities is not by itself enough to avoid an impossibility result." and "In addition, utilities have to be interpersonally comparable." (§5.4). List: "In a welfare-aggregation context, Arrow’s impossibility can therefore be traced to a lack of interpersonal comparability (for detailed analyses, see Sen 1977 and Roberts 1980)." and "An important conclusion, therefore, is that Rawls’s difference principle, the classical utilitarian principle, and even the head-count method of poverty measurement can all be seen as solutions to Arrow’s aggregation problem that become possible once we go beyond Arrow’s framework of ordinal, interpersonally non-comparable preferences." (§4.1).
  - *Limit, by context:* List: "In voting contexts, this assumption may be plausible, as we often may not be able to elicit more information from voters than their ordinal rankings of the options." (§4.1). Arrow's own position, per Morreau: "Arrow saw no reason to provide aggregation procedures with information about the strength of preferences because he thought that they cannot put such information to meaningful use." (§2.1).
- **Grades instead of rankings.** "Michel Balinski and Rida Laraki (2007) showed that scoring and grading enable an “escape” from Arrow’s impossibility while staying within an ordinal framework." Against: when graders' thresholds differ, "Then a close relative of Arrow’s impossibility returns (Morreau 2016)." Morreau also reports that "Arrow came to realize, late in his life, that scoring and grading create possibilities for democracy that his framework unnecessarily rules out of consideration." (§5.3, citing a 2012 interview).

**How often the precursor cycle arises (findings, as List reports them, §2).** "If all possible preference profiles are equally likely to occur (the so-called ‘impartial culture’ scenario), majority cycles should therefore be probable in large electorates (Gehrlein 1983)."
"However, the probability of cycles can be significantly lower under certain systematic, even small, deviations from an impartial culture (List and Goodin 2001: Appendix 3; Tsetlin, Regenwetter, and Grofman 2003; Regenwetter et al."
Mackie's empirical re-examination is reported above from the abstract.

## Arguments in play

(none recorded as separate argument pages yet). The paradox-of-voting cycle (logic check above), Arrow's dead-candidate argument for independence (1950, p. 337) and the equivocation argument against it (Mackie 2003, per Morreau §4.5) are quoted above.

## Thinkers who addressed it

- **Marquis de Condorcet** (1785) — the paradox of voting (Morreau §1); McLean (2003) "finds a first statement of Independence" in him (§4.5).
- **Duncan Black** (1948) — single-peakedness (List §3.3.1). **Kenneth Arrow** (1950; 1951; 1963) — the theorem; Nobel Prize in economics 1972 (Morreau, preamble). **James Buchanan** (1954) — the ordering condition (§4.2).
- **Amartya Sen** (1966–1998) — value restriction, quasi-transitivity, the liberal paradox, cardinal comparability, the "possibilist" reading (List; Morreau). **Allan Gibbard** (1969, 1973) — oligarchy; manipulability (Morreau §§4.2, 4.5). **Bengt Hansson** (1973), **Iain McLean** (2003) — independence (§4.5).
- **William Riker** (1982) against **Gerry Mackie** (2003) — on what follows for democracy (List §1.2; Morreau §§1, 4.5; Crossref abstract). **Michel Balinski & Rida Laraki** (2007) — grading (§5.3).
- **Michael Morreau**, **Christian List** — SEP authors; their assessments are marked as theirs above.

## Framings and reframings

- **Impossibility or possibility.** Arrow named it the "Possibility Theorem" (1950, p. 342); the SEP preamble calls it the "“impossibility” theorem—or “general possibility” theorem, as he called it". List reports Sen's "‘possibilist’ interpretation" (§1.2).
- **Voters' sovereignty against collective rationality.** Arrow's own reframing (1950, pp. 342–343), quoted under The question.
- **Voting method or social evaluation.** List: "The lessons from Arrow’s theorem depend, in part, on how we interpret an Arrovian social welfare function." (§1.2) — ordinal inputs being easier to defend for voting than for welfare evaluation.
- **Precursor, not isolated anomaly.** Morreau reads the theorem as generalising Condorcet's cycle (§1); "Arrow broke new ground by coming at it from the opposite direction." — from conditions to procedures rather than procedure by procedure.
- **Neighbour.** The [liberal paradox](liberal-paradox.md) (Sen 1970a) is presented by List (§3.4) and Morreau (§4.3) as a further conflict involving weak Pareto and unrestricted domain.

Left out: Borda counting (Morreau §5.2), judgment aggregation (Morreau §6), and Arrow 1951/1963 beyond what the SEP quotes (not fetched).

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — see The question, last paragraph.
- [Validity](../vocabulary/validity.md) — the logic check of the cycle.
- Social welfare function, profile, weak ordering, single-peakedness, interpersonal comparability — open work in [vocabulary](../vocabulary/index.md).

Related problems: [no-show paradox](no-show-paradox.md) (Brandt, Geist & Peters §1), [voting paradox](voting-paradox.md) (Arrow 1950, p. 329; Morreau §1), [paradox of voting (Downs)](paradox-of-voting.md) (same name, a different problem), [the liberal paradox](liberal-paradox.md) (Sen 1970a;
List §3.4; Morreau §4.3). Branch: [Problems](./index.md).
