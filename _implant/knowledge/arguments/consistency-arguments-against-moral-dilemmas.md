---
type: article
about: concept
title: The consistency arguments against moral dilemmas
description: "Two arguments, as McConnell (SEP 2024, §4) formalises them, that genuine moral dilemmas are inconsistent with accepted principles — (PC) OA → ¬O¬A plus (PD), and 'ought' implies 'can' plus agglomeration — with a propositional check, the exits each side takes (Williams, van Fraassen, Marcus, Lemmon, Conee, Brink) and the deontic-logic counterparts."
tags: [argument, ethics, moral-dilemmas, deontic-logic, williams, marcus]
timestamp: 2026-09-28T07:01:48Z
---

# The consistency arguments against moral dilemmas

An argument page of the [arguments](index.md) branch, written under
[Reporting, not endorsing](../../conventions/reporting-not-endorsing.md) and
[How claims are graded](../../conventions/how-claims-are-graded.md). The
problem these arguments belong to is [moral dilemmas](../problems/moral-dilemmas.md);
the term is defined on [dilemma](../vocabulary/dilemma.md). Main source:
Terrance McConnell, "Moral Dilemmas", SEP Fall 2024 (substantive revision
2022-07-25), [§§4–5](https://plato.stanford.edu/archives/fall2024/entries/moral-dilemmas/);
excerpts: `raw/sep-moral-dilemmas-fall-2024-concept-and-consistency-arguments.md`.

## Earliest primary source

- **The agglomeration argument.** McConnell names the principle after
  Williams: "dubbed by some the agglomeration principle (Williams 1965)"
  (§4). Bernard Williams, "Ethical Consistency", *Proceedings of the
  Aristotelian Society, Supplementary Volume* 39 (1965), pp. 103–124
  (SEP bibliography; the DOI record [10.1093/aristoteliansupp/39.1.103](https://doi.org/10.1093/aristoteliansupp/39.1.103)
  spans pp. 103–138, the symposium with Atkinson). Reprinted in C. W.
  Gowans (ed.), *Moral Dilemmas* (Oxford UP, 1987), pp. 115–137 (SEP). Its
  text was not read here; it is cited as McConnell and Marcus report it.
- **Earlier on 'ought' implies 'can'.** E. J. Lemmon, "Moral Dilemmas",
  *Philosophical Review* (1962), pp. 139–158 ([10.2307/2182983](https://doi.org/10.2307/2182983);
  volume 71 in the DOI record and in SEP "Deontic Logic", 70 in SEP "Moral
  Dilemmas"), is listed by McConnell among "the earlier contributors to
  this debate" (§5). Not read here.
- **The first (PC + PD) argument** is set out in the form below by
  McConnell (§4), who notes that PC and PD are "two standard principles of
  deontic logic" (§4). Structural note (manifest [G4](../../vision/manifest.md)):
  McConnell's §4 does not name who first derived O¬A from PD and a
  dilemma; this page records no earliest source for that form.
- Other early papers the SEP bibliography lists, all verified by DOI and
  not read here: van Fraassen, *Values and the Heart's Command*, *J. Phil.*
  70 (1973): 5–19 ([10.2307/2024762](https://doi.org/10.2307/2024762));
  McConnell, *Moral Dilemmas and Consistency in Ethics*, *Canadian J.
  Phil.* 8 (1978): 269–287 ([10.1080/00455091.1978.10717051](https://doi.org/10.1080/00455091.1978.10717051));
  Trigg, "Moral Conflict", *Mind* 80 (1971): 41–55 ([10.1093/mind/lxxx.317.41](https://doi.org/10.1093/mind/lxxx.317.41));
  Conee, "Against Moral Dilemmas", *Phil. Review* 91 (1982): 87–97
  ([10.2307/2184670](https://doi.org/10.2307/2184670)); Brink, "Moral
  Conflict and Its Structure", *Phil. Review* 103 (1994): 215–247
  ([10.2307/2185737](https://doi.org/10.2307/2185737)). Gowans's 1987
  anthology reprints Lemmon, Williams, van Fraassen, McConnell 1978, Marcus
  and Conee (SEP bibliography).

## Standard reconstruction

Reconstruction and notation are McConnell's (SEP 2024, §4). OA: the agent
ought to do A; ¬C: "cannot"; □: physical necessity. "Premises (1), (2), and
(3) represent the claim that moral dilemmas exist." (§4)

**Argument 1 — from PC and PD.** PC is "(PC) OA → ¬O¬A": "Intuitively this principle just says that the same action cannot be both obligatory and forbidden." PD is "(PD) □(A → B) → (OA → OB)" (§4).

```
1. OA   2. OB   3. ¬C(A & B)
4. □(A → B) → (OA → OB)           PD
5. □¬(B & A)            (from 3)
6. □(B → ¬A)            (from 5)
7. □(B → ¬A) → (OB → O¬A)         (instance of 4)
8. OB → O¬A             (6, 7)
9. O¬A                  (2, 8)
10. OA and O¬A          (1, 9)
11. ¬O¬A                (PC, 1)   — contradicts 9
```

"So if we assume PC and PD, then the existence of dilemmas generates an inconsistency of the old-fashioned logical sort." (§4) McConnell adds that "Two other principles accepted in most systems of deontic logic entail PC" — "(OP) OA → PA" and "(D) PA ↔ ¬O¬A" (§4).

**Argument 2 — from 'ought' implies 'can' and agglomeration.**

```
1. OA   2. OB   3. ¬C(A & B)
4. OA → CA                  (for all A)           'ought' implies 'can'
5. (OA & OB) → O(A & B)     (for all A and all B) agglomeration
6. O(A & B) → C(A & B)      (an instance of 4)
7. OA & OB                  (from 1 and 2)
8. O(A & B)                 (from 5 and 7)
9. ¬O(A & B)                (from 3 and 6)
```

Form: deductive, reductio — each set of premises is inconsistent, so one
member goes. McConnell: the arguments show "that one cannot consistently acknowledge the reality of moral dilemmas while holding selected (and seemingly plausible) principles" (§4).

**Propositional check (this implant, 2026-09-27).** The encoding is this
implant's, not McConnell's, and abstracts away the modal and deontic logic:
each formula is an atomic letter — OA, OB, ONA for O¬A, OAB for O(A & B),
CAB for C(A & B), NBNA for □(B → ¬A), PA for PA. Steps 4→5→6 and 4→7 of
Argument 1 are modal inferences and are entered as conditionals (`~CAB ->
NBNA`, `NBNA -> (OB -> ONA)`); steps 4→6 of Argument 2 are instantiation.
Inconsistency was tested by asking `logic.py` for `Q & ~Q`:

- Argument 1, premises `OA`, `OB`, `~CAB`, `~CAB -> NBNA`, `NBNA -> (OB -> ONA)`, `OA -> ~ONA`: `VALID` / `premises are jointly inconsistent — argument is vacuously valid`. Without `OA -> ~ONA` (PC): `INVALID`, counterexample `CAB=F, NBNA=T, OA=T, OB=T, ONA=T, Q=T` (and the same row with `Q=F`; 2 counterexample rows). Without the PD line `NBNA -> (OB -> ONA)`: `INVALID`, counterexample `CAB=F, NBNA=T, OA=T, OB=T, ONA=F, Q=T` (and the same row with `Q=F`; 2 counterexample rows).
- Argument 2, premises `OA`, `OB`, `~CAB`, `OAB -> CAB`, `OA & OB -> OAB`: `VALID` / `premises are jointly inconsistent — argument is vacuously valid`. Without agglomeration: `INVALID`, counterexample `CAB=F, OA=T, OAB=F, OB=T, Q=T` (and the same row with `Q=F`; 2 counterexample rows). Without the 'ought'-implies-'can' instance: `INVALID`, counterexample `CAB=F, OA=T, OAB=T, OB=T, Q=T` (and the same row with `Q=F`; 2 counterexample rows).
- `OA -> PA`, `PA <-> ~ONA` therefore `OA -> ~ONA` (OP and D yield PC): `VALID`.

So in the skeleton each principle is needed for the contradiction, and
dropping any one restores consistency. The problem page's earlier check
(2026-09-26) agrees for Argument 2.

## Supports

The denial of genuine moral dilemmas — the position that "Opponents of moral dilemmas have generally held that the crucial principles in the two arguments above are conceptually true, and therefore we must deny the possibility of genuine dilemmas. (See, for example, Conee 1982 and Zimmerman 1996.)" (McConnell §5). Stated on [moral dilemmas](../problems/moral-dilemmas.md).

## Which premise is disputed, and by whom

McConnell lists the exits: "Now obviously the inconsistency in the first argument can be avoided if one denies either PC or PD. And the inconsistency in the second argument can be averted if one gives up either the principle that ‘ought’ implies ‘can’ or the agglomeration principle. There is, of course, another way to avoid these inconsistencies: deny the possibility of genuine moral dilemmas." (§5)

- **Premises 1–3 (a dilemma exists).** Denied by opponents of dilemmas,
  Conee 1982 and Zimmerman 1996 (as reported §5, above). For symmetrical
  cases, "the pertinent, all-things-considered requirement in such a case is disjunctive: Sophie should act to save one or the other of her children, since that is the best that she can do (for example, Zimmerman 1996, Chapter 7)" (§5).
- **Agglomeration (Argument 2, premise 5).** Rejected, per McConnell, by
  "others, as a refutation of the agglomeration principle (for example, Williams 1965 and van Fraassen 1973)" (§5). Marcus (1980) rejects it
  in her own words: "From 'A ought to do x' and 'A ought to do y' it does not follow that 'A ought to do x and y'. Such a claim is of course a departure from familiar systems of deontic logic." (p. 134). She reports that "Van Fraassen and Williams see that such acceptance requires modification of the principle of factoring for the deontic "ought."" (p. 134, n. 13; "such acceptance" is acceptance of 'ought' implies 'can').
- **'Ought' implies 'can' (Argument 2, premise 4).** McConnell: "some took the existence of dilemmas as a counterexample to ‘ought’ implies ‘can’ (for example, Lemmon 1962 and Trigg 1971)" (§5). Marcus locates Lemmon's rejection at "p. 150" of his 1962 paper (n. 13). Marcus herself keeps the principle on one reading: "If we interpret the 'can' of the precept as "having the ability in this world to bring about," then, as indicated above, in a moral dilemma, 'ought' does imply 'can' for each of the conflicting obligations, before either one is met." (p. 134)
- **PD (Argument 1, premise 4).** "A common response to the first argument is to deny PD." (McConnell §5) "Of the principles in question, the most commonly questioned on independent grounds are the principle that ‘ought’ implies ‘can’ and PD." (§5)
- **PC.** McConnell: "Even most supporters of dilemmas acknowledge that PC is quite basic. E.J. Lemmon, for example, notes that if PC does not hold in a system of deontic logic, then all that remains are truisms and paradoxes (Lemmon 1965, p. 51)." (§5) Brink 1994 is cited for OP and D, from which PC follows: "Principles OP and D are basic; they seem to be conceptual truths (Brink 1994, section IV)." (McConnell §4)
- **The principles hold only in ideal worlds.** "A more complicated response is to grant that the crucial deontic principles hold, but only in ideal worlds." (§5, citing Holbo 2002)

## Objections

- **Marcus's reframing: dilemmas are not inconsistency.** "I WANT to argue that the existence of moral dilemmas, even where the dilemmas arise from a categorical principle or principles, need not and usually does not signify that there is some inconsistency (in a sense to be explained) in the set of principles, duties, and other moral directives under which we define our obligations either individually or socially." (Marcus 1980, p. 121) Her criterion: "Analogously we can define a set of rules as consistent if there is some possible world in which they are all obeyable in all circumstances in that world." (p. 128) McConnell reports the same point about the bare premises: "that OA and OB are both true is not itself inconsistent, even if one adds that it is not possible for the agent to do both A and B" and "the contradictory of OA is ¬OA. (See Marcus 1980 and McConnell 1978, 273.)" (§4). Structural note: the propositional check agrees on the bare premises — for `OA`, `OB`, `~CAB` against `Q & ~Q` the tool reports `INVALID` with counterexample rows `CAB=F, OA=T, OB=T, Q=T` and `…, Q=F`; the contradiction needs the added principles.
- **Which argument carries the weight.** McConnell's assessment: "there is little doubt that those in the first argument have a greater claim to being conceptually true than those in the second. (One who recognizes the salience of the first argument is Brink 1994, section V.) Perhaps the focus on the second argument is due to the impact of Bernard Williams’s influential essay (Williams 1965)." (§5)
- **The deontic-logic side.** McNamara and Van De Putte (SEP "Deontic Logic", Fall 2024, §6.4; excerpts `raw/sep-logic-deontic-fall-2024-conflicts-and-aggregation.md`) state the same pair of results for standard deontic logic (SDL): OB j and OB ¬j "are inconsistent in SDL. First, they are simply excluded by NC" (§6.4), and "(DC) in combination with (OB-C) yields triviality as soon as we endorse a minimalistic version of Kant’s law that ought implies can" (§6.4). They list "Non-aggregative deontic logics, which invalidate OB-C (aka the Aggregation rule for OB)" among conflict-tolerant logics (§6.4).

## Replies

- **Opponents need not claim every principle is conceptual.** McConnell: "They may defend ‘ought’ implies ‘can’, but hold that it is a substantive normative principle, not a conceptual truth. Or they may even deny the truth of ‘ought’ implies ‘can’ or the agglomeration principle, though not because of moral dilemmas, of course." (§5)
- **Supporters need not deny every principle.** "Defenders of dilemmas need not deny all of the pertinent principles." (§5) And the burden McConnell assigns them: "If they have no reason other than cases of putative dilemmas for denying the principles in question, then we have a mere standoff." (§5)
- **Marcus's second-order principle.** "One ought to act in such a way that, if one ought to do x and one ought to do y, then one can do both x and y. But the second-order principle is regulative." (Marcus 1980, p. 135)
- McConnell's summary of both sides' burdens and his statement that "the debate is apt to continue" (§9) are quoted on [moral dilemmas](../problems/moral-dilemmas.md).

## Variants

- **Conflict-tolerant deontic logics.** McNamara and Van De Putte date one
  line to van Fraassen: "Originating in the work on conflict-tolerant deontic logics (van Fraassen 1973, cf. Hansen 2008 and Hansen 2013), this route became most influential under the banner of Input/Output logic" (§6.1), and report "a long-ignored and challenging further puzzle for conflicting obligations, sometimes called “van Fraassen’s Puzzle” and inspired by van Fraassen 1973" (§6.4).
- **The same structure outside ethics.** Kyburg's lottery argument turns on
  an agglomeration principle for rational belief, and "Kyburg rejects agglomeration" (Sorensen, SEP "Epistemic Paradoxes", §3; `raw/sep-epistemic-paradoxes-fall-2024-lottery-and-preface.md`). Structural note: the parallel is this implant's.
- **Cases the arguments are applied to.** [Jim and the Indians](../problems/jim-and-the-indians.md)
  and [dirty hands](../problems/dirty-hands.md) are treated on their own
  pages, with the positions taken on each.

## Vocabulary

*Moral dilemma* (genuine: neither requirement overridden; see
[dilemma](../vocabulary/dilemma.md) and McConnell §2); *PC* (deontic
consistency; NC in SEP "Deontic Logic"); *PD*; *OP*, *D*; *'ought' implies
'can'* (OiC; "Kant’s law" in SEP "Deontic Logic"); *agglomeration*
(OB-C, "aggregation"; Marcus: "factoring"); *consistency of rules* in
Marcus's possible-world sense; [validity](../vocabulary/validity.md) of the
reductio. Thinkers: [Williams](../thinkers/williams.md),
[Marcus](../thinkers/marcus.md).
