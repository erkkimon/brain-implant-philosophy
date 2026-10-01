---
type: article
about: concept
title: "Ross's paradox"
description: "From 'Slip the letter into the letter-box!' classical disjunction introduction yields 'Slip the letter into the letter-box or burn it!'. Alf Ross 1941 (Theoria 7) on satisfaction versus validity of imperatives; the deontic form OB m, therefore OB(m ∨ b), as the first challenge to the inheritance principle RM (SEP 'Deontic Logic'); the responses on record — elementary confusion (Føllesdal & Hilpinen), pragmatics (Castañeda; Hare per Vranas), rejecting RM (Jackson, Goble, Cariani, Hansson), intensional disjunction and choice-offering free-choice readings (Aloni)."
tags: [problem, paradox, logic, deontic-logic, imperative-logic]
timestamp: 2026-10-01T21:51:46Z
---

# Ross's paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Primary text: Alf Ross, "Imperatives and Logic", *Theoria* 7(1), 1941,
pp. 53–71 ([doi:10.1111/j.1755-2567.1941.tb00034.x](https://doi.org/10.1111/j.1755-2567.1941.tb00034.x);
scan: [archive.org](https://archive.org/details/theoria_1941_7_part-1);
excerpt: `raw/ross-1941-imperatives-and-logic-letter-box.md`).
Maps: McNamara & Van De Putte, [SEP Fall 2024 "Deontic Logic"](https://plato.stanford.edu/archives/fall2024/entries/logic-deontic/)
§6.3 (excerpts: `raw/sep-logic-deontic-fall-2024-rm-ross-and-permission-definition.md`,
`raw/sep-logic-deontic-fall-2024-ross-letter-and-rejecting-rm.md`);
Aloni, [SEP Fall 2024 "Disjunction"](https://plato.stanford.edu/archives/fall2024/entries/disjunction/)
§§2.2, 6 (excerpts: `raw/sep-disjunction-fall-2024-addition-and-ross-imperatives.md`,
`raw/sep-disjunction-fall-2024-free-choice.md`).
Admitted from Wikipedia's List of paradoxes, revision 1376699902, "Logic"
(excerpt: `raw/wikipedia-imperative-logic-ross-paradox.md`).

## The question

Ross states the inference: "that is to say, from the imperative I(x) we may infer the imperative I(x v y), e.g. from: slip the letter into the letter-box! we may infer, slip the letter into the letter-box or burn it!" (1941, §10, p. 62).
Read as a logic of satisfaction it holds: "It will be seen that, interpreted as a satisfaction-function, this inference is unimpeachable: If the first imperative is satisfied, (if the letter has been slipped into the letter-box), then the other imperative too has been satisfied (it is then true that either has the letter been slipped into the letter-box, or it has been burnt)." (p. 62).
His objection: "But it is equally obvious that this inference is not immediately conceived to be logically valid." (p. 62).
Ross's contrast is between this satisfaction reading and the [validity](../vocabulary/validity.md) of the inference; Wikipedia states the resulting question as "what we mean by a valid imperative inference" (below).

Wikipedia's list entry: "Disjunction introduction poses a problem for imperative inference by seemingly permitting arbitrary imperatives to be inferred." (List of paradoxes, rev. 1376699902).
Its article frames the stake: "The challenge is what we mean by a valid imperative inference. For valid declarative inference, the premises give you a reason to believe the conclusion. One might think that for imperative inference, the premises give you a reason to do as the conclusion says. While Ross's paradox seems to suggest otherwise, its severity has been subject of much debate." ("Imperative logic", rev. 1319526929).

**Deontic form.** McNamara & Van De Putte formalise "It is obligatory that the letter is mailed" as OB *m* and derive OB(*m* ∨ *b*), "the letter is mailed (m) or the letter is burned (b)", by the principle OB-RM: "This principle states that whenever something is obligatory, then everything that is a logical consequence is also obligatory (“inherits” that status)." (SEP §6.3). Their assessment of the result: "It seems rather odd to say that an obligation to mail the letter entails an obligation to mail the letter or burn it (where burning the letter is presumably forbidden), one that can be fulfilled by burning the letter, which invites from the offender: “Well at least I did one thing right by burning it”." (§6.3).

**Propositional check (this implant, 2026-10-01; logic, not a position).**
Let *m* stand for *the letter is mailed* and *b* for *the letter is burned*.
`logic.py check --premises "m" --conclusion "m | b"` outputs `VALID`: the
contents stand in the relation of disjunction introduction, the rule
Wikipedia's entry names. The converse,
`--premises "m | b" --conclusion "m"`, outputs `INVALID` with the
counterexample row `b=T, m=F` — the row in which the disjunctive demand is
met by burning. Adding *not b* restores *m*: `--premises "m | b" "~b" --conclusion "m"`
outputs `VALID`. The tool checks only these truth-functional contents; it
has no imperative mood and no OB operator, so it does not model the step
from *m* ⊢ *m* ∨ *b* to OB *m* ⊢ OB(*m* ∨ *b*), which is the step the
paradox concerns.

## Why it matters

- **Imperative logic.** Ross puts the letter case among inferences "in full accord with the logic of imperatives enunciated, but which are not immediately felt to be evident, but rather evidently false" (§10, pp. 61–62), and adds: "Similar results are arrived at by applying the other truth-functions, but I do not find it necessary to pursue this question." (p. 62).
- **Deontic logic.** "The earliest and most well-known challenge to RM is Ross’s Paradox (Ross 1941)." (McNamara & Van De Putte, SEP §6.3). The same section introduces the Good Samaritan paradox (Prior 1958) as a related case where "similar issues arise when we weaken a conjunction to one of its conjuncts" (§6.3).
- **Disjunction.** Aloni: "The validity of addition has also been disputed in relation to imperative logic." (SEP "Disjunction" §2.2).
- **Free choice.** Aloni links it to permission: "Similar paradoxes arise also for imperatives (see Ross’ paradox, introduced in section 2), epistemic modals (Zimmermann 2000), and other modal constructions." (§6). See [the paradox of free choice](paradox-of-free-choice.md).

## Positions taken

The two SEP entries group the deontic and disjunction responses (their
grouping: keep RM, reject RM; intensional disjunction, choice-offering);
Ross's own view, Hare and Vranas are added by owner. Listed unranked.

- **Ross: two logics, and an "evasion" (1941).** Ross distinguishes a logic of satisfaction from a logic of validity of imperatives. Of the first: "The second possibility ot solution is no actual solution, but an evasion of the problem." (§10, p. 61; OCR "ot"), since "The logical element refers solely to the fulfilment of the demand, or rather to the indicative sentences expressing the theme of demand as real, or the demand as fulfilled." (p. 61). He locates the felt force of practical inference elsewhere: "The immediate feeling of evidence does not refer to the satisfaction of the imperative, but rather to something like the »validity» or the »existence» of the imperative, no matter how those expressions are to be understood." (p. 61). His table gives the disjunction case under both: "»Slip the letter into the letter-box!» is satisfied, then the imperative, »Either slip the letter into the letter-box or burn it!» is also satisfied." (p. 65), and, for validity, "»Slip the letter into the letter-box!» is valid, then the compound imperative, »Either the letter is to be slipped into the letter-box, or it is to be burnt» is valid too." (p. 66).
- **Keep RM; the paradox is a confusion (Føllesdal & Hilpinen 1971).** Reported by the SEP: "Some defend RM and blame the Ross paradox on an elementary confusion (Føllesdal & Hilpinen 1971)" (§6.3). Their text was not read.
- **Keep RM; pragmatics explain it (Castañeda 1981).** "or cite pragmatic features to explain away the puzzle (Castañeda 1981): no one would, e.g., merely utter the statement that John ought to mail or burn the letter, knowing that in fact John ought to just mail the letter." (SEP §6.3). Castañeda 1981, pp. 37–85, was not read.
- **Permissive presuppositions as implicatures (Hare 1967, as Vranas reports it).** "(4) Hare ([21]: 309–17; cf. Bennett [6]: 317–8) argues that permissive presuppositions are Gricean conversational implicatures and are thus cancellable, but Williams replies that he understands permissive presuppositions neither as entailments nor as cancellable implicatures" (Vranas 2010, n. 13, p. 66; excerpt: `raw/vranas-2009-imperative-inference-permissive-presuppositions.md`). Hare's paper (*Mind* 76, 1967) was not read.
- **Reject RM (Jackson 1985; Goble 1990a; Cariani 2013; Hansson 1990, 2001).** "However, since these paradoxes all at least appear to depend on OB-RM, a natural solution to the problems is to undercut the paradoxes by rejecting OB-RM itself." (SEP §6.3; "natural" is the authors' word). "Two accessible and closely related examples of approaches to deontic logic that reject OB-RM from a principled philosophical perspective are Jackson 1985 and Goble 1990a." "A third, somewhat different principled strategy is proposed in Cariani 2013 and studied in formal detail in Van De Putte 2019." Of Hansson: "He also sees OB-RM as the main culprit in the paradoxes of standard deontic logic" (§6.3).
- **Intensional disjunction.** Aloni reports the option and assesses it: "One way to tackle this would be to treat or in (18) as a case of intensional disjunction." "This solution however would fail to account for a characteristic aspect of the interpretation of disjunctive imperatives which arguably explains the failure of addition in these cases, namely their choice offering potential." (SEP "Disjunction" §2.2; the assessment is Aloni's).
- **Choice-offering, free-choice reading (Mastop 2005; Aloni 2007; Aloni & Ciardelli 2013).** "The most natural interpretation of disjunctive imperatives is as one presenting a choice between different actions:" — on which the disjunctive imperative implies that you may post the letter and you may burn it — and "Imperative (17) then cannot imply (18) otherwise when told the former one would be justified in burning the letter rather than posting it (e.g., Mastop 2005; Aloni 2007; Aloni and Ciardelli 2013)." (§2.2; "most natural" is Aloni's).
- **Imperative inference defended (Vranas 2010).** Against those who deny imperative inferences because "distinct imperatives have conflicting permissive presuppositions (“surrender or fight” permits you to fight without surrendering, but “surrender” does not)", Vranas argues "that, on a reasonable understanding of ‘inference’, some everyday-life inferences do have imperatives as premises and conclusions, and that issuing imperatives with conflicting permissive presuppositions does not amount to changing one’s mind." (abstract, p. 59).

## Arguments in play

(none recorded as separate argument pages yet). The inference and the
propositional check are in The question; the step that carries it in
deontic logic is OB-RM, quoted there.

## Thinkers who addressed it

- **Alf Ross** (1941, *Theoria* 7: 53–71; English version *Philosophy of Science* 11, 1944, pp. 30–46, [doi:10.1086/286823](https://doi.org/10.1086/286823), "Reprint of Ross 1941" per Vranas 2010 ref. 39) — states the letter case; satisfaction versus validity.
- **Dagfinn Føllesdal & Risto Hilpinen** ("Deontic Logic: An Introduction", 1971 per SEP, Crossref 1970, [doi:10.1007/978-94-010-3146-2_1](https://doi.org/10.1007/978-94-010-3146-2_1)) — "elementary confusion", per SEP.
- **R. M. Hare** ("Some Alleged Differences between Imperatives and Indicatives", *Mind* 76, 1967, pp. 309–326, [doi:10.1093/mind/lxxvi.303.309](https://doi.org/10.1093/mind/lxxvi.303.309)) — permissive presuppositions as implicatures, per Vranas.
- **Hans Kamp** ("Free Choice Permission", 1974, [doi:10.1093/aristotelian/74.1.57](https://doi.org/10.1093/aristotelian/74.1.57)) — the free-choice permission problem that Wikipedia's article connects to Ross ("Some strands of this debate connect it to Hans Kamp's paradox of free choice", rev. 1319526929).
- **Hector-Neri Castañeda** ("The Paradoxes of Deontic Logic: The Simplest Solution to All of Them in One Fell Swoop", 1981, pp. 37–85, [doi:10.1007/978-94-009-8484-4_2](https://doi.org/10.1007/978-94-009-8484-4_2)) — pragmatic explanation, per SEP.
- **Frank Jackson** (1985), **Lou Goble** (1990a), **Sven Ove Hansson** (1990, 2001), **Fabrizio Cariani** (2013), **Frederik Van De Putte** (2019) — deontic logics without OB-RM, per SEP §6.3.
- **C. L. Hamblin** (*Imperatives*, Blackwell, 1987, ISBN 978-0-631-15193-7) — listed in the bibliography of Wikipedia's "Imperative logic" article; Vranas cites the book (pp. 87–8) on self-addressed imperatives. No passage of it on Ross's paradox was read, so no position is reported.
- **Maria Aloni** (2007; with Ciardelli 2013; SEP "Disjunction", 2016) and **Mastop** (2005) — choice-offering reading of disjunctive imperatives.
- **Peter B. M. Vranas** (2010, [doi:10.1007/s10992-009-9108-8](https://doi.org/10.1007/s10992-009-9108-8)) — defends imperative inference against the permissive-presupposition objection.
- **Paul McNamara & Frederik Van De Putte** (SEP 2021 revision) — survey of the RM-related paradoxes.

## Framings and reframings

- **A problem for imperatives or for obligations?** Ross's case is a pair of imperatives; the SEP "Deontic Logic" entry restates it as obligation sentences, OB *m* and OB(*m* ∨ *b*), and files it under RM (§6.3). Aloni files it under the rule of addition (SEP "Disjunction" §2.2).
- **One of a family under RM.** McNamara & Van De Putte treat Ross's paradox and the Good Samaritan together as "RM-related paradoxes" (§6.3).
- **A free-choice effect.** Aloni: "Von Wright (1968) labeled this the paradox of free choice permissions." "Similar paradoxes arise also for imperatives (see Ross’ paradox, introduced in section 2), epistemic modals (Zimmermann 2000), and other modal constructions." (§6). Wikipedia: "Some strands of this debate connect it to Hans Kamp's paradox of free choice, in which disjunction introduction leads to absurd conclusions when applied under the scope of a possibility modal." (rev. 1319526929). See [the paradox of free choice](paradox-of-free-choice.md).
- **Whether there is imperative inference at all.** Vranas reports a line of authors (Williams 1963; Wedeking 1970; Harrison 1991; Hansen 2008) who "have denied that imperative inferences exist" and the example "“Surrender; therefore, surrender or fight” is apparently an argument corresponding to an inference from an imperative to an imperative." (2010, abstract, p. 59).

Not in the excerpts held: the texts of Hare 1967, Føllesdal & Hilpinen
1971, Castañeda 1981, Kamp 1974, Hamblin 1987, Jackson 1985, Goble 1990a,
Cariani 2013 and Ross's 1944 English version; their arguments are reported
only as the cited secondary sources report them.

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — see The question.
- [Validity](../vocabulary/validity.md) — Ross's "logically valid" and his separate "validity" of an imperative (a term he leaves to be "further defined", §11).
- [Classical logic](../methods/classical-logic.md) — disjunction introduction, the propositional check above.
- *Imperative*, *satisfaction*, *deontic operator*, *RM (inheritance)*, *free choice permission*, *implicature* — open work in [vocabulary](../vocabulary/index.md).
