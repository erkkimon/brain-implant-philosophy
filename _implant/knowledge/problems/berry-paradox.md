---
type: article
about: concept
title: "The Berry paradox"
description: "'The least integer not nameable in fewer than nineteen syllables' is itself named in eighteen syllables — the paradox Russell published (1906, 1908) and credited to G. G. Berry of the Bodleian; Russell's solution by assigned classes of names and the vicious-circle principle, Ramsey's 'notions of meaning', and its reuse as a proof of incompleteness by Vopěnka (1966), Chaitin (program-size complexity) and Boolos (1989)."
tags: [problem, paradox, logic, self-reference, definability, philosophy-of-mathematics]
timestamp: 2026-10-08T19:52:29Z
---

# The Berry paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Primary text: Russell, "Mathematical Logic as Based on the Theory of Types",
*American Journal of Mathematics* 30(3), 1908, pp. 222–262,
[doi:10.2307/2369948](https://doi.org/10.2307/2369948), open copy
[archive.org/details/jstor-2369948](https://archive.org/details/jstor-2369948)
(excerpt: `raw/russell-1908-theory-of-types-berry-paradox.md`).
Maps: Bolander, [SEP Fall 2024 "Self-Reference and Paradox"](https://plato.stanford.edu/archives/fall2024/entries/self-reference/)
§§1.1, 1.6, 2 (excerpt: `raw/sep-self-reference-fall-2024-berry-paradox.md`);
Cantini & Bruni, [SEP Fall 2024 "Paradoxes and Contemporary Logic"](https://plato.stanford.edu/archives/fall2024/entries/paradoxes-contemporary-logic/)
§§2, 3.1, 4.2, 6.4 (excerpt: `raw/sep-paradoxes-contemporary-logic-fall-2024-berry-paradox.md`).
Admitted from Wikipedia's [List of paradoxes, revision 1376699902](https://en.wikipedia.org/w/index.php?title=List_of_paradoxes&oldid=1376699902),
"Logic" (excerpt: `raw/wikipedia-list-of-paradoxes-berry-paradox-entry.md`).

## The question

Russell 1908 (§I, p. 223) states it as the fourth of his contradictions: "Hence "the least integer not nameable in fewer than nineteen syllables" must denote a definite integer; in fact, it denotes 111,777." But that phrase "is itself a name consisting of eighteen syllables; hence the least integer not nameable in fewer than nineteen syllables can be named in eighteen syllables, which is a contradiction."
The premise that some such integer exists: "only a finite number of names
can be made with a given finite number of syllables" (p. 223). Footnote:
"This contradiction was suggested to me by Mr. G. G. Berry of the Bodleian
Library." (p. 223).

Other wordings on record: Bolander's "the least number that cannot be
referred to by a description containing less than 100 symbols." (SEP 2024,
§1.1), a description "containing 93 symbols"; Cantini & Bruni's with "less
than 18 syllables" (SEP 2021/2024, §3.1); Chaitin's "the first positive
integer that cannot be specified in less than a billion words" (1994, p. 3);
the Wikipedia list's "the first number not nameable in under ten words",
which it says "appears to name it in nine words" (rev. 1376699902).
*Count (this implant, 2026-10-01; arithmetic, not a position):* the, first,
number, not, nameable, in, under, ten, words — 9 words, 9 < 10.

The question is what goes wrong: whether the phrase names a number, what
"nameable" or "definable" means, and in which language the naming happens.
The term contracts are [paradox](../vocabulary/paradox.md) and
[validity](../vocabulary/validity.md).

**Logic check (this implant, 2026-10-01; logic, not a position).** Let `d` =
*the phrase denotes a number*, `n` = *that number is nameable in fewer than
nineteen syllables*. The phrase is short, so `d -> n`; by what it says,
`d -> ~n`. `logic.py check --premises "d -> n" "d -> ~n" --conclusion "~d"`
outputs "VALID"; with the added premise `d` and conclusion `n` it outputs
"premises are jointly inconsistent — argument is vacuously valid". With
conclusion `d` it outputs "INVALID" (counterexamples "d=F, n=T" and
"d=F, n=F"). The tool does not decide which conditional, or which reading
of "nameable", a response gives up; the positions below differ on that.

## Why it matters

- **Finite numbers only.** Cantini & Bruni say the paradox "has the merit of not going beyond the domain of finite numbers" (§3.1); Boolos (1989, p. 388) quotes Russell to the same effect from *Essays in Analysis* (1973), p. 210.
- **A paradox of definability.** Cantini & Bruni list Berry among contradictions of "definability and the arithmetical (or atomistic) continuum (Richard, König, Bernstein, Berry, Grelling)." (§2). Bolander (§1.1) files it with the liar as semantic, and judges (§2): "In case of the semantic paradoxes, it seems that it is our understanding of fundamental semantic concepts such as truth (in the liar paradox and Grelling’s paradox) and definability (in Berry’s and Richard’s paradoxes) that are deficient."
- **Incompleteness.** Cantini & Bruni (§6.4) record "applications of Berry’s paradox" to incompleteness (Vopěnka 1966, Boolos 1989, Chaitin); see Framings.
- **Complexity.** Chaitin (1994, p. 8) names as "the central idea that can be extracted from my version of the Berry paradox" the definition of "the program-size complexity of something", from which he developed "algorithmic information theory (AIT)". Cantini & Bruni (§6.4) relate the paradox to "the so-called Kolmogorov complexity and algorithmic information theory".

## Positions taken

Not ranked; each is reported with the source that records it.

- **No legitimate "all names"; nameability is relative (Russell 1908).** Russell's diagnosis (p. 225): "Here we assume, in obtaining the contradiction, that a phrase containing "all names" is itself a name, though it appears from the contradiction that it can not be one of the names which were supposed to be all the names there are. Hence "all names" is an illegitimate notion."
  His solution (p. 240): "nameable must mean "nameable by means of such-and-such assigned names,"" — a finite stock, or "the paradox collapses" — and "The solution of this paradox lies, I think, in the simple observation that "nameable in terms of names of the class N" is never itself nameable in terms of names of that class." Enlarging N to N′ repeats the situation; for "all names", "nameability in terms of such functions is non-predicative" (p. 241).
- **The vicious-circle principle (Russell 1906, after Poincaré).** Cantini & Bruni (§3.1): "Under the influence of Poincaré, Russell (1906, p. 634) accepted the vicious circle principle", in the form "Whatever comprises an apparent variable should not be one among the possible values of that variable."; the Berry paradox receives "Similar considerations" to Russell's 1906 liar solution. Bolander calls the Berry description "impredicative, since it implicitly refers to all descriptions, including itself" (§1.1).
- **Type theory (Hilbert, 1917–1918 lectures).** Per Cantini & Bruni (§4.2), in Hilbert's notes "Variants of the traditional Liar and of the Berry antinomy are introduced", and "Interestingly, Hilbert sticks essentially to type theory".
- **Several notions of meaning (Ramsey).** "In order to solve the semantical antinomies (e.g., the Liar, Berry’s), Ramsey proposes to distinguish several notions of meaning." (Cantini & Bruni, §4.2); as they report Ramsey, such contradictions "are due to faulty ideas about thought or language and they properly belong to “epistemology”."
- **The definability concept is at fault (Bolander's assessment).** Bolander (§2), quoted under Why it matters, continues: "If we fully understood these concepts, we should be able to deal with them without being led to contradictions."

**Cases for and against.** The sources read state these responses and
their scope but record no objection to any of them; none is recorded here.
No survey figure is recorded.

## Arguments in play

(none as separate argument pages yet). Related problems:
[the liar paradox](liar-paradox.md), which Russell 1908 lists with it and
Bolander files with it as semantic; [Russell's paradox](russells-paradox.md),
another item of the same 1908 list; [Curry's paradox](currys-paradox.md);
[the surprise examination paradox](surprise-examination-paradox.md), which
Cantini & Bruni (§6.4) connect to "Chaitin’s results" through Kritchman and
Raz 2011.

## Thinkers who addressed it

- **G. G. Berry** (1867–1928) — the source, per Russell 1908 (p. 223, "of the Bodleian Library"); Bolander (§1.6) calls him "the Oxford librarian", Boolos (1989, p. 388) "a librarian at Oxford University". Bolander reports Sorensen (2003, p. 332) crediting Berry also with the postcard paradox.
- **Henri Poincaré** (1906) — a proper definition "must be predicative, i.e., it must avoid vicious circles" (Cantini & Bruni §3.1, on Poincaré 1906b).
- **Bertrand Russell** — first published statement in Russell 1906, per Cantini & Bruni (§3.1); the nineteen-syllable form and solution in 1908 (pp. 223, 225, 240–241).
- **Beppo Levi** (1908) — "outlined an antinomy which is essentially a variant of Berry’s paradox" (Cantini & Bruni §3.1).
- **David Hilbert** (lectures 1917–1918) — Berry variants in a type-theoretic course (§4.2).
- **Frank P. Ramsey** — several notions of meaning (§4.2).
- **Saul Kripke** (early 1960s) — "noticed a proof somewhat similar" to Boolos's, per Boolos (1989, p. 388, note).
- **Petr Vopěnka** (1966) — second incompleteness theorem for Bernays–Gödel set theory "using a form of the same paradox" (Cantini & Bruni §6.4).
- **Gregory Chaitin** (idea 1970, by his account; lecture 1993, arXiv [chao-dyn/9406002](https://arxiv.org/abs/chao-dyn/9406002), [doi:10.1007/BFb0103569](https://doi.org/10.1007/BFb0103569); "The Berry paradox", *Complexity* 1, 1995, [doi:10.1002/cplx.6130010107](https://doi.org/10.1002/cplx.6130010107), not read) — information-theoretic incompleteness (excerpt: `raw/chaitin-1994-berry-paradox-information-theoretic-incompleteness.md`).
- **George Boolos** (1989, *Notices of the AMS* 36(4): 388–390, [AMS issue PDF](https://www.ams.org/journals/notices/198904/198904FullIssue.pdf)) — incompleteness without diagonalization (excerpt: `raw/boolos-1989-new-proof-goedel-incompleteness-berry.md`).
- **Gabriele Lolli** (2007, "A Berry-type paradox") and **Riccardo Bruni** (2013) — on Levi, as cited by Cantini & Bruni (§3.1); not read.

## Framings and reframings

- **From paradox to theorem (Chaitin).** Chaitin (1994, p. 1) recounts telling Gödel: "Professor Gödel, I’m fascinated by your incompleteness theorem. I have a new proof based on the Berry paradox that I’d like to tell you about.” Gödel said, “It doesn’t matter which paradox you use.”"
  Words become programs on a universal Turing machine and specifying becomes proving, giving "“the first positive integer that can be provedFAS to have the property that it cannot be specifiedUTM by a computer program with less than N bits”." (p. 6). A program of log2 N + cFAS bits finds it by searching proofs in "size order" (p. 7); since that "is much much smaller than N for all sufficiently large N! Thus for such N our FAS cannot enable us to exhibit any numbers that require programs more than N bits long." (p. 7).
- **Incompleteness without diagonalization (Boolos 1989).** "There is no algorithm whose output contains all true statements of arithmetic and no false ones." (p. 388). "In our proof, symbols are the "syllables"" (p. 389): a formula F(x) saying x is the least number not named by any formula of fewer than 10k symbols has 2k + 24 < 10k symbols, so the true statement identifying that number is not in the algorithm's output. Boolos's assessment (p. 389): "In view of this distinction, it seems justified to say that our proof, unlike the usual one, does not involve diagonalization." He credits Kreisel and Chaitin for "the impetus" (p. 389), while saying Chaitin's complexity notions are not used.
- **Randomness and limits.** Cantini & Bruni (§6.4): "In particular, Chaitin has shown in a number of papers how to exploit randomness to prove certain limitations of formal systems (see Chaitin 1995)."
- **Self-reference, or impredicativity.** Russell 1908 (p. 224) gives "self-reference or reflexiveness" as the common characteristic of his list (excerpt: `raw/russell-1903-1919-contradiction-discovery-and-types.md` §C); Bolander (§1.1) speaks of "an impredicative definition, or rather, an impredicative description."

## Vocabulary

- [Paradox](../vocabulary/paradox.md); [Validity](../vocabulary/validity.md);
  [Classical logic](../methods/classical-logic.md), in which the logic check
  above is run.
- Definability, nameability, impredicative definition, vicious-circle
  principle, ramified type theory, diagonalization, program-size
  (Kolmogorov) complexity, algorithmic information theory — open work in
  [vocabulary](../vocabulary/index.md).

Related problems: [Richard's paradox](richards-paradox.md), [the Hilbert–Bernays paradox](hilbert-bernays-paradox.md) (Read 2019: "the paradoxes of denotation"), [the card paradox](card-paradox.md) (Sorensen, per Bolander §1.6, credits Berry).

Related thinkers: [Russell](../thinkers/russell.md).
