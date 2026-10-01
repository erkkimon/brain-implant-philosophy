---
type: article
about: concept
title: "Bhartrhari's paradox (the unnameable)"
description: "If something is unnameable, calling it 'unnameable' seems to name it — so can anything be said to be unsayable? Bhartṛhari's Vākyapadīya 3.3.20–22 on the 'unsignifiable' (avācya), the Herzbergers' 'Unnameability Thesis' (1981) and its set-theoretic defence, Parsons's qualms (2001), Houben's communicative reading (1995) and Desnitskaya's activity-based reading of VP 3.3.26–28 (2006), side by side."
tags: [problem, paradox, logic, philosophy-of-language, self-reference, indian-philosophy]
timestamp: 2026-10-01T21:51:46Z
---

# Bhartrhari's paradox (the unnameable)

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Primary text: Bhartṛhari, *Vākyapadīya* (VP) book 3, chapter on relation
(*Sambandha-samuddeśa*), kārikās 3.3.19–28, Rau's numbering, Sanskrit as
printed by Desnitskaya 2006 and English as printed by Parsons 2001 (no
English translation of the chapter was read in full).
Scholarship read: Evgeniya A. Desnitskaya, "Antinomy of One and Many in Bhartṛhari's
Vākyapadīya", *Acta Orientalia Vilnensia* 7.1–2 (2006): 209–221,
[open PDF](https://www.journals.vu.lt/acta-orientalia-vilnensia/article/download/3761/5242)
(excerpt: `raw/desnitskaya-2006-bhartrharis-paradox-vp-3-3-20-28.md`);
Terence Parsons, "Bhartṛhari on What Cannot Be Said", *Philosophy East and West*
51(4), 2001, pp. 525–534, [doi:10.1353/pew.2001.0058](https://doi.org/10.1353/pew.2001.0058),
opening pages only (excerpt: `raw/parsons-2001-bhartrhari-on-what-cannot-be-said-opening.md`);
Subhash Kak, "Representation and Reasoning in Vedānta", *Studia Humana* 12(3), 2023,
[doi:10.2478/sh-2023-0012](https://doi.org/10.2478/sh-2023-0012)
(excerpt: `raw/kak-2023-vedanta-bhartrharis-paradox.md`).
The originating paper, Hans G. Herzberger and Radhika Herzberger, "Bhartrhari's paradox",
*Journal of Indian Philosophy* 9(1), 1981, [doi:10.1007/bf00202726](https://doi.org/10.1007/bf00202726),
was verified bibliographically only and is reported here as Parsons and
Desnitskaya report it (`raw/bhartrharis-paradox-bibliographic-records.md`).
No SEP or IEP entry on Bhartṛhari was found (both return 404).
Admitted from Wikipedia's List of paradoxes, revision 1376699902, "Logic"
(excerpt: `raw/wikipedia-bhartrharis-paradox-list-entry-trikandi-liar.md`).

## The question

Wikipedia's list entry: "Bhartrhari's paradox: The thesis that there are some things which are unnameable conflicts with the notion that something is named by calling it unnameable." (List of paradoxes, rev. 1376699902).
Kak's statement: "An example of the latter is the Bhartṛhari’s paradox [3] that if something is unnameable or unsignifiable (Sanskrit: avācya) it becomes nameable or signifiable precisely by calling it unnameable or unsignifiable." (Kak 2023, p. 15–16).

The kārikās, in the English Parsons prints (VP 3.3.20–21; Parsons 2001, p. 525):

- "SS 20. That which is signified as unsignifiable, if determined to have been signified through that unsignifiability, would then be signifiable."
- "SS 21. If 'unsignifiable' is being understood as not signifying anything, then its intended state has not been achieved."

The Sanskrit of 3.3.20 as Desnitskaya prints it (n. 25; her PDF's legacy
font renders ṃ as "ü"): "avācyam iti yad vācyaü tad avācyatayā yadā / vācyam ity avasīyeta vācyam eva tadā bhavet // 3.3.20 //".
Desnitskaya's paraphrase: "As a result, the question naturally arises whether to call something ‘insignifiable’ means to signify it. If yes, it would thus be apprehended as signifiable, otherwise there would be no understanding of the issue spoken about." (2006, p. 217).
The question, then: can a speaker say of something that it cannot be
signified, without thereby signifying it — and if not, what becomes of the
claim that some things (the readers below name relations) cannot be
signified?

**Propositional check (this implant, 2026-10-01; logic, not a position).**
For one object, let *u* stand for *it is unnameable* (read: it is not named),
*c* for *it is called "unnameable"*, and *n* for *it is named*. The list
entry's "notion" that calling it so names it is *c* -> *n*; the thesis read
of this object gives *u* -> ~*n*.
`logic.py check --premises "c" "c -> n" "u -> ~n" --conclusion "~u"` outputs `VALID`.
Adding *u* as a premise, `--premises "u" "c" "c -> n" "u -> ~n" --conclusion "n & ~n"`
outputs `VALID` and `premises are jointly inconsistent — argument is vacuously valid`.
Without *c* -> *n*, `--premises "c" "u -> ~n" --conclusion "~u"` outputs
`INVALID` with counterexample row `c=T, n=F, u=T`; and with *c* -> *n* but
without *u*, `--premises "c" "c -> n" "u -> ~n" --conclusion "n & ~n"`
outputs `INVALID` with row `c=T, n=T, u=F`. So the conflict depends on
the step from being called "unnameable" to being named. The tool treats
*naming* as one atom; it does not model the distinctions the readers below
draw (signifying vs denoting, one act of speech vs another, what is
"intended" vs what is understood).

## Why it matters

- **Relation and signification.** Parsons reports that the Herzbergers read Bhartṛhari as discussing "claims that certain relations cannot be signified. Examples are supposed to be the signification relation itself, and the inherence relation." (Parsons 2001, p. 525). The kārikā on inherence, as Parsons prints it: "SS 19. The relation called inherence, which extends beyond the signifying function, cannot be understood through words either by the speaker or by the person to whom the speech is addressed."
- **The liar.** Desnitskaya: the kārikās "are well-known as Bhartçhari’s paradox, similar to the Liar paradox in Greek philosophy, and were extensively studied by different scholars" (2006, p. 217). Wikipedia's liar article, citing Houben 1995: "He analyzes this statement together with the paradox of "unsignifiability" and explores the boundary between statements that are unproblematic in daily life and paradoxes." (Liar paradox, rev. 1377666957). Kak cites VP 3.3.25 for "sarvam mithyā bravīmi, “everything I am saying is false”" (2023, p. 16). See [the liar paradox](liar-paradox.md).
- **Set theory.** On the Herzbergers' defence, as Parsons reports it, "Paradoxes of set theory force one to place limits on what sets exist." (p. 526) — see [Russell's paradox](russells-paradox.md).
- **Truth predicates.** Kak places the paradox in the grammatical tradition, "emphasizing the inconsistency of language when it contains its own truth predicate" (2023, p. 15); compare [Tarski](../thinkers/tarski.md).

## Positions taken

No published grouping of the readings was found in the sources read; they
are listed side by side, chronologically, unranked.

- **Bhartṛhari (VP 3.3.22, 26, 28; c. fifth century — "late fifth century AD" per Wikipedia's liar article).** In the English Parsons prints: "SS 22. Of something which is being declared unsignifiable that condition (of being signifiable) cannot really be denied by those words, in that place, in that way, nor in another way, nor in any way." Desnitskaya's reading of 3.3.22 and 3.3.26: "Therefore, Bhartçhari claims, when something is spoken of as unsignifiable, the very situation of unsignifiability is not prohibited.26 A signifier cannot be the signified thing in the same context (pravçtta). That by means of which something is expressed cannot be expressed at the same time.27" (p. 217). Of 3.3.28, in her words: "He claims that during one process no other process is operative, therefore there would be no contradiction or infinite regress.29" (p. 218). The reading of these kārikās is what the scholars below dispute.
- **Herzberger & Herzberger (1981): the paradoxical claims are Bhartṛhari's and defensible.** As Parsons reports them, they argue: "2. Bhartṛhari was aware of the paradoxical nature of these claims. 3. Bhartṛhari actually endorses these paradoxical claims. 4. These claims can be supported by twentieth-century arguments." (p. 525). Their claims include "R1. The significance relation is unsignifiable." and "R7. The inherence relation is unsignifiable." Desnitskaya credits them with the name: "the so-called Unnameability Thesis (the term introduced by H. and R. Herzberger (Herzberger H., and R. Herzberger 1981))" (p. 217). Their defence, per Parsons: "Step 2. These limits entail that no relation may be one of its own relata. Step 3. So signification cannot be signified. For if it were, it would be one of its own relata." (pp. 525–526).
- **Houben (1995): communication, not truth value.** As Desnitskaya quotes him (Houben 1995c, p. 232): "in contrast with most Western treatments of the paradox, for Bhartçhari ‘true or false’ is not an interesting question, but whether or not the speaker succeeds in expressing his point." Desnitskaya calls Houben 1995b "an exhaustive analysis" of the studies (p. 217; her assessment). Houben's own texts were not read.
- **Parsons (2001): clarify, improve, limit.** His stated aim: "My goal is to clarify what Bhartṛhari actually claims, to improve on the Herzbergers' arguments in support of Bhartṛhari, and to note some limitations on the extent to which the claims under discussion may be supported by twentieth-century developments." (p. 525). He drops one term: "However, neither the word "denote" nor the idea, so far as I can see, occur in Bhartṛhari's text." Desnitskaya describes his article as one "where a formalized study of the paradox is undertaken" (p. 217). The content of his six qualms (listed in Arguments) was not read.
- **Desnitskaya (2006): activity-relative signification.** "Thus, in this kārikā the paradox is eliminated by the recourse to the successfulness of verbal communication." (p. 218), and "Therefore, paradoxes appear only in a formal, logical treatment of the language, in which the specific character of different kinds of activity is ignored." (p. 219). She calls VP 3.3.28 "a very advanced and distinguished solution" (p. 218; her assessment).
- **Kak (2023): the lower and the higher.** Kak reads VP 3.3.25 as "to highlight the tension between the lower and the higher meanings" (p. 16), in a paper where, in the Vedānta texts he reads, "paradox arises when these two categories are conflated [1]" (p. 15).

## Arguments in play

(none recorded as separate argument pages yet). On record in the sources read:

- **For the paradox (the conflict).** VP 3.3.20 as printed by Parsons and Desnitskaya's paraphrase (The question); the propositional check above shows the conflict follows once calling something "unnameable" counts as naming it.
- **For the Unnameability Thesis.** The Herzbergers' three-step set-theoretic argument, as Parsons reports it (Positions).
- **Against reading the thesis as a contradiction.** VP 3.3.22, 26, 28 as Desnitskaya reads them; Houben's "whether or not the speaker succeeds in expressing his point" (Positions).
- **Qualms about the Herzbergers' defence (Parsons 2001), by heading only:** "Qualm #1: Gaps in the reasoning." "Qualm #2: Semantic paradox versus ontological paradox." "Qualm #3: A difficulty about thatness." "Qualm #4: Limitations on what can be shown." "Qualm #5: Inherence is different!" "Qualm #6: Are we misinterpreting Bhartṛhari?" (p. 525). Their arguments were not read and are not reported.

## Thinkers who addressed it

- **Bhartṛhari** (*Vākyapadīya* 3.3, c. fifth century) — the kārikās; Wikipedia's Trikāṇḍī article locates the passage in book 3, chapter "On Relation": "Here Bhartṛ-hari discusses a paradox about how unnameable things can be approached through language." (rev. 1374159180).
- **Helārāja** (commentator on VP book 3) — quoted by Desnitskaya on 3.3.28 (n. 30); per Desnitskaya, the impossibility of expressing and being expressed at once holds for him "because of the unidirectional function (vyāpārasyaikatva) of the sense organs" (p. 217).
- **Hans G. Herzberger and Radhika Herzberger** (1981) — the originating paper and the name "Unnameability Thesis" (per Desnitskaya); bibliographic only.
- **Jan E. M. Houben** (1995, [doi:10.1007/bf01880219](https://doi.org/10.1007/bf01880219); 1995c) — per Desnitskaya and Wikipedia; not read.
- **Terence Parsons** (2001) — opening pages read.
- **Evgeniya A. Desnitskaya** (2006) — read.
- **Subhash Kak** (2023) — read.
- **[Graham Priest](../thinkers/priest.md)** — "Paradox and Ineffability", ch. 6 of *The Fifth Corner of Four* (OUP 2018, pp. 75–92, [doi:10.1093/oso/9780198758716.003.0006](https://doi.org/10.1093/oso/9780198758716.003.0006)) treats a paradox of the ineffable; its publisher abstract, "certain states of affairs are ineffable; but, of course, much is said about them", names Buddhist texts and Jain logic, not Bhartṛhari. Whether the chapter discusses Bhartṛhari was not established; it is listed for the shared problem only.

## Framings and reframings

- **Semantic paradox (liar family).** Desnitskaya's "similar to the Liar paradox in Greek philosophy" (p. 217); Kak's truth-predicate framing (p. 15).
- **Ontological paradox about relations.** The Herzbergers' reading, per Parsons, ties the thesis to set-theoretic limits on what may be "one of its own relata" (p. 526); Parsons's second qualm is headed "Semantic paradox versus ontological paradox." (p. 525).
- **A paradox in the etymological sense.** Desnitskaya, after quoting Houben: "Thus, VP 3.3.20–1 can be called a paradox not in the formal logical, but in the etymological sense: something ‘against’ (‘para’) ‘[common] opinion’ (‘dox’) (REPh 1998)." (p. 217).
- **Self-reference of the word.** Desnitskaya sets VP 3.3.26 against the passage VP 1.51–70: "A very strong objection to the idea of self-reference can be found in the Saübandha-samuddeśa (VP 3.3.26), which claims that a signifier cannot be the signified thing in the same context (pravçtta)." (p. 217).
- **Lower and higher meaning (Vedānta).** Kak 2023 (Positions).
- **Ineffability.** Priest 2018's chapter title and abstract frame a paradox of saying what is ineffable (bibliographic only; see Thinkers).

Not in the excerpts held: the Herzbergers' paper itself, Houben 1995b and
1995c and Houben 2001 (*Bulletin d'Études Indiennes* 19), Parsons 2001
after p. 526, Priest 2018 beyond its abstract, Subramania Iyer's English
translation of VP 3.3 (1971; archive.org OCR unreadable), and Hemanta
Kumar Ganguli's 1963 appendix on logical paradoxes listed in Wikipedia's
Bhartṛhari article; they are left out until a source is read.

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — the logical sense, against Desnitskaya's "etymological sense" (Framings).
- [Validity](../vocabulary/validity.md) — the propositional check.
- [Classical logic](../methods/classical-logic.md) — the tool's reading of the check.
- *avācya* ("unsignifiable", "unnameable", Kak 2023), *vācya* ("signifiable"), *signification* vs *denotation* (Parsons 2001), *inherence*, *relation* (*sambandha*), *self-reference*, *ineffability* — open work in [vocabulary](../vocabulary/index.md).
