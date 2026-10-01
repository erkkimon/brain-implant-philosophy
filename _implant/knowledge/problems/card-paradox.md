---
type: article
about: concept
title: "The card paradox (Jourdain's)"
description: "A card reads on one side 'The sentence on the other side of this card is TRUE' and on the other 'The sentence on the other side of this card is FALSE' — the two-sentence liar cycle credited to P. E. B. Jourdain (1913) and, by Sorensen, to G. G. Berry; no sentence refers to itself, yet the pair yields a liar-style contradiction, which the SEP entries use to separate self-reference from circular reference."
tags: [problem, paradox, logic, self-reference, truth, philosophy-of-language]
timestamp: 2026-10-01T22:52:16Z
---

# The card paradox (Jourdain's)

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md),
a variant of [the liar paradox](liar-paradox.md).
Maps: Bolander, [SEP Fall 2024 "Self-Reference and Paradox"](https://plato.stanford.edu/archives/fall2024/entries/self-reference/)
§§1.6, 3.1 (excerpt: `raw/sep-self-reference-fall-2024-postcard-paradox.md`);
Beall, Glanzberg & Ripley, [SEP Fall 2024 "Liar Paradox"](https://plato.stanford.edu/archives/fall2024/entries/liar-paradox/)
§§1.3, 1.5, 2.3 (excerpt: `raw/sep-liar-paradox-fall-2024-liar-cycles.md`).
Attribution and date: O'Connor & Robertson, [MacTutor, "Philip Edward Bertrand Jourdain"](https://mathshistory.st-andrews.ac.uk/Biographies/Jourdain/)
(February 2005; excerpt: `raw/mactutor-jourdain-2005-card-paradox.md`).
Admitted from Wikipedia's [List of paradoxes, revision 1376699902](https://en.wikipedia.org/w/index.php?title=List_of_paradoxes&oldid=1376699902),
"Logic", and compared with the article [Card paradox, revision 1328189446](https://en.wikipedia.org/w/index.php?title=Card_paradox&oldid=1328189446)
(excerpt: `raw/wikipedia-card-paradox-entry.md`).

## The question

MacTutor (O'Connor & Robertson 2005) reports: "In 1913 Jourdain proposed the card paradox. This was a card on one side of which was printed:- The sentence on the other side of this card is TRUE. On the other side of the card the sentence read:- The sentence on the other side of this card is FALSE."
The biography names no publication; Jourdain's 1913 *Monist* note "A
Correction and Some Remarks" (archive.org `jstor-27900419`), searched for
this page, has no card in it. The primary 1913 text was not found and is
not quoted here.

Bolander's postcard wording (SEP 2024, §1.6): "In the postcard paradox, the front side of a postcard reads “the sentence on the back side is true”, whereas the back side reads “the sentence on the front side is false”. For the sentence on the front to be true, the sentence on the back needs to be true, but for the sentence on the back to be true, the sentence on the front needs to be false. This is a contradiction, achieved similarly as in the liar paradox."
The Wikipedia list (rev. 1376699902) words it: "Card paradox: "The next statement is true. The previous statement is false." A variant of the liar paradox in which neither of the sentences employs (direct) self-reference, instead this is a case of circular reference."
The article (rev. 1328189446) argues by cases: "If the first statement is true, then so is the second. But if the second statement is true, then the first statement is false. It follows that if the first statement is true, then the first statement is false."
and "If the first statement is false, then the second is false, too. But if the second statement is false, then the first statement is true. It follows that if the first statement is false, then the first statement is true."

The SEP "Liar Paradox" gives the same structure as a dialog: "Max: Agnes’ claim is true. Agnes: Max’s claim is not true." and derives: "Hence, what Max said is true if and only if what Max said is not true." (Beall, Glanzberg & Ripley, §1.3).
The question is which of the principles used — that each side says
something true or false, that a sentence calling another true is true just
when that other is, and the classical logic of the step — gives way, and
whether a contradiction without any self-referring sentence calls for a
different diagnosis from the one-sentence liar. Term contracts:
[paradox](../vocabulary/paradox.md), [validity](../vocabulary/validity.md).

**Logic check (this implant, 2026-10-02; logic, not a position).** Let `A`
= *the front sentence is true*, `B` = *the back sentence is true*, reading
"false" as "not true" (as the SEP Max–Agnes version does). What the front
says gives `A <-> B`; what the back says gives `B <-> ~A`.
`logic.py check --premises "A <-> B" "B <-> ~A" --conclusion "A & ~A"`
outputs "VALID" and "premises are jointly inconsistent — argument is
vacuously valid"; the same holds with conclusion `A <-> ~A`. With the
premise `A <-> B` alone and conclusion `A <-> ~A` it outputs "INVALID"
(counterexamples "A=T, B=T" and "A=F, B=F"); with premises `A <-> B` and
`B <-> A` (both sides saying "true") and conclusion `A`, "INVALID"
(counterexample "A=F, B=F"). So in classical propositional logic the
contradiction needs the back sentence's negation; a two-"true" card is
consistent and leaves its value open. The tool does not check the step
from the card's sentences to the two biconditionals, which rests on
principles of truth, not on propositional logic.

## Why it matters

- **Self-reference is not required.** Beall, Glanzberg & Ripley (§1.5): "Liar cycles (e.g., the Max–Agnes dialog) show that explicit self-reference is not necessary, but it is clear that such cycles themselves involve circular reference."
- **Indirect self-reference.** Bolander (§1.6) introduces the postcard as his example of the claim "However, it is easy to construct paradoxes that only employ indirect self-reference, i.e., sentences that refer to other sentences that refer to yet other sentences in such a way as to form a loop back to the original sentence."
- **A step towards Yablo.** Both entries place the cycle between the liar and [Yablo's paradox](yablos-paradox.md): "Yablo (1993b) has argued that a more complicated kind of multi-sentence paradox produces a Liar without circularity." (Beall, Glanzberg & Ripley, §1.5); the Wikipedia article: "Yablo's paradox is a variation of the liar paradox that is intended to not even rely on circular reference."
- **What the liar relies on.** Beall, Glanzberg & Ripley (§2.3): "Putting aside Yablo-type paradoxes, the Liar relies on some form of self-reference, either direct, as in in the simple Liars above, or indirect, as in Liar cycles." ("as in in" sic).

## Positions taken

Not ranked; each is reported with the source that records it. The sources
read discuss the card only as one case of the liar family; responses to
[the liar paradox](liar-paradox.md) in general (truth-value gaps,
dialetheism, revision theory and others) are mapped on that page, and the
sources read do not apply them to the card separately.

- **Hierarchy of languages (Tarski's approach, as Bolander reports it).** Bolander (§3.1): "Building explicit hierarchies is sufficient to avoid circularity, and thus sufficient to block the standard paradoxes of self-reference." In such a hierarchy a sentence can only speak of the truth of sentences at lower levels; for a pair that speak of each other, Bolander's example from Kripke 1975 (below) shows each would have to be above the other. See [Tarski](../thinkers/tarski.md).
- **Against excluding such pairs (Kripke 1975, as Bolander reports it).** Kripke's Nixon–Jones pair refer to each other's utterances, and "In a Tarskian language hierarchy, the sentence \(N\) would have to be on a higher level than all of Jones’ utterances, and, conversely, the sentence \(J\) would have to be on a higher level than all of Nixon’s utterances." Bolander (§3.1): "Kripke uses the fact that \(N\) and \(J\) are only problematic in a certain special case as an argument against an approach that altogether excludes the possibility of formulating \(N\) and \(J\)." Kripke, "Outline of a Theory of Truth", *Journal of Philosophy* 72 (1975), [doi:10.2307/2024634](https://doi.org/10.2307/2024634) (not read; DOI checked).
- **Bolander's report of the field.** Bolander (§3.1): "Building an explicit (well-founded) hierarchy to solve the paradoxes is today by most considered an overly drastic and heavy-handed approach." This is the encyclopedia author's report; no survey is cited for it.

**Cases for and against.** Beyond the two hierarchy items above, the
sources read record no argument for or against any response specific to
the card; none is recorded here. No survey figure is recorded.

## Arguments in play

(none as separate argument pages yet). Related problems:
[the liar paradox](liar-paradox.md), of which the SEP and Wikipedia call
it a variant or cycle; [the no-no paradox](no-no-paradox.md), the sibling
two-sentence case in the Wikipedia list ("Two sentences that each say the
other is not true", rev. 1376699902); [Yablo's paradox](yablos-paradox.md);
[the Epimenides paradox](epimenides-paradox.md);
[the Berry paradox](berry-paradox.md), whose source Sorensen also credits
with the postcard (below).

## Thinkers who addressed it

- **Philip E. B. Jourdain** (1879–1919) — proposed the card in 1913, per MacTutor ("In 1913 Jourdain proposed the card paradox"); Bolander (§1.6): "One example is the postcard paradox, often attributed to Philip Jourdain (1879–1919), though according to Roy Sorensen (2003, p. 332), the true inventor is G.G. Berry (1867–1928), the Oxford librarian to whom also the earlier mentioned Berry’s paradox is accredited." MacTutor: "Inspired by Russell, Jourdain worked mainly in mathematical logic."
- **G. G. Berry** (1867–1928) — the inventor according to Sorensen, *A Brief History of the Paradox* (Oxford UP 2003), p. 332, as Bolander reports it (Sorensen not read).
- **John Buridan** (14th century) — Bolander (§1.6): "There are even much earlier examples of indirect self-reference in the literature: Sophism 9 in John Buridan’s 14th century Sophismata (Buridan [SD], Hughes 1982) is structurally equivalent to the postcard paradox." (Hughes, *John Buridan on Self-Reference*, Cambridge UP 1982; not read.)
- **Alfred Tarski** — the language hierarchy in which, per Bolander (§3.1), such pairs "cannot even be formulated"; [Tarski](../thinkers/tarski.md).
- **Saul Kripke** (1975) — the Nixon–Jones pair, as Bolander reports it (§3.1).
- **Stephen Yablo** (1993b, *Analysis* 53(4): 251–252, [doi:10.1093/analys/53.4.251](https://doi.org/10.1093/analys/53.4.251); not read, DOI checked) — the non-circular contrast case (SEP "Liar Paradox" §1.5).
- **Thomas Bolander**; **Jc Beall, Michael Glanzberg, David Ripley** — authors of the two SEP entries mapped here.

## Framings and reframings

- **Referential graphs (Bolander).** Bolander (§1.6): "The referential structure of the liar is then a graph with a single reflexive loop. The referential structure of the postcard paradox is a cyclic graph with 2 vertices each having an edge to the other vertex. All paradoxes of direct or indirect self-reference have cyclic structures of reference (their underlying graphs are cyclic)." Yablo's is the acyclic case in the same section.
- **A dialog (Beall, Glanzberg & Ripley).** The card's two sides become two speakers, Max and Agnes, with "not true" for "false" (§1.3); the contradiction is then "implying, according to many logical theories, absurdity" (§1.3).
- **Two lines (Wikipedia).** The list replaces the two sides with "The next statement is true. The previous statement is false." (rev. 1376699902), and names the case "circular reference".
- **Names.** "It is also known as the postcard paradox, Jourdain paradox or Jourdain's paradox." (Wikipedia, rev. 1328189446).

## Vocabulary

- [Paradox](../vocabulary/paradox.md); [Validity](../vocabulary/validity.md);
  [Classical logic](../methods/classical-logic.md), in which the logic check
  above is run.
- Self-reference (direct, indirect), circular reference, liar cycle,
  referential graph, language hierarchy, object language and
  meta-language, non-wellfoundedness — open work in
  [vocabulary](../vocabulary/index.md).
