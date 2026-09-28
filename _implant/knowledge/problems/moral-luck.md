---
type: article
about: concept
title: "Moral luck"
description: "Can an agent be rightly judged for what depends on factors beyond their control? Kant's good will 'like a jewel', the Control Principle, Williams's Gauguin and lorry driver and Nagel's four kinds (resultant, circumstantial, constitutive, causal) from the 1976 symposium; denial (epistemic argument, Richards, Zimmerman's scope and degree), acceptance (Walker, Adams, Moore, Otsuka, Hartman), Rescher's incoherence reply, and two experimental studies."
tags: [problem, ethics, responsibility, free-will]
timestamp: 2026-09-28T07:01:48Z
---

# Moral luck

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md), graded as in
[How claims are graded](../../conventions/how-claims-are-graded.md). Map: Dana K. Nelkin, [SEP Fall 2024
"Moral Luck"](https://plato.stanford.edu/archives/fall2024/entries/moral-luck/) (rev. 2019-04-19;
excerpt: `raw/sep-moral-luck-fall-2024-nelkin-map.md`); her assessments are attributed to her.

## The question

Nelkin (preamble): "Moral luck occurs when an agent can be correctly treated as an object of moral judgment despite the fact that a significant aspect of what she is assessed for depends on factors beyond her control."
The conflict is with what she names the Control Principle (§1):

- "(CP) We are morally assessable only to the extent that what we are assessed for depends on factors under our control."
- "(CP-Corollary) Two people ought not to be morally assessed differently if the only other differences between them are due to factors beyond their control."

Nagel's definition (1979, pp. 203–204; excerpt: `raw/nagel-1979-mortal-questions-moral-luck-reprint.md`):
"Where a significant aspect of what someone" … "does depends on factors beyond his control, yet we continue to treat him in that respect as an object of moral judgment, it can be called moral luck."
Nagel (1979, p. 204): "If the condition of control is consistently applied, it threatens to erode most of the moral assessments we find it natural to make."
Williams (1993 "Postscript", as Nelkin quotes it): "when I first introduced the expression moral luck, I expected to suggest an oxymoron"
(see [oxymoron](../vocabulary/oxymoron.md)).

