---
type: article
about: concept
title: "The barber paradox"
description: "A barber shaves all and only those who do not shave themselves: does he shave himself? Russell's 1918 lecture VII calls it a form of his class contradiction 'suggested to me' that 'was not valid' and 'not very difficult to solve'; the standard reply that no such barber exists; and the SEP's report of the dispute over whether it is a 'pseudo paradox' (Quine 1966) or close kin of Russell's paradox (Salmon 2013)."
tags: [problem, paradox, logic, self-reference, set-theory]
timestamp: 2026-10-08T19:52:29Z
---

# The barber paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Primary text: Bertrand Russell, "The Philosophy of Logical Atomism", lecture VII,
*The Monist* 29(3), 1919, pp. 353–355 ([doi:10.5840/monist19192937](https://doi.org/10.5840/monist19192937);
scan: [archive.org jstor-27900748](https://archive.org/details/jstor-27900748);
excerpt: `raw/russell-1918-1919-logical-atomism-lecture-7-barber.md`).
Map: Irvine & Deutsch, [SEP Fall 2024 "Russell's Paradox"](https://plato.stanford.edu/archives/fall2024/entries/russell-paradox/)
§4 (excerpts: `raw/sep-russell-paradox-fall-2024-history-and-responses.md`,
`raw/sep-russell-paradox-fall-2024-barber-pseudo-paradoxes.md`).
Admitted from Wikipedia's List of paradoxes, revision 1376699902, "Logic"
(excerpt: `raw/wikipedia-barber-paradox-rev-1366901156-and-list-entry.md`).
The parent problem is [Russell's paradox](russells-paradox.md).

## The question

Russell's statement: "You can define the barber as "one who shaves all those, and those only, who do not shave themselves." The question is, does the barber shave himself? In this form the contradiction is not very difficult to solve." (lecture VII, p. 355).
Wikipedia's list gives it as: "Barber paradox: A male barber shaves all and only those men who do not shave themselves. Does he shave himself? (Russell's popularization of his set theoretic paradox.) Not to be confused with the Barbershop paradox." (List of paradoxes, rev. 1376699902; see [the barbershop paradox](barbershop-paradox.md)).
Irvine & Deutsch name it "the famous paradox of the barber who shaves all and only those who do not shave themselves" (SEP §4).

**Propositional check (this implant, 2026-10-01; logic, not a position).**
Let *S* stand for *the barber shaves himself*. Instantiating the barber's
definition to the barber himself gives *S* <-> ~*S* (the step Wikipedia's
article describes as assigning the barber to the universally quantified
variable, "an instance of the contradiction a ⟺ ¬a").
`logic.py check --premises "S <-> ~S" --conclusion "S & ~S"` outputs `VALID`
and `premises are jointly inconsistent — argument is vacuously valid`.
Adding *B* for *such a barber exists*, the premise `"B -> (S <-> ~S)"` with
conclusion `"~B"` outputs `VALID`. Each half of the biconditional alone does
not suffice: `"S -> ~S"` against `"S & ~S"` outputs `INVALID` with the
counterexample row `S=F`. The tool is propositional; it treats the
instantiation of the definition to the barber himself
as given and does not model the quantifiers.

## Why it matters

- **Its relation to Russell's paradox.** Russell introduces it directly after the class contradiction: "That contradiction is extremely interesting. You can modify its form ; some forms of modification are valid and some are not. I once had a form suggested to me which was not valid, namely the question whether the barber shaves himself or not." (pp. 354–355). The class contradiction it modifies: "Hence either hypothesis, that it is or that it is not a member of itself, leads to its contradiction. If it is a member of itself, it is not, and if it is not, it is." (p. 354). See [Russell's paradox](russells-paradox.md).
- **A shared logical pattern.** Irvine & Deutsch: "Russell’s paradox is an instance of T269 in this list:" (§4; T269 is ~∃y∀x(Fxy ≡ ~Fxx), from Kalish, Montague and Mar 2000), and "But that pattern also underwrites an endless list of seemingly frivolous “paradoxes” such as the famous paradox of the barber who shaves all and only those who do not shave themselves" (§4).
- **What counts as a paradox.** The SEP poses the question the case raises for the notion of [paradox](../vocabulary/paradox.md): "How do these “pseudo paradoxes,” as they are sometimes called, differ, if at all, from Russell’s paradox?" (§4).
- **Who introduced it.** Wikipedia's list files it as "Russell's popularization of his set theoretic paradox" (rev. 1376699902); its article on the barber says instead that it "was suggested to Bertrand Russell as an illustration of the paradox" (rev. 1366901156, lead). Russell's own words are "I once had a form suggested to me" (p. 355).

## Positions taken

No grouping of responses to the barber was found in the sources read; the
answers on record are listed by owner, unranked.

- **Russell (lecture VII, delivered London 1918, printed 1919): an invalid modification, easily solved.** The lectures were "delivered in London in the first months of 1918" (editorial note, *Monist* 28, 1918, p. 495). On the barber: "I once had a form suggested to me which was not valid" and "In this form the contradiction is not very difficult to solve." (pp. 354–355). He does not say in this passage how it is solved. For the class form he gives a different treatment: "But in our previous form I think it is clear that you can only get around it by observing that the whole question whether a class is or is not a member of itself is nonsense, i. e., that no class either is or is not a member of itself, and that it is not even true to say that, because the whole form of words is just a noise without meaning." (p. 355), grounded in "the fact that classes, as I shall be coming on to show, are incomplete symbols in the same sense in which the descriptions are that I was talking of last time" (p. 355).
- **No such barber exists (the dissolution).** Irvine & Deutsch: "The pattern of reasoning is the same and the conclusion – that there is no such Barber, no such efficient God, no such set of non-self-membered sets – is the same: such things simply don’t exist." (SEP §4). Wikipedia's article: "In its original form, this paradox has no solution, as no such barber can exist. The question is a loaded question in that it assumes the existence of a barber who could not exist, which is a vacuous proposition, and hence false." (rev. 1366901156, "Paradox"), and "Nobody is such a barber, so there is no solution to the paradox." ("In first-order logic").
  *Qualification on record:* Irvine & Deutsch add, of the same conclusion for the class case: "(However, as von Neumann showed, it is not necessary to go quite this far. Von Neumann’s method instructs us not that such things as \(R\) do not exist, but just that we cannot say much about them, inasmuch as \(R\) and the like cannot fall into the extension of any predicate that qualifies as a class.)" (§4).
- **A pseudo paradox, unlike Russell's (Quine 1966, as quoted in SEP §4).** "“why does it [Russell’s paradox] count as an antinomy and the barber paradox not?”; and he answers, “The reason is that there has been in our habits of thought an overwhelming presumption of there being such a class but no presumption of there being such a barber” (1966, 14)." Irvine & Deutsch report that "The standard answer to this question is that the difference lies in the subject matter." (§4).
  *Against, per Irvine & Deutsch (their assessment):* "Even so, psychological talk of “habits of thought” is not particularly illuminating." (§4).
  *Irvine & Deutsch's own restatement:* "More to the point, Russell’s paradox sensibly gives rise to the question of what sets there are; but it is nonsense to wonder, on such grounds as T269, what barbers or Gods there are!" (§4).
- **Closer to Russell's paradox than Quine allowed (Salmon 2013, as reported in SEP §4).** Irvine & Deutsch on their own verdict: "This verdict, however, is not quite fair to fans of the Barber or of T269 generally." "They will insist that the question raised by T269 is not what barbers or Gods there are, but rather what non-paradoxical objects there are." "This question is virtually the same as that raised by Russell’s paradox itself." "Thus, from this perspective, the relation between the Barber and Russell’s paradox is much closer than many (following Quine) have been willing to allow (Salmon 2013)." (§4). Salmon's paper ([doi:10.5840/jphil2013110432](https://doi.org/10.5840/jphil2013110432)) was not read here (record: `raw/barber-paradox-bibliographic-records.md`).

## Arguments in play

(none recorded as separate argument pages yet). The derivation is Russell's
two-hypothesis pattern for the class case — "Let us first suppose that it is
a member of itself" and then that it is not (p. 354) — applied to *shaves
himself*; its propositional core is checked in The question. The first-order
form on record is T269, ~∃y∀x(Fxy ≡ ~Fxx), which Irvine & Deutsch, "Reading the dyadic predicate letter “\(F\)” as “is a member of”", gloss for the class case (§4); with *F* read as *shaves*, the same schema says that nobody shaves all and only those who do not shave themselves (structural note, this implant: a substitution of a reading for the predicate letter, not a source's claim).

## Thinkers who addressed it

- **Bertrand Russell** (lecture VII of "The Philosophy of Logical Atomism", 1918, printed in *The Monist* 1919) — the barber as a form "suggested to me" that "was not valid" (p. 355).
- **W. V. O. Quine** (*The Ways of Paradox and Other Essays*, 1966, p. 14) — the barber is not an antinomy; quoted from SEP §4 (the book is lending-restricted on archive.org and was not read here).
- **John von Neumann** — his method, per Irvine & Deutsch, says that such things as *R* cannot be members of a class rather than that they do not exist (SEP §4).
- **Nathan Salmon** (2013) — the barber is closer to Russell's paradox than Quine allowed (SEP §4; text not read).
- **Andrew David Irvine & Harry Deutsch** (SEP, rev. 2020) — the T269 framing and the assessments quoted above.
- **Martin Gardner** (*Aha!*) — named by Wikipedia's article as an example of attributing the paradox to Russell ("This paradox is often incorrectly attributed to Bertrand Russell (e.g., by Martin Gardner in Aha!)." — the article's claim, no source given for it beyond the example); Gardner's text was not read.

## Framings and reframings

- **Popularisation or rejected variant?** Two attributions stand side by side in the sources read. Wikipedia's list: "Russell's popularization of his set theoretic paradox" (rev. 1376699902). Wikipedia's article: "The barber paradox is a puzzle derived from Russell's paradox. It was suggested to Bertrand Russell as an illustration of the paradox, but he deemed it an invalid modification of his paradox." (rev. 1366901156). Russell: "I once had a form suggested to me which was not valid, namely the question whether the barber shaves himself or not." (pp. 354–355). Russell's passage does not name who suggested it.
- **One pattern, many instances.** Irvine & Deutsch place the barber beside "the paradox of the benevolent but efficient God who helps all and only those who do not help themselves" as instances of the T269 pattern (SEP §4; excerpt: `raw/sep-russell-paradox-fall-2024-history-and-responses.md`).
- **A loaded question.** Wikipedia's article frames the question whether the barber shaves himself as one that "assumes the existence of a barber who could not exist" (rev. 1366901156).
- **Not to be confused with** the [barbershop paradox](barbershop-paradox.md) (Lewis Carroll, on conditionals), which Wikipedia's list cross-refers (rev. 1376699902).

Not in the excerpts held: Quine 1966 at first hand, Salmon 2013, Gardner's
*Aha!*, the *Collected Papers* vol. 8 reprint (p. 228, cited by Wikipedia),
and the UMSL and Oxford Reference pages Wikipedia cites (404 and 403 on
2026-10-01); they are left out until a source is read.

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — and the SEP's "pseudo paradoxes" (§4).
- [Validity](../vocabulary/validity.md) — the propositional check above. Russell's "some forms of modification are valid and some are not" (p. 354) uses the word of modifications of the contradiction; he does not define that use in the passage read.
- [Dilemma](../vocabulary/dilemma.md) — the two hypotheses, shaves himself or not.
- [Classical logic](../methods/classical-logic.md) — the logic of the check.
- *Antinomy* (Quine's term, SEP §4), *incomplete symbol* (Russell, p. 355), *self-reference* — open work in [vocabulary](../vocabulary/index.md).

Related thinkers: [Russell](../thinkers/russell.md).
