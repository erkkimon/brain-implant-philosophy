---
type: article
about: concept
title: "Next steps: where the work stands and how to resume it"
description: "The resume point for any agent or maintainer picking this implant up cold, without the chat that produced it: the current state (v0.1 tagged, counts per branch), the decided next steps in order (paradoxes, dilemmas, ethical problems, oxymoron examples, then MLP), the exact per-batch working routine with commands, and the rules that set direction and boundaries. Update it at the end of every working session."
tags: [plan, handoff, roadmap, resume, process]
timestamp: 2026-09-27T12:22:42Z
---

# Next steps: where the work stands and how to resume it

**Read this first when resuming.** It is kept current at the end of every
working session, so the work can continue after a gap of days or weeks
without the conversation that produced it. The episodic detail is in the
journals ([today's](../journals/2026-09-27.md); earlier days under
`journals/archive/`), the full queue is [todo/open.md](../todo/open.md), and
the release bars are the [MVP](mvp.md) and [MLP](mlp.md) plans. This page
does not duplicate them; it says which item comes next and how to do it.

Last updated: 2026-09-27.

## 1. Where things stand

- **v0.1 is tagged and pushed** (tag `v0.1`, 2026-09-26). Every item of the
  [MVP ship checklist](mvp.md) is closed ([archive of 2026-09-26](../todo/archive/2026-09-26.md)).
  No GitHub release page exists yet (the tag carries the release note);
  creating one from the tag is optional.
- **Pages per `knowledge/` branch** (2026-09-27): problems 6, positions 9,
  arguments 4, thinkers 4, works 5, schools 2, persuasion 3, biases 3,
  vocabulary 13, methods 3. `raw/` holds 75 excerpt files. Compiled: 100
  docs (this page included), 0 ghosts, 0 orphans.
- **Exemplar clusters:** consciousness / AI consciousness (the first), and
  paradoxes, dilemmas and ethics — [trolley problem](../knowledge/problems/trolley-problem.md),
  [moral dilemmas](../knowledge/problems/moral-dilemmas.md),
  [sorites](../knowledge/problems/sorites-paradox.md),
  [liar](../knowledge/problems/liar-paradox.md), with the vocabulary
  contracts [oxymoron](../knowledge/vocabulary/oxymoron.md),
  [paradox](../knowledge/vocabulary/paradox.md) and
  [dilemma](../knowledge/vocabulary/dilemma.md).
- **Known weaknesses, visible on the pages:** 13 older vocabulary/methods
  pages carry a "Citation status: unverified" notice (citations drafted from
  model memory, not yet checked against sources); the list is in
  [todo/open.md](../todo/open.md) under "Quality that survives scrutiny".
- **Sibling implant:** the cognitive-tools implant
  (`https://github.com/erkkimon/brain-implant-cognitive-tools`) holds the
  credence tools; it is the only other implant named in public pages.

## 2. What to do next, in order

The maintainer's standing priority (erkkimon, 2026-09-26, see the
[journal](../journals/archive/2026/09/2026-09-26.md)): **oxymorons, paradoxes,
dilemmas and ethical problems, as soon as possible.** The itemised lists are
in [todo/open.md](../todo/open.md), section "Priority breadth"; work them in
this order, one committed-and-pushed batch of 3–5 pages at a time:

1. **Paradoxes batch 1** — Zeno's paradoxes (Achilles, dichotomy, arrow),
   Russell's paradox, Curry's paradox, the surprise examination, Newcomb's
   problem. Sources: SEP Fall 2024 archive entries (`zeno-paradoxes`,
   `russell-paradox`, `curry-paradox`, `epistemic-paradoxes` for the surprise
   exam, `decision-causal` for Newcomb), plus primary texts by canonical
   locator (Aristotle, *Physics* VI.9, 239b; Russell's 1902 letter to Frege).
2. **Paradoxes batch 2** — preface and lottery, Moore's paradox, Fitch's
   knowability paradox, the Ship of Theseus, Meno's paradox (*Meno* 80d–e),
   the raven paradox, Simpson's paradox, the St Petersburg paradox.
3. **Dilemmas** — Euthyphro (*Euthyphro* 10a), the prisoner's dilemma,
   Buridan's ass, the Agrippan (Münchhausen) trilemma, the Epicurean
   trilemma / problem of evil, the Heinz dilemma, dirty hands, Williams's
   Jim and the Indians, the ticking bomb.
4. **Ethical problems** — abortion (Thomson's violinist), euthanasia, the
   moral status of animals, Singer's drowning child, the non-identity
   problem, the repugnant conclusion, moral luck, the experience machine,
   Kant's murderer at the door, punishment, just war, demandingness.
5. **Oxymorons** — one curated examples page (rhetorical sense, each example
   with literary source and locator), plus the "contradiction in terms"
   disputes reported as claims.
6. **Supporting pages as each batch needs them** — thinker pages (Foot,
   Thomson, Anscombe, Williams, Marcus, Eubulides, Zeno, Russell, Tarski,
   Priest, Williamson), argument pages (double-effect conditions, the two
   consistency arguments against moral dilemmas).
7. **Coverage recount** against Wikipedia's "List of paradoxes" and the
   ethics lists, revision-pinned, in [todo/coverage.md](../todo/coverage.md).
8. **2020 PhilPapers figures** for the trolley problem (the results site
   returned a bot challenge on 2026-09-26; try again or use Bourget &
   Chalmers 2023, *Philosophers' Imprint*).

After that, the [MLP plan](mlp.md) (target v0.2): free will and induction
clusters, verifying the 13 unverified-citation pages, more thinkers, works
and schools, external review. The sequence there is in
[todo/open.md](../todo/open.md), "Post-MVP → MLP".

## 3. The working routine for one batch

Follow [Write a page](../skills/write-a-page.md) for every page. In short,
from the repository root:

1. **Start:** `git pull --ff-only`, then `brainpick compile --root .`. If a
   new UTC day has begun, move the previous day's `_implant/journals/YYYY-MM-DD.md`
   to `_implant/journals/archive/YYYY/MM/` and repoint links to it (the
   contract blocks a commit with two unarchived days).
2. **Sources first:** fetch the SEP entry from the Fall 2024 archive
   (`https://plato.stanford.edu/archives/fall2024/entries/<slug>/`) into
   `_temp/` (gitignored scratch), then save only the quoted excerpts, with
   URL, revision date and retrieval date, as a kebab-case file in
   `_implant/raw/`, listed in `_implant/raw/index.md`. Check DOIs and page
   ranges on Crossref (`https://api.crossref.org/works?query.bibliographic=...`)
   when two sources disagree.
3. **Write** with the branch template from its `index.md` (problem pages:
   The question / Why it matters / Positions taken / Arguments in play /
   Thinkers who addressed it / Framings and reframings / Vocabulary). Every
   quotation must be verbatim from the raw excerpt; every position carries
   its named proponent; nothing is ranked. Check any propositional argument
   with `python3 _implant/skills/tools/logic.py check --premises "..."
   --conclusion "..."` and report the tool's output, not a verdict.
4. **Link in:** add the page to its branch `index.md` and give it at least
   one inbound link from a related page (no orphans).
5. **Bookkeeping:** today's journal entry (newest first, what was done and
   decided, linking the pages); tick finished items in `todo/open.md` as
   `- [x] … (done: YYYY-MM-DD)` and move them to `todo/archive/YYYY-MM-DD.md`;
   update the counts in section 1 of this page and its "Last updated" line.
6. **Timestamps:** set `timestamp:` in every changed doc to the real
   `date -u +%Y-%m-%dT%H:%M:%SZ`.
7. **Check:** `python3 _implant/skills/tools/neutrality-lint.py _implant/knowledge _implant/skills _implant/conventions _implant/vision`
   (0 findings; keep any quotation containing a flagged word on one line),
   `python3 _implant/skills/tools/selftest.py` (all OK), and
   `brainpick compile --root .` (0 ghosts, 0 orphans; slow, allow minutes).
8. **Commit and push:** remove `__pycache__` directories, `git add -A`,
   `henxels bless push`, `git commit -m "..."` (the hooks rerun the
   contract), `henxels bless push`, `git push`. Deleting files additionally
   needs `henxels bless delete`. The maintainer has authorised agents to
   commit and push freely here, overriding the generated AGENTS.md etiquette
   line ([journal 2026-09-27](../journals/2026-09-27.md)).
9. **Clean up:** empty `_temp/` of scratch (keep `page-brief.md` and
   `subagent-brief.md`), stop background jobs, leave `git status` clean.

## 4. Direction and boundaries (do not drift)

- **Benchmark:** beat Wikipedia on neutrality, amount and quality
  ([manifest](../vision/manifest.md)).
- **No opinions, no verdicts:** anything that is not pure logic or
  mathematics is attributed to someone who said it, with a reference
  ([Reporting, not endorsing](../conventions/reporting-not-endorsing.md),
  [Every claim carries its receipt](../conventions/every-claim-carries-its-receipt.md)).
  Selection is neutral too ([Selection is a stated rule](../conventions/selection-is-a-stated-rule.md)).
- **Surveys report opinion, not truth,** and are labelled with year and
  population.
- **Public repository:** no host names, internal paths or personal details
  ([Written to be public](../conventions/written-to-be-public.md)); the
  only sibling implant named publicly is cognitive-tools.
- **Vocabulary:** this repository is an implant, never "a brain"; its root
  is `_implant/` ([An implant is not a brain](../conventions/an-implant-is-not-a-brain.md)).
- **Licensing:** content CC BY-SA 4.0, tooling MIT; decisions attributed to
  erkkimon.
