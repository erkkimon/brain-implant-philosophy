---
type: article
about: concept
title: "Kavka's toxin puzzle"
description: "A billionaire pays you a million dollars tomorrow morning if at midnight you intend to drink a toxin tomorrow afternoon; the drinking itself earns nothing. Can you form the intention, and would drinking be rational? Kavka (1983) on intentions as reason-based dispositions; Gauthier's and McClennen's resolute choice, Bratman's planning view, Mele, Levy's critique of the 'Rationalist Solution', rational irrationality (Parfit's case)."
tags: [problem, decision-theory, philosophy-of-action, intention, rationality]
timestamp: 2026-10-08T20:29:06Z
---

# Kavka's toxin puzzle

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
sources graded as in [How claims are graded](../../conventions/how-claims-are-graded.md).
Sources for the map: Kavka, [1983](https://doi.org/10.1093/analys/43.1.33) (excerpt: `raw/kavka-1983-the-toxin-puzzle.md`); Andreou, [SEP Fall 2024 "Dynamic Choice"](https://plato.stanford.edu/archives/fall2024/entries/dynamic-choice/) (excerpt: `raw/sep-dynamic-choice-fall-2024-toxin-puzzle-resoluteness.md`); Levy, [2009](https://doi.org/10.1111/j.1468-0114.2009.01340.x) (excerpt: `raw/levy-2009-rationalist-solution-toxin-puzzle.md`); abstracts and DOI-checked records in `raw/kavkas-toxin-puzzle-philpapers-abstracts-and-records.md`.
Selected as an entry of Wikipedia's List of paradoxes, [rev. 1376699902](https://en.wikipedia.org/w/index.php?oldid=1376699902), "Decision theory"; the Wikipedia article ([rev. 1343050941](https://en.wikipedia.org/w/index.php?oldid=1343050941)) was used only as a pointer to Kavka 1983, Gauthier 1994 and Levy 2009 (excerpt: `raw/wikipedia-kavkas-toxin-puzzle-rev-1343050941-and-list-entry.md`).

## The question

Kavka's case (1983): "The billionaire will pay you one million dollars tomorrow morning if, at midnight tonight, you intend to drink the toxin tomorrow afternoon." (p. 33).
The vial: "He places before you a vial of toxin that, if you drink it, will make you painfully ill for a day, but will not threaten your life or have any lasting effects." (p. 33).
"He emphasizes that you need not drink the toxin to receive the money; in fact, the money will already be in your bank account hours before the time for drinking it arrives, if you succeed." (pp. 33–34).
"You are perfectly free to change your mind after receiving the money and not drink the toxin." (p. 34).
A brain scanner whose verdict you do not doubt detects the intention (p. 34).

The plan of intending and then reneging fails on Kavka's account: "But if that is your plan, then it is obvious that you do not intend to drink the toxin. (At most you intend to intend to drink it.)" (p. 34).
Binding devices are excluded: "arrangement of such external incentives is ruled out, as are such alternative gimmicks as hiring a hypnotist to implant the intention, forgetting the main relevant facts of the situation, and so forth." (p. 34).
The puzzle as Kavka puts it: "You are asked to form a simple intention to perform an act that is well within your power." (p. 35), with an overwhelming incentive,
"Yet you cannot do so (or have extreme difficulty doing so) without resorting to exotic tricks involving hypnosis, hired killers, etc." (p. 35).

Two questions run through Andreou's and Levy's reconstructions: can the intention be formed, and would drinking, once paid, be rational? Levy's three routes to "I can intend":
"(8) that I can form the intention to drink the toxin; (9) that I can drink the toxin; or (10) that it is rational – i.e. that I have a sufficiently good reason, all things considered – to drink the toxin." (2009, p. 268).

**Label.** Kavka calls it a "puzzle" throughout; "paradoxes" appears in his paper only in the title of his 1978 article (1983, p. 36). Wikipedia's list files it under "Decision theory" among paradoxes, as the question "Can one intend to drink the non-deadly toxin, if the intention is the only thing needed to get the reward?" (rev. 1376699902).
Whether it is a [paradox](../vocabulary/paradox.md) in this implant's normative sense depends on the reconstruction; in Levy's form (below) the conclusions are ones he calls "counter-intuitive" (p. 268).

**Levy's reconstruction (2009, p. 268), propositional core.** (1) whether I win does not depend on tomorrow afternoon; (2) so I will have no good reason to drink; (3) I will have a substantial reason not to (pain); (4) I will recognise this tonight; (5) "I cannot intend to do what I (rightly) believe to be fundamentally irrational – i.e. something that I have no good reason to do and a (substantial) reason not to do"; (6) so I cannot form the intention; (7) so I cannot win.
Levy: "(6) and (7) are counter-intuitive. They both conflict with our intuition that I can form the intention – especially for $1m." (p. 268).

**Logic check (this implant, 2026-10-08; logic, not a position).** With Indep = (1), NoReason = (2), Pain = (3), Believes = I believe that drinking has no good reason and a substantial reason against it ((4)), CanIntend, Win: premises `Indep -> NoReason`, `Indep`, `Pain`, `(NoReason & Pain) -> Believes`, `Believes -> ~CanIntend`, `~CanIntend -> ~Win`, conclusion `~CanIntend & ~Win`: `logic.py` returns `VALID`.
Adding the Rationalist premises `RationalDrink` and `RationalDrink -> CanIntend` (Levy's (10) and (12)) to the first five, `logic.py` reports `premises are jointly inconsistent — argument is vacuously valid`: whoever accepts (10) and (12) must give up at least one of the five. Which one the Rationalist Solution gives up is Levy's report, not logic: "For the inference from (1) to (2) in Kavka’s Argument is invalid." (p. 271), while "But Gauthier also subscribes to step (5) in Kavka’s Argument, which holds that it is impossible to intend to perform an action that I know or believe to be fundamentally irrational." (p. 272).

## Why it matters

- **The nature of intention.** Kavka: "But intentions are better viewed as dispositions to act which are based on reasons to act - features of the act itself or its (possible) consequences that are valued by the agent." (p. 35); hence "you cannot intend to act as you have no reason to act, at least when you have substantial reasons not to act." (p. 35).
  His moral: "It also reveals that intentions are only partly volitional. One cannot intend whatever one wants to intend any more than one can believe whatever one wants to believe. As our beliefs are constrained by our evidence, so our intentions are constrained by our reasons for action." (p. 36).
- **Reasons to intend versus reasons to act.** "While you have no reasons to drink the toxin, you have every reason (or at least a million reasons) to intend to drink it." (p. 35); then "something has to give way: either rational action, rational intention, or aspects of the agent's own rationality" (p. 36). Mele (1992) states the stake: "If these questions are properly given an affirmative answer, at least one popular thesis in the philosophy of action is false." (abstract).
- **Dynamic choice.** Andreou: "In autonomous benefit cases, one benefits from forming a certain intention but not from carrying out the associated action." and "Among the most famous autonomous benefit cases is Gregory Kavka’s “toxin puzzle” (1983)." (SEP §1.5).
- **Deterrence.** Kavka: "I made some similar points in an earlier article ('Some Paradoxes of Deterrence', Journal of Philosophy, June 1978), but there I was discussing an example involving conditional intentions." (p. 36; [Kavka 1978](https://doi.org/10.2307/2025707)).
- **Cooperation and contractarianism.** Mintoff (1996) on Gauthier's claim about the [prisoner's dilemma](prisoners-dilemma.md): "However, the Paradox of Deterrence and the Toxin Puzzle seem to put this general type of claim into doubt." (abstract; [doi](https://doi.org/10.1080/00048409612347091)).
- **Further applications (as their abstracts state).** Theodicy: "I show that Kavka's toxin puzzle raises a problem for the “Responsibility Theodicy,”" (Pittard 2016, [doi](https://doi.org/10.1111/nous.12154)); epistemic dogmatism: "One lesson of the toxin puzzle is that ( ... ) it is irrational to intend to do that which you know will be irrational." (Beddor 2019, [doi](https://doi.org/10.1080/00048402.2018.1556309)).

## Positions taken

Grouped by the two questions; no position is ranked here. Andreou reports that "there is no widespread agreement that a plausible conception of rationality will imply that it is rational to drink the toxin." (SEP §2.4).
Levy, a critic of it, writes: "The Rationalist Solution is arguably the most popular approach to TP, at least in the philosophical literature." (p. 269); that is his assessment, not a survey.

- **The intention cannot (easily) be formed by a clear-sighted agent (Kavka).**
  Kavka 1983, pp. 35–36, quoted above. Andreou's gloss: "Presumably, one cannot form the intention to drink the toxin if one is confident that one will not drink it." (§1.5).
  Levy lists Bratman (1996; 1998a) and Farrell (1989) as appearing "to be sympathetic to Kavka’s Argument" (p. 283, n. 3).
  Later variants of the reasons-constraint, as their abstracts state them: Shah (2008): "reasons for intention are determined by reasons for action. Understanding this feature of practical deliberation thus allows us to solve the toxin puzzle."; Rudy-Hiller ([2019](https://doi.org/10.1080/13869795.2019.1656280)) ties intentions to reasons that "are motivating rather than normative reasons".
- **Resolute choice: drinking is rational, so the intention can be formed
  (Gauthier, McClennen).** Andreou: "Based on their own reasoning concerning rational resoluteness, Gauthier (1994) and McClennen (1990; 1997) argue that rational resoluteness can help an agent do well in autonomous benefit cases like the toxin case." and "They maintain that being rational is not a matter of always choosing the action that best serves one’s concerns. Rather it is a matter of acting in accordance with the deliberative procedure that best serves one’s concerns." (§2.4); "they see drinking the toxin in accordance with a prior plan to drink the toxin as rational, indeed as rationally required, given that one did well to adopt the plan" (§2.4).
  Works: Gauthier, ["Assure and Threaten"](https://doi.org/10.1086/293651), Ethics 104(4) 1994, and ["Rethinking the Toxin Puzzle"](https://doi.org/10.1017/cbo9780511527364.005) (1998); McClennen, [*Rationality and Dynamic Choice*](https://doi.org/10.1017/cbo9780511983979) (1990).
  Levy's name for the family: "The Rationalist Solution is best known in the literature as the theory of ‘resolute planning.’" (n. 7), owners as he lists them: Gauthier, Harman (1998), Holton (2004), McClennen (n. 6).
  The principle Levy reconstructs (RAP): "if it is rational for me to intend to A at future time t when I anticipate circumstances C at t, then, whatever my preferences at t, it is rational for me to A at t if C obtain at t" (pp. 271–272).
  Gauthier against a plan to intend and then change one's mind, as Levy reports it: "A course of action is a plan that I end up executing, an intention that ultimately results in the intended action. And I cannot coherently plan to go back on my present intention." (p. 276).
  - *Case against:* Andreou: "For those who find the idea that it is rational to drink the toxin completely counter-intuitive, its emergence figures as a problematic, rather than welcome, implication of Gauthier’s and McClennen’s views concerning rational resoluteness." (§2.4).
    The Anti-RAP Objection Levy states: "We simply cannot ‘bootstrap’ the rationality of a self-destructive act from the rationality of a self-benefiting intention." (p. 272); his conclusion: "For while I win $1m either way, changing my mind spares me the day of pain that following through would cost me." (p. 282). Mele (1996) is "largely a critique of a pair of recent responses to the puzzle that focus on the connection between rationally forming an intention to A and rationally A-ing, one by David Gauthier and the other by Edward McClennen." (abstract).
  - *Reply:* Lee ([2025](https://doi.org/10.1163/18756735-00000228)) aims "to defend the rationalist solution" against the objections that "Bratman argues that Gauthier’s account does not do justice to the temporal nature of the toxin scenario. And Levy objects that it depends on a problematic assumption that the rationality of a course of action transfers to its constituent action." (abstract).
- **Planning theory (Bratman).** Bratman, *Intention, Plans, and Practical Reason* (1987) and "Toxin, Temptation, and the Stability of Intention" ([1998](https://doi.org/10.1017/cbo9780511527364.006); reprinted [1999](https://doi.org/10.1017/cbo9780511625190.004)). Andreou: "In accordance with these proposed requirements, Bratman (1999) concludes that rationality at least sometimes calls for sticking to a plan even if this is not called for by one’s current preferences." and "So Bratman’s planning conception of rationality includes a “no-regret condition.”" (§2.4).
  On the toxin case specifically, Levy reports: "Bratman (1987, pp. 103–104) concludes from this argument that I have good reason not to intend to drink the toxin but only to cause myself to have the intention to drink the toxin, which he regards as different." (n. 14), and that Bratman "rejects RAP" (n. 20).
  Levy's assessment: "Bratman seems tacitly to assume throughout his discussions of TP that if it is rational for me to intend to A, then I can intend to A." (n. 6).
  Later shift, per Andreou: Bratman (2014; 2018) suggests there "may be “rational pressure” to change one’s current preferences" (§2.4).
- **Rational intention, irrational drinking (rational irrationality).**
  Levy holds the intention rational and the drinking not: "(24) is clearly controversial. Some philosophers, including myself, reject it." (p. 278), where (24) is "(24) If the Course is rational, then my drinking the toxin is also rational." He adds: "I agree with Holton (2004, p. 512), Kavka (1984, pp. 156–57), and Parfit (2001, pp. 91–92) that rational irrationality is possible." (n. 13); Parfit "ultimately rejects" RAP (n. 20).
- **Reasons to decide that are not reasons to act (Clarke).** "Here it is argued that ordinary agents in ordinary cases can have justifying reasons for deciding that are not and will not be justifying reasons for doing what, in making those decisions, they come to intend to do." (Clarke 2007, abstract, [doi](https://doi.org/10.1007/s11098-005-0929-1)).
- **Causal decision theory, reflexively (Spohn).** "The paper will show how one may rationalize one-boxing in Newcomb's problem and drinking the toxin in the Toxin puzzle within the confines of causal decision theory by ascending to so-called reflexive decision models" (Spohn 2012, abstract, [doi](https://doi.org/10.1007/s11229-011-0023-5)).

## Arguments in play

(none recorded as separate argument pages yet). Quoted above: Kavka's reasons-constraint (pp. 35–36) in Levy's seven-step form, checked as valid; RAP and the Anti-RAP Objection (Levy pp. 271–272); the Self-Promise Argument, which Levy rejects: "The Self-Promise Argument fails because my rational intention to drink the toxin construed as a self-promise imposes at most a practical, not a moral, obligation upon me to act in accord with it." (p. 282); and Gauthier's Rational Self-Interest Argument as Levy reconstructs it (pp. 275–276, steps (13)–(23)).

**Practical coping, not solutions (Andreou).** "Two strategies that we can sometimes use to solve (in the sense of practically deal with) dynamic choice problems are suggested in Kavka’s description of the toxin puzzle." (§2.1): gimmicks and external incentives, both excluded in Kavka's case. On the first, "the former strategy can be thought of as aiming at rationally-induced irrationality" (§2.1), and "A fanciful but clear illustration of this strategy is presented in Derek Parfit’s work (1984)." (§2.1) — the case Andreou recounts as "Schelling’s Answer to Armed Robbery" ([Parfit](../thinkers/parfit.md) 1984, 13). Of superstitious fear as a means, she writes: "Although this is not a solution to the toxin puzzle that one can consciously plan on using (nor is it one that resolves the theoretical issues raised by the case), it may nonetheless often help us effectively cope with toxin-type cases." (§2.1).

## Thinkers who addressed it

- **Gregory S. Kavka** (1978; 1983) — posed it. Origin: "The puzzle discussed here emerged from a conversation, some years ago, with Tyler Burge about 'Some Paradoxes of Deterrence'." (1983, p. 36, n. 1).
- **David Gauthier** (1994; 1998), **Edward McClennen** (1990; 1997) — resolute choice (Andreou §2.4); McClennen calls the choice an intra-personal "coordination problem" (Levy p. 269).
- **Michael Bratman** (1987; 1998/1999; 2014, 2018) — planning theory, no-regret condition; rejects RAP (Levy n. 20; Andreou §2.4).
- **[Derek Parfit](../thinkers/parfit.md)** (1984; 2001) — rejects RAP and holds rational irrationality possible, per Levy (nn. 13, 20); the armed-robbery case (Andreou §2.1).
- **Alfred Mele** (1992; 1995; 1996) — reasons to intend versus to act; critique of Gauthier and McClennen (abstracts).
- **Joe Mintoff** (1996) — a Bratman-based account of cooperation without "pointless toxin drinking" (abstract).
- **Gilbert Harman** (1998), **Richard Holton** (2004) — Rationalist Solution, per Levy (n. 6); **Ken Levy** (2009) — its critic.
- **Randolph Clarke** (2007), **Nishi Shah** (2008), **Wolfgang Spohn** (2012), **John Pittard** (2016), **Bob Beddor** (2019), **Fernando Rudy-Hiller** (2019), **Byeong D. Lee** (2025) — as above.

## Framings and reframings

- **An autonomous benefit case.** Andreou places it among the "challenging choice situations" of dynamic choice (§1.5); she reports "widespread agreement" on the self-torturer case but none on drinking the toxin (§2.4).
- **Newcomb.** Kavka's own text: "Remembering Newcomb's Problem, you seek inductive evidence that this is so, hoping that previous recipients of the billionaire's offer won the million when and only when they drank the toxin." (p. 35); the private investigator finds none. Spohn (2012) treats [Newcomb's problem](newcombs-problem.md) and the toxin together (abstract above); Andreou (2008) builds "The Newxin puzzle" from both ([doi](https://doi.org/10.1007/s11098-007-9131-y)).
- **Intention like belief.** Kavka's belief analogy (p. 36); Hieronymi (2006): "It turns out, perhaps surprisingly, that you can no more intend at will than believe at will." (abstract).
- **Three kinds of planner (McClennen's terms).** Levy: on Kavka's Argument the agent "cannot help but be sophisticated" (n. 2); resolute planning "is supposed to constitute a way around (or through) the false dichotomy between being ‘myopic’ and being ‘sophisticated.’" (n. 7) — "false" is the resolute theorists' claim as Levy reports it.

Left out: the Wikipedia article's pay-off tables and its four readings under "Paradox", which carry no source; the 1998 Coleman & Morris essays (Gauthier, Bratman, Harman) and Gauthier 1994 were not read in full text and are cited only as the sources above report them.

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — see The question (Label).
- [Validity](../vocabulary/validity.md) — the logic check above.
- [Dilemma](../vocabulary/dilemma.md) — Levy reports Kavka (1978, p. 295) calling the two options a "cruel dilemma" (p. 269).
- Intention, resolute choice, autonomous benefit, rational irrationality, RAP — open work in [vocabulary](../vocabulary/index.md).

Related problems: [Newcomb's problem](newcombs-problem.md) (Kavka p. 35; Spohn 2012), [the prisoner's dilemma](prisoners-dilemma.md) (Mintoff 1996).
Branch: [Problems](./index.md).

Related thinkers: [Parfit](../thinkers/parfit.md).
