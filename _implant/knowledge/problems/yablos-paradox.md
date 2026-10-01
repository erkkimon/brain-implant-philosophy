---
type: article
about: concept
title: "Yablo's paradox"
description: "An infinite sequence of sentences, each saying that every later sentence is untrue, yields a liar-like contradiction — Yablo's 1993 note 'Paradox without Self-Reference' presents it as paradox without circularity; Priest (1997) argues it is self-referential; the debate (Sorensen 1998, Beall 2001, Cook 2006, 2014), the graph-theoretic framing of non-wellfoundedness, and the infinitary and compactness points the SEP records."
tags: [problem, paradox, logic, self-reference, truth, circularity]
timestamp: 2026-10-01T22:52:16Z
---

# Yablo's paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Primary text: Stephen Yablo, "Paradox without Self-Reference", *Analysis*
53(4), 1993, pp. 251–252, [doi:10.1093/analys/53.4.251](https://doi.org/10.1093/analys/53.4.251),
author's copy [mit.edu/~yablo/pwsr.pdf](https://www.mit.edu/~yablo/pwsr.pdf)
(excerpt: `raw/yablo-1993-paradox-without-self-reference.md`).
Maps: Beall, Glanzberg & Ripley, [SEP Fall 2024 "Liar Paradox"](https://plato.stanford.edu/archives/fall2024/entries/liar-paradox/)
§§1.3, 2.1 (excerpt: `raw/sep-liar-paradox-fall-2024-yablos-paradox.md`);
Bolander, [SEP Fall 2024 "Self-Reference and Paradox"](https://plato.stanford.edu/archives/fall2024/entries/self-reference/)
§§1.6, 3.1 (excerpt: `raw/sep-self-reference-fall-2024-yablos-paradox.md`).
Admitted from Wikipedia's [List of paradoxes, revision 1376699902](https://en.wikipedia.org/w/index.php?title=List_of_paradoxes&oldid=1376699902),
"Logic" (excerpt: `raw/wikipedia-list-of-paradoxes-yablos-paradox-entry.md`).

## The question

Yablo (1993, p. 251): "Imagine an infinite sequence of sentences S1, S2, S3,....., each to the effect that every subsequent sentence is untrue:"
the first is "(S1) for all k >1, Sk is untrue", and so on. His derivation (p. 252): "Suppose for contradiction that some Sn is true. Given what Sn says, for all k>n, Sk is untrue. Therefore (a) Sn+1 is untrue, and (b) for all k>n+1, Sk is untrue. By (b), what Sn+1 says is in fact the case, whence contrary to (a) Sn+1 is true! So every sentence Sn in the sequence is untrue. But then the sentences subsequent to any given Sn are all untrue, whence Sn is true after all! I conclude that self-reference is neither necessary nor sufficient for Liar-like paradox."
Beall, Glanzberg & Ripley (SEP, §1.3) summarise: "(In other words, each claim says of the rest that they’re all untrue.)", and conclude for the first claim "if A0 (the first claim in the infinite sequence) is true or untrue, then it is both." The Wikipedia list's wording: "An ordered infinite sequence of sentences, each of which says that all following sentences are false."

The question is whether this is a [liar](liar-paradox.md)-like paradox
without circularity, as Yablo says, and if so what that shows about the
sources of semantic paradox. The term contracts are
[paradox](../vocabulary/paradox.md) and [validity](../vocabulary/validity.md).

**Logic check (this implant, 2026-10-02; logic, not a position).** The
first half of Yablo's derivation has a propositional core. Let `n` = *Sn is
true*, `m` = *Sn+1 is true*, `r` = *for all k>n+1, Sk is untrue*. Sn says
`~m & r`; Sn+1 says `r`. `logic.py check --premises "n <-> (~m & r)" "m <-> r" --conclusion "~n"`
outputs "VALID". The second half ("every sentence Sn in the sequence is
untrue", hence Sn true) quantifies over infinitely many sentences and is not
expressible in the tool's propositional language. A *finite truncation*
(three sentences, the last referring to nothing, so vacuously true:
premises `s1 <-> (~s2 & ~s3)`, `s2 <-> ~s3`, `s3`) is a different, finite
object: with conclusion `s3 & ~s2 & ~s1` the tool outputs "VALID", and
with conclusion `s1` it outputs "INVALID" with counterexample
"s1=F, s2=F, s3=T" — one assignment satisfies all three premises, so the
truncation is consistent. This matches Bolander's statement (SEP, §1.6) that "Any finitary variant of Yablo’s sequence—where every sentence only refers to finitely many later sentences in the sequence—must necessarily be consistent (non-paradoxical) due to the compactness theorem in propositional logic"; the check is an illustration of one case, not a proof of that statement.

## Why it matters

- **Self-reference as the received diagnosis.** Yablo (1993, p. 251): "Why are some sentences paradoxical while others are not? Since Russell the universal answer has been: circularity, and more especially self-reference." He reports the view "that some sort of self-reference, be it direct or mediated, is necessary for paradox."
- **Liar cycles versus the sequence.** Beall, Glanzberg & Ripley (§1.3): "Liar cycles (e.g., the Max–Agnes dialog) show that explicit self-reference is not necessary, but it is clear that such cycles themselves involve circular reference. Yablo (1993b) has argued that a more complicated kind of multi-sentence paradox produces a Liar without circularity." Their §2.1 sets it aside when discussing ingredients: "Putting aside Yablo-type paradoxes, the Liar relies on some form of self-reference, either direct, as in in the simple Liars above, or indirect, as in Liar cycles."
- **Hierarchy solutions.** Bolander (§3.1) holds that such paradoxes "can also be blocked by a hierarchy approach, but it is necessary to further require the hierarchy to be well-founded, that is, to have a lowest level." He adds: "For instance, Yablo’s paradox may be formalised in a descending hierarchy of languages."
- **Which structures are paradoxical.** Bolander (§1.6): "A complete characterisation is still an open problem (Rabern, Rabern and Macauley, 2013), but it seems to be a relatively widespread conjecture that all paradoxical graphs of reference are either cyclic or contain a Yablo-like structure."

## Positions taken

Not ranked; each is reported with the source that records it. The SEP
entry lists the debate: "Whether Yablo’s paradox really avoids self-reference is much-debated. See, for instance, Barrio (2012), Beall (2001), Cook (2006, 2014), Ojea (2012), Picollo (2012), Priest (1997), Sorensen (1998), and Teijeiro (2012)." (Beall, Glanzberg & Ripley, §1.3).

- **Not circular in any way (Yablo 1993).** "This note gives an example of a Liar-like paradox that is not in any way circular." (p. 251, n. 1). Bolander (§1.6) reports: "Yablo (1993) himself argues that it is non-self-referential".
- **Self-referential after all (Priest 1997).** Bolander (§1.6) reports that "Priest (1997) argues that it is self-referential." Priest, "Yablo's paradox", *Analysis* 57(4), 1997, pp. 236–242, [doi:10.1093/analys/57.4.236](https://doi.org/10.1093/analys/57.4.236); not read, reported here only through Bolander. See [Graham Priest](../thinkers/priest.md).
- **Other Yablo-like paradoxes are not self-referential in Priest's sense (Butler 2017).** Bolander (§1.6): "Butler (2017) claims that even if Priest is correct, there will be other Yablo-like paradoxes that are not self-referential in the sense of Priest."
- **Circular, but not in a sense that bears the blame (Cook 2014).** The abstract of Cook's book: "although the original formulation of the Yablo paradox is circular, it turns out that it is not so in any sense that can bear the blame for the paradox. Further, formulations of the paradox using infinitary conjunction provide genuinely non-circular constructions." Cook's 2006 paper is titled "There are non-circular paradoxes (but Yablo's isn't one of them)" (as listed by the SEP, *The Monist* 89(1): 118–149).
- **Contributions not read here.** Sorensen, "Yablo's paradox and kindred infinite Liars", *Mind* 107(425), 1998, pp. 137–155, [doi:10.1093/mind/107.425.137](https://doi.org/10.1093/mind/107.425.137); Beall, "Is Yablo's paradox non-circular?", *Analysis* 61(3), 2001, pp. 176–187, [doi:10.1093/analys/61.3.176](https://doi.org/10.1093/analys/61.3.176). Both are on the SEP's list above; their positions are not reported here because no read source states them.

**Cases for and against.** For the non-circular reading, Yablo's own
derivation and footnote above, and Bolander's description (§1.6) of an
"acyclic, but non-wellfounded" reference structure. Against it, Priest's
argument as Bolander reports it, and Cook's finding (abstract) that the
original formulation is circular. The sources read do not reproduce the
steps of Priest's, Sorensen's or Beall's arguments; none is reproduced here.
No survey figure is recorded.

## Arguments in play

(none as separate argument pages yet). Related problems:
[the liar paradox](liar-paradox.md), of which the SEP treats it as a
multi-sentence form; [the Berry paradox](berry-paradox.md), which Bolander
files with the liar among semantic paradoxes; [Curry's paradox](currys-paradox.md),
with which Cook's book closes ("connections between the Yablo paradox and
the Curry paradox", abstract). Siblings: [the card paradox](card-paradox.md)
and [the no-no paradox](no-no-paradox.md), which the Wikipedia list places
beside it under the liar.

## Thinkers who addressed it

- **Stephen Yablo** — the ω-liar in "Truth and reflection" (*Journal of Philosophical Logic* 14(3), 1985, pp. 297–349, per Bolander's bibliography); Bolander (§1.6): "In 1985, Yablo succeeded in constructing a semantic paradox that does not involve self-reference at all, not even indirect self-reference." The two-page note of 1993 (above). Bolander (§1.6): "as shown by Yablo (2006), similar set-theoretic paradoxes involving no self-reference can be formulated in certain set theories."
- **Graham Priest** (1997) — argues it is self-referential, per Bolander (§1.6). See [Priest](../thinkers/priest.md).
- **Roy Sorensen** (1998) and **Jc Beall** (2001) — contributions to the circularity debate, per Beall, Glanzberg & Ripley (§1.3); not read.
- **Roy T. Cook** (2006; 2014, *The Yablo Paradox*, OUP, [doi:10.1093/acprof:oso/9780199669608.001.0001](https://doi.org/10.1093/acprof:oso/9780199669608.001.0001), abstract read; excerpt: `raw/cook-2014-yablo-paradox-book-abstract.md`) — the three questions below.
- **Lavinia Picollo** (2012, 2013) — formalisation in arithmetic: "How and whether the Yablo paradox can truthfully be represented this way, and how it relates to compactness of the underlying logic, has been investigated by Picollo (2013)." (Bolander §1.6).
- **Barrio, Ojea, Teijeiro** (2012) — on the SEP liar entry's list; not read.
- **Butler** (2017), **Halbach and Zhang** (2017) — cited by Bolander (§1.6) in the self-reference discussion.
- **Thomas Bolander** (SEP 2008, rev. 2024) — the encyclopedia framing as non-wellfoundedness (below).

## Framings and reframings

- **Paradoxes of non-wellfoundedness (Bolander).** Bolander's assessment (§1.6): "Yablo’s paradox demonstrates that we can have logical paradoxes without self-reference—only a certain kind of non-wellfoundedness is needed to obtain a contradiction." And: "The ordinary paradoxes of self-reference involve a cyclic structure of reference, whereas Yablo’s paradox involve an acyclic, but non-wellfounded, structure of reference." He proposes: "When solving paradoxes we might thus choose to consider them all under one, and refer to them as paradoxes of non-wellfoundedness."
- **Infinitary logic.** Bolander (§1.6): "To formalise it in a setting of propositional logic, it is hence necessary to use infinitary propositional logic"; see the finitary point under The question.
- **Three questions (Cook 2014).** The abstract names "the Characterization Problem: What patterns of sentential reference (circular or not) generate semantic paradoxes?", "the Circularity Question: Is the Yablo paradox genuinely non-circular?" and "the Generalizability Question: Can the Yabloesque pattern be used to generate genuinely non-circular variants of other paradoxes, such as epistemic and set-theoretic paradoxes?" On the last it reports: "Although there are general constructions—unwindings—that transform circular constructions into Yablo-like sequences, it turns out that these sorts of construction are not “well-behaved” when transferred from semantic puzzles to puzzles of other sorts."
- **Beyond truth.** Bolander (§1.6): "Yabloesque" variants in epistemic game theory (Başkent 2016), for provability (Cieśliński and Urbaniak 2013) and around Gödel's theorems (Leach-Krouse).

## Vocabulary

- [Paradox](../vocabulary/paradox.md); [Validity](../vocabulary/validity.md);
  [Classical logic](../methods/classical-logic.md), in which the logic check
  above is run.
- Self-reference, circularity, well-foundedness, reference graph,
  compactness, infinitary logic, ω-liar — open work in
  [vocabulary](../vocabulary/index.md).
