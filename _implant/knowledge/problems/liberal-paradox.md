---
type: article
about: concept
title: "The liberal paradox (Sen's impossibility of a Paretian liberal)"
description: "Can a rule for social choice respect both unanimous preference (the weak Pareto principle) and a minimal personal sphere for at least two people, for every profile of preferences? Sen's 1970 theorem, his Lady Chatterley's Lover example, Gibbard's 1974 paradox, and the responses on record (giving up Pareto, restricting the domain to non-meddlesome preferences, Nozick's rights as constraints on choice, game-form rights after Gaertner, Pattanaik and Suzumura 1992) with their owners."
tags: [problem, paradox, ethics, political-philosophy, social-choice-theory]
timestamp: 2026-10-08T23:52:36Z
---

# The liberal paradox (Sen's impossibility of a Paretian liberal)

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Primary text: Sen, "The Impossibility of a Paretian Liberal", *Journal of Political Economy* 78(1), 1970, pp. 152–157
([doi:10.1086/259614](https://doi.org/10.1086/259614); excerpt: `raw/sen-1970-impossibility-of-a-paretian-liberal.md`).
Response: Nozick, *Anarchy, State, and Utopia* (1974), pp. 164–166 (ISBN 0-631-19780-X;
excerpt: `raw/nozick-1974-anarchy-state-utopia-sens-argument.md`).
Maps: List, [SEP Fall 2024 "Social Choice Theory"](https://plato.stanford.edu/archives/fall2024/entries/social-choice/)
§3.4 (excerpt: `raw/sep-social-choice-fall-2024-liberal-paradox.md`);
Fleurbaey, [SEP Fall 2024 "Normative Economics and Economic Justice"](https://plato.stanford.edu/archives/fall2024/entries/economic-justice/)
§7.1 (excerpt: `raw/sep-economic-justice-fall-2024-sen-gibbard-rights.md`);
Morreau, [SEP Fall 2024 "Arrow's Theorem"](https://plato.stanford.edu/archives/fall2024/entries/arrows-theorem/)
(excerpt: `raw/sep-arrows-theorem-fall-2024-paretian-libertarian.md`).
Gibbard 1974, Gaertner, Pattanaik & Suzumura 1992 and Sen's later papers were verified
bibliographically only (`raw/liberal-paradox-crossref-records.md`); what they argue is
reported here through the sources named at each point.

## The question

Sen opens: "The purpose of this paper is to present an impossibility result that seems to have some disturbing consequences for principles of social choice." (1970, §I, p. 152).
His starting point: "A common objection to the method of majority decision is that it is illiberal." (p. 152), illustrated by walls and sleeping position: "Similarly, whether you should sleep on your back or on your belly is a matter in which the society should permit you absolute freedom, even if a majority of the community is nosey enough to feel that you must sleep on your back." (p. 152).

**The conditions** (Sen 1970, §II, pp. 153–154). Condition U is unrestricted domain. Condition P: "If every individual prefers any alternative x to another alternative y, then society must prefer x to y." Sen notes "Arrow used a weak version of the Pareto principle." Condition L: "For each individual i, there is at least one pair of alternatives, say (x, y), such that if this individual prefers x to y, then society should prefer x to y, and if this individual prefers y to x, then society should prefer y to x."
Its intention: "The intention is to permit each individual the freedom to determine at least one social choice, for example, having his own walls pink rather than white, other things remaining the same for him and the rest of the society."
Condition L* (Minimal Liberalism): "There are at least two individuals such that for each of them there is at least one pair of alternatives over which he is decisive" — two, because with only one "we might have a dictatorship": "Hence, we demand such freedom for at least two individuals." (p. 154).

**The theorems.** Theorem I: "There is no social decision function that can simultaneously satisfy Conditions U, P, and L." (p. 153). Theorem II, the same with L*: "The following theorem is stronger than Theorem I and subsumes it." (p. 154). In the case of four distinct alternatives the proof turns on: "But by Condition L* society should prefer x to y and z to w, while by the Pareto principle society must prefer w to x, and y to z." (p. 154).
List states the result as "Theorem (Sen 1970a): There exists no preference aggregation rule satisfying universal domain, acyclicity of social preferences, the weak Pareto principle, and minimal liberalism." (SEP §3.4), and reports the name: "Sen generalized this problem—now known as the ‘liberal paradox’—as follows." (§3.4).

**The example** (Sen 1970, §III, p. 155). "There is one copy of a certain book, say Lady Chatterly's Lover, which is viewed differently by 1 and 2." (spelling as printed). "The three alternatives are: that individual 1 reads it (x), that individual 2 reads it (y), and that no one reads it (z)." Person 1, "who is a prude": "In decreasing order of preference, his ranking is z, x, y." Person 2: "His ranking is, therefore, x, y, z." Liberal values give "Thus, the society should prefer z to x." and "Hence y should be judged socially better than z.", so "That is, the society should prefer y to z, and z to x."; both persons rank x above y, "i.e., x is Pareto superior to y." Sen: "Every solution that we can think of is bettered by some other solution, given the Pareto principle and the principle of liberalism, and we seem to have an inconsistency of choice."
List retells it with the names Lewd and Prude and concludes: "So, we are faced with a social preference cycle" (§3.4).

**Propositional check (this implant, 2026-10-01; logic, not a position).**
Atoms: `prude_xy`, `lewd_xy` (each person strictly prefers x to y), `prude_zx` (Prude prefers z to x), `lewd_yz` (Lewd prefers y to z), and `s_xy`, `s_yz`, `s_zx` (society strictly prefers the first to the second).
Premises: the three preference facts from Sen's rankings; Pareto on (x, y) as `prude_xy & lewd_xy -> s_xy`; Prude decisive on (x, z) as `prude_zx -> s_zx`; Lewd decisive on (y, z) as `lewd_yz -> s_yz`; acyclicity for this triple as `~(s_xy & s_yz & s_zx)`.
`python3 _implant/skills/tools/logic.py check` with these seven premises and conclusion `q & ~q` prints `VALID` and `premises are jointly inconsistent — argument is vacuously valid`.
Dropping any one of the three rule premises (Pareto, Prude's right, Lewd's right) gives `INVALID`, with counterexample rows `s_xy=F, s_yz=T, s_zx=T`, `s_xy=T, s_yz=T, s_zx=F` and `s_xy=T, s_yz=F, s_zx=T` respectively (other atoms true).
So in this one profile each of the three rule premises is needed for the inconsistency. The check covers one profile and one triple; the theorem's generality (all profiles under U, any pairs under L*) is quantificational and is not what the tool checks.

## Why it matters

- **The Pareto principle.** Morreau: "But WP is not as harmless as it might seem, and in combination with U it tightly constrains the possibilities for social choice." He cites Sen's 1970 result as the evidence and adds: "This important problem of the “Paretian libertarian” meanwhile has its own extensive literature." (SEP "Arrow's Theorem").
- **Social evaluation, not voting.** List places the result where the rule is "a social evaluation method which a social planner can use to rank social alternatives in an order of social desirability" (SEP §3.4).
- **Rights in economics.** Fleurbaey: "Sen (1970b) and Gibbard (1974) propose, within the framework of social choice, paradoxes showing that it may not be easy to rank alternatives when some individuals have a special right to rank some alternatives that differ only in matters belonging to their private sphere, and when their preferences are sensitive to what happens in other individuals’ private spheres." (SEP §7.1).
- **Distributive justice.** Nozick enlists it in his chapter on distributive justice: "Our conclusions are reinforced by considering a recent general argument of Amartya K. Sen." (1974, p. 164).
- **Relation to Arrow.** Sen: "However, unlike in the theorem of Arrow, we have not required transitivity of social preference." and, of independence of irrelevant alternatives, "This way out is not open here, for the theorem holds without imposing this condition." (1970, p. 156).

## Positions taken

Listed in no order of merit. Each entry gives what its owner says for it and, where a read source records one, what is said against it.

- **Weaken or give up the Pareto principle (Sen 1970).** Sen: "What is the moral? It is that in a very basic sense liberal values conflict with the Pareto principle." and "Or, to look at it in another way, if someone does have certain liberal values, then he may have to eschew his adherence to Pareto optimality." (p. 157). List: "This result suggests that if we wish to respect individual rights, we may sometimes have to sacrifice Paretian efficiency." (§3.4).
  *On the other side:* Morreau reports Arrow's view that the weak Pareto condition is "not debatable except perhaps on a philosophy of systematically denying people whatever they want" (Arrow 1951 [1963]: 34, as quoted in SEP "Arrow's Theorem").
- **Restrict the domain to tolerant preferences.** List: "An alternative conclusion is that the weak Pareto principle can be rendered compatible with minimal liberalism only if the domain of admissible preference profiles is suitably restricted, for instance to preferences that are ‘tolerant’ or not ‘meddlesome’ (Blau 1975; Craven 1982; Gigliotti 1986; Sen 1983)." He adds: "Lewd’s and Prude’s preferences in Sen’s example are ‘meddlesome’." (§3.4). Sen 1970, on where liberty might be secured: "The ultimate guarantee for individual liberty may rest not on rules for social choice but on developing individual values that respect each other's" personal choices (pp. 155–156).
  *On the other side:* the restriction gives up condition U, one of the theorem's premises (structural note of this implant). Sen 1970: the conflict is "not necessarily disturbing for every conceivable society, since the conflict arises with only particular configurations of individual preferences." (p. 155).
- **Rights constrain choice; they do not rank alternatives (Nozick 1974).** Nozick: "The trouble stems from treating an individual’s right to choose among alternatives as the right to determine the relative ordering of these alternatives within a social ordering." and "Rights do not determine a social ordering but instead set the constraints within which a social choice is to be made, by excluding certain alternatives, fixing others, and so on." (pp. 165–166). Also: "Individual rights are co-possible; each person may exercise his rights as he chooses." (p. 166).
  *On the other side:* (none recorded in the sources read here.)
- **Rights as game forms (Gaertner, Pattanaik & Suzumura 1992).** Their abstract: "They demonstrate in terms of a counterexample and general reasoning that Sen's concept can, more often than not, be inconsistent with our intuitive view of rights and fails to capture important categories of rights." and "An alternative formulation in terms of game form is introduced and its relative merit vis-a-vis Sen's formulation is discussed." Fleurbaey reports them as arguing "that no matter what choice A and B make, their rights to choose their own shirt is respected" and assesses: "The framework of game forms is an interesting alternative to the social choice model." (SEP §7.1). List groups them with Dowding and van Hees (2003) among those arguing "that his ‘minimal liberalism’ condition uses an inadequate formalization of the notion of individual rights" (§3.4).
  *On the other side:* Sen replied in "Minimal Liberty" (*Economica* 59, 1992, [doi:10.2307/2554743](https://doi.org/10.2307/2554743)); not read here, so its content is not reported.

## Arguments in play

- **Sen's proof** (1970, §II, p. 154), two cases: the two decisive pairs share one alternative, or all four alternatives are distinct; in each, conditions U, P and L* yield a set with no best element. The three-alternative book case of §III has its two decisive pairs, (x, z) and (y, z), sharing z (structural note of this implant).
- **Nozick's restatement** (1974, p. 165): A decisive over (X, Y), B over (Z, W); "Person A prefers W to X to Y to Z, and person B prefers Y to Z to W to X." His conclusion: "There is no transitive social ordering satisfying all these conditions, and the social ordering, therefore, is nonlinear. Thus far, Sen."
- **Against dropping binary social preference.** Sen, n. 4: "It may appear that one way of solving the dilemma is to dispense with the social choice function based on a binary relation, that is, to relax not merely transitivity but also acyclicity." He answers that P and L must then be restated as conditions on choice, and the choice set "may be rendered empty even without bringing in acyclicity" (p. 156).
- **Gibbard's paradox** (Gibbard 1974, as Fleurbaey reports it): "For instance, as an illustration of Gibbard’s paradox, individuals have the right to choose the color of their shirt, but, in terms of social ranking, should A and B wear the same color or different colors, when A wants to imitate B and B wants to have a different color?" (SEP §7.1).

## Thinkers who addressed it

- **Amartya Sen** (1970, pp. 152–157; "Liberty, Unanimity and Rights", 1976, [doi:10.2307/2553122](https://doi.org/10.2307/2553122); "Minimal Liberty", 1992; 1983 per List) — the theorem and the example.
- **Kenneth Arrow** (1951, 2nd ed. 1963) — the weak Pareto condition Sen adopts (Sen 1970, p. 153).
- **Allan Gibbard** ("A Pareto-consistent libertarian claim", *J. Econ. Theory* 7, 1974, pp. 388–410, [doi:10.1016/0022-0531(74)90111-2](https://doi.org/10.1016/0022-0531(74)90111-2)) — the shirt-colour paradox (Fleurbaey §7.1); Sen 1970, n. 5, also cites an earlier unpublished oligarchy theorem of his.
- **Robert Nozick** (1974, pp. 164–166) — rights as constraints on social choice.
- **Julian Blau** (1975, [doi:10.2307/2296852](https://doi.org/10.2307/2296852)), **J. Craven** (1982), **G. Gigliotti** (1986) — domain restrictions (List §3.4).
- **Aanund Hylland** (1986) — "The Purpose and Significance of Social Choice Theory: some general remarks and an application to the ‘Lady Chatterley problem’" (title as listed by Morreau; not read).
- **Wulf Gaertner, Prasanta K. Pattanaik, Kotaro Suzumura** (1992, *Economica* 59, pp. 161–177, [doi:10.2307/2554744](https://doi.org/10.2307/2554744)) — game-form rights.
- **Keith Dowding, Martin van Hees** (2003, *APSR* 97, [doi:10.1017/s0003055403000674](https://doi.org/10.1017/s0003055403000674)) — the formalization of rights (List §3.4).

## Framings and reframings

- **What "liberal" means.** Sen, n. 1: "The term “ liberalism'' is elusive and is open to alternative interpretations." and "I do not wish to engage in a debate on the right use of the term." (p. 153). Morreau calls it the problem of the "Paretian libertarian"; Gibbard's 1974 title speaks of a "libertarian claim".
- **Pareto as liberty.** Sen: "While the Pareto criterion has been thought to be an expression of individual liberty, it appears that in choices involving more than two alternatives it can have consequences that are, in fact, deeply illiberal." (p. 157).
- **Personal sphere.** List: "Intuitively, each individual has a personal sphere in which this individual alone should be able to decide what happens." and why the condition is called minimal: "The requirement is ‘minimal’ because we would ideally want not just two individuals, but everyone to have such rights, and we would ideally want those rights to concern more than a single pair of alternatives each." (§3.4).
- **From ranking to describing rights.** Fleurbaey: "There is a huge literature on this topic, and after Gaertner, Pattanaik and Suzumura (1992), who argue that no matter what choice A and B make, their rights to choose their own shirt is respected, a good part of it examines how to describe rights properly." (SEP §7.1).
- **Name.** The SEP heading is "The liberal paradox"; the paper's title gives the other name; Hylland's 1986 title uses "Lady Chatterley problem".

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — see The question.
- [Validity](../vocabulary/validity.md) — the propositional check reports joint inconsistency as vacuous validity.
- [Classical logic](../methods/classical-logic.md) — the logic of the propositional check above.
- *Weak Pareto principle*, *unrestricted domain*, *minimal liberalism*, *acyclicity*, *social decision function*, *game form*, *meddlesome preference* — open work in [vocabulary](../vocabulary/index.md).

Related thinkers: [Nozick](../thinkers/nozick.md).

Related problems: [voting paradox](voting-paradox.md) (List §3.4, "a social preference cycle"), [Arrow's impossibility theorem](arrows-impossibility-theorem.md) (Morreau §4.3, List §3.4).

Related concepts: [liberty, positive and negative](../vocabulary/liberty-positive-and-negative.md).
