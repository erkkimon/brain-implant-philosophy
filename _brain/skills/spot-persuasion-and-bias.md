---
type: skill
title: Spot persuasion and bias
description: "Use when asked to analyse a text, speech, argument or conversation for the persuasion techniques it uses and the cognitive biases it exploits or exhibits — and when you are about to say 'this is an appeal to emotion' from memory. Produces an annotated, neutral inventory in which every technique and bias is a link to its implant page carrying the receipts: who classifies it, under which theory, what the critique is. Systematic and cited, which a language model alone is not."
timestamp: 2026-09-25T18:30:00Z
depends_on: [using-the-brain-implant.md]
export: agent-skill
---

# Spot persuasion and bias

A large language model is already good at saying "this passage uses an
appeal to authority and exploits the availability heuristic". What it cannot
do alone is do it *systematically* — every technique in the passage, not the
three that came to mind — or *with receipts* — who says this is a technique,
under which theory it counts as a fallacy, and who disagrees. That is the
gap this implant fills ([journal](../journals/2026-09-25.md)). The output is
an inventory, not a verdict: the implant never says a technique is illegitimate,
only who classifies it so and who does not
([Reporting, not endorsing](../conventions/reporting-not-endorsing.md)).

## Steps

### 1. Fix the unit of analysis

Split the text into moves — a claim, a support offered for it, a framing, an
appeal, a question, a concession. Number them. A technique attaches to a
move, not to a paragraph; a bias attaches either to the *author's* reasoning
(exhibited) or to the *audience's* (exploited), and the inventory says
which.

### 2. Walk the persuasion branch, not your memory

Open [persuasion](../knowledge/persuasion/index.md) and go through its
families in order — emotional, authority, structural, framing, and the rest
the index lists — asking of *each* technique whether any numbered move
instances it. Use `brain_search` on the move's wording when a family is
large. Record a hit as: move number → technique page → the observable
marker from the page's *How to spot it* section that matched. A hit without
a marker from the page is a hunch; mark it as one.

### 3. Walk the biases branch the same way

Open [biases](../knowledge/biases/index.md). For each move, ask whether the
reasoning *exhibits* a bias (the author's inference has the shape the page
describes) or *exploits* one (the move works on the audience by it, as a
source on the page says). Record the page, the marker, and — from the page —
the evidence grade of the bias itself. An "exploits anchoring" annotation
carries the replication status of anchoring, because the reader should know
how solid the effect is before acting on the label.

### 4. Attach the classifications, all of them

For each technique found, pull from its page: who classifies it as a
fallacy and under what criterion; who classifies it as a legitimate scheme
and with which critical questions; the critique of each. The inventory
carries both. Where a technique is *only* classified one way in the
literature, say so — that is a finding — but do not fill the gap with your
own view.

### 5. Reconstruct the argument beside the inventory

Run [analyse-an-argument](analyse-an-argument.md) on the text's central
claim so that the reader sees the logical skeleton next to the persuasive
dressing. A text can be entirely made of techniques and still valid; it can
be plain and invalid. The two analyses answer different questions and are
reported separately.

### 6. Report

The report has three parts and no fourth:

1. **Inventory** — a table: move · technique/bias (linked) · marker ·
   exhibited/exploited · classifications (linked, attributed).
2. **Skeleton** — the reconstruction from step 5.
3. **Gaps** — moves you could not match to any page. These are either
   nothing, or a page the implant lacks; add the second kind to
   `todo/open.md`.

No overall verdict on the text — whether it is manipulative, honest, good
or bad. That is the user's judgement and their cortex's entry. If the user
asks for it, say that the inventory is the material and the judgement is
theirs, and offer [estimate-a-credence](index.md) from the cognitive-tools
implant if they want to weigh it.

## What never happens here

- A technique named without a link to its page. If there is no page, the
  annotation says "no page; candidate: …" and goes to the todo.
- "This is a fallacy" in your voice. Always: "classified as … by …".
- Skipping families because the first three hits felt sufficient.
