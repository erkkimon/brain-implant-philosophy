---
type: article
about: concept
title: "The Grelling–Nelson paradox (heterological)"
description: "Call a word heterological if it does not have the property it designates; is 'heterological' heterological? The paradox of Grelling and Nelson (1908), circulated as 'Weyl's contradiction' after Das Kontinuum (1918); Weyl's 'Scholastik' verdict, Ramsey's group-B (semantic) classification and his two solutions (orders of functions; an ambiguity in 'meaning'), Thomson's ill-defined-predicate reading, the structural twin of Russell's paradox and the halting-problem proof that mimics it."
tags: [problem, paradox, logic, self-reference, semantics, philosophy-of-language, philosophy-of-mathematics]
timestamp: 2026-10-01T22:52:16Z
---

# The Grelling–Nelson paradox (heterological)

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Primary text: K. Grelling and L. Nelson, "Bemerkungen zu den Paradoxien von
Russell und Burali-Forti", *Abhandlungen der Fries'schen Schule* 2 (1908),
pp. 301–334 — bibliographic data as given by Cantini & Bruni (SEP, Bibliography,
which prints "Fries’chen"); not read here, no open copy found. Read primary texts: Weyl, *Das Kontinuum*
(1918), §1, p. 2, [archive.org scan](https://archive.org/details/daskontinuumkrit00weyluoft)
(excerpt: `raw/weyl-1918-das-kontinuum-heterologisch.md`); Ramsey, "The
Foundations of Mathematics", *Proc. London Math. Soc.* s2-25 (1926),
pp. 338–384, [doi:10.1112/plms/s2-25.1.338](https://doi.org/10.1112/plms/s2-25.1.338),
read in the 1931 reprint, [archive.org scan](https://archive.org/details/in.ernet.dli.2015.46352)
(excerpt: `raw/ramsey-1926-foundations-of-mathematics-heterological.md`).
Maps: Bolander, [SEP Fall 2024 "Self-Reference and Paradox"](https://plato.stanford.edu/archives/fall2024/entries/self-reference/)
§§1.1, 1.4, 2, 2.4 (excerpts: `raw/sep-self-reference-fall-2024-grelling-paradox.md`,
`raw/sep-self-reference-fall-2024-berry-paradox.md`); Cantini & Bruni,
[SEP Fall 2024 "Paradoxes and Contemporary Logic"](https://plato.stanford.edu/archives/fall2024/entries/paradoxes-contemporary-logic/)
§§3, 3.3.2, 4.2 (excerpt: `raw/sep-paradoxes-contemporary-logic-fall-2024-grelling-nelson-paradox.md`);
Sorensen, [SEP Fall 2024 "Epistemic Paradoxes"](https://plato.stanford.edu/archives/fall2024/entries/epistemic-paradoxes/)
§4 (excerpt: `raw/sep-epistemic-paradoxes-fall-2024-grelling-thomson.md`).
Admitted from Wikipedia's [List of paradoxes, revision 1376699902](https://en.wikipedia.org/w/index.php?title=List_of_paradoxes&oldid=1376699902),
"Logic" (excerpt: `raw/wikipedia-list-of-paradoxes-grelling-nelson-entry.md`).

## The question

Cantini & Bruni (SEP 2021/2024, §3.3.2) render the 1908 formulation: "To each word there corresponds a concept, that the very word designates, and which applies to it or does not apply; in the first case, we call the word autological, else heterological."
Then: "Assuming that the word is autological, the concept that it designates applies, hence ‘heterological’ is heterological. But if the word is heterological, the designated concept does not apply, so ‘heterological’ is not heterological."

Other wordings on record: Bolander (SEP 2024, §1.1): "Say a predicate is heterological if it is not true of itself, that is, if it does not itself have the property it expresses. Then the predicate “German” is heterological, since it is not itself a German word, but the predicate “deutsch” is not heterological."
and the question "Is “heterological” heterological?"; Weyl (1918, p. 2) with
„kurz" and „lang": "Ein Eigenschaftswort heiße autologisch, wenn dieses Wort selber die Eigenschaft besitzt, die seine Bedeutung ausmacht; falls es sie nicht besizt, heterologisch."
Ramsey (1931 reprint, p. 27) with "short" and "long", concluding "So we have a complete contradiction."
The Wikipedia list: "Grelling–Nelson paradox: Is the word "heterological", meaning "not applicable to itself", a heterological word? (A close relative of Russell's paradox.)"

The question is what goes wrong: whether "heterological" is a word of the
kind its own definition ranges over, whether "designates" or "means" is used
in one sense throughout, and whether the question has a sense at all. The
term contracts are [paradox](../vocabulary/paradox.md) and
[validity](../vocabulary/validity.md).

**Logic check (this implant, 2026-10-02; logic, not a position).** Let `h` =
*'heterological' is heterological*. The definition applied to the word itself
gives `h <-> ~h`. `logic.py check --premises "h <-> ~h" --conclusion "q"`
outputs "VALID" and "premises are jointly inconsistent — argument is vacuously valid";
with premises `h -> ~h`, `~h -> h` (the two halves of the 1908 argument) and
conclusion `h & ~h` it outputs the same two lines. With `w` = *the definition
determines a predicate that applies to every word, itself included*,
`--premises "w -> (h <-> ~h)" --conclusion "~w"` outputs "VALID". The tool
does not say which reading of `w` — the range of words, the sense of
"means", or meaningfulness — a response gives up; the positions below differ
on that.

## Why it matters

- **A new paradox in a programme to unify them.** Cantini & Bruni (§3) list "new paradoxes were discovered (Berry, Grelling-Nelson), an old paradox—the Liar—showed up again" for 1905–1913; on the paper (§3.3.2): "Close to the same philosophical inspiration, the influential paper of Grelling and Nelson (1908) provides an attempt to unify paradoxes and to isolate their underlying structure."
- **Semantic or logical.** Ramsey (1931 reprint, p. 20) lists "(8) Weyl’s contradiction about ‘heterologisch" in group B, contradictions that "all contain some reference to thought, language, or symbolism, which are not formal but empirical terms." Cantini & Bruni (§4.2) call this "the by-now standard distinction between logical and epistemological contradictions".
- **Twin of Russell's paradox.** Bolander (§1.4): "The only significant difference between these two sets is that the first is defined on predicates whereas the second is defined on sets." and "We have here two paradoxes of an almost identical structure belonging to two distinct classes of paradoxes: one is semantic and the other set-theoretic."
- **The concept of truth.** Bolander (§2) judges: "In case of the semantic paradoxes, it seems that it is our understanding of fundamental semantic concepts such as truth (in the liar paradox and Grelling’s paradox) and definability (in Berry’s and Richard’s paradoxes) that are deficient."
- **Computability.** Bolander (§2.4) proves the undecidability of the halting problem with "heterological" Turing machines: "The proof mimics Grelling’s paradox."

## Positions taken

Not ranked; each is reported with the source that records it.

- **The question has no sense (Weyl 1918).** Weyl (p. 2) introduces it as showing into what nonsense one falls by forgetting that a sentence of subject–predicate form may be "sinnlos", and concludes: "Der Formalismus sieht sich hier einem unlösbaren Widerspruch gegenüber; in Wahrheit aber handelt es sich um Scholastik schlimmster Sorte: die geringste Besinnung zeigt, daß sich mit der Frage, ob das Wort „heterologisch“ selbst auto- oder heterologisch sei, schlechterdings kein Sinn verbinden läßt."
- **Orders of functions: 'heterological' is not an adjective of the defined kind (Principia, as Ramsey applies it).** Ramsey (p. 27) states the solution "According to the principles of Principia Mathematica": "So that when heterological and autological are unambiguously defined, ‘heterological’ is not an adjective in the sense in question, and is neither heterological nor autological, and there is no contradiction."
- **An ambiguity in "meaning" (Ramsey 1926).** With predicative functions in his own sense, Ramsey (pp. 42–43) derives the contradiction again, so the Principia solution "fails", and denies instead that ‘heterological’ means heterological in the sense R used in the definition: "We can easily show that this is really the case, so that the contradiction is simply due to an ambiguity in the word ‘meaning’ and has no relevance to mathematics whatever."
  Cantini & Bruni (§4.2): "Ramsey’s point is that this sense of meaning cannot be the same as that given by \(R\) and this blocks the contradiction, when we apply \(H\) to “heterological” (ibid.,p. 370). So one needs a new meaning relation depending on the given fixed \(R\). These ideas foreshadow those of Tarski."
- **Not a well-defined predicate (Thomson 1962, as Sorensen reports).** Sorensen (SEP 2022/2024, §4): "The common solution to this puzzle is that ‘heterological’, as defined by Grelling, is not a well-defined predicate (Thomson 1962). In other words, “Is ‘heterological’ heterological?” is without meaning." The "common" is Sorensen's assessment; Thomson's chapter was not read here.
- **Impredicativity as the diagnosis (Bolander's reading).** Bolander (§1.1): "Grelling’s paradox is self-referential, since the definition of the predicate heterological refers to all predicates, including the predicate heterological itself." and such definitions "are called impredicative." (sentence in `raw/sep-self-reference-fall-2024-berry-paradox.md`).

**Cases for and against.** Recorded objections are internal to the sources
read: Ramsey (p. 43) argues that the Principia solution fails once the range
is predicative functions in his sense; Cantini & Bruni (§3.3.2) qualify
Weyl: "It is interesting to observe that, in the light of recent developments, Weyl’s negative verdict ought to be weakened (see section 6)."
No objection to Ramsey's own solution, to Thomson's or to Bolander's reading
is recorded in the sources read; none is recorded here. No survey figure is
recorded.

## Arguments in play

(none as separate argument pages yet). Related problems:
[Russell's paradox](russells-paradox.md), whose set Bolander (§1.4) sets
beside the extension of "heterological", and which Weyl (p. 2) names as the
paradox's origin ("im wesentlichen von Russell herrührende »Paradoxie«");
[the liar paradox](liar-paradox.md), which Bolander (§1.1) says the argument
"runs more or less like"; [the barber paradox](barber-paradox.md), the
parallel Sorensen (§4) draws: "There can be no predicate that applies to all and only those predicates it does not apply to for the same reason that there can be no barber who shaves all and only those people who do not shave themselves."
and Goldstein (2004, p. 299), who groups "the Barber, Russell's, and
Grelling's" as cases where "what seemed, at first sight, to be a specifying
condition turned out to be a biconditional specifying nothing" (excerpt:
`raw/goldstein-2004-catch-22-vacuous-biconditional.md`);
[the Berry paradox](berry-paradox.md), filed with it as semantic by Bolander
(§1.1) and by Cantini & Bruni (§2). Siblings: [Richard's paradox](richards-paradox.md),
[the Epimenides paradox](epimenides-paradox.md).

## Thinkers who addressed it

- **Kurt Grelling** and **Leonard Nelson** (1908) — the paper; the paradox "credited to Grelling" (Cantini & Bruni §3.3.2), part of "a project to develop a philosophically minded “kritische Mathematik”"; Nelson "had Hilbert’s strong support (see Peckhaus 1990)" (same section).
- **Hermann Weyl** (1918, *Das Kontinuum* §1, p. 2) — "Scholastik schlimmster Sorte"; Ramsey's name "Weyl’s contradiction" cites this page.
- **Frank P. Ramsey** (1926; reprint pp. 20, 27, 42–43) — group B; the Principia solution and his own.
- **J. F. Thomson** (1962, "On Some Paradoxes", in R. J. Butler (ed.), *Analytical Philosophy*, pp. 104–119) — not read; reported by Sorensen.
- **Thomas Bolander** (SEP 2024) — structure shared with Russell and Cantor; the halting-problem proof.
- **Volker Peckhaus** — "Paradoxes in Göttingen", in G. Link (ed.), *One Hundred Years of Russell's Paradox*, de Gruyter 2004, pp. 501–516, [doi:10.1515/9783110199680.501](https://doi.org/10.1515/9783110199680.501) (author and pages from the DOI record); and a chapter "The Genesis of Grelling’s Paradox", in I. Max and W. Stelzner (eds), *Logik und Mathematik*, de Gruyter 1995, pp. 269–280, [doi:10.1515/9783110887792.269](https://doi.org/10.1515/9783110887792.269), whose DOI record names no author; Peckhaus's own [list of talks](https://kw.uni-paderborn.de/fileadmin/fakultaet/Institute/philosophie/Peckhaus/Schriften_zum_Download/Peckhaus_Vortraege.pdf) has a talk of that title at the Jena Frege-Kolloquium, 7 October 1993. Cantini & Bruni (§3.3.2) cite a further "Peckhaus 1990" for Nelson and Hilbert. Bibliographically verified only; none read, so nothing is reported from them.
- Further literature found by DOI and not read: R. L. Martin, "On Grelling's Paradox", *Philosophical Review* 77 (1968), [doi:10.2307/2183569](https://doi.org/10.2307/2183569); A. Grzegorczyk, "The Paradox of Grelling and Nelson Presented as a Veridical Observation Concerning Naming" (1998), pp. 183–190, [doi:10.1007/978-94-011-5108-5_15](https://doi.org/10.1007/978-94-011-5108-5_15); J. Ketland, "Jacquette on Grelling's Paradox", *Analysis* 65 (2005), pp. 258–260, [doi:10.1093/analys/65.3.258](https://doi.org/10.1093/analys/65.3.258).

## Framings and reframings

- **Predicates instead of sets.** Bolander (§1.4): "Grelling’s paradox involves the predicate heterological, which is true of all those predicates that are not true of themselves." The extension is {P | P ∉ ext(P)} beside Russell's {x | x ∉ x}; his conclusion: "Thus in many cases it makes most sense to study the paradoxes of self-reference under one, rather than study, say, the semantic and set-theoretic paradoxes separately."
- **From paradox to limitation theorem.** Bolander (§2.4): "We call a Turing machine \(A\) heterological if \(A\) doesn’t halt on input \(\langle A\rangle\), that is, if \(A\) doesn’t halt when given its own Gödel code as input." Given a halting decider H, a machine G built from it is heterological exactly if it is not, so no such H exists.
- **A semantically flawed paradox.** Sorensen (§4) introduces Grelling as an example of paradoxes that "are semantically flawed (Sorensen 2003b, 352)", against reading every paradox as a set of propositions.
- **Toward Tarski.** Cantini & Bruni (§4.2) read Ramsey's relativised meaning relation as foreshadowing Tarski; see [Tarski](../thinkers/tarski.md).

## Vocabulary

- [Paradox](../vocabulary/paradox.md); [Validity](../vocabulary/validity.md);
  [Classical logic](../methods/classical-logic.md), in which the logic check
  above is run.
- Autological, heterological, extension, impredicative definition,
  predicative function, ramified type theory, meaning relation, halting
  problem — open work in [vocabulary](../vocabulary/index.md).
