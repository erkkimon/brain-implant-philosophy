---
type: todo
title: Coverage ledger — this implant vs Wikipedia's lists
description: "The ledger that turns the README's 'more than Wikipedia' amount claim into a number: per branch, pages held here against the entries of a named, revision-pinned Wikipedia list, with the date counted. First count 2026-09-26: the implant is far behind on amount in every branch."
tags: [todo, coverage, benchmark, wikipedia, amount]
timestamp: 2026-10-08T21:37:56Z
---

# Coverage ledger

This is a structural note the implant keeps about itself
([manifest](../vision/manifest.md) G4). It is the *amount* benchmark in the
[MVP plan](../plans/mvp.md) and the [MLP plan](../plans/mlp.md). Neutrality
and quality are measured elsewhere: neutrality by the lint, quality by
receipts in `raw/`.

## How it is counted

- **Wikipedia side.** Each list is pinned to a revision id, so the count
  can be repeated. Entries are the bullet or table lines of the list body
  that begin with an article link. Lines after "See also" and
  "References" are excluded. Headed entries (`===…===`) are counted where
  the list is organised by headings.
- **Implant side.** Pages in the matching `knowledge/` folder, excluding
  `index.md`.
- A match is counted only if the implant has a page for the same topic.
  Mentions inside other pages do not count.

## Recount: paradoxes and ethics, 2026-10-01

