---
type: article
about: concept
title: "The argument from free will (foreknowledge and freedom)"
description: "If a being infallibly believed yesterday what you will do tomorrow, can you do otherwise, and do you act freely? The theological-fatalism argument (Boethius V.3, Augustine on Cicero, Maimonides, Pike 1965, the SEP Basic Argument) and the responses on record, each by the premise it denies: future contingents, limited foreknowledge, Boethian eternity, Ockhamism, dependence, Molinism, Augustine/Frankfurt on PAP, open theism, theological determinism, the modal-fallacy reply."
tags: [problem, paradox, philosophy-of-religion, metaphysics, free-will]
timestamp: 2026-10-01T19:53:21Z
---

# The argument from free will (foreknowledge and freedom)

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md); Wikipedia's
[List of paradoxes](https://en.wikipedia.org/w/index.php?title=List_of_paradoxes&oldid=1376699902) (rev. 1376699902) links it as "Paradox of free will": "If God knows in advance what a person will decide, how can there be free will?"
Map: Zagzebski, [SEP Fall 2024 "Foreknowledge and Free Will"](https://plato.stanford.edu/archives/fall2024/entries/free-will-foreknowledge/)
(copyright line "2021 by David Hunt, Linda Zagzebski"; excerpt:
`raw/sep-free-will-foreknowledge-fall-2024-theological-fatalism.md`).
Primary texts: Boethius, *Consolation of Philosophy* V pr. 3 and pr. 6 (James tr., 1897;
[Gutenberg #14328](https://www.gutenberg.org/ebooks/14328); excerpt: `raw/boethius-consolation-5-3-6-foreknowledge-james.md`);
Augustine, *City of God* V.9–10 (Dods tr., 1887; [New Advent](https://www.newadvent.org/fathers/120105.htm);
excerpt: `raw/augustine-city-of-god-5-9-10-foreknowledge-dods.md`).
Other sources: Swartz, [IEP "Foreknowledge and Free Will"](https://iep.utm.edu/foreknow/) (excerpt:
`raw/swartz-iep-foreknowledge-and-free-will-modal-fallacy.md`); Wikipedia,
["Argument from free will"](https://en.wikipedia.org/w/index.php?title=Argument_from_free_will&oldid=1371942354)
(rev. 1371942354; excerpt: `raw/wikipedia-argument-from-free-will.md`).
The SEP entry's authors also report Zagzebski's own arguments; those are marked as hers.

## The question

Wikipedia: "The argument from free will, also called the paradox of free will or theological fatalism, contends that omniscience and free will are incompatible and that any conception of God that incorporates both properties is therefore inconceivable." (lead, tagged "citation needed").
The SEP entry: "Theological fatalism is the thesis that infallible foreknowledge of a human act makes the act necessary and hence unfree." (preamble).
Boethius puts it in the first person: "It seems,' said I, 'too much of a paradox and a contradiction that God should know all things, and yet there should be free will." (V pr. 3); "For if God foresees everything, and can in no wise be deceived, that which providence foresees to be about to happen must necessarily come to pass." (V pr. 3).
Maimonides, as Wikipedia quotes him (Gorfinkle tr., pp. 99–100): "Does God know or does He not know that a certain individual will be good or bad? If thou sayest 'He knows', then it necessarily follows that the man is compelled to act as God knew beforehand how he would act, otherwise, God's knowledge would be imperfect."

**The Basic Argument (SEP §1).** With *T* the proposition that you will answer the phone tomorrow morning at 9 (the entry's example) and
"now-necessary" the necessity "that the past is supposed to have just because it is past":

1. "Yesterday God infallibly believed T. [Supposition of infallible foreknowledge]"
2. "If E occurred in the past, it is now-necessary that E occurred then. [Principle of the Necessity of the Past]"
3. "It is now-necessary that yesterday God believed T. [1, 2]"
4. "Necessarily, if yesterday God believed T, then T. [Definition of “infallibility”]"
5. "If p is now-necessary, and necessarily (p → q), then q is now-necessary. [Transfer of Necessity Principle]"
6. "So it is now-necessary that T. [3,4,5]"
7. "If it is now-necessary that T, then you cannot do otherwise than answer the telephone tomorrow at 9 am. [Definition of “necessary”]"
8. "Therefore, you cannot do otherwise than answer the telephone tomorrow at 9 am. [6, 7]"
9. "If you cannot do otherwise when you do an act, you do not act freely. [Principle of Alternate Possibilities]"
10. "Therefore, when you answer the telephone tomorrow at 9 am, you will not do it freely. [8, 9]"

The entry reports "there is a consensus that this argument or something close to it is valid" and
names the contested premises: "There are four premises that are not straightforward substitutions in definitions: (1), (2), (5), and (9)."
It locates the difficulty in infallibility, not knowledge as such: "The key problem, then, is the infallibility of the belief about the future" (§1).
The contract terms: [knowledge](../vocabulary/knowledge.md), [validity](../vocabulary/validity.md), [dilemma](../vocabulary/dilemma.md).

**Propositional check (this implant, 2026-10-01; logic, not a position).**
Treating each modal statement as an unanalysed atom — b = (1), nb = (3), l = (4), nt = (6), c = (8), f = *you act freely* —
and using the instances of (2), (5), (7), (9) as conditionals, `logic.py check --premises 'b' 'b -> nb' 'l' 'nb & l -> nt' 'nt -> c' 'c -> ~f' --conclusion '~f'` returns `VALID`.
Dropping the instance of (5) (`nb & l -> nt`) returns `INVALID`, with the counterexample row `b=T, c=F, f=T, l=T, nb=T, nt=F`.
This shows only that the propositional skeleton depends on the transfer step; whether (5) holds for
temporal necessity is a modal question the tool, which has no □ or ◇, does not cover (SEP §2.6 discusses it).

## Why it matters

- **Theism and libertarian freedom.** The SEP entry: the argument "creates a dilemma for anyone who thinks it important to maintain both (1) there is a deity who infallibly knows the entire future, and (2) human beings have free will in the strong sense usually called libertarian." (preamble).
- **Time, truth, modality.** The same entry: it "has also fascinated many who have not shared either of these commitments, because taking the argument’s full measure requires rethinking some of the most fundamental questions in philosophy, especially ones concerning time, truth, and modality." (preamble).
- **Responsibility and prayer.** James's summary of Boethius V.3 (1897 edition, the translator's words): "But if man has no freedom of choice, it follows that rewards and punishments are unjust as well as useless; that merit and demerit are mere names; that God is the cause of men's wickednesses; that prayer is meaningless."
- **Existence of God.** Wikipedia: "Some arguments against the existence of God focus on the supposed incoherence of humankind possessing free will and God's omniscience." It reports Dan Barker's "Free will Argument for the Nonexistence of God" (Barker 1997; not read here).
- **Logical fatalism.** The SEP entry: "A form of fatalism that is even older than theological fatalism is logical fatalism, the thesis that the past truth of a proposition about the future entails fatalism." Diodorus Cronus' version is "remarkably similar in form to our basic argument for theological fatalism" (§4).

## Positions taken

The SEP entry groups responses as compatibilist ("Compatibilists must either identify a false premise in the argument for theological fatalism or show that the conclusion does not follow from the premises.") and incompatibilist ("deny either infallible foreknowledge or free will in the sense targeted by the argument"); compatibilist responses are ordered by the premise they deny (§§1–3). That grouping is followed here; none is ranked.

**Compatibilist: deny premise (1).**
- **No true future contingents (Aristotle *De Int.* 9, as read; Prior 1962; Runzo 1981; Purtill 1988; Lucas 1989; Todd 2016a, 2021).** "This seems to have been the position of Aristotle in the famous Sea Battle argument of De Interpretatione IX" (§2.1); Prior endorsed it "three years before Pike’s seminal article"; Todd is "Another supporter of the all-future-contingents-are-false solution to the problem of theological fatalism" (§2.1).
  *Against:* "A critique of both Rhoda et al. and Tuggy may be found in Craig and Hunt (2013)." (§2.1).
- **Limited foreknowledge (Hasker 1989; Swinburne 2006; van Inwagen 2008).** "who maintain (contrary to Prior) that there are future contingent truths, the impossibility of foreknowing them is the problem with premise (1)." (§2.2).
  *Against:* "This “limited foreknowledge” view has been critiqued by Arbour (2013) and Todd (2014a), among others." (§2.2).
- **Eternity (Boethius; Aquinas *SCG* I.66; Stump & Kretzmann 1981, 1991).** The SEP entry: the solution "probably originated with the 6th century philosopher Boethius, who maintained that God is not in time and has no temporal properties, so God does not have beliefs at a time." (§2.3); Aquinas used "the circle analogy". Boethius: "Now, eternity is the possession of endless life whole and perfect at a single moment."; God's knowledge is "not foreknowledge as of something future, but knowledge of a moment that never passes." (V pr. 6). His distinction: "So, then, there are two necessities--one simple, as that men are necessarily mortal; the other conditioned, as that, if you know that someone is walking, he must necessarily be walking." (V pr. 6).
  *Against:* objections "focus on the idea of timelessness itself" or its fit with "personhood (e.g., Pike 1970, 121–129; Wolterstorff 1975; Swinburne 1977, 221)" (SEP §2.3). Zagzebski's own argument: "an argument structurally parallel to the basic argument can be formulated for timeless knowledge" (1991, ch. 2; 2011), since "The timeless realm is as much out of our reach as the past." (§2.3).

**Compatibilist: deny premise (2).**
- **Ockhamism, soft facts (Ockham; M. Adams 1967).** On God's past beliefs and "what Ockham called “accidental necessity” (necessity per accidens)" (§2.4), Ockham held "that the necessity of the past does not apply to the entire past" (§1); "A “soft” fact about the past is one that is in part about the future." (§2.4). The SEP entry says this approach "has probably attracted more attention, in its various incarnations, than any other solution." (§1).
  *Against:* the entry's assessment: "Adams’s argument was unsuccessful since, among other things, her criterion for being a hard fact had the consequence that no fact is a hard fact (Fischer 1989, introduction)"; and "Perhaps the toughest obstacle confronting the Ockhamist solution is that it is very difficult to give an account of the necessity of the past that preserves the intuition that the past has a special kind of necessity in virtue of being past, but which has the consequence that God’s past beliefs do not have that kind of necessity." (§2.4).
- **Dependence / counterfactual power (Plantinga 1986; Merricks 2009).** Plantinga "defined the accidentally necessary in terms of lack of counterfactual power"; "Notice that counterfactual power over the past is not the same thing as changing the past." (§2.5). Merricks "argues that the idea appears in Molina". *Against:* "Fischer and Todd (2011, 2013) argue that Merricks’ solution is simply a form of Ockhamism and suffers from the same defects, while Merricks (2011) replies that the dependency relation between God’s past beliefs and human acts is different from the one at work in Ockham’s approach." (§2.5).

**Compatibilist: deny premise (5).**
- **Middle knowledge (Molina; Flint 1998; Craig 1994, 1998).** "denial of (5) is the doctrine of Middle Knowledge" (§2.6); "Molinism provides an account of how God knows the contingent future, along with a strong doctrine of divine providence."; "Recently the doctrine has received strong support by Thomas Flint (1998) and Eef Dekker (2000)."
  *Against:* "Robert Adams (1991) argues that Molinism is committed to the position that the truth of a counterfactual of freedom is explanatorily prior to God’s decision to create us."; "William Hasker (1989, 1995, 1997, 2000) has offered a series of objections and replies to William Craig, who defends Middle Knowledge (1994, 1998)." (§2.6).

**Compatibilist: deny premise (9).**
- **Augustine and Frankfurt cases (Augustine; Frankfurt 1969; Hunt 1999a, 2003, 2017a).** PAP "has become well-known in the literature on free will ever since it was attacked by Harry Frankfurt (1969) in some interesting thought experiments." Augustine, who affirms both: "we assert both that God knows all things before they come to pass, and that we do by our free will whatsoever we know and feel to be done by us only because we will it." (V.9); "For a man does not therefore sin because God foreknew that he would sin." (*City of God* V.10). Hunt "argues that this is essentially the solution put forward by Augustine in On Free Choice of the Will III.1–4, though Augustine’s own considered position on free will was not libertarian." and "Divine foreknowledge constitutes its own counterexample to PAP (Hunt 2003)." (§2.8). The entry's comparison: "the Dependence Solution retains PAP by denying the general necessity of the past, while the Augustinian/Frankfurtian approach is to abandon PAP and stick with the necessity of the past." (§2.8).
  *Against:* the entry reports "an important disanalogy between a Frankfurt case and infallible foreknowledge that might lead one to doubt whether an agent really lacks alternate possibilities when her act is infallibly foreknown." (§2.8).

**Compatibilist: deny that the conclusion follows.**
- **The modal reading (Swartz, IEP).** "Ultimately the alleged incompatibility of foreknowledge and free will is shown to rest on a subtle logical error. When the error, a modal fallacy, is recognized and remedied, the problem evaporates." (summary). Of Maimonides' argument with the premise "~◊(gKD & ~D)": "But even with this repair, the argument remains invalid." (§6b). *Structural note (this implant; logic, not a position):* the SEP formulation states transfer as its own premise (5), so in that version the step to (6) rests on (5) together with (3) and (4), not on (4) alone (SEP §1); compare the propositional check above. *Against:* the entry records the contrary judgement "there is a consensus that this argument or something close to it is valid" (§1).

**Incompatibilist.**
- **Deny foreknowledge: Cicero, as Augustine reports him.** "However, in his book on divination, he in his own person most openly opposes the doctrine of the prescience of future things."; "Cicero chooses to reject the foreknowledge of future things, and shuts up the religious mind to this alternative" (*City of God* V.9).
- **Open theism (Pinnock et al. 1994; Sanders 1998; Boyd et al. 2001).** "Open theists reject divine timelessness and immutability, along with infallible foreknowledge, arguing that not only should foreknowledge be rejected because of its fatalist consequences, but the view of a God who takes risks, and can be surprised and even disappointed at how things turn out, is more faithful to Scripture than the classical notion of an essentially omniscient and foreknowing deity (Sanders 1998, Boyd et al 2001, 13–47)." (§3). *Against:* "Arbour (2019) is a recent collection of commisioned essays criticizing open theism on philosophical grounds." (§3); on the side of foreknowledge, Augustine: "For one who is not prescient of all future things is not God." (V.9).
- **Deny libertarian freedom (Edwards; theological determinism).** "Jonathan Edwards, on the other hand, based his Calvinist denial of libertarian freedom, in part, on a sophisticated version of the argument for theological fatalism (FW II.12)." The entry adds that such theists "are typically theological determinists rather than fatalists" (§3).

**Distribution, as reported.** No survey figure is recorded; the SEP entry's comparative remark on Ockhamism (§1) is its own assessment.

## Arguments in play

(none recorded as separate argument pages yet). The Basic Argument (SEP §1) and its timeless
parallel (Zagzebski 1991, as reported in §2.3) are quoted above; logical fatalism (SEP §4,
Diodorus Cronus, Aristotle's sea battle) has no page yet.

## Thinkers who addressed it

- **Aristotle** (*De Interpretatione* 9) — sea battle; read by later authors as denying future-contingent truth (SEP §2.1).
- **Diodorus Cronus** — logical-fatalist argument (SEP §4).
- **Cicero** ("his book on divination", per Augustine) — rejects foreknowledge (*City of God* V.9).
- **Augustine** (*City of God* V.9–10; *On Free Choice of the Will* III.1–4) — affirms both; read by Hunt as denying PAP.
- **Boethius** (*Consolation* V pr. 3–6, c. 524) — eternity; simple and conditioned necessity.
- **Moses Maimonides** (*Eight Chapters*, Gorfinkle tr., pp. 99–100, as quoted by Wikipedia and Swartz) — states the argument.
- **Thomas Aquinas** (*SCG* I.66) — adopts the Boethian solution (SEP §2.3).
- **William of Ockham** — soft facts, "accidental necessity" (SEP §2.4).
- **Luis de Molina**, **Duns Scotus** — middle knowledge; possible denial of (5) (SEP §§1, 2.6).
- **Jonathan Edwards** (*Freedom of the Will* II.12) — Calvinist denial of libertarian freedom (SEP §3).
- **A. N. Prior** (1962, 1967) — future contingents.
- **Nelson Pike** ([1965](https://doi.org/10.2307/2183529), *Philosophical Review* 74(1): 27–46) — the SEP entry credits him with "clearly and forcefully presenting the dilemma" (§1).
- **Marilyn Adams** (1967), **Harry Frankfurt** (1969), **Eleonore Stump** & **Norman Kretzmann** (1981, 1991), **Alvin Plantinga** (1986), **William Hasker** (1989), **John Martin Fischer** (1989), **Linda Zagzebski** (1991, 2011), **Clark Pinnock** et al. (1994), **David Hunt** (1999a, 2003, 2017a), **Trenton Merricks** (2009), **Patrick Todd** (2016a, 2021), **Norman Swartz** (IEP).

## Framings and reframings

- **Infallibility, not knowledge.** "The key problem, then, is the infallibility of the belief about the future" (SEP §1).
- **Any foreknower.** Swartz: "But the problem would arise if anyone at all (that is, anyone whatsoever) were to have knowledge of our future actions." (IEP §2).
- **A thought experiment about Gud.** The SEP entry: if God is timeless the problem is "easily reinstated by replacing God with Gud, an infallibly omniscient being who exists in time" (§5, citing Hunt 2017a).
- **A problem about time.** "Zagzebski has argued that the dilemma of theological fatalism is broader than a problem about free will. The modal or causal asymmetry of time, a transfer of necessity principle, and the supposition of infallible foreknowledge are mutually inconsistent. (1991, appendix)." (§5).
- **Seeing, not foreseeing.** Boethius: "Does the act of vision add any necessity to the things which thou seest before thy eyes?" (V pr. 6).

Not in the excerpts held: Pike 1965 itself (only bibliographically verified), the texts of
Ockham, Molina and Edwards, Augustine's *On Free Choice of the Will*, Barker's essay, and
C. S. Lewis' passage (quoted by Wikipedia); they are left out until a source is read.

## Vocabulary

- [Paradox](../vocabulary/paradox.md), [Dilemma](../vocabulary/dilemma.md) — the filing and the SEP's word for the problem.
- [Knowledge](../vocabulary/knowledge.md) — factivity; the SEP entry says the argument needs only infallible belief.
- [Validity](../vocabulary/validity.md), [Fallacy](../vocabulary/fallacy.md), [Classical logic](../methods/classical-logic.md) — the propositional check and Swartz's reply.
- *Temporal (accidental) necessity*, *soft fact*, *middle knowledge*, *PAP*, *future contingent* — open work in [vocabulary](../vocabulary/index.md).
