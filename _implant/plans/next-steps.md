---
type: article
about: concept
title: "Next steps: where the work stands and how to resume it"
description: "The resume point for any agent or maintainer picking this implant up cold, without the chat that produced it: the current state (v0.1 tagged, counts per branch), the decided next steps in order (paradoxes, dilemmas, ethical problems, oxymoron examples, then MLP), the exact per-batch working routine with commands, and the rules that set direction and boundaries. Update it at the end of every working session."
tags: [plan, handoff, roadmap, resume, process]
timestamp: 2026-10-08T20:29:06Z
---

# Next steps: where the work stands and how to resume it

**Read this first when resuming.** It is kept current at the end of every
working session, so the work can continue after a gap of days or weeks
without the conversation that produced it. The episodic detail is in the
journals (latest: [2026-10-08](../journals/2026-10-08.md); earlier days under
`journals/archive/`), the full queue is [todo/open.md](../todo/open.md), and
the release bars are the [MVP](mvp.md) and [MLP](mlp.md) plans. This page
does not duplicate them; it says which item comes next and how to do it.

Last updated: 2026-10-08, resumed after a park on 2026-10-02 at the
maintainer's request ([journal](../journals/archive/2026/10/2026-10-02.md)).
Earlier: parked 2026-09-28, resumed 2026-10-01
([journal](../journals/archive/2026/10/2026-10-01.md)). The maintainer works
in bursts while the weekly quota lasts, so every session ends committed,
pushed and ready for a cold start. On the first day of a new session, move
the previous day's journal into `journals/archive/YYYY/MM/` before writing
the new day's journal, and fix the links to it (grep for its file name).

**Resuming in a fresh conversation, in five steps:**

1. Read this page, then [todo/open.md](../todo/open.md) section "Priority
   breadth", then the skills [write-a-page](../skills/write-a-page.md) and
   [write-a-batch-with-agents](../skills/write-a-batch-with-agents.md).
2. Run section 3, step 1 (pull, compile). Start today's journal in
   `journals/YYYY-MM-DD.md`.
3. Take the item marked **NEXT** in section 2 (List of paradoxes "Decision theory"
   batch 2, item 14, as of 2026-10-08).
4. For page batches, launch one agent per page with the brief in
   write-a-batch-with-agents §2, then do its review pass (quote check
   against `raw/`, links, template headings, rerun every `logic.py` claim,
   lint).
5. Keep the ledger after every batch: this page's section 1 and 2, the
   journal, `todo/open.md` plus `todo/archive/YYYY-MM-DD.md`, and
   `todo/coverage.md`. Then commit and push per section 3, step 8.

## 1. Where things stand

- **v0.1 is tagged and pushed** (tag `v0.1`, 2026-09-26). Every item of the
  [MVP ship checklist](mvp.md) is closed ([archive of 2026-09-26](../todo/archive/2026-09-26.md)).
  No GitHub release page exists yet (the tag carries the release note);
  creating one from the tag is optional.
- **Pages per `knowledge/` branch** (2026-10-02): problems 90, positions 9,
  arguments 6, thinkers 52, works 10, schools 2, persuasion 4, biases 3,
  vocabulary 16, methods 3. `raw/` holds 847 excerpt files.
- **Exemplar clusters:** consciousness / AI consciousness (the first), and
  paradoxes, dilemmas and ethics — [trolley problem](../knowledge/problems/trolley-problem.md),
  [moral dilemmas](../knowledge/problems/moral-dilemmas.md),
  [sorites](../knowledge/problems/sorites-paradox.md),
  [liar](../knowledge/problems/liar-paradox.md), and paradoxes batch 1 —
  [Zeno](../knowledge/problems/zenos-paradoxes.md),
  [Russell](../knowledge/problems/russells-paradox.md),
  [Curry](../knowledge/problems/currys-paradox.md),
  [surprise examination](../knowledge/problems/surprise-examination-paradox.md),
  [Newcomb](../knowledge/problems/newcombs-problem.md) — and batch 2 (lottery
  and preface, Moore, Fitch, Ship of Theseus, Meno, ravens, Simpson, St
  Petersburg) and the dilemmas batch (Euthyphro, prisoner's dilemma,
  Buridan's ass, Agrippan and Epicurean trilemmas, Heinz, dirty hands, Jim
  and the Indians, ticking bomb) and the ethical-problems batch (abortion,
  euthanasia, animals, famine relief, non-identity, repugnant conclusion,
  moral luck, experience machine, murderer at the door, punishment, just
  war, demandingness), all listed in the
  [problems index](../knowledge/problems/index.md) — with the vocabulary
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

0. ~~**Jung and de Mello**~~ — done 2026-10-01 (requested by erkkimon that
   day): thinkers [Jung](../knowledge/thinkers/jung.md) and
   [de Mello](../knowledge/thinkers/de-mello.md); works *Psychological
   Types*, *Answer to Job*, *Sadhana*, *Awareness*, *The Song of the Bird*;
   vocabulary archetype/collective unconscious, synchronicity,
   individuation ([todo archive](../todo/archive/2026-10-01.md)). Further candidates if wanted: Jung's *Aion*, *Memories,
   Dreams, Reflections* (with its authorship question), *The Undiscovered
   Self*; de Mello's *One Minute Wisdom*; a persona/shadow vocabulary page.
