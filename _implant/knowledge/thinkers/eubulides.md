---
type: article
about: person
title: Eubulides of Miletus
description: "Eubulides of Miletus (mid-4th c. BCE), placed by Diogenes Laertius in the school of Euclides — the seven arguments Diogenes Laertius lists under his name (Liar, Disguised, Electra, Veiled Figure, Sorites, Horned One, Bald Head), who else the ancient sources credit with them, and how SEP authors word the attributions."
tags: [thinker, megarian, ancient-greek, logic, paradox]
timestamp: 2026-09-28T07:01:48Z
---

# Eubulides of Miletus

No writing of Eubulides survives in the sources this page holds; everything
below is what later reporters say of him, each named. What the page adds
itself is marked as a structural note
([Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
[How claims are graded](../../conventions/how-claims-are-graded.md)).

## Facts a claim depends on

- **Date.** Bobzien (SEP "Ancient Logic", 2020 rev., §1) places him in the
  "mid-4th c."; Hyde & Raffman (SEP "Sorites Paradox", 2018 rev., §1) say
  "4th century BC". Excerpts: `raw/sep-logic-ancient-dialectical-school-fall-2024-eubulides.md`,
  `raw/sep-sorites-and-liar-fall-2024-paradox-formulations-and-responses.md`.
- **School.** "To the school of Euclides belongs Eubulides of Miletus"
  (Diogenes Laertius, *Lives* II.108, tr. Hicks 1925). Hyde & Raffman call
  him "The Megarian philosopher Eubulides" (§1).
- **Pupils, per Diogenes.** Alexinus of Elis (II.109), Euphantus of Olynthus
  (II.110), and Apollonius Cronus, teacher of Diodorus Cronus (II.111).
  "Demosthenes was probably his pupil" (II.108). Excerpt:
  `raw/diogenes-laertius-2-108-111-eubulides-hicks.md`.
- **Pupils, per the SEP.** Bobzien & Duncombe (SEP "Dialectical School",
  2023 rev., §1): "Clinomachus of Thurii, a pupil of Eubulides of Miletus"
  and "Euphantus of Olyntus, another pupil of Eubulides, probably born
  before 349 BC".
- **Quarrel with Aristotle.** "Eubulides kept up a controversy with
  Aristotle and said much to discredit him" (II.109).

## Problems addressed

Diogenes' list, in his order: "The Liar, The Disguised, Electra, The Veiled
Figure, The Sorites, The Horned One, and The Bald Head", described as
"dialectical arguments in an interrogatory form" (II.108). Diogenes gives
the wording of none of them in his life of Eubulides; for each, the page
gives the earliest wording held and who else it is ascribed to.

- **[The liar paradox](../problems/liar-paradox.md).** Bobzien: Eubulides
  "is on record as the inventor of both the Liar and the Sorites paradox"
  (§1), and refers to "the discovery of the Liar paradox by Eubulides of
  Miletus (mid-4th c. BCE)". Priest, Berto & Weber (SEP "Dialetheism", 2024
  rev., §3.2): "the standard Liar is attributed to the Greek philosopher Eubulides, probably the greatest paradox-producer of antiquity"
  (excerpt: `raw/sep-dialetheism-fall-2024-priest-liar-inclosure-curry-objections.md`).
  Beall, Glanzberg & Ripley (SEP "Liar Paradox", 2016 rev.) name no
  individual: it "was discussed in classical times, notably by the
  Megarians", and a like sentence is attributed by "the tradition" to
  Epimenides (preamble).
- **[The sorites paradox](../problems/sorites-paradox.md) (the heap).**
  Hyde & Raffman: "The Megarian philosopher Eubulides (4th century BC) is
  usually credited with the first formulation of the puzzle" (§1), adding
  "we don’t know his motivations for introducing it". The earliest wording
  held is the Stoic example in Diogenes VII.82: "But two is few, therefore
  so also is ten."
- **The bald head.** Listed separately by Diogenes (II.108). Hyde & Raffman
  use "bald" as a sorites predicate: "if a man with n hairs is bald then so
  is a man with n+1 hairs" (§2). *Structural note:* the page reads the Bald
  Head as a sorites series on hairs only in the sense that the SEP example
  has that form; no held source states the ancient wording.
- **Electra and the hooded (veiled, disguised) man.** The wording held is
  Lucian's (*The Sale of Creeds*, tr. Fowler), spoken by Chrysippus, not
  Eubulides: Electra "to whom the same thing was known and unknown at the
  same time", and "the Man in the Hood is your father. You don't know the
  Man in the Hood. Therefore you don't know your own father." Excerpt:
  `raw/lucian-sale-of-creeds-electra-hooded-fowler.md`.
