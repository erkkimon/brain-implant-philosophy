---
type: article
about: concept
title: "MVP: the bar for the first usable version"
description: "What the implant must hold before it is worth mounting and worth telling people about — the smallest content set that makes every advertised skill land on at least one fully verified example, every branch populated, and the three README claims checkable. Decided 2026-09-25; the work queue in ../todo/open.md follows this bar. Anything past the bar is Phase 2 breadth, done incrementally, not a gate on the first release."
tags: [plan, mvp, roadmap, release, breadth]
timestamp: 2026-09-25T23:55:00Z
---

# MVP: the bar for the first usable version

A structural note the implant adds to make its own roadmap checkable
([manifest](../vision/manifest.md) G4 — comparison and structure are ours,
evaluation never is). This page decides *what counts as done enough to ship
v0.1*. It is a choice, not a theorem; the reasoning is on the page so a
reader can disagree with the bar and change it.

## What the MVP is for

The README makes three promises — neutrality, quality, amount — and lists
eight skills. The MVP is the point where **every promise is real and every
skill lands on at least one fully verified example**, so that a stranger who
mounts the implant and tries any advertised capability gets a working
answer instead of an empty folder. Before this bar the implant is a scaffold
with two rooms furnished; after it, it is a usable first version worth
publishing.

This is deliberately a *breadth* bar, not a *depth* bar. Phase 2 fills each
room toward the canon; that is incremental work done after the release, one
committed-and-pushed increment at a time, and never a gate on v0.1.

## The bar (a checklist, each item a hard gate)

### 1. Machinery — already true at v0.1 candidate

- [x] Both implants compile fresh, 0 ghosts / 0 orphans.
- [x] Neutrality lint clean across `knowledge/ skills/ conventions/ vision/`.
- [x] Tools pass self-test (`selftest.py`, `logic.py`, `neutrality-lint.py`).
- [x] README documents both install paths and the disclaimer.
- [ ] `brainpick register` succeeds for **both** repos on one machine and a
      mounted agent can cross from a philosophy page to a
      [estimate-a-credence](../skills/index.md) skill in cognitive-tools.

### 2. Every skill lands on a verified example

Each skill in the README must have at least one page whose content it can
act on, end to end:

| Skill | Needs at least one | Status |
| --- | --- | --- |
| Analyse an argument | an `arguments/` page with a `logic.py` reconstruction | ✅ four (Chinese room, Leibniz's mill, zombie, knowledge) |
| Steelman a position | a contested `positions/` page with case-for and case-against | ✅ nine (consciousness) |
| Compare thinkers | two+ thinkers on one problem with attributed reception | ✅ consciousness hub |
| Spot persuasion and bias | `persuasion/` + `biases/` pages with classification and replication record | ✅ three each, thin |
| Write persuasively | a persuasion inventory to choose from | ✅ |
| Debate | a problem page with real opposing positions | ✅ consciousness |
| Estimate a credence (cognitive-tools) | factors/base-rates the model can cite | ⚠️ needs the register check above |

### 3. Every branch populated (no empty advertised folder)

The README lists ten `knowledge/` branches. An empty one is a broken promise:

- [x] `problems/` — consciousness, AI consciousness
- [x] `positions/` — nine on consciousness
- [x] `arguments/` — four
- [x] `thinkers/` — four
- [ ] `works/` — empty → needs primary works (see below)
- [ ] `schools/` — empty → needs at least one real school
- [x] `persuasion/` — three
- [x] `biases/` — three
- [ ] `vocabulary/` — empty → the terms every page leans on
- [ ] `methods/` — empty → classical logic, reflective equilibrium, etc.

### 4. The three README claims made checkable

- **Neutrality** — lint clean (done) *and* selection breadth visible.
- **Quality** — receipts resolve on every shipped page (done via raw/).
- **Amount** — needs `todo/coverage.md`, the ledger that turns "more than
  Wikipedia" into a number. Without it the amount claim is an impression.

## Minimum content to clear the bar

Concrete, small, and enough to make all ten branches non-empty and give the
two thin skills (persuasion, bias) and the vocabulary/methods folders real
teeth. Each item is one page written with
[Write a page](../skills/write-a-page.md) through its review checklist.

**Fill the empty branches (the binding constraint):**
- works: at least one landmark per major tradition already touched — e.g.
  Descartes' *Meditations*, Chalmers *The Conscious Mind*, Dennett
  *Consciousness Explained*, Birch *The Edge of Sentience*; plus one classical
  anchor (*Mūlamadhyamakakārikā* or the *Abhidharma*) for non-Western balance.
- schools: at least two — one ancient (Stoicism or Nyāya), one modern (logical
  positivism or functionalism-as-school) — each with the thinkers it holds.
- vocabulary: the load-bearing terms — argument, validity, knowledge, *fallacy*,
  persuasion/rhetoric/dialectic (the spectrum split), plus consciousness
  (phenomenal/access), qualia, sentience, moral patient.
- methods: classical logic as working logic (G1), reflective equilibrium,
  Bayesian updating with the case against.

**Add one more exemplar problem** so the graph is not one-topic: the free-will
and determinism cluster (problem + compatibilism + hard incompatibilism +
Frankfurt cases + consequence argument + Hume) or the problem of induction
(problem + Hume's argument + the Gettier problem for epistemology). Pick one
for v0.1; the other is first Phase-2 item.

**Make "amount" real:** create `todo/coverage.md` with a first comparison
against Wikipedia's lists (philosophers, unsolved problems, *fallacies*,
cognitive biases) and the date it was last counted.

**Wire the two implants:** register both on one machine, verify a philosophy
page can reach a cognitive-tools skill, record the result.

## What is explicitly NOT in the bar

- The ~1000-page Phase 2 canon — that is post-release breadth.
- Agentic generation against the ledger (Phase 3).
- Every tradition fully represented — MVP needs *some* non-Western anchor in
  each touched branch, not complete coverage.
- A psychology or other sibling implant.

## Ship checklist (the moment v0.1 goes out)

1. `brainpick compile --root .` fresh on both repos, 0 ghosts / 0 orphans.
2. Neutrality lint clean; `selftest.py` green.
3. All ten `knowledge/` branches non-empty and linked in their index.
4. `todo/coverage.md` exists with a dated first count.
5. Both implants registered together; cross-implant skill reach confirmed.
6. README "Quick start" followed top to bottom on a clean machine.
7. Tag `v0.1`; announce with the disclaimer that content is agent-distilled.
