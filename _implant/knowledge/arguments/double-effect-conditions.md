---
type: article
about: concept
title: The doctrine of double effect (the four conditions)
description: "The principle that a harm may sometimes be caused as a foreseen side effect of a good act though not as a means — Aquinas's self-defence article (ST II-II q. 64 a. 7), Gury's 1850 principle and Mangan's 1949 four conditions, a propositional schema, the closeness problem (Foot 1967, Boyle, Davis), criticisms of intention, proportionality and the trolley application (Hart as Foot reports him, McIntyre 2001, Scanlon 2008, Thomson 2008) and the replies McIntyre reports (Quinn 1989, Boyle, Anscombe)."
tags: [argument, ethics, normative-ethics, double-effect, intention, aquinas, trolley-problem]
timestamp: 2026-10-02T03:07:33Z
---

# The doctrine of double effect (the four conditions)

An argument page of the [arguments](index.md) branch, written under
[Reporting, not endorsing](../../conventions/reporting-not-endorsing.md) and
[How claims are graded](../../conventions/how-claims-are-graded.md). McIntyre
states the principle: "According to the principle of double effect, sometimes it is permissible to cause a harm as an unintended and merely foreseen side effect (or “double effect”) of bringing about a good result even though it would not be permissible to cause such a harm as a means to bringing about the same good end."
([SEP, Fall 2024](https://plato.stanford.edu/archives/fall2024/entries/double-effect/),
rev. 2023-07-17, preamble; excerpt: `raw/sep-double-effect-and-doing-allowing-fall-2024-trolley.md`).

## Earliest primary source

- **Thomas Aquinas, *Summa Theologiae* II-II q. 64 a. 7** ("Whether it is
  lawful to kill a man in self-defense?"; [1920 Dominican tr.](https://www.newadvent.org/summa/3064.htm#article7)):
  "Nothing hinders one act from having two effects, only one of which is intended, while the other is beside the intention."
  The act "may have two effects, one is the saving of one's life, the other is the slaying of the aggressor", and a proportion
  clause follows: "though proceeding from a good intention, an act may be rendered unlawful, if it be out of proportion to the end."
  Intending to kill is reserved: "it is not lawful for a man to intend killing a man in self-defense, except for such as have public authority"
  (respondeo; excerpt: `raw/aquinas-st-2-2-q64-a7-self-defense-two-effects.md`).
- **Who credits Aquinas.** McIntyre (SEP 2024, §1): "Thomas Aquinas is credited with introducing the principle of double effect in his discussion of the permissibility of self-defense in the Summa Theologica (II-II, Qu. 64, Art.7)."
  Mangan (1949, p. 61): "Article seven of question 64 of the Secunda Secundae of St. Thomas' Summa Theologica is the historical beginning of the principle of the double effect as a principle."
  Fiala ([SEP "Pacifism"](https://plato.stanford.edu/archives/fall2024/entries/pacifism/), §4) says the idea
  "is derived in the Christian tradition from Aquinas", adding in his own voice: "It is significant that Aquinas does not expand this discussion to make it permissible to kill an innocent third party."
- **The dissent Mangan reports.** "Vicente M. Alonso, S.J., concludes that St. Thomas held merely that the killing of an unjust aggressor may be willed as a means but not as an end in itself."
  (Mangan 1949, p. 45, citing Alonso, Rome 1937). Mangan replies that Alonso's case "does not eliminate the reasonableness of the"
  traditional reading (p. 46). Whether the article states the later principle is therefore a point on which the two historians Mangan discusses differ.
- **Later history, as Mangan reports it.** "Cajetan seems to be the first to apply the principle of the double effect explicitly to the killing of innocent people."
  (pp. 52–54); "Although the principle as such was not accepted generally before the sixteenth century, it was accepted generally in its application to particular cases by the moralists of the sixteenth and seventeenth centuries and by all who have succeeded them."
  (p. 61). Of Joannes P. Gury's (as Mangan names him) *Compendium Theologiae Moralis*: "In Gury's early editions, the first of which appeared in 1850, the treatment is a complete modern one in brief form."
  (p. 59). Gury's statement, in Mangan's translation from the 1874 Ratisbon edition: "Principle. It is lawful to actuate a morally good or indifferent cause from which will follow two effects, one good and the other evil, if there is a proportionately serious reason, and the ultimate end of the agent is good, and the evil effect is not the means to the good effect."
  (pp. 60–61). Gury's Latin was not read for this page.
- **The four-condition formulation.** Joseph T. Mangan, "An Historical
  Analysis of the Principle of Double Effect", *Theological Studies* 10(1),
  1949, pp. 41–61 ([doi:10.1177/004056394901000102](https://doi.org/10.1177/004056394901000102)),
  p. 43, which also notes: "Some authors express four conditions, others taking one or another condition for granted express only three or two conditions."
  Excerpt: `raw/mangan-1949-historical-analysis-principle-of-double-effect.md`.

## Standard reconstruction

The conditions as McIntyre quotes them from Mangan (SEP 2024, §1; Mangan
1949, p. 43): "A person may licitly perform an action that he foresees will produce a good effect and a bad effect provided that four conditions are verified at one and the same time: that the action in itself from its very object be good or at least indifferent; that the good effect and not the evil effect be intended; that the good effect be not produced by means of the evil effect; that there be a proportionately grave reason for permitting the evil effect (Mangan 1949, p. 43)."

- P1 (object). The action in itself is good or at least indifferent — *O*.
- P2 (intention). The good effect and not the evil effect is intended — *I*.
- P3 (means). The good effect is not produced by means of the evil effect — *M*.
- P4 (proportion). There is a proportionately grave reason — *P*.
- P5 (the principle). If O, I, M and P all hold, the action is licit — *(O & I & M & P) -> L*.
- C. The action is licit — *L*.

Form: deductive, conjunction then modus ponens. The lettering and schema are
this implant's reconstruction (manifest [G4](../../vision/manifest.md)).
Checked with `skills/tools/logic.py check --premises "(O & I & M & P) -> L" "O" "I" "M" "P" --conclusion "L"`:

```
  P1: (O & I & M & P) -> L    [((((O & I) & M) & P) -> L)]
  P2: O    [O]
  P3: I    [I]
  P4: M    [M]
  P5: P    [P]
  C:  L    [L]

VALID
```

Mangan states the conditions as sufficient ("provided that"). Read only
as sufficient, the failure of one condition does not by the schema alone
yield impermissibility; `--premises "(O & I & M & P) -> L" "~M" --conclusion "~L"` returns
`INVALID` with `(8 counterexample rows)`. The prohibition on harm as a means
comes in only when the principle is read as a biconditional or joined to a
separate prohibition; `--premises "L <-> (O & I & M & P)" "~M" --conclusion "~L"` returns `VALID`.
McIntyre (§1) records the separate prohibition: "The prohibition is absolute in traditional Catholic applications of the principle."
The New Catholic Encyclopedia's third condition (Connell 1967, as quoted
by McIntyre §1) states P3 causally: "The good effect must flow from the action at least as immediately (in the order of causality, though not necessarily in the order of time) as the bad effect."
Excerpt: `raw/sep-double-effect-fall-2024-conditions-closeness-critics.md`.

## Supports

- Distinctions between paired cases that McIntyre lists (§2): terror vs.
  tactical bombing ([just war](../problems/just-war.md)), euthanasia vs.
  pain relief ([euthanasia](../problems/euthanasia.md)), abortion vs.
  hysterectomy ([abortion](../problems/abortion.md)), self-defence, heroic
  shielding, and the [trolley problem](../problems/trolley-problem.md).
- The just war tradition's permission for foreseen noncombatant deaths, as
  Fiala reports it (§4): "The just war tradition, however, allows that innocent noncombatants may be killed according to the principle of double effect."
  Absolute pacifists, he reports, "will claim that the killing of the innocent in war is always wrong, even if it is an unintended effect."
- Non-absolutist use: "Double effect might also be part of a secular and non-absolutist view according to which a justification adequate for causing a certain harm as a side effect of pursuing a good end might not be adequate for causing that harm as a means to the same good end under the same circumstances."
  (McIntyre §1). Its bearing on [the ticking time bomb](../problems/ticking-bomb.md)
  case is not treated in the sources held.

## Which premise is disputed, and by whom

- **P3 and P2 — closeness.** McIntyre (§4.2): "One important line of criticism is known as the “problem of closeness”: it is difficult to distinguish between grave harms that are regretfully foreseen as side effects of the agent’s means and grave harms that are so close to the agent’s means that it seems that they must be (regretfully) intended as part of the agent’s means."
  [Foot](../thinkers/foot.md) (1967, *Oxford Review* 5; [doi:10.1093/0199252866.003.0002](https://doi.org/10.1093/0199252866.003.0002) for the 1978 reprint), after the case of the fat man stuck in a cave mouth:
  "What is to be the criterion of ‘closeness’ if we say that anything very close to what we are literally aiming at counts as if part of our aim?"
  (excerpt: `raw/foot-1967-problem-of-abortion-double-effect-closeness.md`).
  On hysterectomy and abortion McIntyre reports both directions: "it is hard to see why the death of the fetus would not be a regretfully foreseen side effect of saving the mother’s life in both cases (Boyle 1991). Or, alternatively, it is hard to see why the death of the fetus would not be regretfully intended as part of the physician’s means of saving the mother’s life in both cases (Davis 1984, 110)."
  Her assessment: "no clear resolution of this problem has emerged" (§4.2).
- **P3 in the craniotomy case — Hart, as Foot reports him.** "This last application of the doctrine has been queried by Professor Hart on the ground that the child’s death is not strictly a means to saving the mother’s life and should logically be treated as an unwanted but foreseen consequence by those who make use of the distinction between direct and oblique intention."
  (Foot 1967). Hart's paper ("Intention and Punishment", *Oxford Review* 4, 1967, per Foot's note) was not read.
- **P5 — whether intention bears on permissibility.** McIntyre (§4.1): "Some opponents of the principle of double effect do indeed deny that the distinction between intended and merely foreseen consequences ever has any kind of moral significance."
  McIntyre (§6), citing McCarthy 2002 and Scanlon 2008: "an agent’s intentions are not relevant to the permissibility of an action in the way that the proponents of the principle of double effect would claim, though an agent’s intentions are relevant to moral assessments of the way in which the agent deliberated".
  Scanlon's *Moral Dimensions* (2008) is not read here; the Fall 2018 SEP edition names him: "T.M. Scanlon (2008) has recently developed this kind of criticism by arguing that the appeal of the principle of double effect is, fundamentally, illusory".
- **P4 — proportionality.** "Critics of the use of double effect as an explanatory principle point out that the proportionality condition is vague and too general, requiring only that the good effect outweigh the foreseen bad effect or that there be sufficient reason for causing the bad effect."
  They add that substantive principles "are doing all of the justificatory work (Davis 1984; McIntyre 2001)" (McIntyre §6).
  McIntyre 2001 is "Doing Away with Double Effect", *Ethics* 111(2): 219–255 ([doi:10.1086/233472](https://doi.org/10.1086/233472)); not read.
- **P1** is not reported as a separate target in the sources held.

## Objections

- **Closeness** (Foot 1967; Boyle 1991; Davis 1984; above).
- **Bennett.** Foot cites "J. Bennett, ‘Whatever the Consequences’, Analysis, January 1966, and G. E. M. Anscombe’s reply in Analysis, June 1966."
  (Analysis 26(3): 83–102, [doi:10.1093/analys/26.3.83](https://doi.org/10.1093/analys/26.3.83)); Bennett's text was not read and its argument is not reported here.
- **Trolley.** [Thomson](../thinkers/thomson.md) (2008) "changed her mind and argued that the consensus that it is permissible for the bystander to turn the trolley was mistaken"
  (Woollard, SEP "Doing vs. Allowing Harm", §3); McIntyre (§4.5) places McIntyre 2001 in the camp that would "reject the claim that the principle of double effect could explain the permissibility of switching the trolley"
  (excerpt: `raw/sep-double-effect-and-doing-allowing-fall-2024-trolley.md`).
- **Foot's alternative.** "I have only tried to show that even if we reject the doctrine of the double effect we are not forced to the conclusion that the size of the evil must always be our guide."
  (Foot 1967); her replacement is a distinction between negative and positive duties.
- **End-of-life applications.** McIntyre (§5.2): "The belief that doctors can cite double effect reasoning to justify actions that hasten death tends to obscure rather than clarify these important issues in palliative care."
  (excerpt: `raw/sep-doing-allowing-and-double-effect-fall-2024-euthanasia.md`).

## Replies

- **Quinn 1989** ("Actions, Intentions, and Consequences: The Doctrine of
  Double Effect", *Philosophy and Public Affairs* 18(4): 334–351, per the
  SEP bibliography; no DOI found): "Quinn’s reformulation of double effect is not absolutist in character. He observes that a result brought about through direct agency might not be impermissible; instead it would require more offsetting benefit than the same result brought about through indirect agency in similar circumstances."
  (McIntyre §4.4).
- **Boyle and Anscombe on risky rescue.** "Proponents of double effect have argued that agents may cause certain and serious harm or run the risk of causing serious harm when they are trying to prevent even greater harm that would otherwise be certain to occur."
  "Dangerous surgery undertaken to save a life is one example (Anscombe 1982; Boyle 1991; Uniacke 1998)." (McIntyre §4.6).
  Boyle 1980, "Toward Understanding the Principle of Double Effect", *Ethics* 90(4): 527–538 ([doi:10.1086/292183](https://doi.org/10.1086/292183));
  Boyle 1991, "Who is entitled to Double Effect?", *J. Medicine and Philosophy* 16(5): 475–494 ([doi:10.1093/jmp/16.5.475](https://doi.org/10.1093/jmp/16.5.475)); neither read.
- **Anscombe's absolutist version.** McIntyre (§4.5) places "those who uphold an absolutist version of the principle of double effect and deny that it provides a permission to swerve the trolley (Anscombe, 1982)"
  among the second trolley camp. [Anscombe](../thinkers/anscombe.md)'s "War and Murder" is recorded by Fiala as "Anscombe, G.E.M., 1981a. “War and Murder” in Ethics, Religion, and Politics, Minneapolis: University of Minnesota Press."
  (not read, so its argument is not reported).
- **Cavanaugh 2006.** T. A. Cavanaugh, *Double-Effect Reasoning: Doing Good
  and Avoiding Evil* (Oxford: Clarendon Press, 2006; [doi:10.1093/0199272190.001.0001](https://doi.org/10.1093/0199272190.001.0001)); bibliographic only.
- **Walzer's added condition.** McIntyre (§1) judges: "Michael Walzer (1977) has convincingly argued that agents who cause harm as a foreseen side effect of promoting a good end must be willing to accept additional risk or to forego some benefit in order to minimize how much harm they cause."

## Variants

- **Gury (1850; 5th German ed. 1874)** — three clauses plus "a morally good or indifferent cause" (Mangan's translation, above).
- **New Catholic Encyclopedia (Connell 1967)** — four conditions with the causal-immediacy wording of the third (McIntyre §1).
- **Quinn's direct/indirect agency** (1989) — non-absolutist, above.
- **Secular, non-absolutist reading** (McIntyre §1) — a higher justificatory threshold for harm as a means.

## Vocabulary

Intended vs. merely foreseen; means vs. side effect; "oblique intention" (Foot, after Bentham);
direct vs. indirect agency (Quinn); proportionality; the object of the act.
Related entries: [argument](../vocabulary/argument.md), [validity](../vocabulary/validity.md),
[dilemma](../vocabulary/dilemma.md). Related problems: [moral dilemmas](../problems/moral-dilemmas.md),
[dirty hands](../problems/dirty-hands.md).

Related thinkers: [Aquinas](../thinkers/aquinas.md) (II-II q. 64 a. 7).
