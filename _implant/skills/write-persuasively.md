---
type: skill
title: Write persuasively
description: "Use when the user asks for text meant to move a reader — a pitch, an op-ed, a letter, a speech, a defence of a position. Before writing, presents the user with the persuasion techniques the implant catalogues and asks which are allowed, so that the persuasion is transparent and chosen; then writes with only those, annotates where each was used, and hands over a version the user can audit with spot-persuasion-and-bias."
timestamp: 2026-09-26T09:54:50Z
depends_on: [using-the-brain-implant.md, spot-persuasion-and-bias.md]
export: agent-skill
---

# Write persuasively

Every text persuades — laying down facts is persuasion too, and so is the
order they are laid in ([journal](../journals/archive/2026/09/2026-09-25.md)). The implant
takes no view on which techniques are legitimate
([Reporting, not endorsing](../conventions/reporting-not-endorsing.md)). The
user does, for their own text, and this skill exists to make that choice
explicit *before* the text is written rather than discovered in it
afterwards. Transparent persuasion is persuasion the author chose.

## Steps

### 1. Get the claim and the audience

Ask what the text is meant to make the reader believe or do, and who the
reader is. Write the claim as one sentence. If the user has not yet chosen
the position to defend, run [debate](debate.md) first to find the most
defensible one; do not write for a position the user has not chosen.

### 2. Present the menu

From [persuasion](../knowledge/persuasion/index.md), present the techniques
grouped by family, each on one line: name, what it does (from the page's
*Mechanism*), and a one-word note of how the literature classifies it —
*scheme* (treated as a legitimate argumentation scheme by a cited source),
*contested* (classified as a fallacy by some, legitimate by others), or
*fallacy-only* (every classification on the page is as a fallacy). Link
every line. Do not recommend; the note is the literature's, not yours.

Then ask the user to choose. Offer three shortcuts and say exactly what each
includes:

- **Logos only** — statement, evidence, reconstruction; nothing from the
  emotional or framing families.
- **Classical** — logos plus ethos and pathos as Aristotle's *Rhetoric*
  describes them (I.2, 1356a), i.e. credibility and emotion appealed to
  openly.
- **Everything** — every technique catalogued, including those every
  source classes as a fallacy.

Record the choice verbatim in the deliverable. The user may name techniques
individually or exclude some from a shortcut.

### 3. Write with only what was allowed

Draft the text. Each time a chosen technique is used, mark it inline with a
numbered footnote that names the technique and links its page. A technique
not on the allowed list may not appear; if the draft needs one, stop and
ask rather than slip it in.

### 4. Audit your own draft

Run [spot-persuasion-and-bias](spot-persuasion-and-bias.md) on the draft as
if it were someone else's. Every hit must be on the allowed list and have a
footnote. Anything else is removed or the user is asked. This step is what
makes the transparency real: the same procedure that finds techniques in
others' text finds them in yours.

### 5. Deliver two versions

- The **annotated** version, footnotes in place, with the allowed-list
  statement at the top.
- The **clean** version, footnotes stripped, for use.

Tell the user the annotated one is the audit trail: anyone they show it to
can see which levers were pulled.

## What never happens here

- A technique used that the user did not allow.
- A recommendation from you about which techniques are honest. The pages
  carry who says what; the user decides.
- Facts asserted in the text that the implant or the user cannot receipt.
  Persuasive is not the same as unsourced; a claim in the draft that is a
  fact still gets its citation ([Every claim carries its receipt](../conventions/every-claim-carries-its-receipt.md)).
