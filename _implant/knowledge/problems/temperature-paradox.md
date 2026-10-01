---
type: article
about: concept
title: The temperature paradox
description: "From 'the temperature is ninety' and 'the temperature is rising', 'ninety is rising' seems to follow by substitution of identicals, yet speakers reject it. Partee's puzzle as reported in Montague's PTQ (1973), Montague's individual-concept treatment, the anomaly and Jackendoff objections and the variants that answer them (as Löbner 2020 reports), later formal semantics dropping the treatment, and the responses of Lasersohn 2005 and Romero 2008 (bibliographic only)."
tags: [problem, paradox, logic, philosophy-of-language, formal-semantics, intensionality]
timestamp: 2026-10-01T21:51:46Z
---

# The temperature paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Primary text: Richard Montague, "The Proper Treatment of Quantification in
Ordinary English" (PTQ), in Hintikka, Moravcsik and Suppes (eds.), *Approaches
to Natural Language*, Reidel, 1973, pp. 221–242
([doi:10.1007/978-94-010-2506-5_10](https://doi.org/10.1007/978-94-010-2506-5_10)),
quoted from the reprint in Portner and Partee (eds.), *Formal Semantics: The
Essential Readings*, Blackwell, 2002, pp. 17–34
([doi:10.1002/9780470758335.ch1](https://doi.org/10.1002/9780470758335.ch1)),
reprint page numbers (excerpt: `raw/montague-1973-ptq-partee-temperature-puzzle.md`).
Survey: Sebastian Löbner, "The Partee Paradox. Rising Temperatures and Numbers",
*The Wiley Blackwell Companion to Semantics*, 2020
([doi:10.1002/9781118788516.sem077](https://doi.org/10.1002/9781118788516.sem077)),
author's preprint pages (excerpt: `raw/lobner-2020-partee-paradox-rising-temperatures.md`).
Map: Janssen & Zimmermann, [SEP Fall 2024 "Montague Semantics"](https://plato.stanford.edu/archives/fall2024/entries/montague-semantics/)
§2.4 (excerpt: `raw/sep-montague-semantics-fall-2024-temperature-rising.md`).
Admitted from Wikipedia's List of paradoxes, revision 1376699902, "Logic"
(excerpt: `raw/wikipedia-temperature-paradox.md`).

## The question

Montague states the argument and the puzzle: "From the premises the temperature is ninety and the temperature rises, the conclusion ninety rises would appear to follow by normal principles of logic; yet there are occasions on which both premises are true, but none on which the conclusion is." (PTQ, p. 30).
Wikipedia's list entry: "Temperature paradox: If the temperature is 90 and the temperature is rising, that would seem to entail that 90 is rising." (List of paradoxes, rev. 1376699902).

The principle in play, per Löbner, is Leibniz' Law — from *P(x)* and *x = y*, infer *P(y)* — and "Barbara Partee is credited for the following apparent counterexample to Leibniz’ Law:" (§1.2, p. 3), the argument *the temperature is rising; the temperature is ninety; ninety is rising*.
Löbner's assessment of the conclusion: "This entailment clearly is invalid: the number 90, or the temperature value 90 degree Fahrenheit meant here, are fixed things that cannot rise." (§1.2, p. 3).
Structural note (this implant): the positions below differ over which assumption to deny — that *the temperature is ninety* is an identity, that *the temperature* denotes the same thing in both premises, that the conclusion is well formed, or that the substitution rule holds without exception.
Löbner's own stance on the last option: "Leibniz’ Law must not only be upheld, it cannot be allowed any exception." (§1.2, p. 3).

**Propositional check (this implant, 2026-10-01; logic, not a position).**
Read with each sentence as an unanalysed atom — *n* for *the temperature is
ninety*, *r* for *the temperature is rising*, *s* for *ninety is rising* —
`logic.py check --premises "n" "r" --conclusion "s"` outputs `INVALID` with
the counterexample row `n=T, r=T, s=F`. Adding the substitution step as an
explicit premise, `logic.py check --premises "n" "r" "n & r -> s" --conclusion "s"`
outputs `VALID`. The tool is propositional only: it shows that the inference
does not hold in virtue of sentential form alone, and that it becomes valid
once the substitution step is granted — the step Leibniz' Law supplies in
predicate logic with identity, which the tool does not model. Whether that
step applies here is what the positions below dispute.

## Why it matters

- **Intensional semantics.** Janssen & Zimmermann list it among the puzzles Montague's intensional approach was used for: "The intensional approach also made it possible to deal with several classical puzzles. Two examples from Montague 1973 are: The temperature is rising, which should not be analyzed as stating that some number is rising; and John wishes to catch a fish and eat it, which should not be analyzed as implying that John has a particular fish in mind." (SEP §2.4).
- **A new kind of intensionality.** Montague: "The next few examples concern an interesting puzzle due to Barbara Hall Partee involving a kind of intensionality not previously observed by philosophers." (p. 30).
- **The design of the PTQ fragment.** Montague draws a general lesson for the grammar: "We thus see the virtue of having intransitive verbs and common nouns denote sets of individual concepts rather than sets of individuals" (p. 31).
- **A test for intensional positions.** Löbner: "We now see that the scheme of Leibniz’ Law can be used as a test for checking if a given construction is extensional or intensional with respect to an NP position." (§1.3, p. 6).
- **Related constructions.** In Löbner's abstract: "Constructions known as “concealed questions”—for example know the price—are shown to be closely related." (p. 1).

## Positions taken

No grouping beyond Löbner's was found in the sources read; positions are
listed by owner, unranked. The papers of Lasersohn and Romero were not read
and are reported only as Löbner reports them.

- **The two premises are about different things: intension and extension (Montague 1973, PTQ pp. 30–31).** "According to the following symbolizations, however, the argument in question turns out not to be valid." (p. 30). His reason, "speaking very loosely": "The temperature "denotes" an individual concept, not an individual; and rise, unlike most verbs, depends for its applicability on the full behavior of individual concepts, not just on their extensions with respect to the actual world and (what is more relevant here) moment of time." (pp. 30–31); "Yet the sentence the temperature is ninety asserts the identity not of two individual concepts but only of their extensions." (p. 31). Common nouns such as *temperature* are allowed non-constant individual concepts: "the individual concepts in their extensions would in the most natural cases be functions whose values vary with their temporal arguments." (p. 18).
  Löbner's summary of it: "Montague in PTQ offers the following solution to the puzzle: Partee’s first two sentences – the temperature is rising and the temperature is ninety – are not about the same thing; they are not like ‘P(x)’ and ‘x=y’, but actually instantiate ‘P(x)’ and ‘z=y’ where z is different from x; obviously, ‘P(x)’ and ‘z=y’ do not entail ‘P(y)’." (§1.3, p. 4).
  *Against, as Löbner reports:* "It was observed early on that this feature of Montague’s analysis leads to the logical problem that “the temperature” at one time need not be the same individual concept as at another time (Dowty, Wall, Peters 1981: 284f, see Lasersohn 2005 for discussion)." (n. 11). Löbner reports the cost of the design: "Since there are verbs that apply to the intension of the subject, the interpretation rule must state that the verb in general takes an intension as its subject argument. If a verb happens to be extensional, it applies to the intension and a meaning postulate is added to the system that states that only the given value of the intension (i.e. the extension) matters for this verb." (§1.3, p. 6); and that "In view of all these issues and of the apparent marginality of the phenomenon, the mainstream development in formal semantics chose not to include intensional constructions of the rising-temperature type." (§1.3, p. 6); "As an exception, Janssen (1984) made a plea for not disregarding individual concepts in the framework of formal semantics." (n. 6).
- **The conclusion is anomalous (unnamed, as Löbner reports).** "Some argued that the conclusion (4c) ninety is rising is a semantically anomalous sentence." (§1.2, p. 3).
  *Against, per Löbner:* a variant with *the temperature in Chicago is the same as the temperature in Sidney*, of which he writes "Clearly, (5b) is an identity statement, and (5c) is not anomalous." (§1.2, p. 3).
- **The second premise is not an identity (Jackendoff 1979, "How to keep ninety from rising", *Linguistic Inquiry* 10, as Löbner reports).** "Jackendoff (1979) objected that the temperature is ninety is not an identity statement of the form x=y but rather a statement localizing the temperature at some point of the Fahrenheit scale." (§1.2, p. 3).
  *Against, per Löbner:* the same Chicago/Sidney variant, and "However, there are also instantiations of Partee’s paradox that involve reference to ordinary individuals:" (§1.2, p. 3) — *the president of the US will change in 2021* — from which he concludes: "Partee’s paradox is, hence, not bound to predications about abstract entities like temperatures or prices etc. and to numerical values or measures; it is more general in nature and calls for an answer." (§1.2, p. 4).
- **A presuppositional analysis of definite descriptions (Lasersohn 2005, [doi:10.1162/0024389052993646](https://doi.org/10.1162/0024389052993646)).** Known here by its title and Löbner's report: "Lasersohn (2005) proposes a type ⟨e,t⟩ analysis for temperature and price." (n. 18). Not read.
- **Temporal interpretation (Romero 2008, [doi:10.1162/ling.2008.39.4.655](https://doi.org/10.1162/ling.2008.39.4.655)).** Known by its title, "The Temperature Paradox and Temporal Interpretation", and as one of the reviews Löbner cites: "It has been discussed and criticized in various ways (see Lasersohn 2005, Schwager 2007, and Romero 2008 for reviews of the sparse literature and for further discussion)." (§1.3, p. 6). Not read.
- **Two composition rules and typed nouns (Löbner 1979; 2020).** Löbner's own proposal: "If we do not adhere to Montague’s strategy of generalizing to the worst case, we may assume that there are two different composition rules for extensional and intensional predication: extensional predication applies to arguments of logical type e, and intensional predication to arguments of type ⟨s,e⟩." (§3.2, p. 15); he dates the noun treatment to "Löbner (1979: 181ff)" (n. 18).
  *Against:* no criticism of this proposal was found in the sources read.

## Arguments in play

(none recorded as separate argument pages yet). The argument itself and the
propositional check are in The question; the [validity](../vocabulary/validity.md)
claims in play are Montague's ("turns out not to be valid") and Löbner's
("This entailment clearly is invalid"), both quoted above.

## Thinkers who addressed it

- **Barbara Hall Partee** — the puzzle is "due to" her per Montague (p. 30); "Professor Partee's the temperature is ninety but it is rising" (p. 17). Her own formulation was not read.
- **Richard Montague** (PTQ, 1973, pp. 221–242; reprint pp. 17–18, 30–31) — individual concepts and an intensional *rise*.
- **Ray Jackendoff** ("How to keep ninety from rising", 1979) — the second premise as localisation on a scale, per Löbner.
- **Sebastian Löbner** (*Intensionale Verben und Funktionalbegriffe*, 1979; Companion chapter, 2020) — time-intensional verbs, noun types, two composition rules.
- **David Dowty, Robert Wall, Stanley Peters** (*Introduction to Montague Semantics*, 1981, pp. 284f) — the objection that *the temperature* need not be the same individual concept at different times, per Löbner n. 11.
- **Theo M. V. Janssen** ("Individual concepts are useful", 1984) — for keeping individual concepts, per Löbner n. 6.
- **Peter Lasersohn** (2005) and **Maribel Romero** (2008), *Linguistic Inquiry* — responses (bibliographic only; `raw/temperature-paradox-bibliographic-records.md`).
- **Magdalena Schwager** (2007) — cited by Löbner as a review; not read.
- **Theo M. V. Janssen and Thomas Ede Zimmermann** (SEP 2021, Fall 2024 archive) — encyclopedia placement of the example.

## Framings and reframings

- **A puzzle about substitution of identicals.** Löbner: "Various suggestions were made in order to defend Leibniz’ Law in view of Partee’s (apparent) paradox; they all amount to the result that (4) is not really of the general form given in (3)." (§1.2, p. 3) — that is, not of the form *P(x)*, *x = y*, therefore *P(y)*.
- **A puzzle of formal semantics, not of temperature.** Wikipedia's article frames it so: "The Temperature paradox or Partee's paradox is a classic puzzle in formal semantics and philosophical logic. Formulated by Barbara Partee in the 1970s, it consists of the following argument, which speakers of English judge as wildly invalid." (rev. 1374159050); Löbner extends it to *the president*, *the number of students* and the German verb *wechseln* (§1.2, pp. 3–4).
- **Definite versus indefinite subjects.** Montague: "It would be possible to treat the Partee argument itself without introducing this feature, but not certain analogous arguments involving indefinite rather than definite terms." (p. 31); "Notice, for instance, that a price rises and every price is a number must not be allowed to entail a number rises." (p. 31).
- **Kinship with intensional contexts.** The SEP pairs it with *John wishes to catch a fish and eat it* (§2.4); Löbner with concealed questions such as *know the price* (abstract).

Not in the excerpts held: Partee's own presentation, Lasersohn 2005,
Romero 2008, Schwager 2007, Jackendoff 1979, Dowty, Wall and Peters 1981,
Janssen 1984, Frana 2017 and Gamut 1991 (cited by Wikipedia); they are left
out until a text is read.

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — see The question.
- [Validity](../vocabulary/validity.md) — the claims that the argument is or is not valid.
- [Classical logic](../methods/classical-logic.md) — the propositional check; Leibniz' Law belongs to predicate logic with identity.
- *Intension*, *extension*, *individual concept*, *intensional verb*, *Leibniz' Law (substitution of identicals)*, *concealed question* — open work in [vocabulary](../vocabulary/index.md).
