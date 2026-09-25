---
type: skill
title: Steelman a position
description: "Use when asked to give a position its strongest form — for a user who holds it, opposes it, or is choosing between it and others — and when writing or reviewing the case-for and case-against sections of a position page. Builds the case from cited proponents rather than from invention, applies the ideological Turing test (could a reader tell which side the author is on?) as the acceptance check, and does the same for the case against, so that both sides leave with a version they would sign."
timestamp: 2026-09-25T18:30:00Z
depends_on: [using-the-brain-implant.md, analyse-an-argument.md]
export: agent-skill
---

# Steelman a position

Symmetric steelmanning is the neutrality standard of every position page
([Reporting, not endorsing](../conventions/reporting-not-endorsing.md),
rule 3). The skill is the same whether it is run for a user or for a page:
build the best case from what proponents have actually said, then build the
best case against from what opponents have actually said, and check both
against the same test.

## Steps

### 1. State the thesis in the proponents' own terms

From the position page's *Thesis* and *Canonical statements* — or, if the
page does not exist yet, from the primary texts — write the claim as a
proponent would. Quote where a canonical statement exists, with locator.
Fix each term's sense against the [vocabulary](../knowledge/vocabulary/index.md);
a steelman in the wrong sense of a key term is a strawman with good manners.

### 2. Collect the arguments proponents give

From the page's *Case for* and the linked [argument](../knowledge/arguments/index.md)
pages, and from the proponents' texts: every distinct argument, each with
its source. Reconstruct the strongest one or two with
[analyse-an-argument](analyse-an-argument.md). Where proponents have
answered a standard objection, collect the reply and its source — a
steelman includes the replies.

### 3. Write the case for

In the proponents' vocabulary, in the order they give it, with the
citations inline. Do not add an argument no proponent has made; if you can
think of a better one, that is *your* argument, and it belongs in the
user's cortex, marked as such, not in the implant.

### 4. Apply the test

Caplan's *ideological Turing test*
([Caplan 2011](https://www.econlib.org/archives/2011/06/the_ideological.html)):
could a reader who holds the position tell, from the section alone, that
its author does not? Signs that a section does not pass: hedges the proponents would not
use ("proponents claim that…" where a proponent would just claim it), a
weaker version of a premise than the sources give, an objection
smuggled in as a concession, an argument the sources rank low placed
first. Fix each; the sources, not your sense of proportion, decide the
ranking.

### 5. Do the same for the case against

Steps 1–4 again, from the opponents' side: their objections in their words
with citations, the strongest first as *they* rank them, their replies to
the proponents' replies. The test is now: could an opponent tell the author
is not one?

### 6. Name the divergence

The two cases now sit side by side. Say — as a logical observation, cited to
both sides' texts — where exactly they part: which premise one side accepts
and the other rejects, or which sense of which term. This is the most
useful sentence on the page and it is not a verdict.

### 7. Deliver

For a user: both cases and the divergence, with the note that the choice is
theirs — offer [debate](debate.md) to test their pick, or
[estimate-a-credence](index.md) from the cognitive-tools implant to weigh
it. For a page: the sections, ready for the evaluative-predicate lint
(`skills/tools/neutrality-lint.py`).

## What never happens here

- An argument for or against that no cited source has made.
- A case-for that a proponent would call a caricature, or a case-against an
  opponent would.
- A sentence saying which case is stronger.
