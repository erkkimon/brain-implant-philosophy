---
type: article
about: concept
title: "The demandingness objection: can morality require too much?"
description: "Does a moral theory that requires you always to do the most good, whatever the cost to you, demand too much, and is that a reason to reject it? Williams's integrity objection, Scheffler's agent-centred prerogative, Kagan's defence of the demands, satisficing (Slote), Murphy's co-operative principle, Hooker's rule-consequentialism, Mulgan, and Sobel's reply that the objection presupposes what it opposes."
tags: [problem, ethics, consequentialism]
timestamp: 2026-10-08T19:18:49Z
---

# The demandingness objection

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md), graded as in
[How claims are graded](../../conventions/how-claims-are-graded.md). Map: Thomas Hurka, [SEP Fall 2024
"Moral Demands and Permissions/Prerogatives"](https://plato.stanford.edu/archives/fall2024/entries/moral-demands-permissions/)
(first published 2024-06-27; excerpt: `raw/sep-moral-demands-permissions-fall-2024-demandingness-objection.md`),
who assesses several proposals in his own voice; those assessments are his. Also Walter Sinnott-Armstrong,
[SEP Fall 2024 "Consequentialism"](https://plato.stanford.edu/archives/fall2024/entries/consequentialism/) §6
(rev. 2023-10-04; `raw/sep-consequentialism-fall-2024-limiting-demands.md`); Brad Hooker,
[SEP Fall 2024 "Rule Consequentialism"](https://plato.stanford.edu/archives/fall2024/entries/consequentialism-rule/)
(rev. 2023-01-15; `raw/sep-consequentialism-rule-fall-2024-demandingness.md`); Chappell and Smyth,
[SEP Fall 2024 "Bernard Williams"](https://plato.stanford.edu/archives/fall2024/entries/williams-bernard/) §4
(`raw/sep-williams-bernard-fall-2024-integrity-objection.md`). Works not read are cited as these entries
report them; registry records in `raw/demandingness-objection-bibliographic-records.md`.

## The question

Hurka (§1): "Standard consequentialist moral views, which say the right act is always the one that will result in the most good impartially considered, face two main objections (Kagan 1989)."
One says they permit too much; "The other objection says these views demand too much. They say you must always do what will produce the best outcome, regardless of the cost to you."
On giving to famine relief: "But consequentialism says you must keep giving as long as the benefit to them is greater than the cost to you, which can be until you’ve reduced yourself to their welfare level (Singer 1972: 241)."
And: "For consequentialism there is no moral time off and no sacrifice you can’t be required to make. Its demands, the second objection says, are unreasonably strong."

Sinnott-Armstrong's statement (§6): "Another popular charge is that classic utilitarianism demands too much, because it requires us to do acts that are or should be moral options (neither obligatory nor forbidden). (Scheffler 1982)"
His example is a $100 pair of shoes against a $100 donation that would save a life; he
concludes: "The requirement to maximize utility, thus, strikes many people as too demanding because it interferes with the personal decisions that most of us feel should be left up to the individual."
Hooker (§5) says the same of the maximising criterion: "Thus, the maximising act-consequentialist criterion of wrongness is often accused of being unreasonably demanding."

Hurka's definition (§8): "A moral view is demanding if it requires you, as part of acting rightly, to make large sacrifices or forgo large benefits for yourself."
The objection is not confined to consequentialism. Of W. D. Ross's view (which requires
promoting the most good wherever no negative duty is violated), Hurka writes: "Non-consequentialist views can therefore also be very demanding, making acts of maximizing the good obligatory that many see as merely supererogatory."
Negative duties raise a parallel question (§7): "The question here is whether negative duties too can, in their different way, be excessively demanding."

**Structure (this implant, 2026-09-27; logic, not a position).** With T = "the theory is
correct" and R = "the theory's demands (as described above) are morally required", the
objection has the form T → R, ¬R ⊢ ¬T. `logic.py check --premises "T -> R" "~R" --conclusion "~T"`
returns "VALID" and "matches schema: modus tollens". The form is valid; the replies below
can be sorted (a structural note, not a source's grouping) by what they dispute: T → R
(Hurka's group A below), ¬R (group B), or, in Sobel's (2007) framing below, whether ¬R can be
held independently of ¬T; groups C and D replace T with a less demanding theory.

## Why it matters

- **Famine relief and aid.** Hurka (§2) traces one line of defence of strong demands to
  Singer's drowning-child case: "A different version appeals to intuitions about particular cases (e.g., Singer 1972; Unger 1996). It first describes a case where benefiting others seems uncontroversially required, most famously one of Peter Singer’s where you can save a child from drowning in a pond at the cost of dirtying your clothes (1972: 231)."
  See [Famine, affluence and morality](famine-affluence-and-morality.md).
- **The shape of morality.** Hurka (§1): "There is, then, a distinctive and important issue about how demanding morality is or should be taken to be."
  Sinnott-Armstrong (§6): "If we were required to maximize utility, then we would have to make very different choices in many areas of our lives."
- **Supererogation.** Hurka (§1) reports that consequentialism "makes no distinction between
  what is morally required and what, though admirable and good, is beyond duty or
  supererogatory"; how to restore that distinction is the topic of §§4–5 of his entry.
- **Everyday morality.** Hurka (§2): "Arguments for a strong duty to promote the good, whether maximizing or somewhat weaker, are revisionist of everyday morality."

## Positions taken

Hurka's grouping (§§2–5): resist the objection (deny the view is that demanding, or accept
the demands), weaken the duty to promote the good, or supplement it with a competing factor.
Sinnott-Armstrong (§6) lists overlapping responses. No survey figures on this question are
held (none recorded).

**A. Resist: the view is less demanding in practice.**
1. *Local focus.* "(e.g., Sidgwick 1907: 430–39). This, they say, makes their view not in practice that demanding." (Hurka §2)
   Hurka's assessment: "But though it contains some truth, this argument hardly meets all the objection."
2. *Indirect or two-level consequentialism* (Bales 1971; Hare 1981; Parfit 1984, per Hurka §2).
   Against: "Even if the rule with the best consequences demands less than full maximization, it may still be considerably more demanding than those concerned about demandingness will find plausible (Mulgan 2001: 44)."
   And: "Both allow that objectively, or relative to the facts, any act that fails to maximize the good is wrong, and objectors may still find that unacceptable."
3. *Wrong but blameless.* "A possible response distinguishes between what’s wrong and what you can be blamed for." (Hurka §2, citing Arneson 2004, 2009.)
   Against (Hurka §2): "But the objectors can again deny that this meets their point, which isn’t just about what morality says you can be blamed for but also about what it says you must, objectively, do."
   Sinnott-Armstrong (§6) reports Mill's version: "John Stuart Mill, for example, argued that an act is morally wrong only when both it fails to maximize utility and its agent is liable to punishment for the failure (Mill 1861)."

**B. Resist: the demands are legitimate.**
4. *The failing is ours.* Hurka (§2): "If we don’t always do what results in the most good, it says, that’s a failing in us rather than in the moral view that requires us to do more; if we think we’re sometimes permitted not to maximize the good, we’re mistaken."
   He adds a version from Wilson 1993: "In fact, those who urge such a permission may just be trying to justify retaining their privileged social position (Wilson 1993)."
5. *Kagan 1989.* "A more theoretical version of this reply says, first, that all views recognize a duty to promote the good impartially as at least one element in morality, and then argues that none of the revisions or additions needed to generate a less demanding view can be justified (Kagan 1989)."
   Hurka's comment: "This assumes, perhaps controversially, that the revisions need further justification and are unacceptable without one."
   Sinnott-Armstrong (§6) groups Kagan 1989, Singer 1993 and Unger 1996 as utilitarians who hold "we really are morally required to change our lives so as to do a lot more to increase overall utility"; "Such hard-liners claim that most of what most people do is morally wrong, because most people rarely maximize utility."
6. *Case-based (Singer 1972; Unger 1996).* The pond argument above. Hurka: "As Singer recognizes, a defence starting from his pond case can’t support a duty as strong as the fully maximizing one he himself prefers."
   For the case: "Those who defend a strong duty of aid deny that these differences, either individually or together, are morally significant (e.g., Singer 1972; Unger 1996; Kagan 1998: 134–35; Pummer 2023: 99–125); thus, they deny that this duty is weakened by physical distance (contrast Kamm 2000)."
   Against: "Others argue that one or more of the differences do weaken the duty (e.g., Woollard 2015: 129–43). More specifically, they argue that the pond case invokes a duty of immediate or emergency rescue that’s distinct from, and stronger than, any general duty of beneficence (Kagan 1998; Igneski 2006)."

**C. Weaken the duty to promote the good.**
7. *No positive duty.* "The resulting view, which may be libertarian, never requires you to sacrifice any of your good to benefit others, or even to benefit them when that would be costless for you, and is therefore completely undemanding (Narveson 2003)." (Hurka §3)
   Hurka: "But many will find this view too radical and will prefer a version of the strategy that retains a duty to promote the good, either on its own or as one duty among others, but weakens the duty so that by itself it permits some or even many acts that produce less than the most good possible."
8. *Satisficing consequentialism* (Slote 1984, per Sinnott-Armstrong; Slote 1985, per Hurka).
   Sinnott-Armstrong: "Yet another way to reach this conclusion is to give up maximization and to hold instead that we morally ought to do what creates enough utility. This position is often described as satisficing consequentialism (Slote 1984)."
   Sinnott-Armstrong: "Both satisficing and progressive consequentialism allow us to devote some of our time and money to personal projects that do not maximize overall good."
   Against (Hurka §3): "It gives you, first, no duty to improve a situation that’s already good enough even if that would involve just pushing a button and so no cost to you, and no duty ever to do more than two thirds of the most you can even if that means just pushing one button rather than another."
   And: "Since it gives no weight to costs, a satisficing view doesn’t really address what for many is the core of the demandingness objection, which concerns costs."
   Related, per Sinnott-Armstrong: progressive consequentialism (Elliot and Jamieson 2009) and scalar consequentialism (Norcross 2006, 2020; Sinhababu 2018). A Kantian imperfect duty is a further weakening Hurka discusses (§3).
9. *Murphy's co-operative principle* (Murphy 1993, 2000). Hurka (§3): "A different weakening, proposed by Liam B. Murphy, requires you to do only as much as you would have to do if everyone else were fulfilling their duty. In charitable giving, for example, you need give only as much as would be your share if everyone else were contributing as they should (Murphy 1993, 2000)."
   Its rationale: "This “co-operative” view can be motivated by concerns other than demandingness and is so for Murphy; his rationale is more that a duty shouldn’t become more onerous for you because others aren’t fulfilling theirs."
   Against: "If you and another could save a third person’s life at a total cost of $20 but the other refuses to contribute his $10, the view gives you no duty to spend $20 to save the life (Tadros 2016: 106; also Mulgan 2001: 217–18; Arneson 2004: 36–37)."
   And: "On its own it does nothing to block the claim that if two people are drowning and no one else can save them, you must sacrifice your life to do so."
10. *Rule-consequentialism* (Hooker 2000). Hurka (§3): "A final, more complex weakening, that of rule-consequentialism, may have better prospects of doing so. It says an act is right if it’s required or permitted by the set of moral rules whose internalization by a large majority, say 90%, of people in your society would have the best consequences through time (Hooker 2000)."
    Hooker's own statement (SEP §8): "At some level of demandingness, the costs of getting such demanding rules internalised will outweigh the benefits that following them will produce. Hence, doing a careful cost/benefit analysis of internalising demanding rules will come out opposing rules’ being too demanding."
    Against: "Could there not be better consequences if most people obey a more demanding rule 30% of the time than if they obey a less demanding one 80% of the time?" (Hurka §3.) Hooker (§9): "For example, Tom Carson (1991) argued that rule-consequentialism turns out to be extremely demanding in the real world. Mulgan (2001, esp. ch. 3) agreed with Carson about that, and went on to argue that, even if rule-consequentialism’s implications in the actual world are fine, the theory has counterintuitive implications in possible worlds."

**D. Supplement the duty with a competing factor.**
11. *Agent-centred prerogative* (Scheffler 1982). "The result is an “agent-relative permission” (Parfit 1978; Davis 1980) or “agent-centred prerogative” (Scheffler 1982) not to make certain sacrifices." (Hurka §4)
    Scheffler's ground: "An adequate moral view should reflect this duality in our psychology, or reflect the “independence of the personal point of view”, as it will if it grants agent-relative permissions (Scheffler 1982: 56–70)."
    Other grounds Hurka lists: ownership of one's body, time and resources (Woollard 2015: 109–12), moral autonomy (Slote 1985; Shiffrin 1991), moral status (Kamm 2007; Lazar 2019a).
    Against: "And of any proposed grounding we can ask whether it really gives the permissions an independent rationale rather than just restating the idea that there are some in more grandiose terms (Kagan 1989)."
    And (§7): "A view with agent-favouring permissions but no deontological duties, as in Scheffler (1982), is therefore even more open to the objection about permitting too much than consequentialism is, since it can allow killing or lying when that won’t have the best outcome (Kagan 1984; 1989: 19–24; Myers 1994; Mulgan 2001)."
    Hurka (§4): "If it’s unavoidable that either you or two strangers will die, this factor allows you to save yourself even though sacrificing your life to save the others would preserve more good; saving them is permitted and even heroic but not required."
    Weighted variants: a permission whose weight grows with the cost at stake "(Mulgan 2001: 152; Kamm 2007: 15–16; Pummer 2023: 22–23)" (Hurka §5); requiring-reason and two-stage variants (Parfit 2011; Slote 1991; Portmore 2003, 2011, 2019; Harman 2016; McElwee 2017), per Hurka §4.
12. *Agent-relative value.* Sinnott-Armstrong (§6) reports this route and a difficulty: "A problem is that such consequentialism would seem to imply that we morally ought not to contribute those resources to charity, although such contributions seem at least permissible."

**Over time.** Hurka (§6): "Over time a sequence of individually modest demands can end up requiring a large sacrifice from you."
He reports a lifetime cap and a sacrifice-sensitive permission (Pummer 2023: 138–44) as proposals.

Hurka's overall assessment (§8): "These different proposals have different implications and are differentially successful—perhaps none entirely so—at capturing the various intuitions one can have about what it is and is not reasonable for morality to demand."

## Arguments in play

(None recorded as argument pages yet.) The objection's form is the modus tollens shown
under The question; see [Validity](../vocabulary/validity.md). Singer's pond analogy is
summarised under positions 6 and Why it matters; Williams's integrity objection under
Framings.

## Thinkers who addressed it

- **Mill, 1861** — wrongness tied to liability to punishment (Sinnott-Armstrong §6).
- **Sidgwick, 1907** — concentrating efforts locally (*Methods of Ethics*, 430–39, per Hurka §2).
- **Singer, 1972** — "Famine, Affluence, and Morality": the pond case (p. 231); Hurka cites p. 241 for giving until one's welfare level reaches the recipients' (Hurka §§1–2).
- **[Williams, 1973](../thinkers/williams.md)** — "Bernard Williams gave an influential early statement of this objection, though not of it alone (1973: 93–100, 108–18)." (Hurka §1.) See Framings below and [Jim and the Indians](jim-and-the-indians.md).
- **Scheffler, 1982** — the agent-centred prerogative (*The Rejection of Consequentialism*, 56–70).
- **Kagan, 1984, 1989** — argues no less demanding revision can be justified (1989, per Hurka §2); presses the grounding and permitting-too-much objections to prerogatives (1984; *The Limits of Morality*, 19–24, per Hurka §§4, 7).
- **Slote, 1984, 1985** — satisficing consequentialism; moral autonomy; agent-sacrificing permissions (Sinnott-Armstrong §6; Hurka §§3–4).
- **Murphy, 1993, 2000** — the co-operative principle (*Moral Demands in Nonideal Theory*); per Sinnott-Armstrong (§6) also questions whether the opponents' intuitions are reliable: "Opponents of utilitarianism find this claim implausible, but it is not obvious that their counter-utilitarian intuitions are reliable or well-grounded (Murphy 2000, chs. 1–4; cf. Mulgan 2001, Singer 2005, Greene 2013)."
- **Wilson, 1993** — permission-seekers defending privilege (per Hurka §2).
- **Unger, 1996** — *Living High and Letting Die*, with Singer on the case-based defence.
- **Hooker, 2000** — rule-consequentialism (*Ideal Code, Real World*, ch. 8, per Sinnott-Armstrong §6).
- **Mulgan, 2001** — *The Demands of Consequentialism*: against indirect consequentialism (p. 44), Murphy (pp. 217–18) and rule-consequentialism (ch. 3); weighted permissions (p. 152). Hooker (§9): "And Mulgan has become a developer of rule-consequentialism rather than a critic (Mulgan 2006, 2009, 2015, 2017, 2020)."
- **Sobel, 2007** — the objection presupposes anti-consequentialist conclusions (below).
- **Woollard, 2015** — rescue versus beneficence; ownership as a ground for permissions. **Pummer, 2023** — demands through time. **Portmore, 2011, 2019** — a two-stage view of rational permission (all per Hurka §§2, 4, 6).

## Framings and reframings

- **Integrity, not only cost (Williams).** Hurka (§1): "He said consequentialism requires you to treat your own projects, including those you’re most committed to and that define your identity, as no more important than anyone else’s and so to sacrifice them whenever that will produce more good."
  On the chemist George: "Williams’s charge that requiring George to set aside his commitments and do what’s impersonally best is “absurd” (1973: 116) is largely, but not only, about demandingness."
  Chappell and Smyth (§4) quote Williams (UFA 116–117): "It is absurd to demand of such a man, when the sums come in from the utility network which the projects of others have in part determined, that he should just step aside from his own project and decision and acknowledge the decision which utilitarian calculation requires."
  Their reading: "In a slogan, the integrity objection is this: agency is always some particular person’s agency; or to put it another way, there is no such thing as impartial agency, in the sense of impartiality that utilitarianism requires."
  They reject reading it as the inference that Jim's and George's required acts are wrong, so "utilitarianism is false": "But this cannot be Williams’ argument, because in fact Williams denies (2)."
- **The objection presupposes its conclusion (Sobel 2007).** Sobel's abstract: "The objection cannot itself provide good reason to break with Consequentialism, because it must presuppose prior and independent breaks with the view. The way the objection measures the demandingness of an ethical theory reflects rather than justifies being in the grip of key anti-Consequentialist conclusions."
  (Excerpt: `raw/sobel-2007-impotence-of-the-demandingness-objection.md`; abstract only read.)
  Hurka's report of it (§1): "It has been argued that the demandingness objection is therefore not in fact distinct from the objection that consequentialist views permit too much. Since it relies on the same distinction between what you actively cause (here your death if you make the sacrifice) and what you merely allow (the others’ deaths if you don’t) that’s central to many versions of the other objection, it just repeats that objection (Sobel 2007)."
  Hurka's reply: "But the doing/allowing distinction doesn’t figure in all claims about demandingness."
  On the other side, Hurka says of Kagan's defence of the demands that it "assumes, perhaps controversially" that revisions need justification (position 5). Hooker (§9) lists Perl 2022, "Some Question-Begging Objections to Rule consequentialism", in the continuing debate (not read).
- **Ought versus wrong.** Sinnott-Armstrong (§6), on Mill: "If Mill is correct about this, then utilitarians can say that we ought to give much more to charity, but we are not required or obliged to do so, and failing to do so is not morally wrong (cf. Sinnott-Armstrong 2005)."
- **Related problems.** [Jim and the Indians](jim-and-the-indians.md); [Famine, affluence and morality](famine-affluence-and-morality.md); [Dirty hands](dirty-hands.md); [Trolley problem](trolley-problem.md) (Hurka §7 on self-preference in trolley cases); [Moral dilemmas](moral-dilemmas.md).

## Vocabulary

- [Validity](../vocabulary/validity.md) — the modus tollens form above.
- [Dilemma](../vocabulary/dilemma.md) — see also [Moral dilemmas](moral-dilemmas.md), a separate problem.
- Consequentialism, supererogation, agent-relative permission / agent-centred prerogative,
  satisficing, rule-consequentialism, integrity (Williams's sense) — open work in
  [vocabulary](../vocabulary/index.md). Branch: [Problems](./index.md).

Related thinkers: [Singer](../thinkers/singer.md).
