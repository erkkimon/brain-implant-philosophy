---
type: article
about: person
title: Alfred Tarski
description: "Alfred Tarski (1901–1983), Polish logician, later at Berkeley: the 1933 truth monograph (Convention T, object language and metalanguage, the indefinability theorem), the hierarchy of languages as a response to the liar, and the 1936 model-theoretic definition of logical consequence."
tags: [thinker, logic, philosophy-of-language, truth, twentieth-century, tarski]
timestamp: 2026-10-08T19:52:29Z
---

# Alfred Tarski

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md) and [How claims are
graded](../../conventions/how-claims-are-graded.md); a hub in the [thinkers](index.md) branch.

## Facts a claim depends on

- **Dates.** Gómez-Torrente (SEP, Fall 2024, §1): "Tarski was born on January 14, 1901 in Warsaw, then a part
  of the Russian Empire" and "remained affiliated to Berkeley until his death, on October 27, 1983". O'Connor
  and Robertson (MacTutor, 2003) give "Died 26 October 1983 Berkeley, California, USA"; both dates recorded.
- **Name.** "His family name at birth was Tajtelbaum, changed to Tarski in 1923" (Gómez-Torrente, §1);
  MacTutor: "It was around 1923 that Alfred Teitelbaum changed his name to Alfred Tarski."
- **Teachers.** He studied at Warsaw "from 1918 to 1924, taking courses with Kotarbiński, Leśniewski,
  Łukasiewicz, Mazurkiewicz and Sierpiński among others"; "He got a doctoral degree, under Leśniewski’s
  supervision, in 1924" (Gómez-Torrente, §1).
- **Emigration.** "In August 1939 Tarski traveled to the United States to attend a congress of the Unity of
  Science movement" (Gómez-Torrente, §1; see [Vienna Circle](../schools/vienna-circle.md)). At Berkeley he
  "was eventually given tenure in 1945 and a professorship in mathematics in 1948" (Gómez-Torrente, §1);
  MacTutor dates the permanent post to 1942 and has him "becoming Professor of Mathematics in 1949"; both recorded.
- **Self-description.** Tarski "described himself as “a mathematician (as well as a logician, and perhaps a
  philosopher of a sort)” (1944, p. 369)" (Gómez-Torrente, preamble).

## Problems addressed

- **Truth — Convention T.** Hodges (SEP, Fall 2024, §1.3): "Tarski’s own name for this criterion of material
  adequacy was Convention T. More generally his name for his approach to defining truth, using this criterion,
  was the semantic conception of truth." Gómez-Torrente (§2) quotes the convention from the English text
  (Tarski 1983b, pp. 187–8): a definition of "Tr" is adequate if the metatheory proves every sentence
  "obtained from the expression “Tr(x) if and only if p” by substituting for the symbol “x” a
  structural-descriptive name of any sentence of the language in question and for the symbol “p” the
  expression which forms the translation of this sentence into the metalanguage". Beall, Glanzberg and Ripley
  (SEP "Liar Paradox", §2.2) call the resulting biconditional the T-schema: "The tradition, going back to
  Tarski (1935), is that the behavior of the truth predicate Tr is described by the following biconditional."
- **[The liar paradox](../problems/liar-paradox.md) — the hierarchy of languages.** "As Tarski himself
  emphasised, Convention T rapidly leads to the liar paradox if the language L has enough resources to talk
  about its own semantics"; "Tarski’s own conclusion was that a truth definition for a language L has to be
  given in a metalanguage which is essentially stronger than L" (Hodges, §1.3). Beall, Glanzberg and Ripley
  (§4.3.1): "Tarski concluded from the paradox that no language could contain its own truth predicate (in his
  terminology, no language can be ‘semantically closed’)"; "Instead, Tarski proposed that the truth predicate
  for a language is to be found only in an expanded metalanguage"; "There is no Liar paradox because there is
  no Liar sentence." Gómez-Torrente (§2) reports that the version Tarski used was "offered by Tarski (due to
  Łukasiewicz)" and that the predicate Tr "is always a predicate of a language (the metalanguage) different
  from the language of the sentences to which it applies (the object language)". Priest, Berto and Weber (SEP
  "Dialetheism", §3.2) add that "Tarski himself insisted that his solution is inapplicable to natural
  languages".
