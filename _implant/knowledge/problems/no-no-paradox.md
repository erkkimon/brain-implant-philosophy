---
type: article
about: concept
title: "The no-no paradox"
description: "Two sentences each say that the other is false (or not true): only the two divergent truth-value assignments are consistent, and nothing appears to choose between them — Buridan's eighth sophism of Sophismata ch. 8, named the no-no paradox by Sorensen (2001), the 'open pair' of Woodbridge & Armour-Garb (2005); Goldstein's gaps, Sorensen's truthmaker gaps, Priest's gluts, Greenough's liar reading."
tags: [problem, paradox, logic, self-reference, truth, insolubles]
timestamp: 2026-10-01T22:52:16Z
---

# The no-no paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Primary text: Buridan, *Sophismata* ch. 8, eighth sophism, in *Summulae de Dialectica*, tr. Klima, Yale UP 2001, ISBN 0-300-08425-0, pp. 971–974 (excerpt: `raw/buridan-c1350-sophismata-8-8-no-no-klima.md`).
Maps: Spade & Read, [SEP Fall 2024 "Insolubles"](https://plato.stanford.edu/archives/fall2024/entries/insolubles/) §§1.4, 5 (excerpt: `raw/sep-insolubles-fall-2024-no-no-paradox.md`);
Woodbridge & Armour-Garb, "Semantic Pathology and the Open Pair", *PPR* 71(3), 2005, pp. 695–703, [doi:10.1111/j.1933-1592.2005.tb00482.x](https://doi.org/10.1111/j.1933-1592.2005.tb00482.x) (excerpt: `raw/woodbridge-armour-garb-2005-semantic-pathology-open-pair.md`);
DOI-verified records and abstracts in `raw/no-no-paradox-bibliographic-records.md`.
Admitted from Wikipedia's [List of paradoxes, revision 1376699902](https://en.wikipedia.org/w/index.php?title=List_of_paradoxes&oldid=1376699902), "Logic"
(excerpt: `raw/wikipedia-no-no-paradox-rev-1376421880-and-list-entry.md`).

## The question

The list entry: "No-no paradox: Two sentences that each say the other is not true." Buridan's case (p. 971): "Let it be the case that Socrates utters this proposition: ‘Plato says something false’, and none other, and, conversely, Plato utters this: ‘Socrates says something false’, and none other."
Greenough (2011, abstract) states it with "not true": "Consider the following sentences: The neighbouring sentence is not true. The neighbouring sentence is not true. Call these the no-no sentences. Symmetry considerations dictate that the no-no sentences must both possess the same truth-value."
Classically only divergent values are consistent; Spade & Read (SEP 2021/2024, §5): "For example (the ‘no’-‘no’ paradox), where a = ‘b is false’ and b = ‘a is false’, no Liar-type paradox arises; contradiction can be avoided by simply taking one of the two propositions as true and the other as false."
What the medievals found troubling, per the same authors: "But medieval logicians regarded such cases as problematic because they require us to assign different truth values to propositions that are semantically exactly alike; there is no reason to pick a as the true proposition rather than b or conversely (see Read 2006)."
The question is which value each sentence has, whether either has one, and whether symmetry or consistency gives way. Term contracts: [paradox](../vocabulary/paradox.md), [validity](../vocabulary/validity.md), [knowledge](../vocabulary/knowledge.md) (for the epistemic reading below).

**Logic check (this implant, 2026-10-02; logic, not a position).** Let `a` = *the first sentence is true*, `b` = *the second is true*; by the truth schema each premise is the content of one sentence: `a <-> ~b`, `b <-> ~a`.
`logic.py check --premises "a <-> ~b" "b <-> ~a" --conclusion "a"` outputs "INVALID" with the counterexample "a=F, b=T"; with conclusion `~a` it outputs "INVALID" with the counterexample "a=T, b=F" — so exactly two rows satisfy both premises, one per divergent assignment.
With conclusion `~(a <-> b)` it outputs "VALID". Adding the symmetry premise `a <-> b` (conclusion `a`) outputs "premises are jointly inconsistent — argument is vacuously valid".
The tool does not decide between the two rows, or whether symmetry, bivalence or the truth schema gives way; the positions below differ on that.

## Why it matters

- **Pathology without contradiction.** Woodbridge & Armour-Garb (2005, p. 696): "(1) and (2) together yield inconsistency, if we ascribe them matching truth-values. But inconsistency is not inevitable here; we can avoid it by claiming one of these sentences is true and the other false. This, however, yields indeterminacy, as there are two ways of ascribing divergent truth-values, and nothing appears to favor one over the other."
- **A semantic principle of sufficient reason.** Spade & Read (§5): "Cases like this, which violate only a kind of semantic “principle of sufficient reason”, were often included under the heading “insolubles” (for example, Buridan, Sophismata VIII.8)."
- **Ungrounded sentences.** The Wikipedia article (rev. 1376421880, "Discussion"), citing Herzberger 1970: "Generally speaking, the paradox instantiates the problem of determining the status of ungrounded sentences that are not inconsistent."
- **Vagueness.** Per Woodbridge & Armour-Garb (p. 695), Sorensen uses his solution "as a precedent for an epistemic account of the sorites paradox"; they quote him (p. 702): "“the truthmaker gap solution to the [open pair] is a precedent for an epistemic solution to the sorites paradox” (p. 176)." See [the sorites paradox](sorites-paradox.md).
- **Truthmaking.** Greenough (2011, abstract) reports Sorensen's claim that the sentences "are bivalent but give rise to “truthmaker gaps”"; the Wikipedia article reads this as a challenge to truthmaker maximalism (citing Sorensen 2001, p. 176), contested by López de Sa & Zardini 2007 (not read).

## Positions taken

Not ranked; each is reported with the source that records it.

- **Both false (Buridan).** "We should briefly reply that Socrates’ proposition is false and not true, for every proposition is false that, along with something true, entails something false;" and "and similarly, for the same reason, we would have to say that Plato’s proposition would be false." (p. 972). The SEP "Insolubles" (§3.8) gives his later theory: "Rather, his later theory claims that every proposition virtually implies another proposition asserting the truth of the first." (excerpt: `raw/sep-insolubles-fall-2024-bridge-variety-and-buridan.md`).
- **Truth-value gaps (Goldstein 1992).** As reported by Woodbridge & Armour-Garb (p. 697), from two assumptions — "(DA) If each statement in [the open pair] has a unique truth-value, then each has the opposite value of the other." and "(SA) If each statement in [the open pair] has a unique truth-value, then each has the same value as the other." — "As Goldstein rejects inconsistency, he concludes that the antecedent of both (DA) and (SA) is false and thus that each sentence suffers from a truth-value gap."
- **Divergent values, unknowable, truthmaker gap (Sorensen 2001).** The chapter is "Chapter 11" per Woodbridge & Armour-Garb (p. 695), "Truthmaker Gaps", pp. 165–184 per Crossref. Per Woodbridge & Armour-Garb (p. 696), Sorensen "maintains that (1) and (2) have determinate, consistent truth-values, though which truth-value each sentence has is epistemically indeterminate."; a truthmaker gap is one "where a truthmaker gap obtains when a true sentence is not made true by anything else in the world." (p. 698). Greenough's (2011, abstract) summary of Sorensen (2001, 2005a, 2005b) includes "(4) It is metaphysically impossible to know these truth-values."
- **Both true and false (Priest 2005, "Words Without Knowledge", not read).** As reported by Woodbridge & Armour-Garb (p. 702): "Priest, in his contribution to this symposium, argues that the open pair requires a dialetheic resolution." Divergent values are, in Priest's words as they quote him, "maintaining that (1) and (2) have different semantic properties is “a manifest a priori repugnance” (Priest (2004), p. 6)."; against gaps, "Priest (2004), fn. 3 argues that an ascription of gaps leads to an assignment of both gaps and gluts, so it is simpler, methodologically speaking, just to go with gluts." See [Priest](../thinkers/priest.md).
- **Both true for the "definite" variant (Sorensen 2003/2004).** Woodbridge & Armour-Garb (p. 700, n. 10) report: "Here Sorensen notes, “Symmetry precludes one from being true while the other is false” (p. 228)."
- **A form of the liar (Greenough 2011).** "In consequence, the no-no paradox is best seen as a form of the liar paradox. As such, it cannot provide a case for epistemicism." (abstract). Sorensen, as Greenough summarises him, holds the opposite: "(1) The no-no paradox is not a version of the liar but rather a cousin of the truth-teller paradox."

**Cases for and against.** Each objection below is its author's; replies on record are given where read.

- *Against Buridan:* his opponents' argument P.1 (p. 971): "for there is no reason why Socrates’ proposition should be true or false rather than Plato’s, or conversely, for they are related to each other in exactly the same way." *For:* his replies to P.1–P.4 (pp. 972–974); he calls the arguments "very difficult" (p. 972).
- *Against Goldstein:* Woodbridge & Armour-Garb (p. 698) give an "asymmetric open pair" — "(5) (6) is false (6) (6) is false → (5) is false." — where (SA) has no ground, so gaps are not derived. *For:* (none recorded in the sources read).
- *Against Sorensen:* the revenge pair "(7) (8) has no truthmaker (8) (7) has no truthmaker." (p. 699) and further variants; their conclusion (p. 701): "Sorensen does not meet this condition of adequacy, thereby leaving the semantic pathology of the open pair both undiagnosed and untreated." Greenough (abstract) cites "the dunno-dunno paradox, the strengthened no-no paradox, and the strengthened truth-teller paradox". *For:* Woodbridge & Armour-Garb (p. 699) grant: "As this approach already denies the apparent force of symmetry, the version of the open pair that thwarts Goldstein’s reliance on (SA) poses no challenge for Sorensen."; López de Sa & Zardini 2011 (not read) is a later contribution.
- *Against Priest:* Woodbridge & Armour-Garb (p. 702): "For, although the dialetheist can ascribe the same truth-value to (5) and (6), (9) and (10), or (13) and (14), he can also consistently ascribe them divergent truth-values, with no apparent reason for favoring any matching or divergent assignment over any other." *For:* Priest's own paper (not read); see the dialetheism excerpt `raw/sep-dialetheism-fall-2024-priest-liar-inclosure-curry-objections.md` for his general view.

No survey figure is recorded.

## Arguments in play

(none as separate argument pages yet). Related problems: [the liar paradox](liar-paradox.md), from which Spade & Read (§5) separate the case ("no Liar-type paradox arises") and Greenough assimilates it; [Buridan's bridge](buridans-bridge.md), the seventeenth sophism of the same chapter; [the card paradox](card-paradox.md), a two-sentence cycle; compare the medieval "yes"-"no" case Spade & Read (§1.4) report beside this one, "Socrates says “What Plato is saying is false”, while Plato says “What Socrates is saying is true”"; [Yablo's paradox](yablos-paradox.md); [Curry's paradox](currys-paradox.md), on whose model Woodbridge & Armour-Garb (p. 700, n. 11) build "what we call the curried open pair"; [the sorites paradox](sorites-paradox.md).

## Thinkers who addressed it

- **Thomas Bradwardine** (c. 1321–1324) — "A variation on the paradox occurs already in Thomas Bradwardine’s Insolubilia." (Wikipedia, rev. 1376421880, citing the Roure 1970 edition, pp. 304–305; not checked here).
- **John Buridan** (mid-1350s) — *Sophismata* ch. 8, eighth sophism, "and it seems to me to be more difficult" (p. 971); both propositions false.
- **Albert of Saxony** — a three-sentence cycle, the "‘no’-‘no’-‘no’ paradox" (Spade & Read §1.4, citing [AS-I]: 353).
- **Hans Herzberger** (1970) — ungrounded sentences, as cited by the Wikipedia article.
- **Laurence Goldstein** (1992) — truth-value gaps, per Woodbridge & Armour-Garb (p. 696).
- **Roy Sorensen** (2001, ch. "Truthmaker Gaps", [doi:10.1093/oso/9780199241309.003.0012](https://doi.org/10.1093/oso/9780199241309.003.0012); "A Definite No-No", 2004, [doi:10.1093/oso/9780199264803.003.0011](https://doi.org/10.1093/oso/9780199264803.003.0011); précis, PPR 2005) — the name, per Woodbridge & Armour-Garb (p. 695): "what he calls the no-no paradox—a “neglected cousin” of the more famous liar".
- **Graham Priest** (2005, PPR 71(3): 686–694, [doi:10.1111/j.1933-1592.2005.tb00481.x](https://doi.org/10.1111/j.1933-1592.2005.tb00481.x)) — dialetheic resolution, as reported above.
- **James Woodbridge and Bradley Armour-Garb** (2005; and Armour-Garb & Woodbridge 2006, *AJP* 84(3): 395–416, [doi:10.1080/00048400600895912](https://doi.org/10.1080/00048400600895912), abstract only) — the "open pair"; the 2006 abstract: "The problem that we present seems to have broader bite, afflicting both consistent and inconsistent proposals for resolving semantic pathology."
- **Stephen Read** (2006, "Symmetry and Paradox", *HPL* 27(4): 307–318, [doi:10.1080/01445340600593942](https://doi.org/10.1080/01445340600593942), not read) — cited by Spade & Read (§5).
- **Dan López de Sa and Elia Zardini** (2007, [doi:10.1111/j.1467-8284.2007.00681.x](https://doi.org/10.1111/j.1467-8284.2007.00681.x); 2011, "No-no. Paradox and consistency", [doi:10.1093/analys/anr044](https://doi.org/10.1093/analys/anr044); not read).
- **Patrick Greenough** (2011, *PPR* 82(3): 547–563, [doi:10.1111/j.1933-1592.2011.00491.x](https://doi.org/10.1111/j.1933-1592.2011.00491.x), abstract only) — a form of the liar.

## Framings and reframings

- **Pathological, not paradoxical.** Woodbridge & Armour-Garb (p. 695, n. 1) prefer the name "open pair" because "while the open pair is pathological, it is not paradoxical because it does not force inconsistency."
- **Cousin of the truth-teller, or of the liar.** Sorensen, per Greenough's summary, files it with the truth-teller; Greenough with the liar (abstract, quoted above). Woodbridge & Armour-Garb (p. 695): "It is widely appreciated that this phenomenon bifurcates into two symptoms: inconsistency, as manifested in liar sentences (e.g., ‘This sentence is false’), and indeterminacy, as manifested in truth-teller sentences (e.g., ‘This sentence is true’)." Of the pair (p. 696): "In fact, this case will manifest either symptom of resistance, depending on what we say about these sentences."
- **Equivalence and reference (Buridan).** To the variant where Robert says the same words as Socrates, Buridan replies: "Socrates’ proposition and Robert’s proposition are similar in utterance and intention of the speaker and hearer alike, and yet they are not equivalent, because Plato’s proposition, of which both of them were speaking, is referring to [habet reflexionem super] Socrates’ proposition and not to Robert’s proposition." (pp. 972–973).
- **Symmetry breaking.** Woodbridge & Armour-Garb's asymmetric pairs (pp. 698–701) separate the symmetry worry from the indeterminacy worry.

## Vocabulary

- [Paradox](../vocabulary/paradox.md); [Validity](../vocabulary/validity.md);
  [Knowledge](../vocabulary/knowledge.md); [Classical logic](../methods/classical-logic.md), in which the logic check above is run; [Tarski](../thinkers/tarski.md): Greenough (abstract) runs the argument through "Tarski’s truth-schema—if a sentence S says that p then S is true iff p—".
- Insoluble, truth-value gap, glut (dialetheia), truthmaker gap, truth-teller, open pair, groundedness, epistemicism — open work in [vocabulary](../vocabulary/index.md).
