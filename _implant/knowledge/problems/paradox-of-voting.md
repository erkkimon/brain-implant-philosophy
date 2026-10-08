---
type: article
about: concept
title: "Paradox of voting (Downs paradox)"
description: "If a single vote almost never decides an election, why does a rational person bear the cost of voting? The page sets out the problem as Downs's 1957 analysis is reported, and the responses on record side by side — Riker and Ordeshook's duty term, Ferejohn and Fiorina's minimax regret, mandate, causal, expressive and duty accounts, Edlin, Gelman and Kaplan's social preferences, laboratory tests — and the critique of rational-choice explanation by Green and Shapiro, each with its owner."
tags: [problem, paradox, decision-theory, political-philosophy, rational-choice, voting]
timestamp: 2026-10-08T21:37:56Z
---

# Paradox of voting (Downs paradox)

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
sources graded as in [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md). Admitted from Wikipedia's
[List of paradoxes, rev. 1376699902](https://en.wikipedia.org/w/index.php?title=List_of_paradoxes&oldid=1376699902),
section "Decision theory", which gives it as "Paradox of voting: Also known as the Downs paradox. For a rational, self-interested voter the costs of voting will normally exceed the expected benefits, so why do people keep voting?"
(excerpt: `raw/wikipedia-list-of-paradoxes-paradox-of-voting-entry.md`). The
same list's separate "Voting paradox" entry (Condorcet's cycle) is a different
problem, treated under [Arrow's impossibility theorem](arrows-impossibility-theorem.md).
Map: Jason Brennan, [SEP Fall 2024 "The Ethics and Rationality of Voting"](https://plato.stanford.edu/archives/fall2024/entries/voting/), §1
(excerpt: `raw/sep-voting-fall-2024-rationality-of-voting.md`); Christiano &
Bajaj, [SEP Fall 2024 "Democracy"](https://plato.stanford.edu/archives/fall2024/entries/democracy/), §4.1
(excerpt: `raw/sep-democracy-fall-2024-problem-of-participation.md`).
Downs, *An Economic Theory of Democracy* (New York: Harper and Row, 1957; ISBN
0060417501 for the Harper & Row printing, per Open Library) was not available
to read and is reported only as the SEP authors and Edlin, Gelman & Kaplan
cite it. Papers read only as abstracts are collected in
`raw/voting-paradox-classic-papers-abstracts.md`.

## The question

Brennan (SEP, §1) states it: "Economics, in its simplest form, predicts that rational people will perform an activity only if doing so maximizes expected utility."
"However, economists have long worried that, that for nearly every individual citizen, voting does not maximize expected utility."
"This leads to the “paradox of voting”(Downs 1957): Since the expected costs (including opportunity costs) of voting appear to exceed the expected benefits, and since voters could always instead perform some action with positive overall utility, it’s surprising that anyone votes."

**The model, in the SEP's notation (§1.1).** The expected value of a vote
cast only to change the outcome is p·(V(D) − V(R)) − C, with p the
probability of being decisive and C the opportunity cost. Brennan: "In short, the value of her vote is the value of the difference between the two candidates discounted by her chance of being decisive, minus the opportunity cost of voting."
"In this way, voting is indeed like buying a lottery ticket."

**Logic check (this implant, 2026-10-09; logic, not a position).** Write M
for: the voter maximises expected utility; G for: the voter's only aim is to
change the outcome; V for: the voter votes; X for: voting has positive
expected utility. `logic.py check --premises "M & G -> (V -> X)" "~X" "V" --conclusion "~M | ~G"`
prints `VALID`. Whoever accepts that turnout occurs and that X is false must
give up M or G; the responses below divide over which, or deny ~X.

**How small is p?** The figures are the researchers'. Brennan reports that binomial models imply that "the expected benefit of voting (i.e., \(p[V(D) - V(R)]\)) for a good candidate is worth far less than a millionth of a penny (G. Brennan and Lomasky 1993: 56–7, 119)."
and that a statistical model "suggests that that a vote in very close states could have on the order of a 1 in 10 million chance of breaking a tie (Edlin, Gelman, and Kaplan 2007)."
Christiano & Bajaj (SEP "Democracy", §4.1) write: "For example, one widely accepted estimate puts the odds of an individual casting the deciding vote in a United States presidential election at 1 in 100 million."
Edlin, Gelman & Kaplan's own worked case (2007, p. 297; decisiveness about
1/(0.12n), n = 1 million): "even if the outcome of the election is worth $10,000 to a particular voter, the expected utility gain is less than 10 cents."
Arithmetic (this implant): 10,000 / (0.12 × 1,000,000) ≈ 0.083 dollars.

**Is it a paradox?** Riker & Ordeshook (1968, opening paragraph) call it "an apparent paradox in the theory"; Ferejohn & Fiorina (1974) title theirs "The Paradox of Not Voting"; Mackie's manuscript is listed by Edlin, Gelman & Kaplan as "The nonparadox of nonvoting" (2007; not read).
See [paradox](../vocabulary/paradox.md) for this implant's normative sense.

## Why it matters

- **For rational-choice explanation.** Riker & Ordeshook: "The writers who constructed these analyses were engaged in an endeavor to explain political behavior with a calculus of rational choice; yet they were led by their argument to the conclusion that voting, the fundamental political act, is typically irrational." Their verdict on that: "We find this conflict between purpose and conclusion bizarre but not nearly so bizarre as a non-explanatory theory: The function of theory is to explain behavior and it is certainly no explanation to assign a sizeable part of politics to the mysterious and inexplicable world of the irrational." (1968, first paragraph, via OpenAlex; text: [doi:10.2307/1953324](https://doi.org/10.2307/1953324)).
- **For democratic theory.** Christiano & Bajaj report the argument that voting is not rational and add Downs's further claim: "Worse still, Anthony Downs has argued that almost all of those who do vote have little reason to become informed about how best to vote (Downs 1957: ch.13)." Their assessment: "These observations pose challenges for any robustly egalitarian or deliberative conception of democracy." (§4.1).
- **For the ethics of voting.** Brennan's entry takes the question first among six, before the duty to vote; he applies the same small-probability point to Downs's suggestion that voting is insurance against democratic collapse ("Downs 1957: 257"): "The problem here is that just as there is a vanishingly small probability that any individual’s vote would decide the election, so there is a vanishingly small chance that any vote would decisively put the number of votes above that threshold." (§2).

## Positions taken

Brennan's grouping (§1): "However, whether voting is rational or not depends on just what voters are trying to do."
He sorts the answers into instrumental (outcome, mandate), expressive,
consumption and duty theories. The lines below follow that grouping and add
the decision-theoretic and social-preference responses from their own papers.
None is ranked.

**Accept the conclusion for outcome-seeking voters.**

- **Downs (1957)**, as reported: the costs "appear to exceed the expected benefits" (Brennan §1, above). Brennan on the instrumental case: "If their goal is to in some way change the outcome of the election, or to change which policies are implemented, then voting is indeed irrational, or rational only in unusual circumstances or for a small subset of voters." (§1.3) — his assessment.
- **Closeness matters (Edlin, Gelman & Kaplan's estimates, as Brennan reads them).** "The binomial model suggests it will almost never be rational to vote, while the statistical model suggests it will be rational for voters to vote in sufficiently close elections or in swing states." (§1.1). Against even this: "However, some claim even these assessments are optimistic." — courts (Somin 2013) and voters' ability to judge which candidate is better (J. Brennan 2011a; Freiman 2020), per Brennan.

**Add a term for duty or participation (deny that only the outcome counts).**

- **Riker & Ordeshook (1968).** The abstract: "We describe a calculus of voting from which one infers that it is reasonable for those who vote to do so and also that it is equally reasonable for those who do not vote not to do so." and "Furthermore we present empirical evidence that citizens actually behave as if they employed this calculus." Ordeshook's 2006 retrospective names the added term: "the necessity for positing a D term (“citizen duty”) to render the act of voting rational." ([doi:10.1017/s0003055406322563](https://doi.org/10.1017/s0003055406322563)). The 1968 formula itself was not read here.
- **Duty, as surveys report it (Mackie 2010, via Brennan).** "Another simple and plausible argument is that it can be rational to vote in order to discharge a perceived duty to vote (Mackie 2010)." and "Surveys indicate that most citizens in fact believe there is a duty to vote or to “do their share” (Mackie 2010: 8–9)." (§1.3).
- **Against the duty term (the tautology charge).** Ordeshook (2006) reports it: "with the addition of D the question arose as to whether we made voting rational only by rendering the concept of rationality a tautology: rational people voted because, with D, we assumed they were rational." His reply compares voting with eating: "Yet the argument that the benefits of voting are dominated by a private D term as opposed to some public PB calculation occasions precisely that accusation." Edlin, Gelman & Kaplan: "Of course, one could allow civic duty to be higher in close elections but then the theory becomes tautological." (2007, §3).

**Change the decision rule (deny M as expected-utility maximisation).**

- **Ferejohn & Fiorina (1974), minimax regret.** "Such analyses treat rational behavior as synonymous with expected utility maximization." and "In this paper we show that an alternative criterion for decision making under uncertainty, minimax regret, specifies voting under quite general conditions." They draw a testable difference: "Interestingly, a minimax regret decision maker never votes for his second choice in a three candidate election, whereas expected utility maximizers clearly may." (abstract; [doi:10.2307/1959502](https://doi.org/10.2307/1959502); full text not read).

**Change the goal (deny G).**

- **Mandate.** Brennan: "One popular response to the paradox of voting is to posit that voters are not trying to determine who wins, but instead trying to change the “mandate” the elected candidate receives." Against, as he reports the empirical work: "Political scientists have done extensive empirical work trying to test whether electoral mandates exist, and they now roundly reject the mandate hypothesis (Dahl 1990b; Noel 2010)." A variant: "Perhaps voting is rational not as a way of trying to change how effective the elected politician will be, but instead as a way of trying to change the kind of mandate the winning politician enjoys (Guerrero 2010)." — to which Brennan applies the same threshold reasoning (§1.2).
- **Causal responsibility (Tuck 2008; Goldman 1999, via Brennan).** "These causal theories of voting claim that voting is rational provided the voter sufficiently cares about being a cause or among the joint causes of the outcome." (§1.3).
- **Expressive voting (G. Brennan & Lomasky 1993).** "The expressive theory of voting (G. Brennan and Lomasky 1993) holds that voters vote in order to express themselves." and "On the expressive theory, voting is a consumption activity rather than a productive activity; it is more like reading a book for pleasure than it is like reading a book to develop a new skill." (§1.3). Against intrinsic accounts generally, Edlin, Gelman & Kaplan: "Intrinsic theories of voting understand voting as an experience that provides psychological benefits, but such explanations do not help us predict variations in voter turnout, such as high turnout in close elections and presidential elections." (2007, p. 294).
- **Consumption value.** Brennan: "Alternatively, one might hold that voting is rational because it is has consumption value; many people enjoy political participation for its own sake or for being able to show others that they voted." (§1).

**Change the benefit (social preferences).**

- **Edlin, Gelman & Kaplan (2007),** [doi:10.1177/1043463107077384](https://doi.org/10.1177/1043463107077384), *Rationality and Society* 19(3) 293–314: "We demonstrate that voting is rational even in large elections if individuals have ‘social’ preferences and are concerned about social welfare." The mechanism: "This is multiplied by a probability of decisiveness that is proportional to 1/n, and thus the expected utility of voting is proportional to N/n, which is approximately independent of the size of the electorate." For the selfish voter they agree with the paradox: "For a selfish voter, the expected benefits from being pivotal and swinging the election vanish as n grows." and "Conversely, rational and purely selfish people should not vote." They set their term against duty: "The natural way to empirically distinguish our social preference, Bsoc, from civic duty is that Bsoc is multiplied by Pr (election is tied), and civic duty is not."

**Question the model's scope.** Brennan: "However, these are controversial simplifying assumptions." and "It is possible that the choice to cast a vote may induce others to vote, might improve the quality of the ground decision by adding cognitive diversity, might have some marginal influence on which candidates or platforms parties run, or might have some other effect not modeled in the equation above." (§1.1).

**Empirical tests, as the researchers report them.**
- Levine & Palfrey (2007, laboratory study, [doi:10.1017/s0003055407070013](https://doi.org/10.1017/s0003055407070013); pointer: Wikipedia "Paradox of voting", [oldid 1368673256](https://en.wikipedia.org/w/index.php?title=Paradox_of_voting&oldid=1368673256)) start from "It is widely believed that rational choice theory is grossly inconsistent with empirical observations about voter turnout." and report "We find that the three main comparative statics predictions are observed in the data: the size effect, whereby turnout goes down in larger electorates; the competition effect, whereby turnout is higher in elections that are expected to be close; and the underdog effect, whereby voters supporting the less popular alternative have higher turnout rates." Deviations from Nash equilibrium "are consistent with the logit version of Quantal Response Equilibrium, which provides a good fit to the data, and can also account for significant voter turnout in very large elections." (abstract).
- Against reading closeness effects as decisiveness: "However, it has been pointed out from both proponents and opponents of the rational-choice model (e.g., Aldrich 1993; Green and Shapiro 1994) that, for large elections, the probability of a single vote being decisive is minuscule even if the election is anticipated to be close." (Edlin, Gelman & Kaplan 2007, §3).
- François & Gergaud, "Is civic duty the solution to the paradox of voting?", *Public Choice* 180 (2019) 257–283 ([doi:10.1007/s11127-018-00635-7](https://doi.org/10.1007/s11127-018-00635-7)) — verified bibliographically only; its findings are not reported here.

**The critique of the research programme.** Green & Shapiro, *Pathologies of
Rational Choice Theory* (Yale University Press, 1994; ISBN 0300059140), not
read; Edlin, Gelman & Kaplan cite its chapter 4 on voting and list it among
works holding that turnout in large elections cannot be explained by selfish
benefits (2007, p. 294). The publisher's description: "This is the first comprehensive critical evaluation of the use of rational choice theory in political science."
and "In their hard-hitting critique, Green and Shapiro demonstrate that the much heralded achievements of rational choice theory are in fact deeply suspect and that fundamental rethinking is needed if rational choice theorists are to contribute to the understanding of politics."
A later appraisal, Hug (2014, [doi:10.1111/spsr.12123](https://doi.org/10.1111/spsr.12123)): "While the publication of this book has fruitfully led rational choice scholars to be more attentive to links between theoretical models and their empirical implications, some misunderstandings about the theoretical contributions of this approach still affect the discipline." (abstract).

## Arguments in play

(none recorded as separate argument pages yet). The decision-theoretic argument (logic check above), the threshold argument Brennan applies to mandate and insurance responses (§§1.2, 2), and the tautology charge against the duty term (Ordeshook 2006; Edlin, Gelman & Kaplan 2007) are quoted above.

## Thinkers who addressed it

- **G. W. F. Hegel** (1821), *Philosophy of Right* §311 note (Dyde trans. 1896, p. 320; excerpt: `raw/hegel-1821-philosophy-of-right-311-electors.md`; pointer: the Wikipedia article): "Of elections by means of many separate persons it may be observed that there is necessarily little desire to vote, because one vote has so slight an influence." and "Even when those who are entitled to vote are told how extremely valuable their privilege is, they do not vote." See [Hegel](../thinkers/hegel.md). (Condorcet 1793 is cited by the Wikipedia article via McLean & Hewitt 1994; not read.)
- **Anthony Downs** (1957) — the economic analysis the SEP names the paradox after; rational ignorance, ch. 13; voting as insurance, p. 257 (as reported by the SEP authors).
- **William Riker & Peter Ordeshook** (1968; Ordeshook 2006) — the calculus of voting and the duty term.
- **John Ferejohn & Morris Fiorina** (1974) — minimax regret; **Paul Meehl** (1977) is listed beside them by Edlin, Gelman & Kaplan (not read).
- **Geoffrey Brennan & Loren Lomasky** (1993) — expressive voting (via Brennan, SEP).
- **Donald Green & Ian Shapiro** (1994) — critique of rational-choice applications.
- **Alvin Goldman** (1999), **Richard Tuck** (2008) — causal responsibility (via Brennan, SEP). **Edlin, Gelman & Kaplan** (2007) — social preferences. **Levine & Palfrey** (2007) — laboratory tests.
- **Gerry Mackie** (2007, 2010 manuscripts) — duty surveys, "nonparadox" (via Brennan; Edlin et al.).
- **Alexander Guerrero** (2010) — mandate as kind of representation (via Brennan).
- **Jason Brennan** (SEP, 2016/2020) and **Tom Christiano & Sameer Bajaj** (SEP "Democracy") — encyclopedia authors; their assessments are marked as theirs above.

## Framings and reframings

- **Paradox of the theory, not of the voter.** Riker & Ordeshook: "Rather we are concerned with an apparent paradox in the theory." (1968).
- **Selfishness, not rationality, as the assumption at issue.** Edlin, Gelman & Kaplan argue that separating the two assumptions "reveals that (a) the act of voting can be rational" — see their p. 294; their summary: "Conversely, rational and purely selfish people should not vote."
- **Goals first.** Brennan: "What these alternative theories make clear is that whether voting is rational depends in part upon what the voters’ goals are." (§1.3).
- **Participation in democratic theory.** Christiano & Bajaj place the problem among the "criticisms Plato and Hobbes made" of mass participation (§4.1) and turn to elite, interest-group and deliberative responses (§4.2, not summarised here).

Left out: Downs 1957 and Riker & Ordeshook 1968 beyond what secondary sources and abstracts state (full texts not reached); the duty-to-vote debate (SEP §2 onward); Condorcet 1793 (not read).

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — see The question, last paragraph.
- [Validity](../vocabulary/validity.md) — the logic check.
- Expected utility, decisive (pivotal) vote, minimax regret, expressive voting — open work in [vocabulary](../vocabulary/index.md).

Related problems: [Arrow's impossibility theorem](arrows-impossibility-theorem.md)
(the Condorcet "paradox of voting", a different problem under the same name;
Morreau, SEP §1, as quoted there). Branch: [Problems](./index.md).