- **The undefinability (indefinability) theorem, 1933/1935.** Gómez-Torrente (§2) gives Theorem I from Tarski
  1983b, p. 247, part (b): "assuming that the class of all provable sentences of the metatheory is consistent,
  it is impossible to construct an adequate definition of truth in the sense of convention T on the basis of
  LGTC+". He reports that "In the postscript to the 1935 German translation of the monograph on truth, Tarski
  abandons the 1933 requirement that the apparatus of the metatheory be formalizable in finite type theory",
  and that one cannot define a truth predicate "“if the order of the metalanguage is at most equal to that of
  the language itself” (Tarski 1983b, p. 273)". Hodges (§1.3) draws the consequence for set theory: "by
  Tarski’s result this truth definition can’t be given in set theory itself."
- **Logical consequence, 1936.** Gómez-Torrente (§3) quotes condition (F) (Tarski 1983c, p. 415) — replacing
  the non-logical constants of premises K and conclusion X by any others, "the sentence X′ must be true
  provided only that all sentences of the class K′ are true" — and the definition: "A sentence X is a
  (Tarskian) logical consequence of the sentences in set K if and only if every model of the set K is also a
  model of sentence X (cf. Tarski 1983c, p. 417)." Beall, Restall and Sagi (SEP "Logical Consequence"): "The
  contemporary model-theoretic definition of logical consequence traces back to Tarski (1936)." See
  [validity](../vocabulary/validity.md) and [classical logic](../methods/classical-logic.md).

Structural note (G4, propositional logic only): Gómez-Torrente's liar reconstruction ends in "c is a true
sentence if and only if c is not a true sentence"; with *t* for "c is a true sentence", `logic.py` gives:

```
$ python3 _implant/skills/tools/logic.py check --premises "t <-> ~t" --conclusion "t & ~t"
  P1: t <-> ~t    [(t <-> ~t)]
  C:  t & ~t    [(t & ~t)]

VALID
premises are jointly inconsistent — argument is vacuously valid
```

This shows only that the biconditional is classically unsatisfiable; which premise to drop is what the
positions above dispute.

## Works

Titles and editions from Gómez-Torrente's bibliography; no [works](../works/index.md) pages yet.

- *Pojęcie prawdy w językach nauk dedukcyjnych* (Warsaw, 1933); German translation by L. Blaustein with a
  postscript, "Der Wahrheitsbegriff in den formalisierten Sprachen", *Studia Philosophica* 1 (1935): 261–405;
  English, "The Concept of Truth in Formalized Languages", trans. J. H. Woodger, in *Logic, Semantics,
  Metamathematics*, 2nd ed., ed. J. Corcoran (Hackett, 1983), pp. 152–278 ("1983b", the locator used here).
