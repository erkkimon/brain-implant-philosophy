---
type: article
about: concept
title: "MLP: the bar for minimum lovable product"
description: "What the implant must hold before it is worth telling people about beyond early adopters — the point where the graph is broad enough that a stranger mounting it for the first time finds something useful on their actual question, not just on the exemplar topics. Decided 2026-09-25; follows the MVP bar in mvp.md and defines the next release target."
tags: [plan, mlp, roadmap, release, breadth]
timestamp: 2026-09-25T23:59:00Z
---

# MLP: the bar for minimum lovable product

A structural note the implant adds to make its own roadmap checkable
([manifest](../vision/manifest.md) G4). This page decides *what counts as
done enough to tell people about*. It follows the
[MVP bar](mvp.md) and defines the gap between "usable" and "worth sharing".

## What MLP is for

MVP proves the machinery works and every advertised skill lands on at least
one verified example. MLP proves the graph is **broad enough that a stranger
mounting it for the first time finds something useful on their actual
question**, not just on the exemplar topics the maintainers happened to
build first. The difference: MVP is "the thing works"; MLP is "the thing
works *for you*".

This is still a choice, not a theorem. The bar below is calibrated for a
public announcement and early community adoption; it can be revised as the
implant learns what users actually need.

## The bar (a checklist, each item a hard gate)

### 1. MVP shipped and stable

- [ ] v0.1 tagged and announced with the agent-distilled disclaimer.
- [ ] Both implants registered together; cross-implant skill reach confirmed.
- [ ] `todo/coverage.md` exists with a dated first count.

### 2. Breadth that covers real questions

A stranger's first question is unlikely to be about consciousness or free
will. The graph needs enough coverage that common philosophical questions
land on populated pages:

- [ ] **Three exemplar problems** complete (not one): consciousness (done),
      free will and determinism, and the problem of induction. Each with
      problem page, at least two positions, at least one argument with
      `logic.py`, and at least one thinker.
- [ ] **Works branch** populated with at least five landmark texts spanning
      traditions: *Meditations*, *The Conscious Mind*, *Consciousness
      Explained*, *The Edge of Sentience*, and one non-Western anchor
      (*Mūlamadhyamakakārikā* or the *Abhidharma*).
- [ ] **Schools branch** populated with at least three schools spanning
      eras and traditions: one ancient Western (Stoicism), one ancient
      non-Western (Nyāya), one modern (logical positivism).
- [ ] **Thinkers branch** has at least ten pages spanning eras and
      traditions: the four done (Descartes, Nagel, Chalmers, Dennett) plus
      Hume, Nāgārjuna, Kant, Frankfurt, Anscombe, and one non-Western
      thinker not yet covered.
- [ ] **Persuasion and biases** each have at least ten pages with full
      primary-source quotations and replication records (currently three
      each).

### 3. Quality that survives scrutiny

- [ ] Every page passes the [write-a-page](../skills/write-a-page.md) review
      checklist: admission rule, six claim kinds, receipts resolve, lint
      clean, case-for and case-against pass the ideological Turing test.
- [ ] No SEP-only pages remain without at least one primary-text excerpt
      (the consciousness cluster follow-ups).
- [ ] Coverage ledger updated against Wikipedia's lists; the implant beats
      Wikipedia on at least one of the three benchmarks (neutrality, amount,
      quality) in at least one branch.

### 4. Usability beyond the maintainer

- [ ] README "Quick start" followed top to bottom on a clean machine by
      someone who has never seen the repo.
- [ ] At least one external user (not erkkimon) has mounted the implant and
      reported what broke or confused them.
- [ ] The cognitive-tools implant is registered alongside philosophy on at
      least one external machine; cross-implant credence estimation works.

### 5. Community readiness

- [ ] Contributing guide tested: an external contributor (human or agent)
      writes a page through [write-a-page](../skills/write-a-page.md) and
      it passes henxels on first try.
- [ ] License and disclaimer visible in README and in every distributed
      artifact.
- [ ] Tag `v0.2`; announce with a changelog from v0.1.

## What is explicitly NOT in the bar

- The ~1000-page Phase 2 canon — that is post-MLP breadth.
- Agentic generation against the ledger (Phase 3).
- Every tradition fully represented — MLP needs *some* representation in
  each touched branch, not complete coverage.
- A psychology or other sibling implant.
- Perfection. MLP is "worth telling people about", not "finished".

## Relationship to MVP

| Dimension | MVP (v0.1) | MLP (v0.2) |
| --- | --- | --- |
| Skills land | One verified example each | Multiple examples across branches |
| Branches populated | All ten non-empty | Key branches have depth |
| Problems covered | One (consciousness) | Three (consciousness, free will, induction) |
| Thinkers | Four | Ten+ |
| Works | Zero | Five+ |
| Schools | Zero | Three+ |
| External validation | Maintainer only | At least one external user |
| Coverage ledger | Created | Updated, beating Wikipedia in one branch |

## Ship checklist (the moment v0.2 goes out)

1. All MVP items still pass.
2. Three exemplar problems complete.
3. Works, schools, thinkers branches meet the bar above.
4. Persuasion and biases each have ten+ pages.
5. Coverage ledger updated; one branch beats Wikipedia.
6. At least one external user has tested the install.
7. Contributing guide tested by an external contributor.
8. Tag `v0.2`; announce with changelog.
