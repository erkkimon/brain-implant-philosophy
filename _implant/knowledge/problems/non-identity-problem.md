---
type: article
about: concept
title: "The non-identity problem"
description: "If a choice changes who will exist, and those born have lives worth living, the choice seems worse for no one; is it then not wrong? Adams, Schwartz, Kavka and Parfit's cases (the 14-year-old girl, Depletion, the slave child), the person affecting intuition, and the responses: biting the bullet, impersonal principles and Theory X, rights and wronging without harming, non-comparative harm, identity and description, probabilities, and the agent's attitudes."
tags: [problem, ethics, population-ethics, future-generations]
timestamp: 2026-09-28T07:01:48Z
---

# The non-identity problem

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md), graded as in
[How claims are graded](../../conventions/how-claims-are-graded.md). Map: M. A. Roberts, [SEP Fall 2024
"The Nonidentity Problem"](https://plato.stanford.edu/archives/fall2024/entries/nonidentity-problem/)
(rev. 2024-07-19; excerpt: `raw/sep-nonidentity-problem-fall-2024-cases-and-responses.md`), who states
her own proposal there (§3.5); her assessments are hers. Primary texts read: Parfit 1984, ch. 16
(`raw/parfit-1984-reasons-and-persons-ch16-non-identity-problem.md`), Kavka 1982
(`raw/kavka-1982-paradox-of-future-individuals.md`), Schwartz 1978 (`raw/schwartz-1978-obligations-to-posterity.md`),
Adams 1979 (`raw/adams-1979-existence-self-interest-problem-of-evil.md`).

## The question

Parfit's case ([Reasons and Persons](https://doi.org/10.1093/019824908X.001.0001), 1984, §122; p. 358 per Roberts):
"This girl chooses to have a child. Because she is so young, she gives her child a bad start in life. Though this will have bad effects throughout this child’s life, his life will, predictably, be worth living. If this girl had waited for several years, she would have had a different child, to whom she would have given a better start in life."
Whether or not causing someone to exist can benefit them, Parfit writes: "On both views, this girl’s decision was not worse for her child."
He continues: "We cannot claim that this girl’s decision was worse for her child. What is the objection to her decision? This question arises because, in the different outcomes, different people would be born."

The same structure at social scale is **Depletion** (§123): "If we choose Depletion, the quality of life over the next two centuries would be slightly higher than it would have been if we had chosen Conservation. But it would later, for many centuries, be much lower than it would have been if we had chosen Conservation."
Because the policy changes who is conceived, "We know that, even if it greatly lowers the quality of life for several centuries, our choice will not be worse for anyone who ever lives."
Parfit's naming: "Our need to answer (1), and other similar questions, I call the Non-Identity Problem." — question (1) being "What is the moral reason not to choose Depletion?"

The factual premise is Parfit's "The Time-Dependence Claim: If any particular person had not been conceived when he was in fact conceived, it is in fact true that he would never have existed." (§119), and his illustration: "(It may help to think about this question: how many of us could truly claim, ‘Even if railways and motor cars had never been invented, I would still have been born’ ?)"
Roberts calls this "the phenomenon Gregory Kavka called the “precariousness” of existence (Kavka, 1982, 93): we all just barely missed never coming into existence at all."

The moral premise, per Roberts (§1): "The person affecting intuition itself was described by Derek Parfit as the idea that “what is bad must be bad for someone” (Parfit 1987, 363)."
Kavka's version is his "Obligation Principle: One can have an obligation to choose act or policy A rather than alternative B only if it is the case that if one chose B, some particular person would exist and be worse off than if one had chosen A." (p. 95).
A related slogan Roberts cites: agents are in favour of "making people happy" but "neutral" about "making happy people" (Narveson 1976, 73, via §1).

**Propositional skeleton (this implant, 2026-09-27; logic only, not a position).** Atoms: `wrong` (the choice is wrong),
`worse_for_future` (worse for someone it brings into existence), `worse_for_present` (worse for someone else),
`owes_existence`, `worth_living`. P1 `wrong -> (worse_for_future | worse_for_present)` (the person affecting
intuition / Obligation Principle); P2 `(owes_existence & worth_living) -> ~worse_for_future` (Parfit's "On both views" step);
P3 `owes_existence`; P4 `worth_living`; P5 `~worse_for_present` (Roberts's stipulation "that no one else is affected", preamble).
`logic.py check --premises P1 P2 P3 P4 P5 --conclusion ~wrong` prints `VALID`. Adding P6 `wrong` and asking for
`q & ~q` prints `VALID` / `premises are jointly inconsistent — argument is vacuously valid`. Dropping P1 from that set prints
`INVALID` (2 counterexample rows, `wrong=T, worse_for_future=F`); dropping P2 instead also prints `INVALID` (rows with
`worse_for_future=T`). P1–P5 with conclusion `wrong` prints `INVALID`, counterexample
`owes_existence=T, worse_for_future=F, worse_for_present=F, worth_living=T, wrong=F`. So the six claims cannot all
be held; each family of responses below gives up a different one. The form does not say which.

## Why it matters

- **Roberts's assessment** (preamble): "It today remains among the most challenging problems in all of population ethics."
- **Parfit's assessment** (§123): "Some people believe that this problem is a mere quibble. This reaction is unjustified. The problem arises because of superficial facts about our reproductive system. But, though it arises in a superficial way, it is a real problem."
- **Link to the repugnant conclusion.** Per Roberts (§1), dropping the person affecting intuition for the total theory leads to the [repugnant conclusion](repugnant-conclusion.md); she reports that Parfit's "repugnant" verdict "continues to be the dominant view in moral philosophy writ large, and the repugnant conclusion, together with the nonidentity problem, continues to define the basic contours of the contemporary controversy surrounding the person affecting intuition." The goal, per Roberts, is "to identify a “Theory X” (Parfit 1987, 378) that manages to avoid the nonidentity problem and the repugnant conclusion."
- **Other cases** (SEP §2): Kavka's slave child, which Roberts says arises "at a more local level"; wrongful life, where "a majority of courts have felt themselves forced to deny the child’s claim altogether" (§2.4); and reparations for historic injustices, where if reparations require that the claimant was harmed, "then we seem forced to conclude that reparations to later-conceived progeny are not owed." (§2.5).
- **Kavka's slave child** (p. 100): "In a society in which slavery is legal, a couple that is planning to have no children is offered $50,000 by a slaveholder to produce a child to be a slave to him. They want the money to buy a yacht." His assessment: "But acting in this manner is outrageous." (p. 101).

## Positions taken

**Origins.** Kavka (p. 93) speaks of "a surprising argument, discovered in-dependently by Robert M. Adams, Derek Parfit, and Thomas Schwartz,," (his n. 1 cites Adams 1979, Parfit 1976 and Schwartz 1978). Parfit's notes: "This problem has been called by Kavka The Paradox of Future Individuals. See KAVKA (4)."; "10 I follow ADAMS (3)."; "11 See T. Schwartz, Obligations to Posterity’, in SIKORA AND BARRY." Roberts: "By the 1980s, the nonidentity problem had become widely recognized."

1. **No obligation to distant posterity (Schwartz 1978).** Schwartz, [Obligations to Future Generations](https://stafforini.com/works/schwartz-1978-obligations-posterity/), p. 3: "The contrary claim rests on an identifiable fallacy." His conclusion (p. 13): "So those who would like our distant descendants to enjoy a clean, commodious, well-stocked world just may owe it to their like-minded contemporaries to contribute to these goals."
2. **Accept the conclusion ("bite the bullet").** Roberts (§3.1): "They “bite the bullet.”" Heyd: "David Heyd accepts that conclusion even in the case in which the existence that is brought about is less than worth having." For him the choice is "genethical and not the straightforwardly ethical: it’s neither morally permissible nor morally wrong." Boonin restricts it: "for Boonin, application of the person affecting intuition is restricted to those cases in which the life at issue isn’t “worse than no life at all” (Boonin 2014, 2, 14, 17)." (Gives up P6.)
3. **Impersonal principles (give up P1).** Parfit (§123): "Some believe that what is bad must be bad for someone. On this view, there is no objection to our choice." and "Certain writers accept this conclusion.* But it is very implausible." He proposes "The Same Number Quality Claim, or Q: If in either of two possible outcomes the same number of people would ever live, it would be worse if those who live are worse off, or have a lower quality of life, than those who would have lived." (§122), then: "Though Q is plausible, it does not solve the Non-Identity Problem. Q covers only the cases where, in the different outcomes, the same number of people would ever live." and "Call what we ought to accept Theory X." In §127: "We can predict that Theory X will not take a person-affecting form." Roberts reports total, average and critical-level theories (§3.2.1) and substitution principles such as Holtug's (§3.2.2); Parfit later proposed a "wide" "dual" principle (Parfit 2017, 154, via §3.2.2).
4. **Conservation grounded in the kind of society (Adams 1979).** Adams ([Noûs 13](https://doi.org/10.2307/2214795)): "But if their lives are worth living it would not have been better for them if we had followed a policy of fuel conservation. For they would not have existed in that case." Then: "If it followed further that there is nothing wrong with squandering the earth's resources, that consequence would discredit my argument. But it does not follow." and "The chief reason why we ought to conserve is to be found in the concern we ought to have about the kind of society to which our actions will lead in the future." (pp. 57–58).
5. **Wronging without harming (rights; Kavka, Woodward).** Kavka (pp. 96–97): "This argument, however, contains an error. It may sometimes be" / "possible to act wrongly by wronging someone without harming him." His principle concerns "a restricted life, a life that is significantly deficient in one or more of the major respects that generally make human lives valuable and worth living." (p. 105). Roberts: "one suggestion has been that what makes the choice under scrutiny wrong is that it violates the apparent victim’s right against being brought into a flawed existence (Woodward 1986; Elliot 1989; Elliot 1997; Smolkin 1999; Velleman 2008; Cohen 2009)." Woodward's analogy, via Roberts: the ticket agent case (Woodward 1986, 810–11, citing Adams), and "“What makes racial discrimination wrong is that it is unfair and that it stigmatizes … and a choice may have that character – and be wrong for that reason – regardless of how it affects [a person’s] other interests” (Woodward 1986, 811)." ([Woodward 1986](https://doi.org/10.1086/292801), not read.)
6. **Harm without being made worse off (Shiffrin, Harman).** Per Roberts (§3.3.2), Shiffrin's example: "if you are hit on the head by a gold bar dropped from the sky as a gift to you, you have been harmed even if you have been more than compensated for that harm in virtue of the fact that you are now own a gold bar (Shiffrin 1999, 120–135)." ([Shiffrin 1999](https://doi.org/10.1017/s1352325299052015), not read.) Harman: "On Harman’s view, that a choice imposes any of the listed conditions on the child is sufficient to establish that that choice harms the child whether or not the child has been made worse off (Harman 2004, 92–93 and 107; Harman 2009, 139)." (Reinterprets "worse for" in P1.)
7. **Identity and description (§3.4).** Hare's "“de dicto” harm" (Hare 2007, 512–23); a proposal that "challenges the metaphysical claims about cross-world identity that are inherent in the nonidentity problem" (gives up P3); Dasgupta's "many entities" view (Dasgupta 2018, 541–542; 550–554); Mulgan's rule consequentialism, whose "ideal code" condemns both choices: "Because the ideal code is violated by the depletion choice and the 14-year-old girl’s choice to have a child, both are declared wrong (Mulgan 2006, 155–56 and 204; Mulgan 2009)."; Bontly's "affects that person for the worse" test (Bontly 2016).
8. **Probabilities (Roberts's own proposal, §3.5).** "What that closer scrutiny shows is that the conclusion that the future person who is the subject of our concern has not been made worse off, or harmed (in the traditional, comparative sense of that term), by the choice under scrutiny is not one that we can validly reach." Of a child Harry: "What has been missed is that, under the agents’ original, wrong choice, Harry’s chances of existence, calculated as of the moment just prior to choice and limited just to information available to the agents at that moment, were also very, very small." (Gives up P2.) ([Roberts 2024](https://doi.org/10.1093/oso/9780197544143.001.0001), not read.)
9. **The agent's reasons and attitudes (§3.6).** Kumar's contractualist principles "“no one can reasonably reject”" (§3.6.1); "Finneron-Burns offers an alternative account of how Scanlon’s contractualism can be applied to solve the nonidentity problem." Of Wasserman's attitude-based view Roberts writes: "An implication of this view is that there need be nothing wrong in choosing to have a less happy rather than a happier child." (§3.6.2).

## Arguments in play

(No argument pages yet.) Each response has cited support and cited objections:

| response | for (cited) | against (cited) |
| --- | --- | --- |
| bite the bullet | Heyd, Boonin (§3.1) | "Not surprisingly, the “bite the bullet” strategy has encountered substantial resistance. See, e.g., Parfit 2017, 126–129."; Roberts: "Boonin’s deflationist suggestion seems to run counter, however, to our own lived experience, given that we – post-Parfit – feel strongly that we always have the relevant distinction clearly in mind but continue to consider the depletion choice wrong." |
| impersonal views | Parfit: "The great lowering of the quality of life must provide some moral reason not to choose Depletion. This is believed by most of those who consider cases of this kind." | Roberts: "But the average theory implausibly prohibits bringing even the very happy child into existence if it so happens that the people who are already in existence happen to be even happier (Parfit 1987, 420; Feldman 1995, 192–93)."; "Critical level utilitarianism struggles, however, in the face of what Arrhenius called the “sadistic conclusion.”"; total theory → [repugnant conclusion](repugnant-conclusion.md) |
| pluralism | Parfit 2017, 154 (dual principle) | Roberts: "It is not clear, however, that any of the forms of pluralism (radical or not) outlined above, as they now stand, make any significant headway in solving our population problems." |
| rights | Woodward 1986; Kavka pp. 96–97 | Parfit §124 on the man born to a 14-year-old mother: "But this man’s letter shows that he was glad to be alive." and "If we had claimed that her act was wrong, because he has a right that cannot be fulfilled, he could have said. ‘I waive this right’."; Roberts: "The second objection asks whether a rights-based or claims-based approach proves too much."; Persson 2009 on inconsistency (§3.3.1) |
| non-comparative harm | Shiffrin 1999; Harman 2004, 2009 | Roberts: "Objections to proposals that rely on non-comparative concepts of harm to solve the nonidentity problem focus on whether that concept itself can be clearly worked out."; Parfit on a "“morally relevant sense” (Parfit 1987, 374)"; Gardner 2015 |
| description / de dicto | Hare 2007; Reiman 2007 | the explanatory gap: "No “familiar moral principle” takes us from the shorthand claim to the assessment we are aiming to explain (Parfit 1987, 359; Wasserman 2008, 529–35; for discussion, see Weinberg 2008.)" |
| probabilities | Roberts 2024, 196–204 | "For criticism of the proposal outlined here, see Greene 2016; Smilansky 2017; Harney 2019." |

Parfit's own reply to the rights view (§124): "It would have been better if this man’s mother had waited. But this is not because of what she did to her actual child. It is because of what she could have done for any child that she could have had when she was mature."
and "We should expect that, as I have claimed, appealing to rights cannot wholly solve the Non-Identity Problem."
Parfit accepts the implication for the actual child: "I suggest that, on reflection, we can accept (3)." — (3) being that it would have been better if the child who existed had not been her actual child (§122).
Of Depletion and a medical case he writes: "In considering both cases, I accept the No-Difference View. So do many other people." (§125).

**Arithmetic check (this implant, 2026-09-27; mathematics, not a position).** Schwartz (p. 6) models the divergence of
populations under two policies by "(*) p(i) ≤ p(i−1)²", p(i) being the probability that a person born in generation i
under one policy would also exist under the other. He writes that if p(i) = .8, then p(i + 6) ≤ .0000005, and: "the chances of this happening six generations later are at most one in two million."
Iterating the bound six times gives p(i + 6) ≤ 0.8^(2^6) = 0.8^64; this implant's computation (Python, 2026-09-27) gives
0.8^64 ≈ 6.28 × 10⁻⁷ (about one in 1.59 million). The printed figure and the computed bound are both reported; the page
does not adjust either.

## Thinkers who addressed it

- **Robert M. Adams** (1979) — the non-identity point in a theodicy, then applied to fuel conservation.
- **Thomas Schwartz** (1978) — "Obligations to Posterity"; no obligation of widespread benefit to distant descendants.
- **Derek Parfit** (1976 per Kavka n. 1; 1984, ch. 16; 2017) — the name, the cases, Q, Theory X, the No-Difference View.
- **Gregory S. Kavka** (1982) — "The Paradox of Future Individuals"; the slave child; restricted lives. Journal issue Spring 1982; the scan prints "© 1981"; SEP's bibliography lists 1981.
- **James Woodward** (1986) — rights. **David Heyd** (1992, 2009) — genethics. **Seana Shiffrin** (1999), **Elizabeth Harman** (2004, 2009) — non-comparative harm.
- **Tim Mulgan** (2006, 2009); **Caspar Hare** (2007); **Nils Holtug** (2009, 2010); **David Boonin** (2014); **Thomas Bontly** (2016); **Rahul Kumar** (2018); **Shamik Dasgupta** (2018); **M. A. Roberts** (1998–2024).

## Framings and reframings

- **Kavka's framing as a paradox** (p. 95): "This argument poses a paradox. It moves by a correct route from plausible premises about biology, personal identity, and moral obliga-tion to a strongly counterintuitive conclusion."
- **Population policy** (Kavka p. 94, Schwartz pp. 3–4): the laissez-faire argument, "Thus, in doing so, we make no one worse off (than he otherwise would be) and hence do nothing wrong."
- **Theodicy** (Adams p. 53): "The first contribution is a proof that if our lives will have been worth living on the whole, we cannot have been injured by" the evils preceding our existence; "If it had not been for the First World War, for example, my par-ents would probably never have met and married, and I would not have been born." (p. 54).
- **The asymmetry** (SEP §4): "According to the asymmetry, it is wrong, and makes a future morally worse, to bring a miserable child – a child whose life is less than worth living – into existence but it is perfectly permissible, and does not make a future worse, to leave the happy child out of existence." Objection: "The objection is just this: the asymmetry is itself internally inconsistent."; reply: "Claims of an internal inconsistency, however, have been challenged."
- **Roberts's closing framing** (§5): "The reason the nonidentity problem is of such intense and continuing interest is that neither of those options seems even remotely plausible."
- **Related problems.** [Repugnant conclusion](repugnant-conclusion.md); [moral dilemmas](moral-dilemmas.md); [famine, affluence and morality](famine-affluence-and-morality.md).

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — Kavka's name, "The Paradox of Future Individuals".
- [Validity](../vocabulary/validity.md) — the skeleton above; Roberts's claim that the conclusion "is not one that we can validly reach".
- [Moral patient](../vocabulary/moral-patient.md) — whether merely possible people are owed anything.
- Person affecting intuition, Time-Dependence Claim, Theory X, Q, non-comparative harm, genethics, wrongful life —
  open work in [vocabulary](../vocabulary/index.md). Branch: [Problems](./index.md).
