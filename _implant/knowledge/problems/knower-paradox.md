---
type: article
about: concept
title: "The knower paradox"
description: "'This sentence is not known' seems provably true, and a proof seems to give knowledge — so it is known, and false. Kaplan and Montague's 'A Paradox Regained' (1960) and Montague's theorem (1963) on a knowledge predicate; the responses recorded by the SEP and Wikipedia: a hierarchy of knowledge predicates (Anderson 1983), doubts about proof-yields-knowledge or about knowing factivity (Maitzen 1998, Cross 2001), restricted or operator treatments, rejecting excluded middle or accepting the contradiction (Priest 1991, Beall 2000)."
tags: [problem, paradox, logic, self-reference, epistemology, knowledge]
timestamp: 2026-10-01T22:52:16Z
---

# The knower paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Primary text: Kaplan & Montague, "A paradox regained", *Notre Dame Journal of
Formal Logic* 1(3), 1960, pp. 79–90 per the SEP, [doi:10.1305/ndjfl/1093956549](https://doi.org/10.1305/ndjfl/1093956549)
— not read; reported only through the encyclopedias below (record:
`raw/knower-paradox-bibliographic-records.md`).
Maps: Sorensen, [SEP Fall 2024 "Epistemic Paradoxes"](https://plato.stanford.edu/archives/fall2024/entries/epistemic-paradoxes/)
§5.1 (excerpt: `raw/sep-epistemic-paradoxes-fall-2024-knower.md`);
Bolander, [SEP Fall 2024 "Self-Reference and Paradox"](https://plato.stanford.edu/archives/fall2024/entries/self-reference/)
§§1.3, 2.3, 3.1 (excerpt: `raw/sep-self-reference-fall-2024-knower-and-montague-theorem.md`);
Cantini & Bruni, [SEP Fall 2024 "Paradoxes and Contemporary Logic"](https://plato.stanford.edu/archives/fall2024/entries/paradoxes-contemporary-logic/)
§§6.4–6.5 (excerpt: `raw/sep-paradoxes-contemporary-logic-fall-2024-knower.md`);
Brogaard & Salerno, [SEP Fall 2024 "Fitch's Paradox of Knowability"](https://plato.stanford.edu/archives/fall2024/entries/fitch-paradox/)
§3.5 (excerpt: `raw/sep-fitch-paradox-fall-2024-knower-version.md`).
Admitted from Wikipedia's [List of paradoxes, revision 1376699902](https://en.wikipedia.org/w/index.php?title=List_of_paradoxes&oldid=1376699902),
"Logic", which gives it as "This sentence is not known."; the responses map
uses [Wikipedia "Knower paradox", revision 1327062460](https://en.wikipedia.org/w/index.php?title=Knower_paradox&oldid=1327062460)
(excerpt: `raw/wikipedia-knower-paradox-rev-1327062460-and-list-entry.md`).

## The question

Bolander (SEP 2024, §1.3) uses "the sentence “This sentence is not known by anyone.”" (KS). Step one: "Assume to obtain a contradiction that \(KS\) is not true. Then what \(KS\) expresses cannot be the case, that is, \(KS\) must be known by someone. Since everything known is true (this is part of the definition of the concept of knowledge), \(KS\) is true, contradicting our assumption."
Step two: that reasoning "should be available to any agent (person) with sufficient reasoning capabilities." So KS comes to be known; "However, if \(KS\) is known by someone, then what it expresses is not the case, and thus it cannot be true. This is a contradiction, and thus we have a paradox."

Wikipedia (rev. 1327062460) names the two principles: "(KF): If the sentence ' P ' is known, then P" and "(PK): If the sentence ' P ' has been proved, then ' P ' is known", applied to "(K): (K) is not known". Sorensen (SEP 2024, §5.1) states the premise as "Believing a proposition by seeing it to be proved is a sufficient for knowledge of it, so someone must know (K)."

The question is which of these gives way: factivity, proof-yields-knowledge,
the self-referential sentence, or the logic that chains them. The term
contracts are [paradox](../vocabulary/paradox.md),
[knowledge](../vocabulary/knowledge.md) and [validity](../vocabulary/validity.md).

**Logic check (this implant, 2026-10-02; logic, not a position).** Let `n` =
*(K) is known*, `t` = *(K) is true*, `p` = *(K) has been proved*. KF gives
`n -> t`; what (K) says gives `t -> ~n`; PK gives `p -> n`.
`logic.py check --premises "n -> t" "t -> ~n" --conclusion "~n"` outputs
"VALID" — step one. With `p -> n` added and conclusion `~p` it outputs "VALID".
With `p` also added as a premise and conclusion `n` it outputs "VALID" and
"premises are jointly inconsistent — argument is vacuously valid". Without
`p -> n` and `p`, conclusion `n` outputs "INVALID" (counterexamples "n=F, t=T"
and "n=F, t=F"). The tool treats `p` as a free premise; whether deriving `~n`
counts as (K) being proved, and so known, is what the positions below differ on.

## Why it matters

- **Formal theories of knowledge.** Bolander (§2.3): "The epistemic paradoxes constitute a threat to the construction of formal theories of knowledge, as the paradoxes become formalisable in many such theories." See Montague's theorem under Framings.
- **Negative results.** Cantini & Bruni (§6.5) report that techniques from incompleteness and indefinability "have yielded negative results (Kaplan and Montague 1960, Montague 1963, Thomason 1980) and established an interesting link with the surprise test paradox."
- **Bearing on knowability.** Brogaard & Salerno (SEP 2024, §3.5) report Beall (2000) using the knower against Fitch's proof; see [Fitch's paradox of knowability](fitchs-paradox-of-knowability.md).
- **Rank in its family (Bolander's assessment).** "The most well-know epistemic paradox is the paradox of the knower (Kaplan & Montague, 1960; Montague, 1963)." (§1.3; "well-know" as printed).

## Positions taken

Not ranked; each is reported with the source that records it. Wikipedia
(rev. 1327062460) sorts them: "absurdity can only be avoided either by rejecting one of the two principles of knowledge (KF) and (PK) or by rejecting classical logic (which validates the reasoning from (KF) and (PK) to absurdity)."

- **A hierarchy of knowledge predicates (Anderson 1983).** Per Wikipedia: "One approach takes its inspiration from the hierarchy of truth predicates familiar from Alfred Tarski's work on the Liar paradox and constructs a similar hierarchy of knowledge predicates." — citing Anderson, *J. Phil.* 80, [doi:10.2307/2026335](https://doi.org/10.2307/2026335) (not read). Bolander (§3.1) describes the typed route: "In the case of the epistemic paradoxes, a similar stratification could be obtained by making an explicit distinction between first-order knowledge (knowledge about the external world), second-order knowledge (knowledge about first-order knowledge), third-order knowledge (knowledge about second-order knowledge), and so on."
- **Doubt about PK, or about knowing KF (Maitzen 1998; Cross 2001).** Per Wikipedia: "Another approach upholds a single knowledge predicate but takes the paradox to call into doubt either the unrestricted validity of (PK) or at least knowledge of (KF)." — citing Maitzen, *Synthese* 114, [doi:10.1023/a:1005064624642](https://doi.org/10.1023/a:1005064624642), for PK, and Cross, *Mind* 110, [doi:10.1093/mind/110.438.319](https://doi.org/10.1093/mind/110.438.319), for KF (neither read). Sorensen (§5.1), discussing the skeptic, holds: "Proof does not always yield knowledge." — "Consider a student who correctly guesses that a step in his proof is valid. The student does not know the conclusion but did prove the theorem."
- **Weaker or restricted principles.** Bolander (§2.3) records the reply "that even axiom schemas A1–A4 are too strong, and should be weakened further", and restriction to a subset of sentences: "Revières and Levesque (1988) showed that the principles stay consistent when only instantiated over the so-called regular sentences, and this result was later generalised to the more inclusive class of so-called RPQ sentences (Morreau and Kraus, 1998)."
- **Knowledge as an operator.** Bolander (§2.3): "In the semantic treatment of knowledge, one generally avoids problems of self-reference, and thus inconsistency, but it is at the expense of the expressive power of the formalism"; the stratification "actually comes for free in the semantic treatment of knowledge, where knowledge is formalised as a modal operator." (§3.1).
- **Provability logic (Egré 2005; De Vos, Kooi & Verbrugge 2018).** Cantini & Bruni (§6.4) report that they "applied provability logic to solving the Knower’s paradox." Egré, *JoLLI* 14, [doi:10.1007/s10849-004-6406-y](https://doi.org/10.1007/s10849-004-6406-y) (not read).
- **Rejecting excluded middle (Morgenstern 1986).** Per Wikipedia: "One approach rejects the law of excluded middle and consequently reductio ad absurdum."
- **Accepting the contradiction (Priest 1991; Beall 2000).** Per Wikipedia: "Another approach upholds reductio ad absurdum and thus accepts the conclusion that (K) is both not known and known, thereby rejecting the law of non-contradiction." — citing [Priest](../thinkers/priest.md), *NDJFL* 32, [doi:10.1305/ndjfl/1093635745](https://doi.org/10.1305/ndjfl/1093635745) (not read). Brogaard & Salerno (§3.5): "Beall suggests that the knower gives us some independent evidence for thinking \(Kp \wedge \neg Kp\), for some \(p\), that the full description of human knowledge has the interesting feature of being inconsistent. With a paraconsistent logic, one may accept this without triviality."

**Cases for and against.** Against restriction, Bolander (§2.3): "It is however not at all clear that we can sensibly point out exactly which sentences are normal and which are pathological." Against the operator route, the cost he names is expressive power (above). On the skeptic's options Sorensen (§5.1): "The skeptic could hope to solve (K-0) by denying that anything is known. This remedy does not cure (K). If nothing is known then (K) is true." On Beall's line, the SEP authors list what it turns on, including "(2) the adequacy of the proposed resolutions to the knower paradox," (§3.5). The sources read record no objection to the hierarchy, provability-logic or excluded-middle responses; none is recorded here. No survey figure is recorded.

## Arguments in play

(none as separate argument pages yet). Related problems:
[the liar paradox](liar-paradox.md) — Bolander (§1.3) calls KS "obviously quite similar to the liar sentence, except the central concept involved is knowledge rather than truth.";
[the surprise examination paradox](surprise-examination-paradox.md), whose
announcement Kaplan and Montague read as self-referential (Sorensen §5.1);
[Fitch's paradox of knowability](fitchs-paradox-of-knowability.md), which
Brogaard & Salerno (§3.5) keep apart: "The independent evidence lies in the paradox of the knower (not to be mistaken with the paradox of knowability)."
[Moore's paradox](moores-paradox.md) and the
[lottery and preface paradoxes](lottery-and-preface-paradoxes.md) are other
epistemic paradoxes in Sorensen's entry.

## Thinkers who addressed it

- **Thomas Bradwardine** (14th c.) — per Wikipedia: "A version of the paradox occurs already in chapter 9 of Thomas Bradwardine’s Insolubilia." (citing Read's 2010 edition; not read).
- **David Kaplan & Richard Montague** (1960) — "A Paradox Regained" (§5.1; Bolander §1.3).
- **Richard Montague** (1963) — "Syntactical treatment of modality, with corollaries on reflection principles and finite axiomatizability", *Acta Philosophica Fennica* 16: 153–167 (as printed in the SEP; no DOI found; not read).
- **C. Anthony Anderson** (1983) — hierarchy of knowledge predicates (per Wikipedia).
- **Steven Maitzen** (1998) and **Charles B. Cross** (2001) — PK and knowledge of KF (per Wikipedia). Uzquiano, "The Paradox of the Knower without Epistemic Closure?", *Mind* 113 (2004), [doi:10.1093/mind/113.449.95](https://doi.org/10.1093/mind/113.449.95), answers Cross by title; not read, and not cited by the sources read.
- **Leora Morgenstern** (1986) — excluded middle (per Wikipedia).
- **Graham Priest** (1991) and **J. C. Beall** (2000, [doi:10.1080/00048400012349521](https://doi.org/10.1080/00048400012349521)) — accepting the contradiction.
- **Richmond Thomason** (1980) — negative results (Cantini & Bruni §6.5).
- **Paul Egré** (2005); **De Vos, Kooi & Verbrugge** (2018) — provability logic (§6.4).
- **Roy Sorensen** and **Thomas Bolander** — SEP authors of the formulations above.

## Framings and reframings

- **From the surprise test (Kaplan & Montague 1960).** Sorensen (§5.1): "David Kaplan and Richard Montague (1960) think the announcement by the teacher in our surprise exam example is equivalent to the self-referential" sentence (K-3); "Kaplan and Montague note that the number of alternative test dates can be increased indefinitely. Shockingly, they claim the number of alternatives can be reduced to zero! The announcement is then equivalent to" "(K-0) This sentence is known to be false."
  Sorensen's derivation: "If (K-0) is true then it known to be false. Whatever is known to be false, is false. Since no proposition can be both true and false, we have proven that (K-0) is false. Given that proof produces knowledge, (K-0) is known to be false. But wait! That is exactly what (K-0) says – so (K-0) must be true."
- **K~p or ~Kp (Sorensen's assessment).** "The (K-0) argument bears a suspicious resemblance to the liar paradox." He reports that "Subsequent commentators sloppily switch the negation sign in the formal presentations of the reasoning" and "Ironically, this garbled transmission results in a cleaner variation of the knower:" "(K) No one knows this very sentence." The Fitch entry's version is "k is unknown", with the premise "granting that a proven falsehood is known to be false" (§3.5).
- **From paradox to theorem (Montague 1963).** Bolander (§2.3) sets four principles for a knowability predicate K — "First of all, all knowable sentences must be true." (A1); "Of course this principle must itself be knowable" (A2); "In addition, all theorems of first-order arithmetic ought to be knowable" (A3); "Furthermore, knowability must be closed under logical consequences" (A4) — and states Montague's theorem: "Any formal theory extending first-order arithmetic and containing axiom schemas A1–A4 is inconsistent." His reading: "Montague’s theorem shows that in the setting of first-order arithmetic we cannot have a theory of knowledge or knowability satisfying even the basic principles A1–A4."
- **A generalisation of Tarski.** Bolander (§2.3): "Montague’s theorem is a generalisation of Tarski’s theorem." (see [Tarski](../thinkers/tarski.md)); A1–A4 are a weakening of the T-schema. In §2.4 he lists it beside Tarski's theorem and a set-theoretic result as limits on the properties one may consistently assume "and a knowledge predicate to have (Montague’s theorem)."

## Vocabulary

- [Paradox](../vocabulary/paradox.md); [Knowledge](../vocabulary/knowledge.md);
  [Validity](../vocabulary/validity.md); [Classical logic](../methods/classical-logic.md),
  in which the logic check above is run.
- Factivity, knowability predicate, diagonal lemma, syntactic vs semantic
  (operator) treatment of knowledge, regular sentences, provability logic,
  paraconsistent logic — open work in [vocabulary](../vocabulary/index.md).
