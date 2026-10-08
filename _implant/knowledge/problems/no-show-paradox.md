---
type: article
about: concept
title: No-show paradox
description: "Can casting a sincere ballot leave a voter worse off than staying at home? Fishburn and Brams (1983) named the no-show paradox for instant-runoff and similar rules; Moulin (1988) proved that with four or more candidates every Condorcet-consistent rule is open to it; the page sets out the definitions, the theorem and its sharpened bounds, the two senses of the term, and the assessments on record, each with its owner."
tags: [problem, paradox, decision-theory, social-choice-theory, voting-theory]
timestamp: 2026-10-08T21:37:56Z
---

# No-show paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
sources graded as in [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md). Admitted from Wikipedia's
[List of paradoxes, rev. 1376699902](https://en.wikipedia.org/w/index.php?title=List_of_paradoxes&oldid=1376699902),
section "Decision theory", which gives it as "No-show paradox: A situation in some voting systems where voting for one's candidate could cause them to lose, as opposed to not showing up to vote."
(excerpt: `raw/wikipedia-list-of-paradoxes-no-show-paradox-entry.md`, which also excerpts the
[Participation criterion article, rev. 1373018325](https://en.wikipedia.org/w/index.php?title=Participation_criterion&oldid=1373018325),
used only as a pointer to sources).
Primary texts, verified bibliographically and not read: Fishburn & Brams, "Paradoxes of Preferential Voting", *Mathematics Magazine* 56(4), 1983, pp. 207–214 ([doi:10.1080/0025570X.1983.11977044](https://doi.org/10.1080/0025570X.1983.11977044));
Moulin, "Condorcet's principle implies the no show paradox", *Journal of Economic Theory* 45(1), 1988, pp. 53–64 ([doi:10.1016/0022-0531(88)90253-0](https://doi.org/10.1016/0022-0531%2888%2990253-0))
(records: `raw/no-show-paradox-crossref-records.md`); what they say is reported here as the sources below report it.
Map: Pacuit, [SEP Fall 2024 "Voting Methods"](https://plato.stanford.edu/archives/fall2024/entries/voting-methods/), §3.3
(excerpt: `raw/sep-voting-methods-fall-2024-no-show-paradox.md`).
Research read: Brandt, Geist & Peters, [arXiv 1602.08063](https://arxiv.org/abs/1602.08063) (AAMAS 2016; journal version *Mathematical Social Sciences* 90, 2017, 18–27, [doi:10.1016/j.mathsocsci.2016.09.003](https://doi.org/10.1016/j.mathsocsci.2016.09.003); excerpt: `raw/brandt-geist-peters-2017-no-show-paradox-sat-bounds.md`);
Holliday & Pacuit, "Split Cycle", *Public Choice* 197, 2023, 1–62 ([doi:10.1007/s11127-023-01042-3](https://doi.org/10.1007/s11127-023-01042-3); excerpt: `raw/holliday-pacuit-2023-strong-no-show-paradox-participation.md`);
McCune & Wilson, [arXiv 2403.18857](https://arxiv.org/abs/2403.18857) (*Theory and Decision* 98, 2025; excerpt: `raw/mccune-wilson-2025-negative-participation-paradox-irv.md`).

## The question

Pacuit places it among "Variable Population Paradoxes" (SEP §3.3): "No-Show Paradox: One way that a candidate may receive “more support” is to have more voters show up to an election that support them. Voting methods that do not satisfy this version of monotonicity are said to be susceptible to the no-show paradox (Fishburn and Brams 1983)."
The monotonicity in question: "A voting method is monotonic provided that receiving more support from the voters is always better for a candidate." (§3.2).
Brandt, Geist & Peters state the axiom whose failure is at issue: "Participation was first considered by Fishburn and Brams [18] and requires that no voter should be worse off by joining an electorate, or—alternatively—that no voter should benefit by abstaining from an election." (§1), formally "Definition 2. A voting rule f satisfies participation if all voters always weakly prefer voting to not voting" (§3).
The question, then: can a voting method guarantee that turning out to vote sincerely never yields an outcome the voter likes less than the one produced by staying away — and which methods can?

**Pacuit's example (SEP §3.3), Plurality with Runoff.** Eleven voters: 4 rank A > B > C, 3 rank B > C > A, 1 ranks C > A > B, 3 rank C > B > A.
"Candidate \(C\) is the Plurality with Runoff winner" — A and C go to the runoff with 4 first places each, and C beats A 7–4.
If 2 voters of the first group stay home, A has the fewest first places, B and C go to the runoff, and "Candidate \(B\) is the Plurality with Runoff winner" (5–4).
Pacuit: "Since the 2 voters that did not show up to this election rank \(B\) above \(C\), they prefer the outcome of the second election in which they did not participate!"

**Arithmetic check (this implant, 2026-10-09; arithmetic, not a position).**
Full electorate, first places: A 4, B 3, C 1 + 3 = 4; B eliminated; B's 3 voters (B > C > A) go to C: C 4 + 3 = 7, A 4. C wins.
Two A-voters absent: A 2, B 3, C 4; A eliminated; A's 2 voters (A > B > C) go to B: B 3 + 2 = 5, C 4. B wins. The absent voters rank B above C.

**Is it a paradox?** Pacuit uses the word for "anomalies that highlight problems with different voting methods" (§3).
Brandt, Geist & Peters judge the axiom's appeal "evident" — "The desirability of this axiom in any context with voluntary participation is evident." — and call Fishburn and Brams's finding surprising: "All the more surprisingly, Fishburn and Brams have shown that single transferable vote (STV), a common voting rule, violates participation and referred to this phenomenon as the no-show paradox." (§1).
Holliday & Pacuit dissent on Moulin's sense of the term: "In our view, this participation criterion is problematic." (§1.2; see Positions).
See [paradox](../vocabulary/paradox.md) for this implant's normative sense.

## Why it matters

- **Turnout and sincere voting.** Pacuit's example has voters who "prefer the outcome of the second election in which they did not participate!" (SEP §3.3). Holliday & Pacuit: "Of course, a method not satisfying participation will incentivize some strategic non-voting, as the voters in question will have an incentive not to vote (sincerely)." — quoted in their assessment below.
- **Condorcet consistency.** A common requirement collides with it. Pacuit: "However, one natural requirement for a voting method is that if there is a Condorcet winner, then that candidate should be elected. Voting methods that satisfy this property are called Condorcet consistent." (§3.1.1); "It turns out that always electing a Condorcet winner, if one exists, makes a voting method susceptible to the above failure of monotonicity." (§3.3).
- **Rules in use.** Pacuit lists methods affected: "The Coombs Rule, Hare Rule and Majority Judgement (using the tie-breaking mechanism from Balinski and Laraki 2010) are all susceptible to the no-show paradox." (§3.3). Brandt, Geist & Peters name single transferable vote (§1, quoted above).
- **Law.** The Wikipedia article reports that in German constitutional law "courts have ruled such a possibility violates the principle of one man, one vote" (citing BVerfG 2 BvC 1/07, 3 July 2008); the ruling was not read here.

## Positions taken

Grouped by what each owner holds; none is ranked.

**The impossibility (Moulin 1988).** Pacuit's statement: "Theorem (Moulin 1988)." "If there are four or more candidates, then every Condorcet consistent voting method is susceptible to the no-show paradox." (SEP §3.3).
Brandt, Geist & Peters give Moulin's bounds: "A seminal result in social choice theory by Moulin [28] has shown that Condorcet-consistency and participation are incompatible whenever there are at least 4 alternatives and 25 voters." and "Moulin proves that the bound on the number of alternatives is tight by showing that the maximin voting rule (with lexicographic tie-breaking) satisfies the desired properties when there are at most 3 alternatives." (§1).

**Sharpened bounds.** Brandt, Geist & Peters report that "This bound was recently brought down to 21 voters by Kardel [23]." (§2) and prove, using SAT solvers: "Theorem 3. There is no Condorcet extension that satisfies participation for m ⩾ 4 and n ⩾ 12." and "Theorem 4. There is a Condorcet extension f that satisfies participation for m = 4 and n ⩽ 11." (§6; m alternatives, n voters).
They also report: "Simplified proofs of Moulin’s theorem are given by Schulze [33] and Smith [34]. Holzman [21] and Sanver and Zwicker [32] strengthen Moulin’s theorem by weakening Condorcet-consistency and participation, respectively." (§2).

**Strong forms.** Duddy (2014), in his abstract: "We show that when there are at least four candidates and when voters may express indifference, every voting rule satisfying Condorcet’s principle must generate both of these paradoxes." — the two being a first-place ballot that makes its candidate lose and a last-place ballot that makes its candidate win.
Pacuit lists "Perez 2001, Campbell and Kelly 2002, Jimeno et al. 2009, Duddy 2014, Brandt et al. 2017, 2019, and Nunez and Sanver 2017" for "further discussions and generalizations of this result." (§3.3).

**Escapes by changing the model.** Brandt, Geist & Peters: "When assuming that voters have incomplete preferences over sets or lotteries, participation and Condorcet-consistency can be satisfies simultaneously" (§1, "satisfies" sic). Holliday & Pacuit note a limit of Moulin's proof: "Note that Moulin (1988) only proves participation failure for Condorcet consistent voting methods that are resolute, i.e., always pick a unique winner, which requires imposing an arbitrary tiebreaking rule that violates anonymity or neutrality (see Section 5.1.1)." (§1.2, n. 11).

**Which axiom to keep, side by side.**
- *Condorcet consistency valued.* Brandt, Geist & Peters: "While the desirability of Condorcet-consistency—as that of any other axiom—has been subject to criticism, many scholars agree that it is very appealing—if not indispensable—and a large part of the social choice literature deals exclusively with Condorcet-consistent voting rules" (§1).
- *Participation valued.* The same authors: "The desirability of this axiom in any context with voluntary participation is evident." (§1).
- *Participation too strong; involvement kept.* Holliday & Pacuit: "Thus, we are not so troubled by results showing that all Condorcet consistent voting methods fail versions of participation11 and therefore incentivize some strategic behavior. By contrast, we are troubled by failures of positive or negative involvement, as this shows that the method responds in the wrong way to unequivocal support for (resp. rejection of) a candidate." (§1.2; "11" is their footnote marker) and "In our view, the examples in the proof of Proposition B.6 show that participation is too strong to require." (App. B). Their method, Split Cycle, is in their words "not only immune to spoilers but also immune to the strong no show paradox." (§1.2).

**How often it occurs (findings, as their authors report them).** Brandt, Geist & Peters: "Ray [30] and Lepelley and Merlin [26] investigate how frequently this phenomenon occurs in practice." (§2; Ray 1986, not read).
McCune & Wilson, for the related "negative participation paradox" under instant runoff (defined: "if the addition of voters who rank candidate A last causes A to go from losing to winning"), studied "361 single-winner IRV elections with at least three candidates" (§4) and report a probability of 3.3% with actual ballots and 6.4% with completed ballots, and 46.2% / 56.1% among elections where the IRV winner differs from the plurality winner (Table 5).
For Condorcet methods, the Wikipedia article states "Studies suggest such failures may be empirically rare, however." citing Mohsin et al. (AAMAS 2023), not read here.

## Arguments in play

(none recorded as separate argument pages yet).

**Logic check (this implant, 2026-10-09; logic, not a position).** Write CC: the method is Condorcet consistent; M4: there are four or more candidates; PART: the method satisfies participation. Moulin's theorem in Pacuit's statement gives the conditional "CC & M4 -> ~PART".
`logic.py check --premises "CC & M4 -> ~PART" "PART" "M4" --conclusion "~CC"` prints `VALID`: whoever keeps participation with four or more candidates gives up Condorcet consistency.
`logic.py check --premises "CC & M4 -> ~PART" "~PART" --conclusion "CC"` prints `INVALID` with counterexample rows such as `CC=F, M4=T, PART=F`: from a violation of participation, Condorcet consistency does not follow.
That is the propositional shape only; the theorem's content is the conditional, which the sources prove and this implant does not.

- **Holliday & Pacuit's neutrality argument against participation (§1.2).** When new voters rank x above y but x is not at their top nor y at their bottom, majority cycles can shift both, and in their words "A certain kind of neutrality then requires that the winner changes from x to y." (the passage is excerpted in the raw file).

## Thinkers who addressed it

- **Peter C. Fishburn & Steven J. Brams** (1983) — named the no-show paradox for STV (Brandt, Geist & Peters §1; Holliday & Pacuit §1.2; SEP §3.3).
- **Dipankar Ray** (1986) — practical possibility under STV (Brandt, Geist & Peters §2).
- **Hervé Moulin** (1988) — the Condorcet impossibility (SEP §3.3).
- **Joaquín Pérez** (2001) — "strong" no-show paradoxes for correspondences (Holliday & Pacuit n. 10). **Conal Duddy** (2014) — both strong forms (abstract).
- **Felix Brandt, Christian Geist, Dominik Peters** (2016/2017) — the 12-voter bound and its optimality.
- **Wesley H. Holliday & Eric Pacuit** (2023) — the critique of participation; Pacuit also wrote the SEP entry.
- **David McCune & Jennifer Wilson** (2024/2025) — frequency under instant runoff.

## Framings and reframings

- **Two senses of "no-show paradox".** Holliday & Pacuit: "The term “no show paradox” was coined by Fishburn and Brams (1983) for violations of what is now called the negative involvement criterion (see Pérez 2001)." and "The reason seems to be that Moulin (1988) changed the meaning of “no show paradox” to stand not for a violation of negative (or positive) involvement but rather for a violation of the participation criterion" (§1.2). Hence: "The failure of positive or negative involvement is now sometimes called the “strong no show paradox.”" and "Perez (2001) calls violations of positive involvement the “positive strong no show paradox” and violations of negative involvement the “negative strong no show paradox.”" (n. 10).
- **A failure of monotonicity.** Pacuit treats it as a "version of monotonicity" for variable populations, next to the monotonicity failures of §3.2 (SEP §3.3).
- **Fishburn and Brams's example, as reported.** Holliday & Pacuit: "In an example of Fishburn and Brams, two voters are unable to make it to an Instant Runoff election, due to their car breaking down. They later realize that had they voted in the election, their least favorite candidate would have won." (§1.2).
- **One impossibility among others.** Brandt, Geist & Peters: "There are a number of well-known impossibility theorems—among which Arrow’s impossibility is arguably the most famous—which state that certain axioms are incompatible with each other." and "One impossibility that requires unusually high bounds on the number of voters and alternatives is Moulin’s no-show paradox [28], which states that the axioms of Condorcet-consistency and participation are incompatible whenever there are at least 4 alternatives and 25 voters." (§1) — see [Arrow's impossibility theorem](arrows-impossibility-theorem.md).
- **Condorcet's paradox in the background.** Pacuit: "The Condorcet Paradox shows that there may not always be a Condorcet winner in an election." (§3.1.1) — see the [voting paradox](voting-paradox.md); Condorcet consistency only constrains profiles that have one.
- **Neighbour: multiple districts.** Pacuit: "Note that these methods are also susceptible to the no-show paradox. As is the case with the no-show paradox, every Condorcet consistent voting method is susceptible to the multiple districts paradox (see Zwicker, 2016, Proposition 2.5)." (§3.3).

Left out: the German *negatives Stimmgewicht* case and quorum rules in referendums (reported only by the Wikipedia article; primary sources not read); Fishburn & Brams 1983 and Moulin 1988 beyond what the sources above report (not fetched); Brandt et al.'s set-valued and probabilistic results in detail.

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — see The question, last paragraph.
- [Validity](../vocabulary/validity.md) — the logic check.
- Participation, Condorcet consistency, monotonicity, positive/negative involvement, resolute voting method — open work in [vocabulary](../vocabulary/index.md).

Related problems: [Arrow's impossibility theorem](arrows-impossibility-theorem.md) (Brandt, Geist & Peters §1);
[the voting paradox](voting-paradox.md) (SEP "Voting Methods" §3.1). Branch: [Problems](./index.md).
