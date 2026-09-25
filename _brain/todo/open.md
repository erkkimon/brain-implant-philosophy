---
type: todo
title: Open
description: What is still to be done — the implant's live work queue.
timestamp: 2026-09-25T18:30:00Z
---

# Open

Tasks that surface mid-work land here instead of derailing the task at hand.
Check this list before planning new work. Tick an item as `- [x] … (done:
YYYY-MM-DD)` and move it to `archive/YYYY-MM-DD.md` the same or the next day.

## Phase 1 — exemplars (one to three pages per branch, fully verified)

- [ ] problems: the problem of induction; the Gettier problem; free will and determinism
- [ ] positions: compatibilism; hard incompatibilism; Madhyamaka emptiness (as a position on the problem of intrinsic nature)
- [ ] arguments: Frankfurt cases; the consequence argument; Hume's argument concerning induction — each with `logic.py` output
- [ ] thinkers: Hume; Nāgārjuna; Kant; Frankfurt; Anscombe — hubs of links, reception attributed
- [ ] works: *Treatise of Human Nature*; *Mūlamadhyamakakārikā*; *Critique of Pure Reason*
- [ ] schools: Nyāya; Stoicism; logical positivism
- [ ] persuasion: appeal to authority (scheme and fallacy classifications side by side); framing; the straw man
- [ ] biases: anchoring; confirmation bias; availability — each with canonical DOI, replication record, ecological-rationality critique
- [ ] vocabulary: argument; validity; knowledge; persuasion / rhetoric / dialectic / argumentation (the spectrum split); fallacy
- [ ] methods: classical logic (working logic, G1); Bayesian updating with the case against; reflective equilibrium

## Infrastructure

- [ ] `todo/coverage.md`: the coverage ledger — per branch, count of pages here vs Wikipedia's lists of philosophers, unsolved problems in philosophy, fallacies, cognitive biases; date of last comparison
- [ ] `henxels_checks.py`: a make_sure_that henxel that runs `neutrality-lint.py` over `knowledge/` on commit
- [ ] extend `logic.py` schema matching beyond the seven named forms; consider a first-order fragment
- [ ] settle the `[knowledge]` search excludes for `raw/` in brainpick.toml once raw/ has files
- [ ] set `origin` in brainpick.toml when the upstream repository exists

## Phase 2 — core canon

- [ ] ~100 thinkers, ~50 problems, ~150 positions, ~200 arguments, ~150 techniques, ~150 biases, ~300 terms — each page through [Write a page](../skills/write-a-page.md) with the review checklist
- [ ] traditions entering under the same rule from the start: Indian, Chinese, Islamic, African, Indigenous, Japanese, Latin American, European

## Phase 3 — breadth

- [ ] agentic generation against the coverage ledger, with the verification gate (receipts resolve, lint clean, ideological Turing test) as a hard stop
