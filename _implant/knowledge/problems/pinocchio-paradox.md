---
type: article
about: concept
title: "The Pinocchio paradox"
description: "Pinocchio, whose nose grows if and only if what he says is not true, says 'My nose is growing' — the paradox devised by Veronique Eldridge-Smith (2001) and published with Peter Eldridge-Smith in Analysis (2010); claimed by its authors to be a liar paradox without a semantic predicate, set against Tarskian-Kripkean hierarchies (2010) and semantic dialetheism (2011), answered by Beall (2011) as an impossible story, with replies by Eldridge-Smith (2012, 2018), Luna (2016) and D'Agostini & Ficara (2016)."
tags: [problem, paradox, logic, self-reference, liar, truth, dialetheism]
timestamp: 2026-10-01T22:52:16Z
---

# The Pinocchio paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Primary text: P. Eldridge-Smith & V. Eldridge-Smith, "The Pinocchio paradox",
*Analysis* 70(2), 2010, pp. 212–215,
[doi:10.1093/analys/anp173](https://doi.org/10.1093/analys/anp173) — verified by
DOI content negotiation, full text not read (publisher 403, repository copy 401);
its content is reported here only through the authors' later papers and the
sources named. Read in full: Eldridge-Smith, "Pinocchio against the dialetheists",
*Analysis* 71(2), 2011, pp. 306–308, [doi:10.1093/analys/anr007](https://doi.org/10.1093/analys/anr007),
open copy [hdl:1885/54731](http://hdl.handle.net/1885/54731)
(excerpt: `raw/eldridge-smith-2011-pinocchio-against-the-dialetheists.md`).
Read as abstracts: Eldridge-Smith 2012 and 2018 (excerpt:
`raw/eldridge-smith-2012-2018-pinocchio-abstracts.md`).
Admitted from Wikipedia's [List of paradoxes, revision 1376699902](https://en.wikipedia.org/w/index.php?title=List_of_paradoxes&oldid=1376699902),
"Logic" (excerpt: `raw/wikipedia-list-of-paradoxes-pinocchio-paradox-entry.md`).

## The question

Eldridge-Smith (2018, abstract) states the principle and the question: "Pinocchio’s nose grows if, and only if, what Pinocchio is saying is untrue (the Pinocchio principle). What happens if Pinocchio says that his nose is growing?"
In the 2011 note: "Should Pinocchio say that his nose is growing, a contradiction would obtain (Eldridge-Smith and Eldridge-Smith 2010)." (p. 306).
The 2012 abstract names the utterance: "One day Pinocchio was beguiled by the dark side of logical force into saying ‘My nose is growing’ (the Pinocchio statement)."
The Wikipedia list asks "What would happen if Pinocchio said "My nose grows now"?" (rev. 1376699902).

The premise comes from fiction. In Collodi's novel (ch. 17, Della Chiesa
translation; excerpt: `raw/collodi-1883-pinocchio-ch17-nose-grows-della-chiesa.md`),
after a lie: "As he spoke, his nose, long though it was, became at least two inches longer."
The novel's passage reports growth at lies; the "if, and only if" is the
Eldridge-Smiths' stipulation (2011, p. 306; 2018, abstract).

**Logic check (this implant, 2026-10-02; logic, not a position).** Let `N` =
*Pinocchio's nose is growing*, `T` = *what Pinocchio says is true*. The
principle gives `N <-> ~T`; since what he says is "My nose is growing", read
classically, `T <-> N`. `logic.py check --premises "N <-> ~T" "T <-> N" --conclusion "N <-> ~N"`
outputs "VALID" and "premises are jointly inconsistent — argument is vacuously valid".
`logic.py check --premises "N <-> ~N" --conclusion "N & ~N"` outputs the same
two lines. With the principle alone, `--premises "N <-> ~T" --conclusion "N <-> ~N"`
outputs "INVALID" (counterexamples "N=T, T=F" and "N=F, T=T"): the
contradiction needs the second premise, the reading of the statement. The
tool does not say which premise, or whether classical logic, a response
gives up; the positions below differ on that.
The term contracts are [paradox](../vocabulary/paradox.md),
[validity](../vocabulary/validity.md) and [classical logic](../methods/classical-logic.md).

## Why it matters

- **A liar without a semantic predicate.** Eldridge-Smith (2018, abstract): "The Liar paradox is an obstacle to a theory of truth, but a Liar sentence need not contain a semantic predicate. The Pinocchio paradox, devised by Veronique Eldridge-Smith, was the first published paradox to show this."
  In 2011 (p. 307): "‘Is growing’ is an empirical predicate, not a semantic one."
- **A test for liar solutions.** Eldridge-Smith (2018, abstract) reports that the 2010 paper "posed the Pinocchio paradox against the Tarskian-Kripkean solutions to the Liar paradox that use language hierarchies", and that the 2011 note "also set the Pinocchio paradox against semantic dialetheic solutions to the Liar."
- **Metaphysical, not only semantic, contradiction.** Eldridge-Smith (2011, p. 307): "If it is a true contradiction that Pinocchio’s nose grows and does not grow, then such a world is metaphysically impossible, not merely semantically impossible."

## Positions taken

Not ranked; each is reported with the source that records it. Only the 2011
note and the blog post below were read in full; the 2010, 2012 and 2018
positions and those of Beall, Luna and D'Agostini & Ficara are reported as
Eldridge-Smith's 2018 abstract summarises them.

- **Hierarchies do not solve it (Eldridge-Smith & Eldridge-Smith 2010; Eldridge-Smith 2018).** The 2018 abstract ends: "I respond to Luna, and D’Agostini & Ficara, and prove that the Pinocchio paradox is a counterexample to hierarchical solutions to the Liar." On the hierarchy itself, Beall, Glanzberg & Ripley (SEP 2024, §4.3.1) report: "Tarski concluded from the paradox that no language could contain its own truth predicate (in his terminology, no language can be ‘semantically closed’)." (excerpt: `raw/sep-sorites-and-liar-fall-2024-paradox-formulations-and-responses.md`).
- **Semantic dialetheism does not solve it (Eldridge-Smith 2011).** "Astute dialetheists do not believe in metaphysical contradictions, just semantic ones." (p. 307). He grants that "It has been substantially demonstrated by Priest (2006) that this can be made systematic, and that such a system of paraconsistent logic is a solution to the Liar paradox." and continues: "However, the Pinocchio paradox, devised by my daughter, Veronique, is a version of the Liar paradox that resists such a solution." (p. 307).
- **An impossible story (Beall 2011).** J. Beall, "Dialetheists against Pinocchio", *Analysis* 71(4), 2011, pp. 689–691, [doi:10.1093/analys/anr084](https://doi.org/10.1093/analys/anr084) (verified by DOI content negotiation; not read). As Eldridge-Smith (2018, abstract) reports it: "Beall (2011) argued the Pinocchio story was just an impossible story."
- **The principle is possible unless the T-schema is necessary (Eldridge-Smith 2012).** "Pinocchio beards the Barber", *Analysis* 72(4), 2012, pp. 749–752, [doi:10.1093/analys/ans103](https://doi.org/10.1093/analys/ans103) (not read). Per the 2018 abstract, he "responded that unless the T-schema is a necessary truth of some sort (logical, metaphysical or analytic), the Pinocchio principle is possible."
- **The contradiction refutes the principle (Luna 2016).** Per Eldridge-Smith (2018, abstract): "Luna (Mind & Matter 14(1): 77–86, 2016) argues that the Pinocchio contradiction proves the principle is false." Not read; not located by DOI.
- **Not a metaphysical dialetheia (D'Agostini & Ficara 2016).** Per the same abstract: "D’Agostini & Ficara (2016) discuss a more plausible physical truth-tracking trait, the Blushing Liar, and argue that the Pinocchio contradiction is not a metaphysical dialetheia." Not read.
- **Lying is not saying something false; no paradox (Vallicella 2010).** A blog post on the cartoon wording "My nose will grow now" (excerpt: `raw/vallicella-2010-pinocchio-paradox-blog.md`), assuming that a lie "is a false statement made with the intention to deceive  by someone who knows the truth.  (Or so I will assume for the space of this post.)" He reads the sentence as future tense: "It follows that Pinocchio cannot be lying." For the present tense he argues: "Therefore, either his nose does not grow now or his nose does grow now.  But that is wholly unproblematic." He states: "There is a 2010 Analysis article under this rubric.  But I don't have access to it at the moment, and I'm not sure the topic is exactly the same."

**Cases for and against.** For treating it as a liar without semantic
vocabulary: Eldridge-Smith's empirical-predicate claim (2011, p. 307; 2018).
Against: Beall's impossible-story reply and Luna's reading that the
contradiction refutes the principle (both as reported in 2018), and
Vallicella's distinction between lying and falsehood (2010). The 2011 note
words the principle both with "telling a lie" (p. 306) and with "not true"
(p. 307); the logic check above encodes "not true", and Vallicella's
response turns on "lie". No survey
figure is recorded.

## Arguments in play

(none as separate argument pages yet). Related problems:
[the liar paradox](liar-paradox.md), of which Eldridge-Smith (2011, p. 307)
calls it "a version"; [Buridan's bridge](buridans-bridge.md), which
Eldridge-Smith (2011, n. 1) records among the "intellectual ancestors" pointed out
by the referee and editor: "These are scenarios about promises paradoxically thwarted by logic."
— "in Buridan’s 17th sophism in Chapter 8 of his Sophismata, Plato promises to either let Socrates across a bridge or throw him into the water depending on whether his next statement is respectively true or false."
The 2012 title pairs it with [the barber paradox](barber-paradox.md); the
paper's content on that pairing was not read. Siblings on liar variants:
[the no-no paradox](no-no-paradox.md), [the card paradox](card-paradox.md),
[Quine's paradox](quines-paradox.md), [Yablo's paradox](yablos-paradox.md).

## Thinkers who addressed it

- **Veronique Eldridge-Smith** — "The Pinocchio paradox was devised by Veronique Eldridge-Smith in February 2001." (Eldridge-Smith 2011, p. 307, n. 1); co-author of the 2010 paper.
- **Peter Eldridge-Smith** (Australian National University, per the 2011 note's address) — 2010 (with V. Eldridge-Smith), 2011, 2012, 2018 ([doi:10.1007/s11406-018-9948-y](https://doi.org/10.1007/s11406-018-9948-y), *Philosophia* 46(4), pp. 817–830, abstract read).
- **J. Beall** — "Dialetheists against Pinocchio" (2011), as above.
- **[Graham Priest](../thinkers/priest.md)** — his paraconsistent solution to the liar (Priest 2006, *In Contradiction*, 2nd edn) is the target of the 2011 note.
- **[Alfred Tarski](../thinkers/tarski.md)** — the language hierarchy the 2010 paper is set against (2018 abstract: "Tarskian-Kripkean solutions").
- **Luna** (2016) and **F. D'Agostini & E. Ficara** (2016) — as reported by Eldridge-Smith 2018; given names and full references not verified here.
- **Bill (William F.) Vallicella** — blog post, 7 April 2010.
- **Carlo Collodi** — the novel (1883) supplies the character and the growing nose.

## Framings and reframings

- **Empirical versus semantic contradiction.** Eldridge-Smith (2011, p. 307) describes semantic dialetheism by the case of standing in a doorway: "a semantic contradiction in the extension of the predicate ‘am in the room’"; the Pinocchio case is meant to move the contradiction from the extension of a predicate to the world ("metaphysically impossible, not merely semantically impossible").
- **Possibility of the scenario.** Beall (as reported, 2018) frames the story as impossible; Eldridge-Smith (as reported, 2018) ties the possibility of the principle to the modal status of the T-schema. Beall, Glanzberg & Ripley (SEP 2024, §1.1) note that contradictions "according to many logical theories (e.g., classical logic, intuitionistic logic, and many others) imply triviality, that is, that every sentence is true."
- **Lying and tense.** Vallicella (2010) reframes it through the definition of a lie and the tense of "will grow now"; on the future tense he writes: "'Now' does not refer to the time of utterance, but to a time right after it."
- **Popular reception.** The Wikipedia list's footnote says an image with the bubble "My nose will grow now!" had become "a minor Internet phenomenon" as of 2010 (rev. 1376699902); Vallicella's post responds to that cartoon.

## Vocabulary

- [Paradox](../vocabulary/paradox.md); [Validity](../vocabulary/validity.md);
  [Classical logic](../methods/classical-logic.md), in which the logic check
  above is run.
- Pinocchio principle, Pinocchio statement (Eldridge-Smith 2012, 2018),
  semantic predicate, empirical predicate, semantic closure, language
  hierarchy, T-schema, dialetheism, paraconsistent logic — open work in
  [vocabulary](../vocabulary/index.md).
