---
type: article
about: concept
title: "I know that I know nothing (the Socratic paradox)"
description: "Can anyone know that they know nothing, when that knowledge would be something known? The saying credited to Socrates, what Plato's Apology (21b, 21d, 22d, 29b) has him say, the formula's ancient sources (Cicero, Academica 1.16, 1.45, 2.74; Diogenes Laertius 2.32), and the readings on record — the self-refuting formula, Arcesilaus's withdrawal of even that one item, and Vogt's and Fine's restricted readings."
tags: [problem, paradox, epistemology, ancient-philosophy, self-reference]
timestamp: 2026-10-01T22:52:16Z
---

# I know that I know nothing (the Socratic paradox)

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Primary text: Plato, *Apology* 21b–22d, 29a–b, in Jowett's translation
([Gutenberg #1656](https://www.gutenberg.org/cache/epub/1656/pg1656.txt)), Fowler's
Loeb translation and Burnet's Greek on [Perseus](https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0170:text=Apol.:section=21d)
(excerpt: `raw/plato-apology-21b-22d-29b-socratic-ignorance-jowett-fowler.md`).
Ancient formula: Cicero, *Academica* ([Latin Library](https://www.thelatinlibrary.com/cicero/acad.shtml);
Yonge's translation, [Gutenberg #29247](https://www.gutenberg.org/cache/epub/29247/pg29247.txt))
and Diogenes Laertius 2.32 ([Hicks, Wikisource](https://en.wikisource.org/wiki/Lives_of_the_Eminent_Philosophers/Book_II))
(excerpt: `raw/cicero-diogenes-laertius-socrates-knows-only-that-he-knows-nothing.md`).
Maps: SEP Fall 2024 — Nails & Monoson, ["Socrates"](https://plato.stanford.edu/archives/fall2024/entries/socrates/);
Vogt, ["Ancient Skepticism"](https://plato.stanford.edu/archives/fall2024/entries/skepticism-ancient/) §2.2;
Frede & Lee, ["Plato's Ethics: An Overview"](https://plato.stanford.edu/archives/fall2024/entries/plato-ethics/);
Ichikawa & Steup, ["The Analysis of Knowledge"](https://plato.stanford.edu/archives/fall2024/entries/knowledge-analysis/) §1.1
(excerpt: `raw/sep-socrates-skepticism-ancient-plato-ethics-fall-2024-socratic-ignorance.md`).
Scholarship: Fine 2008 and 2021, Vlastos 1985 (excerpt and verified
bibliographic data: `raw/fine-2008-vlastos-1985-does-socrates-claim-to-know-that-he-knows-nothing.md`).
Admitted from Wikipedia's [List of paradoxes, revision 1376699902](https://en.wikipedia.org/w/index.php?title=List_of_paradoxes&oldid=1376699902),
"Logic", which reads: "I know that I know nothing: Purportedly said by Socrates."
(excerpt: `raw/wikipedia-list-of-paradoxes-i-know-that-i-know-nothing-entry.md`).

## The question

The formula: Cicero has Varro say of Socrates that he "knows this one thing alone, that he knows nothing" (*Academica* 1.16, Yonge); Diogenes Laertius lists among his sayings "that he knew nothing except just the fact of his ignorance." (2.32, Hicks).
If knowing nothing excludes knowing even that, the formula undercuts itself;
the question is whether Socrates says it, and if he says something close,
whether that is consistent. The term contracts are
[knowledge](../vocabulary/knowledge.md), [paradox](../vocabulary/paradox.md)
and [validity](../vocabulary/validity.md).

**What the *Apology* says.** Readings side by side (Jowett / Fowler; Greek, Burnet):

| Stephanus | Jowett | Fowler |
|---|---|---|
| 21b | "for I know that I have no wisdom, small or great." | "For I am conscious that I am not wise either much or little." |
| 21d | "I neither know nor think that I know." | "whereas I, as I do not know anything, do not think I do either." |
| 21d | "In this latter particular, then, I seem to have slightly the advantage of him." | "that what I do not know I do not think I know either." |
| 22c–d | "I was conscious that I knew nothing at all, as I may say" | "For I was conscious that I knew practically nothing" |
| 29b | "but I do know that injustice and disobedience to a better, whether God or man, is evil and dishonourable" | "But I do know that it is evil and disgraceful to do wrong and to disobey him who is better than I, whether he be god or man." |

The Greek at 21d: "ἐγὼ δέ, ὥσπερ οὖν οὐκ οἶδα, οὐδὲ οἴομαι"; at 21b, "σύνοιδα ἐμαυτῷ" (Fowler: "I am conscious"); at 22c–d, "συνῄδη οὐδὲν ἐπισταμένῳ ὡς ἔπος εἰπεῖν".
*Structural note (this implant, 2026-10-02):* the string "I know that I
know nothing" does not occur in the Jowett or Fowler text of these
passages as fetched; Wikipedia (rev. 1377681317) states that the saying "actually occurs nowhere in Plato's works in precisely the form "I know I know nothing.""
Vogt (SEP 2024, §2.2) renders 22d as "“About myself I knew that I know nothing”".

**Logic check (this implant, 2026-10-02; logic, not a position).** Let `k` =
*I know that I know nothing*, `n` = *I know nothing*. Knowledge is factive,
`k -> n` (Ichikawa & Steup, SEP §1.1, report that "Most epistemologists have found it overwhelmingly plausible that what is false cannot be known."); knowing
nothing includes not knowing `k`, `n -> ~k`.
`logic.py check --premises "k -> n" "n -> ~k" --conclusion "~k"` outputs
"VALID"; with the added premise `k` and conclusion `n` it outputs
"premises are jointly inconsistent — argument is vacuously valid". With
conclusion `k` it outputs "INVALID" (counterexamples "k=F, n=T" and
"k=F, n=F"). Restricted form: `w` = *I know that I lack wisdom about the
most important things*, `i` = *I lack that wisdom*; `logic.py check
--premises "w -> i" "w" --conclusion "~w"` outputs "INVALID" (counterexample
"i=T, w=T"). The tool does not decide which form Socrates asserts; the
readings below differ on that.

## Why it matters

- **A root of Academic skepticism.** Vogt (SEP 2024, §2.2): "Socrates’ commitment to reason—examination as the way to find out—inspires the skepticism of the Hellenistic Academy (Cooper 2004b, Vogt 2013)."
- **The elenchus.** Frede & Lee (SEP 2023/2024, §2.1) raise a limit on the method "given Socrates’ disavowal of knowledge."
- **Irony.** Nails & Monoson (SEP 2022/2024, §1): Socrates "had a reputation for irony, though what that means exactly is controversial; at a minimum, Socrates’s irony consisted in his saying that he knew nothing of importance and wanted to listen to others, yet keeping the upper hand in every discussion."
- **Inquiry.** Vogt (§2.2) passes from Socratic ignorance to Meno's puzzle; see [Meno's paradox](menos-paradox.md), raised after Socrates says he does not know what virtue is (*Meno* 80c–d; `raw/plato-meno-80d-86c-98a-paradox-and-recollection-jowett-lamb.md`).

## Positions taken

Not ranked; each is reported with the source that records it.

- **Socrates knows one thing: that he knows nothing (Cicero's Varro).** "He says that he knows nothing, except that one fact, that he is ignorant" (*Acad.* 1.16, Yonge); Latin: "ipse se nihil scire id unum sciat". Cicero (2.74, Yonge) states it as Socrates' view: "He excepted one thing only, asserting that he did know that he knew nothing; but he made no other exception."
- **Not even that one item is known (Arcesilaus, per Cicero).** "therefore Arcesilas asserted that there was nothing which could be known, not even that very piece of knowledge which Socrates had left himself." (*Acad.* 1.45, Yonge).
- **Socrates knows he lacks knowledge of the most important matters (Vogt).** Vogt (SEP 2024, §2.2): "Some readers (ancient and modern) take Socrates to profess that he knows nothing. But the context of the dialogue allows us to read his pronouncement as unproblematical. Socrates knows that he does not know about important things."
- **Knows, or is aware, that he is not wise — no contradiction (Fine).** Fine (2021, ch. 2 abstract) "argues that Socrates does not say, or imply, that he knows that he knows nothing in a way that involves self-contradiction. Rather, he is saying either that he knows that he is not wise (where knowing something falls short of being wise with respect to it); or else that he is aware that he is not wise (where being aware of something falls short of knowing it)." Wikipedia (rev. 1377681317) reports her 2008 article (p. 51) as saying "it is better not to attribute it to him".
- **A misreading of Plato (Taylor, as Wikipedia reports him).** Wikipedia's footnote: C. C. W. Taylor "has argued that the "paradoxical formulation is a clear misreading of Plato" (Socrates, Oxford University Press 1998, p. 46)." Not read in the original.
- **Two senses of knowledge (Vlastos 1985).** Vlastos, "Socrates' Disavowal of Knowledge", *Philosophical Quarterly* 35(138), 1985, [doi:10.2307/2219545](https://doi.org/10.2307/2219545), reworked in *Socratic Studies* (1994), [doi:10.1017/cbo9780511518515.003](https://doi.org/10.1017/cbo9780511518515.003). Bibliographic data verified; the text was not read, so its thesis is not stated here.

**Cases for and against.** Text on record bearing on the restricted
readings: at 29b Socrates says "but I do know" something (Jowett), and at
21d the object of not knowing is "anything really beautiful and good"
(Jowett). Text on record bearing on the formula: Cicero's speakers (1.16,
2.74) and Diogenes (2.32) attribute it to Socrates. On how to read
Cicero, Fine (2008, n. 1) cites J. Annas (1994, at p. 310) "For this reading of what Cicero says" and adds: "For a recent challenge to this reading, see M. F. Burnyeat".
No survey figure is recorded.

## Arguments in play

(none as separate argument pages yet). Related problems:
[Meno's paradox](menos-paradox.md); [the knower paradox](knower-paradox.md)
("This sentence is not known."); [Fitch's paradox of knowability](fitchs-paradox-of-knowability.md),
which uses the factive operator "It is known that";
[Moore's paradox](moores-paradox.md); [the liar paradox](liar-paradox.md)
and [the Epimenides paradox](epimenides-paradox.md), self-referential
items of the same Wikipedia list section.

## Thinkers who addressed it

- **Socrates**, as Plato presents him — *Apology* 21b–23b, 29a–b; Republic 354c in Frede & Lee's translation (SEP §3.1): "As far as I am concerned, the result is that I know nothing".
- **Plato** — author of the *Apology*, the passages tabled under The question.
- **Arcesilaus** — denies even Socrates' one item (Cicero, *Acad.* 1.45).
- **Cicero** (*Academica*) — the Latin formula, 1.16; Fine (2008, n. 1) names "Cicero, Acad 1. 16" as "One early source often thought to do so".
- **Diogenes Laertius** (*Lives* 2.32) — "εἰδέναι μὲν μηδὲν πλὴν αὐτὸ τοῦτο" (2.32).
- **Gregory Vlastos** — "Socrates' Disavowal of Knowledge" (1985); Nails & Monoson (SEP §2.2) name him the doyen of the analytic strand ("Gregory Vlastos (1907–1991) of the analytic.").
- **J. Annas** (1994) and **M. F. Burnyeat** (1997) — on how to read Cicero, as cited by Fine (2008, n. 1); not read.
- **C. C. W. Taylor** (*Socrates*, 1998, p. 46) — as Wikipedia reports him.
- **Gail Fine** (2008, *OSAP* 35: 49–88, [doi:10.1093/oso/9780199557790.003.0003](https://doi.org/10.1093/oso/9780199557790.003.0003); reprinted 2021, *Essays in Ancient Epistemology*, pp. 33–62, [doi:10.1093/oso/9780198746768.003.0002](https://doi.org/10.1093/oso/9780198746768.003.0002)).
- **Katja Vogt** (SEP "Ancient Skepticism", 2010, rev. 2022, §2.2).

## Framings and reframings

- **Not knowledge but awareness.** Fine's second option (2021 abstract) moves the claim from knowing to being "aware that he is not wise (where being aware of something falls short of knowing it)"; Fowler renders the Greek verb at 21b and 22d (σύνοιδα, συνῄδη) as "I am conscious" / "I was conscious".
- **Not "nothing" but "nothing of importance".** Vogt's "megista; 22d" and Nails & Monoson's "knew nothing of importance" restrict the object.
- **Simple and double ignorance.** The Jowett text at 29b names the contrast: "Is not this ignorance of a disgraceful sort, the ignorance which is the conceit that a man knows what he does not know?"
- **Another "Socratic paradox".** Wikipedia (rev. 1377681317, lead) notes the name "is often instead used to refer to other seemingly paradoxical claims made by Socrates in Plato's dialogues (most notably, Socratic intellectualism and the Socratic fallacy)."

## Vocabulary

- [Knowledge](../vocabulary/knowledge.md) — the factive reading used in the
  logic check is Ichikawa & Steup's report, not this implant's; they also
  report Hazlett (2010) as arguing that "knows" is not factive.
- [Paradox](../vocabulary/paradox.md); [Validity](../vocabulary/validity.md);
  [Classical logic](../methods/classical-logic.md), in which the logic check
  above is run.
- Socratic ignorance, disavowal of knowledge, elenchus, irony, Academic
  skepticism — open work in [vocabulary](../vocabulary/index.md).