**The Kantian source.** Kant, *Groundwork* (1785), First Section, Ak. 4:394 per Nelkin §1, Abbott's
public-domain translation ([Gutenberg #5682](https://www.gutenberg.org/ebooks/5682); excerpt:
`raw/kant-1785-groundwork-4-394-good-will-jewel-abbott.md`): "A good will is good not because of what it performs or effects, not by its aptness for the attainment of some proposed end, but simply by virtue of the volition; that is, it is good in itself"; even without power to accomplish anything, "then, like a jewel, it would still shine by its own light, as a thing which has its whole value in itself. Its usefulness or fruitlessness can neither add nor take away anything from this value."
Nelkin (§1): "Thomas Nagel approvingly cites this passage in the opening of his 1979 article, “Moral Luck.” Nagel’s article began as a reply to Williams’ paper of the same name"
— the 1976 Aristotelian Society symposium ([doi:10.1093/aristoteliansupp/50.1.115](https://doi.org/10.1093/aristoteliansupp/50.1.115),
Williams pp. 115–135, Nagel pp. 137–151; excerpt: `raw/williams-nagel-1976-moral-luck-symposium.md`).

**Nagel's four kinds.** "Nagel identifies four kinds of luck in all: resultant, circumstantial, constitutive, and causal." (Nelkin §1). Nagel's own 1979 wording (p. 205):
"There are roughly four ways in which the natural objects of moral assessment are disturbingly subject to luck. One is the phenomenon of constitutive luck – the kind of person you are, where this is not just a question of what you deliberately do, but of your inclinations, capacities, and temperament. Another category is luck in one’s circumstances – the kind of problems and situations one faces. The other two have to do with the causes and effects of action: luck in how one is determined by antecedent circumstances, and luck in the way one’s actions and projects turn out."
Nelkin's labels and cases (§1):

| Kind | Nelkin's gloss | Case in the sources |
|---|---|---|
| Resultant | "Resultant luck is luck in the way things turn out." | Nagel 1979, p. 207: "If one negligently leaves the bath running with the baby in it, one will realize, as one bounds up the stairs towards the bathroom, that if the baby has drowned one has done something awful, whereas if it has not one has merely been careless." |
| Circumstantial | "Circumstantial luck is luck in the circumstances in which one finds oneself." | Nagel 1979, p. 203: "Someone who was an officer in a concentration camp might have led a quiet and harmless life if the Nazis had never come to power in Germany. And someone who led a quiet and harmless life in Argentina might have become an officer in a concentration camp if he had not left Germany for business reasons in 1930." |
| Constitutive | "Constitutive luck is luck in who one is, or in the traits and dispositions that one has." | Williams 1976, p. 116, names it and sets it aside: "This, the matter of what I have called “constitutive” luck, I shall leave entirely on one side." |
| Causal | "Finally, there is causal luck, or luck in “how one is determined by antecedent circumstances” (Nagel 1979, 60)." | "Nagel points out that the appearance of causal moral luck is essentially the classic problem of free will." |

Nelkin adds: "some have viewed the inclusion of the category of causal luck as redundant, since what it covers is completely captured by the combination of constitutive and circumstantial luck (Latus 2001)."

**Williams's cases (1976).** Williams (p. 117): "Let us take first an outline example of the creative artist who turns away from definite and pressing human claims on him in order to live a life in which, as he supposes, he can pursue his art."
"Without feeling that we are limited by any historical facts, let us call him Gauguin." Williams (p. 118): "I want to explore and uphold the claim that it is possible that in such a situation the only thing that will justify his choice will be success itself."
The lorry driver (p. 124), for Williams's "agent-regret": "The lorry driver who, through no fault of his, runs over a child, will feel differently from any spectator, even a spectator next to him in the cab, except perhaps to the extent that the spectator takes on the thought that he might have prevented it, an agent's thought."
"We feel sorry for the driver, but that sentiment co-exists with, indeed presupposes, that there is something special about his relation to this happening, something which cannot merely be eliminated by the consideration that it was not his fault."
His closing sentence (p. 134): "This is one way-only one of many-in which an agent's moral view of his life can depend on luck."

**Structural note** (the implant's, manifest [G4](../../vision/manifest.md)): the conflict as three
propositions. U: the difference between two agents is due to factors beyond their control. A: the
agents may be assessed differently. CP-Corollary gives U → ¬A. The judgment Nelkin describes for the
two would-be murderers (§1: "We certainly seem to be committed to the existence of moral luck.") gives
U and A together. `logic.py check --premises "U -> ~A" "U" "A" --conclusion "Z"` prints
`premises are jointly inconsistent — argument is vacuously valid`; `--premises "U -> ~A" "A"
--conclusion "~U"` prints `VALID`. Holding all three is inconsistent; the responses below differ
on which to give up, and for which kind of luck.

## Why it matters

- **Punishment and law.** Nelkin (§2.1): "The question of how resultant luck should affect punishment has been debated at least since Plato (The Laws IX, 876–877)."
  "H.L.A. Hart puts this conclusion in the form of a rhetorical question: “Why should the accidental fact that an intended harmful outcome has not occurred be a ground for punishing less a criminal who may be equally dangerous and equally wicked?” (1968, 129)."
  She reports: "Interestingly, however, the Model Penal Code takes a different approach for at least some offenses, prescribing the same punishment for attempts and completed crimes."
  See [The justification of punishment](justification-of-punishment.md).
- **Egalitarianism.** Nelkin (§2.2): "Inspired by the work of John Rawls, some egalitarians have invoked the idea that our constitution and circumstances are out of our control in the justification of their view."
  "Egalitarians who treat luck in this way are sometimes called “luck egalitarians.”"
- **Free will.** Nagel 1976 (p. 146): "A person can be morally responsible only for what he does; but what he does results from a great deal that he does not do; therefore he is not morally responsible for what he is and is not responsible for. (This is not a contradiction, but it is a paradox.)"
- **Epistemology.** Nagel 1979 (p. 204): "It resembles the situation in another area of philosophy, the theory of knowledge."
  Nelkin (§1): "Some recent work has instead taken moral luck to be a species of a larger genus of luck, of which there are other species, as well, such as epistemic luck"

## Positions taken

Grouped as Nelkin groups them (§4), not ranked: "There are three general approaches to responding to the problem of moral luck: (i) to deny that there is moral luck despite appearances, (ii) to accept the existence of moral luck while rejecting or restricting the Control Principle, or (iii) to argue that it is simply incoherent to accept or deny the existence of some type(s) of moral luck, so that with respect to at least the relevant types of moral luck, the problem of moral luck does not arise."
Nelkin (§5): "Most writers who have responded to the problem fall somewhere in between; either they explicitly take a mixed approach or they confine their arguments to a carefully delineated subset of types of moral luck while remaining uncommitted with respect to the others."

**1. Denial — no moral luck, appearances explained (§4.1.1).**
- *Epistemic argument.* "An important tool for those who wish to explain away the existence of moral luck is what Latus (2000) calls the “epistemic argument” (see Richards, Rescher, Rosebury, and Thomson)."
  Its core: "Because, according to the epistemic argument, we rarely know exactly what a person’s intentions are or the strength of her commitment to a course of action. One (admittedly fallible) indicator is whether she succeeds or not. In particular, if someone succeeds, that is some evidence that the person was seriously committed to carrying out a fully formed plan. The same evidence is not usually available when the plan is not carried out."
  Thomson (1993, as Nelkin quotes): "“Well do we regard Bert [a negligent driver who causes a death] with an indignation that would be out of place in respect to Carol [an equally negligent driver who does not]? Even after we have been told about how bad luck figured in his history and good luck in hers?” And Thomson answers: “I do not find it in myself to do so” (1993, 205)."
- *Richards* ([1986, *Mind* 95(378): 198–209](https://doi.org/10.1093/mind/xcv.378.198), not read): "Richards argues that we do judge people for what they would have done, but that what they do is often our strongest evidence for what they would have done. As a result, given our limited knowledge, we might not be entitled to treat the counterpart in the same way as the Nazi sympathizer, even though they are equally morally deserving of such treatment (Richards 1986, 174 ff.)."
- *Feelings, not judgments* (§4.1.1): "Those who adopt this strategy argue that it is understandable or even appropriate to feel differently about the driver who kills a child than about the one who does not. What is not appropriate is to offer different moral assessments of their behavior (e.g., Rosebury, Richards, Wolf, Thomson)." Nelkin presents Williams's agent-regret and lorry driver (above) in this context.
  "Wolf argues that there is a “nameless virtue” which consists in “taking responsibility for one’s actions and their consequences” (2001, 13)."
  "Henning Jensen (1984) argues that while both are equally culpable, there are consequentialist reasons for not subjecting the first negligent driver to the same degree of blame behavior."
- *Legal luck.* "A third strategy is to point out that we mistakenly infer moral luck from legal luck." — with reasons for the law such as "the balancing of deterrence and privacy (Rosebury 521–24)."
- *Agent causation* (causal luck): "The view is known as “Agent-Causal Libertarianism,” and the basic idea is that agents themselves cause actions or at least the formation of intentions, without their being caused to do so."
- *Zimmerman* ([2002, *J. Phil.* 99(11): 553ff.](https://doi.org/10.2307/3655750), not read): "Zimmerman begins where Richards leaves off, proposing to pursue “the implications of the denial of the relevance of luck to moral responsibility” to their “logical conclusion” (2002, 559)."
  "But, according to Zimmerman, we must distinguish between scope and degree of responsibility." Of the counterpart who never met the test: "He is responsible tout court even if he is not responsible for anything (2002, 565)."
  "Zimmerman concedes that “the role that luck plays in the determination of moral responsibility may not be entirely eliminable…” (2002, 575)."

*Case against denial, as reported.* Nelkin (§4.1.1) on the epistemic argument: "It is hard to see how the argument can be extended further to cover constitutive or causal luck."
Against Wolf: "For example, it has been argued against Wolf’s view, in particular, that once we acknowledge the appropriateness of greater self-blame in cases of greater harm, no good reason for denying moral luck remains, and indeed we have good reason for accepting it. (See Moore 2009, 31 ff.)"
Against Zimmerman: "A number of objections can be raised to Zimmerman’s view, including (i) that at least large classes of the counterfactuals in virtue of which he thinks people are responsible lack truth value (e.g., Adams 1977, Nelkin 2004, Zimmerman 2002, 572, and Zimmerman 2015), and (ii) that he is simply mistaken that one can be responsible without being responsible for anything."
"Hanna’s intuition is that Jenny is not as culpable as an actual Nazi collaborator, whereas it seems that Zimmerman, having all the counterfactuals in view for each of the two agents, has the opposite reaction."

**2. Denial of moral luck, with morality set aside for ethics (§4.1.2).** "But in the Postscript, Williams makes a distinction between morality and ethics that allows him to deny the existence of moral luck, thus preserving a certain integrity for morality."
"Instead, Williams suggests, we should care about ethics, where ethics is understood to address the most general question of how we ought to live."
Nelkin notes the other reading: "Many commentators have read Williams as advocating the position that moral luck exists and is deeply threatening to morality."
Nagel's 1976 objection to the original paper (p. 137): "Williams sidesteps the fascinating question raised in his paper." "He does not defend the possibility of moral luck against Kantian doubts, but instead redescribes the case which seems to be his strongest candidate in terms which have nothing to do with moral judgment."

**3. Acceptance (§4.2).** "All of those who accept the existence of some type of moral luck reject the Control Principle and the Kantian conception of morality that embraces it."
- *With revision of practice:* "Browne (1992), for example, suggests that if the Control Principle is false, we ought not to respond to an agent’s wrongdoing with anger and blame that is “against” him, but rather with anger that does not include hostility or the desire to punish."
- *Without much revision:* "Others suggest that the Control Principle does not have nearly the hold on us that Nagel and Williams assume, and that rejecting it would not change our practices in a significant way."
  "Margaret Urban Walker (1991) argues in this vein that moral luck is only problematic for a conception of moral agents as “noumenal” or pure (238)."
  "Adams (1985) adopts this strategy, drawing our attention to common practices, such as blaming people for their racist attitudes even if we do not think that such people are in control of their attitudes."
  "According to Moore, the best explanation of these reactive attitudes, such as guilt and resentment, is that their objects are genuinely more blameworthy."
  "Michael Otsuka offers yet another principle in place of the Control Principle: One is only blameworthy in cases in which one had the kind of control that would have allowed one to be entirely blameless."
  "For example, in the case of the two assassins, both are blameworthy, but, Otsuka argues, the one who hits and kills his target is more blameworthy."
- *Every kind or none:* "The main idea is that rejecting resultant luck, but not other sorts of luck, is an unstable position (e.g., Moore 1997 and Hartman 2017)." Nelkin: "In effect, this argument is Nagel’s argument in reverse."

*Case against acceptance, as reported.* On Walker: "Moral luck skeptics have material with which to question Walker’s claim. For example, those who deny resultant moral luck can still agree that agents have an obligation to minimize their risks of doing harm, and those who deny circumstantial moral luck can still agree that agents have an obligation to cultivate qualities that prepare them to act well in whatever circumstances arise."
"Sverdlik (1988) argues that it is not obvious how such a challenge can be met." On Otsuka: "Appealing to the distinction between scope and degree, one might grant that the reckless driver is, importantly, responsible for more things (including a death), but not more blameworthy."
On Hartman, one reply is "such as that offered by Rivera-López (2016), which claims that there is a principled difference resting on the need to make moral attributions at all."

**4. Incoherence (§4.3).** "According to this approach, it is simply incoherent to accept or deny the existence of some type(s) of moral luck. This approach has been used for constitutive luck in particular."
Rescher (1993, in Statman ed., not read): "Nicholas Rescher (1993), according to which “[o]ne cannot meaningfully said to be lucky in regard to who one is, but only with respect to what happens to one. Identity must precede luck” (155)."
*Against*, Nelkin: "It is easy to take Rescher’s point out of context without realizing that he is working with a notion of luck that differs from the notion of “lack of control.”"
"But it is less clear that there is anything odd—let alone incoherent—about saying that one’s identity is not a matter within one’s control."

**Nelkin's own assessments** (hers): on reactive attitudes versus reflection, "We seem to have something of a stalemate."; on Hartman's argument, "Thus, one way of seeing this argument is as a shift-the-burden one."; in §5, "The extreme positions are vulnerable to the objection that they have left some consideration or other completely unaccounted for." and "But those who occupy the middle also face a formidable challenge: where can one draw a principled line between acceptable and unacceptable forms of luck?"
No survey of philosophers' views on moral luck is recorded in the sources read.

## Arguments in play

- **Nagel's erosion argument** (1979, p. 204): "Ultimately, nothing or almost nothing about what a person does seems to be under his control."
  Why not drop the condition of control? Nagel: "What rules out this escape is that we are dealing not with a theoretical conjecture but with a philosophical problem."
  Nagel 1976 (p. 146): "The area of genuine agency, and therefore of legitimate moral judgment, seems to shrink under this scrutiny to an extensionless point."
- **Nagel's argument in reverse** (Moore 1997; Hartman 2017, pp. 105–07, per Nelkin §4.2.2.2): "Consider three agents who all form the intention and plan to carry out a murder. Each has a single opportunity to pull the trigger of a gun. Sneezy sneezes and so is unable to pull the trigger; Off-Target pulls the trigger, but the bullet is intercepted by a bird, and Bulls-Eye pulls the trigger and hits her target."
  Replies are reported under Positions (3).
- **Experimental studies.** Cushman 2008 ([*Cognition* 108(2): 353–380](https://doi.org/10.1016/j.cognition.2008.03.006);
  PubMed abstract only, full text not read; excerpt: `raw/moral-luck-bibliographic-records-and-study-abstracts.md`):
  "Judgments of the wrongness or permissibility of action were found to rely principally on the mental states of an agent, while judgments of blame and punishment are found to rely jointly on mental states and the causal connection of an agent to a harmful consequence."
  Kneer and Machery 2019 ([*Cognition* 182: 331–348](https://doi.org/10.1016/j.cognition.2018.09.003); abstract only): "First, in within-subjects experiments favorable to reflective deliberation, the vast majority of people judge a lucky and an unlucky agent as equally blameworthy, and their actions as equally wrong and permissible."
  "Third, in between-subjects experiments, outcome has an effect on all four types of moral judgments. This effect is mediated by negligence ascriptions and can ultimately be explained as due to differing probability ascriptions across cases."
  The abstracts give no sample sizes or participant populations, so no figures are given here. Nelkin (§4.2.2.2): "there would still be philosophical work to do to sort out what the normative facts are."
  Other empirical work she cites, not read: "For example, see Cushman and Green (2012), who offer an explanation of apparently conflicting intuitions about moral results luck in terms of two dissociable processes, and Björnsson and Persson (2012), who offer an explanation in terms of shifting explanatory perspectives."

## Thinkers who addressed it

- **Plato** — *Laws* IX, 876–877, on resultant luck and punishment (per Nelkin §2.1; not read here).
- **Kant** — *Groundwork* (1785) 4:394, the good will "like a jewel" (read, Abbott trans.).
- **Adam Smith** — *Theory of Moral Sentiments* (1790) II.iii.intro.3, as Nelkin quotes: "all praise or blame, all approbation or disapprobation, of any kind, which can justly be bestowed upon any action, must ultimately belong." (to "the intention or affection of the heart").
- **H. L. A. Hart** — 1968, p. 129, the question quoted above (per Nelkin).
- **[Bernard Williams](../thinkers/williams.md)** — "Moral Luck" (1976, pp. 115–135); "Postscript" (1993, in Statman ed.); Nelkin's bibliography also lists his *Moral Luck: Philosophical Papers 1973–1980* (1981).
- **Thomas Nagel** — reply (1976, pp. 137–151); "Moral Luck", *Mortal Questions* (1979), ch. 3.
- **Jensen** (1984), **Richards** (1986), **Adams** (1985), **Sverdlik** (1988), **Walker** (1991), **Browne** (1992),
  **Rescher**, **[Thomson](../thinkers/thomson.md)** (1993), **Rosebury** (1995), **Moore** (1997, 2009), **Latus** (2000, 2001), **Wolf** (2001),
  **Zimmerman** (2002), **Otsuka** (2009), **Rivera-López** (2016), **Hartman** (2017) — each as reported under Positions.
- **Cushman** (2008), **Kneer and Machery** (2019) — experimental work, from abstracts.

## Framings and reframings

- **A paradox without a solution.** Nagel 1976 (p. 139): "The view that moral luck is paradoxical is not a mistake, ethical or logical, but a perception of one of the ways in which the intuitively acceptable conditions of moral judgment threaten to undermine it all."
  Nagel 1976 (p. 148): "I believe that in a sense the problem has no solution, because something in the idea of agency is incompatible with actions being events, or people being things."
  And (p. 145): "Nevertheless, Kant's conclusion remains intuitively unacceptable. We may be persuaded that these moral judgments are irrational, but they reappear involuntarily as soon as the argument is over. This is the pattern throughout the subject."
- **Not about morality but about regret.** Nagel 1976 (p. 137) on Williams: "Williams misdescribes his result in the closing paragraph of the paper: he has argued not that an agent's moral view of his life can depend on luck but that ultimate regret is not immune to luck because ultimate regret need not be moral."
- **Ethics, not morality.** Williams's 1993 Postscript (position 2); Nelkin (§4.1.2) links it to Aristotle: "Hence, “the fragility of goodness” (Nussbaum)."
- **Luck as a wider genus.** Luck analysed without the contrast to control (Pritchard 2006, Coffman 2015, per Nelkin §1); Nelkin (§1) holds that "in order to engage in the debate as found in Kant and Nagel and many others, moral luck must be understood as in contrast to control."
- **Related pages** (a structural note, not a claim of the sources): [the trolley problem](trolley-problem.md), [moral dilemmas](moral-dilemmas.md), [dirty hands](dirty-hands.md), [the ticking bomb](ticking-bomb.md), [the justification of punishment](justification-of-punishment.md).

## Vocabulary

- [Oxymoron](../vocabulary/oxymoron.md) — Williams's word for the phrase (1993).
- [Paradox](../vocabulary/paradox.md) — Nagel's word for the problem (1976, pp. 139, 146).
- Control, responsibility (scope and degree), blameworthiness, agent-regret, resultant /
  circumstantial / constitutive / causal luck — open work in [vocabulary](../vocabulary/index.md).
  Branch: [Problems](./index.md).
