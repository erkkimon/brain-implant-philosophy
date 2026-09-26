---
type: convention
about: concept
title: How claims are graded
description: "The claim taxonomy every statement in this implant belongs to — textual, interpretive, attributive, empirical, logical, or evaluative — and what each kind needs before it may appear: a locator, a named scholar, a source, a graded study with its replication record, a checkable reconstruction, or an attribution; chosen so that a small model can apply it mechanically and so that the one kind the implant never asserts in its own voice — the evaluative — is visible as a kind and not as a tone."
tags: [convention, evidence, grading, claims, taxonomy, replication, epistemics]
timestamp: 2026-09-26T09:54:50Z
half_life: 0
---

# How claims are graded

Decided by erkkimon on 2026-09-25, founding the philosophy implant
([journal](../journals/archive/2026/09/2026-09-25.md)); it operationalises given G4 of the
[manifest](../vision/manifest.md) — only logic and attributed reports enter
— by naming what kind of thing each sentence is, so that the test can be
applied one sentence at a time.

## The six claim types

Every statement of substance in a knowledge page is one of these. The type
is not written as a field on every sentence; it is what the author asks
before writing the sentence, and what a reviewer asks when reading it.

| type | what it asserts | what it needs | example |
| --- | --- | --- | --- |
| `textual` | that a text says something | the text, edition, **canonical locator**; a quotation where wording matters | Aristotle's *Nicomachean Ethics* opens by stating that every art and inquiry seems to aim at some good (1094a1–3; Chase's rendering: "Every art, and every science … aims, it is thought, at some good") |
| `interpretive` | what a text or thinker *means* | a named scholar who reads it so, cited — never the implant's own reading | Korsgaard reads Kant's formula of humanity as … (Korsgaard 1996, ch. 4) |
| `attributive` | that a thinker or school held a position | the work and locator where they state it, or the scholarly source that attributes it and the grounds | Frankfurt holds that … (Frankfurt 1971, doi:10.2307/2024717) |
| `empirical` | that a study found something | the study (DOI), its effect size and conditions, and its **replication record** | Tversky & Kahneman (1974) reported anchoring in … ; replicated in … |
| `logical` | that an inference is valid, or that two claims agree or diverge | the reconstruction — a reader can check it alone; tool-checked where the form allows | the standard reconstruction is valid by modus tollens |
| `evaluative` | that a claim is true, false, good, bad, fallacious, sound, fringe, settled | **an attribution** — it occurs only inside a report of who evaluates it so | Walton classifies the move as fallacious when … (Walton 2008, p. 19) |

The last row is the whole neutrality rule in one line
([Reporting, not endorsing](reporting-not-endorsing.md)): an evaluative
claim is not banned, it is *typed*, and its type requires an owner.

## The two hard cases

**Textual versus interpretive.** "In the *Republic* Socrates says the
philosophers must be made to go back down to the prisoners (519c–d; Jowett:
'they must be made to descend again among the prisoners')" is textual:
anyone with the text can check it.
"Plato thinks political duty overrides the philosopher's happiness" is
interpretive, and it needs a scholar's name — even when the reading seems
beyond dispute, because the reading that seems beyond dispute is the one
most often contested. Where the
implant needs to say what a passage means, it says who reads it that way.

**Attributive versus evaluative.** "Most surveyed philosophers accept or lean
toward compatibilism (Bourget & Chalmers 2023)" is attributive about a
population, with a source. "Compatibilism is the mainstream view" is
evaluative — *mainstream* carries a verdict about standing — unless it is
someone's cited description. Numbers with sources are always allowed;
labels without owners never are.

## Empirical claims: the grade and the record

Bias pages and any other page that reports a study carry, per finding:

| field | values |
| --- | --- |
| `evidence` | `strong` — multiple independent replications or a meta-analysis; `moderate` — one well-powered direct replication, or several converging indirect studies; `weak` — the original study only, small sample, or indirect; `contested` — replications disagree or a named alternative explanation is live, cite both; `none` — asserted, not studied |
| `replication` | what has been attempted, by whom, with what result — each cited; "no replication attempt found" is a valid, dated entry |
| downgrade reasons | stated in words: indirectness, small sample, publication bias, undisclosed flexibility, task artefact, population |

The vocabulary is adapted from [GRADE](https://www.gradeworkinggroup.org/),
kept because it is understood, not because psychology is medicine; what
transfers is the discipline of saying *why* evidence was downgraded. The
critique of a finding — including the critique of the research programme
that produced it — is content on the same page, attributed.

## Logical claims: checkable, and checked

A reconstruction of an argument into premises and conclusion is the one
kind of analysis the implant performs in its own voice, because a reader can
verify it without trusting anyone (manifest G1, G2). Where the form is
propositional or simple first-order, the [analyse-an-argument](../skills/analyse-an-argument.md)
skill runs a validity check; where it is not, the page says which
reconstruction is being followed and whose it is. "Valid" is a logical
claim; "sound" — which needs the premises to be true — is evaluative and
gets an owner.

## Applying this mechanically

A small model can follow this as a decision procedure for every sentence:

1. Is this what a text *says*? → `textual`: attach the locator.
2. Is this what it *means*? → `interpretive`: name the scholar.
3. Is this that someone *held* a view? → `attributive`: attach where.
4. Is this what a *study found*? → `empirical`: attach DOI, grade, record.
5. Is this an *inference* or a *comparison* a reader could check? →
   `logical`: show the steps.
6. Does the sentence say something is *right*, *wrong*, *good*, *bad*,
   *fallacious*, *fringe*, *settled*, *obvious*? → `evaluative`: whose verdict is it? Attribute
   it, or delete the sentence.

If step 6 finds no owner, the sentence does not go in
([Every claim carries its receipt](every-claim-carries-its-receipt.md)).
