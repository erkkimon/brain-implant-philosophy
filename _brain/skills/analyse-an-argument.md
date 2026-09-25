---
type: skill
title: Analyse an argument
description: "Use when a text, a user, or another skill presents an argument and the question is what it actually claims and whether the inference holds — before saying 'that doesn't follow' from intuition. Reconstructs the argument into numbered premises and a conclusion, classifies its form, checks propositional validity with the logic tool instead of by eye, separates validity (checkable) from soundness (someone's verdict), and maps the reconstruction onto the implant's argument pages so the objections to each premise arrive with their citations."
timestamp: 2026-09-25T18:30:00Z
depends_on: [using-the-brain-implant.md]
tools:
  - skills/tools/logic.py
  - skills/tools/selftest.py
export: agent-skill
---

# Analyse an argument

Reconstruction is the one kind of analysis this implant performs in its own
voice, because a reader can check it without trusting anyone
([manifest](../vision/manifest.md), G1–G2; [How claims are graded](../conventions/how-claims-are-graded.md),
*logical*). Everything past reconstruction — is the premise true, is the
argument good — is somebody's verdict and is reported as such.

## Steps

### 1. Find the conclusion, then the premises

Write the conclusion as one declarative sentence. Then list, as numbered
premises, only what the text actually offers in its support — quoted or
closely paraphrased, with locator if the text is a work in
[works](../knowledge/works/index.md). Do not add a premise the text does not
state; if the inference needs one, add it *marked* as a suppressed premise
(`P3*`) — that mark is often the whole finding.

### 2. Fix the terms

For each term that does work in the argument, say which sense it is being
used in, against the [vocabulary](../knowledge/vocabulary/index.md). An
argument whose key term shifts sense between premises is noted here, by
premise and sense, as a logical observation — not as "equivocation", which
is a classification that has owners
([Reporting, not endorsing](../conventions/reporting-not-endorsing.md)).

### 3. Classify the form

Deductive, inductive, abductive, or analogical — by what the text claims
for the inference, not by what you think it should claim. If deductive and
expressible in propositional logic, go to step 4. If it needs quantifiers,
modality, or an informal scheme, say which and whose reconstruction you are
following; validity is then reported as "valid under reconstruction R
(cite)" rather than tool-checked.

### 4. Check validity with the tool — never by eye

```bash
python3 _brain/skills/tools/logic.py check --premises "P -> Q" "P" --conclusion "Q"
```

or save the argument as JSON and run `logic.py check argument.json`. The
tool enumerates the truth table and reports VALID or the counterexample
rows; it also names the schema when the argument matches one, flags
inconsistent premises, a tautological conclusion, and premises that are not
needed. A counterexample row is the most useful output: it says exactly
which assignment the argument cannot rule out. Paste the tool's output; do
not summarise it into "seems valid".

### 5. Separate validity from soundness

Validity is now a logical claim with a receipt (the tool's output).
Soundness needs every premise to be *true*, and that is a verdict. For each
premise, report — from the argument's page in
[arguments](../knowledge/arguments/index.md) if one exists — who accepts it,
who disputes it, and on what grounds, cited. If no page exists, the
reconstruction plus a note "no page; candidate" goes to `todo/open.md`.

### 6. Map to the graph

Say which [problem](../knowledge/problems/index.md) the argument bears on
and which [position](../knowledge/positions/index.md) it supports or
attacks. If the argument is a known one under another name, link the page
and note the variant.

### 7. Report

1. The reconstruction (premises, suppressed premises marked, conclusion).
2. Terms and senses.
3. Form, and the tool output verbatim.
4. Per premise: who disputes it and why, cited.
5. Graph position.

No line saying whether the argument is good. If asked, point to part 4 and
say the verdict is the reader's; offer the debate skill if they want it
stress-tested.
