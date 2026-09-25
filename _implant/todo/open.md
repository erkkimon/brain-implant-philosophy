---
type: todo
title: Open
description: What is still to do — the implant's live work queue, ordered against the MVP bar in ../plans/mvp.md.
timestamp: 2026-09-25T23:59:00Z
---

# Open

Tasks that surface mid-work land here instead of derailing the task at hand.
Check this list before planning new work. Tick an item as `- [x] … (done:
YYYY-MM-DD)` and move it to `archive/YYYY-MM-DD.md` the same or the next day
(first day closed: [2026-09-25](archive/2026-09-25.md)).

The order below follows the MVP bar in [plans/mvp.md](../plans/mvp.md): the
first section is everything standing between now and a usable v0.1; the
later sections are the incremental breadth that follows the release, one
committed-and-pushed increment at a time.

## To v0.1 — clear the bar (see [MVP plan](../plans/mvp.md))

The binding constraint is four empty branches (`works/ schools/ vocabulary/
methods/`) plus making the "amount" claim a number and wiring the two
implants together. Write each page with
[Write a page](../skills/write-a-page.md) through its review checklist.

### Fill the empty branches

- [ ] works: *Meditations*; *The Conscious Mind*; *Consciousness Explained*;
      *The Edge of Sentience*; one non-Western anchor (*Mūlamadhyamakakārikā*
      or the *Abhidharma*)
- [ ] schools: at least two — one ancient (Stoicism or Nyāya), one modern
      (logical positivism, or functionalism as a school) — each listing the
      thinkers it holds

### Make the README claims checkable

- [ ] `todo/coverage.md`: the coverage ledger — per branch, count of pages
      here vs Wikipedia's lists of philosophers, unsolved problems in
      philosophy, fallacies, cognitive biases; date of last comparison (this
      is what makes "amount" a number, not an impression)
- [ ] `brainpick register` **both** repos (philosophy + cognitive-tools) on one
      machine; confirm a philosophy page can reach a cognitive-tools skill
      (`estimate-a-credence`); record the result in the journal

### One more exemplar problem (so the graph is not single-topic)

- [ ] free will and determinism **or** the problem of induction — pick one for
      v0.1, the other is the first post-MVP item:
  - free will: problem + compatibilism + hard incompatibilism + Frankfurt
    cases (argument, with `logic.py`) + the consequence argument (argument,
    with `logic.py`) + Frankfurt and Anscombe (thinkers)
  - induction: problem + Hume's argument concerning induction (argument, with
    `logic.py`) + Hume (thinker) + *Treatise* (work)

### Ship checklist (all must pass to tag v0.1)

- [ ] compile fresh on both repos, 0 ghosts / 0 orphans
- [ ] neutrality lint clean; `selftest.py` green
- [ ] all ten `knowledge/` branches non-empty and listed in their index
- [ ] `todo/coverage.md` exists with a dated first count
- [ ] both implants registered together; cross-implant skill reach confirmed
- [ ] README "Quick start" followed top to bottom on a clean machine
- [ ] tag `v0.1` with the agent-distilled disclaimer in the release note

## Post-MVP — incremental breadth (commit + push each increment)

### Consciousness cluster follow-ups

- [ ] primary-text excerpts for the Buddhist, Advaita and Chinese rows (now
      SEP-only); Metzinger, Schneider (ACT), Shanahan, Lau, Michel for the AI
      table; Levine 1983 as its own argument page; a citable primary source
      for the Kyle Fish credence figure or drop the mention
- [ ] the exemplar problem not chosen for v0.1 (free will or induction)

### Remaining Phase 1 exemplars (one to three pages per branch)

- [ ] problems: the Gettier problem; the problem of intrinsic nature
- [ ] positions: Madhyamaka emptiness (as a position on intrinsic nature)
- [ ] thinkers: Hume; Nāgārjuna; Kant; Frankfurt; Anscombe
- [ ] works: *Treatise of Human Nature*; *Mūlamadhyamakakārikā*; *Critique of
      Pure Reason*
- [ ] schools: Nyāya; Stoicism; logical positivism (beyond the two in v0.1)

### Tooling

- [ ] extend `logic.py` schema matching beyond the seven named forms; consider
      a first-order fragment

## Later phases

- [ ] **Phase 2 canon:** ~100 thinkers, ~50 problems, ~150 positions, ~200
      arguments, ~150 techniques, ~150 biases, ~300 terms — each page through
      [Write a page](../skills/write-a-page.md); traditions entering under the
      same rule from the start (Indian, Chinese, Islamic, African, Indigenous,
      Japanese, Latin American, European)
- [ ] **Phase 3 breadth:** agentic generation against the coverage ledger, with
      the verification gate (receipts resolve, lint clean, ideological Turing
      test) as a hard stop

## Related implants (cross-repo, not this repo's pages)

- [ ] mount cognitive-tools in stem / apologetics / theology implants
- [ ] possible psychology implant (biases would move or cross-link there)
