---
type: convention
about: concept
title: Every claim carries its receipt
description: No statement enters this implant without a resolvable, verifiable citation attached to that specific statement — a canonical locator such as a Stephanus, Bekker or Akademie number, a DOI, a survey's published dataset, an encyclopedia entry pinned to its archive edition — because the value this implant adds over a model's own memory is not the claim but the source, and a claim whose source cannot be checked is indistinguishable from a fluent guess.
tags: [convention, grounding, citation, traceability, provenance, locators]
timestamp: 2026-09-25T18:30:00Z
half_life: 0
---

# Every claim carries its receipt

Decided by erkkimon on 2026-09-25, founding the philosophy implant
([journal](../journals/2026-09-25.md)). It is the second half of the
manifest's fourth given (manifest [G4](../vision/manifest.md)): the only
sentence this implant admits besides verifiable logic is *a report that
someone said something, at a location* — and the location is the receipt.

That given is this implant's entire economic case. A capable model already
"knows" that Plato compares the unenlightened to prisoners in a cave; it
cannot tell you that the image is at *Republic* 514a, which translation it
is paraphrasing, whether the wording it remembers is Plato's or a
commentator's, or what to read next. The claim is cheap. **The receipt is
the product.**

## The rule

**A claim and its citation are one unit.** A citation at the bottom of a
page, or a "sources" section listing six works for thirty claims, does not
satisfy this rule — a reader cannot tell which work backs which sentence,
so no sentence is checkable. The link goes at the claim, inline, in the
sentence that makes it.

### What counts as a receipt

In descending order of preference:

1. **A canonical locator into a primary text** — the scheme scholars of
   that text use so that a citation resolves in any edition and any
   translation: Plato, *Republic* 514a (Stephanus); Aristotle, *Nicomachean
   Ethics* 1094a1 (Bekker); Kant, *Critique of Pure Reason* A51/B75 (first
   and second edition pagination); Nāgārjuna, *Mūlamadhyamakakārikā* 24.18
   (chapter and verse); Hume, *Treatise* 1.4.6, SBN 252 (book, part,
   section, with the Selby-Bigge/Nidditch page). See
   [Locators, not page numbers](#locators-not-page-numbers) below.
2. **A DOI** — resolvable, permanent, and machine-verifiable by content
   negotiation against `doi.org`, which returns structured metadata for a
   DOI that exists and an error for one that does not. A DOI is the only
   citation form that can be *mechanically proven to exist* in one request.
   Gettier's "Is Justified True Belief Knowledge?" is
   [10.1093/analys/23.6.121](https://doi.org/10.1093/analys/23.6.121); a
   reader who doubts the attribution can resolve it in a second.
3. **A survey or dataset cited to the study that produced it** — a claim
   about what philosophers believe cites the PhilPapers 2020 survey
   (Bourget & Chalmers, "Philosophers on Philosophy: The 2020 PhilPapers
   Survey", *Philosophers' Imprint* 23,
   [10.3998/phimp.2109](https://doi.org/10.3998/phimp.2109)) with the
   question and the figure — not a blog post summarising it.
4. **A reference work pinned to a fixed edition** — the Stanford
   Encyclopedia of Philosophy is cited by its *archive* edition URL, never
   its living URL, because the living entry is revised in place:
   [Nāgārjuna, SEP Fall 2023 edition](https://plato.stanford.edu/archives/fall2023/entries/nagarjuna/),
   from the [SEP archives](https://plato.stanford.edu/archives/). The same
   holds for any page that changes: a Wikipedia `oldid` permalink, a dated
   revision, a specific edition and page of a book.
5. **A stable repository identifier** — a PhilPapers record, an arXiv id,
   a PhilArchive or OSF record, an ISBN with edition and page for a modern
   book that has no locator scheme.
6. **An explicit statement that there is no receipt** — see below.

### What does not count

- A bare URL to a news article, lecture summary or blog post reporting on a
  text or a study, when the text or the study itself is citable. Cite the
  primary; the report may be cited *additionally* if what is being claimed
  is that the report exists.
- A secondary source *for what a primary text says*. A handbook chapter is
  fine for the state of a debate; it is not the receipt for "Aristotle says
  every art aims at some good" — that is *Nicomachean Ethics* 1094a1, and
  the reader should be sent there.
- A translation, cited as if it were the original, for a claim that turns
  on wording. Where the claim depends on a word — *svabhāva*, *eudaimonia*,
  *Vorstellung* — the receipt names the translation used and the term in
  the source language.
- A model's own confidence. "It is well known that…", "philosophers
  generally agree…" — neither is a receipt.
- A link to another page of this implant, *as the sole grounding of a
  claim*. Internal links carry the argument; the chain has to terminate in
  an external source somewhere. A page whose only outbound links are
  internal has moved the problem, not solved it.

## Locators, not page numbers

Primary philosophical texts are cited by their **canonical locator scheme**
— Stephanus pages for Plato, Bekker numbers for Aristotle, A/B pagination
for the first *Critique* and Akademie volume and page for the rest of Kant,
book–part–section for Hume, chapter and verse for the *Mūlamadhyamakakārikā*
— because the locator resolves in any edition and any translation, in any
language, on any shelf. A page number belongs to one printing of one
edition; a reader with a different one cannot use it.

So a page number of a particular edition is given **in addition** to the
locator, never **instead** of it: "Hume, *Treatise* 1.4.6, SBN 252" tells a
reader with any edition where to look and tells a reader with the
Selby-Bigge/Nidditch edition which page. Where a text has no established
scheme — most twentieth-century and later books — the edition, ISBN and
page are the locator, and the edition is named so the number means
something.

## Six kinds of claim, one receipt each

A receipt proves that a claim was *reported faithfully*; what the claim is
*about* decides what the receipt has to be. Claims here are **textual**
(what a text says — the receipt is the locator), **interpretive** (what it
means — the receipt names the scholar whose reading it is), **attributive**
(X held Y — the receipt is where X said so, or where the attribution is
made), **empirical** (a study found — the receipt is the study, with its
grade and replication record), **logical** (an argument is valid or not —
checkable by the reader, so the receipt is the reconstruction itself), or
**evaluative** (a claim is good, weak, decisive — never in the implant's
voice, only inside an attributed report, where the receipt is the
assessor's). The taxonomy, and how each kind is graded, is detailed in
[How claims are graded](how-claims-are-graded.md).

## Uncited statements, when they are allowed

They are allowed, and they are marked. Two kinds:

- **A derivation** — a reconstruction of an argument into premises and
  conclusion, a validity check, a comparison of two attributed positions.
  It cites the texts the premises come from and states the steps, so that
  the reader checks the logic rather than trusts it (manifest
  [G1](../vision/manifest.md), [G4](../vision/manifest.md)).
- **An assumption** — a premise adopted to make a reconstruction possible,
  such as a reading of an ambiguous passage. It says *in words* that it is
  an assumption, and says whose. The contract's grounding rule accepts
  "this is an assumption" as valid grounding precisely so that assumptions
  are declared rather than disguised.

What is never allowed is the third kind: a confident sentence that is
neither of the above and has no source. That is the failure mode this whole
implant exists to prevent. (A *judgement* — the implant's own assessment
of a position — is not a third permitted kind here; it is the sentence
the manifest's G3 and G4 exclude, and it belongs to the reader's cortex.)

## Verification is mechanical, not aspirational

A citation nobody ever checks decays into decoration. So citations in this
implant are stored in a machine-readable record alongside the prose, and
they are re-verified: a DOI that stops resolving, an archive URL that
moved, a locator that points at a passage which does not say what was
claimed — these are findable by a script or a reader, and a broken receipt
is a defect in the page that carries it.

The contract already enforces that links *inside* the bundle land
(`links_resolve` in `henxels.yaml`; the reasoning is brainpick's
[grounding](https://github.com/benquemax/brainpick/blob/main/docs/grounding.md)
rule). External receipts need the same treatment, which is why they live in
a citation register rather than only in prose.

## Why the strictest possible reading

Because the alternative degrades silently. An implant with 95 % of its
claims sourced is not 95 % as good as one with 100 %: a reader who finds one
unsourced confident sentence must now treat *every* sentence as possibly
unsourced, and the receipts stop being load-bearing. Traceability is a
property of the whole corpus or it is not a property at all.

This is also why the rule survives [audience = public](written-to-be-public.md):
a receipt that only resolves for the maintainer is not a receipt. And it is
what [Evidence before authority](evidence-before-authority.md) relies on —
the argument can only outweigh the arguer if the argument can be read.
