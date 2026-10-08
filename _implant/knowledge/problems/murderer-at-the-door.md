---
type: article
about: concept
title: "Lying to the murderer at the door (Kant and Constant)"
description: "May you lie to a murderer who asks whether the friend he pursues is hiding in your house? Constant's 1797 objection, Kant's reply 'On a Supposed Right to Lie' (Ak. 8:425 ff.), the universalizability test, Korsgaard's 1986 Universal Law vs. Humanity reading, Varden's Doctrine of Right reading, definitional escapes (Grotius, Donagan), and utilitarian and virtue-ethical treatments."
tags: [problem, ethics, kant, lying, deontology]
timestamp: 2026-10-08T19:18:49Z
---

# Lying to the murderer at the door (Kant and Constant)

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md), graded as in
[How claims are graded](../../conventions/how-claims-are-graded.md). Primary text: Kant, 1797, in
Abbott's public-domain translation ([archive.org scan, pp. 361–365](https://archive.org/details/kantscritiqueofp00kantuoft);
excerpt: `raw/kant-1797-supposed-right-to-lie-constant-abbott.md`). Map of positions: James Edwin
Mahon, [SEP Fall 2024 "The Definition of Lying and Deception"](https://plato.stanford.edu/archives/fall2024/entries/lying-definition/)
(rev. 2015-12-25; excerpt: `raw/sep-lying-definition-fall-2024-murderer-and-kant.md`). What Kant
wrote is kept in *The question*; how interpreters read him is under Positions (group 4) and
Framings, each reading with its owner.

## The question

**Constant's case**, as Kant quotes it from the German translation of *Des réactions politiques*
(Abbott p. 361): "The moral principle that it is one's duty to speak the truth, if it were taken singly and unconditionally, would make all society impossible. We have the proof of this in the very direct consequences which have been drawn from this principle by a German philosopher, who goes so far as to affirm that to tell a falsehood to a murderer who asked us whether our friend, of whom he was in pursuit, had not taken refuge in our house, would be a crime."
Constant's argument (p. 361): "It is a duty to tell the truth. The notion of duty is inseparable from the notion of right. A duty is what in one being corresponds to the right of another. Where there are no rights there are no duties. To tell the truth then is a duty, but only towards him who has a right to the truth. But no man has a right to a truth that injures others."
In Constant's French (1796, ch. VIII; [Wikisource](https://fr.wikisource.org/wiki/Des_r%C3%A9actions_politiques_-_2nde_%C3%A9dition/VIII._Des_principes);
excerpt: `raw/constant-1796-des-reactions-politiques-viii-des-principes.md`) the pursuers are
plural, "envers des assassins qui vous demanderoient", and the remedy is "des principes
intermédiaires"; he adds that if the principle is rejected, "la société n’en sera pas moins
détruite".

**Kant's two questions** (p. 362): "Now, the first question is whether a man—in cases where he cannot avoid answering Yes or No—has the right to be untruthful. The second question is whether, in order to prevent a misdeed that threatens him or some one else, he is not actually bound to be untruthful in a certain statement to which an unjust compulsion forces him."

**Kant's answer**, in his words (pp. 362–365):

- "Truth in utterances that cannot be avoided is the formal duty of a man to everyone, however great the disadvantage that may arise from it to him or any other; and although by making a false statement I do no wrong to him who unjustly compels me to speak, yet I do wrong to men in general in the most essential point of duty, so that it may be called a lie (though not in the jurist's sense), that is, so far as in me lies I cause that declarations in general find no credit, and hence that all rights founded on contract should lose their force; and this is a wrong which is done to mankind."
- Responsibility: "For instance, if you have by a lie hindered a man who is even now planning a murder, you are legally responsible for all the consequences. But if you have strictly adhered to the truth, public justice can find no fault with you, be the unforeseen consequence what it may."
- "Whoever then tells a lie, however good his intentions may be, must answer for the consequences of it, even before the civil tribunal, and must pay the penalty for them, however unforeseen they may have been" (p. 363).
- "To be truthful (honest) in all declarations is therefore a sacred unconditional command of reason, and not to be limited by any expediency." (p. 363)
- Scope, in Kant's footnote (p. 362, n. 1): "For this principle belongs to Ethics, and here we are speaking only of a duty of justice."
- Against Constant's premise: "the expression "to have a right to the truth" is unmeaning" (p. 361), "for truth is not a possession the right to which can be granted to one, and refused to another" (p. 364); Constant "confounds the action by which one does harm (nocet) to another by telling the truth, the admission of which he cannot avoid, with the action by which he does him wrong (lædit)" (p. 364).
- Against "middle principles": they "can only contain the closer definition of their application to actual cases (according to the rules of politics), and never exceptions from them, since exceptions destroy the universality, on account of which alone they bear the name of principles." (p. 365)

