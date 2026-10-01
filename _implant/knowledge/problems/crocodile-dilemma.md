---
type: article
about: concept
title: The crocodile dilemma
description: "A crocodile that has seized a child promises to return it if the parent guesses truly what it will do; the parent says it will not return the child. What should the crocodile do? The ancient sophism in Lucian (Vitarum auctio) and Quintilian I.10.5, Prantl's placing among the Stoic sophisms, Walker's reading as a retortable dilemma, Wikipedia's wording, and the relation to the liar and to the paradox of the court."
tags: [problem, paradox, logic, self-reference, dilemma, ancient-philosophy]
timestamp: 2026-10-01T21:51:46Z
---

# The crocodile dilemma

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md);
Wikipedia also files it as a [dilemma](../vocabulary/dilemma.md).
Ancient witnesses: Lucian, *The Sale of Creeds* (*Vitarum auctio*), lot of Chrysippus, and *Dialogues of the Dead* (Diogenes and Pollux), tr. H. W. and F. G. Fowler, [Gutenberg #6327](https://www.gutenberg.org/ebooks/6327) (excerpt: `raw/lucian-sale-of-creeds-crocodile-fowler.md`);
Quintilian, *Institutio Oratoria* I.10.5, tr. H. E. Butler, Loeb 1920, p. 163, via [LacusCurtius](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Quintilian/Institutio_Oratoria/1C*.html) (excerpt: `raw/quintilian-institutio-1-10-5-crocodile-butler.md`).
Modern maps: Carl Prantl, *Geschichte der Logik im Abendlande* I (1855), p. 493, [archive.org](https://archive.org/details/geschichtederlog01pran) (excerpt: `raw/prantl-1855-geschichte-der-logik-krokodil.md`);
John Walker's commentary in Murray's *Compendium of Logic* (1847), p. 159, [archive.org](https://archive.org/details/murrayscompendi00murrgoog) (excerpt: `raw/walker-1847-murrays-compendium-crocodile-retorted-dilemma.md`).
Admitted from Wikipedia's List of paradoxes, revision 1376699902, "Logic" (excerpt: `raw/wikipedia-crocodile-dilemma.md`).

## The question

Lucian's Chrysippus puts it to a buyer about the buyer's own child: "A crocodile catches him as he wanders along the bank of a river, and promises to restore him to you, if you will first guess correctly whether he means to restore him or not. Which are you going to say?" (*Sale of Creeds*, Fowler tr.).
Butler's note to Quintilian I.10.5 gives the answer that makes the trouble: "A crocodile, having seized a woman's son, said that he would restore him, if she would tell him the truth." The mother replies that he will not restore him; the note ends: "Was it the crocodile's duty to give him up?" (Loeb 1920, n. 98).
Prantl's statement (1855, p. 493): "Ein Krokodil hat ein Kind geraubt und verspricht dem Vater desselben die Zurückgabe, wofern er errathe, welchen Entschluss betreffs der Rückgabe oder Nicht-Rückgabe das Krokodil gefasst habe." If the father guesses non-return, "so ist das Krokodil rathlos, was es thun solle".
Wikipedia's list entry: "Crocodile dilemma: If a crocodile steals a child and promises its return if the father can correctly guess exactly what the crocodile will do, how should the crocodile respond in the case that the father guesses that the child will not be returned?" (rev. 1376699902).
Wikipedia's article (rev. 1376050273) spells out both horns: "If the crocodile decides to keep the child, he violates his terms: the parent's prediction has been validated, and the child should be returned. However, if the crocodile decides to return the child, he still violates his terms, even if this decision is based on the previous result: the parent's prediction has been falsified, and the child should not be returned."

The versions differ in wording the sources give, and the question depends on it: Lucian has *if* ("promises to restore him to you, if you will first guess correctly"), Wikipedia's article has "if and only if", and Butler's note asks about the crocodile's "duty".

**Propositional check (this implant, 2026-10-01; logic, not a position).**
Let *g* stand for *the parent's guess is correct* and *r* for *the crocodile returns the child*.
The parent guesses that the child will not be returned, so *g* <-> ~*r*.
Read with Wikipedia's "if and only if" as two material conditionals, the promise is *g* -> *r* and ~*g* -> ~*r*.
`logic.py check --premises "g <-> ~r" "g -> r" "~g -> ~r" --conclusion "r & ~r"` outputs `VALID` and `premises are jointly inconsistent — argument is vacuously valid`.
The promise alone (`"g -> r" "~g -> ~r"` against `"r & ~r"`) outputs `INVALID` with counterexample rows `g=T, r=T` and `g=F, r=F`;
the guess alone (`"g <-> ~r"`) outputs `INVALID` with rows `g=T, r=F` and `g=F, r=T`.
With the one-way *if* of Lucian and Butler's note (*g* -> *r* only), `--premises "g <-> ~r" "g -> r" --conclusion "r & ~r"` outputs `INVALID` with the single row `g=F, r=T`,
and `--premises "g <-> ~r" "g -> r" --conclusion "r"` outputs `VALID`: on that reading the premises are satisfiable, and only by returning the child.
Had the parent guessed return (*h* <-> *r*, with *h* for that guess being correct), the biconditional promise plus the guess leaves both `r` and `~r` unproved: each check outputs `INVALID`, with rows `h=F, r=F` and `h=T, r=T` respectively, matching Wikipedia's "logically smooth but unpredictable".
The tool reads *if … then* as the material conditional and *g* as an atom; it does not model the future tense, the step from the content of the guess to *g* <-> ~*r*, or obligation.

## Why it matters

- **A named Stoic sophism.** Prantl lists it among the Stoic sophisms on p. 493, after the Reaper; his n. 216 cites Diogenes Laertius VII.44 and 82, scholia on Hermogenes, and Lucian's *Vitarum auctio* for the name. Lucian's Chrysippus offers it as a specimen of "the far-famed syllogism" (*Sale of Creeds*). The Diogenes Laertius passages (Hicks tr.) name "The Mowers" and lists of "insoluble arguments" without the crocodile (excerpt: `raw/diogenes-laertius-2-108-111-eubulides-hicks.md`); the link to the crocodile is Prantl's.
- **A stock example of logical subtlety.** Quintilian says the sage is taught such things "not that acquaintance with the so called "horn" or "crocodile" problems can make a man wise, but because it is important that he should never trip even in the smallest trifles." (I.10.5, Butler tr.). Lucian's Diogenes urges philosophers to stop "tricking each other with horn and crocodile puzzles" (*Dialogues of the Dead*).
- **Relation to the liar.** Wikipedia's article: "The crocodile paradox, also known as crocodile sophism, is a paradox in logic in the same family of paradoxes as the liar paradox." (citing MathWorld). See [the liar paradox](liar-paradox.md).
- **Relation to the paradox of the court.** Murray's text gives Protagoras and Euathlus as the case of a dilemma that "can be retorted", and Walker calls the crocodile "probably a similar instance of a dilemma that might be retorted." (1847, p. 159). Prantl treats the next sophism, which his n. 217 finds complete in Gellius V.10 (Protagoras and Euathlus), as "eine andere Wendung hievon" (p. 493). See [the paradox of the court](paradox-of-the-court.md).
- **Knowledge and prediction.** Wikipedia's article: "The crocodile dilemma exposes some of the logical problems posed by metaknowledge." It compares the case to the unexpected hanging, which it says Richard Montague (1960) used to show three assumptions about knowledge inconsistent (see [the surprise examination paradox](surprise-examination-paradox.md)), and lists the halting problem under "See also".

## Positions taken

No grouping of responses was found in the sources read; the answers on record are listed by owner, unranked.

- **No answer given (Lucian, *Sale of Creeds*).** The buyer: "A difficult question. I don't know which way I should get him back soonest. In Heaven's name, answer for me, and save the child before he is eaten up." Chrysippus: "Ha, ha. I will teach you far other things than that." — and moves on to other arguments.
- **A retortable dilemma, which proves nothing (Walker 1847, p. 159, applying Murray's rule).** The father argues "that, if he had told truth, he must have his child, according to the crocodile's promise ; and if he had not told truth, the crocodile must restore his child, as it was false that he would not restore it." Walker: "It is easy to see how the crocodile might retort this dilemma, and prove that in either case he must keep the child." Murray's rule for such cases: "for an argument, which proves things contradictory, proves nothing, as in the following instance." *Check (this implant, 2026-10-01; logic, not a position):* the father's dilemma `"g -> r" "~g -> r"` to `"r"` and the retort `"g -> ~r" "~g -> ~r"` to `"~r"` each output `VALID`; all four premises together against `"r & ~r"` output `VALID` and `premises are jointly inconsistent — argument is vacuously valid`.
- **The father guessing return risks loss (Prantl 1855, p. 493).** Prantl adds that if the father guesses return, he risks the crocodile claiming to have decided on non-return so as to refuse the child for a false guess (paraphrase of the German on p. 493; this implant's translation).
- **No justifiable solution (Wikipedia).** "The question of what the crocodile should do is therefore paradoxical, and there is no justifiable solution." (rev. 1376050273; Wikipedia's assessment, citing Siekmann ed. 1989, Young 2005 and Murray's Compendium 1847, p. 159). MathWorld (Weisstein & Barile) likewise calls it "an unsolvable problem in logic" (excerpt: `raw/weisstein-barile-mathworld-crocodiles-dilemma.md`).
- **A game with a rationality gap (Gerogiorgakis 2016).** From the abstract only: "The Crocodile Paradox is reformulated and analyzed as a game—named CP—whose Nash equilibrium is shown to trigger a cyclic choice and to invite a rationality gap." and "It is shown that CP is a counter-example to Gaifman's solution of the rationality gaps problem." (*History and Philosophy of Logic* 37(2), 2016, pp. 101–113, [doi:10.1080/01445340.2015.1046211](https://doi.org/10.1080/01445340.2015.1046211); excerpt: `raw/gerogiorgakis-2016-mind-the-croc-abstract.md`; full text not read).

## Arguments in play

(none recorded as separate argument pages yet). The father's dilemma and the crocodile's retort are quoted from Walker under Positions taken; the propositional core is under The question.

## Thinkers who addressed it

- **Chrysippus** (3rd c. BCE) — the case is put in his mouth by Lucian; Walker calls it "Chrysippus' Sophism of the Crocodile" (1847, p. 159). No text of Chrysippus on it was read.
- **Quintilian** (*Institutio Oratoria* I.10.5, 1st c. CE) — names "crocodile" problems among the logical subtleties of the sage's training.
- **Lucian of Samosata** (*Vitarum auctio*; *Dialogues of the Dead*, 2nd c. CE) — states the case in full; Walker says it is the sophism "which Lucian laughs at in his Vit. Auct.".
- **Richard Murray and John Walker** (*Compendium of Logic*, 1847) — the rule on retorted dilemmas and the crocodile as an instance.
- **Carl Prantl** (1855) — places it among the Stoic sophisms with sources and a pirate variant: "In einer anderen Version sind statt des Krokodils Seeräuber genannt" (p. 493).
- **Eric W. Weisstein and Margherita Barile** (MathWorld) — the encyclopedia entry Wikipedia cites.
- **Stamatios Gerogiorgakis** (2016) — game-theoretic reformulation (abstract read).
- On the liar side, see [Eubulides](../thinkers/eubulides.md), who per Bobzien "is on record as the inventor of both the Liar and the Sorites paradox." (SEP Fall 2024 "Ancient Logic" §1; excerpt `raw/sep-logic-ancient-dialectical-school-fall-2024-eubulides.md`); no source read connects him with the crocodile. The Fall 2024 SEP entries "Ancient Logic", "Insolubles", "Liar Paradox", "Dialectical School" and "Self-Reference" were searched and do not mention the crocodile.

## Framings and reframings

- **A sophism of the Stoic school.** Prantl's framing, and Lucian's, who gives it to Chrysippus beside the Reaper, the Electra and the Man in the Hood (see `raw/lucian-sale-of-creeds-electra-hooded-fowler.md`).
- **A liar-family paradox.** Wikipedia (citing MathWorld), and its category "Self-referential paradoxes". *Structural note (this implant):* the self-reference runs through the case, not through one sentence — the guess is about the act that the promise makes depend on the guess's truth; the propositional check above shows the inconsistency arises only when the guess *not returned* meets the two-way reading of the promise.
- **A retortable dilemma.** Walker's framing, which puts it beside [Protagoras and Euathlus](paradox-of-the-court.md) rather than the liar.
- **A problem about knowledge and prediction.** Wikipedia's metaknowledge paragraph and its comparison with the unexpected hanging.
- **A problem about choice.** Gerogiorgakis's "self-referential/cyclic choice", "choosing according to a norm that refers to the choosing itself" (abstract).
- **Kin cases.** Wikipedia's List of paradoxes ends the entry on [Buridan's bridge](buridans-bridge.md) with "Similar to the crocodile dilemma."; Walker also points to "a similarly ludicrous instance" in *Don Quixote*, without naming the chapter.

Not read and left out: the Greek scholia on Hermogenes (Walz IV) cited by Prantl; Kleene (1964) p. 39, cited by MathWorld; Siekmann ed. (1989) and Young (2005), cited by Wikipedia; Montague (1960); Akhvlediani (2011, *ΣΧΟΛΗ* 5.1), and the full text of Gerogiorgakis 2016.

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — see The question.
- [Dilemma](../vocabulary/dilemma.md) — Walker's father's argument and its retort.
- [Validity](../vocabulary/validity.md) — the checks above; Murray's sense of a dilemma "invalid" when retorted differs from formal validity (both of Walker's dilemmas check `VALID`).
- [Classical logic](../methods/classical-logic.md) — the material conditional used in the checks.
- *Sophism*, *self-reference*, *retorted dilemma* — open work in [vocabulary](../vocabulary/index.md).
