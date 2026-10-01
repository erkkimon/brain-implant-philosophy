---
type: article
about: concept
title: "The paradox of free choice permission"
description: "'You may A or B' is normally understood as 'you may A and you may B', but adding that principle to standard deontic logic lets any permission follow from any other. Von Wright's 1968 name, Kamp's derivation, the pragmatic (implicature) and semantic families of solution as SEP 'Disjunction' groups them, Zimmermann's epistemic reading of 'or', and the link to Ross's paradox."
tags: [problem, paradox, logic, deontic-logic, philosophy-of-language]
timestamp: 2026-10-01T21:51:46Z
---

# The paradox of free choice permission

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Map: Maria Aloni, [SEP Fall 2024 "Disjunction"](https://plato.stanford.edu/archives/fall2024/entries/disjunction/)
§6 (excerpt: `raw/sep-disjunction-fall-2024-free-choice.md`); background:
McNamara & Van De Putte, [SEP Fall 2024 "Deontic Logic"](https://plato.stanford.edu/archives/fall2024/entries/logic-deontic/)
(excerpt: `raw/sep-logic-deontic-fall-2024-rm-ross-and-permission-definition.md`).
Primary works cited, bibliographically verified only (texts not read):
von Wright 1968, Kamp 1974 ([doi:10.1093/aristotelian/74.1.57](https://doi.org/10.1093/aristotelian/74.1.57)),
Zimmermann 2000 ([doi:10.1023/a:1011255819284](https://doi.org/10.1023/a:1011255819284))
(records: `raw/paradox-of-free-choice-bibliographic-records.md`).
Admitted from Wikipedia's List of paradoxes, revision 1376699902, "Logic"
(excerpt: `raw/wikipedia-paradox-of-free-choice-list-entry-and-free-choice-inference.md`).

## The question

Aloni states the datum: "Sentences of the form “You may A or B” are normally understood as implying “You may A and you may B”." (SEP "Disjunction" §6).
The principle that would capture it, labelled there "Free Choice Principle", is P(α ∨ β) → Pα (with P for *it is permitted that*); Aloni: "The following, however, is not a valid principle in standard deontic logic, e.g., von Wright (1968)." (§6).
Adding it does not help, per Aloni's report of Kamp: "As Kamp (1973) pointed out, plainly making the Free Choice principle valid, for example by adding it as an axiom, would not do because it would allow us to derive P q from P p as shown in (37), which is clearly unacceptable:" (§6; the verdict "clearly unacceptable" is Aloni's wording).
The derivation (37): 1. Pp (assumption); 2. P(p ∨ q), by principle (38), Pα → P(α ∨ β); 3. Pq, by the free choice principle. Of (38): "The step leading to 2 in (37) uses the following principle which holds in standard deontic logic:" (§6).
The clash, in Aloni's words: "Intuitively, however, (38) seems invalid (You may go to the beach doesn’t seem to imply You may go to the beach or the cinema), while (36) seems to hold, in direct opposition to the principles of deontic logic." (§6).
The name: "Von Wright (1968) labeled this the paradox of free choice permissions." (§6). Wikipedia's list entry: "Paradox of free choice: Disjunction introduction poses a problem for modal inferences, permitting arbitrary modal statements to be inferred." (List of paradoxes, rev. 1376699902).

**Propositional check (this implant, 2026-10-01; logic, not a position).**
Treat the three permission statements as atoms: *pp* for Pp, *ppq* for
P(p ∨ q), *pq* for Pq; the two principles enter as their instances.
`logic.py check --premises "pp" "pp -> ppq" "ppq -> pq" --conclusion "pq"`
outputs `VALID`. Without the free choice instance,
`logic.py check --premises "pp" "pp -> ppq" --conclusion "pq"` outputs
`INVALID` with the counterexample row `pp=T, ppq=T, pq=F`. Inside the
operator, `logic.py check --premises "p" --conclusion "p | q"` outputs
`VALID` (disjunction introduction) and `logic.py check --premises "p | q" --conclusion "q"`
outputs `INVALID` with `p=T, q=F`. The tool is propositional: it does not
model P, does not derive (38) from the rules of standard deontic logic, and
checks only that the two instances jointly carry Pp to Pq for arbitrary *q*.

## Why it matters

- **Permission defined from obligation.** In standard deontic logic, as McNamara & Van De Putte report, "The most prevalent approach is to take OB as primitive", with PE p defined as ¬OB¬p: "These definitions imply that something is permissible iff (if and only if) its negation is not obligatory, impermissible iff its negation is obligatory," (SEP "Deontic Logic" §2). The rule behind Ross's paradox there is OB-RM (if ⊢ p → q then ⊢ OB p → OB q): "This principle states that whenever something is obligatory, then everything that is a logical consequence is also obligatory (“inherits” that status)." (§6.3). *Steps (this implant; logic, not a position):* ⊢ ¬(p ∨ q) → ¬p; by OB-RM, ⊢ OB¬(p ∨ q) → OB¬p; contraposing, ⊢ ¬OB¬p → ¬OB¬(p ∨ q), which by the definition of PE is ⊢ PE p → PE(p ∨ q), Aloni's (38).
- **A family of paradoxes.** Aloni: "Similar paradoxes arise also for imperatives (see Ross’ paradox, introduced in section 2), epistemic modals (Zimmermann 2000), and other modal constructions." (§6). Wikipedia's article reports that free choice inferences "also arise with other flavors of modality as well as imperatives, conditionals, and other kinds of operators." (Free choice inference, rev. 1374160145).
- **The meaning of "or".** Several solutions revise the analysis of disjunction itself (Positions, below); Aloni reports that the authors she names "all agree in endorsing an “alternative-based” analysis of or" (§6).
- **Granting versus describing permission.** McNamara & Van De Putte cite Kamp among those on the speech act of permitting: "This sentence may be used by an authority to provide permission on the spot or it may be used by a passerby to report on an already existing norm (e.g., a standing municipal regulation)." (§7), with note 79: "See Lemmon 1962b; Kamp 1974, 1979."

## Positions taken

The grouping is Aloni's (SEP "Disjunction" §6): solutions that treat free
choice as pragmatic, and modal (semantic) systems that validate it. Listed
in her order, unranked.

- **Pragmatic: the inference is an implicature, so step 3 fails.** "Many have argued that what we called the Free Choice Principle is merely a pragmatic inference and therefore the step leading to 3 in (37) is unjustified." Owners named by Aloni: "Various ways of deriving free choice inferences as implicatures have been proposed (e.g., Gazdar 1979; Kratzer and Shimoyama 2002; Schulz 2005; Fox 2007 and Franke 2011; see however Fusco 2014 for a critical discussion of pragmatic accounts to free choice)." Schulz's title states the aim: "A Pragmatic Solution for the Paradox of Free Choice Permission" (Synthese 147, 2005, [doi:10.1007/s11229-005-1353-y](https://doi.org/10.1007/s11229-005-1353-y)).
  *For, as Aloni reports it:* "One argument in favor of such a pragmatic account comes from the observation that free choice effects disappear in negative contexts." — "For example, No one is allowed to eat the cake or the ice-cream cannot merely mean that no one is allowed to eat the cake and the ice-cream, as would be expected if free choice effects were semantic entailments rather than pragmatic implicatures (Alonso-Ovalle 2006)."
  *Against, as Aloni reports it:* Fusco 2014 ("Free choice permission and the counterfactuals of pragmatics", *Linguistics and Philosophy* 37, [doi:10.1007/s10988-014-9154-8](https://doi.org/10.1007/s10988-014-9154-8)) is cited for "a critical discussion of pragmatic accounts"; its arguments were not read here.
- **Semantic: step 3 holds, step 2 fails.** "Others have proposed modal systems where the step leading to 3 in (37) is justified while the step leading to 2 is no longer valid, e.g., Aloni 2007, which proposes a uniform account of free choice effects of disjunctions and indefinites under both modals and imperatives." On Aloni 2007 ([doi:10.1007/s11050-007-9010-2](https://doi.org/10.1007/s11050-007-9010-2)): "Thus, You may go to the beach or to the cinema is true only if You may go to the beach and You may go to the cinema are both true." Further owners: "Simons (2005) and Barker (2010) also proposed semantic accounts of free choice inferences, the latter crucially employing an analysis of or in terms of linear logic additive disjunction combined with a representation of strong permission using the deontic reduction strategy (as in Lokhorst 2006)."
  *For, as Aloni reports it:* (38) "seems invalid" intuitively while (36) "seems to hold" (§6, quoted in The question).
  *Against:* the negative-context observation above is offered by Aloni as an argument for the pragmatic family; no reply from a semantic account to it was read here.
- **Zimmermann's epistemic reading (2000).** "Zimmermann (2000), by contrast, proposes a modal analysis of linguistic disjunction which identifies the semantic contribution of or with precisely these epistemic effects (see also Geurts 2005 for a further development of this idea)." — "On Zimmermann’s account linguistic disjunctions should be analyzed as conjunctive lists of epistemic possibilities:" (S1 or … or Sn ↦ ◇S1 ∧ … ∧ ◇Sn). On the paradox: "Finally Zimmermann (2000) distinguishes between (36), which, according to him, is an unjustified logical principle, from the following intuitively valid principle:" — (39) *X may A or may B* ⊨ *X may A and X may B*. Aloni adds: "Zimmermann, however, actually derives only the weaker principle in (41) (under certain assumptions including his Authority principle)." — (41) ◇PA ∧ ◇PB ⊨ □PA ∧ □PB, with □ read "it is certain that" (all §6).
  *Against, in the literature Aloni cites:* "Grice, as we just saw, argued against a semantic account of such effects, which he labeled as the non truth-functional ground of disjunction (Grice 1989)." (§6; in Aloni's text "such effects" are the epistemic effects of disjunction in general, not free choice permission specifically).

Also on record, not read: Asher & Bonevac, "Free Choice Permission is
Strong Permission" (Synthese 145, 2005, [doi:10.1007/s11229-005-6196-z](https://doi.org/10.1007/s11229-005-6196-z));
Kamp's own proposal in the 1974 paper. Their content is not reported.

## Arguments in play

(none recorded as separate argument pages yet). Kamp's derivation (37) and
its propositional check are in The question; the negative-context argument
(Alonso-Ovalle 2006, via Aloni) is in Positions taken.

## Thinkers who addressed it

- **Georg Henrik von Wright** (*An Essay in Deontic Logic and the General Theory of Action*, North-Holland, 1968) — named the paradox, per Aloni (§6).
- **Hans Kamp** ("Free Choice Permission", *Proceedings of the Aristotelian Society* 74, 1974, pp. 57–74; SEP "Disjunction" dates it 1973) — showed that adding the principle lets Pq follow from Pp, per Aloni (§6); also cited on granting permission (SEP "Deontic Logic", n. 79).
- **Gerald Gazdar** (1979), **Angelika Kratzer & Junko Shimoyama** (2002), **Katrin Schulz** (2005), **Danny Fox** (2007, [doi:10.1057/9780230210752_4](https://doi.org/10.1057/9780230210752_4)), **Michael Franke** (2011) — pragmatic derivations as implicatures, per Aloni.
- **Thomas Ede Zimmermann** (*Natural Language Semantics* 8, 2000, pp. 255–290) — "or" as a conjunctive list of epistemic possibilities.
- **Mandy Simons** (2005, [doi:10.1007/s11050-004-2900-7](https://doi.org/10.1007/s11050-004-2900-7)), **Chris Barker** (2010) — semantic accounts, per Aloni.
- **Luis Alonso-Ovalle** (2006, PhD thesis, UMass Amherst) — the negative-context argument; a pragmatic derivation using alternative sets.
- **Maria Aloni** (2007; SEP "Disjunction", 2016) — semantic account in which modals operate on alternatives; the SEP map used here.
- **Melissa Fusco** (2014) — critical discussion of pragmatic accounts, per Aloni.

## Framings and reframings

- **A puzzle about "or", not about permission.** Aloni opens §6: "We can think of disjunction as a means of entertaining different alternatives." Per her report, Kratzer and Shimoyama, Alonso-Ovalle, Aloni, Simons and Zimmermann "differ in their solution of the free choice paradox" but "all agree in endorsing an “alternative-based” analysis of or according to which a disjunctive sentence “A or B” contributes the set of propositional alternatives {A, B}." (§6).
- **Semantics versus pragmatics.** The pragmatic family locates the inference in what is conveyed rather than what is entailed (Positions). Kamp's 1979 paper is titled "Semantics Versus Pragmatics" (SEP "Deontic Logic" bibliography); its content was not read.
- **Kinship with Ross's paradox.** Aloni treats the two together for imperatives: "The most natural interpretation of disjunctive imperatives is as one presenting a choice between different actions:" — "Imperative (17) then cannot imply (18) otherwise when told the former one would be justified in burning the letter rather than posting it (e.g., Mastop 2005; Aloni 2007; Aloni and Ciardelli 2013)." (§2, (17) "Post this letter!", (18) "Post this letter or burn it!"). See [Ross's paradox](ross-paradox.md).
- **Beyond deontic modals.** Wikipedia's article: "Indefinite noun phrases give rise to a similar inference which is also referred to as "free choice" though researchers disagree as to whether it forms a natural class with disjunctive free choice." (rev. 1374160145).

Not in the excerpts held: the texts of von Wright 1968 (archive.org scan
lending-restricted), Kamp 1974 and 1979, Zimmermann 2000, and every other
work in the lists above; they are reported only as SEP "Disjunction"
reports them.

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — see The question.
- [Validity](../vocabulary/validity.md) — (36) "is not a valid principle in standard deontic logic" (Aloni).
- [Classical logic](../methods/classical-logic.md) — disjunction introduction and the propositional check.
- *Permission (PE)*, *deontic logic*, *implicature*, *disjunction introduction*, *strong permission* — open work in [vocabulary](../vocabulary/index.md).
