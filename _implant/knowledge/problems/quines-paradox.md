---
type: article
about: concept
title: "Quine's paradox"
description: "Quine's 1962 sentence that says of itself, without 'this sentence', that it is false — a nine-word phrase put down twice, the first time in quotation marks; Quine's subscript hierarchy as the response, its non-theorem twin as a route to Gödel's proof, the diagonal lemma, and later readings (Boolos, Hofstadter, Dowden)."
tags: [problem, paradox, logic, self-reference, truth, philosophy-of-language]
timestamp: 2026-10-08T19:52:29Z
---

# Quine's paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Primary text: W. V. Quine, "The Ways of Paradox", ch. 1 of *The Ways of
Paradox and Other Essays*, rev. ed., Harvard University Press, 1976 (ISBN
0-674-94835-1; first ed. 1966), first published as "Paradox", *Scientific
American* 206(4), 1962, pp. 84–96, [doi:10.1038/scientificamerican0462-84](https://doi.org/10.1038/scientificamerican0462-84);
copy read at [math.dartmouth.edu](http://web.archive.org/web/20251226013800/https://math.dartmouth.edu/~matc/Readers/HowManyAngels/Paradox.html)
(excerpt: `raw/quine-1962-1976-ways-of-paradox-quotation-antinomy.md`; the
copy shows no page numbers, so Quine is located by his section headings).
Maps: Bolander, [SEP Fall 2024 "Self-Reference and Paradox"](https://plato.stanford.edu/archives/fall2024/entries/self-reference/);
Raatikainen, [SEP Fall 2024 "Gödel's Incompleteness Theorems"](https://plato.stanford.edu/archives/fall2024/entries/goedel-incompleteness/);
Beall, Glanzberg & Ripley, [SEP Fall 2024 "Liar Paradox"](https://plato.stanford.edu/archives/fall2024/entries/liar-paradox/)
(excerpt: `raw/sep-self-reference-goedel-liar-fall-2024-quines-paradox.md`);
Dowden, [IEP "Liar Paradox"](https://iep.utm.edu/par-liar/)
(excerpt: `raw/iep-dowden-liar-paradox-quine-tarski-hierarchy.md`).
Admitted from Wikipedia's [List of paradoxes, revision 1376699902](https://en.wikipedia.org/w/index.php?title=List_of_paradoxes&oldid=1376699902),
"Logic" (excerpt: `raw/wikipedia-list-of-paradoxes-quines-paradox-entry.md`).

## The question

Quine (1962/1976, "The Paradox of Epimenides") starts from the liar in the
form "This sentence is false", of which he writes: "Here we seem to have the irreducible essence of antinomy: a sentence that is true if and only if it is false."
He reports a protest against it — "it has been protested that the phrase ‘This sentence', so used, refers to nothing" — and that substituting a quotation for the phrase yields a sentence that "attributes falsity no longer to itself but merely to something other than itself, thereby engendering no paradox."
His reply is a sentence that "does attribute falsity unequivocally to itself":

> ‘‘Yields a falsehood when appended to its own quotation' yields a falsehood when appended to its own quotation'.

Quine's own gloss: "This sentence specifies a string of nine words and says of this string that if you put it down twice, with quotation marks around the first of the two occurrences, the result is false. But that result is the very sentence that is doing the telling. The sentence is true if and only if it is false, and we have our antinomy."
Wikipedia's article words it "yields falsehood when preceded by its quotation" (rev. 1342778228); the list entry says it "Shows that a sentence can be paradoxical even if it is not self-referring and does not use demonstratives or indexicals." (rev. 1376699902), a gloss without its own citation there.

*Count (this implant, 2026-10-02; arithmetic, not a position):* yields, a,
falsehood, when, appended, to, its, own, quotation — 9 words, as Quine says.

The question is what the sentence shows about truth, quotation and
self-reference, and what a response must give up. Term contracts:
[paradox](../vocabulary/paradox.md), [validity](../vocabulary/validity.md).

**Logic check (this implant, 2026-10-02; logic, not a position).** Let `q` =
*Quine's sentence is true*. Quine's gloss gives `q <-> ~q`.
`logic.py check --premises "q <-> ~q" --conclusion "q & ~q"` outputs
"VALID" and "premises are jointly inconsistent — argument is vacuously valid".
The tool does not decide which assumption behind the biconditional a
response drops; the positions below differ on that.

## Why it matters

- **Against the "this sentence" diagnosis.** Quine (1962/1976) builds the sentence as the answer to the protest that the phrase ‘This sentence' "refers to nothing" (quoted above).
- **A family of semantic antinomies.** Quine calls it "a genuine antinomy, on a par with the one about ‘heterological'"; it "turns merely on ‘true', through the construct ‘falsehood', or ‘statement not true'." He groups "Grelling's antinomy and Berry's and the Epimenides as all in a family, to which Russell's antinomy does not belong", since "these strike at the semantics of truth and denotation" ("Russell's Antinomy").
- **Gödel's proof.** Quine writes that "Gödel's proof may conveniently be related to the Epimenides paradox or the pseudomenon in the ‘yields a falsehood' version." (see Framings).

## Positions taken

Not ranked; each is reported with the source that records it.

- **Stop applying truth locutions to expressions containing them (Quine 1962/1976).** Quine lists, as one way out, "ceasing to use ‘true of' and ‘true' and their equivalents and derivatives, or at any rate ceasing to apply such truth locutions to adjectives or sentences that themselves contain such truth locutions."
- **A subscripted hierarchy of truth locutions (Quine, after Russell and Tarski).** "This restriction can be relaxed somewhat by admitting a hierarchy of truth locutions, as suggested by the work of Bertrand Russell and Alfred Tarski." A truth locution's subscript must exceed any inside what it applies to; "Violations of this restriction would be treated as meaningless, or ungrammatical, rather than as true or false sentences." With subscripts "in ascending order", Quine's verdict on his sentence: "Thereupon paradox vanishes. This sentence is unequivocally false." — what it calls false1 "is not false1; it is meaningless" (excerpt, "The Paradox of Epimenides").
  Quine's own costing: "Either method is less economical than this method of subscripts."; "Each resort is desperate; each is an artificial departure from natural and established usage." Bolander (SEP 2024, §3.1) describes Tarski's hierarchy as one in which "a sentence such as the liar that expresses its own untruth cannot be formed."
- **Quotation itself is ambiguous (Boolos, after Michael Ernst).** As Wikipedia reports it: "George Boolos, inspired by his student Michael Ernst, has written that the sentence might be syntactically ambiguous, in using multiple quotation marks whose exact mate marks cannot be determined." (Boolos, "Quotational Ambiguity", in Leonardi & Santambrogio (eds.), *On Quine*, CUP 1995, ISBN 978-0-521-47091-9; *Logic, Logic, and Logic*, 1998, pp. 392–405; not read here).

**For and against the hierarchy.** For: Dowden (IEP) reports that "Quine defends Tarski’s way out as the best of the ways." and quotes Quine's hope that "truth locutions without implicit subscripts, or like safeguards, will really sound as nonsensical as the antinomies show them to be." Against: Dowden reports, without naming its owner, "One criticism of Quine is that he is asking us to be patient and not to be so bothered by the complexity of the hierarchy, but he is giving no other justification for the hierarchy."; he reports that Kripke (1975) "criticized Tarski’s way out for its inability to handle contingent versions of the Liar Paradox"; Bolander (SEP 2024, §3.1) reports that such a hierarchy "is today by most considered an overly drastic and heavy-handed approach." and that with it "so do all non-paradoxical occurrences of self-reference" disappear. Neither Boolos's response nor the first (no-truth-locution) option has a recorded objection in the sources read. No survey figure is recorded.

## Arguments in play

(none as separate argument pages yet). Related problems:
[the liar paradox](liar-paradox.md), of which Quine presents this as the
"most perverse version of the pseudomenon"; [the Berry paradox](berry-paradox.md),
which Quine (1962/1976) resolves by the same subscripts ("This resolution of Berry's antinomy is the one that would come through automatically if we paraphrase ‘specifiable' in terms of ‘true of' and then subject ‘true of' to the subscript treatment.");
[Russell's paradox](russells-paradox.md), which Quine puts in another family;
siblings in the same Wikipedia sub-list: [the Epimenides paradox](epimenides-paradox.md),
[the Grelling–Nelson paradox](grelling-nelson-paradox.md), [the card paradox](card-paradox.md),
[the no-no paradox](no-no-paradox.md), [Yablo's paradox](yablos-paradox.md),
which Bolander (SEP 2024, §1.6) says "does not involve self-reference at all, not even indirect self-reference."

## Thinkers who addressed it

- **W. V. Quine** — the sentence, its gloss and the subscript response (lecture, Akron, November 1961; *Scientific American* 1962; book 1966, rev. 1976, per the essay's headnote and the DOI record); also *Quiddities* (1987), "Paradoxes", pp. 145–149, cited by Wikipedia, not read.
- **[Alfred Tarski](../thinkers/tarski.md)** and **Bertrand Russell** — the hierarchy Quine says his subscripts are "suggested by the work of".
- **Kurt Gödel** — whose 1931 construction Quine relates to the sentence (Framings).
- **George Boolos** and **Michael Ernst** — quotational ambiguity, as Wikipedia reports (not read).
- **Douglas Hofstadter** (*Gödel, Escher, Bach*, Basic Books, 1979; not read) — per Wikipedia, "Douglas Hofstadter suggests that the Quine sentence in fact uses an indirect type of self-reference."
- **Bradley Dowden** (IEP) — reads Quine as defending Tarski's hierarchy; reports a criticism.

## Framings and reframings

- **The non-theorem twin (Quine).** "For ‘falsehood' read ‘non-theorem', thus:" — and the sentence, as printed in the copy read (its opening mark a double quote):

  > "Yields a non-theorem when appended to its own quotation' yields a non-theorem when appended to its own quotation'.

  Quine: "This statement no longer presents an antinomy, because it no longer says of itself that it is false." Then: "If it is true, here is one truth that that deductive theory, whatever it is, fails to include as a theorem. If the statement is false, it is a theorem, in which event that deductive theory has a false theorem and so is discredited."
  Gödel, on Quine's account, "shows how the sort of talk that occurs in the above statement — talk of non-theoremhood and of appending things to quotations — can be mirrored systematically in arithmetical talk of integers."; Quine's classification: "Gödel's discovery is not an antinomy but a veridical paradox."
  *Logic check (this implant, 2026-10-02; logic, not a position):* `g` = *the twin is true*, `t` = *it is a theorem*; the twin says `g <-> ~t`, soundness says `t -> g`. `logic.py check --premises "g <-> ~t" "t -> g" --conclusion "g & ~t"` outputs "VALID"; without `t -> g` it outputs "INVALID" with counterexample "g=F, t=T" — Quine's second horn, a false theorem.
- **The diagonal lemma.** Bolander (SEP 2024, §2.1) states it: "For every formula \(\phi(x)\) there is a sentence \(\psi\) such that \(S \vdash \psi \leftrightarrow \phi \langle \psi \rangle\)." for any theory extending first-order arithmetic; Gödel codes can be thought of "as a naming device or quotation mechanism for formulae—just like quotation marks in natural language." Of the sentence the lemma yields he writes it "is of course not self-referential in a strict sense, but mathematically it behaves like one." Raatikainen (SEP 2024, §2.4) says it is "sometimes also called “the self-referential lemma” or “the fixed point lemma”" and cautions that "says of itself" talk "may be heuristically useful, but they are also easily misleading and suggest too much."; per §5, "The general lemma was apparently first discovered by Carnap 1934 (see Gödel 1934, 1935)." Neither SEP entry names Quine's sentence; the comparison with it is Quine's (above).
- **Direct, indirect, or none.** Bolander (SEP 2024, §1.6) separates direct self-reference from indirect, "sentences that refer to other sentences that refer to yet other sentences in such a way as to form a loop back to the original sentence."; Beall, Glanzberg & Ripley (SEP 2024, §2.3.1): "Any language capable of expressing some basic syntax can generate self-referential sentences via so-called diagonalization". Wikipedia's list classes Quine's sentence as "not self-referring"; Quine says it does "attribute falsity unequivocally to itself"; Hofstadter, per Wikipedia, calls it indirect.

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — Bolander (SEP 2024, §1) defines one, citing Quine 1976, as "a seemingly sound piece of reasoning, based on apparently true assumptions, that still leads to a contradiction (Quine, 1976)."; Quine's own kinds are veridical, falsidical and antinomy. [Validity](../vocabulary/validity.md); [Classical logic](../methods/classical-logic.md), in which the logic checks above run.
- Antinomy, pseudomenon, truth locution, quotation, indexical, demonstrative, diagonal (fixed-point) lemma, Gödel numbering, hierarchy of languages — open work in [vocabulary](../vocabulary/index.md).

Related thinkers: [Russell](../thinkers/russell.md).
