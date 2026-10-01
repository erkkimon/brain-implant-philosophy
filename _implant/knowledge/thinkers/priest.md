---
type: article
about: person
title: Graham Priest
description: "Graham Priest (first academic post 1974; CUNY Graduate Center from 2009), co-coiner of dialetheism (1981), the view that some contradictions are true — the logic of paradox LP (1979), In Contradiction (1987) on the liar, the inclosure schema (Beyond the Limits of Thought, 1995/2002) and the dialetheic treatment of Curry's paradox, with the objections the SEP records."
tags: [thinker, logic, analytic, contemporary, paradox, dialetheism, priest]
timestamp: 2026-10-01T22:52:16Z
---

# Graham Priest

A hub page ([thinkers](index.md)). Every statement below reports a cited
source ([Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
[How claims are graded](../../conventions/how-claims-are-graded.md)). The
two SEP entries relied on are co-authored by Priest, so what they say of
his work is partly his own report.

## Facts a claim depends on

From his own website's third-person biography
(`raw/priest-website-about-education-and-appointments.md`;
[grahampriest.net, Wayback 2026-06-06](http://web.archive.org/web/20260606232236/https://grahampriest.net/)):

- Education: "He obtained his doctorate in mathematics at the London School of Economics".
- 1974, first post: "So, luckily, he got his first job (in 1974) in a philosophy department, as a temporary lecturer in the Department of Logic and Metaphysics" (at St Andrews).
- Then the University of Western Australia; "After 12 years at the University of Western Australia, he moved to take up the chair of philosophy at the University of Queensland", "and after 12 years there, he moved again to take up the Boyce Gibson Chair of Philosophy at Melbourne University" (where the page says he is now emeritus).
- 1995: "He was elected a Fellow of the Australian Academy of Humanities in 1995".
- 2009: "In 2009 he took up the position of Distinguished Professor at the Graduate Center , City University of New York".
- School: the SEP "Paraconsistent Logic" entry places him in the Canberra relevant-logic group: "A school developed around them in Canberra which included Brady and Mortensen, and later Priest who, together with R. Routley, incorporated dialetheism to the development." (Priest, Tanaka & Weber, [SEP 2022](https://plato.stanford.edu/archives/fall2024/entries/logic-paraconsistent/), §1.3).
- 1981, the word: "The word ‘dialetheism’ was coined by Graham Priest and Richard Routley (later Sylvan) in 1981 (Priest et al. 1989, p. xx)." (Priest, Berto & Weber, [SEP 2024](https://plato.stanford.edu/archives/fall2024/entries/dialetheism/), §1).

No birth year is given in the sources read; none is stated here.

## Problems addressed

The position throughout is dialetheism: "Dialetheism is the view that some contradictions are true." (SEP 2024, §1). Its standard pairing with a
non-explosive logic: "By adopting a paraconsistent logic, a dialetheist can countenance some contradictions without being thereby committed to countenancing everything and, in particular, all contradictions." (§1). The
entry records that "Probably the master argument used by modern dialetheists invokes the logical paradoxes of self-reference." (§3.1); see
[paradox](../vocabulary/paradox.md).

- **[Liar paradox](../problems/liar-paradox.md).** Position: the liar
  sentences are true and false. Priest, Berto & Weber report that in the
  theory of Priest 1987 the truth predicate obeys the unrestricted T-schema
  and "It is admitted that some sentences—notably, the Liars—are truth-value gluts, that is, both true and false" (§3.2). Against
  [Tarski](tarski.md)'s stratification: "Dialetheists agree, but draw the conclusion in the other direction: the appropriate formalization of a language such as ours, because it is semantically closed and is not hierarchically stratified, will be inconsistent (Priest 1987, Ch. 1, Beall 2009, Ch. 1)." (§3.2).
  Work: *In Contradiction* (1987; 2nd edn 2006), ch. 1.
- **The logic of paradox, LP.** Priest, Tanaka & Weber (SEP 2022, §3.6),
  after three-valued tables over *t*, *b*, *f* with *t* and *b* designated:
  "If we define a consequence relation in terms of preservation of these designated values, then we have the paraconsistent logic LP (Priest 1979). In LP, ECQ is invalid." The same section: "Hence modus ponens for \(\supset\) is invalid in LP."
  Work: "The logic of paradox" (1979).
- **Inclosure schema and uniform solution.** "Priest argues that the paradoxes share an underlying structure (which he calls the Inclosure Schema in Priest 2002)." and "This is used in tandem with what Priest dubs the principle of uniform solution (“same kind of paradox, same kind of solution”) to urge that, since all the set-theoretic and semantic paradoxes are of a kind, dialetheism presents a uniquely unified solution." (SEP 2024, §3.3).
  Work: *Beyond the Limits of Thought* (1995; "Priest 2002" is its 2nd
  edn per the entry's bibliography); "The Structure of the Paradoxes of
  Self-Reference" (1994), cited for uniform solution in the SEP "Curry's
  Paradox" entry.
- **[Russell's paradox](../problems/russells-paradox.md).** Set-theoretic
  paradoxes fall under the same treatment in the SEP report (§3.3); the
  paraconsistent response and its critics are on the problem page, citing
  *In Contradiction* 2006, ch. 18 (bibliographic only).
- **[Curry's paradox](../problems/currys-paradox.md).** "A dialetheist, though, cannot simply accept that the Curry sentence is both true and false, because if it is true then \(\bot\) follows." The reported response: "A standard dialetheic strategy to deal with the Curry paradox has consisted in exploiting paraconsistent logics with a ‘noncontractive’ conditional (see again Priest 1987, Ch, 6, Beall 2009, Ch. 2)" (SEP 2024, §3.3). Shapiro & Beall (SEP "Curry's Paradox", §5.2) report that "Priest evaluates Liar sentences as both true and false, whereas he rejects the claim that Curry sentences are true."
- **The law of non-contradiction in Aristotle.** "A critical analysis of Aristotle’s arguments is given point for point by Priest (1998b/2006 Ch. 1), who finds them to often conflate dialetheism with trivialism" (SEP 2024, §4).
- **Madhyamaka.** "On a dialetheic interpretation, advocated by Priest, Garfield, and Deguchi (see Priest 2002 Ch. 16, Deguchi et al. 2008), readers should take Nagarjuna and others in the Madhyamaka school at their word" (§2.2); see [Mūlamadhyamakakārikā](../works/mulamadhyamakakarika.md).

**Structural note (implant's own, logic shown).** *Ex contradictione
quodlibet* checked classically with `logic.py check --premises "p" "~p" --conclusion "q"`:

```
VALID
premises are jointly inconsistent — argument is vacuously valid
```

The tool is two-valued. The counter-model SEP gives for LP (p = *b*,
q = *f*, so p and ¬p designated and q not; SEP 2022 §3.6) uses the third value
*b*, which the tool does not model; the two results concern different
logics and do not conflict.

## Works

Held bibliographically only (DOIs verified by content negotiation,
2026-09-27; no sentence of these is quoted here). Works pages are not yet
written ([works](../works/index.md)).

- "The logic of paradox", *Journal of Philosophical Logic* 8(1), 1979,
  pp. 219–241 (pages per SEP). DOI: [10.1007/BF00258428](https://doi.org/10.1007/BF00258428).
- *In Contradiction: A Study of the Transconsistent*, Dordrecht: Martinus
  Nijhoff, 1987, DOI: [10.1007/978-94-009-3687-4](https://doi.org/10.1007/978-94-009-3687-4);
  2nd expanded edn, OUP 2006, DOI: [10.1093/acprof:oso/9780199263301.001.0001](https://doi.org/10.1093/acprof:oso/9780199263301.001.0001).
  Locators by chapter.
- "The Structure of the Paradoxes of Self-Reference", *Mind* 103(409),
  1994, pp. 25–34. DOI: [10.1093/mind/103.409.25](https://doi.org/10.1093/mind/103.409.25).
- *Beyond the Limits of Thought*, CUP 1995 (no DOI found); 2nd expanded
  edn, OUP 2002, DOI: [10.1093/acprof:oso/9780199254057.001.0001](https://doi.org/10.1093/acprof:oso/9780199254057.001.0001).
- SEP co-authorships: "Dialetheism" (with Berto & Weber; rev. 2024) and
  "Paraconsistent Logic" (with Tanaka & Weber; rev. 2022).

Excerpts: `raw/sep-dialetheism-fall-2024-priest-liar-inclosure-curry-objections.md`,
`raw/sep-logic-paraconsistent-fall-2024-lp-and-dialetheism-distinction.md`,
`raw/sep-curry-paradox-fall-2024-construction-lemma-and-responses.md`.

## In dialogue with

- **[Eubulides](eubulides.md)** — liar: "the standard Liar is attributed to the Greek philosopher Eubulides, probably the greatest paradox-producer of antiquity" (SEP 2024, §3.2; the "greatest" assessment is the entry authors').
- **Aristotle** — law of non-contradiction; Priest's analysis as above (SEP 2024, §4).
- **[Tarski](tarski.md)** — liar: "Tarski, in short, identified the cause of the semantic paradoxes to be semantic closure—the fact that natural languages such as English satisfy the T-schema." (SEP 2024, §3.2); Priest draws the opposite conclusion (above).
- **Richard Routley (Sylvan)** — co-coiner and collaborator: "In the collaboration between Priest and Routley, the contemporary dialetheic program was launched." (SEP 2024, §2.4).
- **Jc Beall** — a second dialetheic truth theory: "The two most prominent such theories to date are presented in Priest 1987 and Beall 2009." (§3.2, the entry authors' assessment); also a critic on Curry (Reception).
- **Hartry Field** — liar, paracomplete rival: "For a sustained critical engagement with paraconsistent dialetheism as a solution to the semantic paradoxes, see Field 2008, part 5 (chapters 23–26)." (§3.2).
- **Terence Parsons, Stewart Shapiro, Littman & Simmons, B. H. Slater** — critics named in SEP 2024 §§3.2, 4.2, 4.3 (Reception).

## Reception

Assessments as the SEP entries report them; none is the implant's.

**For.**
- Priest, Berto & Weber (SEP 2024, §2.4), on Priest's 1979 paper: "In 1979, Priest’s paper “The Logic of Paradox”, developed eventually into the book In Contradiction (1987/2006), presented what are now the most famous arguments for dialetheism."
- Shapiro, quoted in §3.2 as a critic stating the view's appeal: dialetheists "do not need to keep running through richer and richer meta-languages in order to chase our semantic tails…. We embrace some contradictions in the semantics, and get it all from the start. (Shapiro 2002, p. 818)"
- On explosion as an objection, the entry authors judge: "Since this argument assumes that Explosion is logically valid, it will carry no weight against a dialetheic paraconsistentist." (§4.1).

**Against.**
- Explosion: "A standard argument against dialetheism is to invoke the logical principle of Explosion, in virtue of which dialetheism would entail trivialism." (§4.1).
- Exclusion / expressing disagreement: "One argument from exclusion, with a more ad hominem twist, claims that the dialetheist has trouble with expressing disagreement with rival positions in debates (see Parsons 1990, Shapiro 2004, Littman and Simmons 2004)." Parsons: "How can he indicate that he genuinely disagrees with you? The natural choice is for him to say ‘\(A\) is not true.’ However, the truth of this assertion is also consistent with \(A\)’s being true—for a dialetheist, anyway. (Parsons 1990, p. 345)" (§4.2). Reply reported: "Priest has argued that the logical operation of negation should be distinguished from the speech acts of denial and the cognitive state of rejection." "Then the dialetheist can rule out that \(A\) is the case by denying \(A\); and this does not amount to the assertion of \(\neg A\) (Priest 2006, Ch. 6)." (§4.2).
- Negation / change of subject: "A version of this objection to dialetheism is due to Slater (1995); see also Restall 1993." (§4.3).
- Curry and uniform solution: "Stronger forms of the paradox, though, validity curry, seem to show that dropping these principles is not enough (Beall and Murzi 2013)." "Curry’s paradox puts pressure on the dialetheic story about uniform solution to the paradoxes. Beall (2014a, 2014b) urges this point; Weber et al. 2014 is a reply." (§3.3).
- Liar: Field 2008, part 5, as cited above (§3.2).

**Distinction the co-authors draw.** Priest, Tanaka & Weber (SEP 2022,
§1.1): "The view that a consequence relation should be paraconsistent does not entail the view that there are true contradictions." and "If this interpretative strategy is successful, we can separate LP from necessarily falling under dialetheism." (§3.6).

## Vocabulary

- *Dialetheia*, *dialetheism* — "Dialetheism is the view that some contradictions are true." (SEP 2024, §1); spelled with and without the "e".
- *Glut* — a sentence both true and false (§3.2).
- *Trivialism* — distinct from dialetheism (§1).
- *Paraconsistent* — a consequence relation that is not explosive (§1;
  SEP 2022 §1.1).
- *Rejection*, *denial* — distinguished from assertion of a negation (§4.2).
- *Inclosure schema*, *principle of uniform solution* (§3.3).

Normative entries: [paradox](../vocabulary/paradox.md),
[validity](../vocabulary/validity.md); the others are open work in
[vocabulary](../vocabulary/index.md).

Related problems: [the Hilbert–Bernays paradox](../problems/hilbert-bernays-paradox.md) (Priest 1997), [Yablo's paradox](../problems/yablos-paradox.md) (Priest 1997 on its self-reference), [the paradoxes of entailment and material implication](../problems/paradoxes-of-material-implication.md) (LP invalidates explosion, SEP "Paraconsistent Logic" §3.6).
