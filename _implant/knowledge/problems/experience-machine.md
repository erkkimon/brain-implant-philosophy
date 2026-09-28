---
type: article
about: concept
title: "The experience machine"
description: "Would you plug into a machine that gives you any experiences you want, for life? Nozick (1974) says we would not, and that something matters besides how life feels from the inside — the case against hedonism about well-being; the hedonist replies (Silverstein, Crisp), the reversed machine and status quo bias (Kolber 1994, De Brigard 2010, Weijers 2014), the desire and objective-list alternatives, and the survey figures."
tags: [problem, ethics, well-being, hedonism]
timestamp: 2026-09-28T07:01:48Z
---

# The experience machine

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md), graded as in
[How claims are graded](../../conventions/how-claims-are-graded.md). Maps: Andrew Moore, [SEP Fall 2024
"Hedonism"](https://plato.stanford.edu/archives/fall2024/entries/hedonism/) (rev. 2013-10-17; excerpt:
`raw/sep-hedonism-fall-2024-experience-machine.md`); Roger Crisp, [SEP Fall 2024
"Well-Being"](https://plato.stanford.edu/archives/fall2024/entries/well-being/) (rev. 2021-09-15; excerpt:
`raw/sep-well-being-fall-2024-experience-machine.md`), who defends hedonism elsewhere (his entry lists
"Crisp (2006), which defend hedonism"); Lorenzo Buscicchi, [IEP "The Experience Machine"](https://web.archive.org/web/20260928011151/https://iep.utm.edu/experience-machine/) (undated;
excerpt: `raw/iep-experience-machine-buscicchi.md`). Their assessments are theirs and are marked so.

## The question

Nozick, *Anarchy, State, and Utopia* (1974, pp. 42–45; excerpt:
`raw/nozick-1974-anarchy-state-utopia-experience-machine.md`): "Suppose there were an experience machine that would give you any experience you desired."
"Superduper neuropsychologists could stimulate your brain so that you would think and feel you were writing a great novel, or making a friend, or reading an interesting book. All the time you would be floating in a tank, with electrodes attached to your brain."
The runs last "the next two years", with "ten minutes or ten hours out of the tank" between them;
"while in the tank you won't know that you're there"; "Others can also plug in to have the experiences they want, so there's no need to stay unplugged to serve them." (pp. 42–43).
Then: "Would you plug in? What else can matter to us, other than how our lives feel from the inside?" (p. 43).

