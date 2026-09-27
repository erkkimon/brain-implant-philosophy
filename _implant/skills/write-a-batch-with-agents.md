---
type: skill
title: Write a batch of pages with parallel agents
description: "Use when adding several knowledge pages at once (a batch of 3–5 from plans/next-steps.md) by delegating one page per sub-agent. Gives the brief every sub-agent receives — nothing from memory, raw excerpt file format, the page rules — and the integration and review pass the coordinating agent runs before committing: index entries, inbound links, unsourced characterisations, arithmetic, bookkeeping."
timestamp: 2026-09-27T13:17:25Z
depends_on: [write-a-page.md]
tools:
  - skills/tools/neutrality-lint.py
  - skills/tools/logic.py
---

# Write a batch of pages with parallel agents

The batch form of [Write a page](write-a-page.md), first used for paradoxes
batch 1 ([journal 2026-09-27](../journals/2026-09-27.md)). The order of
batches is in [Next steps](../plans/next-steps.md). One sub-agent writes one
page and its raw excerpts; the coordinating agent integrates, reviews and
commits. Sub-agents never run git and never edit shared pages, so parallel
work cannot collide.

## 1. Prepare (coordinator)

- Pick the batch from [Next steps](../plans/next-steps.md) §2.
- For each page choose: the file slug, the title, the main source (usually
  a Stanford Encyclopedia entry, Fall 2024 archive:
  `https://plato.stanford.edu/archives/fall2024/entries/<slug>/`), its
  authors and revision date (from the entry's copyright line and pubinfo),
  and a *focus* paragraph: which primary texts and locators to seek, which
  responses and their owners to cover, which neighbouring topics to leave
  to a later batch.
- Optionally pre-fetch the entries into `_temp/` so agents share them.

## 2. The brief each sub-agent receives

Give every agent the whole of this section plus its page parameters.

**Nothing from memory.** Every quotation must have been read by the agent
in the source's actual text (fetched HTML, a PDF through a text extractor,
a scan). A source that cannot be fetched is cited only with bibliographic
data verified by DOI content negotiation
(`curl -sL -H "Accept: application/vnd.citationstyles.csl+json" https://doi.org/<DOI>`)
or the Crossref API, and the page says what it says only as a secondary
source reports it. Open sources that work: the SEP archive, Project
Gutenberg, Perseus, the Internet Classics Archive, Wikisource, archive.org
scans, arXiv, PubMed Central, author pages, the Internet Archive for pages
that block bots. Publisher pages that return 403 are not fought.

**Raw excerpt files** go in `_implant/raw/`, kebab-case
`<author>-<year>-<topic>.md` (SEP: `sep-<slug>-fall-2024-<topic>.md`), in
this form, and are listed in `raw/index.md` with a one-line bullet
(appended, re-reading the index immediately before the edit):

```
# <Author Year> — <what the excerpt is about>

Source: <full reference, with pages/section>
Original: <DOI or stable URL or canonical locator + edition>
  (copyrighted; excerpts only | public domain | CC BY ...)
Retrieved: <date> (<how verified>)

> "<verbatim quotation, minimum needed>"  (<locator>)

Relied on for: <which claims a page makes from this>
Context: <what surrounds the quotation, so a reader can judge fairness>
```

Excerpts only, never whole works ([Raw holds excerpts, not copies](../conventions/raw-holds-excerpts-not-copies.md));
translations are separately copyrighted, so public-domain originals are
quoted in public-domain translations with the translator named.

**The page** follows the branch template in its `index.md` exactly, every
heading in order, 80–200 lines, frontmatter `type`, `about`, `title`,
quoted `description`, `tags`, `timestamp`. Every quotation on the page is
copied from a raw file. Every position and response names its owner with
year and locator; positions are not ranked; where the encyclopedia author
assesses, the page says it is that author's assessment ("Huggett (SEP 2024,
§3.1) judges …"), including when the author reports their own solution.
The implant's own additions are marked as structural notes (manifest
[G4](../vision/manifest.md)) or as logic/arithmetic shown step by step;
propositional cores are checked with `logic.py` and its output quoted.
Grounding links: [Reporting, not endorsing](../conventions/reporting-not-endorsing.md),
[How claims are graded](../conventions/how-claims-are-graded.md), the
branch index, the relevant vocabulary page; links only to pages that exist
or are siblings in the batch. The lint runs clean on the page
(`python3 _implant/skills/tools/neutrality-lint.py <page>`; a quotation
containing a flagged word stays on one physical line).

**Scope.** The agent edits only its page, its raw files and the append to
`raw/index.md`; no git, no compile; scratch in `_temp/`, removed at the end.
Its final message lists files written, which quotations were read where,
what was only bibliographically verified, what was left out and why, an
index line for the branch index and where the page should be linked from.

## 3. Integrate and review (coordinator)

1. Add each page to its branch `index.md` with the agent's index line;
   add inbound links where the agents suggested (vocabulary page, related
   problem pages), so nothing is orphaned.
2. **Read every page for what the lint cannot see**: characterisations of
   an author with no source ("X writes as a proponent of …"), selection
   that leaves out a response the source records, arithmetic, and
   sentences in the implant's voice that are neither logic nor a marked
   structural note. Fix, and record the fix in the journal.
3. Remove sibling links to pages that did not land.
4. Bookkeeping per [Next steps](../plans/next-steps.md) §3: journal entry
   with the agents' findings (source-versus-popular-story gaps are
   findings), todo ticked and archived, next-steps §1 counts and §2 status,
   a note in [the coverage ledger](../todo/coverage.md).
5. Timestamps, lint, self-test, compile, commit, push.