- **The horned one.** Diogenes VII.187, among arguments Chrysippus "used to
  propound": "you never lost horns, ergo you have horns"; Diogenes adds
  "Others attribute this to Eubulides."
  Bobzien classes the Horned One among "the paradoxes of presupposition"
  (§5.5).

*Structural note (logic).* The horned argument as quoted has the form
if not lost, then had; not lost; so had. With L for *you lost horns* and
H for *you have horns*, the tool's actual output:

```
$ python3 _implant/skills/tools/logic.py check --premises "~L -> H" "~L" --conclusion "H"
  P1: ~L -> H    [(~L -> H)]
  P2: ~L    [~L]
  C:  H    [H]

VALID
matches schema: modus ponens
```

The Stoic reply Bobzien reports is a "hidden scope ambiguity of negation",
i.e. a reading of the premises, not of the form.

## Works

(none recorded) No title by Eubulides is quoted in the sources held.
Diogenes calls him "the author of many dialectical arguments" (II.108).

## In dialogue with

- **Aristotle:** the controversy in Diogenes II.109.
- **Diodorus Cronus:** Diogenes II.111 says Diodorus "was supposed to have
  been the first who discovered the arguments known as the" Veiled Figure
  and Horned One — a competing ascription for two of the seven. Bobzien & Duncombe read it
  so: "DL 2.111 gives Diodorus as the author of the Veiled and Horned
  arguments" (§6).
- **The Dialectical School:** Bobzien & Duncombe define it as "philosophizing
  in the — Socratic — tradition of Eubulides of Miletus" (preamble); Bobzien
  calls the dialecticians "possibly influenced by Eubulides" (§4).
- **Chrysippus and the [Stoics](../schools/stoicism.md):** "The Stoics
  recognized the importance of both the Liar and the Sorites paradoxes"
  (Bobzien §5.5); Diogenes lists the Veiled, Horned, Sorites among Stoic
  "insoluble arguments" (VII.82) and a Chrysippus title on "the Veiled Person" (VII.198). Hyde & Raffman: the sorites was later
  used "most notably by the Sceptics against the Stoics’ claims to
  knowledge" (§1).
- **Modern work on the same problems:** [Tarski](tarski.md) and
  [Priest](priest.md) on the liar; [Williamson](williamson.md) on the
  sorites (epistemicism). *Structural note:* these link by problem, not by
  any response to Eubulides that a held source records.

## Reception

- **Crediting him:** Bobzien (§1, §3) and Hyde & Raffman (§1), in the
  terms quoted above ("on record", "said to have been",
  "usually credited"); Priest, Berto & Weber's "attributed to" and their
  "probably the greatest paradox-producer of antiquity" (§3.2); Cantini
  (SEP "Paradoxes and Contemporary Logic", preamble) credits "the arguments entangling the notions of truth and vagueness" to "the Megarian School, and Eubulides of Miletus".
- **Crediting others or no one:** Diogenes himself gives Diodorus as first
  discoverer of the Veiled and Horned (II.111) and reports the horns
  argument from Chrysippus with only "Others" naming Eubulides (VII.187);
  Lucian gives Electra and the Hood to Chrysippus; Beall, Glanzberg &
  Ripley credit "the Megarians" and the Epimenides tradition, not
  Eubulides by name.
- **Ancient hostile assessment:** a comic poet quoted by Diogenes calls
  him "Eubulides the Eristic, who propounded his quibbles about horns and
  confounded the orators with falsely pretentious arguments" (II.108).
- **Bibliographic only:** Roy Sorensen, *Eubulides and the Politics of
  the Liar*, in *A Brief History of the Paradox* (Oxford University Press,
  2003), pp. 83–99, DOI [10.1093/oso/9780195159035.003.0007](https://doi.org/10.1093/oso/9780195159035.003.0007)
  (verified by DOI content negotiation; chapter not read).

## Vocabulary

[Paradox](../vocabulary/paradox.md): Diogenes' Hicks translation calls
the seven "dialectical arguments" (II.108), the Stoic list "insoluble
arguments" (VII.82) and "fallacies" (VII.44); the comic poet "quibbles".
The SEP entries say "paradox" or "puzzle". "Megarian" and "school of
Euclides" name the same affiliation in Hyde & Raffman and Diogenes.
Branch index: [thinkers](index.md).
