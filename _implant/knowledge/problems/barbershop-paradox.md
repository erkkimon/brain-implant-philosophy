---
type: article
about: concept
title: "The barbershop paradox"
description: "Three barbers, Allen, Brown and Carr; 'if Carr is out, then if Allen is out Brown is in' and 'if Allen is out Brown is out' — can Carr ever be out? Lewis Carroll's 'A Logical Paradox' (Mind 1894) and its questions about hypotheticals, the replies of Sidgwick, Johnson, Venn, Russell (Principles §19 n. 1, material implication), Jones and Cook Wilson, the encyclopedia assessments, and a propositional check of the material-implication reading."
tags: [problem, paradox, logic, conditionals, history-of-logic]
timestamp: 2026-10-08T19:52:29Z
---

# The barbershop paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Primary text: Lewis Carroll, "A Logical Paradox", *Mind* N.S. 3(11), July 1894,
pp. 436–438, [doi:10.1093/mind/III.11.436](https://doi.org/10.1093/mind/III.11.436)
(excerpt: `raw/carroll-1894-a-logical-paradox-mind.md`). Replies in *Mind*
1894–1905 (excerpt: `raw/mind-1894-1905-replies-to-carrolls-logical-paradox.md`);
Venn 1894 (`raw/venn-1894-symbolic-logic-alices-problem.md`); Russell 1903
(`raw/russell-1903-principles-19-note-carrolls-paradox.md`). Maps: Marion,
[SEP Fall 2024 "John Cook Wilson"](https://plato.stanford.edu/archives/fall2024/entries/wilson/) §1;
Abeles, [IEP "Lewis Carroll: Logic"](https://iep.utm.edu/lewis-carroll/)
(excerpts: `raw/encyclopedias-barbershop-paradox-sep-wilson-iep-carroll-wikipedia.md`).
Admitted from Wikipedia's List of paradoxes, revision 1376699902, "Logic". Not to be confused with the [barber paradox](barber-paradox.md).

## The question

In Carroll's story Uncle Jim hopes the barber Carr will be in; Uncle Joe claims he can prove it. Two premisses are granted. First: "Do you grant me that, if Carr is out, it follows that if Allen is out Brown must be in?" — Uncle Jim: "Of course he must," (¶¶ 19–20), since otherwise there would be nobody in the shop. Second, Uncle Jim says of Allen "that ever since he had that fever he’s been so nervous about going out alone, he always takes Brown with him." (¶ 26).
Uncle Joe's argument: "Then if Carr is out, we have two Hypotheticals, “if Allen is out Brown is in” and “If Allen is out Brown is out,” in force at once. And two incompatible Hypotheticals, mark you! They ca’n’t possibly be true together!" (¶ 29), and so: "If Carr is out, these two Hypotheticals are true together. And we know that they cannot be true together. Which is absurd. Therefore Carr cannot be out. There’s a nice Reductio ad Absurdum for you!" (¶ 33).
Uncle Jim's counter: "If Allen is out Brown is out. If Carr and Allen are both out, Brown is in. Which is absurd. Therefore Carr and Allen ca’n’t be both of them out. But, so long as Allen is in, I don’t see what’s to hinder Carr from going out." (¶ 34). The story breaks off at the shop door: "But, just at this moment, we arrived at the barber’s shop; and, on going inside, we found——" (¶ 36).

Carroll's abstract form, in his Note: "(1) If C is true, then, if A is true, B is not true;" "(2) If A is true, B is true." "The question is, can C be true?" (¶¶ 42–44). Wikipedia's list entry: "Barbershop paradox: The supposition that, "if one of two simultaneous assumptions leads to a contradiction, the other assumption is also disproved" leads to paradoxical consequences. Not to be confused with the Barber paradox." (rev. 1376699902).

**Propositional check (this implant, 2026-10-01; logic, not a position).**
Let *c*, *a*, *b* stand for *Carr is out*, *Allen is out*, *Brown is out* (Carroll's
"true"/"not true" read as "out"/"in", ¶ 45), with *if … then* read as the
material conditional.
1. `logic.py check --premises "c -> (a -> ~b)" "a -> b" --conclusion "~c"` outputs `INVALID` with counterexample rows `a=F, b=T, c=T` and `a=F, b=F, c=T`: on this reading Uncle Joe's conclusion does not follow, and Carr is out in both rows while Allen is in.
2. The same premisses with `--conclusion "c -> ~a"` output `VALID`.
3. `--premises "a -> b" "a -> ~b" --conclusion "~a"` outputs `VALID`, and `--premises "~q" --conclusion "(q -> r) & (q -> ~r)"` outputs `VALID`: the two "incompatible" hypotheticals are jointly satisfiable exactly when the shared antecedent is false.
4. Adding Carr out as a premiss (`"c -> (a -> ~b)" "a -> b" "c"`, conclusion `"c & ~c"`) outputs `INVALID` (rows `a=F, b=T, c=T` and `a=F, b=F, c=T`): the three are consistent.
5. Carroll's four forms (¶¶ 53–56): `"(c & a) -> ~b"` ⊢ `"c -> (a -> ~b)"`, `"c -> (a -> ~b)"` ⊢ `"a -> (c -> ~b)"`, `"a -> (c -> ~b)"` ⊢ `"~(a & b & c)"` and `"~(a & b & c)"` ⊢ `"(c & a) -> ~b"` each output `VALID`, so on the material reading the four are equivalent.
6. The shop rule as a premiss: `--premises "~a | ~b | ~c" "a -> b"` outputs `VALID` for `"~a | ~c"` and `INVALID` for `"~c"` (rows `a=F, b=T, c=T` and `a=F, b=F, c=T`).
The tool reads every conditional as material and has no tense, modality or
Hypotheticals "in force" (¶ 29); whether that reading fits Carroll's hypotheticals is
what the respondents below dispute.

## Why it matters

- **Carroll's own claim.** "The paradox, of which the forgoing paper is an ornamental presentation, is, I have reason to believe, a very real difficulty in the Theory of Hypotheticals." (Note, ¶ 38); he adds that "the various and conflicting opinions, which my correspondence with them has elicited, convince me that the subject needs further consideration, in order that logical teachers and writers may come to some agreement as to what Hypotheticals are, and how they ought to be treated." (¶ 38).
- **Questions Carroll lists.** "Can a Hypothetical, whose protasis is false, be regarded as legitimate?" (¶ 50); "Are two Hypotheticals, of the forms “If A then B” and “If A then not-B,” compatible?" (¶ 51); and the difference in meaning, if any, between four forms beginning "(1) A, B, C, cannot be all true at once;" (¶¶ 52–56).
- **Material implication.** Russell cites it as a case of his principle: "The principle that false propositions imply all propositions solves Lewis Carroll’s logical paradox in Mind, N. S. No. 11 (1894)." (*Principles* §19 n. 1). Abeles (IEP): "Bertrand Russell used the barber shop problem in his Principles of Mathematics to illustrate his principle that a false proposition implies all others." See [paradoxes of material implication](paradoxes-of-material-implication.md).
- **History of logic.** Abeles (IEP) reads Carroll's drafts as showing his development: "The many versions the Barbershop Paradox that Dodgson developed demonstrate an evolution of his thoughts on hypotheticals and material implication in which the connection between the antecedent and the consequent of the conditional (if (antecedent), then (consequent)) is formal, that is, it does not depend on their truth values." Marion (SEP §1) links its origin to that of [What the Tortoise Said to Achilles](tortoise-and-achilles.md): "Cook Wilson was also involved on the same occasion in the genesis of Carroll’s better-known ‘paradox of inference’, in ‘What the Tortoise Said to Achilles’ (Carroll 1895),".

## Positions taken

No grouping of the responses was found in the sources read; they are listed
by owner in order of publication, unranked.

- **Uncle Joe's side: Carr cannot be out (the reductio).** Stated in the story, ¶¶ 29–35; Carroll's Note (¶¶ 38–66) poses questions and states no answer. Uncle Joe's reply to the counter: "Don’t you see that you are wrongly dividing the protasis and the apodosis of the Hypothetical? Its protasis is simply “Carr is out”; and its apodosis is a sort of sub-Hypothetical, “If Allen is out, Brown is in”." (¶ 35). Abeles (IEP): "It is the transcription of a dispute which opposed him to John Cook Wilson." Wikipedia's article, citing Bartley (1977): "Cook Wilson's view is represented in the story by the character of Uncle Joe, who attempts to prove that Carr must always remain in the shop." (rev. 1370692118). Cook Wilson's own 1905 note, below, rejects the conclusion that Carr's absence is impossible; the sources read do not reconcile the two.
- **Sidgwick (Mind, Oct. 1894, p. 582; Jan. 1895, p. 143): the two hypotheticals are not to be made compatible.** "the second premiss “If A then B” is stated as a fact, quite independently of the truth of C; while “If A, then not B” is not stated as a fact, but as being possibly false." Making them compatible requires A false, and "this assumption is not only not warranted by anything in the premisses, but would render each of the ‘compatible’ propositions meaningless as hypotheticals; they would become mere denials of the existence of certain classes." In 1895: "in the context in which it is here placed, it requires to be taken in a less negative sense than this" ("this" being "the conjunction of A with B is false"), and "It is evident that Lewis Carroll has tacitly assumed, what Mr Johnson’s treatment of hypotheticals assumes openly, that these propositions are equivalent."
- **Johnson (Mind, Oct. 1894, p. 583; Jan. 1895, pp. 143–144): "If Carr is out Allen is in".** "But in reality the two sub-hypotheticals which form his principal consequents are not incompatible. For in saying that two propositions are incompatible we mean that their combination involves a logical impossibility." Hence "the two principal hypotheticals of which these are the consequents prove “If Carr is out Allen is in.”" His reading of the conditional: "As regards the hypothetical of the general form “If A then B” we have interpreted this as the mere denial of the conjunction “A true and B false.”" Against Sidgwick: "he is simply begging the question at issue." and "For the import or force of a given form of words is altogether unaffected by its possible falsity."
- **Venn (*Symbolic Logic*, 2nd ed., 1894, pp. 442–443): C can be out.** He calls it "Alice's Problem" and treats it in class algebra: "We are then asked, Must C = 0? It is almost intuitively obvious that, on all the principles hitherto laid down, the answer must be in the negative." In the barbers' reading: "If they denote the absence and presence of individuals, then we interpret by saying that C may go out when A remains at home, whether or not B goes out." On the hypotheticals: "But to us there is no difficulty in such an implication, whether under such a condition as C, or without any condition."
- **Russell (*Principles of Mathematics*, 1903, §19 n. 1): material implication.** "But in virtue of our definition of negation, if q be false both these implications will hold: the two together, in fact, whatever proposition r may be, are equivalent to not-q." and "Thus the only inference warranted by Lewis Carroll’s premisses is that if p be true, q must be false, i.e. that p implies not-q; and this is the conclusion, oddly enough, which common sense would have drawn in the particular case which he discusses." (Abeles maps *p*, *q*, *r* to Carr, Allen, Brown out: "Russell asserted that the only correct inference from (1) and (2) is: if p is true, q is false, that is, if Carr is out, Allen is in. (Russell 1903, p. 18)").
- **Jones (Mind, Jan. 1905, pp. 146–148): a Mill-type reading of "if".** Her view is "a modification of that propounded by J. S. Mill, according to whom If A then C means The proposition C is a legitimate inference from the proposition A." She objects "to calling Carr is out the “ Principal Antecedent,” and think that the whole root of the matter is that Carr is out is not the Antecedent of (2)." Two hypotheticals with contradictory consequents disprove their antecedent, she argues, only "if A gives the whole ground for the contradictory conclusions"; her derivation ends "Therefore if C is out, A is in."
- **Cook Wilson ("W.", Mind, Apr. 1905, pp. 292–293): "a mere verbal fallacy".** Attribution of "W." per SEP's bibliography item CLP. "It is difficult to see how this argument, which is no paradox but a paralogism, should have been taken seriously, and that the fallacy in it should not have had its true character made clear nor have received the simple treatment of which it is capable." His conclusion: "Thus the conclusion is that the conjunction of Carr’s absence and Allen’s absence is impossible, not that Carr’s absence is impossible." His diagnosis: "But the proposition ‘If Allen is out Brown is in’ is a universal proposition which if valid at any time is valid at all times; it represents a rule which is always valid." Of Jones: "The attempt to solve the ‘puzzle’ in the January number of Mind fails in all points."

**Encyclopedia assessments, attributed.** Marion (SEP §1) writes that "Russell had already satisfactorily resolved it in a footnote to The Principles of Mathematics (Russell 1903, 18)." Abeles (IEP) writes: "Bertrand Russell gave what is now the generally accepted conclusion to this problem in his 1903 book, The Principles of Mathematics." Abeles reports Bartley's assessment: "Bartley remarks in his book that the Barbershop Paradox is not a genuine logical paradox as is the Liar Paradox." Wikipedia's article states, without a source on that sentence: "From the viewpoint of modern logic, it is seen not so much as a paradox than as a simple logical error." (rev. 1370692118). Structural note (this implant): among the texts read, Sidgwick (1895) and Jones (1905) are the ones that reject reading "if" as Johnson and Russell do; no later text on either side was read.

## Arguments in play

(none recorded as separate argument pages yet). The forms used are in The question:
- **Uncle Joe's reductio:** from *c* derive two hypotheticals "in force", judge them incompatible, conclude ~*c* (¶¶ 29–33).
- **Uncle Jim's / Johnson's / Russell's re-division:** apply the reductio to the inner antecedent, concluding *c* → ~*a* (¶ 34; Johnson 1894; Russell 1903) — check 2 above.
- **Cook Wilson's "direct argument"** from "Either Allen is in, or Brown is in, or Carr is in" and "If Allen is out Brown is out" to "Either Allen is in, or Carr is in" (1905, p. 292, summarised in the raw file) — check 6 above.
- **Sidgwick's modus tollens reading**, which Johnson calls "begging the question at issue" (1895).

## Thinkers who addressed it

- **Lewis Carroll (C. L. Dodgson)** — "A Logical Paradox", *Mind* 1894; per Abeles (IEP), versions also in his papers and a 1899 *Educational Times* question (14122).
- **John Cook Wilson** — the dispute's origin (SEP §1; IEP); "W." 1905, [doi:10.1093/mind/XIV.2.292](https://doi.org/10.1093/mind/XIV.2.292). IEP: "Wilson believed that all propositions are categorical and therefore hypotheticals could not be propositions."
- **Alfred Sidgwick** — [doi:10.1093/mind/III.12.582](https://doi.org/10.1093/mind/III.12.582); [doi:10.1093/mind/IV.13.143-a](https://doi.org/10.1093/mind/IV.13.143-a).
- **W. E. Johnson** — [doi:10.1093/mind/III.12.583-a](https://doi.org/10.1093/mind/III.12.583-a); [doi:10.1093/mind/IV.13.143-b](https://doi.org/10.1093/mind/IV.13.143-b).
- **John Venn** — *Symbolic Logic*, 2nd ed., Macmillan 1894 ([archive.org scan](https://archive.org/details/symboliclogic02venngoog)).
- **Bertrand Russell** — *Principles of Mathematics* (1903) §19 n. 1 ([transcription](https://fair-use.org/bertrand-russell/the-principles-of-mathematics/s.19)).
- **E. E. Constance Jones** — [doi:10.1093/mind/XIV.1.146](https://doi.org/10.1093/mind/XIV.1.146).
- **J. N. Keynes** — per Abeles, included the problem "as an exercise in chapter IX of the 1906 edition of his book" (not read).
- **Hugh MacColl, H. W. Curjel** — solutions to the 1899 version, per Abeles (not read).
- **W. W. Bartley III** (ed., Carroll's *Symbolic Logic* Part II, 1977) and **Amirouche Moktefi** (2007, 2008; cited by SEP §1) — historians of the episode (not read).

## Framings and reframings

- **Hypotheticals as material conditionals.** Johnson's "mere denial of the conjunction" and Russell's "false propositions imply all propositions" make the two hypotheticals compatible when Allen is in; on that reading the propositional check above applies.
- **Hypotheticals in a context.** Sidgwick's framing: the clause "If A, then not B" "is not stated as a fact, but as being possibly false", so its sense depends on context (1894; 1895).
- **Hypotheticals as inference.** Jones's Mill-type reading, where "If A then C" says C is "a legitimate inference" from A (1905).
- **Rules and times.** Cook Wilson's framing: a hypothetical "valid at any time is valid at all times", so it cannot be a consequence of Carr's being out (1905).
- **Classes rather than propositions.** Venn reads the letters as classes and the conclusion as class emptiness ("Must C = 0?"); Abeles reports that Carroll's own early versions also used classes: "In the earlier versions, he expressed a hypothetical proposition in terms of classes, that is, if A is B, then C is D. Only later did he designate A, B, C, and D as propositions."
- **Kinship.** Marion (SEP §1) places its genesis beside the [tortoise and Achilles](tortoise-and-achilles.md); Abeles: "Both the Barbershop and Achilles paradoxes involve conditionals and Dodgson employed material implication to argue them, but he was uncomfortable with it."

Not in the excerpts held: Bartley's eight versions and commentary, Moktefi's
studies, Keynes 1906, MacColl's and Curjel's solutions, Cook Wilson's 1905
correction (p. 439), and later treatments the Wikipedia article lists.

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — the label disputed by Cook Wilson ("no paradox but a paralogism") and, per Abeles, by Bartley.
- [Validity](../vocabulary/validity.md) — Carroll's "validity as a logical sequence" (¶ 23) and the checks above.
- [Fallacy](../vocabulary/fallacy.md) — Cook Wilson (1905, p. 293): "This is a mere verbal fallacy."
- [Argument](../vocabulary/argument.md) — premisses and the reductio form.
- [Classical logic](../methods/classical-logic.md) — the propositional check above.
- *Hypothetical*, *protasis*, *apodosis*, *material implication*, *reductio ad absurdum* — open work in [vocabulary](../vocabulary/index.md).

Related thinkers: [Russell](../thinkers/russell.md).
