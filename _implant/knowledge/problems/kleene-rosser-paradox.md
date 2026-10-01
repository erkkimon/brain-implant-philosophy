---
type: article
about: concept
title: "The Kleene–Rosser paradox"
description: "Kleene and Rosser (1935) proved that Church's 1932–1933 logic and Curry's early combinatory logic are inconsistent by setting up a version of Richard's paradox inside them; Curry's 1941 diagnosis (combinatorial and deductive completeness are incompatible), his 1942 simplification now known as Curry's paradox, and how the encyclopedia sources separate the illative systems from the pure untyped lambda calculus."
tags: [problem, paradox, logic, self-reference, lambda-calculus, combinatory-logic, philosophy-of-mathematics]
timestamp: 2026-10-01T22:52:16Z
---

# The Kleene–Rosser paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Primary text: S. C. Kleene and J. B. Rosser, "The Inconsistency of Certain
Formal Logics", *Annals of Mathematics* 36(3), 1935, from p. 630,
[doi:10.2307/1968646](https://doi.org/10.2307/1968646) (bibliographic data
verified by DOI content negotiation; the text was not read — what it proves
is reported here only as the sources below report it). Read: Curry, "The
paradox of Kleene and Rosser", *Transactions of the AMS* 50(3), 1941,
pp. 454–516, [doi:10.1090/S0002-9947-1941-0005275-6](https://doi.org/10.1090/S0002-9947-1941-0005275-6)
(excerpt: `raw/curry-1941-paradox-of-kleene-and-rosser.md`).
Maps: Cantini & Bruni, [SEP Fall 2024 "Paradoxes and Contemporary Logic"](https://plato.stanford.edu/archives/fall2024/entries/paradoxes-contemporary-logic/)
§4.1 (excerpt: `raw/sep-paradoxes-contemporary-logic-fall-2024-kleene-rosser.md`);
Alama & Korbmacher, [SEP Fall 2024 "The Lambda Calculus"](https://plato.stanford.edu/archives/fall2024/entries/lambda-calculus/)
§§2, 4.1 (excerpt: `raw/sep-lambda-calculus-fall-2024-early-inconsistency.md`);
Deutsch & Marshall, [SEP Fall 2024 "Alonzo Church"](https://plato.stanford.edu/archives/fall2024/entries/church/)
(excerpt: `raw/sep-church-fall-2024-kleene-rosser-richard.md`); Shapiro &
Beall, [SEP Fall 2024 "Curry's Paradox"](https://plato.stanford.edu/archives/fall2024/entries/curry-paradox/)
(excerpt: `raw/sep-curry-paradox-fall-2024-construction-lemma-and-responses.md`).
Admitted from Wikipedia's [List of paradoxes, revision 1376699902](https://en.wikipedia.org/w/index.php?title=List_of_paradoxes&oldid=1376699902),
"Logic" (excerpt: `raw/wikipedia-list-of-paradoxes-kleene-rosser-entry.md`).

## The question

The Wikipedia list states it as: "Kleene–Rosser paradox: By formulating an equivalent to Richard's paradox, untyped lambda calculus is shown to be inconsistent." (rev. 1376699902).
Curry (1941, p. 454) reports the result: "In 1935 Kleene and Rosser published a proof that certain systems of formal logic are inconsistent, in the sense that every formula which can be expressed in their notation is also demonstrable"; by his count it applies to Church's system of 1932–1933 and his own combinatory system of 1934.
Deutsch & Marshall (SEP 2022/2024) say the same targets "fell prey to Richard’s paradox"; Cantini & Bruni (SEP 2021/2024, §4.1) date the proof to 1934 and say Kleene and Rosser "(essentially) proved a version of the Richard paradox (both systems can provably enumerate their own provably total definable number theoretic functions)."

The core, as Curry (1941, p. 456) sets it out informally: "In any formal system of arithmetic the number of definable numerical functions of natural numbers is enumerable"; enumerate them φ1, φ2, …, define f(x) = φx(x) + 1, and if f is some φn then φn(n) = φn(n) + 1, "which is a contradiction."
In a system that is both combinatorially and deductively complete, per
Curry, the enumeration and f can both be carried out inside the system.

The question is which feature of such systems is responsible, and whether
the result touches the untyped λ-calculus itself or only the logical
systems built around it. Term contracts: [paradox](../vocabulary/paradox.md),
[validity](../vocabulary/validity.md); "inconsistent" here means, per
Curry (1941, p. 454), that every expressible formula is demonstrable.

**Logic check (this implant, 2026-10-02; logic, not a position).** Curry's
1941 thesis (p. 455) has the shape: let `c` = *the system is
combinatorially complete*, `d` = *it is deductively complete*, `i` = *it is
inconsistent*. `logic.py check --premises "(c & d) -> i" "~i" --conclusion "~(c & d)"`
outputs "VALID" ("matches schema: modus tollens"); with conclusion `~c` it
outputs "INVALID" (counterexample "c=T, d=F, i=F"). The tool says only that
a consistent system must lack at least one of the two properties, not which;
the responses below differ on that.

## Why it matters

- **A limit on foundational systems.** Curry (1941, p. 454) judges that "the argument of Kleene and Rosser represents a theorem of great importance for the guidance of future research. It is a theorem of the same general character as the famous incompleteness theorems of Löwenheim, Skolem, and Godel"
- **The origin of Curry's paradox.** Alama & Korbmacher (SEP 2023/2024, §2): "It turned out that these early attempts at so-called illative \(\lambda\)-calculus and combinatory logic were inconsistent. Curry isolated and polished the inconsistency; the result is now known as Curry’s paradox." Curry 1942b took the same title as Kleene and Rosser, per Cantini & Bruni (§4.1) "“in deference to the original discoverers of the contradiction”".
- **Richard's paradox made formal.** Curry (1941, p. 455): "The argument is essentially a refinement of the Richard paradox; it shows, in fact, that the Richard paradox can be set up formally within the system"; Cantini & Bruni (§4.1) report that "The result was triggered by Church himself in 1934, when he used the Richard paradox to prove a kind of incompleteness theorem (with respect to statements asserting the totality of number theoretic functions)."

## Positions taken

Not ranked; each is reported with the source that records it. The sources
read record diagnoses and later constructions rather than rival solutions.

- **Church's design: restrict excluded middle (Church 1932).** Church, as quoted by Deutsch & Marshall: "Rather than adopt the method of Russell for avoiding the paradoxes of mathematical logic, or that of Zermelo, both of which appear somewhat artificial, we introduce for this purpose, as we have said, a certain restriction on the law of excluded middle. (1932 [BE: 52])" Cantini & Bruni (§4.1): "Church’s hope was that contradictions could be avoided by ensuring the possibility that a propositional function be undefined for some argument." Per Deutsch & Marshall, the 1933 paper corrected a Russell-type derivation in the 1932 system, and Kleene and Rosser then reached both.
- **The two completeness properties are incompatible (Curry 1941).** "The essence of the Kleene-Rosser theorem is that it shows that these two kinds of completeness are incompatible—i.e., that any system which possesses both of them is inconsistent." (p. 455). Cantini & Bruni (§4.1) report that "The reason for the inconsistencies was eventually clarified by Curry’s 1941 essay."
- **A simpler route through Russell's paradox (Curry 1941 note, 1942b).** Curry (1941, p. 455, n. 9, added in proof): "Since this was written, I have discovered a much simpler way of deriving the contradiction for a system which is combinatorially complete in the strong sense"; "This new derivation which is based on the Russell paradox is contained in a paper, The inconsistency of certain formal logics, now in preparation." Cantini & Bruni (§4.1) assess Curry's 1941 proof as "unsatisfactory because it heavily uses a detour through number theory and Gödelization, which, as a matter of fact, is unnecessary as Curry himself soon discovered".
- **A constraint on functional application (Curry 1942).** Per Shapiro & Beall (SEP 2018/2024, supplement), "Curry regarded his paradox as a constraint on an adequate theory of functional application."; for the responses to the resulting paradox see [Curry's paradox](currys-paradox.md).
- **The pure calculus survives (Church–Rosser 1936).** Deutsch & Marshall: "The mere part—the pure untyped λ-calculus—is, however, consistent in the sense that not all equations between λ terms are derivable. This follows from an early result due to Church himself and Rosser (1936)—the Church-Rosser theorem". Alama & Korbmacher (§4.1) likewise: "We can thus take inconsistency of \(\lambda\) to mean: all equations are derivable." and report that this is not the case.

**Cases for and against.** The sources read record no objection to any of
these diagnoses; none is recorded here. No survey figure is recorded.

## Arguments in play

(none as separate argument pages yet). Related problems:
[Curry's paradox](currys-paradox.md), Curry's 1942 simplification;
[Russell's paradox](russells-paradox.md), on which the simpler route is
"based" per Curry (1941, n. 9); [Richard's paradox](richards-paradox.md),
the core per Curry 1941, Cantini & Bruni and Deutsch & Marshall;
[the liar paradox](liar-paradox.md), to which Curry likened the indirect
route (Cantini & Bruni §4.1); [the Berry paradox](berry-paradox.md), filed
with Richard's among paradoxes of definability by Cantini & Bruni (§2).

## Thinkers who addressed it

- **Alonzo Church** — the 1932 and 1933 systems ([doi:10.2307/1968337](https://doi.org/10.2307/1968337), [doi:10.2307/1968702](https://doi.org/10.2307/1968702); verified by content negotiation, not read); per Deutsch & Marshall, in 1932 "Church first formulated the (untyped) λ-calculus as a mere part of the whole system"; used Richard's paradox for an incompleteness result in 1934 (Cantini & Bruni §4.1).
- **Stephen Cole Kleene** and **J. Barkley Rosser** — the 1935 proof; Curry (1941, p. 454, n. 5) says it "depends on results in a whole series of previous papers (viz., Church's C 359.4 and 6, Kleene's C 497.1 and 2, and Rosser's 546.1), totalling 162 pages."
- **Haskell B. Curry** — the 1941 analysis, "The proof of Kleene and Rosser is long and intricate" (p. 454); the 1942 paper (*Journal of Symbolic Logic* 7(3): 115–117, [doi:10.2307/2269292](https://doi.org/10.2307/2269292), verified by content negotiation, not read).
- **Rosser** with Church — the Church–Rosser theorem (1936), per Deutsch & Marshall.

## Framings and reframings

- **Two kinds of completeness (Curry 1941).** "I shall call these combinatorial completeness and deductive completeness respectively." (p. 455). "A theory is deductively complete if whenever we can derive a proposition B on the hypothesis that another proposition A holds then we can derive without hypothesis a third proposition" (p. 455); combinatorial completeness, as Curry describes it, lets every expression in a variable x be represented as a function of x. Cantini & Bruni (§4.1) relate this to the deduction theorem and to Church's λx.M.
- **Direct and indirect self-reference (Curry 1942, as reported).** Cantini & Bruni (§4.1) report two constructions of a term A with A = A ⊃ B: a direct one, and an indirect one using an enumerator and Gödel numbers that exploits "the machinery of Curry 1941 and Kleene-Rosser"; "Curry suggests that these two routes are akin, respectively, to Russell’s paradox and to the Liar." Their assessment: "It is interesting to note that the two ways correspond to by-now standard tools, the so-called first fixed point theorem and second fixed point theorem of combinatory logic and lambda calculus (Barendregt 1984, p. 131 and p. 143"
- **Illative systems vs the pure calculus.** The Wikipedia entry speaks of "untyped lambda calculus"; Deutsch & Marshall say Kleene and Rosser reached "both systems—those of Church 1932 and 1933—as well as related early systems of combinatory logic", and Alama & Korbmacher (§4.1): "Early formulations of the idea of \(\lambda\)-calculus by A. Church were indeed inconsistent; see (Barendregt, 1985, appendix 2) or (Rosser, 1985) for a discussion." *Structural note (this implant, manifest G4):* the Wikipedia entry names
its object "untyped lambda calculus", Deutsch & Marshall name Church's two
systems and early combinatory logic, and the same entry calls "the pure
untyped λ-calculus" consistent; the two wordings are recorded side by side.

## Vocabulary

- [Paradox](../vocabulary/paradox.md); [Validity](../vocabulary/validity.md);
  [Classical logic](../methods/classical-logic.md), in which the logic check
  above is run.
- Untyped λ-calculus, illative combinatory logic, combinatorial
  completeness, deductive completeness (deduction theorem), enumerator,
  Gödel numbering, fixed point theorem, Church–Rosser theorem — open work in
  [vocabulary](../vocabulary/index.md).