Method as above. Counted by script over the pinned wikitext (bullet lines
whose first element is an article link, `{{bl|…}}` or `{{anl|…}}`; "See
also" and later excluded; an entry listed in two sections counted once, under the first); the
matches were assigned by hand, one implant page per entry
([journal](../journals/archive/2026/10/2026-10-01.md)).

**[List of paradoxes](https://en.wikipedia.org/w/index.php?oldid=1376699902)
(1376699902):** 294 unique entries, 20 matched.

| Section | Entries | Matched here |
|---|---|---|
| Logic | 34 | 8 (lottery, raven, unexpected hanging, Curry, liar, Russell, Ship of Theseus, sorites) |
| Philosophy | 18 | 6 (Fitch, Meno, mere addition, Moore, preface, problem of evil) |
| Decision theory | 28 | 3 (Buridan's ass, Newcomb, prisoner's dilemma) |
| Mathematics | 46 | 2 (Simpson, Zeno) |
| Economics | 34 | 1 (St. Petersburg) |
| Physics, Biology, Chemistry, Time travel, Perception | 101 | 0 |
| Psychology and sociology, Politics, Linguistics and AI, Mysticism, Miscellaneous | 33 | 0 |

"Problem of evil" is matched to the [Epicurean trilemma](../knowledge/problems/epicurean-trilemma.md),
"Mere addition paradox" to the [repugnant conclusion](../knowledge/problems/repugnant-conclusion.md)
and the preface paradox to the joint [lottery and preface](../knowledge/problems/lottery-and-preface-paradoxes.md)
page; each is a page on the entry's topic under another title. Several
problem pages here are not on the list (trolley problem, Euthyphro,
Agrippan trilemma, Jim, the ethics pages).

**[Outline of ethics](https://en.wikipedia.org/w/index.php?oldid=1369745706)
(1369745706)** (the title "Index of ethics articles" redirects to it; no
"List of ethical problems" or "List of oxymorons" article exists at this
date): 347 unique entries, 10 matched — Branches 4 of 139 (non-identity
problem, animal rights and ethics of eating meat → [moral status of animals](../knowledge/problems/moral-status-of-animals.md),
population ethics → [repugnant conclusion](../knowledge/problems/repugnant-conclusion.md)),
Concepts 2 of 49 (just war, moral patienthood), Persons 4 of 38 (Anscombe,
Foot, Williams, Nagel); History, Law, agencies, awards, organisations,
events and publications 0 of 123.

**Selection rule for the next batches (stated, not taste).** The list
sections that are philosophy by their own heading come first: unmatched
entries of "Philosophy" (12), then "Logic" (26), then the 34 unmatched
"Persons influential in the field of ethics", then "Decision theory" and
"Concepts". Within a section, entries are taken in the list's own order,
8–12 per batch. The batches are queued in [open work](open.md).

## Interim note: 2026-10-09 (after "Decision theory" batch 2)

List of paradoxes "Decision theory": 18 → 28 of 28 (complete); list overall
73 → 83 of 294. Problems held: 100.

## Interim note: 2026-10-08 (after "Decision theory" batch 1)

List of paradoxes "Decision theory": 3 → 18 of 28 (the apportionment page
covers its three sub-entries); list overall 58 → 73 of 294. Problems held: 90.

## Interim note: 2026-10-08 (after ethics thinkers batch 3)

"Persons influential": 29 → 38 of 38 (complete); Outline of ethics overall
35 → 44 of 347. Thinkers held: 49.

## Interim note: 2026-10-08 (after ethics thinkers batch 2)

"Persons influential": 19 → 29 of 38; Outline of ethics overall 25 → 35
of 347. Thinkers held: 40.

## Interim note: 2026-10-02 (parked)

Mill, Sidgwick and Nietzsche were added: "Persons influential" 16 → 19 of
38; Outline of ethics overall 22 → 25 of 347. Thinkers held: 30.

## Interim note: 2026-10-02 (after ethics thinkers batch 1)

Outline of ethics, "Persons influential": 4 → 16 of 38. Outline of ethics
overall: 10 → 22 of 347. Thinkers held: 27.

## Interim note: 2026-10-02 (after paradoxes batch 5)

The "Logic" section is complete: 34 of 34. List of paradoxes: 58 of 294
matched. Problems held: 78.

## Interim note: 2026-10-02 (after paradoxes batch 4)

13 of the 26 unmatched "Logic" entries now have pages: List of paradoxes
32 → 45 of 294 matched; "Logic" 8 → 21 of 34. Problems held: 65.

## Interim note: 2026-10-01 (after paradoxes batch 3)

The 12 unmatched "Philosophy" entries of the List of paradoxes now have
pages: that list's matches go from 20 to 32 of 294, and the "Philosophy"
section from 6 to 18 of 18. Problems held: 52.

## Interim note: 2026-10-01

Not a recount. Added: thinkers 13 → 15 (Jung, de Mello), works 5 → 10,
vocabulary 13 → 16 ([journal](../journals/archive/2026/10/2026-10-01.md)). Neither Jung nor
de Mello is on the pinned "List of philosophers of mind"; the full
"Lists of philosophers" count (open work below) is where they would be
matched.

## Interim note: 2026-09-27

Not a recount (the next full count follows the paradox, dilemma and
ethics batches, per [next steps](../plans/next-steps.md)). Problems held:
40 (6 before today, 34 added today). The 13 paradoxes, 9 dilemmas and 12 ethical problems added today (listed in the
[problems index](../knowledge/problems/index.md)) are to be matched
against Wikipedia's "List of paradoxes", which is not yet pinned or counted.

## First count: 2026-09-26

Counted in the session recorded in the [journal of 2026-09-26](../journals/archive/2026/09/2026-09-26.md).

| Branch | Here | Wikipedia list (revision) | Entries | Matched here |
|---|---|---|---|---|
| biases | 3 | [List of cognitive biases](https://en.wikipedia.org/w/index.php?oldid=1376537524) (1376537524) | 213 | 3 (anchoring, availability, confirmation bias) |
| persuasion | 3 | [List of fallacies](https://en.wikipedia.org/w/index.php?oldid=1376371622) (1376371622) | 131 | 2 (appeal to authority, straw man); framing is on the biases list |
| problems | 2 | [List of philosophical problems](https://en.wikipedia.org/w/index.php?oldid=1375414325) (1375414325) | 27 headed entries | 1 direct (hard problem of consciousness); AI consciousness overlaps "Cognition and AI" |
| thinkers | 4 | [List of philosophers of mind](https://en.wikipedia.org/w/index.php?oldid=1373599106) (1373599106) | 200 | 4 (Descartes, Nagel, Chalmers, Dennett) |
| positions, arguments, works, schools, vocabulary, methods | 9, 4, 5, 2, 10, 3 | no single comparable list chosen yet | — | — |

Result on amount: Wikipedia's lists are between about 13× and 70× larger in
every branch counted. The README's amount claim is a goal, not a present
fact. The quality side of the comparison is different in kind. Each page
here holds the verbatim receipts, positions ranked by no one, and the case
for and against. A per-page quality comparison has not been made yet.

## Open work

- [ ] choose a comparable Wikipedia list (or category) for positions,
      arguments, works, schools, vocabulary and methods, and count it
- [ ] count against the full "Lists of philosophers" set, not only
      philosophers of mind, once thinkers go beyond the consciousness
      cluster
- [ ] per-page quality comparison: for each matched page, compare it with
      the Wikipedia article on citations per claim, positions represented,
      and primary-text quotations; record the method before the result
- [ ] recount on every release tag and add a dated section above the
      previous one
- [ ] problems: Gettier problem, problem of induction, personal identity,
      mind–body problem, qualia (as a problem), demarcation problem, moral
      luck — the entries on Wikipedia's list nearest the MLP clusters
