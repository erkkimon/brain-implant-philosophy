---
type: article
about: concept
title: "Opposite Day"
description: "The children's make-believe game in which things are said and done in an opposite manner, and the puzzle of declaring 'It is opposite day today' on Opposite Day: Wikipedia's article and List of paradoxes file it as a self-referential paradox, a 2018 children's-science lesson pairs it with the liar paradox; no philosophical or logical publication on it was found, so the page stays descriptive."
tags: [problem, paradox, logic, self-reference, liar-family]
timestamp: 2026-10-01T22:52:16Z
---

# Opposite Day

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Sources: Wikipedia, ["Opposite Day"](https://en.wikipedia.org/w/index.php?title=Opposite_Day&oldid=1374161290)
rev. 1374161290 and [List of paradoxes](https://en.wikipedia.org/w/index.php?title=List_of_paradoxes&oldid=1376699902)
rev. 1376699902, "Logic" (excerpt: `raw/wikipedia-opposite-day-rev-1374161290-and-list-entry.md`);
Brains On! (American Public Media), [educator sheet](https://files.apmcdn.org/production/c36785c689e0d730451a4d80eb70bee2.pdf)
for the episode of 20 February 2018 (excerpt: `raw/apm-brains-on-2018-opposite-day-paradoxes-educator-guide.md`).
Admitted from Wikipedia's List of paradoxes, revision 1376699902, "Logic".
The related problem is [the liar paradox](liar-paradox.md).

**Sources are thin.** Searches made on 2026-10-02 found no philosophical or
logical publication discussing Opposite Day: the SEP Fall 2024 entries "Liar
Paradox", "Self-Reference" and "Dialetheism" contain no occurrence of the
phrase, and Crossref and OpenAlex full-text queries for "opposite day" with
"paradox", "liar" or "liar paradox" returned no work on the topic. The page
therefore reports the two non-academic sources above and adds only a
propositional check; it is kept short until a source is found.

## The question

Wikipedia's article describes the game: "Opposite Day is a make believe game usually played by children. Conceptually, Opposite Day is a holiday where things are said and done in an opposite manner." (rev. 1374161290, lead).
The puzzle, in the List's words: "Opposite Day: "It is opposite day today." Therefore, it is not opposite day, but if one says it is a normal day it would be considered a normal day, which contradicts the fact that it has previously been stated that it is an opposite day." (List of paradoxes, rev. 1376699902, "Logic").
A question form from the children's-science source: "Think about it: the answer to the question “Is it opposite day?” will always be no. So how do you figure out if it is, in fact, opposite day?" (Brains On! 2018, educator sheet, p. 1).

**Propositional check (this implant, 2026-10-02; logic, not a position).**
Let *O* stand for *it is Opposite Day*, and read the List's two steps as
conditionals: on Opposite Day the declaration "It is opposite day today"
counts as its opposite, giving *O* -> ~*O*; the List's second clause, that
saying it is a normal day would make it count as Opposite Day after all, is
read as ~*O* -> *O*. (The choice of formalisation is this implant's; the
sources state the case in prose only.)
- `logic.py check --premises "O -> ~O" "~O -> O" --conclusion "O & ~O"` outputs `VALID` and `premises are jointly inconsistent — argument is vacuously valid`.
- The first step alone: `--premises "O -> ~O" --conclusion "~O"` outputs `VALID`; against `--conclusion "O & ~O"` it outputs `INVALID` with the counterexample row `O=F`.
- The second step alone: `--premises "~O -> O" --conclusion "O & ~O"` outputs `INVALID` with the counterexample row `O=T`.

So, within classical propositional logic, a contradiction follows only when
both directions are taken together; the first direction alone yields ~*O*, which matches the List's first conclusion, "it is not opposite day". The tool is
propositional and does not model the declaring, the time at which the day
begins, or the reversal of meaning itself.

## Why it matters

- **Filed among the self-referential paradoxes.** The List places it in the subsection of paradoxes, "insolubilia (insolubles)", that "have in common a contradiction arising from either self-reference or circular reference" (rev. 1376699902, "Logic"), between "Yablo's paradox" and "Richard's paradox". The article is in Wikipedia's category "Self-referential paradoxes" (rev. 1374161290).
- **Paired with the liar.** The Brains On! lesson objective: "Students will understand the concept of paradoxes, specifically the opposite day paradox and the liar paradox, and learn how logic and inference can be used to analyze and solve these types of puzzles." (educator sheet, p. 1). See [the liar paradox](liar-paradox.md), whose List entry reads "Liar paradox: "This sentence is false." This is the canonical self-referential paradox. Also "Is the answer to this question 'no'?", and "I'm lying."" (rev. 1376699902).
- **A children's way into the notion of paradox.** The article reports that "The game has also been compared to a children's "philosophy course" in the way that it encourages children to think." (rev. 1374161290, citing Shelton, *Preschool Confidential*, 2001, pp. 232–234, not read here).

## Positions taken

No published position on how the Opposite Day puzzle is resolved was found
(see *Sources are thin* above). What is on record, by owner, unranked:

- **A self-contradiction (Wikipedia article, rev. 1374161290, lead; no reference attached).** "Opposite Day is an example of a paradox; declaring Opposite Day is a self-contradiction meaning that it is in fact not Opposite Day but is at the same time."
- **The declaration undoes itself (Wikipedia List, rev. 1376699902).** From "It is opposite day today." the entry draws "Therefore, it is not opposite day", then adds the reverse step quoted in The question.
- **The question answers no (Brains On! 2018, educator sheet).** "How does the answer to 'Is it opposite day?' always end up being 'no'?" (p. 1, a question put to students; the sheet refers to the episode for the answer, and the episode audio was not heard here).

## Arguments in play

(none recorded as separate argument pages yet). The only derivation on
record is the List's two-step prose, formalised and checked in The question.

## Thinkers who addressed it

No philosopher or logician is on record in the sources read. The sources are
anonymous or collective: Wikipedia contributors (the article and the List),
and the Brains On! team at American Public Media (2018). Sandi Kahn Shelton
(*Preschool Confidential*, Macmillan 2001, ISBN 9780312254582) is cited by
the article for the "philosophy course" comparison; her text was not read.

## Framings and reframings

- **A game rule rather than a sentence.** The article frames Opposite Day as a declaration that changes how speech is taken: "one can declare that any day of the year is Opposite Day (sometimes retroactively) to indicate something which will be said, or has just been said should be understood opposite to its original meaning (similar to the practice of crossed fingers to automatically nullify promises)." (rev. 1374161290, lead), and "Opposite Day begins when someone declares it to be Opposite Day, and ends whenever they stop." ("Game mechanics", a section tagged unreferenced since May 2022).
- **In comic and sketch form.** The article reports Hobbes's line "I meant 'no, there is a bee'. Today is Opposite Day!" (*Calvin and Hobbes*, 2 June 1988), and a *Whitest Kids U' Know* sketch in which "The judge and prosecution both protest that "it's not Opposite Day", but their statements are taken in the opposite meaning, accidentally affirming that it is in fact Opposite Day." (rev. 1374161290, "In popular culture").
- **Structural note (this implant, not a source's claim).** The List's liar entry includes the question form "Is the answer to this question 'no'?"; the Brains On! sheet poses "Is it opposite day?" as a question whose answer "will always be no". No source read compares the two forms.

Not in the excerpts held: Shelton 2001; the Brains On! episode audio; a
Philosophy Stack Exchange thread and several blog posts on the topic that
returned 403 or were not scholarly; they are left out until a source is read.

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — the List's "insolubilia (insolubles)" heading.
- [Validity](../vocabulary/validity.md) — the propositional check above.
- [Classical logic](../methods/classical-logic.md) — the logic of the check.
- *Self-reference*, *circular reference* (the List's terms) — open work in [vocabulary](../vocabulary/index.md).
