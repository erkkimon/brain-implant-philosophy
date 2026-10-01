---
type: article
about: concept
title: "Meno's paradox (the paradox of inquiry)"
description: "How can one inquire into what one does not know, or recognise it when found? Meno's three questions at Meno 80d, Socrates' 'eristic' dilemma at 80e, recollection and the slave-boy (81a–86c), and the responses on record — Aristotle's knowing universally but not without qualification, Epicurean and Stoic preconceptions (prolepsis), al-Rāzī's twelfth-century restatement, partial knowledge, and Fine's (2014) targeting and recognition objections — each with its owner."
tags: [problem, paradox, epistemology, ancient-philosophy]
timestamp: 2026-10-01T19:53:21Z
---

# Meno's paradox (the paradox of inquiry)

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
claim grades as in [How claims are graded](../../conventions/how-claims-are-graded.md).
Part of the [problems](./index.md) branch. Map: Roy Sorensen,
[SEP Fall 2024 "Epistemic Paradoxes" §6.1](https://plato.stanford.edu/archives/fall2024/entries/epistemic-paradoxes/)
(revised 2022-03-03), with Silverman, Markie & Folescu, Samet and Adamson &
Benevich (SEP Fall 2024) and Rawson, [IEP "Meno"](https://iep.utm.edu/meno/)
(excerpts: `raw/sep-epistemic-paradoxes-and-plato-entries-fall-2024-menos-paradox.md`,
`raw/iep-meno-rawson-and-epicurus-okeefe-paradox-of-inquiry.md`). Plato in
Jowett's translation ([Gutenberg #1643](https://www.gutenberg.org/ebooks/1643)),
Stephanus locators from Lamb and Burnet's Greek on
[Perseus](https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0178%3Atext%3DMeno%3Asection%3D80e)
(excerpt: `raw/plato-meno-80d-86c-98a-paradox-and-recollection-jowett-lamb.md`).

## The question

Can anyone inquire into, and learn, what they do not already know? After three
attempts to define virtue, Meno asks (*Meno* 80d, Jowett): "And how will you enquire, Socrates, into that which you do not know? What will you put forth as the subject of enquiry? And if you find what you want, how will you ever know that this is the thing which you did not know?"

Socrates restates it as a two-horned [dilemma](../vocabulary/dilemma.md)
(80e, Jowett): "You argue that a man cannot enquire either about that which he knows, or about that which he does not know; for if he knows, he has no need to enquire; and if not, he cannot; for he does not know the very subject about which he is to enquire". He calls it
ἐριστικὸν λόγον (Burnet), which Jowett renders "tiresome dispute" and
Lamb "captious argument"; at 81d it becomes a "sophistical argument about
the impossibility of enquiry" (Jowett). Rawson (IEP §2b) reports that "This reformulation of Meno’s objection has come to be known as “Meno’s Paradox.”"
and that Socrates "interprets Meno’s objection in the obstructionist way".

Silverman (SEP 2014, §10) sets out the argument as printed:

1. "For anything, F, either one knows F or one does not know F."
2. "If one knows F, then one cannot inquire about F."
3. "If one does not know F, then one cannot inquire about F."
4. "Therefore, for all F, one cannot inquire about F."

**Structural note (logic).** With *k* for *one knows F* and *i* for *one can
inquire about F*, `python3 _implant/skills/tools/logic.py check --premises 'k | ~k' 'k -> ~i' '~k -> ~i' --conclusion '~i'`
reports "VALID" and "premise 1 is not needed for validity". So a reply must
reject premise 2 or premise 3, or read "know" differently in them (below).

The term contracted is [knowledge](../vocabulary/knowledge.md): which
cognitive state "know" and "not know" name in each horn. Sorensen (§6.1)
gives the general structure: "If you know the answer to the question you are asking, then nothing can be learned by asking. If you do not know the answer, then you cannot recognize a correct answer even if it is given to you." Not to be
confused with the "Meno problem" of why knowledge is worth more than true
belief (Pritchard, Turri & Carter, SEP 2022, §1).

## Why it matters

- Socrates (86b–c, Jowett), on the practical stake: "we shall be better and braver and less helpless if we think that we ought to enquire, than we should have been if we indulged in the idle fancy that there was no knowing and no use in seeking to know what we do not know".
- Sorensen (§6.1) reads Meno as discerning "a conflict between Socratic ignorance and Socratic inquiry".
- Markie & Folescu (SEP 2021, §3): "Plato presents an early version of the Innate Knowledge thesis in the Meno as the doctrine of knowledge by recollection"; Samet (SEP 2019, §2) reports that "Nativists have treated the slave-episode in the Meno as a touchstone for their view".
- Silverman (§10) writes that the dialogue offers "perhaps the first attempt to offer a justified true belief account of knowledge" (98a).

## Positions taken

In chronological order of owner; no grouping from the literature and no
survey figure is recorded.

- **Recollection (Plato's Socrates, 81a–86c).** On the word of "priests and
  priestesses" and poets "like Pindar" (81a–b), the soul "has knowledge of
  them all" and "all enquiry and all learning is but recollection" (81c–d,
  Jowett; ἀνάμνησις, 81d). Demonstration: the slave-boy (82b–85b) is asked to
  double a square of side two feet; he answers "double", then three, then
  "Indeed, Socrates, I do not know" (84a), and is led to "the square of the
  diagonal" (85b). Socrates infers "he who does not know may still have true
  notions of that which he does not know" (85c), that they "have just been
  stirred up in him, as in a dream" (85c–d), and "if the truth of all things
  always existed in the soul, then the soul is immortal" (86b), adding "Some
  things I have said of which I am not altogether confident" (86b). At 98a
  recollection is the tying of true opinions "by the tie of the cause".
  *Readings:* Silverman (§10): "Plato resolves the paradox by showing that there are different ways in which one might be said to ‘know’ something and that sometimes having a belief about F is adequate to begin an inquiry into F."
  Rawson (IEP §2b) reports "a false dichotomy between complete knowledge and pure ignorance" and judges "That is enough to refute Meno’s Paradox, which inferred the impossibility of learning from a false dichotomy between complete knowledge and pure ignorance."
  *Against:* Markie & Folescu (§3): "Contemporary supporters of Plato’s position are scarce." and "The metaphysical assumptions in the solution need justification."
  Samet (§2): "Skeptics see Socrates’ ‘questioning’ as really implicitly feeding the slave the right answers."
  Rawson (§2b): "Here, Socrates clearly asks “leading questions,” and eventually even shows the slave the answer in the form of a question (84e)."
- **Knowing universally, not without qualification (Aristotle, *Posterior
  Analytics* I.1, 71a–b).** "All instruction given or received by way of
  argument proceeds from pre-existent knowledge" (71a, Mure). A student who
  knows every triangle's angles equal two right angles, shown a figure not
  known to be a triangle, "knows not without qualification but only in the sense that he knows universally. If this distinction is not drawn, we are faced with the dilemma in the Meno: either a man will learn nothing or what he already knows" (71a, Mure; τὸ ἐν τῷ Μένωνι ἀπόρημα, Bekker).
  He rejects restricting the universal to instances one knows: "The solution which some people offer is to assert that they do not know that every pair is even, but only that everything which they know to be a pair is even" (71a).
  His formula: "there is nothing to prevent a man in one sense knowing what he is learning, in another not knowing it" (71b). (Excerpt: `raw/aristotle-posterior-analytics-1-1-71a-meno-dilemma-mure.md`.)
  Adamson & Benevich (SEP 2023, §2) report that "Al-Fārābī and Ibn Sīnā mostly accepted the Aristotelian solution to the paradox".
- **Preconceptions, prolepsis (Epicureans; Stoics).** O'Keefe (IEP
  "Epicurus", §4a) reports that Epicurus holds "we must already be in possession of certain basic concepts" to "start any inquiry whatsoever", a concern "similar to the Paradox of Inquiry explored by Plato in the Meno"; instead of prenatal acquaintance with Forms, "Epicurus thinks that we have certain ‘preconceptions’" formed "as the result of repeated sense-experiences of similar objects".
  Schwab (NDPR 2014) reports that Fine treats prolepsis as both schools' "orthodox response to Meno’s Paradox", resting on "Plutarch’s claim that they did so to explain “the possibility of inquiry” (300)", while noting they are "the first thinkers who do not explicitly mention Meno’s Paradox or the Meno".
  *Against:* Schwab: "the motivation for claiming that they posit prolepsis as a way of solving Meno’s Paradox is somewhat suspect." (Excerpt: `raw/schwab-2014-review-of-fine-2014-possibility-of-inquiry.md`.)
- **Not knowing is not a cognitive blank (Fine 2014).** Gail Fine, *The
  Possibility of Inquiry: Meno's Paradox from Socrates to Sextus* (OUP,
  [doi:10.1093/acprof:oso/9780199577392.001.0001](https://doi.org/10.1093/acprof:oso/9780199577392.001.0001);
  not read here — reported through Schwab's review). Schwab reports that M2 raises the “Targeting Objection”, according to which “one can’t inquire into something if one doesn’t at all know what it is since, in that case, one won’t have a target to aim at” (75), and M3 the “Recognition Objection” (80).
  "Meno’s worry, Fine thinks, is warranted if the alternative to knowing something is being in a cognitive blank about it"; his “mistake” is that lacking knowledge “doesn’t imply that one is in a complete cognitive blank. There are also true beliefs, and roughly-accurate beliefs” (82; cf. 103).
  On recollection, "Fine argues that Plato posits only prenatal knowledge", not innate knowledge.
  *Against (Schwab):* Socrates says the slave takes up knowledge "himself from himself (autos ex hautou). Fine only addresses this phrase in a footnote".
- **Partial knowledge as knowledge of conditionals (Sorensen, SEP 2022,
  §6.1).** "The natural solution to Meno’s paradox is to characterize the inquirer as only partially ignorant." and "It is natural to analyze partial knowledge as knowledge of conditionals."
  — learning the antecedent then yields the consequent "by applying the inference rule modus ponens".
  These are Sorensen's own assessments; §6.2 turns to conditionals that are
  "repudiated when we learn their antecedents".

**Structural note (logic).** If premise 3 is asserted only for *b*, *one is
in a complete cognitive blank about F* (the case in which, per Schwab, Fine
holds Meno's worry "warranted"), then `logic.py check --premises 'k -> ~i' 'b -> ~i' --conclusion '~i'`
reports "INVALID" with the counterexample "b=F, i=T, k=F": an inquirer who
neither knows F nor is blank about it. Adding the premise `k | b` makes the
tool report "VALID".

## Arguments in play

(none recorded as separate argument pages yet); the dilemma is stated above.

## Thinkers who addressed it

- **Plato** (*Meno*, "probably about 385 B.C.E." per Rawson, IEP §3) —
  Meno's questions, the eristic dilemma, recollection, the slave-boy; Silverman's next section (§11) is "Recollection in the
  Phaedo".
- **Aristotle** — *Posterior Analytics* I.1, 71a–b: knowing universally.
- **Epicurus** — preconceptions (O'Keefe, IEP §4a); **the Stoics** —
  prolepsis (as Fine treats them, per Schwab); **Plutarch** — reported
  source for prolepsis as explaining "the possibility of inquiry".
- **Sextus Empiricus** — Fine 2014 devotes "two chapters to Sextus
  Empiricus (Chs. 10-11)" (Schwab); Sextus' text not read here.
- **Al-Fārābī** and **Ibn Sīnā** — the Aristotelian solution (Adamson &
  Benevich §2, citing Black 2008 and Marmura 2009).
- **Fakhr al-Dīn al-Rāzī** (1149–1210) — restates the paradox and rejects
  the solution by respects (see below).
- **Alexander Nehamas** (1992), **Dominic Scott** (2006, *Plato's Meno*,
  [doi:10.1017/cbo9780511482632](https://doi.org/10.1017/cbo9780511482632))
  — listed by Rawson (IEP §4); not read here.
- **Gail Fine** (2014) — targeting and recognition objections;
  **Whitney Schwab** (2014) — review; **Roy Sorensen** (2022) — partial
  knowledge as conditionals.

## Framings and reframings

- **Al-Rāzī: every respect falls to a horn.** Adamson & Benevich (§2) write that his "main argument against real definitions is a reapplication of an old epistemological problem that goes back to Meno’s paradox in Plato (Meno, 80d6–10)".
  In their translation (*Muḥaṣṣal* 81–82): "If one is not aware of the object of inquiry, inquiry is impossible." and "the respect in which he is aware of it is distinct from the respect in which he is not aware of it."
  He "rejects this solution, on the grounds that the problem may be applied to each aspect individually" (Adamson & Benevich §2).
- **An eristic trap, not a practical doubt.** Markie & Folescu (§3) report that the paradox, "which Plato describes as a “trick argument” (Meno, 80e), rings sophistical"; Rawson (§2b) asks whether Meno raises "a practical difficulty" or "an abstract, defensive obstacle".
- **Broad and narrow senses.** Schwab reports that for Fine "Meno’s Paradox" covers, beyond 80d–e, “arguments that challenge the possibility of inquiry by focusing on questions about knowing and not knowing” (27).
- **Recollection as innatism, or not.** Samet (§2): "Plato’s anamnesis solution sees inquiry as a kind of deep memory recall."; Rawson (§2b) reads 86a as "the beginnings of a theory of innate ideas"; Fine (per Schwab) argues Plato's appeal is not "a commitment to innatism about knowledge".
- **Other paradox pages:** [surprise examination](../problems/surprise-examination-paradox.md)
  (same SEP entry), [Fitch's paradox of knowability](../problems/fitchs-paradox-of-knowability.md),
  [lottery and preface](../problems/lottery-and-preface-paradoxes.md),
  [Zeno's paradoxes](../problems/zenos-paradoxes.md),
  [sorites](../problems/sorites-paradox.md).

## Vocabulary

- [Paradox](../vocabulary/paradox.md); [dilemma](../vocabulary/dilemma.md)
  (argument form); [knowledge](../vocabulary/knowledge.md);
  [validity](../vocabulary/validity.md); [classical logic](../methods/classical-logic.md).
- *Recollection* (anamnesis), *eristic*, *preconception* (prolepsis),
  *innate idea*, *true belief* — open work in
  [vocabulary](../vocabulary/index.md).

Related problems: [the paradox of analysis](paradox-of-analysis.md) (Beaney & Raysmith, SEP "Analysis" §2, trace it to the *Meno*).