**Attribution.** A note by Constant's translator K. F. Cramer names Kant as the philosopher and
Michaelis as earlier ("J. D. Michaelis, in Göttingen, propounded the same strange opinion even before Kant."), and Kant replies:
"I hereby admit that I have really said this in some place which I cannot now recollect." (p. 361, notes).

**Logic of Constant's step (this implant, 2026-09-27; logic, not a position).** Let D = *I have a
duty to tell this person the truth*, R = *this person has a right to the truth*. Constant's
premises are D → R ("only towards him who has a right") and ¬R ("no man has a right to a truth
that injures others"). `python3 _implant/skills/tools/logic.py check --premises "D -> R" "~R" --conclusion "~D"`
prints "VALID" and "matches schema: modus tollens". Kant's reply, quoted above, rejects the first
premise: the duty is owed "to everyone" and "makes no distinction between persons" (p. 364).

The case is a [dilemma](../vocabulary/dilemma.md) in the loose sense; whether it is a genuine moral
dilemma is the topic of [Can there be genuine moral dilemmas?](moral-dilemmas.md).

## Why it matters

- **Kant's rigorism.** Korsgaard (1986, pp. 325–326; [*Phil. & Pub. Aff.* 15(4): 325–349](https://www.jstor.org/stable/2265252),
  reprint [doi:10.1017/CBO9781139174503.006](https://doi.org/10.1017/CBO9781139174503.006); excerpt:
  `raw/korsgaard-1986-right-to-lie-kant-dealing-with-evil.md`): "The most well-known example of this "rigorism", as it is sometimes called, concerns Kant's views on our duty to tell the truth."
- **Test case for interpreters.** Varden (2010, p. 403; [doi:10.1111/j.1467-9833.2010.01507.x](https://doi.org/10.1111/j.1467-9833.2010.01507.x);
  excerpt: `raw/varden-2010-kant-lying-murderer-door-legal-philosophy.md`): "Kant’s example of lying to the murderer at the door has been a cherished source of scorn for thinkers with little sympathy for Kant’s philosophy and a source of deep puzzlement for those more favorably inclined."
- **Defining lying.** Mahon (SEP §2.3) uses the case against definitions that make a lie's wrongness
  part of what a lie is (see position 3).
- **Scholarship.** The publisher's abstract of Timmermann's *Kant and the Supposed Right to Lie*
  (CUP 2025, [doi:10.1017/9781108992435](https://doi.org/10.1017/9781108992435); abstract only; excerpt:
  `raw/murderer-at-the-door-bibliographic-records.md`) calls it "the first monograph to explore
  Kant's essay in detail".

## Positions taken

Grouped first as Mahon groups them (SEP §2.3): "Surely, for example, it is possible to lie to a would-be murderer, whether it is impermissible, as some absolutist deontologists maintain (Augustine 1952; Aquinas 1972 (cf.  MacIntyre 1995b); Kant 1996 (cf. Mahon 2006); Newman 1880; Geach 1977; Betz 1985; Pruss 1999; Tollefsen 2014), or permissible (i.e., either optional or obligatory), as consequentialists and moderate deontologists maintain (Constant 1964; Mill 1863; Sidgwick 1981; Bok 1978; MacIntyre 1995a; cf. Kagan 1998)."
Groups 3 and 4 are added from the sources named in them. Not ranked. No survey of philosophers'
answers is recorded; Engelmann (2025, [doi:10.5040/9781350377837.ch-10](https://doi.org/10.5040/9781350377837.ch-10))
is an experimental-philosophy chapter on the case, not read, so no figures are given.

**1. Impermissible (absolutist deontology).** Holders as listed by Mahon above.
*For:* Kant's argument that the lie, while no wrong to the murderer, is a "wrong which is done to
mankind" because it makes "declarations in general find no credit" (p. 362); it injures "mankind generally, since it vitiates the source of justice" (p. 362).
Newman, as quoted by Korsgaard (n. 12, via Bok) for an alternative to lying: "to knock the man down, and to call out for the police".
*Against:* Constant: the principle "taken singly and unconditionally, would make all society
impossible" (p. 361). Sidgwick (*Methods*, 7th ed., III.vii.2; [Gutenberg #46743](https://www.gutenberg.org/ebooks/46743);
excerpt: `raw/mill-1863-sidgwick-1907-hursthouse-2022-lying-exceptions.md`): "so if we may even kill in defence of ourselves and others, it seems strange if we may not lie, if lying will defend us better against a palpable invasion of our rights: and Common Sense does not seem to prohibit this decisively."
Korsgaard (p. 327) reports that "Unsympathetic readers are inclined to take them as evidence of the horrifying conclusions to which Kant was led by his notion that the necessity in duty is rational necessity".

**2. Permissible — optional or obligatory (consequentialists, moderate deontologists).** Holders as
listed by Mahon above.
*For:* Constant's right-based argument (quoted under *The question*). Mill (*Utilitarianism*, ch. II;
[Gutenberg #11224](https://www.gutenberg.org/ebooks/11224)): "Yet that even this rule, sacred as it is, admits of possible exceptions, is acknowledged by all moralists; the chief of which is when the withholding of some fact (as of information from a male-factor, or of bad news from a person dangerously ill) would preserve some one (especially a person other than oneself) from great and unmerited evil, and when the withholding can only be effected by denial."
Sidgwick (III.vii.2) asks whether truth-speaking is "merely a general right of each man to have
truth spoken to him by his fellows, which right however may be forfeited or suspended under
certain circumstances".
*Against:* Kant (p. 364): "the duty of veracity (of which alone we are speaking here) makes no distinction between persons towards whom we have this duty, and towards whom we may be free from it; but is an unconditional duty which holds in all circumstances."
Kant (p. 365): exceptions "destroy the universality" of principles. Mill himself states the cost
the exception must weigh: a lie weakens "the trustworthiness of human assertion" (ch. II).

**3. Not a lie at all (moral-deceptionist definitions).** Donagan (1977, p. 89, as Mahon reports
him): one cannot lie to "a would-be murderer who threatens your life if you will not tell him where his quarry has gone"; Grotius, via Bok (1978, p. 14, as
Mahon quotes her): "speaking falsely to those—like thieves—to whom truthfulness is not owed cannot
be called lying". Kant's *Lectures on Ethics* thief case, as Mahon reports it (§2.2): the robbed man's "I have no money" is not a lie, "for the other knows that… he also has no right whatever to demand the truth from me" (Kant 1997, 203; Mahon adds "but see Mahon 2009").
*For:* the definitions themselves, as Mahon sets them out: Grotius's lie violates the hearer's
"right to exercise liberty of judgment"; Donagan's is "to freely make a believed-false statement
to another fully responsible and rational person". *Against:* Mahon (§2.3): "It has been objected that
these moral deceptionist definitions are unduly narrow and restrictive (Bok 1978)"; Fried (1978,
55 n1, as Mahon reports) holds "it is possible for the victim to lie to the thief in Kant’s example".

**4. Readings of Kant's own theory** (a second question: what Kant's principles imply). Korsgaard
(p. 327): "Kant's readers differ about whether Kant's moral philosophy commits him to the claims he makes in these passages."

- **4a. Traditional reading**, as Varden describes it (p. 405): the essay is read through the
  *Groundwork*, so that it "simply repeats how one ought never to lie as the maxim of lying cannot
  be universalized". The test, in Kant's words (Abbott tr., [Gutenberg #5682](https://www.gutenberg.org/ebooks/5682);
  excerpt: `raw/kant-1785-groundwork-4-402-4-422-universal-law-lying-promise-abbott.md`): "Act only
  on that maxim whereby thou canst at the same time will that it should become a universal law."
  (4:421); for the lying promise, "no one would consider that anything was promised to him, but
  would ridicule all such statements as vain pretences" (4:422). Johnson and Cureton (SEP Fall 2024
  §5; excerpt: `raw/sep-kant-moral-fall-2024-universal-law-lying-promise.md`) note that "Kant’s
  interpreters differ over exactly how to reconstruct the derivation of these duties."
- **4b. Korsgaard (1986): Universal Law permits, Humanity forbids.** "It is permissible to lie to deceivers in order to counteract the intended results of their deceptions, for the maxim of lying to a deceiver is universalizable." (p. 330),
  because "A murderer who expects to conduct his business by asking questions must suppose that you do not know who he is and what he has in mind." (p. 329).
  But "When we apply the Formula of Humanity, however, the argument against lying that results applies to any lie whatever." (p. 330).
  She concludes that "we need special principles for dealing with evil" (p. 327): "When dealing
  with evil circumstances we may depart from this ideal." (p. 346). On the same page she writes
  that "morality itself sometimes allows or even requires us to do something that from an ideal
  perspective is wrong" (p. 327). She cites Kant's *Lectures* (LE 228): "if I cannot save myself by
  maintaining silence, then my lie is a weapon of defence" (p. 338).
- **4c. Varden (2010): Doctrine of Right reading.** "In this paper, I argue that Kant’s discussion of lying to the murderer at the door has been seriously misinterpreted." (p. 403)
  "Kant never discusses first-personal ethics (universalizable maxims and actions from duty) in this paper." (p. 406)
  Her reconstruction: "His basic claim is that if a person chooses to stay out of the interaction between the murderer and his potential victim by telling the truth to the potential murderer, then a public court of justice cannot punish her for having done so." (p. 410);
  the liar "becomes responsible for the unintended, yet bad consequences of the lie" (p. 410); and
  "The Nazis, however, did not represent a public authority on Kant’s view and consequently there is no duty to abstain from lying to Nazis." (p. 404).
  Varden (n. 5) reports that Sussman (2009), Weinrib (2008) and Wood (2008, ch. 14) "agree with me
  on the importance of reading Kant’s remarks on lying to the murderer at the door from the point of view of the Doctrine of Right", and that "Sussman defends lying in cases of self-defense".
- *Between the readings:* Korsgaard ties her Universal Law result to the murderer's deception ("He has created a situation which universalization cannot reach.", p. 330);
  her note 4 (p. 330) says that if the murderer announces his intentions "your only recourse is
  refusal to answer". Varden (p. 407) rejects refusing to answer, and answering yes while barring entry, as readings of Kant's case, since Kant
  stipulates that one "cannot avoid answering Yes or No" (p. 362): "Yet, it is clear that these two responses do not permit us to conclude that we can lie to the murderer at the door."
  Korsgaard (p. 337) on her own result: "lying to the murderer at the door was not shown to be
  permissible in a straightforward manner: the maxim did not so much pass as evade universalization".

**5. Virtue ethics.** No source held treats this case in virtue terms. Hursthouse and Pettigrove
([SEP Fall 2024 "Virtue Ethics"](https://plato.stanford.edu/archives/fall2024/entries/ethics-virtue/) §1.1)
state the general view: "The honest person recognises “That would be a lie” as a strong (though perhaps not overriding) reason for not making certain statements in certain circumstances, and gives due, but not overriding, weight to “That would be the truth” as a reason for making them."
On conflicts (§3): "Honesty points to telling the hurtful truth, kindness and compassion to
remaining silent or even lying." Deontology and virtue ethics, they write, "aim to resolve a number of dilemmas by arguing that the conflict is merely apparent".

## Arguments in play

- **Constant's rights argument** — modus tollens from duty-implies-right (checked above).
- **Kant's wrong-to-mankind argument** — the lie makes "declarations in general find no credit"
  and undermines "all rights founded on contract" (p. 362).
- **The universalizability test** (G 4:402, 4:421–422) and **the Formula of Humanity** (G 4:429,
  "never as means only") as applied by Korsgaard (group 4b).
- **Self-defence analogy** — Sidgwick (III.vii.2); Kant's *Lectures* (LE 228, via Korsgaard).
- **Harm versus wrong** — Kant's *nocet*/*lædit* distinction (p. 364).
- (No argument page in this implant yet; see [arguments](../arguments/index.md).)

## Thinkers who addressed it

- **Augustine, Aquinas** — impermissible (listed by Mahon §2.3; texts not read here).
- **Hugo Grotius** — false speech to those without the right to liberty of judgment is no lie (via Mahon, Bok).
- **Johann David Michaelis** — held the view "even before Kant", per Cramer's note (Abbott p. 361).
- **Benjamin Constant**, 1796/1797 — permissible: no right to a harmful truth (*Des réactions politiques*, ch. VIII).
- **Immanuel Kant**, 1797 — no right to lie, as a duty of justice (Ak. 8:425 ff.; Abbott pp. 361–365).
- **J. S. Mill**, 1863 — exception for "information from a male-factor" (*Utilitarianism* ch. II).
- **J. H. Newman**, *Apologia Pro Vita Sua* (1880 ed., p. 361, via Bok and Korsgaard n. 12) — knock the man down instead.
- **Henry Sidgwick**, *Methods of Ethics* (1st ed. 1874; 7th ed. 1907) — Common Sense does not prohibit the defensive lie "decisively" (III.vii.2).
- **H. J. Paton**, 1954 — "An Alleged Right to Lie", *Kant-Studien* 45: 190–203 ([doi](https://doi.org/10.1515/kant.1954.45.1-4.190); record only, not read, so his reading is not reported).
- **Alan Donagan**, 1977; **Sissela Bok**, 1978; **Charles Fried**, 1978 — as Mahon reports (groups 2–3).
- **Christine Korsgaard**, 1986 — group 4b. **James Edwin Mahon**, 2006 ([doi](https://doi.org/10.1080/09608780600956407); not read), SEP 2015.
- **Jacob Weinrib**, 2008 ([doi](https://doi.org/10.1017/S1369415400001126)); **Allen Wood**, 2008 ([doi](https://doi.org/10.1017/CBO9780511809651.015)); **David Sussman**, 2009 — as Varden reports them (not read).
- **Helga Varden**, 2010 — group 4c. **Seana Shiffrin**, *Speech Matters*, ch. 1 "Lies and the Murderer Next Door" ([doi](https://doi.org/10.1515/9781400852529-003); record only).
- **Jens Timmermann**, 2025 — monograph; per its abstract, "Kant's core argument against Constant: lying, or a right to lie, would undermine contractual rights and spell disaster for all humanity".

## Framings and reframings

- **Right, not ethics.** Kant's own footnote limits the essay to "a duty of justice" (p. 362, n. 1);
  Varden (p. 406) builds her reading on this, against what she calls the traditional reading.
- **Ideal and non-ideal theory.** Korsgaard (p. 349) proposes "special principles to use when
  dealing with evil", on the model of Rawls's non-ideal theory and Kant's laws of war.
- **A question about the word "lie".** Mahon (§2.3) presents the Grotius–Donagan route as
  definitional: on it the statement to the murderer is not a lie; he reports Bok's objection.
- **Two texts of Constant.** Constant's French has "des assassins" (plural) and presents
  truth-telling as needing "principes intermédiaires"; Kant answers the German translation.
  Timmermann's abstract lists "the peculiarities of Constant's version of the case" among his topics.
- **Related cases.** [The ticking time bomb scenario](ticking-bomb.md); [dirty hands](dirty-hands.md);
  [the trolley problem](trolley-problem.md);
  [the justification of punishment](justification-of-punishment.md) (Kant on right).

## Vocabulary

- [Dilemma](../vocabulary/dilemma.md) — loose sense (see *The question*).
- Lie, deception, maxim, categorical imperative, perfect duty, duty of justice (right) vs. duty of
  virtue — open work in [vocabulary](../vocabulary/index.md). Branch: [Problems](./index.md).

Related thinkers: [MacIntyre](../thinkers/macintyre.md) (Mahon §2.3), [Rawls](../thinkers/rawls.md) (Korsgaard), [Kant](../thinkers/kant.md), [Augustine](../thinkers/augustine.md) (*De mendacio*; Mahon SEP §2.3), [Aquinas](../thinkers/aquinas.md).
