---
type: article
about: concept
title: "The ethics of abortion (Thomson's violinist and the debate)"
description: "Is abortion morally permissible, and if so when? The conservative view (Noonan's criterion, Marquis's future like ours), the liberal personhood view (Warren's five criteria, Tooley's self-consciousness requirement), moderate and gradualist views, Thomson's violinist and bodily autonomy, Hursthouse's virtue-theoretic reframing, with each side's case and its critics' reply, and the 2020 PhilPapers survey figure."
tags: [problem, ethics, applied-ethics, bioethics]
timestamp: 2026-09-28T07:01:48Z
---

# The ethics of abortion (Thomson's violinist and the debate)

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md), graded as in
[How claims are graded](../../conventions/how-claims-are-graded.md). The Stanford Encyclopedia has no
"Abortion" entry (the Fall 2024 archive URLs `entries/abortion/` and `entries/ethics-abortion/`
returned 404 on 2026-09-27). Map: John-Stewart Gordon, [IEP "Abortion"](https://iep.utm.edu/abortion/)
([archived](http://web.archive.org/web/20260815153508/https://iep.utm.edu/abortion/); undated; excerpt:
`raw/iep-abortion-gordon-three-views-and-arguments.md`), who argues his own view there; his
assessments are his. Structural note (manifest [G4](../../vision/manifest.md)): the page names each
side with the words the cited authors use — Gordon's "opponents (anti-abortionists, pro-life
activists)" and "proponents (abortionists)" (§1a), Warren's "antiabortionist" and "proabortion",
Thomson's "opponents of abortion" — always attributed. Self-descriptions not found in a read
source are not used.

## The question

Gordon (§1): "Is there any morally relevant break along the biological process of development from the unicellular zygote to birth?"
He lists as candidates (abstract): "Leading candidates for the morally relevant point are: the onset of movement, consciousness, the ability to feel pain, and viability."
Two further questions are separated by the authors cited: whether the fetus's status settles the matter
(Thomson 1971 grants it personhood and asks what follows), and whether morality or law is at issue
(Hursthouse 1991, p. 234, discusses "the morality of abortion rather than the question of
permissible legislation"). The page treats the moral question; see *Framings* for the law.

Gordon's "standard argument" (§1b), a practical syllogism:
"The killing of human beings is prohibited." / "A fetus is a human being." / "The killing of fetuses is prohibited."
Warren (1973, ¶23) says "the term “human” has two distinct, but not often distinguished, senses" —
a "moral sense" and a "genetic sense" (¶24). Structural note: in propositional form, with one sense
(H) in both premises, and with the moral sense (Hm) in premise 1 and the genetic sense (Hg) in
premise 2, `python3 _implant/skills/tools/logic.py check` reports:

```
  P1: H -> W    [(H -> W)]
  P2: H    [H]
  C:  W    [W]

VALID
matches schema: modus ponens
```

```
  P1: Hm -> W    [(Hm -> W)]
  P2: Hg    [Hg]
  C:  W    [W]

INVALID
Counterexamples (premises true, conclusion false):
  Hg=T, Hm=F, W=F
  (1 counterexample row)
```

Which reading the premises need is disputed below; the tool checks form only.

## Why it matters

- **Moral status generally.** Jaworska & Tannenbaum, [SEP Fall 2024 "The Grounds of Moral Status"](https://plato.stanford.edu/archives/fall2024/entries/grounds-moral-status/)
  (rev. 2021-03-03, §1; excerpt: `raw/sep-grounds-moral-status-fall-2024-abortion-potentiality.md`):
  "Debates concerning abortion, stem cell research (see the entry on the ethics of stem cell research), and the question of what to do with unused frozen embryos from in vitro fertilization also rest on the theoretical question of the moral status of extremely underdeveloped human beings at various stages of development: zygote, embryo, and fetus (see section 5.2)."
- **Bioethics.** Gordon (§1) assesses: "One of the most important issues in biomedical ethics is the controversy surrounding abortion."
- **Infanticide, euthanasia, animals.** Tooley's and Warren's criteria are tested against newborns
  (positions 2 below); Marquis (1989, §II) says his account "does not entail, as sanctity of human
  life theories do, that active euthanasia is wrong" — see [Euthanasia](euthanasia.md); Tooley
  (1972, p. 51) asks why killing "an unborn member of the species Homo sapiens" should differ from
  killing "an unborn kitten" — see [The moral status of animals](moral-status-of-animals.md).
- **Duties to aid.** Thomson (1971, p. 62): "We have in fact to distinguish between two kinds of Samaritan: the Good Samaritan and what we might call the Minimally Decent Samaritan."
  Structural note: for how much aid morality requires, see also [Famine, affluence and morality](famine-affluence-and-morality.md) and the [demandingness objection](demandingness-objection.md).

## Positions taken

Grouped first as Gordon groups them (§1a: "There are three main views: first, the extreme conservative view (held by the Catholic Church); second, the extreme liberal view (held by Singer); and third, moderate views which lie between both extremes."),
then Thomson's bodily-autonomy argument, which Gordon treats separately (§3g). Not ranked. Each
has the case for, in its holders' words, and the case against, in its critics'.

**1. Conservative: wrong from conception, or with rare exceptions.** Gordon (§1a): "Some opponents (anti-abortionists, pro-life activists) holding the extreme view, argue that human personhood begins from the unicellular zygote"
— he names Schwarz 1990 (not read). Two grounds on record. *For (Noonan's criterion):* Noonan, [1968](https://doi.org/10.1093/ajj/13.1.134) ("Deciding Who Is
Human", *Natural Law Forum* 13; excerpt: `raw/noonan-1968-deciding-who-is-human.md`), p. 134:
"The argument I made is that it is wrong to kill humans, however poor, weak, defenseless, and lacking in opportunity to develop their potential they may be."
p. 137: "If their efforts are unsuccessful, the theologians' criterion is left in possession: Whoever is conceived of human beings is human."
His "buttressing" argument from probabilities (p. 136): "If a fetus is destroyed, one destroys a being already possessed of the genetic code, organs, and sensitivity to pain, and one which had an 80% chance of developing further into a baby outside the womb who, in time, would reason."
(Noonan's figures; his 1970 chapter "An Almost Absolute Value in History", [doi](https://doi.org/10.4159/harvard.9780674183032.c2), was not read.)
*For (Marquis's future like ours):* Marquis, [1989](https://doi.org/10.2307/2026961) (*J. Phil.*
86(4): 183–202; excerpt: `raw/marquis-1989-why-abortion-is-immoral-future-like-ours.md`), §II:
"The loss of one’s life deprives one of all the experiences, activities, projects, and enjoyments which would otherwise have constituted one’s future. Therefore, killing someone is wrong, primarily because the killing inflicts (one of) the greatest possible losses on the victim."
"The future of a standard fetus includes a set of experiences, projects, activities, and such which are identical with the futures of adult human beings and are identical with the futures of young children."
He says (§II) the argument "does not rely on the invalid inference that, since it is wrong to kill
persons, it is wrong to kill potential persons also", and (§V) that contraception is not covered
"because there is no nonarbitrarily identifiable subject of the loss".
*Against:* Warren (1973, ¶¶23–24) holds that the premise "it is wrong to kill innocent human beings"
is acceptable only in the moral sense of "human", and "fetuses are innocent human beings" only in the genetic sense. Tooley ([1972](http://www.jstor.org/stable/2264919), *Phil. & Pub. Aff.* 2(1): 37–65;
excerpt: `raw/tooley-1972-abortion-and-infanticide-self-consciousness.md`), p. 57: "the conservative position on abortion is acceptable only if the potentiality principle is sound";
p. 62: "One is therefore forced to conclude that the conservative's potentiality principle is false."
Gordon (§1a) assesses: "it seems implausible to say that the zygote is a human person", and reports
opponents' view (§3f) that "it is impossible to derive current rights from the potential ability of
having rights at a later time". The SEP (§5.2) reports Feinberg's analogy: "A potential US president has neither rights nor even a claim to command the military; likewise in the case of potentially cognitively sophisticated beings and the rights associated with moral status (Feinberg 1980, p.193)."
— which, it adds, "has been contested (Wilkins 1993, pp. 126–127 and Boonin 2003, pp. 46–49)". On
Marquis: Reitan ([2016](https://doi.org/10.1111/bioe.12211), abstract only; excerpt:
`raw/reitan-2016-marquis-future-like-ours-identity-and-contraception-objections.md`) names "the chief objections to FLO – the ‘identity objection’ and the ‘contraception objection’"
and argues that answering them needs a stand "on what is most essential to being the kind of entity
that an adult human being is"; the SEP (§5.2) reports McInerney 1990: "a fetus arguably lacks this sufficient connection" to the future person.

**2. Liberal: personhood as the criterion.** Gordon (§1a) names Singer (not read) for the view that
personhood "begins immediately after birth or a bit later".
*For:* Warren ([1973](https://doi.org/10.5840/monist197357133), *Monist* 57(1): 43–61; excerpt:
`raw/warren-1973-moral-and-legal-status-of-abortion-personhood.md`), ¶30, lists the traits "most
central to the concept of personhood": "1. consciousness (of objects and events external and/or internal to the being), and in particular the capacity to feel pain;"
"2. reasoning (the developed capacity to solve new and relatively complex problems);" "3. self-motivated activity (activity which is relatively independent of either genetic or direct external control);"
"4. the capacity to communicate, by whatever means, messages of an indefinite variety of types, that is, not just with an indefinite number of possible contents, but on indefinitely many possible topics;"
"5. the presence of self-concepts, and self-awareness, either individual or racial, or both." ¶32: "All we need to claim, to demonstrate that a fetus is not a person, is that any being which satisfies none of (1)-(5) is certainly not a person."
On potential (¶42): "the rights of any actual person invariably outweigh those of any potential person, whenever the two conflict."
Tooley (1972, p. 44): "An organism possesses a serious right to life only if it possesses the concept of a self as a continuing subject of experiences and other mental states, and believes that it is itself such a continuing entity."
*Against:* Warren states the objection herself (Postscript, 1982, ¶46): "it may appear to justify not
only abortion but infanticide as well"; her reply (¶47): "In this country, and in this period of history, the deliberate killing of viable newborns is virtually never justified."
Tooley accepts the implication (p. 63): "If so, infanticide during a time interval shortly after birth must be morally acceptable."
Marquis (1989, §II): "Personhood theories of the wrongness of killing, on the other hand, cannot straightforwardly account for the wrongness of killing infants and young children."
The SEP (§5.1): "A stock objection to Sophisticated Cognitive Capacities accounts is their underinclusiveness." "For example, infants lack sophisticated cognitive capacities, and so fail to meet this necessary condition for FMS."
Gordon (§1a) assesses: "it is not at all clear where the morally relevant difference is between the fetus five minutes before birth and a just born offspring".

**3. Moderate and gradualist views.** Gordon (§1a): "The proponents of the moderate views argue that there is a morally relevant break in the biological process of development – from the unicellular zygote to birth – which determines the justifiability and non-justifiability of having an abortion."
*For:* Gordon (§1a): "Some moderate views have commonsense plausibility especially when it is argued that there are significant differences between the developmental stages."
Hursthouse (1991, p. 238), within virtue theory: "Abortion for shallow reasons in the later stages is much more shocking than abortion for the same reasons in the early stages".
Thomson (1971, p. 47) is "inclined to think" the fetus "has already become a human person well before
birth", and (p. 66): "A very early abortion is surely not the killing of a person".
*Against:* Gordon (§1a): "The fact that they also claim for a break in the biological process, which is morally relevant, seems to be a relapse into old and unjustified habits."
The line-drawing worry, as Thomson reports it (p. 47): to "choose a point in this development"
is said "to make an arbitrary choice"; Tooley (p. 38) sets the liberal the task of "specifying a
cutoff point which is not arbitrary"; Noonan (p. 136), for conception: "One evidence of the nonarbitrary character of the line drawn is the difference of probabilities on either side of it."

**4. Bodily autonomy: permissible even if the fetus is a person (Thomson).** Thomson
([1971](http://links.jstor.org/sici?sici=0048-3915%28197123%291%3A1%3C47%3AADOA%3E2.0.CO%3B2-G),
*Phil. & Pub. Aff.* 1(1): 47–66; excerpt: `raw/thomson-1971-defense-of-abortion-violinist.md`),
p. 48: "I propose, then, that we grant that the fetus is a person from the moment of conception."
*For:* the violinist (pp. 48–49): "You wake up in the morning and find yourself back to back in bed with an unconscious violinist. A famous unconscious violinist. He has been found to have a fatal kidney ailment, and the Society of Music Lovers has canvassed all the available medical records and found that you alone have the right blood type to help."
"To unplug you would be to kill him. But never mind, it's only for nine months. By then he will have recovered from his ailment, and can safely be unplugged from you."
"Is it morally incumbent on you to accede to this situation? No doubt it would be very nice of you if you did, a great kindness."
Her two theses: "the fact that for continued life that violinist needs the continued use of your kidneys does not establish that he has a right to be given the continued use of your kidneys" (p. 55);
"the right to life consists not in the right not to be killed, but rather in the right not to be killed unjustly." (p. 57).
And (p. 63): "it is not morally required of anyone that he give long stretches of his life—nine years or nine months—to sustaining the life of a person who has no special right (we were leaving open the possibility of this) to demand it."
Thomson limits it herself (pp. 65–66): "I am inclined to think it a merit of my account precisely that it does not give a general yes or a general no."
She calls a seventh-month abortion "just to avoid the nuisance of postponing a trip abroad" indecent,
and writes (p. 66): "I am not arguing for the right to secure the death of the unborn child."
*Against:* Warren (1973, ¶13): "for it is only in the case of pregnancy due to rape that the woman’s situation is adequately analogous to the violinist case for our intuitions about the latter to transfer convincingly."
¶14: "Consequently, there is room for the antiabortionist to argue that in the normal case of unwanted pregnancy a woman has, by her own actions, assumed responsibility of the fetus."
Thomson's own answer to the voluntary case (people-seeds, p. 59) concedes "at most that there are some cases in which the unborn person has a right to the use of its mother's body, and therefore some cases in which abortion is unjust killing."
Structural note: Marquis (1989, opening) states that he "will assume, but not argue" that permissibility "stands or falls on whether or not a fetus is the sort of being whose life it is seriously wrong to end".

**Survey.** 2020 PhilPapers Survey, population "All respondents" (the survey's respondents; excerpt:
`raw/philpapers-2020-survey-abortion.md`): "Abortion (first trimester, no special circumstances): permissible or impermissible? Accept or lean towards: permissible 81.73% (81.37%) Accept or lean towards: impermissible 13.10% (12.83%) Other 5.79% N = 1122, excluding skipped & insufficiently familiar (58 respondents)"
(inclusive percentages, exclusive in brackets, per the page legend). It measures respondents' views
on that wording, not the general public; no public-opinion poll was read for this page.

## Arguments in play

No argument pages yet. On record: the standard argument and the equivocation charge (above, with the
tool output); the future-like-ours argument (Marquis 1989, §II); the potentiality principle
(Tooley 1972, p. 56, "critical to the conservative's defense") and the potentiality argument, which
Gordon (abstract) calls "The most important argument with regard to this conflict"; the violinist
analogy (Thomson 1971); the infanticide objection (Warren 1982 postscript; Tooley 1972, p. 63).

## Thinkers who addressed it

- **Noonan, 1968** (1970 chapter not read) — conservative; "Whoever is conceived of human beings is human" (1968, p. 137).
- **[Thomson, 1971](../thinkers/thomson.md)** — grants personhood for argument's sake; the violinist; Samaritans (pp. 47–66).
- **Tooley, 1972** — self-consciousness requirement; against the potentiality principle (pp. 44, 56–62).
- **Warren, 1973 (postscript 1982)** — five criteria of personhood; potential; infanticide (¶¶30–47).
- **Marquis, 1989** — future like ours; abortion "in the same moral category as killing an innocent adult human being" (opening).
- **Hursthouse, 1991** — virtue theory; rights and fetal status set aside (pp. 234–240).
- **Gordon, IEP (undated)** — three views; his own "pragmatic account" (§5).
- **Reitan, 2016** — identity and contraception objections to Marquis (abstract).
- Named by the sources, not read here: Singer, Feinberg (1980), English (1984), Schwarz (1990), McInerney (1990), Boonin (2003).

## Framings and reframings

- **Virtue theory (Hursthouse 1991;** excerpt: `raw/hursthouse-1991-virtue-theory-and-abortion.md`; [JSTOR](http://www.jstor.org/stable/2265432)). p. 234: "virtue theory quite transforms the discussion of abortion by dismissing the two familiar dominating considerations as, in a way, fundamentally irrelevant."
  p. 235: "So whether women have a moral right to terminate their pregnancies is irrelevant within virtue theory, for it is irrelevant to the question “In having an abortion in these circumstances, would the agent be acting virtuously or viciously or neither?”"
  p. 236: "that the status of the fetus—that issue over which so much ink has been spilt—is, according to virtue theory, simply not relevant to the rightness or wrongness of abortion (within, that is, a secular morality)."
  p. 237: "These facts make it obvious that pregnancy is not just one among many other physical conditions; and hence that anyone who genuinely believes that an abortion is comparable to a haircut or an appendectomy is mistaken."
  She adds (p. 238): "Although I say that the facts make this obvious, I know that this is one of my tendentious points."
  And (p. 239): "When women are in very poor physical health, or worn out from childbearing, or forced to do very physically demanding jobs, then they cannot be described as self-indulgent, callous, irresponsible, or light-minded if they seek abortions mainly with a view to avoiding pregnancy as the physical condition that it is."
  The general criticism she states and rejects (p. 230): "Virtue theory can't get us anywhere in real moral issues because it's bound to be all assertion and no argument."
- **Reasons, not stages (Gordon, §5).** "According to this account, one has to examine the different kinds of reasons for abortion in a particular case to decide about the reasonableness of the justification given."
- **Personhood sidestepped.** Reitan (abstract): "One reason for the persistent appeal of Don Marquis' ‘future like ours’ argument (FLO) is that it seems to offer a way to approach the debate about the morality of abortion while sidestepping the difficult task of establishing whether the fetus is a person."
  Thomson instead grants the premise for the sake of argument (p. 48, quoted in position 4).
- **Morality vs. law.** Hursthouse (p. 234) and Thomson ("we are not here concerned with the law",
  p. 63) separate the two. Legal history (court rulings, statutes) is left out: no read source on
  this page reports it.
- **Related cases.** [Trolley problem](trolley-problem.md); [Moral dilemmas](moral-dilemmas.md); [Non-identity problem](non-identity-problem.md).

## Vocabulary

- [Moral patient](../vocabulary/moral-patient.md) — whose interests count; "full moral status" (FMS) in the SEP's usage.
- Person (Warren's moral sense of "human", ¶24) vs. human being (genetic sense); potential person; viability — open work in [vocabulary](../vocabulary/index.md). [Dilemma](../vocabulary/dilemma.md). Branch: [Problems](./index.md).
