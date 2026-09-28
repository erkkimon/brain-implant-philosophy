---
type: article
about: concept
title: "The Euthyphro dilemma"
description: "Plato's question at Euthyphro 10a — is the holy loved by the gods because it is holy, or holy because it is loved? — and its monotheist restatement: does God command what is right because it is right, or is it right because God commands it? Theological voluntarism (Ockham, al-Ash'ari, Luther, Calvin, Quinn), an independent standard (the Mu'tazilites, Aquinas, Cudworth, Leibniz), and the restricted and 'God's nature' replies (Adams, Alston), with the arbitrariness and goodness objections as sourced."
tags: [problem, dilemma, ethics, philosophy-of-religion]
timestamp: 2026-09-28T07:01:48Z
---

# The Euthyphro dilemma

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
sources graded as in [How claims are graded](../../conventions/how-claims-are-graded.md).
Sources for the map: Plato, *Euthyphro* (Jowett, [Gutenberg #1642](https://www.gutenberg.org/ebooks/1642); Fowler, [Perseus](https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0170%3Atext%3DEuthyph.%3Asection%3D10a);
excerpt: `raw/plato-euthyphro-9e-11b-pious-loved-because-pious-jowett-fowler.md`);
Murphy, [SEP Fall 2024 "Theological Voluntarism"](https://plato.stanford.edu/archives/fall2024/entries/voluntarism-theological/)
(rev. 2019; excerpt: `raw/sep-voluntarism-theological-fall-2024-goodness-and-arbitrariness.md`);
Hare, [SEP Fall 2024 "Religion and Morality"](https://plato.stanford.edu/archives/fall2024/entries/religion-morality/)
(rev. 2019; excerpt: `raw/sep-religion-morality-fall-2024-euthyphro-ashari-voluntarists.md`);
Austin, [IEP "Divine Command Theory"](https://iep.utm.edu/divine-command-theory/)
(excerpt: `raw/iep-divine-command-theory-austin-euthyphro-responses.md`).
Where an encyclopedia author assesses, the assessment is attributed to that author.

## The question

Euthyphro has proposed "what all the gods love is holy and, on the other hand, what they all hate is unholy" (9e, Fowler). Socrates asks:

> "Is that which is holy loved by the gods because it is holy, or is it holy because it is loved by the gods?" (10a, Fowler)

Jowett's rendering: "whether the pious or holy is beloved by the gods because it is holy, or holy because it is beloved of the gods" (10a).
Euthyphro accepts the first: "It is loved because it is holy, not holy because it is loved?" — "I think so." (10d, Fowler).
Socrates concludes that "that which is dear to the gods and that which is holy are not identical" (10e), since "the one becomes lovable from the fact that it is loved, whereas the other is loved because it is in itself lovable" (11a, Fowler); Euthyphro has offered "an attribute only, and not the essence" (11a, Jowett).

**The name and the monotheist form.** Hare (SEP, §1): the problem "gives rise to what is sometimes called ‘the Euthyphro dilemma’". Austin (IEP, §3) writes "it will be useful to rephrase Socrates’ question" and gives "Does God command this particular action because it is morally right, or is it morally right because God commands it?"
The two horns, as Austin states them: on the first, "God’s commands and therefore the foundations of morality become arbitrary"; on the second, "ethics no longer depends on God in the way that Divine Command Theorists maintain" (§3).
He sums up: "morality either rests on arbitrary foundations, or God is not the source of ethics and is subject to an external moral law, both of which allegedly compromise his supreme moral and metaphysical status" (§3).

**The family of views at stake.** Murphy (SEP, intro) calls the views that hold "what God wills is relevant to determining the moral status of some set of entities" *theological voluntarism*, "following Quinn 1990", because not all of them make commanding the relevant act of will. He separates metaethical from normative versions and notes "One does not have to be a theist in order to be a theological voluntarist" (§1.1).

**Structural note (this implant; logic, not a position).** Read as an argument, the restated dilemma has the form of a constructive dilemma in the sense of [Dilemma](../vocabulary/dilemma.md). With C = right because commanded, G = commanded because right, A = morality is arbitrary, I = morality is independent of God's will, `logic.py check --premises "C | G" "C -> A" "G -> I" --conclusion "A | I"` returned "VALID" and "matches schema: constructive dilemma" (2026-09-27). Without the disjunctive premise `C | G` it returned "INVALID" with the counterexample "A=F, C=F, G=F, I=F". The replies below therefore divide by which premise they deny: the disjunction (a third option), or one of the two conditionals.

## Why it matters

- **Its place in the debate.** Austin: "The dialogue between Socrates and Euthyphro is nearly omnipresent in philosophical discussions of the relationship between God and ethics." (IEP, §3). Hare reports that Quinn (1978) defended divine command theory "against the usual objections (one, deriving from Plato's Euthyprho, that it makes morality arbitrary, and the second, deriving from a misunderstanding of Kant, that it is inconsistent with human autonomy)" (SEP, §5; spelling as in the source).
- **What depends on God's will.** Murphy lists arguments offered for voluntarism from the divine nature: "Some appeal to omnipotence: since God is both omnipotent and impeccable, theological voluntarism must be true: for if God cannot act in a way that is morally wrong, then God’s power would be limited by other normative states of affairs were theological voluntarism not the case." (§2.1); a parallel argument appeals to God's freedom (§2.1).
- **Metaethics.** Murphy reports that "John Mackie, an atheist, and George Mavrodes, a theist, have both drawn from this the same moral: if there is a God, then the normativity of morality can be understood in theistic terms; otherwise, the normativity of morality is unintelligible (Mavrodes 1986; Mackie 1977, p. 48)." (§2.1).
- **God's goodness and praise.** Leibniz asks "why praise him for what he has done, if he would be equally praiseworthy in doing the contrary?" (*Discourse on Metaphysics* §II, 1686, Montgomery tr.; excerpt: `raw/leibniz-1686-discourse-on-metaphysics-2-against-arbitrary-goodness-montgomery.md`).
- **The present state, per Hare.** Hare concludes that the revival of divine command theory together with natural law theory "shows evidence that the attempt to connect morality closely to religion is undergoing a robust recovery within professional philosophy" (§5) — Hare's assessment.

## Positions taken

No position pages exist yet; positions are listed here, unranked. Murphy
groups current views by *which* moral statuses depend on God's will
(unrestricted vs. restricted, §2.2) and by the dependence relation
(analysis, reduction, supervenience, causation, §2.4); Austin groups the
responses to the dilemma as bite the bullet, human nature, Alston's
advice, and modified divine command theory (§4a–d). The grouping below
follows the dilemma's premises (see the structural note).

**1. The first horn: right because God wills it (unrestricted voluntarism).**
- *Holders, as reported.* Ockham "states that the actions which we call “theft” and “adultery” would be obligatory for us if God commanded us to do them" (Austin §4a, citing *Super 4 Libros Sententiarum* II, 19). Al-Ash'ari (d. 935): "‘if God declared lying to be right, it would be right, and if He commanded it, none could gainsay Him’" (Hare §3). Luther: "‘What God wills is not right because he ought or was bound so to will; on the contrary, what takes place must be right, because he so wills.’" and Calvin: "whatever he wills, by the very fact that he wills it, must be considered righteous" (Hare §4). "Quinn’s 1978 work offers a theological voluntarist view on which all moral statuses are to be understood in terms of God’s will." (Murphy §2.2).
- *Case for.* The omnipotence and freedom arguments and the Mackie–Mavrodes point above (Murphy §2.1). Adams (1973, p. 105), as Murphy reports, holds it "worthwhile taking seriously the hypothesis that morality is not just a nonnatural matter but a supernatural one" (§2.1). Adams (1987), as Austin reports, reads Ockham as saying "it is a mere logical possibility that God could command adultery or cruelty, and not a real possibility" (§4a).
- *Case against.* Cudworth (1731, I.i.5, p. 10): on this view "nothing can be imagined fo grofsly wicked, or fo fouly unjuft or difhoneft, but if it were fuppofed to be commanded by this Omnipotent Deity, muft needs upon that Hypothefis forthwith become Holy, Juft and Righteous" (excerpt: `raw/cudworth-1731-eternal-and-immutable-morality-1-1-2-arbitrary-will.md`). Leibniz (§II): "Where will be his justice and his wisdom if he has only a certain despotic power, if arbitrary will takes the place of reasonableness". The goodness objection as Murphy states it: "God’s goodness consists only in God’s measuring up to a standard that God has set for Godself" (§3.1). Austin: "Most people find this to be an unacceptable view of moral obligation" (§4a) — Austin's report of reception.

**2. The second horn: God wills it because it is right (an independent standard).**
- *Holders, as reported.* 'Abd al-Jabbar (d. 1025, Mu'tazilite) "holds that the right and wrong character of acts is known immediately to human reason, independently of revelation. These standards that we learn from reason apply also to God, so that we can use them to judge what God is and is not commanding us to do." (Hare §3). Cudworth: moral good and evil "cannot poffibly be Arbitrary things, made by Will without Nature; becaufe it is Univerfally true, That things are what they are, not by Will but by Nature." (I.ii.1, p. 14). Leibniz places "the principles of goodness, of justice, and of perfection" in God's "understanding, which does not depend upon his will any more than does his essence" (§II).
- *Case for.* Cudworth's argument from natures: "things may as well be made White or Black by meer Will, without Whitenefs or Blacknefs, Equal and Unequal, without Equality and Inequality, as Morally Good and Evil" by will alone (p. 15); the will of God is "not the Formal Caufe of any Thing befides itfelf" (p. 15). Leibniz: "Besides it seems that every act of willing supposes some reason for the willing and this reason, of course, must precede the act." (§II).
- *Case against.* Austin (§3): "God is no longer the author of ethics" and "is subject to a moral law external to himself"; he quotes Arthur (2005, p. 20): "If God approves kindness because it is a virtue and hates the Nazis because they were evil, then it seems that God discovers morality rather than inventing it". The omnipotence and freedom arguments (Murphy §2.1) are the voluntarists' case against this horn. A reply Austin records: "God is subject to moral principles in the same way that he is subject to logical principles, which nearly all agree does not compromise his sovereignty" (§4c).

**3. The standard is God's nature; commands ground only obligation (restricted or modified theory).**
- *Holders, as reported.* Adams: "an act is wrong if and only if it is contrary to God’s will or commands (assuming God loves us)" and, as a necessary truth, "Any action is ethically wrong if and only if it is contrary to the commands of a loving God" (Austin §4d, quoting Adams 1987, pp. 121, 132; the 1973 and 1979 papers are reprinted there, per Murphy's bibliography). Hare §5: Adams 1999 "first separates off the good (which he analyzes Platonically in terms of imitating the ultimate good, which is God) and the right". Murphy §2.2: "Quinn, following Adams and Alston (1990), eventually rejected" the unrestricted view. Alston (1990, as Austin reports; not read here): "a theist can in fact grasp both horns of this putative dilemma" and "we can think of God himself as the supreme standard of goodness" (§4c).
- *Case for.* On emptiness: Alston, quoted by Austin, "no moral obligations attach to God, assuming, as we are here, that God is essentially perfectly good" (1990, p. 315). Murphy: "The strength of the objection from God’s goodness is directly proportional to the size of the range of normative properties that one wishes to explain in theological voluntarist terms" (§3.1). On arbitrariness: "If one holds that only moral obligations are determined by God’s will, then God might have moral reasons for selecting one set of commands/intentions rather than another" (§3.2); against the charge that a particular individual is an arbitrary standard, Alston holds "it is no more arbitrary to invoke God as the supreme moral standard than it is to invoke some supreme moral principle" (Austin §4c). Why obligation in particular: Adams's view that obligation is "ineliminably social" (Murphy §2.2: Adams "suggests, with some plausibility" — Murphy's assessment).
- *Case against.* Austin: "is not arbitrariness still present, insofar as it seems that it is arbitrary to take a particular individual as the standard of goodness" (§4c). Hooker (2001, p. 334), as Murphy reports, argues the appeal to God's justice is "illegitimate within a theological voluntarist account" (§3.1). Murphy's motivation worry: "If we are willing to give up theological voluntarism in some moral domains, why not in all of them?" (§3.3); if there are demand-independent protected reasons, "which natural law theorists, for example, would hold—then Adams’ gambit will not work" (§3.3; Murphy's assessment). The omnipotence objection to a God who cannot command cruelty (Austin §4d: "It is not possible for a loving God to command cruelty for its own sake.") and Aquinas's reply are in Austin §7a.

**4. Intermediate and alternative views.**
- *Aquinas* (c. 1224–74): "God's will is not exercised by arbitrary fiat" and reason "is participating in the eternal law, which is in the mind of God" (Hare §3); Austin's "human nature" response draws on Aquinas via Clark and Poortenga (2003), and adds that its defender "should explain why God created us with the nature that we possess" (§4b).
- *Scotus* (c. 1266–1308): the first table of the Decalogue necessary, "But the second table is contingent, though fitting our nature, and God could prescribe different commands even for human beings (Ord. I, dist. 44)." (Hare §3).
- *Al-Maturidi* (d. 944): "in some ways intermediate between Mu'tazilites and Asharites" (Hare §3).
- *Zagzebski* (2004): divine motivation theory, "as an alternative to divine command theory", grounding moral normativity in "a good emotion" with "God's emotions" as "the best exemplar" (Hare §5).
- *Murphy* (2002, 2011/2012): an objection that "divine command only has authority over those persons that have submitted themselves to divine authority, but moral obligation has authority more broadly" (Hare §5).

## Arguments in play

No argument pages exist yet. The arguments the sources set out:

- **The arbitrariness objection, two versions** (Murphy §3.2): "One claim is that theological voluntarism implies that God’s commands/intentions, on which moral statuses depend, must be arbitrary. A distinct claim is that theological voluntarism implies that the content of morality is itself arbitrary". Against the first, Murphy judges that "the chastened claim—that there is some arbitrariness in God’s commands—is far less troubling on its own" (see also Carson 2012). The second rests on the thesis "that every obtaining moral state of affairs either has a justification or is necessary"; Murphy judges its "appeal to necessary moral states of affairs as the only proper starting point is dubious", and points to Schroeder 2005 for "a similar objection raised against theological voluntarism by Ralph Cudworth (1731), and a similar response on behalf of theological voluntarism" (§3.2).
- **The goodness objection** (the emptiness worry) (Murphy §3.1; Austin §7b, who traces it to Leibniz and to Quinn 1978, Wierenga 1989, Alston 1989 and Wainwright 2005). Murphy's summary: "the strain needed to answer the charge becomes greater the wider the range of normative properties that the formulation of theological voluntarism aims to explain" (§3.1).
- **The omnipotence and freedom arguments** for voluntarism (Murphy §2.1, citing Idziak 1979, pp. 8–10).
- **Cudworth's argument from natures** (I.ii.1) and **Leibniz's "every act of willing supposes some reason"** (§II), under Positions 2.

## Thinkers who addressed it

- **Plato**, *Euthyphro* 9e–11b — the question; Socrates' view is the second alternative, per Hare, who adds Socrates "does not argue for this conclusion in addressing this question" (§1).
- **al-Ash'ari** (d. 935), *The Theology of al-Ash'ari* 169–70 — first horn (Hare §3).
- **al-Maturidi** (d. 944) — intermediate (Hare §3).
- **'Abd al-Jabbar** (d. 1025), Mu'tazilite — standards known by reason apply to God (Hare §3).
- **Thomas Aquinas** — natural law as participation in eternal law, ST I-II q. 91 a. 2 (Hare §3).
- **John Duns Scotus** — second table contingent, *Ord.* I d. 44 (Hare §3).
- **William of Ockham** (d. 1349) — first horn, *Sent.* II q. 19 (Austin §4a); named by Cudworth "among the firft that maintained That there is no Act Evil but as it is prohibited by God" (p. 10), followed by "Petrus Alliacus and Andreas de Novo Caftro".
- **Luther** (1483–1546), *Bondage of the Will*; **Calvin** (1509–64), *Institutes* 3.23.2 — first horn (Hare §4).
- **Descartes** (1596–1650) "located the source of moral law (surprisingly for a rationalist) in God's will" (Hare §4); see [Descartes](../thinkers/descartes.md).
- **Leibniz**, *Discourse on Metaphysics* §II (1686) — against goodness "simply by the will of God".
- **Ralph Cudworth**, *Eternal and Immutable Morality* (1731) I.i–ii — against "the Arbitrary Will and Pleafure of God".
- **Robert M. Adams** (1973, 1979, 1987, 1999) — modified divine command theory; obligation as social.
- **Philip Quinn** (1978; 1979, 1990, 1999) — unrestricted view, later restricted; causal dependence "in a particularly strong form" (Murphy §2.4).
- **William Alston** (1990) — both horns; God as the standard of goodness.
- **Brad Hooker** (2001) — against the appeal to God's justice.
- **Linda Zagzebski** (2004); **John Hare** (2007, 2015, "a version of the theory that derives from God's sovereignty", Hare §5); **Mark Murphy** (2002, 2011, 2012); **Thomas Carson** (2012); **Mark Schroeder** (2005).

## Framings and reframings

- **Not an objection to religious ethics, per Hare.** Hare: Socrates' "view is not an objection to tying morality and religion together. He hints at the end of the dialogue (Euthyphro, 13de) that the right way to link them is to see that when we do good we are serving the gods well." (§1).
- **A question about definition.** In the text, what Socrates draws from the answer is that "dear to the gods" and "holy" "are not identical" and that Euthyphro gave "an attribute only, and not the essence" (10e–11a). Hare reads Socrates as "probably relying on the earlier premise, at Euthyphro, 7c10f, that we love things because of the properties they have" (§1).
- **From gods to God, from love to command.** The monotheist form is a restatement (Austin: "rephrase", §3); Plato's text concerns what "all the gods love". Murphy's entry treats the same objections without naming the *Euthyphro* ("Perennial difficulties for metaethical theological voluntarism", §3 title).
- **A "putative" dilemma.** Alston's claim that both horns can be grasped (Austin §4c) and the modified theory's aim "at avoiding both horns" (Austin §4d) deny that the two alternatives exclude each other or exhaust the field; in the structural note's terms, they reject the premise `C | G` as the dilemma frames it (a *false dilemma* charge in the sense of [Dilemma](../vocabulary/dilemma.md)).
- **Beyond theism.** Murphy: an atheist can hold that "the concept of obligation is ineliminably theistic, though there is no God; that God does not exist counts not against metaethical theological voluntarism but rather against the claim that the concept of obligation has application" (§1.1).

## Vocabulary

- [Dilemma](../vocabulary/dilemma.md) — the argument-form sense; the *false dilemma* charge is against the disjunctive premise, not the form.
- [Validity](../vocabulary/validity.md) — what the logic check shows and does not show.
- Theological voluntarism, divine command theory, natural law, obligation vs. goodness — open work in [vocabulary](../vocabulary/index.md).

Related problems: [Can there be genuine moral dilemmas?](moral-dilemmas.md),
[Meno's paradox](menos-paradox.md) (another Socratic question of
definition). Branch: [Problems](./index.md).
