---
type: article
about: concept
title: Catch-22 (as a logical situation)
description: "Heller's catch in Catch-22 (1961) — anyone who asks to be grounded for insanity shows he is sane, so nobody is grounded — read as a logical structure: Wikipedia's propositional formalisation, Goldstein's (2004) diagnosis of it as a vacuous biconditional of the form p if and only if not-p, its grouping with the barber, Russell's paradox and Protagoras and Euathlus, and the relation to Bateson's double bind. Philosophical literature on it found here is thin."
tags: [problem, paradox, logic, self-reference, contradiction]
timestamp: 2026-10-01T21:51:46Z
---

# Catch-22 (as a logical situation)

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Primary text: Joseph Heller, *Catch-22* (1961), ch. 5 "Chief White Halfoat",
read in the Corgi paperback (1977 reprint) on
[archive.org](https://archive.org/details/catch-22-by-joseph-heller-fiction-london-1977-corgi-books)
(excerpt: `raw/heller-1961-catch-22-ch5-the-catch.md`). Philosophical
analysis: Laurence Goldstein, "The Barber, Russell's Paradox, Catch-22, God
and More", in Priest, Beall & Armour-Garb (eds), *The Law of
Non-Contradiction*, OUP 2004, pp. 295–313
([doi:10.1093/acprof:oso/9780199265176.003.0019](https://doi.org/10.1093/acprof:oso/9780199265176.003.0019);
excerpt: `raw/goldstein-2004-catch-22-vacuous-biconditional.md`).
Admitted from Wikipedia's List of paradoxes, revision 1376699902, "Logic"
([oldid](https://en.wikipedia.org/w/index.php?title=List_of_paradoxes&oldid=1376699902);
excerpt: `raw/wikipedia-catch-22-logic-and-double-bind.md`).

## The question

Heller's statement of the catch: "Sure there's a catch," Doc Daneeka replied. "Catch-22. Anyone who wants to get out of combat duty isn't really crazy." (ch. 5).
The case of Orr: "Orr was crazy and could be grounded. All he had to do was ask; and as soon as he did, he would no longer be crazy and would have to fly more missions." (ch. 5).

Wikipedia's list entry: "Catch-22: A situation in which someone is in need of something that can only be had by not being in need of it. A soldier who wants to be declared insane to avoid combat is deemed not insane for that very reason and will therefore not be declared insane." (List of paradoxes, rev. 1376699902, "Logic").
The article's lead: "A catch-22 is a paradoxical situation from which an individual cannot escape because of contradictory rules or limitations. The term was first used by Joseph Heller in his 1961 novel Catch-22." ("Catch-22 (logic)", rev. [1369910046](https://en.wikipedia.org/w/index.php?title=Catch-22_(logic)&oldid=1369910046)).

The logical question is what structure the rule has: a set of conditions
that cannot all be met, a condition stated in a self-defeating way, or no
condition at all (Positions taken). It turns on the
[biconditional](../methods/classical-logic.md) and on whether sentences of
the form *p* if and only if not-*p* are false or say nothing (Goldstein,
below).

**Propositional check of Wikipedia's formalisation (this implant, 2026-10-01; logic, not a position).**
The article's premises are "For a person to be excused from flying on the grounds of insanity (E), he must both be insane (I) and have requested an evaluation (R)." (formula 1, E → (I ∧ R)) and "An insane person (I) does not request an evaluation (¬R) because he does not realize he is insane." (formula 2, I → ¬R); its conclusion is ¬E.
`logic.py check --premises "E -> (I & R)" "I -> ~R" --conclusion "~E"`
outputs `VALID`. With premise 2 alone (`"I -> ~R"` against `"~E"`) it
outputs `INVALID` with `(3 counterexample rows)`, among them `E=T, I=T, R=F`:
the conclusion needs both premises.

**Propositional check of Goldstein's formalisation (this implant, 2026-10-01; logic, not a position).**
Goldstein's formulas are quantified; dropping the quantifier, his glosses
read: *A* ↔ *I* ("an airman can avoid flying dangerous missions (A) on condition and only on condition that he is insane (I)", p. 299),
*I* ↔ ¬*R* ("it defines you as being insane if you don't request to be spared flying such missions (R)", p. 299),
and, for formula (3), whose symbols are cut off in the scan read here, *A* → *R*
from the gloss "But you cannot be spared flying dangerous missions unless you request it" (p. 300; this reading is the implant's assumption).
`logic.py check --premises "A <-> I" "I <-> ~R" "A -> R" --conclusion "~A"`
outputs `VALID`. The same premises with conclusion `"A <-> ~A"` (Goldstein's
formula (4)) output `INVALID` with the single row `A=F, I=F, R=T`
(`(1 counterexample row)`); with `"~R -> ~A"` for formula (3) the outputs
are the same. And `logic.py check --premises "A <-> ~A" --conclusion "B"`
outputs `VALID` and `premises are jointly inconsistent — argument is vacuously valid`.
The tool is classical and two-valued: in it *A* ↔ ¬*A* is false in every
row. Goldstein's abstract denies "the assumption that contradictions and biconditionals of the form p, if and only if not-p are necessarily false" (DOI record), so the
tool's reading is the one his chapter questions, and his footnote allows
other formalisations ("I do not claim that my formalization is the only possible one", p. 300 n. 4; OCR "1 do not").

## Why it matters

- **A family of paradoxes.** Goldstein (2004, p. 299) puts it beside the barber, Russell's and Grelling's paradoxes: "In each of the paradoxes considered above (the Barber, Russell's, and Grelling's), what seemed, at first sight, to be a specifying condition turned out to be a biconditional specifying nothing." See [Russell's paradox](russells-paradox.md) and [the barber paradox](barber-paradox.md).
- **The law of non-contradiction.** Goldstein's chapter is a defence of a view he attributes to Wittgenstein: "He took the highly distinctive line that contradictions are neither true nor false, a view he defended early and late." (abstract); Catch-22 is one of his test cases. See [Priest](../thinkers/priest.md), co-editor of the volume.
- **Legal and ancient analogues.** Goldstein: "The ancient paradox of Protagoras and Euathlus turns out, perhaps surprisingly, to be related to Catch-22." (p. 301), crediting the comparison to Poundstone: "The suggestion that Catch-22 bears comparison with the paradox of Protagoras and Euathlus is made in Poundstone (1988: 128)." (p. 299 n. 3). See [the paradox of the court](paradox-of-the-court.md).
- **Teaching.** Goldstein: "Formalizing Catch-22 would be an interesting exercise for an introductory logic class." (p. 300 n. 4).
- **Communication and psychiatry.** Wikipedia's "Double bind" article links "Catch-22 (logic)" under See also (rev. [1368395486](https://en.wikipedia.org/w/index.php?title=Double_bind&oldid=1368395486)); see Framings.

## Positions taken

The sources read give no grouping of responses; the readings on record are
listed by owner, unranked.

- **A rule that excludes everyone (Wikipedia's formalisation).** "Catch-22 ensures that no pilot can ever be grounded for being insane even if he is." and "Therefore, no person can be excused from flying on the grounds of insanity (¬E) because no person can be both insane and have requested an evaluation." ("Catch-22 (logic)", rev. 1369910046, "Logic"; the derivation uses material implication, De Morgan and modus tollens). On this reading the conditions are jointly unsatisfiable for any pilot.
- **A vacuous biconditional (Goldstein 2004).** "Thus Catch-22 boils down to a biconditional of the sort that we have already encountered in paradoxes." (p. 300); formula (4) glossed as "one can avoid flying dangerous missions if and only if one cannot avoid it" (p. 300). He separates this from an unsatisfiable condition: "A vacuous bicondition is clearly not the same as a condition that cannot be satisfied, such as ‘You can avoid flying dangerous missions if and only if you can trisect an arbitrary angle using only straightedge and compass’; a vacuous biconditional just does not amount to the expression of any condition." (p. 300). His assessment: "But Catch-22 is worse—a welter of words that amounts to nothing; it is without content, it conveys no information at all." (p. 300), and "It does not state a truth or a falsity about the conditions under which danger can be avoided; on the Wittgensteinian view, it states nothing at all, though it has meaning, can be understood and may have the perlocutionary effect of engendering confusion. Catch-22 is an elaborate oxymoron." (p. 300).
  Wikipedia's summary of Goldstein: "The philosopher Laurence Goldstein argues that the "airman's dilemma" is logically not even a condition that is true under no circumstances; it is a "vacuous biconditional" that is ultimately meaningless." (rev. 1369910046).
  *Bearing on it:* the two-valued check above (The question) yields ¬*A* from Goldstein's three glosses but not *A* ↔ ¬*A*; that is the tool's output under the implant's reading of formula (3), not a position of any author read here.
- **Power rather than logic (Gregson, as reported).** Wikipedia reports a literary reading of a later episode: "According to literature professor Ian Gregson, the old woman's narrative defines "Catch-22" more directly as the "brutal operation of power", stripping away the "bogus sophistication" of the earlier scenarios." (rev. 1369910046, citing Gregson 2006, p. 38; Gregson's text was not read here).

Philosophical sources on Catch-22 found in this search are thin: no SEP
entry checked mentions it (Fall 2024 "Contradiction", "Dialetheism",
"Moral Dilemmas", "Paradoxes and Contemporary Logic", "Russell's Paradox",
"Self-Reference" — none contain the string), a Crossref title search for
"catch-22" returned no logic or philosophy journal article, and Goldstein
(2004) is the only formal philosophical analysis read.

## Arguments in play

(none recorded as separate argument pages yet). The two derivations — the
article's E/I/R argument and Goldstein's A/I/R argument — are in The
question with the tool's outputs; Goldstein's grounds for calling the
result empty rather than false are in Positions taken.

## Thinkers who addressed it

- **Joseph Heller** (*Catch-22*, 1961, ch. 5) — states the catch; Goldstein quotes the passage from "Heller (1994: 62-3)" (p. 299 n. 3).
- **Laurence Goldstein** (2004, pp. 299–301) — formalisation as a vacuous biconditional; relation to the barber, Russell's paradox and Protagoras and Euathlus.
- **William Poundstone** (1988, p. 128) — compared Catch-22 with Protagoras and Euathlus, per Goldstein (p. 299 n. 3); not read here.
- **Ludwig Wittgenstein** — the conception of contradiction Goldstein applies (abstract).
- **Graham Priest, J. C. Beall, Bradley Armour-Garb** — editors of the volume in which Goldstein's chapter appears ([Priest](../thinkers/priest.md)).
- **Gregory Bateson** and colleagues (1956) — the double bind; see Framings.
- **Ian Gregson** (2006) — literary reading, as reported by Wikipedia.

## Framings and reframings

- **Specification that specifies nothing.** Goldstein's frame for the barber, Russell's, Grelling's paradoxes and Catch-22 alike (p. 299, quoted above); he calls such biconditionals vacuous: "I propose to call biconditionals of the form “p <> ~p’ vacuous." (p. 300, as scanned).
- **A dilemma.** Wikipedia's summary calls the case the "airman's dilemma" (rev. 1369910046). See [dilemma](../vocabulary/dilemma.md).
- **An oxymoron.** Goldstein: "Catch-22 is an elaborate oxymoron." (p. 300). See [oxymoron](../vocabulary/oxymoron.md).
- **A double bind.** The "Double bind" article: "A double bind is a dilemma in communication in which an individual (or group) receives two or more mutually conflicting messages." and "Double bind theory was first stated by Gregory Bateson and his colleagues in the 1950s, in a theory on the origins of schizophrenia." (rev. 1368395486). The same article separates it from a bare contradiction: "The double bind is often misunderstood to be a simple contradictory situation, where the subject is trapped by two conflicting demands. While it is true that the core of the double bind is two conflicting demands, the difference lies in how they are imposed upon the subject, what the subject's understanding of the situation is, and who (or what) imposes these demands upon the subject." The source paper is Bateson, Jackson, Haley & Weakland, "Toward a theory of schizophrenia", *Behavioral Science* 1(4), 1956, pp. 251–264 ([doi:10.1002/bs.3830010402](https://doi.org/10.1002/bs.3830010402); bibliographic record verified, text not read); no source read here analyses Catch-22 and the double bind together beyond the See also links.
- **Neighbouring cases in the same list.** Wikipedia's "Catch-22 (logic)" See also includes Double bind, False dilemma, Hobson's choice, Morton's fork, No-win situation, Self-reference, Vicious circle and Zugzwang (rev. 1369910046); "Double bind" lists Barber paradox and Buridan's bridge beside it (rev. 1368395486). See [Buridan's bridge](buridans-bridge.md).

Not in the excerpts held: Poundstone 1988, Gregson 2006, Bateson et al.
1956 and Bateson's *Steps to an Ecology of Mind* (1972), and Sukaina
Hirji's paper *Oppressive Double Binds* (cited by the "Double bind" article; the
PhilPapers PDF did not download); they are left out until a source is read.

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — see The question.
- [Validity](../vocabulary/validity.md) — the two propositional checks; "vacuously valid" in the tool's output.
- [Dilemma](../vocabulary/dilemma.md) — "airman's dilemma"; the double bind defined as "a dilemma in communication".
- [Oxymoron](../vocabulary/oxymoron.md) — Goldstein's description.
- [Classical logic](../methods/classical-logic.md) — the two-valued reading the checks use.
- *Biconditional*, *vacuous biconditional* (Goldstein), *contradiction*, *double bind*, *self-reference* — open work in [vocabulary](../vocabulary/index.md).