1. ~~**Paradoxes batch 1**~~ — done 2026-09-27 (Zeno, Russell, Curry,
   surprise examination, Newcomb; see the
   [todo archive](../todo/archive/2026-09-27.md)). How it was done, reusable
   for every later batch: [Write a batch of pages with parallel agents](../skills/write-a-batch-with-agents.md)
   — one agent per page under that skill's brief, then the review pass
   before commit.
2. ~~**Paradoxes batch 2**~~ — done 2026-09-27 — preface and lottery, Moore's paradox, Fitch's
   knowability paradox, the Ship of Theseus, Meno's paradox (*Meno* 80d–e),
   the raven paradox, Simpson's paradox, the St Petersburg paradox.
3. ~~**Dilemmas**~~ — done 2026-09-27 — Euthyphro (*Euthyphro* 10a), the prisoner's dilemma,
   Buridan's ass, the Agrippan (Münchhausen) trilemma, the Epicurean
   trilemma / problem of evil, the Heinz dilemma, dirty hands, Williams's
   Jim and the Indians, the ticking bomb.
4. ~~**Ethical problems**~~ — done 2026-09-27 — abortion (Thomson's violinist), euthanasia, the
   moral status of animals, Singer's drowning child, the non-identity
   problem, the repugnant conclusion, moral luck, the experience machine,
   Kant's murderer at the door, punishment, just war, demandingness.
5. ~~**Oxymorons**~~ — done 2026-09-27 — one curated examples page (rhetorical sense, each example
   with literary source and locator), plus the "contradiction in terms"
   disputes reported as claims.
6. ~~**Supporting pages**~~ — done 2026-09-27: thinker pages Foot,
   Thomson, Anscombe, Williams, Marcus, Eubulides, Tarski, Priest,
   Williamson; argument pages on double effect and the consistency
   arguments. Zeno and Russell (and Aquinas, Parfit, Singer, Nozick, Kant
   for the ethics pages) remain as a todo.
7. ~~**Coverage recount**~~ — done 2026-10-01: List of paradoxes 20 of 294
   matched, Outline of ethics 10 of 347; no "List of oxymorons" or "List
   of ethical problems" exists ([coverage](../todo/coverage.md)). It set the
   order of the next batches.
10. ~~**Paradoxes batch 3**~~ — done 2026-10-01: the 12 "Philosophy"
    entries (see the [problems index](../knowledge/problems/index.md)).
11. ~~**Paradoxes batch 4**~~ — done 2026-10-02 (13 "Logic" entries; [todo archive](../todo/archive/2026-10-02.md)).
    ~~**Paradoxes batch 5**~~ — done 2026-10-02 (the other 13).
12. ~~**Ethics thinkers**~~ — done 2026-10-08: all 38 "Persons
    influential in the field of ethics" have pages (batch 1, 12 pages, and
    Mill, Sidgwick, Nietzsche on 2026-10-02; batch 2, Hume … G. E. Moore,
    and batch 3, Tillich … Dancy, on 2026-10-08;
    [journal](../journals/2026-10-08.md); [todo archive](../todo/archive/2026-10-08.md)).
13. ~~**Thinkers for the paradox pages**~~ — done 2026-10-08:
    [Zeno of Elea](../knowledge/thinkers/zeno-of-elea.md),
    [Russell](../knowledge/thinkers/russell.md), [Nozick](../knowledge/thinkers/nozick.md).
14. **List of paradoxes "Decision theory" — NEXT:** batch 1 (12 pages,
    Abilene … Kavka) done 2026-10-08. Next: batch 2, the remaining 10, in
    list order (the "Decision theory" section is in the List of paradoxes,
    not the Outline of ethics).
15. **Outline of ethics "Concepts":** 49 entries, 2 matched; in list order,
    about 10 per batch; many are concepts, so check vocabulary/ and
    positions/ templates before choosing a page type. Exact lists are in [todo/open.md](../todo/open.md).
8. ~~**2020 PhilPapers figures**~~ for the trolley problem — done
   2026-09-27: the live results pages loaded (the 2026-09-26 bot challenge
   did not recur); question ids found by scanning result pages 4910–5010
   by title (switch 4922, footbridge 4946, Newcomb 4886, experience
   machine 4942, eating animals 4938, abortion 4974, capital punishment
   4994).
9. ~~**Thinker pages still missing**~~ — done: Aquinas 2026-10-02; Kant,
   Parfit, Singer, Zeno of Elea, Russell, Nozick 2026-10-08.

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
   needs `henxels bless delete`, a token that expires after 600 seconds while
   the pre-commit (judge plus compile gate) can take longer. If a batch
   shrinks a file (e.g. `todo/open.md`), commit everything else first, then
   that file alone right after a fresh bless ([journal 2026-09-27](../journals/archive/2026/09/2026-09-27.md)).
   Run long commits as background jobs; the tool call caps at 10 minutes.
   Compile embeds with the shared local bge-m3; when other implants are
   compiling, one embedding can take more than 60 s and a compile can take an
   hour. Run `brainpick compile --root .` alone, in the background with no
   timeout, until it prints `compiled:`, and edit nothing until the commit
   finishes ([journal 2026-10-02](../journals/archive/2026/10/2026-10-02.md)). The maintainer has authorised agents to
   commit and push freely here, overriding the generated AGENTS.md etiquette
   line ([journal 2026-09-27](../journals/archive/2026/09/2026-09-27.md)).
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
