---
type: article
about: concept
title: "Buridan's bridge"
description: "Plato vows to let Socrates cross if his first proposition is true and to throw him in the water if it is false; Socrates says 'You will throw me in the water'. What should Plato do to keep his promise? Buridan's seventeenth sophism of Sophismata ch. 8 (the insolubles), his three answers (future contingent, a promise false by self-reference, no duty to keep it), Bradwardine's earlier case, Paul of Venice's classification, Sancho Panza's two verdicts in Don Quixote II.51, and the relation to the liar."
tags: [problem, paradox, logic, self-reference, medieval-philosophy]
timestamp: 2026-10-01T19:53:21Z
---

# Buridan's bridge

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Primary text: John Buridan, *Summulae de Dialectica*, Treatise 9 (*Sophismata*),
ch. 8, seventeenth sophism, tr. Gyula Klima (Yale, 2001, ISBN 0-300-08425-0),
pp. 993–994 (excerpt: `raw/buridan-c1350-sophismata-8-17-bridge-klima.md`).
Maps: Spade & Read, [SEP Fall 2024 "Insolubles"](https://plato.stanford.edu/archives/fall2024/entries/insolubles/)
§§1.4, 3.8, 4.5 (excerpt: `raw/sep-insolubles-fall-2024-bridge-variety-and-buridan.md`);
Zupko, [SEP Fall 2024 "John Buridan"](https://plato.stanford.edu/archives/fall2024/entries/buridan/)
§4 (excerpt: `raw/sep-buridan-fall-2024-insolubles-final-solution.md`).
Admitted from Wikipedia's List of paradoxes, revision 1376699902, "Philosophy"
(excerpt: `raw/wikipedia-buridans-bridge.md`).

## The question

Buridan sets the case: "Let us posit the case that Plato is the master of the bridge and that he guards it with such a powerful military support that nobody can cross it without his permission." (Klima tr., p. 993).
Plato's vow: "Then Plato, getting angry, vows and takes an oath of the form: ‘Certainly, Socrates, if with your first proposition that you will utter you say something true, I will let you pass, but certainly if you say something false, I will throw you in the water’." (p. 993).
Socrates' reply is the sophism itself: "The seventeenth sophism concerns some conditional promises or vows. And let the sophism be ‘You will throw me in the water’." (p. 993).
Buridan's question: "The problem then is: what should Plato do to keep his promise?" (p. 993).

The dilemma, in Buridan's words: "If you say that he should throw Socrates in the water, then this goes against the promise, for then Socrates said something true; therefore, Plato should have let him pass. And if you say that he should let him pass, it appears again that this goes against the promise and the oath, for then Socrates said something false, in which case Plato should have thrown him in the water." (p. 993).
Wikipedia's list entry gives the same structure: "Whatever Plato does, he will seemingly break his promise." (List of paradoxes, rev. 1376699902).

**Propositional check (this implant, 2026-10-01; logic, not a position).**
Let *t* stand for *Socrates' proposition is true* and *w* for *Plato throws
Socrates in the water*. Socrates' proposition says that *w*, so *t* <-> *w*; Plato's vow,
read as two material conditionals with letting pass as not throwing, is
*t* -> ~*w* and ~*t* -> *w*. `logic.py check --premises "t <-> w" "t -> ~w" "~t -> w" --conclusion "w & ~w"`
outputs `VALID` and `premises are jointly inconsistent — argument is vacuously valid`.
The vow alone (`"t -> ~w" "~t -> w"` against `"w & ~w"`) outputs `INVALID`
with counterexample rows `t=T, w=F` and `t=F, w=T`, and *t* <-> *w* alone is
likewise `INVALID` (rows `t=T, w=T` and `t=F, w=F`): each part is satisfiable,
their combination is not. The tool reads *if … then* as the material
conditional and treats *t* as an atom; it does not model the future tense,
the step from the content of Socrates' sentence to *t* <-> *w*, or Buridan's
distinction between strict and promissive conditionals (below).

## Why it matters

- **It is filed among the insolubles.** Buridan opens the chapter that contains it: "The eighth chapter will be about propositions that are self-referential [de propositionibus habentibus reflexionem supra seipsas] on account of the signification of their terms. This chapter contains [propositions] called insolubles." (p. 952). Spade & Read: "The medieval name for paradoxes like the famous Liar Paradox (“This proposition is false”) was “insolubles” or insolubilia," (preamble), and "The medievals discussed many more insolubles than the Liar Paradox, though most can be seen as variants of it." (§1.4) — the bridge being one of the examples listed there.
- **Relation to the liar.** Zupko places the chapter in Buridan's work on "alethic paradoxes such as the Liar": "Most modern logicians know of his solutions to alethic paradoxes such as the Liar, addressed in the eighth and final chapter of ninth treatise of the Summulae, which belongs to the medieval literature of sophismata or insolubilia." (SEP "John Buridan", §4). See [the liar paradox](liar-paradox.md).
- **Conditionals and promises.** Buridan uses the case to separate strict from promissive conditionals (Positions, below); the same distinction appears in his rules of consequence: "Further, they do not apply to promissive consequences concerning future contingents, either, e.g., ‘If you visit me, I’ll give you a horse’; for the antecedent can be true while the consequent is false" (Treatise 1, 1.7.3, p. 62).
- **Future contingents.** Buridan's first answer refers the reader to Aristotle's *On Interpretation* (Klima's n. 197 identifies "On Interpretation I.9"), the text of the sea-battle and future contingents.
- **Literature.** Spade & Read point to the same case in Cervantes: "see also Cervantes Don Quixote, vol. II book III ch. XIX, p. 714" (§1.4).

## Positions taken

No grouping of responses to this case was found in the sources read; the
answers on record are listed by owner, in chronological order, unranked.

- **Buridan's three answers (Sophismata 9.8, seventeenth sophism, c. 1350s).** He splits the problem: "The first is whether Socrates’ proposition, which was posited as the sophism, is true; the second is whether Plato’s proposition expressing his promise or vow was true or false; the third concerns what Plato should do to keep his promise and vow." (p. 993).
  1. *Socrates' proposition is a future contingent:* "To the first I reply that Socrates’ proposition is a future contingent; therefore, I cannot know whether it is true or false until I see what will be the case with that future act, because it is in the power of Plato to make it true or false." (p. 993). He adds: "For he uttered a proposition that had to be true or false, although not determinately true or false until the future act came about, as one should see [this point] in On Interpretation." (p. 994).
  2. *Plato's vow is not true.* Strictly: "As to the second question, it is clear that Plato’s proposition was a conditional that could not be true in the strict sense, because the antecedent could be true without the consequent." (p. 993), since "For it was possible that Socrates would have said something very true, say, that God exists, and that Plato would still not have permitted him to pass." (p. 993). In the looser sense: "Promissive conditionals, however, are conceded to be true in a less strict sense in that when the condition is being fulfilled, then the promise is also fulfilled" (p. 993); "And speaking in this sense I say that Plato did not say something true, since Socrates fulfilled the condition." (p. 994). The ground is self-reference: "But given this, Plato cannot fulfill the promise, for because of Socrates’ proposition Plato’s promise has reference to itself whence it follows that it is false." (p. 994).
  3. *No duty to keep it; promise with an exception:* "Thus when the third question asks what Plato should do to keep his promise, I say that he does not have to keep his promise, nor should he promise anything in this way, but with an exception that excludes the case that Socrates utters a proposition that has reference to the promise such that it thence follows that what is promised cannot be made to happen." (p. 994).
  *On the general theory behind ch. 8:* Spade & Read assess Buridan's later theory of insolubles — "Rather, his later theory claims that every proposition virtually implies another proposition asserting the truth of the first." — as follows: "Buridan’s solution has been much discussed in recent decades and has been edited and translated several times (see Buridan [B-S], [B-S2], [B-B], [B-SD], [B-SD2]), but it is deeply problematic (see, e.g., Read 2002: §5; Read 2006: §6; with a response on Buridan’s behalf in Klima 2009, §10.5)." (§3.8; the assessment is theirs, and it concerns the general theory, illustrated in the SEP with the liar-type sophisms, not the bridge specifically). Zupko calls the final theory one that "receives the somewhat tepid endorsement of being “closer to the truth” than the previous solution—a reflection, perhaps, of his awareness of the imperfectability of any formal system that tries to stick close to the facts of human language." (§4; Zupko's reading). Klima's response (2009, §10.5) is cited by Spade & Read and was not read here.
- **Sancho Panza's division (Cervantes, *Don Quixote* II.51, 1615).** "“Well then I say,” said Sancho, “that of this man they should let pass the part that has sworn truly, and hang the part that has lied; and in this way the conditions of the passage will be fully complied with.”" (Ormsby tr.; excerpt: `raw/cervantes-1615-don-quixote-2-51-bridge-ormsby.md`).
  *Against, in the novel:* "“But then, señor governor,” replied the querist, “the man will have to be divided into two parts; and if he is divided of course he will die; and so none of the requirements of the law will be carried out, and it is absolutely necessary to comply with it.”"
- **Sancho Panza's mercy rule (same chapter).** Since "as the arguments for condemning him and for absolving him are exactly balanced, they should let him pass freely, as it is always more praiseworthy to do good than to do evil", following a precept from Don Quixote "that when there was any doubt about the justice of a case I should lean to mercy".
- **Modern papers on record, not read.** Dale Jacquette, "Buridan's Bridge", *Philosophy* 66(258), 1991, pp. 455–471 ([doi:10.1017/s0031819100065116](https://doi.org/10.1017/s0031819100065116)), and Joseph W. Ulatowski, "A Conscientious Resolution of the Action Paradox on Buridan's Bridge", *Southwest Philosophical Studies* 25, 2003 (image-only scan); their positions are not reported here because their texts were not read.

## Arguments in play

(none recorded as separate argument pages yet). The dilemma Buridan states
and the propositional check are in The question; the reasoning behind
Buridan's second answer (a promissive conditional falsified by
self-reference) is quoted in Positions taken.

## Thinkers who addressed it

- **Aristotle** (*On Interpretation* I.9) — cited by Buridan for the status of future contingents (Klima n. 197).
- **Thomas Bradwardine** (*Insolubilia*, Oxford, "sometime between 1321 and 1324" per SEP "Insolubles") — gives the case before Buridan, per Spade & Read, who cite "Bradwardine [B-I]: 135" beside "Buridan [B-SD]: 993" for it (SEP "Insolubles" §1.4).
- **John Buridan** (*Sophismata* ch. 8, seventeenth sophism, mid-1350s version per SEP §3.8) — three answers above.
- **Paul of Venice** (*Logica Magna*, c. 1396–7) — classification; see Framings. His *Insolubilia* ch. 5, per Spade & Read, extends his account "to deal with other examples, such as that where Socrates says that his sole business is to be hung on the gallows, which are not obviously insolubles until the background scenario is added" (§4.5).
- **Miguel de Cervantes** (*Don Quixote* II.51, 1615) — the gallows version; Sancho's two answers.
- **G. E. Hughes** (ed. and tr., *John Buridan on Self-Reference*, Cambridge, 1982) — translation with commentary of ch. 8 (SEP bibliography [B-B]).
- **Gyula Klima** (tr. 2001; *John Buridan*, OUP 2009, [doi:10.1093/acprof:oso/9780195176223.001.0001](https://doi.org/10.1093/acprof:oso/9780195176223.001.0001), §10.5) — defends Buridan's theory of insolubles, per Spade & Read.
- **Dale Jacquette** (1991), **Joseph W. Ulatowski** (2003) — papers on the case (bibliographic only).
- **Stephen Read** (2002, [doi:10.1163/156853402320901812](https://doi.org/10.1163/156853402320901812); 2006; 2022) — critic of Buridan's theory of insolubles (with Spade, SEP §3.8); reports Paul of Venice's classification.
- **Jack Zupko** (SEP 2024) — exposition of Buridan's final solution.

## Framings and reframings

- **A liar variant.** Spade & Read list the bridge among "many more insolubles than the Liar Paradox", "most" of which "can be seen as variants of it" (§1.4): "There is also a nice example where a landowner has decreed that only those who speak truly will be allowed across his bridge and those who lie about their business will be thrown in the water (or maybe even hanged on the nearby gallows). When Socrates is challenged on coming to the river, he says “You will throw me in the water” (Bradwardine [B-I]: 135; Buridan [B-SD]: 993; see also Cervantes Don Quixote, vol. II book III ch. XIX, p. 714)."
- **Self-reference through the case, not the sentence.** Buridan locates the reflexivity in the promise: Plato's promise "has reference to itself" "because of Socrates’ proposition" (p. 994). Spade & Read describe Paul of Venice's similar cases as "not obviously insolubles until the background scenario is added" (§4.5).
- **Insoluble or not?** Read reports Paul of Venice's definition — "An insoluble proposition is a proposition having reflection on itself wholly or partially implying its own falsity or that it is not itself true." — and that "Paul comments that his definition excludes many propositions counted as insolubles by others, such as ‘Socrates will not cross the bridge’ and ‘Plato will not have a penny’, for he says, they do not have reflection on themselves. But he is not consistent here, for in the fifth chapter he includes them under what he calls ‘insolubles that don’t appear at first glance to be insolubles’ (insolubilia que prima facie insolubilia non apparent)." (Read 2022, §3, [doi:10.1080/01445340.2022.2040797](https://doi.org/10.1080/01445340.2022.2040797); excerpt: `raw/read-2022-paul-of-venice-socrates-will-not-cross-the-bridge.md`; the inconsistency charge is Read's).
- **A question about promising.** Buridan's own framing is practical — "what should Plato do to keep his promise?" — and his last answer concerns how a promise should be worded, not only a truth value (p. 994).
- **Kinship with the crocodile.** Wikipedia's list entry: "Similar to the crocodile dilemma." (rev. 1376699902); no source for the crocodile case was read here.

Not in the excerpts held: Bradwardine's text ([B-I]: 135), Hughes's
commentary, Klima 2009 §10.5, Read 2002 §5 and 2006 §6, Jacquette 1991,
Ulatowski 2003, Clark's *Paradoxes from A to Z*, and Walter Burley's
treatment reported by Wikipedia; they are left out until a source is read.

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — see The question.
- [Validity](../vocabulary/validity.md) — the strict sense of a conditional in Buridan's second answer (antecedent true without the consequent).
- [Knowledge](../vocabulary/knowledge.md) — Buridan's "I cannot know whether it is true or false" of a future contingent.
- [Classical logic](../methods/classical-logic.md) — the propositional check above.
- *Insoluble (insolubile)*, *sophism*, *future contingent*, *promissive conditional*, *self-reference* — open work in [vocabulary](../vocabulary/index.md).
