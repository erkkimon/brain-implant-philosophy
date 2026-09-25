---
type: article
about: concept
title: "Validity"
description: "The property of an argument whose form guarantees that if all premises are true, the conclusion must be true — a mechanical relation between sentences, independent of whether anyone believes them or whether the premises are in fact true."
tags: [vocabulary, logic]
timestamp: 2026-09-25T23:58:00Z
---

# Validity

## Normative definition (this implant)

An argument is **valid** when its form guarantees that if every premise is
true, the conclusion is true. Validity is a relation between sentences, not
between beliefs; it is checked mechanically by
`logic.py` and does not depend on whether the
premises are actually true, whether anyone accepts them, or whether the
conclusion is plausible. An argument can be valid with false premises and a
false conclusion; it cannot be valid with true premises and a false
conclusion.

Why this definition: validity is what makes
[analyse-an-argument](../../skills/analyse-an-argument.md) a computation
rather than a judgement. If validity depended on content, plausibility, or
audience response, the tool could not decide it. This sense is the one
[classical logic](../methods/classical-logic.md) implements and the one
the implant's G1 trusts ([manifest](../../vision/manifest.md)).

Fixed 2026-09-25 ([journal](../../journals/2026-09-25.md)).

## Descriptive definitions

- **Classical logic (standard):** "An argument is valid if and only if it is
  impossible for all the premises to be true and the conclusion false"
  (Copi, Cohen & Flage, *Introduction to Logic*, 14th ed., 2018, p. 7).
  This is the sense `logic.py` checks via
  truth tables and named forms.
- **Model-theoretic:** an argument is valid when every model that satisfies
  the premises also satisfies the conclusion. Equivalent to the standard
  definition for propositional and first-order classical logic; diverges in
  non-classical logics where truth-preservation and consequence come apart.
- **Proof-theoretic:** an argument is valid when there exists a derivation
  of the conclusion from the premises in a given proof system. Soundness
  and completeness theorems relate this to the semantic definition.
- **Informal / everyday usage:** often "convincing" or "reasonable". This
  sense is excluded; when a source uses "valid" this way, the implant
  reports the ordinary sense explicitly and distinguishes it from logical
  validity.
- **Legal / administrative:** "having legal force". Excluded; no collision
  risk in philosophical context.

## Collisions

- **Validity vs. soundness.** A sound argument is a valid argument with all
  true premises. Soundness depends on facts about the world; validity does
  not. The implant evaluates validity mechanically; soundness requires
  checking each premise against its receipt
  ([every claim carries its receipt](../../conventions/every-claim-carries-its-receipt.md))
  and is reported as a separate assessment, never as a property of the
  argument's form.
- **Validity vs. cogency.** In informal logic, a cogent argument is a strong
  inductive argument with true premises. Cogency is to induction what
  soundness is to deduction. The implant records cogency claims when citing
  informal-logics sources but does not use cogency as a substitute for
  validity in reconstructions.
- **Validity vs. persuasiveness.** A valid argument may persuade no one; a
  persuasive text may contain no valid argument. The distinction is why
  [spot-persuasion-and-bias](../../skills/spot-persuasion-and-bias.md) and
  [analyse-an-argument](../../skills/analyse-an-argument.md) are separate
  skills.

## Related terms

- [Argument](argument.md) — the unit whose validity is evaluated.
- [Classical logic](../methods/classical-logic.md) — the working logic that
  defines validity for this implant (G1).
- [*Fallacy*](fallacy.md) — patterns classified as defective; some are invalid # lint: allow
  forms, others are valid but misleading.
