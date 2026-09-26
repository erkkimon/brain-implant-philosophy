---
type: article
about: concept
title: "Can there be genuine moral dilemmas?"
description: "Whether an agent can be morally required to do each of two acts that cannot both be done, with neither requirement overridden — the examples (Plato, Sartre, Agamemnon, Antigone, Sophie's Choice), the two consistency arguments whose premises make dilemmas impossible, and which premise each side gives up."
tags: [problem, ethics, metaethics, deontic-logic, dilemma]
timestamp: 2026-09-26T12:00:19Z
---

# Can there be genuine moral dilemmas?

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md).
The map follows McConnell's SEP entry
([Fall 2024](https://plato.stanford.edu/archives/fall2024/entries/moral-dilemmas/);
excerpt: `raw/sep-moral-dilemmas-fall-2024-concept-and-consistency-arguments.md`);
where he evaluates, the evaluation is attributed to him.

## The question

A **genuine moral dilemma**, as McConnell defines it (§2): "the agent is
required to do each of two (or more) actions; the agent can do each of the
actions; but the agent cannot do both (or all) of the actions", and
"neither of the conflicting requirements is overridden" (after
Sinnott-Armstrong, *Moral Dilemmas*, 1988, ch. 1). The question is whether
any situation satisfies all of this — or whether in every conflict one
requirement overrides the other, or the real requirement is disjunctive. The
term's senses are separated in [Dilemma](../vocabulary/dilemma.md).

**The cases usually cited** (McConnell §1, §5):

- Plato, *Republic* I 331c (Shorey trans., [Perseus](https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0168%3Abook%3D1%3Asection%3D331c)): returning a borrowed weapon to a friend "who is
  not in his right mind". McConnell: this "strikes many as too easy to be
  characterized as a genuine moral dilemma" (§2), because protecting others
  overrides repaying.
- Sartre's student (Sartre, *Existentialism Is a Humanism*; McConnell cites
  the 1957 English edition): avenge his brother and fight, or stay with his
  mother, for whom "he was her one consolation in life" (§1).
- Aeschylus' Agamemnon (his daughter or the expedition) and Sophocles'
  Antigone (bury Polyneices or obey Creon) (§1).
- *Sophie’s Choice*: a **symmetrical** case, where "the same precept
  generates the conflicting requirements" (§5).

## Why it matters

- **Action-guidance.** "theories that allow for dilemmas fail to be uniquely
  action-guiding" (McConnell §4) — the reason he gives why Kant, Mill and
  Ross "would be disturbed" if their theories allowed them.
- **Deontic logic.** Allowing dilemmas forces the rejection of one of
  several principles of deontic logic (next section).
- **Moral emotion.** McConnell's conclusion asks opponents: "Why are certain
  moral emotions appropriate if the agent has done no wrong?" (§9; the
  "moral residue" debate, §6, not yet excerpted).
- **Applied ethics.** Cases in "biomedical ethics, business ethics, and legal
  ethics" (§1), e.g. a defence attorney's duties of confidentiality and of
  candour to the court (§4, citing Freedman 1975).

## Positions taken

The two arguments McConnell sets out (§4) each derive a contradiction from
"dilemmas exist" plus two principles. Every position is a choice of what to
give up. None is ranked here.

**Argument 1 (PC + PD).** "(PC) OA → ¬O¬A" (deontic consistency: the same
act is not both obligatory and forbidden) and "(PD) □(A → B) → (OA → OB)"
(what an obligatory act necessarily brings about is obligatory). From OA,
OB and "¬C(A & B)" (cannot do both), McConnell derives "OA and O¬A", which
"directly conflicts with PC".

**Argument 2 (ought-implies-can + agglomeration).**

```
1. OA
2. OB
3. ¬C(A & B)
4. OA → CA          ("ought" implies "can", for all A)
5. (OA & OB) → O(A & B)   (agglomeration, Williams 1965)
6. O(A & B) → C(A & B)    (instance of 4)
7. OA & OB          (1, 2)
8. O(A & B)         (5, 7)
9. ¬O(A & B)        (3, 6)
```