- "O pojęciu wynikania logicznego", *Przegląd Filozoficzny* 39 (1936): 58–68; German "Über den Begriff der
  logischen Folgerung" (1936); English "On the Concept of Logical Consequence", in the 1983 volume, pp. 409–20
  ("1983c"); English from the Polish, "On the Concept of Following Logically", trans. M. Stroińska and D.
  Hitchcock, *History and Philosophy of Logic* 23(3) (2002): 155–196, DOI:
  [10.1080/0144534021000036683](https://doi.org/10.1080/0144534021000036683).
- "The Semantic Conception of Truth: And the Foundations of Semantics", *Philosophy and Phenomenological
  Research* 4(3) (1944): 341–376, DOI: [10.2307/2102968](https://doi.org/10.2307/2102968) (bibliographic data
  verified by DOI; text not read here).
- Tarski–Vaught 1956: "In 1956 he and his colleague Robert Vaught published a revision of one of the 1933
  truth definitions, to serve as a truth definition for model-theoretic languages" (Hodges, preamble).

## In dialogue with

- **Russell and Whitehead, Zermelo:** before the monograph "there were no definitions of these notions in terms
  of concepts accepted in the foundational systems designed for the reconstruction of classical mathematics
  (for example, Russell and Whitehead’s theory of types or Zermelo’s set theory)" (Gómez-Torrente, §2); see
  [Russell's paradox](../problems/russells-paradox.md).
- **Kripke 1975:** "As Kripke notes, any syntactically fixed set of levels will make it extremely hard, if not
  impossible, to place various non-paradoxical claims within the hierarchy" (Beall, Glanzberg and Ripley,
  §4.3.1); Kripke 1975, DOI [10.2307/2024634](https://doi.org/10.2307/2024634) (bibliographic only).
- **[Priest](priest.md) and the dialetheists:** "Dialetheists agree, but draw the conclusion in the other
  direction: the appropriate formalization of a language such as ours, because it is semantically closed and
  is not hierarchically stratified, will be inconsistent (Priest 1987, Ch. 1, Beall 2009, Ch. 1)" (Priest,
  Berto and Weber, §3.2; Priest co-authors the entry).
- **[Curry's paradox](../problems/currys-paradox.md):** the SEP "Curry's Paradox" entry lists "Tarski’s
  hierarchical theory" among theories that "restrict the “naive” transparency principle (Truth)" (§4.1;
  excerpt: `raw/sep-curry-paradox-fall-2024-construction-lemma-and-responses.md`).
- **Vienna Circle / Quine:** Uebel (SEP "Vienna Circle", §3.2) reports that Quine's criticism of the
  analytic/synthetic distinction "can only be sustained by extending objections of a type first published by
  Tarski" (excerpt: `raw/sep-vienna-circle-fall-2024-members-and-doctrines.md`).

## Reception

- **Assessments of standing (attributed).** Gómez-Torrente (SEP, preamble) reports:
  "He is widely considered as one of the greatest logicians of the twentieth century (often regarded as second only to Gödel), and thus as one of the greatest logicians of all time."
  O'Connor and Robertson (MacTutor, 2003):
  "Tarski is recognised as one of the four greatest logicians of all time, the other three being Aristotle, Frege, and Gödel."
- **For the hierarchy (as reported).** Beall, Glanzberg and Ripley (§4.3.1) call it "Traditionally, the main
  avenue for resolving the paradox within classical logic" (excerpt:
  `raw/sep-sorites-and-liar-fall-2024-paradox-formulations-and-responses.md`); in it a truth predicate for the
  language below "obeys capture and release, and yields no paradox" (§4.3.1).
- **Against the hierarchy (as reported).** Beall, Glanzberg and Ripley (§4.3.1):
  "his ruling Liar sentences syntactically not well-formed seems overly drastic";
  "many have concluded that Tarski’s hierarchy of languages and metalanguages buys a solution to the Liar paradox at the cost of implausible restrictiveness";
  and (§4.1.3) non-classical approaches aim to avoid Tarski's conclusion,
  "which many have seen as far too drastic."
  The same authors add that "how successful these approaches have been in this regard remains a highly
  contentious issue" (§4.1.3).
- **On the definition of consequence.** For: Beall, Restall and Sagi trace "The contemporary model-theoretic
  definition of logical consequence" to Tarski (1936). Against: they report that on Etchemendy's (1990) two
  readings of models, "The interpretational approach, by looking only at the actual world fails to account for
  necessity, and the representational approach fails to account for formality" (Etchemendy, "Tarski on Truth
  and Logical Consequence", *Journal of Symbolic Logic* 53(1) (1988): 51–79, DOI:
  [10.2307/2274427](https://doi.org/10.2307/2274427), is listed by Gómez-Torrente, §5; bibliographic only).
  Reply: "A possible response to Etchemendy would be to blend the representational and the interpretational
  perspectives" (Shapiro 1998). Tarski himself did not think the 1936 construction "completely solved the
  problem of offering “a materially adequate definition of the concept of consequence”", naming "the division
  of all terms of the language discussed into logical and extra-logical" (Gómez-Torrente, §4; Tarski 1983c,
  p. 418).

## Vocabulary

*Object language* and *metalanguage*; *semantically closed*; *Convention T* / *T-schema*; *material adequacy*
— Hodges (§1.3) notes that Tarski's Polish word "trafny" is rendered "materially adequate" and that "a better
translation would be ‘accurate’"; *logical consequence* in the model-theoretic sense (compare this implant's
[validity](../vocabulary/validity.md)); *antinomy* for [paradox](../vocabulary/paradox.md). No descriptive
entries yet ([vocabulary](../vocabulary/index.md)).

Related problems: [the knower paradox](../problems/knower-paradox.md) (Bolander §2.3: Montague's theorem generalises Tarski's), [Quine's paradox](../problems/quines-paradox.md).

Related thinkers: [Russell](russell.md).
