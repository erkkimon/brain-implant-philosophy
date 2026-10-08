---
type: article
about: concept
title: "The Epimenides paradox"
description: "A Cretan says that Cretans are always liars: is what he says true? The saying in Titus 1:12, Clement and Callimachus; Fowler's 1869 alternation and Russell's 1908 'oldest contradiction'; the observation, reported by Spade & Read (SEP) with Prior 1958, that the sentence can be consistently false; and the name it lends to the liar paradox."
tags: [problem, paradox, logic, self-reference, truth]
timestamp: 2026-10-08T19:52:29Z
---

# The Epimenides paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Primary texts: Titus 1:12–13 (KJV), Clement of Alexandria, *Stromata* I.14, and Callimachus, *Hymn I*
(excerpts: `raw/cretans-always-liars-titus-clement-callimachus.md`); Fowler, *The Elements of Deductive Logic*, 3rd ed. 1869, p. 163
([archive.org](https://archive.org/details/elementsdeducti08fowlgoog); excerpt: `raw/fowler-1869-deductive-logic-epimenides.md`);
Russell, "Mathematical Logic as Based on the Theory of Types", 1908 ([doi:10.2307/2369948](https://doi.org/10.2307/2369948);
excerpt: `raw/russell-1908-theory-of-types-epimenides.md`).
Maps: Spade & Read, [SEP Fall 2024 "Insolubles"](https://plato.stanford.edu/archives/fall2024/entries/insolubles/) §1.2 and note 5
(excerpt: `raw/sep-insolubles-fall-2024-epimenides-titus-and-prior.md`);
Beall, Glanzberg & Ripley, [SEP Fall 2024 "Liar Paradox"](https://plato.stanford.edu/archives/fall2024/entries/liar-paradox/)
preamble and note 1 (excerpt: `raw/sep-liar-paradox-fall-2024-epimenides-and-new-testament.md`);
Dowden, [IEP "Liar Paradox"](https://iep.utm.edu/par-liar/) §3d (excerpt: `raw/iep-liar-paradox-dowden-prior-simply-false.md`).
Admitted from Wikipedia's [List of paradoxes, revision 1376699902](https://en.wikipedia.org/w/index.php?title=List_of_paradoxes&oldid=1376699902),
"Logic" (excerpt: `raw/wikipedia-epimenides-paradox-rev-1376530197-and-list-entry.md`).
The parent problem is [the liar paradox](liar-paradox.md).

## The question

The saying, as Titus quotes it: "1:12 One of themselves, even a prophet of their own, said, The Cretians are alway liars, evil beasts, slow bellies." (Titus 1:12, KJV).
Clement names the prophet: "others, Epimenides the Cretan, whom Paul knew as a Greek prophet, whom he mentions in the Epistle to Titus" (*Stromata* I.14, tr. Wilson).
Wikipedia's list gives it as: "Epimenides paradox: A Cretan says: "All Cretans are liars". This paradox works in mainly the same way as the liar paradox." (rev. 1376699902).
The question is whether a Cretan who says this says something true. Russell's 1908 statement adds a condition: "Epimenides the Cretan said that all Cretans were liars, and all other statements made by Cretans were certainly lies. Was this a lie?" (p. 222).

**Propositional check (this implant, 2026-10-02; logic, not a position).**
Let *S* stand for *Epimenides' statement is true* and *O* for *some other Cretan statement is true*.
Reading the statement as *every Cretan statement is a lie*, and since it is itself a Cretan statement, *S* holds just when neither it nor any other Cretan statement is true: `S <-> (~S & ~O)`.
`logic.py check --premises "S <-> (~S & ~O)" --conclusion "S & ~S"` outputs `INVALID` with the counterexample row `O=T, S=F` (`(1 counterexample row)`): the premise is consistent, with the statement false and some other Cretan statement true.
With the same premise, conclusion `"~S"` outputs `VALID`, and conclusion `"O"` outputs `VALID`.
Adding Russell's condition as `"~O"` (no other Cretan statement is true), the premises `"S <-> (~S & ~O)" "~O"` against `"S & ~S"` output `VALID` and `premises are jointly inconsistent — argument is vacuously valid`, the same output the tool gives for the bare liar form `"S <-> ~S"`.
The tool is propositional: it takes the reading of *liars* as *every statement false* and the self-application as given, and does not model the quantifier over Cretans or times.

## Why it matters

- **It names the liar.** Beall, Glanzberg & Ripley: "The paradox is sometimes called the ‘Epimenides paradox’ as the tradition attributes a sentence like the first one in this essay to Epimenides of Crete, who is reputed to have said that all Cretans are always liars." (SEP, preamble). Spade & Read: "For this reason, the Liar Paradox is nowadays sometimes referred to as the “Epimenides”." (SEP "Insolubles" §1.2). See [the liar paradox](liar-paradox.md).
- **Whether it is a liar at all.** Spade & Read: "It is sometimes observed that Epimenides’s statement is not really a paradox of the Liar type at all." (note 5). The check in The question shows the propositional difference between the two forms.
- **A text that went unremarked.** Spade & Read: "Yet, blatant as the paradox is here, and authoritative as the Epistle was taken to be, not a single medieval author is known to have discussed or even acknowledged the logical and semantic problems this text poses." and "It is not known who was the first to link this text with the Liar Paradox." (§1.2).
- **A starting point for type theory.** Russell opens his list of contradictions with it: "The oldest contradiction of the kind in question is the Epimenides." (1908, p. 222), and names the shared feature: "there is a common characteristic, which we may describe as self-reference or reflexiveness. The remark of Epimenides must include itself in its own scope" (p. 224).

## Positions taken

No grouping of answers to the Epimenides was found in the sources read; the answers on record are listed by owner, unranked.

- **It yields an endless alternation (Fowler 1869).** "Thus we may go on alternately proving that Epimenides and the Cretans are truthful and untruthful." (p. 163). Fowler sets it among examples for the reader and labels it "(Fallacy of Mentiens.)" (raw file, context).
- **It is not a contradiction; the statement is false (the observation reported by Spade & Read).** "If he did say “The Cretans [i.e., all Cretans] are always liars, evil beasts, slow bellies”, then his statement is true only if it is false, since he himself is a Cretan and so always lying. Thus it cannot be true. But if it is false, all that follows is that some Cretans are not always liars and evil beasts and slow bellies. It does not follow that Epimenides’s own remark is not a lie, and so it does not follow that it is not false." (note 5). Spade & Read's assessment: "This much is correct about what Epimenides said." (note 5). Wikipedia's article states the same view in its own voice: "It is often claimed that a paradox of self-reference arises when one considers whether it is possible for Epimenides to have spoken the truth, but in fact there is no paradox because it may simply be a false statement." (rev. 1376530197, lead; no reference given for the sentence).
- **The puzzle is what follows from it (Prior 1958, as reported by Spade & Read).** "(or at least, no contradiction; the paradox or puzzle, as Prior 1958 pointed out, is that we can infer from his statement the surprising fact that at least one Cretan utterance is true)" (note 5). Prior's paper, "Epimenides the Cretan", *Journal of Symbolic Logic* 23(3), 1958, pp. 261–266 ([doi:10.2307/2964285](https://doi.org/10.2307/2964285)), was not read here (record: `raw/prior-1958-epimenides-the-cretan-bibliographic-record.md`). Dowden reports a related position of Prior's on the liar sentence in general: "Arthur Prior, following the informal suggestions of Jean Buridan and C. S. Peirce, takes this way out and concludes that the Liar Sentence is simply false." (IEP §3d).
- **With every other Cretan statement a lie, it is a liar (Russell 1908).** Russell's version adds "and all other statements made by Cretans were certainly lies" and pairs it with "The simplest form of this contradiction is afforded by the man who says " I am lying;" if he is lying, he is speaking the truth, and vice versa." (p. 222). His treatment by orders of propositions: "Thus, e.g., if Epimenides asserts "all first-order propositions affirmed by me are false," he asserts a second-order proposition ; he may assert this truly, without asserting truly any first-order proposition, and thus no contradiction arises." (p. 238).
- **Read with the next verse, it becomes a liar (Spade & Read on Titus 1:13).** "But St. Paul (or whoever wrote the epistle) goes on to say in the very next verse (Titus 1:13) “This witness is true”. Hence there was ample opportunity for a reader of this text to be introduced to the Liar Paradox, even if he did not already know about it." (note 5). Beall, Glanzberg & Ripley: "Thus, a paradox nearly occurs in the New Testament." (note 1, pointing to Anderson 1970, not read here).

## Arguments in play

(none recorded as separate argument pages yet). Two derivations are on record.
The alternation: Fowler's chain from "Epimenides is himself a Cretan ; therefore he is himself a liar" back to "the Cretans are liars" (p. 163).
The one-way derivation: Spade & Read's "true only if it is false" with "Thus it cannot be true", but falsity giving only "some Cretans are not always liars" (note 5).
The propositional core of both is checked in The question; the difference turns on whether the premise `~O` is present, which is Russell's added condition (structural note, this implant).
The words "always" and "liars" carry the argument: the check reads *liar* as one whose every statement is false; the SEP authors note that "Lying is a complicated matter, but what’s puzzling about sentences like the first one of this essay isn’t essentially tied to intentions, social norms, or anything like that." (Beall, Glanzberg & Ripley, preamble), and Wikipedia's article reads the negation as "being untrue only means "Not all Cretans are liars" instead of the assumption that "All Cretans are honest"" (rev. 1376530197, "Logical paradox").

## Thinkers who addressed it

- **Epimenides of Crete** — the reputed author of the saying, "traditionally said to have been the sixth-century BCE thinker" (Spade & Read, §1.2); attribution in Clement (*Stromata* I.14) and in Mair's note to Callimachus ("This proverbial saying, attributed to Epimenides, is quoted by St. Paul.").
- **Callimachus** (*Hymn I, To Zeus*) — uses the saying of the Cretan tomb of Zeus: "did these or those, O Father lie? “Cretans are ever liars.” Yea, a tomb, O Lord, for thee the Cretans builded; but thou didst not die, for thou art for ever." (tr. Mair).
- **The author of the Epistle to Titus** — quotes it and adds "1:13 This witness is true." (KJV).
- **Clement of Alexandria** — identifies the prophet as Epimenides (*Stromata* I.14).
- **Thomas Fowler** (1869) — states the alternation as an exercise (p. 163).
- **Bertrand Russell** (1908) — the Epimenides as "The oldest contradiction of the kind in question" (p. 222), treated by the theory of types.
- **A. N. Prior** (1958) — the inference to a true Cretan utterance, as reported in SEP "Insolubles" note 5; text not read.
- **Paul Vincent Spade & Stephen Read** (SEP, rev. 2021) and **Jc Beall, Michael Glanzberg & David Ripley** (SEP, rev. 2016) — the assessments quoted above.
- For the liar in general see [Eubulides](../thinkers/eubulides.md), [Tarski](../thinkers/tarski.md) and [Priest](../thinkers/priest.md), via [the liar paradox](liar-paradox.md).

## Framings and reframings

- **A paradox, or a false statement?** Wikipedia's list says it "works in mainly the same way as the liar paradox" (rev. 1376699902); Spade & Read report that "It is sometimes observed that Epimenides’s statement is not really a paradox of the Liar type at all." (note 5). Both are on record; the check in The question gives the propositional condition under which each reading holds.
- **A theological saying.** In Callimachus the saying concerns the Cretan claim of a tomb of Zeus; Mair's note: "The Cretan legend was that Zeus was a prince who was slain by a wild boar and buried in Crete." (tr. Mair, note).
- **When it became a logical puzzle.** Spade & Read report the medieval silence (§1.2). Wikipedia's article: "Finally, in 1740, the second volume of Pierre Bayle's Dictionnaire Historique et Critique explicitly connects Epimenides with the paradox, though Bayle labels it a "sophisme"." (rev. 1376530197; Bayle not read here).
- **Not tied to lying.** Beall, Glanzberg & Ripley move from Epimenides to sentences that say of themselves that they are false, a puzzle they say is not "essentially tied to intentions, social norms, or anything like that" (preamble).

Not in the excerpts held: Prior 1958 and 1961 at first hand, Anderson 1970, Sorensen 2003, Bayle 1740,
Rendel Harris's 1906–1907 *Expositor* notes and the Theodore of Mopsuestia commentary cited by Wikipedia's article; they are left out until a source is read.

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — and the question whether this case is one.
- [Validity](../vocabulary/validity.md) — the propositional check above.
- [Classical logic](../methods/classical-logic.md) — the logic of the check.
- *Liar* (one whose every statement is false, in the check's reading), *self-reference or reflexiveness* (Russell, p. 224), *insoluble* (SEP "Insolubles") — open work in [vocabulary](../vocabulary/index.md).

Related thinkers: [Russell](../thinkers/russell.md).
