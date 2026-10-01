---
type: article
about: concept
title: "The paradoxes of entailment and material implication"
description: "Classical logic makes a false proposition imply any proposition, a true one be implied by any, and a contradiction entail everything (explosion, the 'paradox of entailment'). Is that what 'implies' and 'follows' mean? Lewis 1912/1918 and strict implication, MacColl 1908, Lewis's argument for explosion and its twelfth-century discovery by William of Soissons, Anderson & Belnap's relevance logic, Tennant's Core Logic, and paraconsistent and dialetheist responses, each attributed."
tags: [problem, paradox, logic, philosophy-of-logic, conditionals]
timestamp: 2026-10-01T21:51:46Z
---

# The paradoxes of entailment and material implication

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md), filed as a [paradox](../vocabulary/paradox.md)
in the sense fixed there; the notion of [validity](../vocabulary/validity.md)
and the [classical logic](../methods/classical-logic.md) page give the
background. Primary texts: C. I. Lewis, "Implication and the Algebra of
Logic", *Mind* 21 (1912): 522–531,
[doi:10.1093/mind/XXI.84.522](https://doi.org/10.1093/mind/XXI.84.522), and
*A Survey of Symbolic Logic* (1918),
[archive.org scan](https://archive.org/details/cu31924028923451)
(excerpt: `raw/lewis-1912-1918-implication-false-proposition-implies-any.md`).
Map: Mares, [SEP Fall 2024 "Relevance Logic"](https://plato.stanford.edu/archives/fall2024/entries/logic-relevance/)
(excerpt: `raw/sep-logic-relevance-fall-2024-paradoxes-variable-sharing-lewis-argument.md`).
Admitted from Wikipedia's List of paradoxes, revision 1376699902, "Logic"
(excerpt: `raw/wikipedia-paradoxes-of-material-implication-and-explosion.md`).

## The question

The List of paradoxes entry: "Paradox of entailment: Inconsistent premises always make an argument valid."
Wikipedia's article (rev. 1360716189) defines the wider group: "The paradoxes of material implication are a group of classically true formulae involving material conditionals whose translations into natural language are intuitively false when the conditional is translated with English words such as "implies" or "if ... then ..."."
In its table, explosion, read as "If it is the case that P and it is not the case that P, then it is the case that Q"; anything follows from a contradiction.", carries the names "principle of explosion, or paradox of entailment. It is also a paradox of strict implication."

Mares (SEP 2024, preamble) lists three paradoxes of material implication,
p → (q → p), ¬p → (p → q) and (p → q) ∨ (q → r), and glosses them: "The first asserts that every proposition implies a true one; the second that a false proposition implies every proposition, and the third that for any three propositions, either the first implies the second or the second implies the third."
He lists three paradoxes of strict implication, (p & ¬p) → q,
p → (q → q) and p → (q ∨ ¬q): "The first asserts that a contradiction strictly implies every proposition; the second and third imply that every proposition strictly implies a tautology."
His summary of their status: "These so-called paradoxes are valid conclusions that follow from the definitions of material and strict implication but are seen, by some, as problematic."

So the question (structural note, this implant): do "implies", "if … then" and "follows from" mean what the
material (or strict) conditional and classical [validity](../vocabulary/validity.md) make them mean, and if not, which classical principle goes?

**Logic check (this implant, 2026-10-01; logic, not a position).**
`python3 _implant/skills/tools/logic.py check`, propositional only:

- `--premises "p & ~p" --conclusion "q"`: "VALID" / "premises are jointly inconsistent — argument is vacuously valid".
- `--premises "q" --conclusion "p -> q"` and `--premises "~p" --conclusion "p -> q"`: each "VALID".
- `--premises "p | q" "~p" --conclusion "q"`: "VALID" / "matches schema: disjunctive syllogism".
- `--premises "p" --conclusion "p | q"`: "VALID".
- `--premises "p" --conclusion "q"`: "INVALID", counterexample "p=T, q=F".

The tool computes classical two-valued truth tables and tests none of the
non-classical logics below. The last line: q does not follow from an
arbitrary premise; it follows when the premises cannot all be true.

## Why it matters

- **The meaning of "implies".** Lewis (1912, p. 522) on the two theorems: "They exhibit only, in sharp outline, the meaning of “implies” which has been incorporated into the algebra."
  Lewis (1918, p. 291): "We have already called attention to the fact that this is not the usual meaning of "implies"."
- **Inconsistent theories.** Priest, Berto & Weber (SEP 2024 "Dialetheism", §1) define the property at stake: "A logical consequence relation \(\vdash\) is explosive if, according to it, a contradiction entails everything (ex contradictione quodlibet: for all \(A\) and \(B\): \(A,\neg A \vdash B\))."
  They report the standard argument against dialetheism: "A standard argument against dialetheism is to invoke the logical principle of Explosion, in virtue of which dialetheism would entail trivialism." (§4.1; `raw/sep-dialetheism-fall-2024-priest-liar-inclosure-curry-objections.md`).
- **A motive for non-classical logics.** Wikipedia: "The paradoxes of material and strict implication have been motivations for the development of relevance logics (also called relevant logics), where the principles of logic are weakened in ways that prevent the derivation of the paradoxes as valid."
- **Related paradoxes.** The same List section says of the [paradox of free choice](paradox-of-free-choice.md)
  and [Ross's paradox](ross-paradox.md) that "Disjunction introduction poses a problem", the rule used in Lewis's argument below.
  On [Curry's paradox](currys-paradox.md), Shapiro & Beall (SEP, preamble) say it "doesn’t essentially involve the notion of negation".

## Positions taken

Structural note (this implant): grouped by which principle each keeps or drops; not ranked.

**Keep classical logic; the paradoxes are not paradoxes.**
- Wikipedia reports Anderson and Belnap's statement of the view they oppose: "Anderson and Belnap, in their seminal book Entailment on relevant logic, represented what they called the "Official" (classical-logical) view as follows:"
  The quoted view ends: "Properly understood there are no "paradoxes" of implication." (Anderson & Belnap 1975, vol. I, p. 3, as quoted by Wikipedia; not read here).
- Wikipedia's account of classical practice, citing Egré & Rott (SEP 2021): "Classical logic, with the material implication connective, remains widely used despite the paradoxes, because most users simply get used to them or ignore them, judging the paradoxes to be minor drawbacks compared with the benefits of the material conditional's "considerable virtues of simplicity" and logical strength."
- Lewis (1912, p. 522), before proposing an alternative, on the two theorems: "In themselves, they are neither mysterious sayings, nor great discoveries, nor gross absurdities."

**Strict implication: drop the material reading, keep explosion.**
- Lewis (1918, p. 291) introduces another meaning of "implies": "We shall call it the system of Strict Implication."
  He says the resulting calculus "does not contain the useless and doubtful theorems" about false and true propositions (p. 319), while it contains 3·52: "If p is impossible (not self-consistent, absurd), then p strictly implies any proposition, q." (p. 303).
- Wikipedia: "Strict implication retains the principle of explosion (p ∧ ¬p) → q, which Lewis regarded as an a priori truth, but which others still consider a paradox (a "paradox of strict implication") since an impossibility such as 2+2=5 can seem irrelevant to various facts which one may try to prove from it."
- Mares (§1) assesses it from the relevantist side: "Unfortunately, from a relevant point of view, the theory of strict implication is still irrelevant."

**Relevance (relevant) logic: require relevance, reject disjunctive syllogism.**
- Mares (preamble): "Relevance logicians claim that what is unsettling about these so-called paradoxes is that in each of them the antecedent seems irrelevant to the consequent."
- Their formal test, which Mares calls necessary but not sufficient: "The variable sharing principle says that no formula of the form \(A \rightarrow B\) can be proven in a relevance logic if \(A\) and \(B\) do not have at least one propositional variable (sometimes called a proposition letter) in common and that no inference can be shown valid if the premises and conclusion do not share at least one propositional variable."
  And its limit: "Moreover, this principle does not give us a criterion that eliminates all of the paradoxes and fallacies."
- Against explosion (§6): "Mainstream relevance logicians block this argument by rejecting disjunctive syllogism."
  Mares's bibliography calls Anderson & Belnap's *Entailment* (vol. I, Princeton UP, 1975) and vol. II (1992) "still the standard books on the subject" (not read here).
- Parry's analytic implication, as Mares (§6) presents it, restricts disjunction introduction instead (strong variable sharing).

**Keep disjunctive syllogism, restrict transitivity.**
- Mares (§6): "Tennant’s core logic, however, accepts disjunctive syllogism."
  "What is different is its treatment of one of the structural rules of proof -- it rejects the transitivity of logical consequence in its most general form."

**Paraconsistent logic, with or without dialetheism.**
- Priest, Tanaka & Weber (SEP "Paraconsistent Logic", §3.6): "If we define a consequence relation in terms of preservation of these designated values, then we have the paraconsistent logic LP (Priest 1979). In LP, ECQ is invalid." (`raw/sep-logic-paraconsistent-fall-2024-lp-and-dialetheism-distinction.md`; Priest 1979, [doi:10.1007/BF00258428](https://doi.org/10.1007/BF00258428)).
- Priest, Berto & Weber (§1) separate the two commitments: "Whereas dialetheists must embrace some paraconsistent logic or other to avoid trivialism, paraconsistent logicians need not be dialetheists: they may subscribe to a non-explosive view of entailment for other reasons."
- Horn (SEP 2024 "Contradiction", §4) on the dialetheist reply: "Dialetheists reject the charge of incoherence by noting that to accept some contradictions is not to accept them all; in particular, they seek to defuse the threat of logical armageddon or “explosion” posed by Ex Contradictione Quodlibet, the inference in (6):"

No survey figure is recorded in the sources held.

## Arguments in play

**Lewis's (independent) argument for explosion.** Mares (§6): "C.I. Lewis justified explosion by means of a little argument."
His reconstruction: from p & ¬p, conjunction elimination gives p; disjunction
introduction gives p ∨ q; conjunction elimination gives ¬p; disjunctive
syllogism gives q. Wikipedia: "This proof was published by C. I. Lewis and is named after him, though versions of it were known to medieval logicians."
(it cites Lewis & Langford, *Symbolic Logic*, 2nd ed., Dover 1959, p. 250;
not read here). Each step is checked above with `logic.py`: p ⊢ p ∨ q and
p ∨ q, ¬p ⊢ q are reported "VALID" (this implant, 2026-10-01; logic, not
a position). Responses, as Mares (§6) reports
them, differ in the step they question: "Mainstream relevance logicians block this argument by rejecting disjunctive syllogism."
Parry restricts disjunction introduction; Tennant's Core Logic rejects
general transitivity, the rule that chains the steps.

**For and against rejecting disjunctive syllogism.** Mares (§6): "The rejection of disjunctive syllogism, however, has become one of the most controversial aspects of relevance logic."
On the other side, Mares (preamble) gives the classical inference relevance logicians resist: "The moon is made of green cheese. Therefore, either it is raining in Ecuador now or it is not."

**For and against true contradictions.** Horn (§4) quotes Smiley (1993: 19): "Dialetheism stands to the classical idea of negation like special relativity to Newtonian mechanics: they agree in the familiar areas but diverge at the margins (notably the paradoxes)."
And David Lewis (1982: 434): "No truth does have and no truth could have, a true negation."
Priest, Berto & Weber (§4.1) on the explosion argument: "Since this argument assumes that Explosion is logically valid, it will carry no weight against a dialetheic paraconsistentist."

Related problems: [Curry's paradox](currys-paradox.md), [the liar paradox](liar-paradox.md),
[the barbershop paradox](barbershop-paradox.md), [the drinker paradox](drinker-paradox.md).

## Thinkers who addressed it

- **Aristotle** — Priest, Tanaka & Weber (§1.2) attribute to him "what is sometimes called the connexive principle: “it is impossible that the same thing should be necessitated by the being and by the not-being of the same thing” (Prior Analytic II 4 57b3)"; Priest, Berto & Weber (§4.1): "Aristotle held that some syllogisms with inconsistent premises are valid, whereas others are not (An. Pr. 64a 15)."
- **Dignāga** (5th c.) and **Dharmakīrti** (7th c.) — per §1.2 their logics "do not embrace ECQ" (`raw/sep-logic-paraconsistent-fall-2024-history-of-ecq.md`).
- **Boethius**, **Peter Abelard** — truth-preservation and containment accounts of consequence; **Alberic of Paris** (1130s) — a difficulty for Abelard's (§1.2).
- **William of Soissons** (12th c., Parvipontanian) — per §1.2, "who discovered in the twelfth century what we now call the C.I. Lewis (independent) argument for ECQ (see Martin 1986)".
- **The Cologne School** (late 15th c.) — "argued against ECQ by rejecting disjunctive syllogism (see Sylvan 2000)" (§1.2).
- **Hugh MacColl** (1908, *Mind* 17) — "Many philosophers, beginning with Hugh MacColl (1908), have claimed that these theses are counterintuitive." (Mares, preamble).
- **C. I. Lewis** (1912; 1918; *Symbolic Logic* with C. H. Langford, cited by Wikipedia in the Dover 2nd ed. 1959, p. 250) — named the theorems ("This is the famous — or notorious — theorem: "A false proposition implies any proposition"." 1918, p. 229), built Strict Implication, and published the argument for explosion.
- **Alan Ross Anderson & Nuel Belnap** (*Entailment*, vol. I, 1975; vol. II with J. M. Dunn, 1992) — relevance logic R and E (Mares §§4–5).
- **William Parry** — analytic implication (Mares §6).
- **Richard Routley** (later Sylvan) and **Robert K. Meyer** — the Routley–Meyer semantics for relevant implication (Mares §1).
- **Graham Priest** ([page](../thinkers/priest.md); 1979, LP) — a paraconsistent logic in which ECQ is invalid; dialetheism (SEP "Paraconsistent Logic" §3.6; "Dialetheism" §1).
- **David Lewis** (1982, "Logic for equivocators") — against true contradictions, as quoted by Horn (§4).
- **Neil Tennant** — Core Logic, keeping disjunctive syllogism (Mares §6).

## Framings and reframings

- **Not paradoxes but a definition.** Lewis (1912, p. 522) treats the theorems as exhibiting a meaning; the "Official" view in Anderson & Belnap's report says "Properly understood there are no "paradoxes" of implication."
- **A failure of relevance.** The relevantist reframing (Mares, preamble), which moves the problem from truth conditions to topic, made formal as variable sharing.
- **A history, not a fixed point.** Priest, Tanaka & Weber (§1.2): "It is now standard to view ex contradictione quodlibet as valid."
  "It was towards the end of the nineteenth century, when the study of logic achieved mathematical articulation, that an explosive logical theory became the standard."
  "In antiquity, however, no one seems to have endorsed the validity of ECQ."
  Priest, Berto & Weber (§4.1): "The principle of Explosion had a certain tenure at places and times in Medieval logic, but it became well-established mainly with the Fregean and post-Fregean development of what is now called classical logic."
- **Two questions, separated.** Whether consequence is explosive (paraconsistency) and whether any contradiction is true (dialetheism) are distinct questions in Priest, Berto & Weber (§1).
- **Structural note (this implant).** Wikipedia's List entry speaks of "inconsistent premises"; the logic check above shows the classical verdict depends on the premises being jointly unsatisfiable, not on their topic — which is the feature the relevance framing targets.

## Vocabulary

- [Paradox](../vocabulary/paradox.md); [Validity](../vocabulary/validity.md); [Argument](../vocabulary/argument.md); [Classical logic](../methods/classical-logic.md).
- Material and strict implication, entailment, explosion (ex falso / ex contradictione quodlibet, ECQ), disjunctive syllogism, disjunction introduction, variable sharing, relevance logic, paraconsistent, dialetheism, trivialism — open work in [vocabulary](../vocabulary/index.md).
