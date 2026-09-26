---
type: convention
about: concept
title: Reporting, not endorsing
description: "The neutrality rule that lets every position in philosophy share one repository: a page proves that a named thinker, school or text said something — a claim that is checkable and either true or false — and never asserts, in the implant's own voice, that what they said is correct, mistaken, fallacious, fringe or settled. Evaluative predicates occur only inside attributed reports, and a lint flags them anywhere else; every position page carries a case for and a case against that a proponent and an opponent would each accept as fair."
tags: [convention, neutrality, npov, reporting, steelman, lint]
timestamp: 2026-09-26T09:54:50Z
half_life: 0
---

# Reporting, not endorsing

Decided by erkkimon on 2026-09-25, founding the philosophy implant
([journal](../journals/archive/2026/09/2026-09-25.md)); it follows from givens G3 and G4 of
the [manifest](../vision/manifest.md): nobody — including us — knows what is
true on a contested question, and only logic or an attributed report may
enter the implant.

## The rule

**We claim that somebody said something. We prove that. We do not claim that
what they said is true — or false.**

"Hume argued that no ought can be derived from an is (*Treatise* 3.1.1, SBN
469–470)" is verifiable and either true or false. "Hume was right" is
neither; nor is "Hume's argument fails". Both are positions, and positions
belong to the reader's cortex, not the implant
([Using the brain implant](../skills/using-the-brain-implant.md)).

This is a *stronger* epistemic stance than advocacy, not a weaker one: every
sentence the implant asserts in its own voice can be checked by a stranger
with the cited text in hand.

## In practice

1. **Attribute, never assert.** The grammatical subject of a contested
   claim is the thinker, school or text — never the claim. Not "free will
   is compatible with determinism" but "compatibilists hold that free will
   is compatible with determinism (e.g. Frankfurt 1971, doi:10.2307/2024717)".
2. **Present the disagreement, not a winner.** A problem page lists the
   positions taken; a position page carries the case for and the case
   against; an argument page names who disputes which premise. Each stops
   there. The exact point of divergence — which premise, which sense of
   which term — is usually the most informative thing on the page, so it is
   stated precisely.
3. **Symmetric steelmanning.** The case-for on a position page is written so
   that a proponent would accept it as a fair statement of their best
   argument; the case-against so that an opponent would accept it likewise.
   Both are built from cited statements. The test is the one Caplan named the
   *ideological Turing test* ([Caplan 2011](https://www.econlib.org/archives/2011/06/the_ideological.html)):
   could a reader tell from the section which side the author holds? If
   yes, the section is not done.
4. **Criticism lands on the argument, in its author's words.** An objection
   is reported as *that critic's objection*, cited, close to their wording.
   Never as the implant's verdict.
5. **Proportion is reported, never enforced.** How many hold a view is data
   with a source (e.g. the PhilPapers survey, [Bourget & Chalmers 2023](https://doi.org/10.3998/phimp.2109)),
   stated on the page. It is never a reason to give a position less
   careful treatment or to leave it out
   ([Selection is a stated rule](selection-is-a-stated-rule.md)).
6. **No weasel neutrality.** "Some believe", "it is widely held", "critics
   say" hide who. Name them, cite them, date them
   ([Every claim carries its receipt](every-claim-carries-its-receipt.md)).
7. **The implant's own methods get the same treatment.** Bayesian updating
   is the method the cognitive-tools implant offers; the objections to it
   are documented in [methods](../knowledge/methods/index.md) with the same
   care as the case for it (manifest G7).

## The evaluative-predicate lint

Words that carry a verdict never appear in the implant's voice. The
authoring skills run a lint (`skills/tools/neutrality-lint.py`) over every
page; it flags, outside quotation marks and outside sentences whose subject
is an attributed source, at least these:

> fallacious, fallacy (as a classification), debunked, refuted, discredited,
> fringe, pseudo-, pseudoscience, crank, obviously, clearly, of course,
> rightly, wrongly, correctly, fails, succeeds, widely regarded, generally
> accepted, mainstream, notorious, infamous, so-called, controversial
> (unattributed), naive, sophisticated, compelling, unconvincing.

A flagged word is not forbidden — it is a prompt: *whose* verdict is this?
Attribute it and cite it, or delete it. "Walton classifies this as a
fallacy when the critical questions go unanswered (Walton 2008, p. 19)" is
fine; "this is a fallacy" is not.

## What this does not mean

It does not mean the implant has no standards. A claim still needs its
receipt, a misattributed quotation is an error to be fixed, a reconstruction
that is not valid is corrected, and a study's replication record is stated
plainly ([How claims are graded](how-claims-are-graded.md)). Neutrality
governs *what we assert*, not *how carefully we assert it* — and the care
is strict.

Nor does it mean false balance. A position held by one writer for a decade
and one held by a school for two millennia both get a page with the same
template; the page *says* which is which, with the numbers and their source.
Neutrality is achieved by reporting the proportion, not by hiding it and not
by pretending it is a verdict.
