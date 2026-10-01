---
type: article
about: concept
title: "Russell's paradox: is the set of all sets that are not members of themselves a member of itself?"
description: "The set R of all sets that are not members of themselves is a member of itself if and only if it is not — the contradiction Russell (1901) and Zermelo found in naive comprehension and Russell sent to Frege in 1902, with every response family the sources record (types, Separation, von Neumann's classes, Quine's stratification, paraconsistency) and the Barber as its disputed analogue."
tags: [problem, paradox, logic, philosophy-of-mathematics, set-theory]
timestamp: 2026-10-01T22:52:16Z
---

# Russell's paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
grades of claims as in [How claims are graded](../../conventions/how-claims-are-graded.md).
Source for the map: Irvine & Deutsch,
[SEP Fall 2024 "Russell's Paradox"](https://plato.stanford.edu/archives/fall2024/entries/russell-paradox/),
substantive revision 2020-10-12 (excerpt: `raw/sep-russell-paradox-fall-2024-history-and-responses.md`).
Primary texts: `raw/russell-1903-1919-contradiction-discovery-and-types.md`,
`raw/zermelo-1908-separation-axiom-and-independent-discovery.md`,
`raw/frege-1893-basic-law-v-and-russell-frege-letters.md`,
`raw/russells-paradox-responses-bibliographic-quine-1937-priest-2006.md`.
One of the [problems](./index.md); a [paradox](../vocabulary/paradox.md) in
the sense recorded there.

## The question

"Russell’s paradox is the most famous of the logical or set-theoretical paradoxes. Also known as the Russell-Zermelo paradox, the paradox arises within naïve set theory by considering the set of all sets that are not members of themselves. Such a set appears to be a member of itself if and only if it is not a member of itself."
(Irvine & Deutsch, preamble.)

The premise the SEP authors name is that "naïve set theory assumes the so-called naïve or unrestricted Comprehension Axiom" (§1): any condition
determines a set. With the condition "not a member of itself", R is defined,
and "Since by classical logic one case or the other must hold – either \(R\) is a member of itself or it is not – it follows that the theory implies a contradiction." (§1).

Russell's own 1919 statement ([Introduction to Mathematical Philosophy](https://archive.org/details/introductiontoma00russ), ch. XIII, p. 136):
"Form now the assemblage of all classes which are not members of themselves. This is a class: is it a member of itself or not? If it is, it is one of those classes that are not members of themselves, i.e. it is not a member of itself. If it is not, it is not one of those classes that are not members of themselves, i.e. it is a member of itself. Thus of the two hypotheses—that it is, and that it is not, a member of itself—each implies its contradictory. This is a contradiction."
In 1908: "Let w be the class of all those classes which are not members of themselves." — and then
"w is a w" turns out equivalent to "w is not a w"
([Russell 1908](https://doi.org/10.2307/2369948), §I, p. 222).

**Logic check (this implant, 2026-09-27).** Writing p for "R ∈ R", the
biconditional R ∈ R ↔ ¬(R ∈ R) is `p <-> ~p`. The run
`python3 _implant/skills/tools/logic.py check --premises 'p <-> ~p' --conclusion 'p & ~p'`
printed:

```
  P1: p <-> ~p    [(p <-> ~p)]
  C:  p & ~p    [(p & ~p)]

VALID
premises are jointly inconsistent — argument is vacuously valid
```

The tool checks only the propositional step. The step *to* `p <-> ~p` rests
on the unrestricted Comprehension Axiom (Irvine & Deutsch, §1) and on
instantiating it at R itself, which is
first-order and set-theoretic; it is that step the responses below
intervene on. Priest, Tanaka & Weber give the same derivation from the
Comprehension Schema, ending with r ∈ r ∧ r ∉ r
([SEP "Paraconsistent Logic"](https://plato.stanford.edu/archives/fall2024/entries/logic-paraconsistent/), §2.3.2).
Irvine & Deutsch add that the derivation need not use excluded middle: "However it is possible to formulate the paradox without appealing to Excluded Middle by relying instead upon the Law of Non-contradiction." — "So we can deduce both \(R \in R\) and its negation using only intuitionistically acceptable methods." (§4).

## Why it matters

- **For Frege's logicism.** "The paradox was of significance to Frege’s logical work since, in effect, it showed that the axioms Frege was using to formalize his logic were inconsistent." (Irvine & Deutsch, §2).
  The axiom is Frege's Axiom V, which the SEP glosses: "Frege’s Law states that the course-of-values of a concept \(f\) is identical to the course-of-values of a concept \(g\) if and only if \(f\) and \(g\) agree on the value of every argument" (§2).
  In 1893 Frege had named that law, his "Grundgesetz der Werthverläufe (V)",
  as the one place a dispute could arise: "Ein Streit kann hierbei, soviel ich sehe, nur um mein Grundgesetz der Werthverläufe (V) entbrennen" — "Ich halte es für rein logisch." ([Grundgesetze I](https://archive.org/details/bub_gb_LZ5tAAAAMAAJ), Vorwort, p. VII).
- **For set theory.** Zermelo opened his 1908 axiomatisation with it: "Angesichts namentlich der „Russellschen Antinomie“ von der „Menge aller Mengen, welche sich selbst nicht als Element enthalten“ scheint es heute nicht mehr zulässig, einem beliebigen logisch definierbaren Begriffe eine „Menge“ oder „Klasse“ als seinen „Umfang“ zuzuweisen." ([Zermelo 1908b](https://doi.org/10.1007/BF01449999), p. 261).
- **For how deep it goes.** Quine, as the SEP reports him, "describes the paradox as an “antinomy” that “packs a surprise that can be accommodated by nothing less than a repudiation of our conceptual heritage” (1966, 11)." (§4).
  Dana Scott, quoted there: "“It is to be understood from the start that Russell’s paradox is not to be regarded as a disaster. It and the related paradoxes show that the naïve notion of all-inclusive collections is untenable. That \(is\) an interesting result, no doubt about it” (1974, 207)." (§4).

## Positions taken

The SEP's summary of the common thread: "Standard responses to the paradox attempt to limit in some way the conditions under which sets are formed." (§1).
Families in the order the entry treats them (§§3–4). None is ranked here.

- **Sets versus classes (Cantor).** "Even prior to Russell’s discovery, Cantor had rejected unrestricted Comprehension in favour of what was, in effect, a distinction between sets and classes" (§3).
- **Frege's own diagnosis (1903).** The SEP quotes Frege's appendix to
  vol. II: "“Is it always permissible to speak of the extension of a concept, of a class? And if not, how do we recognize the exceptional cases?" (§2, Frege 1903, 127).
  Russell's 1903 note on that appendix: "suggesting that the solution is to be found by denying that two propositional functions which determine equal classes must be equivalent. As it seems very likely that this is the true solution, the reader is strongly recommended to examine Frege's argument on the point."
  ([Principles of Mathematics](https://archive.org/details/cu31924001610421), App. A, p. 522). The SEP reports that "Frege eventually felt forced to abandon many of his views about logic and mathematics" (§2).
- **Type theory (Russell 1903, 1908; Whitehead & Russell).** In 1903 "The doctrine of types is here put forward tentatively, as affording a possible solution of the contradiction" (App. B, §497, p. 523);
  its own limit: "there is at least one closely analogous contradiction which is probably not soluble by this doctrine." (§500, p. 528).
  In 1908, the rule "Whatever involves all of a collection must not be one of the collection;" (p. 225), the "vicious-circle principle" (p. 237).
  *Case against, as reported:* "Both versions have been criticized for being too ad hoc to eliminate the paradox successfully." (Irvine & Deutsch, §3; no critic named in the excerpt).
- **Formalism (Hilbert) and intuitionism (Brouwer)** are listed by the SEP
  among early responses: Hilbert's "idea of allowing the use of only finite, well-defined and constructible objects" and Brouwer's "basic idea was that one cannot assert the existence of a mathematical object unless one can define a procedure for constructing it." (§3).
  *Case against the intuitionist route, as Irvine & Deutsch argue:* the
  paradox is derivable "using only intuitionistically acceptable methods." (§4).
- **Separation (Zermelo 1908).** Axiom III, "Axiom der Aussonderung": only
  elements of an existing set M are separated out by a definite condition
  (implant's gloss of Zermelo 1908b, p. 263). The result: "der Bereich 𝔅 ist selbst keine Menge, — womit die „Russellsche Antinomie“ für unseren Standpunkt beseitigt ist." (p. 265).
  Irvine & Deutsch: "But in this case, all the contradiction shows is that \(V\) is not a set." (§4).
  *Cost, as they state it:* "As one might imagine, this requires a host of additional set-existence axioms, none of which would be required if NC had held up." (§4).
- **Sets and classes by membership (von Neumann 1925).** "Von Neumann introduces a distinction between membership and non-membership and, on this basis, draws a distinction between sets and classes." (§4).
  Irvine & Deutsch judge that "Von Neumann’s method, while admired by the likes of Gödel and Bernays, has been undervalued in recent years." (§4).
- **Stratified comprehension (Quine 1937, "New Foundations").** "Quine (1937) and (1967) similarly provide another untyped method (in letter if not in spirit) of blocking Russell’s paradox, and one that is rife with interesting anomalies. Quine’s basic idea is to introduce a stratified comprehension axiom." (§4; [Quine 1937](https://doi.org/10.2307/2300564), Amer. Math. Monthly 44: 70–80, held bibliographically only).
- **Paraconsistent logic (Priest 2006, ch. 18; Brady; Weber).** The SEP
  entry names it: "this is the paraconsistent approach, which limits the overall effect of an isolated contradiction on an entire theory." (§4).
  *Case for, by its proponents:* "A paraconsistent approach makes it possible to have theories of truth and sethood in which the mathematically fundamental intuitions about these notions are respected." (Priest, Tanaka & Weber, §2.3.2), citing Brady (1989; 2006) and Weber (2010b, 2012).
  *Case against:* Irvine & Deutsch: "Unfortunately, even giving up EFQ is not enough to retain a semblance of NC." — the reason being "a negation-free paradox due to Curry" (§4; see [Curry's paradox](../problems/currys-paradox.md)). Priest, Tanaka & Weber record that "Incurvati (2020, chapter 4) gives a detailed critique of the paraconsistent approach to naive set theory." (§2.3.2).
  [Priest 2006](https://doi.org/10.1093/acprof:oso/9780199263301.001.0001) is held bibliographically only; no sentence of his book is quoted here.
- **Irvine & Deutsch's comparison.** They conclude that "neither intuitionism nor paraconsistency plus the abandonment of Contraction will offer an advantage over the untyped solutions of Zermelo, von Neumann, or Quine." (§4) — their assessment, reported, not the implant's.
- **Frege's arithmetic without Axiom V.** "although the matter remains controversial, later research has revealed that the paradox does not necessarily short circuit Frege’s derivation of arithmetic from logic alone. Frege’s version of NC (his Axiom V) can simply be abandoned." (Irvine & Deutsch, §4; the researchers are not named in the excerpt).

No survey figure is recorded.

## Arguments in play

(none recorded as separate argument pages yet). The derivation above is
checked in propositional form only; compare the same pattern in the
[liar paradox](../problems/liar-paradox.md) (T ↔ ¬T) and the negation-free
[Curry's paradox](../problems/currys-paradox.md).

## Thinkers who addressed it

- **Cesare Burali-Forti** (1897) — "had discovered a similar antinomy in 1897" (Irvine & Deutsch, §2).
- **Ernst Zermelo** (1897–1902) — the SEP dates his find "sometime between 1897 and 1902, possibly anticipating Russell by some years", adding that "Kanamori concludes that the discovery could easily have been as late as 1902 (Kanamori 2009, 411)." (§2).
  Zermelo's own claim (1908a, footnote, pp. 118–119, [DOI](https://doi.org/10.1007/BF01450054)): "Indessen hatte ich selbst diese Antinomie unabhängig von Russell gefunden und sie schon vor 1903 u. a. Herrn Prof. Hilbert mitgeteilt."
- **Bertrand Russell** (1901) — "Exactly when the discovery took place is not clear." Russell gave "in June 1901" (1944), "in the spring of 1901" (1959), and May (1969) (SEP §2).
  His 1919 account: "When I first came upon this contradiction, in the year 1901, I attempted to discover some flaw in Cantor's proof that there is no greatest cardinal" (p. 136).
- **Russell to Frege, 16 June 1902** — "Russell wrote to Frege with news of his paradox on June 16, 1902." (SEP §2). The letters are printed in van Heijenoort (ed.), *From Frege to Gödel* (1967), pp. 124–125 and 126–128 (bibliographic only; not read).
- **Gottlob Frege** (1893, 1903) — Basic Law V (1893, p. VII); the appendix
  to vol. II, "hastily composed" (SEP §2).
- **Georg Cantor** — sets versus classes (SEP §3).
- **David Hilbert**, **Luitzen Brouwer** — formalism, intuitionism (SEP §3).
- **John von Neumann** (1925) — sets and classes (SEP §4).
- **W. V. Quine** (1937, 1966) — stratified comprehension; the "antinomy"
  reading and the Barber contrast (SEP §4).
- **Dana Scott** (1974) — "not to be regarded as a disaster" (SEP §4).
- **[Graham Priest](../thinkers/priest.md)** (2006, ch. 18), **Brady** (1989; 2006), **Zach Weber** —
  paraconsistent set theory (SEP §4; SEP "Paraconsistent Logic" §2.3.2).
- **Nathan Salmon** (2013) — the Barber is closer to Russell's paradox than
  Quine allowed (SEP §4).

## Framings and reframings

- **The Barber: analogue or twin?** Russell's paradox "is an instance of T269" — ~∃y∀x(Fxy ≡ ~Fxx), a theorem of first-order logic (Irvine & Deutsch §4, citing Kalish, Montague and Mar 2000).
  "But that pattern also underwrites an endless list of seemingly frivolous “paradoxes” such as the famous paradox of the barber who shaves all and only those who do not shave themselves" (§4).
  "The pattern of reasoning is the same and the conclusion – that there is no such Barber, no such efficient God, no such set of non-self-membered sets – is the same: such things simply don’t exist." (§4).
  Why then call only one an antinomy? "The standard answer to this question is that the difference lies in the subject matter." Quine: "The reason is that there has been in our habits of thought an overwhelming presumption of there being such a class but no presumption of there being such a barber" (1966, 14, quoted in §4).
  The other side, as the SEP reports it: "They will insist that the question raised by T269 is not what barbers or Gods there are, but rather what non-paradoxical objects there are." — "Thus, from this perspective, the relation between the Barber and Russell’s paradox is much closer than many (following Quine) have been willing to allow (Salmon 2013)." (§4).
- **Self-reference as the common root (Russell 1908).** "In all the above contradictions (which are merely selections from an indefinite number) there is a common characteristic, which we may describe as self-reference or reflexiveness." (p. 224).
- **Russell's 1903 admission.** "And the contradiction discussed in Chapter x. proves that something is amiss, but what this is I have hitherto failed to discover." (Preface, pp. v–vi).
- **From classes to propositions.** The 1903 propositions paradox "together with the semantic paradoxes, led Russell to formulate his ramified version of the theory of types." (Irvine & Deutsch, §4).

Other paradox pages: [sorites](../problems/sorites-paradox.md),
[Zeno](../problems/zenos-paradoxes.md),
[surprise examination](../problems/surprise-examination-paradox.md),
[Newcomb's problem](../problems/newcombs-problem.md).

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — the SEP calls this one a
  "set-theoretical" paradox; Quine an "antinomy".
- [Validity](../vocabulary/validity.md) — the logic check reports a
  vacuously valid argument from inconsistent premises.
- [Classical logic](../methods/classical-logic.md) — the logic the §1
  derivation uses; the intuitionistic and paraconsistent routes revise it.
- *Set*, *class*, *comprehension*, *separation*, *type*, *stratification*,
  *antinomy* — open work in [vocabulary](../vocabulary/index.md).

Related problems: [the Grelling–Nelson paradox](grelling-nelson-paradox.md) and [Richard's paradox](richards-paradox.md) (Russell 1908 lists them with the class paradox), [the barber paradox](barber-paradox.md) (SEP "Russell's Paradox" §4 discusses the barber).
