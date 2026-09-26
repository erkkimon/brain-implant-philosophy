---
type: convention
about: concept
title: Raw holds excerpts, not copies
description: What may be stored under raw/ — only the minimum excerpt needed to support a citation with enough context to check it, always beside a canonical locator or link to the original where the full text can be fetched; never a wholesale copy of a copyrighted work or translation, because this repository is public and redistributing source material is a legal exposure the implant does not need.
tags: [convention, raw, copyright, legal, sources, public, translations]
timestamp: 2026-09-26T09:54:50Z
half_life: 0
---

# Raw holds excerpts, not copies

Decided by erkkimon on 2026-09-25, founding the philosophy implant
([journal](../journals/archive/2026/09/2026-09-25.md)); it follows from the manifest's
ninth given, that the repository is public from its first commit (manifest
[G9](../vision/manifest.md)).

`raw/` is where source material grounds the distilled layers. The
temptation is to drop whole articles, whole translations, whole chapters
of a critical edition into it so that a future reader has everything to
hand. For this repository that is a mistake, for a plain legal reason:
[this repository is public](written-to-be-public.md), and redistributing a
copyrighted article, translation, chapter or edition is not something a
public repository should do. The implant does not own that right, and it
does not need it.

What the implant actually needs from a source is narrower than the source
itself. It needs **enough of the source to support the specific claim, with
enough surrounding context to check that the claim is fair**, and it needs a
**pointer back to the original** so anyone who wants the rest can fetch it
from the party who is entitled to distribute it. That is what `raw/` stores.
Nothing more.

## The rule

A file under `raw/` is admissible when **both** hold:

1. **It is an excerpt, not the whole work.** Only the passage(s), verse(s),
   table row(s) or quotation that a claim in this brain implant actually
   relies on, plus the immediate context needed to read them honestly — not
   the full article, not the full dialogue, not the full translation. If a
   file reproduces substantially all of a source, it is a copy and does not
   belong here.

2. **It carries a resolvable pointer to the original.** A canonical locator
   — Stephanus, Bekker, A/B or Akademie page, book–part–section, chapter
   and verse — together with the edition or translation actually quoted; a
   DOI; a stable URL to an archive edition; an ISBN with page numbers. An
   identifier that lets a reader retrieve the complete source from its
   rightful home, as [Every claim carries its receipt](every-claim-carries-its-receipt.md)
   requires of every citation. An excerpt without a way back to the
   original is an orphan: it cannot be checked and cannot be updated.

This is a copyright-and-context rule, not a fair-use legal opinion. When in
doubt, store **less** and point **harder**: a one-sentence quotation with a
locator beats three paragraphs without one, every time.

## Translations are separately copyrighted

The original of most of the canon is in the public domain; **its
translations are not.** Hume's own English is free; a 2013 translation of
the *Mūlamadhyamakakārikā* is the translator's and publisher's property,
and so is a modern English *Republic* or *Critique*. An excerpt from a
translation is therefore held to the same limit as an excerpt from a
journal article, and it names the translator and edition it was taken
from, both for the copyright and because the wording is the translator's
choice — a claim that turns on a word cites the source-language term
beside it. Where a public-domain translation exists (older translations of
Plato, Aristotle and Kant are out of copyright in most jurisdictions), it
may be quoted more freely, and the file says which translation it is.

## What this looks like in practice

A raw file that grounds a claim about a public-domain text reads roughly
like this:

```markdown
# Hume's fork — the opening of Enquiry section 4

Source: David Hume, An Enquiry concerning Human Understanding (1748),
  section 4, part 1, paragraph 1 (EHU 4.1; SBN 25).
Original: https://davidhume.org/texts/e/4  (public domain; Hume's own text,
  1777 edition)
Retrieved: 2026-09-25

> "All the objects of human reason or enquiry may naturally be divided into
>  two kinds, to wit, Relations of Ideas, and Matters of Fact."  (EHU 4.1)

Relied on for: the attributive claim that Hume divides the objects of
enquiry into relations of ideas and matters of fact.
Context: the paragraph goes on to give geometry, algebra and arithmetic as
relations of ideas; the excerpt is the division itself, not the argument
that follows about matters of fact.
```

And the *form* for a modern, copyrighted article — the bibliographic data
is real; the bracketed lines mark where a real file's excerpt goes and are
not a quotation:

```markdown
# Harman & Kulkarni on the problem of induction — the framing claim

Source: Gilbert Harman & Sanjeev R. Kulkarni (2006), "The Problem of
  Induction", Philosophy and Phenomenological Research 72(3), 559–575.
Original: https://doi.org/10.1111/j.1933-1592.2006.tb00583.x
  (copyrighted; excerpt only — one sentence, p. 559)
Retrieved: 2026-09-25

> [one sentence from the opening page, quoted verbatim]  (p. 559)

Relied on for: [the one attributive claim about the paper's framing that
the excerpt supports, stated in the page that cites it].
Context: the sentence states the paper's framing; the argument for it
occupies the following sections and is not reproduced.
```

The quotation is short, its purpose is stated, and the locator or DOI takes
a reader to the whole text. That is the shape every raw file should have —
the same shape for a verse of Nāgārjuna (chapter and verse, translator,
edition, page), a row from the PhilPapers 2020 survey (the question, the
figure, the paper's DOI), or an encyclopedia paragraph (the archive-edition
URL and the section number).

## What must never go in raw/

- A full PDF, HTML dump, or scanned chapter of a copyrighted work — and a
  copyrighted *translation* counts as a copyrighted work even when the
  original is centuries old.
- A complete survey dataset that its publishers distribute under their own
  terms — store the question and the figures used, and let the reader fetch
  the set from its home.
- Anything whose only pointer is "I found it somewhere" — no resolvable
  original means it cannot be checked and does not belong.

Public-domain and open-licensed material (Hume's own text, a CC-BY article)
*may* legally be copied in full, but the excerpt-plus-pointer habit is
still the right default: it keeps `raw/` small, greppable and
[orderly](../conventions/index.md) rather than a mirror of the open web.

## How this is enforced

Two layers, both described in the
[founding of this rule](../journals/archive/2026/09/2026-09-25.md):

- The standing [raw/ is orderly source material](../conventions/index.md)
  henxel keeps `raw/` named and indexed.
- A `make_sure_that` henxel shows each new or changed `raw/` file to the
  contract's judge and asks whether it is an excerpt-with-a-pointer rather
  than a wholesale copy. A judge is fallible, so it only warns unless it is
  confident — but it catches the plain case of a whole article or
  translation pasted in, which is exactly the case that creates the legal
  exposure. How such natural-language henxels work is documented by
  [henxels](https://github.com/benquemax/henxels) itself.
