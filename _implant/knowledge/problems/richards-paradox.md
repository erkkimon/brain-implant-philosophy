---
type: article
about: concept
title: "Richard's paradox"
description: "The real number built by changing the nth digit of the nth finitely definable real is defined in finitely many words, yet differs from every such real — the paradox Jules Richard published in 1905; his own vicious-circle diagnosis, taken up by Poincaré (1906) and Russell (1908), Peano's 'linguistics, not mathematics', Borel, Brouwer, Weyl, Ramsey's Group B, and Gödel's 1931 analogy."
tags: [problem, paradox, logic, self-reference, definability, diagonalisation, philosophy-of-mathematics]
timestamp: 2026-10-01T22:52:16Z
---

# Richard's paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Primary text: Jules Richard, "Les principes des mathématique et le problème
des ensembles" (title spelled as in Cantini & Bruni's bibliography),
*Revue générale des sciences pures et appliquées* 16 (1905), p. 541; also
*Acta Mathematica* 30 (1906), pp. 295–296, titled *Lettre: A Monsieur le
rédacteur de la Revue Générale des Sciences* in the DOI record,
[doi:10.1007/BF02418575](https://doi.org/10.1007/BF02418575); English in van
Heijenoort (ed.), *From Frege to Gödel* (1967), pp. 142–144 (data per Cantini
& Bruni's bibliography and the DOI record; the letter itself not read here).
Maps: Cantini & Bruni, [SEP Fall 2024 "Paradoxes and Contemporary Logic"](https://plato.stanford.edu/archives/fall2024/entries/paradoxes-contemporary-logic/)
§§2.5–5.3 (excerpt: `raw/sep-paradoxes-contemporary-logic-fall-2024-richards-paradox.md`);
Bolander, [SEP Fall 2024 "Self-Reference and Paradox"](https://plato.stanford.edu/archives/fall2024/entries/self-reference/)
§§1.1, 1.4, 2 (excerpts: `raw/sep-self-reference-fall-2024-richards-paradox.md`,
`raw/sep-self-reference-fall-2024-berry-paradox.md`).
Admitted from Wikipedia's [List of paradoxes, revision 1376699902](https://en.wikipedia.org/w/index.php?title=List_of_paradoxes&oldid=1376699902),
"Logic", which gives: "Richard's paradox: We appear to be able to use simple English to define a decimal expansion in a way that is self-contradictory."
(excerpt: `raw/wikipedia-list-of-paradoxes-richards-paradox-entry.md`).

## The question

Cantini & Bruni (§2.5) report the 1905 construction: "Richard noticed that the set \(E\) of reals that can be defined by finitely many French words is denumerable and hence one can assume to have an enumeration \(u_1, u_2,\ldots\) of all those numbers."
A real N is then defined whose nth digit differs from the nth digit of the
nth number (Richard's rule as they report it: p + 1 for a digit p other than
8 and 9, otherwise 1). "By construction, \(N\) will not occur in \(u_1, u_2,\ldots\). On the other hand, if we consider that \(N\) is defined by means of a finite collection of letters, this must occur in \(u_1, u_2,\ldots\)." (§2.5).
Russell's 1908 statement ([doi:10.2307/2369948](https://doi.org/10.2307/2369948),
p. 223; excerpt `raw/russell-1908-theory-of-types-richards-paradox.md`):
"Consider all decimals that can be defined by means of a finite number of words; let E be the class of such decimals."
and, after the diagonal step, "Nevertheless we have defined N in a finite number of words, and therefore N ought to be a member of E. Thus N both is and is not a member of E."
Bolander (§1.1) gives an English version: "the real number whose \(n\)th decimal place is 1 whenever the \(n\)th decimal place of the number denoted by the \(n\)th phrase is 0; otherwise 0."

The question is whether N is defined at all, what "definable" means and in
which language, and whether the totality E may be used in defining one of
its own members.

**Logic check (this implant, 2026-10-02; logic, not a position).** Let `f` =
*N is defined by finitely many words*, `m` = *N is a member of E*. By the
definition of E, `f -> m`; by the diagonal construction, `~m`.
`logic.py check --premises "f -> m" "~m" --conclusion "~f"` outputs "VALID"
and "matches schema: modus tollens"; adding the premise `f` with conclusion
`m` outputs "premises are jointly inconsistent — argument is vacuously valid".
With conclusion `f` it outputs "INVALID" (counterexample "f=F, m=F"). The tool
does not say which premise a response gives up; the positions below differ on
that. Terms: [paradox](../vocabulary/paradox.md), [validity](../vocabulary/validity.md).

## Why it matters

- **Definability and the continuum.** Cantini & Bruni (§2) list among the early contradictions those of "definability and the arithmetical (or atomistic) continuum (Richard, König, Bernstein, Berry, Grelling)."
- **The vicious-circle line.** Per Cantini & Bruni (§2.5), Richard's own diagnosis "soon became the basis of Poincaré’s solution, and eventually also Russell’s"; Russell 1908 (p. 223) lists it as contradiction (6) of seven.
- **Semantic versus logical paradoxes.** Peano's remark, per Cantini & Bruni (§3.3.1), "opens up the distinction between set-theoretic or mathematical antinomies and semantical antinomies"; Bolander (§1.1) lists Richard's paradox among the semantic paradoxes.
- **Diagonalisation.** Bolander (§1.1): "The particular construction employed in this paradox is called diagonalisation."; of Cantor's theorem (§1.2): "The theorem is proved by a form of diagonalisation, the same idea underlying Richard’s paradox."
- **Incompleteness and inconsistency proofs.** Gödel 1931, Finsler 1926, Church 1934 and Kleene–Rosser 1934 used or compared it; see Framings.

## Positions taken

Not ranked; each is reported with the source that records it.

- **Vicious circle: the definition of N is illusory (Richard 1905).** Cantini & Bruni (§2.5): "He pointed out that the definition of the number \(N\) refers to the totality of definable reals, to which \(N\) itself belong; but no object should be definable in terms of a collection containing it. So it appears that the definition is viciously circular, and that makes the definition illusory."
- **Predicative definitions only (Poincaré 1906).** Poincaré, "Les mathématiques et la logique", *Revue de métaphysique et de morale* 14 (1906), §IX "La vraie Solution" (excerpt: `raw/poincare-1906-mathematiques-et-logique-antinomie-richard.md`), says the solution is contained in Richard's letter: "Il me semble que la solution est contenue dans une lettre de M. Richard dont j’ai parlé plus haut et qu’on trouvera dans la Revue Générale des Sciences du 30 juin 1905."
  E is the set of numbers definable in finitely many words "sans introduire la notion de l’ensemble E lui-même"; since N was defined "en nous appuyant sur la notion de l’ensemble E", "Et voilà pourquoi N ne fait pas partie de E." He concludes: "Ainsi les définitions qui doivent être regardées comme non prédicatives sont celles qui contiennent un cercle vicieux." (paraphrase in English by this page; no translation quoted). Cantini & Bruni (§3.1) say Poincaré "thus somewhat extended Richard’s diagnosis", and later restated the paradox (1909, 1910) as "there is no definable enumeration of definable reals".
- **"All definitions" is illegitimate (Russell 1908).** "This is solved, like (5), by remarking that "all definitions" is an illegitimate notion. Thus the number E is not defined in a finite number of words, being in fact not defined at all." (p. 225). The general rule: "Whatever involves all of a collection must not be one of the collection" (p. 225).
- **Linguistics, not mathematics (Peano 1906).** Per Cantini & Bruni (§3.3.1), Peano held that "Richard’s example pertains to linguistics, not to mathematics"; "For instance, there is no precise criterion for deciding whether a given expression of the natural language represents a rule uniquely defining a number." His formal treatment, as they report it, ends: "The conclusion is that no such a real can exist and Richard’s definition is defective in the same way that “the greatest prime number” is."
- **Denumerable but not effectively enumerable (Borel 1908).** Per Cantini & Bruni (§3.3.1): "The Richard paradox is then solved by observing that Richard’s set \(E\) is certainly denumerable, because one can only determine at most a denumerable set of reals by finite means. Yet \(E\) is not effectively enumerable"
- **Denumerably unfinished sets (Brouwer 1907).** "A positive by-product of Richard’s paradox in Brouwer’s work (1907, p. 149) is the notion of denumerably unfinished set" (Cantini & Bruni §3.3.1).
- **Explicit definitions are denumerable (Weyl 1910).** "According to Weyl, Richard’s paradox teaches us the following distinction: on the one hand, we are able to characterize only denumerably many subsets of a given set by means of explicit definitions; but, on the other hand, new objects and (possibly uncountable) sets can be introduced by applying the remaining set theoretic operations, like power set or union." (§3.3.2).
- **Group B, orders of meaning (Ramsey 1926).** Ramsey, "The Foundations of Mathematics" ([doi:10.1112/plms/s2-25.1.338](https://doi.org/10.1112/plms/s2-25.1.338); 1931 reprint, excerpt `raw/ramsey-1926-foundations-of-mathematics-richards-contradiction.md`) lists "Richard's Contradiction" in Group B: "But the contradictions of Group B are not purely logical, and cannot be stated in logical terms alone ; for they all contain some reference to thought, language, or symbolism, which are not formal but empirical terms." (p. 20).
  His solution (p. 48): "All these result from the obvious ambiguity of ‘ naming ’ and ‘ defining ’." and "The sense in which it means must be made precise by fixing its order ; the name or definition involving all such names or definitions will be of a higher order, and this removes the contradiction."

**Cases for and against.** Recorded objections, each with its owner:
- Ramsey (p. 21) against Peano's dismissal: "For instance, Peano decided that " Exemplo de Richard non pertine ad Mathematica, sed ad linguistica and therefore dismissed it. But such an attitude is not completely satisfactory."; for "the mathematician dismisses them by saying that the fault must lie in the linguistic elements, but the linguistician may equally well dismiss them for the opposite reason, and the contradictions will never be solved."
- Chwistek against the type-theoretic answer, per Cantini & Bruni (§4.2): "His position in 1921 was that Principia Mathematica were not enough to avoid Richard’s classical antinomy."
- On Zermelo's view that separation blocks it, Cantini & Bruni (§3.3.2) assess: "But this is not the case, because Zermelo’s notion of definite property (definite Eigenschaft) is given informally and is ultimately vague."
- On the state of the question around 1930, Cantini & Bruni (§5.2) assess that "the problem of finding a formal solution to the semantical paradoxes, such as the Liar and the Richard paradox, remained essentially open."
The sources read record no published objection to Poincaré's, Borel's,
Brouwer's or Weyl's treatment of this paradox; none is recorded here. No
survey figure is recorded.

## Arguments in play

(none as separate argument pages yet). Related problems:
[the Berry paradox](berry-paradox.md), listed with it by Russell 1908 and
Ramsey 1926 and by Bolander (§2) as a paradox of definability;
[Russell's paradox](russells-paradox.md), which Bolander (§1.4) fits to the
same Inclosure Schema; [the liar paradox](liar-paradox.md), named beside it by
Gödel 1931; [the Grelling–Nelson paradox](grelling-nelson-paradox.md), in
Ramsey's Group B; [the Kleene–Rosser paradox](kleene-rosser-paradox.md),
which the Wikipedia list describes as "By formulating an equivalent to Richard's paradox, untyped lambda calculus is shown to be inconsistent."

## Thinkers who addressed it

- **Jules Richard** (1905) — "a mathematician of a Lyceé in Dijon" (Cantini & Bruni §2.5).
- **Henri Poincaré** (1906 §§VII, IX; 1909, 1910) — see Positions.
- **Giuseppe Peano** (1906, "Additione a Super Theorema de Cantor-Bernstein", per Cantini & Bruni §3.3.1; not read).
- **Bertrand Russell** (1908, pp. 223, 225).
- **L. E. J. Brouwer** (1907), **Émile Borel** (1908), **Hermann Weyl** (1910), **Ernst Zermelo** — as reported by Cantini & Bruni (§§3.3.1–3.3.2); not read.
- **Leon Chwistek** (1921) — per Cantini & Bruni (§4.2).
- **Frank P. Ramsey** (1926) — Group B; orders of meaning.
- **Paul Finsler** (1926), **Kurt Gödel** (1931), **Alonzo Church** ("The Richard paradox", *American Mathematical Monthly* 41, 1934, pp. 356–361, per Cantini & Bruni's bibliography; not read), **Stephen Kleene** and **J. Barkley Rosser** (1934–1935) — see Framings.
- **Graham Priest** (1994) — Inclosure Schema, per Bolander (§1.4); see [Priest](../thinkers/priest.md).

## Framings and reframings

- **Gödel's analogy (1931).** Gödel, *Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I* ([doi:10.1007/BF01700692](https://doi.org/10.1007/BF01700692)), §1, in Hirzel's English translation (excerpt: `raw/goedel-1931-formal-unentscheidbare-saetze-richard-antinomie.md`): "The analogy of this conclusion with the Richard-antinomy leaps to the eye; there is also a close kinship with the liar-antinomy, because our undecidable theorem Rq (q) states that q is in K, i.e. according to (1) that Rq (q) is not provable."
  Cantini & Bruni (§5.1) read this as Gödel relating "his construction of formally undecidable sentences to epistemological paradoxes".
- **Before Gödel: Finsler.** "Finsler 1926 applies Richard’s paradox in order to produce metamathematical results, in particular ‘formally undecidable propositions’. However, Finsler’s arguments are not conclusive and cannot be considered a proper anticipation of the Gödel incompleteness theorems" (Cantini & Bruni's assessment, §4.1).
- **From paradox to inconsistency proof.** Cantini & Bruni (§5.3): Kleene and Rosser "(essentially) proved a version of the Richard paradox (both systems can provably enumerate their own provably total definable number theoretic functions)", after Church "used the Richard paradox to prove a kind of incompleteness theorem".
- **One schema for many paradoxes (Priest 1994).** Bolander (§1.4) fits Richard's paradox to the Inclosure Schema with "\(P(x)\) is the predicate “\(x\) is a real definable by a phrase in English.”" and a diagonal function δ: "Letting \(y\) equal \(w\) we thus get \(\delta(w) \not\in w\). However, at the same time \(\delta(w)\) is definable by a phrase in English, so \(\delta(w) \in w\), and we have a contradiction. This contradiction is Richard’s paradox."
  He adds: "Whether the Inclosure Schema can in full generality count as a necessary and sufficient condition for self-referential paradoxicality is however disputable (Slater, 2002; Abad, 2008; Badici, 2008; Zhong, 2012, and others), hence not all authors agree on the principle of uniform solution either."
- **A defect in the concept (Bolander's assessment).** Bolander (§2): "In case of the semantic paradoxes, it seems that it is our understanding of fundamental semantic concepts such as truth (in the liar paradox and Grelling’s paradox) and definability (in Berry’s and Richard’s paradoxes) that are deficient."

## Vocabulary

- [Paradox](../vocabulary/paradox.md); [Validity](../vocabulary/validity.md);
  [Classical logic](../methods/classical-logic.md), in which the logic check
  above is run.
- Definability, diagonalisation, denumerable, effectively enumerable,
  impredicative / non-predicative definition, vicious-circle principle,
  Inclosure Schema — open work in [vocabulary](../vocabulary/index.md).
