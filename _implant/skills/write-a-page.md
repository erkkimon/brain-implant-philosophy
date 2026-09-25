---
type: skill
title: Write a page
description: "Use before adding or substantially changing any page under knowledge/ — a problem, position, argument, thinker, work, school, persuasion technique, bias, vocabulary term or method. The one authoring procedure: check the admission rule, take the branch's template, type every sentence against the six claim kinds, cite primary sources by canonical locator, verify that every receipt resolves, run the neutrality lint, run the ideological Turing test on any case-for/case-against, link the page into the graph, and record the coverage count."
timestamp: 2026-09-25T18:30:00Z
depends_on: [using-the-brain-implant.md, steelman-a-position.md, analyse-an-argument.md]
tools:
  - skills/tools/neutrality-lint.py
  - skills/tools/logic.py
export: agent-skill
---

# Write a page

Every knowledge page is written the same way, whatever branch it is in. The
procedure exists so that a contributor — human or agent, large model or
small — who never read the founding conversation still produces a page the
[manifest](../vision/manifest.md) can vouch for.

## Steps

### 1. Admission

Does the subject have a named proponent or source in a citable published
place? ([Selection is a stated rule](../conventions/selection-is-a-stated-rule.md)).
If yes, note the source; it will be the first citation. If no, stop, and
record the search in today's journal so nobody repeats it.

Check `brain_search` for an existing page under another name. One concept,
one page; a near-duplicate is merged, not added.

### 2. Template

Take the template from the branch's index —
[problems](../knowledge/problems/index.md), [positions](../knowledge/positions/index.md),
[arguments](../knowledge/arguments/index.md), [thinkers](../knowledge/thinkers/index.md),
[works](../knowledge/works/index.md), [schools](../knowledge/schools/index.md),
[persuasion](../knowledge/persuasion/index.md), [biases](../knowledge/biases/index.md),
[vocabulary](../knowledge/vocabulary/index.md), [methods](../knowledge/methods/index.md)
— and keep every section heading, in order. A section with nothing citable
yet says "(none recorded)" rather than being dropped: an empty section is a
visible gap; a missing one is an invisible one.

### 3. Sources first

Collect the sources before writing a sentence: primary texts with canonical
locators, the standard scholarly treatments, the Stanford Encyclopedia entry
cited by its archive edition, surveys, and for empirical claims the study
plus its replications. Store any excerpt you will quote in `raw/` under the
excerpt rule ([Raw holds excerpts, not copies](../conventions/raw-holds-excerpts-not-copies.md)).

### 4. Write, typing each sentence

For every sentence, ask which of the six kinds it is
([How claims are graded](../conventions/how-claims-are-graded.md)) and give
it what that kind needs: locator, scholar, source, grade and record, shown
steps, or an owner. A sentence that is none of the six is an opinion and
does not go in ([manifest](../vision/manifest.md), G4). Use the vocabulary's
normative senses; mark any departure
([Words are contracts](../conventions/words-are-contracts.md)).

For a position page, write the case-for and case-against with
[steelman-a-position](steelman-a-position.md). For an argument page,
reconstruct with [analyse-an-argument](analyse-an-argument.md) and paste the
tool's validity output.

### 5. Verify every receipt

Each DOI resolves (`curl -sIL https://doi.org/<doi>` returns 200); each
URL is pinned (SEP archive edition, not the live page; a Wayback snapshot
for anything else that could change); each locator has been checked
against an edition you name. A citation you did not check is not a receipt
([Every claim carries its receipt](../conventions/every-claim-carries-its-receipt.md)).

### 6. Lint

```bash
python3 _implant/skills/tools/neutrality-lint.py _implant/knowledge/<branch>/<page>.md
```

Every hit is a verdict word without an owner. Attribute it, quote it, or
delete it. `# lint: allow` at the end of a line is permitted only with a
reason in the same line, and it is what a reviewer looks at first.

### 7. Link into the graph

Every page links out — to its problem, positions, arguments, thinkers,
works, terms — and every page it names links back. Add the page to the
branch index's list. A page nobody links to is a page the graph cannot
find; `brainpick compile` reports orphans and ghosts, and the count should
not go up.

### 8. Frontmatter and bookkeeping

`type: article`, the branch's `about`, title, quoted description, tags
starting with the branch name, a real ISO timestamp. Update the coverage
ledger in `todo/coverage.md` if the branch tracks one. Journal what was
added in one line that points at the page.

## Review checklist

A reviewer — or the author, once more, as a stranger — checks:

- [ ] admitted by the rule, with the source named
- [ ] every section of the template present
- [ ] every sentence one of the six kinds, with what it needs
- [ ] every receipt verified to resolve
- [ ] lint clean, or each `allow` justified
- [ ] case-for and case-against each pass the ideological Turing test
- [ ] linked in and out; branch index updated
- [ ] no personal data, no infrastructure ([Written to be public](../conventions/written-to-be-public.md))
