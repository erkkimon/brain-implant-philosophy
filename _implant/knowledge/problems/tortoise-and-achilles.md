---
type: article
about: concept
title: What the Tortoise Said to Achilles
description: "Lewis Carroll's 1895 dialogue in Mind: the Tortoise accepts premises A and B and each added hypothetical ('If A and B are true, Z must be true'), yet withholds Z, and the list of premises grows without end. Can a rule of inference be written in as one more premise, and what makes anyone draw a conclusion? Carroll's own diagnosis, Russell's 'therefore', Ryle's knowing-how, Quine against conventionalism, Stroud's non-propositional factor, Boghossian on rule-circularity, and Engel's four readings."
tags: [problem, paradox, logic, philosophy-of-logic, inference, epistemology]
timestamp: 2026-10-01T21:51:46Z
---

# What the Tortoise Said to Achilles

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Primary text: Lewis Carroll, "What the Tortoise Said to Achilles", *Mind* n.s. IV(14), 1895,
pp. 278–280, [doi:10.1093/mind/IV.14.278](https://doi.org/10.1093/mind/IV.14.278), read on
[Wikisource](https://en.wikisource.org/wiki/What_the_Tortoise_Said_to_Achilles), public domain
(excerpt: `raw/carroll-1895-what-the-tortoise-said-to-achilles.md`); reprinted *Mind* 104(416), 1995,
pp. 691–693 ([doi:10.1093/mind/104.416.691](https://doi.org/10.1093/mind/104.416.691)).
Map of readings: Pascal Engel, "Dummett, Achilles and the Tortoise", in *The Philosophy of Michael
Dummett* (Open Court, 2005), author's draft [HAL ijn_00000571](https://jeannicod.ccsd.cnrs.fr/ijn_00000571)
(excerpt: `raw/engel-2005-dummett-achilles-and-the-tortoise.md`).
Admitted from Wikipedia's List of paradoxes, revision 1376699902, "Logic"
(excerpt: `raw/wikipedia-what-the-tortoise-said-to-achilles.md`). Not to be confused with
Zeno's race ([Zeno's paradoxes](zenos-paradoxes.md)), which the dialogue opens on.

## The question

Carroll's setting: "Achilles had overtaken the Tortoise, and had seated himself comfortably on its back." (p. 278).
The Tortoise takes three propositions from Euclid's First Proposition: "(A)  Things that are equal to the same are equal to each other.", "(B)  The two sides of this Triangle are things that are equal to the same." and "(Z)  The two sides of this Triangle are equal to each other." (p. 278).
It asks: "Readers of Euclid will grant, I suppose, that Z follows logically from A and B, so that any one who accepts A and B as true, must accept Z as true?" (p. 278).
The challenge: "Well, now, I want you to consider me as a reader of the second kind, and to force me, logically, to accept Z as true." (p. 279) — the second kind being a reader who accepts A and B but not the hypothetical.

The regress. Achilles writes in "(C)  If A and B are true, Z must be true." and says "Then I must ask you to accept C." (p. 279). The Tortoise grants C and still withholds Z: "If A and B and C are true, Z must be true," the Tortoise thoughtfully repeated.  "That's another Hypothetical, isn't it?  And, if I failed to see its truth, I might accept A and B and C, and still not accept Z, mightn't I?" (p. 279).
So "(D)  If A and B and C are true, then Z must be true." is added (p. 279), and then "(E)  If A and B and C and D are true, Z must be true." (p. 280), with the Tortoise's rider "Until I've granted that, of course I needn't grant Z.  So it's quite a necessary step, you see?" (p. 280).
Months later the count stands at: "Unless I've lost count, that makes a thousand and one.  There are several millions more to come." (p. 280).

The question the dialogue leaves, as Wikipedia's list entry puts it: "If a presumption needs to be made that a specific result can be deduced from premises, then the result can never be deduced. An inference rule, which is valid (or not), cannot be a premise, which is true (or false), otherwise one has an infinite regress." (rev. 1376699902).
Engel names two features — the Tortoise accepts C, and makes its acceptance conditional on C being entered as a further premise — and asks: "The puzzle is: how, given these facts, can she fail to accept Z?" (draft p. 2).
The terms at stake are [validity](../vocabulary/validity.md) (of the "sequence") and the difference between a premise and a rule of inference in an [argument](../vocabulary/argument.md).

**Propositional check (this implant, 2026-10-01; logic, not a position).**
Treat A, B, Z as atoms *a*, *b*, *z* and C as the material conditional (*a* & *b*) -> *z*.
`logic.py check --premises "a" "b" "(a & b) -> z" --conclusion "z"` outputs `VALID`.
`logic.py check --premises "a" "b" --conclusion "z"` outputs `INVALID` with
`Counterexamples (premises true, conclusion false):` `a=T, b=T, z=F`.
The tool checks validity by truth table: it reports that Z follows from A, B, C; it
does not model a reasoner's accepting or refusing Z, which is what the Tortoise
withholds. Read as atoms, A and B do not yield Z without C, because the step from
things equal to the same to these two sides of this triangle is first-order (instantiation), which
the propositional tool does not represent.

## Why it matters

- **Premises and rules.** Russell (1903, *Principles of Mathematics* § 38) uses it to show that a principle of inference is independent of the implications it licenses: "The independence of this principle is brought out by a consideration of Lewis Carroll's puzzle, What the Tortoise said to Achilles" (excerpt: `raw/russell-1903-principles-38-tortoise-therefore.md`).
- **Knowing how.** Pavese (SEP Fall 2024 "Knowledge How", §1.4) reports: "A less discussed regress that can be found in Ryle (1946: 6–7) is an adaptation of Lewis Carroll’s (1895) regress." (excerpt: `raw/sep-knowledge-how-fall-2024-carrolls-regress-ryle.md`).
- **Conventionalism about logic.** Gómez-Torrente (SEP Fall 2024 "Logical Truth", §1.1) on Quine 1936: "Quine (1936, §III) famously criticized the Hobbesian view noting that since the logical truths are infinite in number, our ground for them must not lie just in a finite number of explicit conventions, for logical rules are presumably needed to derive an infinite number of logical truths from a finite number of conventions (an argument derived from Carroll 1895; see Soames 2018, ch. 10, for exposition and Gómez-Torrente 2019 for criticism of the argument)." (excerpt: `raw/sep-logical-truth-fall-2024-quine-carroll-conventions.md`).
- **Justifying logic.** Boghossian ("Knowledge of Logic", 2000, p. 230 n. 2) attaches it to the difference between a disposition to reason by modus ponens and the belief that modus ponens is truth-preserving: "This is at least part of the moral both of Lewis Carroll's 'What the Tortoise Said to Achilles', in Mind 1898 and of Wittgenstein's discussion of rule-following in Philosophical Investigations (Oxford: Blackwell, 1958)." ("1898" as printed; excerpt: `raw/boghossian-2000-knowledge-of-logic-rule-circularity.md`).
- **The force of reasons.** Engel (draft p. 1) calls it "Lewis Carroll‟s paradox of Achilles and the Tortoise, which is often called the “paradox of inference”" and ends that "Unless we answer these questions the Tortoise‟s challenge might well be still with us." (p. 18; Engel's assessment).

## Positions taken

Engel groups the responses by the moral drawn: "It is not easy to say what the meaning of the tale might be. At least four kinds of morals have been drawn, whether or not they were actually intended by Carroll himself." (draft p. 2). The list follows his grouping, unranked; owners and dates are given for each.

1. **A rule of inference is not a premise (Engel's first moral).**
   - *Carroll's own diagnosis,* as Engel quotes it from a letter to the editor of *Mind* (via Smiley 1995): "This is Carroll‟s own diagnosis when he explains his article to the Editor of Mind: “My paradox turns on the fact that in an Hypothetical, the truth of the Protasis, the truth of the Apodosis, and the validity of the sequence are three distinct propositions.”" (p. 2). Engel's gloss: "In other terms, we can neither treat a rule of inference, such as Modus ponens ( MP), as conditionals, nor as premises. Once we respect this distinction, Carroll‟s regress cannot start." (p. 2). Engel lists, for this line, "Peirce 1902 ( Collected Papers 2.27), Russell 1903, p. 35, note, Ryle 19 45-46, Brown 1954,Geach 1965, Thomson 1960, Smiley 1995" (n. 4); of these only Russell was read here.
   - *Russell 1903, "therefore" vs "implies":* "At first sight, it might be thought that this would enable us to assert q provided p is true and implies q. But the puzzle in question shows that this is not the case, and that, until we have some new principle, we shall only be led into an endless regress of more and more complicated implications, without ever arriving at the assertion of q." and "We need, in fact, the notion of therefore, which is quite different from the notion of implies, and holds between different entities." (§ 38). He adds that the principle "eludes formal statement, and points to a certain failure of formalism in general." (§ 38).
   - *Dummett,* per Engel: "Dummett‟s diagnosis is very much along the lines of 1) above" (p. 4); Dummett's *Frege* (1973) was not read here.
   - *Ryle 1950/1954 and Geach 1965,* per Engel only: "Ryle 1954, although he notoriously takes the modus ponens rule to be an “inference ticket” to the conclusion, to which Geach (1965) objects that if the inference from the premisses to the conclusion is valid, there is neither need of a supplementary premiss nor of a licence for going from the premises to the conclusion." (n. 12). Ryle's *If, So, and Because* first appeared in M. Black (ed.), *Philosophical Analysis* (Cornell, 1950), pp. 323–340, per the review record [doi:10.1017/s0022481200101136](https://doi.org/10.1017/s0022481200101136); Engel cites its 1954 reprint in *Dilemmas*. Its text was not read here.
2. **Understanding, and knowing how (Engel's second moral).** Engel: "The second moral has to do with the epistemology of understanding." (p. 2): someone who accepts P and if P then Q but not Q either does not understand *if* or is not sincere (Engel citing Black 1970 and Brown 1954). A variant: "Our knowledge of the rule is not a form of knowledge that or propositional" knowledge "but a form of knowledge how" (pp. 2–3), which Engel calls Ryle's reaction.
   - *Ryle 1946,* as quoted by Pavese: "Knowing a rule of inference is not possessing a bit of extra information but being able to perform an intelligent operation. Knowing a rule is knowing how. It is realized in performances which conform to the rule, not in theoretical citations of it." (SEP "Knowledge How" §1.4, quoting Ryle 1946: 7; Ryle 1946 is [doi:10.1093/aristotelian/46.1.1](https://doi.org/10.1093/aristotelian/46.1.1), not read here). See also [knowledge](../vocabulary/knowledge.md).
   - *Stroud 1979* (*Inference, Belief, and Understanding*, *Mind* 88, pp. 179–196, [doi:10.1093/mind/lxxxviii.1.179](https://doi.org/10.1093/mind/lxxxviii.1.179)), as quoted by Engel (p. 12): "The additional factor cannot be identified as simply some further proposition he accepts or acknowledges. There must always exist some “non propositional” factor if any of his beliefs are based on others.”" (Stroud 1979: 189). Stroud's paper itself was not read here.
   - *Winch 1958,* as Wikipedia reports him: "Learning to infer is not just a matter of being taught about explicit logical relations between propositions; it is learning to do something" (*The Idea of a Social Science*, p. 57, per the article rev. 1374160185; not read here).
   - *Rule-following reading,* per Engel: "One could also read the tale as a version of Wittgenstein‟s “scepticism” about rules, as it is interpreted by Kripke (1981)." He adds: "Of course given that neither Carroll nor the Tortoise had heard about Kripke, this interpretation is far fetched, but there are clear similarities with Wittgenstein‟s problem." (p. 3; Engel's assessment).
3. **The justification of logic (Engel's third moral).** "The third kind of interpretation concerns the justification of logical laws." (p. 3).
   - *Quine 1936 against conventionalism:* "This is indeed Quine‟s famous argument against Carnap‟s conventionalism about logic in “Truth by convention”. Quine explicitly refers to Lewis Carroll‟s regress when he mounts his argument." (Engel p. 3; also SEP "Logical Truth" §1.1, quoted above).
   - *Rule-circularity (Boghossian 2000):* any inferential justification of modus ponens (MPP) is "rule-circular": "This brings us, then, to the inferential path. Here there are a number of distinct possibilities, but they would all seem to suffer from the same master difficulty: in being inferential, they would have to be rule-circular." (p. 231). Of the truth-table argument for MPP: "As is clear, however, this justification for MPP must itself take at least one step in accord with MPP." (p. 231). He reports that "And many philosophers have maintained that a rule-circular justification of a rule of inference is no justification at all." (p. 231), and grants that "At a minimum, then, the sceptical context discloses that a rule-circular argument for MPP would beg a sceptic's question about MPP and would, therefore, be powerless to quell his doubts about it." (p. 246); the chapter goes on to defend a constrained rule-circular justification (not excerpted). As Engel quotes Boghossian 2002: "At some point it must be possible to use a rule in reasoning in order to arrive at a justified conclusion, without this use needing to be supported by some knowledge about the rule one is relying on." (Engel pp. 12–13).
   - *A deductive sceptic:* "In other words the Tortoise would be a radical sceptic about deduction, just as Hume is sceptic with respect to induction." (Engel p. 4, as a reading).
4. **The normative force of logic (Engel's fourth moral).** "Either she is a sort of akratic in the domain of logical inference, seeing what she ought to infer, but failing to comply, or she explicitly questions the normative power of the logical must." and "In parallel fashion, the Tortoise would be a sceptic about the power of logical reasons to force us to believe any sort of conclusion." (p. 4). Engel cites Blackburn 1995 ("Practical Tortoise Raising", *Mind* 104, pp. 695–711, [doi:10.1093/mind/104.416.695](https://doi.org/10.1093/mind/104.416.695); not read here) for this line. His verdict on Dummett: "So it is not obvious that the Tortoise‟s challenge about the force of logical reasons has been appropriately answered." (p. 17; Engel's assessment).

**Against the inferentialist reply, as reported.** Pavese (SEP §1.4) reports a reply to the Rylean regress — "One might respond (cf. Stanley 2011b) to this regress challenge that the student does not really understand the premises of an argument by modus ponens (p, if p then q), for that involves grasping the concept of a conditional, and on an inferentialist understanding (Boghossian 1996, 2003), that would dispose one to accept the conclusion of an inference by that rule." — and an objection to it: "Inferentialism about meaning is, however, a controversial doctrine (for several criticisms, see Williamson 2011, 2012)." Both are Pavese's report.

## Arguments in play

(none recorded as separate argument pages yet). The regress as Carroll stages it
and the propositional check are in The question; the rule-circularity argument is
in Positions taken, 3. Engel recasts reasoning by belief in a rule as a
three-step inference — "(i) Any inference of the form MP is valid", "(ii) This particular inference ( from A and B to Z) is of MP form", "(iii) Hence this particular inference ( from A and B to Z) is valid" — and names the view: "Let us call this reflective internalism." He then says: "Reflective internalism is the psychological counterpart of the Carroll story." (draft p. 12).

## Thinkers who addressed it

- **Lewis Carroll** (*Mind* 1895) — the dialogue; the diagnosis quoted by Engel.
- **Bertrand Russell** (*Principles of Mathematics*, 1903, § 38) — "therefore" vs "implies".
- **Gilbert Ryle** (1946, Proc. Aristotelian Soc. 46: 1–16; *If, So, and Because*, 1950) — knowing how; inference tickets (per Pavese and Engel).
- **W. V. O. Quine** (*Truth by Convention*, 1936) — argument against conventionalism, "derived from Carroll 1895" (SEP "Logical Truth" §1.1).
- **Peter Winch** (1958) — per Wikipedia.
- **Michael Dummett** (*Frege*, 1973) — per Engel, first-moral diagnosis.
- **Barry Stroud** (*Mind* 1979) — the "non propositional" factor, via Engel.
- **Simon Blackburn** (*Mind* 1995) and **Timothy Smiley** ("A Tale of Two Tortoises", *Mind* 104, pp. 725–736, [doi:10.1093/mind/104.416.725](https://doi.org/10.1093/mind/104.416.725)) — papers in *Mind* 104(416), 1995, the issue that carries the reprint; texts not read.
- **Paul Boghossian** (2000; 2002 and 2003 as cited by Engel and Pavese) — rule-circularity; reasoning without knowledge about the rule.
- **Pascal Engel** (2005) — four readings; the normative-force reading.
- **Carlotta Pavese** (SEP 2021/2024) — Ryle's version and replies.

## Framings and reframings

- **Is it a paradox?** Engel: "It is not clear, however, that this puzzle is a genuine paradox, in the ordinary sense of a set of acceptable premisses leading to an unacceptable conclusion through apparently acceptable rules of inference, for in the case at point precisely nothing is is inferred from the premisses." (draft p. 1 n. 1). Wikipedia files it under "Logic" as "Also known as Carroll's paradox" (rev. 1376699902).
- **A race-course of premises.** After Zeno's race, the Tortoise offers its own: "Well now, would you like to hear of a race-course, that most people fancy they can get to the end of in two or three steps, while it really consists of an infinite number of distances, each one longer than the previous one?" (p. 278).
- **Compulsion by logic.** Achilles' appeal — "Then Logic would take you by the throat, and force you to do it!" (p. 280) — is answered by the Tortoise: "Whatever Logic is good enough to tell me is worth writing down," said the Tortoise.  (p. 280); Engel: "This is why her acknowledgement of the authority of logic is somewhat ironic" (p. 4).
- **First obstacle to conventionalism.** Wikipedia: "Carroll's dialogue is apparently the first description of an obstacle to conventionalism about logical truth, later reworked in more sober philosophical terms by W. V. O. Quine." (rev. 1374160185, citing Maddy 2012, [doi:10.2178/bsl.1804010](https://doi.org/10.2178/bsl.1804010), not read here).
- **Related pages.** The [rule-following paradox](rule-following-paradox.md) (Engel's Kripke–Wittgenstein reading; Boghossian's note); the [Agrippan trilemma](agrippan-trilemma.md) as another regress of justification (a structural note by this implant, G4; no source read draws the link); Carroll's other *Mind* puzzle is the [barbershop paradox](barbershop-paradox.md).

Not in the excerpts held: Ryle's *If, So, and Because* and Ryle 1946 (read only
as quoted), Stroud 1979 (read only as quoted by Engel), Boghossian 2002 and 2003, Dummett 1973, Smiley 1995, Blackburn 1995, Brown 1954, Geach 1965,
Thomson 1960, Winch 1958, Maddy 2012, Soames 2018, Gómez-Torrente 2019. The SEP
Fall 2024 entries *Logical Consequence*, *Classical Logic* and *The Normative Status of Logic*
were searched (archive HTML, 2026-10-01) and contain no mention of Carroll or the Tortoise.

## Vocabulary

- [Validity](../vocabulary/validity.md) — Carroll's "validity of the sequence"; the check above.
- [Argument](../vocabulary/argument.md) — premises versus rule of inference.
- [Paradox](../vocabulary/paradox.md) — whether this is one (Engel, above).
- [Knowledge](../vocabulary/knowledge.md) — knowing how vs knowing that (Ryle).
- [Classical logic](../methods/classical-logic.md) — material conditional and modus ponens in the check.
- *Modus ponens*, *rule of inference*, *rule-circularity*, *conventionalism*, *inferentialism*, *entitlement* — open work in [vocabulary](../vocabulary/index.md).