**The 1989 restatement** (*The Examined Life*, pp. 104–5; not read here — as quoted by Buscicchi, IEP §1,
and Silverstein 2000, note 16): "Imagine a machine that could give you any experience (or sequence of experiences) you might desire."
"The question is not whether to try the machine temporarily, but whether to enter it for the rest of your life."
"Upon entering, you will not remember having done this; so no pleasures will get ruined by realizing they are machine-produced."
(Silverstein's text version reads "mined" for "ruined".) Buscicchi (§1): "In the 1974’s EMTE the plugging in is for two years, while in the 1989’s EMTE the plugging in is for life."

**Target.** Crisp (SEP §4.1) defines "‘prudential hedonism’, according to which well-being consists in the greatest balance of pleasure over pain",
and presents the machine as "a yet more weighty objection both to hedonism and to the view that well-being consists only in conscious states".
Buscicchi (§2): "the points being made against prudential hedonism by the EMTE equally apply to non-hedonistic mental state theories of well-being."
Moore (SEP §2.3.1) files it among non-necessity objections: "The objectors' claim is that there is something that is sufficient for value and that is missing from the life of perfect pleasure. If the objection stands then pleasure is not necessary for value."

**Two readings of the argument** (Buscicchi §4). Deductive: "if the vast majority of reasonable people value reality in addition to pleasure, then reality has intrinsic prudential value; therefore, prudential hedonism is false."
Abductive: "the best explanation for something intrinsically mattering to many people is something being intrinsically valuable."

**Logic check (this implant, 2026-09-27; logic, not a position).** Atoms: M = most reasonable people
value reality besides pleasure; R = reality has intrinsic prudential value; H = prudential hedonism.
`logic.py check --premises "M" "M -> R" "R -> ~H" --conclusion "~H"` printed `VALID`. Without the
bridge premise, `--premises "M" "R -> ~H" --conclusion "~H"` printed `INVALID` with counterexample
`H=T, M=T, R=F`. Since the first form is valid, rejecting ~H requires rejecting a premise; Buscicchi's
objection (§4) is to the step from M to R: "The main problem with this deductive argument consists in disregarding the is-ought dichotomy: knowing “what is” does not by itself entail knowing “what ought to be”."

## Why it matters

- **Theories of well-being.** Crisp (SEP §4.2): "The experience machine is one motivation for the adoption of a desire theory (for a good introduction to the view, see Heathwood 2016; 2019)."
  On the remaining contest, Crisp (§4.3, his assessment): "The best way to resolve this matter would consist, in large part at least, in returning once again to the experience machine objection, and seeking to discover whether that objection really stands."
- **Its reception.** Buscicchi (intro, his assessment): "In the last decades of the 20th century, an argument based on this thought experiment has been considered a knock-down objection to hedonism about well-being".
  He reports that Weijers (2014) "compiled a non-exhaustive list of twenty-eight scholars writing that the EMTE constitutes a successful refutation of prudential hedonism and mental state theories of well-being."
  Silverstein (2000, Introduction) names "James Griffin, David Brink, Stephen Darwall, and L.W. Sumner" as taking it "to be the definitive response to hedonism".
  Crisp (2006, p. 620): "Finally, while hedonism was down, Robert Nozick dealt it a near-fatal blow with his famous example of the experience machine."
- **Method.** Buscicchi (intro) links it to "the desirability of an experimental method in philosophy";
  "it has become particularly relevant with the technological developments of virtual reality."
- **Animals.** Nozick's section opens by asking whether utilitarianism is "at least adequate for animals"
  and ends: "Until one finds a satisfactory answer, and determines that this answer does not also apply to animals, one cannot reasonably claim that only the felt experiences of animals limit what we may do to them." (p. 45).
  See [the moral status of animals](moral-status-of-animals.md).

## Positions taken

Grouped by the threefold division of theories of well-being, which Crisp (SEP §4.3) calls
"standard in contemporary ethics (Parfit 1984: app. I)", plus the responses about the case itself, in the order
of Buscicchi's two phases (§12). Not ranked. For each: the case for, in its holders' words, and the
case against, in its critics'.

**1. The machine tells against hedonism and mental-state theories** (Nozick 1974 and those listed above).
*For:* Nozick's three reasons (pp. 43–44): "First, we want to do certain things, and not just have the experience of doing them."
"A second reason for not plugging in is that we want to be a certain way, to be a certain sort of person." "Plugging into the machine is a kind of suicide."
"Thirdly, plugging into an experience machine limits us to a man-made reality, to a world no deeper or more important than that which people can construct."
Conclusion (p. 44): "We learn that something matters to us in addition to experience by imagining an experience machine and then realizing that we would not use it."
Moore (§2.3.1) on the parallel schematic lives of Nozick (1971) and Nagel (1970): "hedonism is committed to the hedonic equality and thus the equal value of these lives."
*Against:* Silverstein (Nozick's Experience Machine): "But it is unclear how one arrives at this claim merely from the fact that we care about more than happiness."
Buscicchi's is-ought objection to the deductive reading (above). Crisp (SEP §4.1, his assessment): "Certainly the current trend of quickly dismissing hedonism on the basis of a quick run-through of the experience machine objection is not methodologically sound."

**2. It favours desire-satisfaction theories.** *For:* Crisp (SEP §4.2) reports the argument: "Take your desire to write a great novel. You may believe that this is what you are doing, but in fact it is just a hallucination. And what you want, the argument goes, is to write a great novel, not the experience of writing a great novel."
Buscicchi (§2): standard desire-satisfactionism "is usually thought to be immune from objections based on the EMTE".
*Against:* Buscicchi (§2): "given that a minority of people want to plug into the EM, these people’s lives, according to standard desire-satisfactionism, would be better inside the EM."
Crisp (§4.3) conditions his closing remark on the case "if desire theories are indeed mistaken in their reversal of the relation between desire and what is good".

**3. It favours objective-list theories.** Crisp (§4.3): "Objective list theories are usually understood as theories which list items constituting well-being that consist neither merely in pleasurable experience nor in desire-satisfaction. Such items might include, for example, knowledge or friendship."
*For:* Nozick's reasons name goods beyond experience; Moore (§2.3.1) reports Nozick "claiming that it is also good in itself “to do certain things, and not just have the experience [as if] of doing them”".
*Against:* the hedonist replies in 4, and Crisp's anhedonic life R (2006, p. 639), "as far as is possible like P’s, with all the enjoyment-and the suffering-stripped out": "Is it plausible to think that R’s life is of any valuefor her?" (spacing as in the scan)

**4. Hedonist and mental-statist replies.** Moore (§2.3.1) lists the families: the item "just is an instance of pleasure";
its value "is merely instrumental value"; or "there is also at least one sort of value (e.g., prudential value) for which pleasure is necessary."
- *Silverstein 2000* ([doi](https://doi.org/10.5840/soctheorpract200026225); excerpt:
  `raw/silverstein-2000-in-defense-of-happiness.md`) grants the isolation — "Nozick's argument does succeed, then, in isolating the fact that we care about more than our experiences" —
  then argues from desire formation: "We develop a desire to track reality because, in almost all cases, the connection to reality is conducive to happiness."
  "Thus, all of the evidence to which the experience machine argument appeals--all of our desires, including our desire to avoid the machine itself--ultimately points towards happiness as the source of prudential value. But that is precisely the doctrine of hedonism."
  *Against:* Buscicchi (§5): "Notice that Silverstein’s argument for the claim that pleasure-maximization alone explains the anti-hedonistic preferences depends on the truth of psychological hedonism—that is, the idea that our motivational system is exclusively directed at pleasure."
- *Crisp 2006* ([doi](https://doi.org/10.1111/j.1933-1592.2006.tb00551.x); excerpt:
  `raw/crisp-2006-hedonism-reconsidered-experience-machine.md`): "My conclusion will be that the ‘unkindness’ of recent ethics towards hedonism is not justified." (p. 620).
  His replies (pp. 636–639): accomplishment is usually enjoyed; the paradox of hedonism — "One version of the paradox of hedonism is that one will gain more enjoyment by trying to do something other than to enjoy oneself." (p. 637);
  values as products of history, which he says "throw that claim into some doubt" (p. 638). The same strategy in his SEP entry (§4.1, his assessment): "The strongest tack for hedonists to take is to accept the apparent force of the experience machine objection, but to insist that it rests on ‘common sense’ intuitions, the place in our lives of which may itself be justified by hedonism."
  *Against:* Crisp himself (2006, p. 636): "It is true that the intuitions of many of those who are inclined to reject hedonism when faced with the experience machine example will stand up to their own calm reflection."
  On the externalist variant he reports (SEP §4.1): "If the world can affect the very content of my experience without my being in a position to be aware of it, why should it not directly affect the value of my experience?"

**5. The intuition is biased, so the case does not decide** (Kolber 1994; De Brigard 2010; Weijers 2014).
- *Kolber 1994* (*Bard J. Soc. Sci.* 3: 10–17, [SSRN 1322059](https://ssrn.com/abstract=1322059); scan read, no DOI;
  excerpt: `raw/kolber-1994-mental-statism-experience-machine.md`) reverses the question; his "revised-EMQ" (p. 15) is "Would you get off of an experience machine to which you are already connected?";
  "Certainly, more people would stay on the machine than would agree to connect in the first place. This fact alone indicates that we may be biased in our response to the EMQ." (p. 15; no data offered);
  "In order for Nozick's argument to refute mental statism, it must go beyond affirmation of our status quo bias." (p. 16).
- *De Brigard 2010* ([doi](https://doi.org/10.1080/09515080903532290); excerpt:
  `raw/de-brigard-2010-if-you-like-it-status-quo.md`) tested a "backward-looking" machine: participants told they
  were plugged in by error choose "Remain connected" or "Go back to reality". Sample: "Participants were randomly assigned to one of three conditions, with 24 participants in each condition and each participant receiving only one vignette." (p. 46);
  "Participants were undergraduate students from UNC with no previous exposure to philosophy" (p. 47). Results: "For the Negative scenario, only 13% of the participants said to prefer reality; 87% of them would prefer to remain connected." (real life: "a prisoner in a maximum security prison");
  Positive (real life: "a multimillionaire artist living in Monaco"), 50% / 50%; "Finally, when assessing the Neutral scenario, 54% of the participants said they would like to go back to reality, whereas 46% would prefer to remain connected." (pp. 47–48).
  Follow-up: "I conducted a follow-up study with 80 participants, all undergraduates from UNC with no previous exposure to philosophy." (p. 49); "59% of participants wanted to remain connected, while only 41% wanted to disconnect." (p. 49).
  His reading (p. 53): "people may be choosing not to plug in to the experience machine because of their aversion to relinquish their status quo, and not—as Nozick and many others think—because they prefer to be ‘‘in contact with reality.’’" He credits Kolber in note 10 (p. 56).
- *Weijers 2014* ([doi](https://doi.org/10.1080/09515089.2012.757889); excerpt:
  `raw/weijers-2014-experience-machine-is-dead.md`), first-year students at Victoria University of Wellington, 2012
  (two marketing, two philosophy classes; no significant difference found between them, p. 531 note):
  Nozick's 1974 text, "about 16% (13/79) of the students indicated that they would connect" (p. 520); of main reasons for refusing, "34% (20/66)" showed "imaginative resistance" (p. 520);
  his "Stranger NSQ" case (a stranger who has spent half his life in a machine), "About 55% (42/77) of participants responding to the Stranger NSQ scenario thought Boris should connect to an experience machine" (p. 526).
  His conclusion for that case: "it does not provide strong evidence to refute or endorse them." (p. 513).
- *Against 5.* Buscicchi (§7, his assessment) says Weijers "avoided the main methodological flaws of De Brigard’s (2010), such as a small sample size and a lack of details on the conduct of the experiments";
  Weijers (p. 531 note) reports Smith (2011) on a disanalogy in De Brigard's scenarios and "concern with the representativeness of De Brigard’s all-student sample".
  Silverstein, before the experiments (Nozick's Experience Machine): "Even without these doubts, though, most of us continue to share Nozick's intuitions: we remain unwilling to accept a lifetime on the experience machine."
  Buscicchi (§9) reports the expertise objection — lay judgements "cannot be granted the same epistemic status as the judgements of philosophers" — and his own reply, citing Löhr (2018): "The current empirical evidence does not support granting an inferior epistemic status to the preferences of laypeople that inform the aforementioned studies on the EMTE."

**6. New-generation machines** (Buscicchi §11). *Crisp 2006* sets the choice aside — "Let me avoid the question whether we as individuals would plug in to such a machine" (p. 635) —
and compares P, who lives the accomplished life, with Q: "Q is connected to an experience machine from birth, and has experiences which are introspectively indiscernible from P’s" (p. 636);
"According to hedonism, P and Q have exactly the same level of well-being. And that is surely a claim from which most of us will recoil." (p. 636).
*Lin 2016* ([doi](https://doi.org/10.1017/s0953820815000424); not read), as Buscicchi reports: "we should consider the choice between two lives that are experientially identical but differently related to reality".
*Inglis 2021* (not read; Buscicchi): a pure-pleasure machine for every sentient being; "Only 5.3% of the subjects presented with this question replied positively." — "the first to be conducted in a Chinese university" (sample size not given in the IEP).
*Against:* Buscicchi (§11, his assessment) on Inglis: "the universality condition that, according to Inglis, is able to reduce biases descending from morality, might, on the contrary, work as a moral intuition pump."
His summary (§12): "Further scholarship is needed to establish whether and to what extent these new versions are able to resuscitate the EMTE and its goal."

**Surveys.** 2020 PhilPapers Survey, "All respondents" population (1785 respondents; excerpt:
`raw/philpapers-2020-survey-experience-machine-and-well-being.md`):
"Experience machine (would you enter?): yes or no?" — yes 13.34%, no 76.86%, other 9.81%, N = 1642;
"Well-being: hedonism/experientialism, desire satisfaction, or objective list?" — hedonism/experientialism 12.72%,
desire satisfaction 18.61%, objective list 53.15%, other 24.82%, N = 967 (inclusive accept-or-lean-towards
figures). Lay samples: see 5 (Weijers, De Brigard); Hindriks & Douven
([2018](https://doi.org/10.1080/09515089.2017.1406600); not read), as Buscicchi (§1, §10) reports: "71% of the subjects facing the succinct version of EMTE developed by Hindriks and Douven (2018) shared the pro-reality judgement",
and with an experience pill "an increase of pro-pleasure judgements from 29% to 53% was observed" (population and N not given in the IEP).

**Arithmetic check (this implant; arithmetic, not a position).** De Brigard's 13% of 24 is 3/24 =
12.5%, the count Weijers gives ("less than 13% (3/24)", p. 518). Weijers's Nozick-scenario 13/79 =
16.5%; Stranger NSQ 42/77 = 54.5%; difference 38.1 points, matching his "38%" (p. 527). His Self
scenario is printed as "About 34% (27/69)" (p. 521), but 27/69 = 39.1% and 27/79 = 34.2%; he reports
"79 survey sheets on the Self scenario" (p. 521), so the printed denominator and percentage disagree.

## Arguments in play

No argument pages yet. The case is an [argument](../vocabulary/argument.md) by thought experiment;
its two readings (deductive, abductive) and the logic check are under The question.

## Thinkers who addressed it

- **Plato**, *Philebus* 21a, as Moore (§2.3.1) reports: a life of pleasure alone would be "the life, not of a man, but of an oyster".
- **Nagel 1970, Nozick 1971** — schematic lives with "all the appearance but none of the reality" (Moore §2.3.1).
- **Nozick 1974**, *Anarchy, State, and Utopia* pp. 42–45 — the machine, the transformation and result machines; **1989**, *The Examined Life* pp. 104–106 (as Silverstein, notes 16–18, cites it) — the lifelong version.
- **Kolber 1994** — the revised (reversed) question; status quo bias.
- **Silverstein 2000** — desire conditioning; the intuitions point to hedonism.
- **Crisp 2006** — P and Q; hedonist replies; SEP "Well-Being" (rev. 2021).
- **De Brigard 2010** — backward-looking machine experiments.
- **Moore**, SEP "Hedonism" (rev. 2013) — the case as a non-necessity objection.
- **Weijers 2014** — survey experiments; the Stranger NSQ case.
- **Lin 2016; Hindriks & Douven 2018; Löhr 2018; Inglis 2021** — as reported by Buscicchi (IEP).
- **Buscicchi**, IEP (undated) — the two phases; is-ought objection to the deductive reading.
- Nozick also posed [Newcomb's problem](newcombs-problem.md) (1969).

## Framings and reframings

- **Choice versus value.** Crisp (SEP §4.1) asks both: "Would you plug in? Would it be wise, from the point of your own well-being, to do so?"
  Crisp (2006, p. 635) avoids the choice question because it "is likely to elicit answers influenced by contingent and differing attitudes each of us might have to risk."
- **Moral versus prudential.** Buscicchi (§6b): "By Nozick’s stipulation, only prudential judgements are at stake in this though experiment."
  He reports Weijers's participants answering "“I can’t because I have responsibilities to others”".
- **Isolation and stipulation.** Crisp (SEP §4.1) stipulates "there is no worry about its breaking down or whatever";
  De Brigard (p. 45) reports an informal class survey in which "60%" of refusers "gave reasons that had nothing to do with their preference for a real life over a virtual one" (N not given).
- **Machine versus pill.** Buscicchi (§10, his assessment): "Thus, the experience pill should be seen as an interesting but different thought experiment not to be compared with the EMTE."
- **Whether the first machine is spent.** Buscicchi (§12, his assessment): "Nevertheless, the necessity felt by anti-hedonistic scholars to devise a new generation of EMTE demonstrates that the first generation is dead."
  Weijers's title (2014): "Nozick’s experience machine is dead, long live the experience machine!"

Not covered, because not read: Nozick 1989 directly; Sumner 1996; Feldman 2011; Hewitt 2009; Smith 2011;
Bramble 2016; Rowland 2017; Lin 2016 and Inglis 2021 in their own texts.

## Vocabulary

- Well-being, prudential value, hedonism, mental statism, desire satisfaction, objective list, status
  quo bias — no pages yet; open work in [vocabulary](../vocabulary/index.md). Crisp's and Buscicchi's
  definitions are quoted under The question and Positions 3.
- [Argument](../vocabulary/argument.md), [validity](../vocabulary/validity.md) — the logic check.
- Related problems: [the moral status of animals](moral-status-of-animals.md) (Nozick's context);
  [the repugnant conclusion](repugnant-conclusion.md) and [the trolley problem](trolley-problem.md)
  (other cases argued from intuitions about imagined lives and choices). Branch: [Problems](./index.md).
