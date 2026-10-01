---
type: article
about: concept
title: "The Epicurean trilemma and the logical problem of evil"
description: "Can a God who is omnipotent, omniscient and perfectly good coexist with evil? The ancient willing/able dilemma Lactantius attributes to Epicurus and Hume restates, Mackie's 1955 inconsistency charge, the responses (free will defence, soul-making, privation, skeptical theism, denying an attribute) with the case for and against each, and Rowe's evidential argument as a distinct problem."
tags: [problem, dilemma, philosophy-of-religion, metaphysics, ethics]
timestamp: 2026-10-01T19:31:15Z
---

# The Epicurean trilemma and the logical problem of evil

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
sources graded as in [How claims are graded](../../conventions/how-claims-are-graded.md).
Main source: Tooley, [SEP Fall 2024 "The Problem of Evil"](https://plato.stanford.edu/archives/fall2024/entries/evil/)
(substantive revision 2015; excerpt: `raw/sep-evil-fall-2024-logical-evidential-and-responses.md`);
where Tooley evaluates, the evaluation is his. Other excerpts are named at each claim.

## The question

**The ancient form.** Lactantius, *De Ira Dei* 13 (Fletcher trans., 1886, [New Advent](https://www.newadvent.org/fathers/0703.htm); excerpt: `raw/lactantius-de-ira-dei-13-epicurus-argument-fletcher.md`), introduces "that argument also of Epicurus":
"God, he says, either wishes to take away evils, and is unable; or He is able, and is unwilling; or He is neither willing nor able, or He is both willing and able. If He is willing and is unable, He is feeble, which is not in accordance with the character of God; if He is able and unwilling, He is envious, which is equally at variance with God; if He is neither willing nor able, He is both envious and feeble, and therefore not God; if He is both willing and able, which alone is suitable to God, from what source then are evils? Or why does He not remove them?"
Hume's Philo, *Dialogues Concerning Natural Religion* Part X (1779; [Gutenberg #4583](https://www.gutenberg.org/cache/epub/4583/pg4583.txt); excerpt: `raw/hume-1779-dialogues-part-10-epicurus-old-questions.md`), gives three questions:
"EPICURUS's old questions are yet unanswered. Is he willing to prevent evil, but not able? then is he impotent. Is he able, but not willing? then is he malevolent. Is he both able and willing? whence then is evil?"
Lactantius lists four cases, Hume three; Wikipedia's "Epicurean paradox"
page calls the argument "this trilemma" (excerpt:
`raw/epicurean-trilemma-attribution-sources-okeefe-russell-wikipedia.md`).
Structural note (this implant): in the argument-form sense of
[dilemma](../vocabulary/dilemma.md) both are constructive dilemmas with
more than two horns, closed by the fact of evil.

**The modern form.** Mackie, "Evil and Omnipotence", *Mind* 64 (1955):
200–212, [doi:10.1093/mind/LXIV.254.200](https://doi.org/10.1093/mind/LXIV.254.200)
(bibliographic data verified; the article was not read), as Beebe quotes him
([IEP "Logical Problem of Evil"](https://iep.utm.edu/evil-log/) §1; excerpt:
`raw/iep-evil-log-beebe-and-evil-evi-trakakis-mackie-plantinga-rowe-wykstra.md`):
"Evil is a problem, for the theist, in that a contradiction is involved in the fact of evil on the one hand and belief in the omnipotence and omniscience of God on the other." (p. 200).
Beebe's set is (1) God is omnipotent, (2) omniscient, (3) perfectly good,
(4) evil exists; "None of the statements in (1) through (4) directly contradicts any other"
(§1); Beebe therefore adds premises (6)–(8) connecting each attribute to
the prevention of evil. Tooley (§1.1) gives a seven-line
version and holds that "premises (1) through (6) do validly imply (7)".

**Logic check (this implant, 2026-09-27; logic, not a position).**
`logic.py` on the propositional core — *g* God is perfectly good, *o*
omnipotent, *w* omniscient, *e* evil exists:
premises `g & o & w -> ~e`, `e`, conclusion `~(g & o & w)` — output "VALID".
Tooley's seven lines (*x* God exists; *o*, *n*, *m* omnipotent, omniscient,
morally perfect; *p*, *k*, *d* has the power / knows / desires to eliminate
evil): `x -> o & n & m`, `o -> p`, `n -> k`, `m -> d`, `e`,
`e & x -> ~p | ~k | ~d`, conclusion `~x` — output "VALID".
Lactantius' four cases (*w* willing, *a* able, *g* is God):
`w & ~a -> ~g`, `a & ~w -> ~g`, `~w & ~a -> ~g`, `w & a -> ~e`, `e`,
conclusion `~g` — output "VALID"; with the case `~w & ~a -> ~g` removed,
output "INVALID" with "a=F, e=T, g=T, w=F", so the form needs every case.
Validity is a matter of form ([validity](../vocabulary/validity.md)); every
response below denies or qualifies a premise.

## Why it matters

- Tooley (§1.1): if God is conceived in purely metaphysical terms with no link to power, knowledge and goodness, "the problem of evil is irrelevant"; and "But when that is the case, it would seem that God thereby ceases to be a being who is either an appropriate object of religious attitudes, or a ground for believing that fundamental human hopes are not in vain."
- Russell ([SEP "Hume on Religion"](https://plato.stanford.edu/archives/fall2024/entries/hume-religion/) §5) on the *Dialogues*: "It is clear, as Cleanthes acknowledges, that if this cannot be done then the case for theism in any traditional form will collapse (D, 10.28/199)."
- Beebe (§1) reports a Barna survey for Strobel: "The most common response, offered by 17% of those who could think of a question was “Why is there pain and suffering in the world?” (Strobel 2000, p. 29)."
- Lactantius (ch. 13): "many of the philosophers, who defend providence, are accustomed to be disturbed by this argument".

## Positions taken

Tooley divides responses into "total refutations, theodicies, and defenses"
(§4); a defence, against incompatibility versions, means "attempts to show that there is no logical incompatibility between the existence of evil and the existence of God."
Beebe (§9) calls Plantinga's response "merely a “defense”" and Hick's "a “theodicy”". No response is ranked here;
each has its case for and against from the sources held. No survey of
philosophers on this question was fetched.

**Accept the conclusion (atheological).** Mackie (1955, p. 200, as quoted by Beebe §8): religious beliefs "are positively irrational, that several parts of the essential theological doctrine are inconsistent with one another."
Against: the responses below, each of which denies or qualifies a premise.

**Deny an attribute.** Beebe (§1): "Rabbi Harold Kushner (1981) offers the following escape route for the theist: deny the truth of (1)."
Calder ([SEP "The Concept of Evil"](https://plato.stanford.edu/archives/fall2024/entries/concept-evil/) §2.1; excerpt:
`raw/augustine-enchiridion-11-privation-shaw-and-sep-concept-evil-calder.md`): "The Manichaean solution to the problem of evil is that God is neither all-powerful nor the sole creator of the world."
Against: Beebe (§1) judges it "would not be a very palatable option to many theists"; Calder (§2.1): "Since its inception, Manichaean dualism has been criticized for providing little empirical support for its extravagant cosmology."

**Morally sufficient reason (the general defence).** Beebe (§3): "(17) It is possible that God has a morally sufficient reason for allowing evil."
If so, (12′) reads "either: a) God is not omnipotent, not omniscient, or not perfectly good; or b) God has a morally sufficient reason for allowing evil."
*Logic check (this implant):* with *r* for the reason, `e -> ~o | ~n | ~g | r`, `e`,
conclusion `~(o & n & g)` — output "INVALID", counterexample
"e=T, g=T, n=T, o=T, r=T". Tooley (§1.3) names two candidate reasons —
evils "logically necessary for goods that outweigh them", and "The good of libertarian free will requires, in short, the possibility of moral evil." — and adds
"Neither of these lines of argument is immune from challenge."

**Free will defence — Plantinga** (*God, Freedom, and Evil*, 1974a;
*The Nature of Necessity*, 1974b, as Tooley's bibliography gives them;
quoted only through Beebe §4, whose "1974" is *The Nature of Necessity*).
For: Plantinga (1974, p. 190): "The essential point of the Free Will Defense is that the creation of a world containing moral good is a cooperative venture; it requires the uncoerced concurrence of significantly free creatures."
And (pp. 166–167): "The fact that these free creatures sometimes go wrong, however, counts neither against God’s omnipotence nor against his goodness; for he could have forestalled the occurrence of moral evil only by excising the possibility of moral good."
Mackie later (*The Miracle of Theism*, 1982, p. 154, as Beebe §8 quotes): "we can concede that the problem of evil does not, after all, show that the central doctrines of theism are logically inconsistent with one another. But whether this offers a real solution of the problem is another question."
Beebe (§8): "As an attempt to rebut the logical problem of evil, it is strikingly successful."
Against: Mackie (1955, p. 209, as Beebe §4 quotes): "there was open to him the obviously better possibility of making beings who would act freely but always go right."
Beebe (§10), from heaven and God's own freedom: "If W3 is possible, then the complaint lodged by Flew and Mackie above that God could (and therefore should) have created a world full of creatures who always did what is right is not answered."
Tooley (§7.2): "the fact that libertarian free will is valuable does not entail that one should never intervene in the exercise of libertarian free will."; natural evils "certainly do not appear to result from morally wrong actions"; Plantinga's suggestion that they may be due to "supernatural beings" is reported there (Plantinga 1974a, 58).

**Soul-making theodicy — Hick** (*Evil and the God of Love*, 1966, rev.
1978; quoted from the 1977 edition by Tooley §7.1 and Beebe §9).
For: Hick (1977, 255–6): "one who has attained to goodness by meeting and eventually mastering temptation, and thus by rightly making responsibly choices in concrete situations, is good in a richer and more valuable sense than would be one created ab initio in a state either of innocence or of virtue."
Against: Tooley (§7.1): "there seems to be no reason at all why a world must contain horrendous suffering if it is to provide a good environment for the development of character in response to challenges and temptations."; it "provides no justification for the existence of any animal pain"; and "no account of the suffering that young, innocent children endure".

**Evil needed for wisdom — Lactantius** (*De Ira Dei* 13), his own answer
to the argument he reports: "He is able, therefore, to take away evils; but He does not wish to do so, and yet He is not on that account envious. For on this account He does not take them away, because He at the same time gives wisdom, as I have shown; and there is more of goodness and pleasure in wisdom than of annoyance in evils."
Against: (none recorded in the sources held for this reply specifically).

**Privation — Augustine** (*Enchiridion* 11, Shaw trans. 1887,
[New Advent](https://www.newadvent.org/fathers/1302.htm)).
For: "For what is that which we call evil but the absence of good?"; Calder (§2.1): "The Neoplatonist theory of evil provides a solution to the problem of evil because if evil is a privation of substance, form, and goodness, then God creates no evil."
Against: Calder (§2.1): it "provides only a partial solution to the problem of evil since even if God creates no evil we must still explain why God allows privation evils to exist (See Calder 2007a; Kane 1980)."; and "Pain is a distinct phenomenological experience which is positively bad and not merely not good."

**Skeptical theism — Wykstra** (1984, *Int. J. Philos. Religion* 16:
73–93, [doi:10.1007/bf00136567](https://doi.org/10.1007/bf00136567); not
read). Perrine ([SEP "Skeptical Theism"](https://plato.stanford.edu/archives/fall2024/entries/skeptical-theism/); excerpt:
`raw/sep-skeptical-theism-fall-2024-cornea-and-objections.md`) calls it "a family of responses to arguments from evil" "reintroduced into the contemporary literature in a 1984 paper by Stephen Wykstra";
Trakakis (§3) and Tooley (§5.1) discuss it as a reply to evidential
arguments (next section).
For: Wykstra (1984: 91, as Trakakis quotes, [IEP](https://iep.utm.edu/evil-evi/) §3b): "it is entirely expectable – given what we know of our cognitive limits – that the goods by virtue of which this Being allows known suffering should very often be beyond our ken"; Alston (1991: 61, as Trakakis §3 quotes): "the inductive argument from evil is in no better shape than its late lamented deductive cousin".
Against: Tooley (§5.1): "Short of embracing compete inductive skepticism, then, it would seem that an appeal to human cognitive limitations cannot provide an answer to evidential versions of the argument from evil."
Perrine reports a regress objection to CORNEA (Swinburne 1998: 32–3, §5.1)
and a moral-deliberation objection (Almeida and Oppy 2003: 505–7; Piper
2007: 71ff; Rancourt 2013, §6.1).

## Arguments in play

- **The evidential argument — Rowe** ("The Problem of Evil and Some Varieties of Atheism", *American Philosophical Quarterly* 16 (1979): 335–41, per Tooley's bibliography; no DOI found in Crossref — the candidate 10.2307/20009775 returns 404). As Trakakis (§2a) quotes it: "There exist instances of intense suffering which an omnipotent, omniscient being could have prevented without thereby losing some greater good or permitting some evil equally bad or worse."
  and "An omniscient, wholly good being would prevent the occurrence of any intense suffering it could, unless it could not do so without thereby losing some greater good or permitting some evil equally bad or worse." Trakakis (introduction) separates it from logical arguments, "which have the more ambitious aim of showing that, in a world in which there is evil, it is logically impossible—and not just unlikely—that God exists."
- **Hume's indirect evidential form.** Philo concedes compatibility — "A mere possible compatibility is not sufficient." (Part X) — and in Part XI offers four hypotheses about the first causes, of which "The fourth, therefore, seems by far the most probable."; Tooley (§§3.1, 3.3) reads this as the indirect inductive approach later developed by Draper.
- **Tooley on abstract versions.** Tooley (§1.3) judges Plantinga's view that what remains is "“pastoral care”" to be "very implausible", and holds that "To concentrate exclusively on abstract versions of the argument from evil is therefore to ignore the most plausible and challenging versions of the argument."
  Beebe (§8) reports the shift: "Current discussions of the problem focus on what is called “the probabilistic problem of evil” or “the evidential problem of evil.”"
- Probabilistic machinery: [Bayesian updating](../methods/bayesian-updating.md) (Tooley §3.1 reports a "Bayesian approach" "advanced by William Rowe"; §3.4 not excerpted).

## Thinkers who addressed it

- **Epicurus** — attributed author (Lactantius, *De Ira Dei* 13; Hume, *Dialogues* X); see Framings on the attribution.
- **Lactantius** — reports the four-case argument and answers that evils are the condition of wisdom (*De Ira Dei* 13).
- **Augustine** — evil as "the absence of good" (*Enchiridion* 11).
- **David Hume** — Philo's three questions (Part X) and four hypotheses (Part XI), 1779.
- **J. L. Mackie** — the inconsistency charge (1955, p. 200); later concession on the free will defence (1982, p. 154, as quoted by Beebe).
- **John Hick** — soul-making theodicy (1966).
- **Alvin Plantinga** — free will defence (1974a, 1974b).
- **William Rowe** — evidential argument (1979).
- **Stephen Wykstra** — CORNEA and skeptical theism (1984).
- **Michael Tooley** — SEP author; a fourth, inductive-logic approach of his own (§3.1).

## Framings and reframings

- **Who first stated it.** Lactantius attributes the argument to Epicurus;
  in the same chapter he reports that "the Academics, arguing against the Stoics," asked why many things are "injurious to us" (see [Stoicism](../schools/stoicism.md)).
  O'Keefe ([IEP "Epicurus"](https://iep.utm.edu/epicur/) §3): "Epicurus is one of the earliest philosophers we know of to have raised the Problem of Evil".
  Wikipedia ("Epicurean paradox", [rev. 1368515956](https://en.wikipedia.org/w/index.php?title=Epicurean_paradox&oldid=1368515956)): "There is no text by Epicurus confirming his authorship of the argument." — citing McBrayer 2013 without a page; it also reports that Glei "believes that the theodicy argument is from a non-Epicurean or anti-Epicurean academic source".
  Glei's article, "Et invidus et inbecillus. Das angebliche Epikurfragment
  bei Laktanz, De ira Dei 13,20–21" ("the alleged Epicurus fragment"),
  *Vigiliae Christianae* 42 (1988): 47–58, [doi:10.1163/157007288x00327](https://doi.org/10.1163/157007288x00327),
  was not read. Wikipedia's further claims — that the oldest version is in
  Sextus Empiricus and that Hume took it from Bayle — carry no citation
  there and are not verified here.
- **Logical vs. evidential.** Tooley (§1.2) sets the "purely deductive" form beside an evidential one "for the more modest claim".
- **Defence vs. theodicy.** Tooley (§4): a consistent story "will do nothing to show that evil does not render the existence of God unlikely, or even very unlikely."

## Vocabulary

- [Dilemma](../vocabulary/dilemma.md) — argument-form sense; "trilemma" is
  the three-horn case. Not a [moral dilemma](moral-dilemmas.md).
- [Validity](../vocabulary/validity.md), [classical logic](../methods/classical-logic.md) — what the checks show.
- [Paradox](../vocabulary/paradox.md) — Wikipedia's title uses it.
- Jung's *[Answer to Job](../works/answer-to-job.md)* (1952), which Ryan
  (1983) reads as a work on the problem of evil, with Jung's objection to
  the *privatio boni*.
- Omnipotence, theodicy, defence, gratuitous evil, CORNEA — open work in
  [vocabulary](../vocabulary/index.md).

Related problems: [the Euthyphro dilemma](euthyphro-dilemma.md),
[the Agrippan trilemma](agrippan-trilemma.md),
[moral dilemmas](moral-dilemmas.md). Branch: [Problems](./index.md).