Propositional check (this implant, 2026-09-26): with the modal formulas
taken as atoms — OA, OB, OAB for O(A & B), CAB for C(A & B) — the premises
`OA`, `OB`, `~CAB`, `OAB -> CAB`, `OA & OB -> OAB` are reported by
`logic.py` as "jointly inconsistent"; dropping premise 1 makes `~OA`
follow validly. That is: given 2–6, the tool confirms, any one of the
premises can be kept only by rejecting another. Which one to reject is the
dispute. (The check covers the propositional skeleton only; the step from
4 to 6 is instantiation, outside `logic.py`.)

- **No genuine dilemmas.** "Opponents of moral dilemmas have generally held
  that the crucial principles in the two arguments above are conceptually
  true, and therefore we must deny the possibility of genuine dilemmas.
  (See, for example, Conee 1982 and Zimmerman 1996.)" (§5). For symmetrical
  cases they posit a disjunctive requirement: "Sophie should act to save one
  or the other of her children" (Zimmerman 1996, ch. 7, as reported §5).
- **Dilemmas; reject "ought" implies "can".** "some took the existence of
  dilemmas as a counterexample to ‘ought’ implies ‘can’ (for example,
  Lemmon 1962 and Trigg 1971)" (§5).
- **Dilemmas; reject agglomeration.** "others, as a refutation of the
  agglomeration principle (for example, Williams 1965 and van Fraassen
  1973)" (§5).
- **Dilemmas; reject PD.** "A common response to the first argument is to
  deny PD" (§5).
- **Principles hold only in ideal worlds.** Holbo (2002): in the real world
  they "have heuristic value, bidding agents in conflict cases to look for
  permissible options, though none may exist" (as reported §5).
- **Independent reasons against the principles.** "Walter Sinnott-Armstrong
  (Sinnott-Armstrong 1988, Chapters 4 and 5) has gone to the greatest
  lengths to provide independent reasons for questioning some of the
  relevant principles" (§5).
- **Consistency is not the issue.** Ruth Barcan Marcus: rules are consistent
  "if there are possible circumstances in which no conflict will emerge"
  ("Moral Dilemmas and Consistency", *Journal of Philosophy* 77 (1980):
  121–136, at 128–129, as quoted §4) — on which dilemma-generating rules can
  be consistent.

**Burdens as McConnell states them (§9):** "Opponents of dilemmas must show
why appearances are deceiving. [...] Supporters must show why several of
many apparently plausible principles should be given up". His own summary:
"the debate is apt to continue".

No survey figure on this question is recorded (the 2009 PhilPapers Survey
did not ask it; see `raw/philpapers-2009-survey-trolley-and-ethics.md`).

## Arguments in play

(none recorded as separate argument pages yet). The two consistency
arguments above are stated in full on this page; they are candidates for
their own argument pages.

## Thinkers who addressed it

- **Plato** — *Republic* I 331c, the weapon case.
- **Aeschylus, Sophocles** — the literary cases.
- **Thomas Aquinas** — cited in McConnell's bibliography (*Summa
  Theologiae*); his position is not excerpted yet.
- **Kant, Mill, Ross** — "were likely aware that a dilemma-generating theory
  need not be inconsistent" yet "would be disturbed if their own theories
  allowed for such predicaments" (McConnell's own "speculation", §4).
- **Jean-Paul Sartre** — the student (1957 edition, as cited).
- **E. J. Lemmon** (1962, 1965), **Bernard Williams** (1965, "Ethical
  Consistency", *PAS Supp.* 39: 103–124), **Bas van Fraassen** (1973),
  **Ruth Barcan Marcus** (1980), **Earl Conee** (1982), **Walter
  Sinnott-Armstrong** (1988), **David Brink** (1994), **Michael Zimmerman**
  (1996), **John Holbo** (2002) — positions as above.

## Framings and reframings

- **Uncertainty is not a dilemma.** Opponents reply that "the mere fact that
  one does not know which of two (or more) conflicting obligations prevails
  does not show that none does" (§5).
- **Multiple moralities.** McConnell's §8 treats conflicts between different
  moral codes; not yet excerpted.

## Vocabulary

- [Dilemma](../vocabulary/dilemma.md) — the moral sense and the argument
  form.
- [Validity](../vocabulary/validity.md) — what the logic check does and does
  not show.
- [Paradox](../vocabulary/paradox.md) — the two arguments share a paradox's
  shape: plausible premises, an unacceptable conclusion.
