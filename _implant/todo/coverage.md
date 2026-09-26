---
type: todo
title: Coverage ledger — this implant vs Wikipedia's lists
description: "The ledger that turns the README's 'more than Wikipedia' amount claim into a number: per branch, pages held here against the entries of a named, revision-pinned Wikipedia list, with the date counted. First count 2026-09-26: the implant is far behind on amount in every branch."
tags: [todo, coverage, benchmark, wikipedia, amount]
timestamp: 2026-09-26T09:54:50Z
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

## First count: 2026-09-26

Counted in the session recorded in the [journal of 2026-09-26](../journals/2026-09-26.md).

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
