---
type: article
about: concept
title: "The sorites paradox: how can one grain make no difference, yet a million make a heap?"
description: "Eubulides' heap — one grain is not a heap; adding one grain never turns a non-heap into a heap; so a million grains are not a heap — and the four families of response the SEP lists (deny that logic applies, reject a premise, reject the logic, embrace the conclusion), each with its proponents."
tags: [problem, logic, philosophy-of-language, vagueness, paradox]
timestamp: 2026-09-26T12:00:19Z
---

# The sorites paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md).
Source for the map: Hyde & Raffman,
[SEP Fall 2024 "Sorites Paradox"](https://plato.stanford.edu/archives/fall2024/entries/sorites-paradox/)
(excerpt: `raw/sep-sorites-and-liar-fall-2024-paradox-formulations-and-responses.md`).

## The question

The SEP's conditional form (preamble):

```
1 grain of wheat does not make a heap.
If 1 grain doesn’t make a heap, then 2 grains don’t.
If 2 grains don’t make a heap, then 3 grains don’t.
…
If 999,999 grains don’t make a heap, then 1 million grains don’t.
Therefore, 1 million grains don’t make a heap.
```

"The argument is a paradox because apparently impeccable reasoning from
apparently impeccable premises yields a falsehood" (Hyde & Raffman,
preamble). The same chain run the other way concludes that one grain makes a
heap. The trigger is vague predicates — "‘Bald’, ‘heap’, ‘tall’, ‘old’, and
‘blue’" — terms "with unclear (“blurred” or “fuzzy”) boundaries of
application".

**Logic check (this implant, 2026-09-26).** A four-step instance —
`~H1`, `~H1 -> ~H2`, `~H2 -> ~H3`, `~H3 -> ~H4`, therefore `~H4` — is
reported "VALID" by `logic.py`: the chain is repeated *modus ponens* in
classical propositional logic. So in classical logic the conclusion can be
avoided only by rejecting a premise; the responses that keep every premise
change the logic ([validity](../vocabulary/validity.md)).

**Origin.** "The Megarian philosopher Eubulides (4th century BC) is usually
credited with the first formulation of the puzzle. (The name ‘sorites’
derives from the Greek word soros, meaning ‘heap’.)" (§1). It "was later
used by Greek philosophers as a dialectical weapon, most notably by the
Sceptics against the Stoics’ claims to knowledge" (§1; see
[Stoicism](../schools/stoicism.md)).

## Why it matters

- Vague terms are everywhere in ordinary language; the SEP notes "we use
  these ordinary words successfully all the time" (preamble).
- Everyday versions: Edgington's "‘mañana paradox’" and "dieter’s paradox"
  (1997: 296, quoted in the preamble).
- The responses bear on classical logic itself — bivalence, truth-value
  gaps, degrees of truth — the same principles the
  [liar paradox](liar-paradox.md) presses on.

## Positions taken

Hyde & Raffman's four types (§3): "deny that logic applies to soritical
expressions"; reject "some premise(s)"; deny "that it’s valid"; or "embrace
the paradox". Their subsections, with the proponents they name:

- **Ideal-language approaches** (logic does not apply to vague terms) —
  §3.1; §1 speaks of "the demise of the ideal language doctrines of the
  latter half of the twentieth century".
- **Epistemicism** (reject a premise; vague terms have sharp but unknown
  boundaries): "vagueness is just a form of ignorance: vague terms have
  sharp boundaries whose locations are hidden from us" — Sorensen (1988,
  2001), Williamson (1994a,b, 2000), Graff (2000), Fara (2008), Rescher
  (2009) (§3.2).
- **Supervaluationism** (reject a premise; truth-value gaps): adapts "Van
  Fraassen’s supervaluation semantics (1966)" — Fine (1975), Keefe (2000);
  "retains the classical consequence relation and classical laws while
  admitting truth-value gaps" (§3.3.1).
- **Many-valued and degree theories** (change the logic): three-valued logic
  "first developed in Halldén 1949 and Körner 1960 and revamped in Tye
  1994"; degree theories continue the line (§3.3.3; Edgington 1996 is
  among the authors discussed there).
- **Contextualism**: "Kamp (1981) introduced a contextualist solution"
  (§3.3.4).
- **Multiple range theory** (§3.3.5; not yet excerpted).
- **Embrace the paradox**: "the paradox is unsolvable; we are just stuck with
  it" — Dummett (1975) holds that some vague observational predicates "are
  incoherent" (§3.4). A further type (4) view holds the paradox sound: "it
  is true, after all, that no number of grains of wheat make a heap" (§3.4).

**Distribution as the SEP reports it:** "most theorists of vagueness suppose
that the paradox is solvable, i.e., that the paradoxical argument is
defective and we can discover the defect" (preamble). No survey figure is
recorded.

## Arguments in play

(none recorded as separate argument pages yet). The sorites argument is
stated in full above.

## Thinkers who addressed it

- **Eubulides of Miletus** (4th c. BCE) — first formulation, as usually
  credited (§1).
- **Academic Sceptics vs. the Stoics** — the sorites as a dialectical weapon
  (§1).
- **G. V. Plekhanov** (1908) — cited the paradox as evidence for the "‘logic
  of contradiction’" (§1).
- **Michael Dummett** (1975), **Kit Fine** (1975), **Hans Kamp** (1981),
  **Roy Sorensen** (1988), **Michael Tye** (1994), **Timothy Williamson**
  (1994), **Dorothy Edgington** (1996, 1997), **Rosanna Keefe** (2000),
  **Delia Graff Fara** (2000, 2008) — positions as above.

## Framings and reframings

- **Paradox of vagueness, not of heaps.** The entry treats the sorites as
  generated by vague terms in general (preamble), and lists three conditions
  an argument must meet to be a sorites, beginning with a "sorites series"
  for the predicate (§2).

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — the normative sense this page uses.
- [Validity](../vocabulary/validity.md) — the chain is valid in classical
  logic.
- [Knowledge](../vocabulary/knowledge.md) — epistemicism locates the
  paradox in what we cannot know.
