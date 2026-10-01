---
type: article
about: concept
title: The rule-following paradox
description: "If every course of action can be made out to accord with a rule, what makes one continuation correct, and what fact makes someone mean addition rather than quaddition? Wittgenstein's PI §201 and §§185–242, Kripke's 1982 quus sceptic and sceptical solution, and the responses on record (non-factualism, the community view, dispositionalism and its critics, non-reductionism, McDowell's and Stroud's dissolution) with their owners."
tags: [problem, paradox, philosophy-of-language, philosophy-of-mind, metaphysics]
timestamp: 2026-10-01T19:53:21Z
---

# The rule-following paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
claim grades as in [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Primary texts: Wittgenstein, *Philosophical Investigations* I §§185–242
(Anscombe tr., 1953/1958; excerpt:
`raw/wittgenstein-1953-philosophical-investigations-185-242-rule-following.md`);
Kripke, *Wittgenstein on Rules and Private Language* (Harvard UP, 1982,
ISBN 0-674-95401-7; excerpt: `raw/kripke-1982-wittgenstein-on-rules-and-private-language-quus.md`).
Maps: Miller & Sultanescu, [SEP Fall 2024 "Rule-Following and Intentionality"](https://plato.stanford.edu/archives/fall2024/entries/rule-following/)
(excerpt: `raw/sep-rule-following-fall-2024-sceptical-argument-and-responses.md`);
Candlish & Wrisley, [SEP Fall 2024 "Private Language"](https://plato.stanford.edu/archives/fall2024/entries/private-language/)
§4 (excerpt: `raw/sep-private-language-fall-2024-kripkes-sceptical-wittgenstein.md`);
Glüer, Wikforss & Ganapini, [SEP Fall 2024 "The Normativity of Meaning and Content"](https://plato.stanford.edu/archives/fall2024/entries/meaning-normativity/)
(excerpt: `raw/sep-meaning-normativity-fall-2024-kripke-and-simple-argument.md`);
Biletzki & Matar, [SEP Fall 2024 "Ludwig Wittgenstein"](https://plato.stanford.edu/archives/fall2024/entries/wittgenstein/)
§3.5 (excerpt: `raw/sep-wittgenstein-fall-2024-rule-following-pi-201.md`).
McDowell ([1984](https://doi.org/10.1007/BF00485246), *Synthese* 58: 325–363) and
Boghossian ([1989](https://doi.org/10.1093/mind/XCVIII.392.507), *Mind* 98: 507–549)
are cited by DOI-verified bibliographic data only and reported as the SEP authors report them.
The SEP authors' own assessments are marked as theirs; Miller, Glüer and
Wikforss appear in the bibliographies they survey.

## The question

Wittgenstein: "201. This was our paradox: no course of action could be determined by a rule, because every course of action can be made out to accord with the rule. The answer was: if everything can be made out to accord with the rule, then it can also be made out to conflict with it. And so there would be neither accord nor conflict here." (PI I §201).
The case that precedes it: "Now we get the pupil to continue a series (say +2) beyond 1000— and he writes 1000, 1004, 1008, 1012." and, corrected, "—He answers: “Yes, isn’t it right? I thought that was how I was meant to do it.”" (§185).

Kripke's version starts from the same sentence (1982, p. 7) and replaces the series with addition: "perhaps in the past I used ‘plus’ and ‘+’ to denote a function which I will call ‘quus’" (pp. 8–9).
Miller & Sultanescu summarise the function: "Quaddition yields the same result as addition if the numbers are lower than 57, and 5 otherwise, so the correct result of the aforementioned computation is ‘5’, not ‘125’." (SEP, §2; the computation is 68 + 57).
Kripke's conclusion on the sceptic's behalf: "This, then, is the sceptical paradox. When I respond in one way rather than another to such a problem as ‘68+57’, I can have no justification for one response rather than another. Since the sceptic who supposes that I meant quus cannot be answered, there is no fact about me that distinguishes between my meaning plus and my meaning quus." (p. 21), and "It seems that the entire idea of meaning vanishes into thin air." (p. 22).
Candlish & Wrisley state the finitude premise: "The application of the rule is potentially infinite, and bizarre interpretations of the rule, as well as the standard use of it, are compatible with any finite set of applications of the usual sort such as 7 + 14 = 21." (SEP "Private Language", §4).
Miller & Sultanescu tie the question to meaning in general: "meaning something by a linguistic expression is analogous to following a rule." (§1).

Kripke frames the two demands on an answer as Miller & Sultanescu quote them (1982: 11): a fact "that constitutes my meaning plus, not quus", which must also "show how I am justified in giving the answer ‘125’" — the entry names these the extensionality condition (§2.1) and the normativity condition (§2.2).

**Propositional check (this implant, 2026-10-01; logic, not a position).**
The survey of candidates has the form: let *f* be *some fact about me constitutes my meaning plus*, and *d*, *i*, *p* stand for three of the candidate kinds Kripke examines (dispositions, introspected states or images, a primitive state). `logic.py check --premises 'f -> (d | i | p)' '~d' '~i' '~p' --conclusion '~f'` returns `VALID`. Adding *a*, *I mean addition*, with premises `~f`, `a -> f` and conclusion `~a` returns `VALID` with `matches schema: modus tollens`; without the premise `a -> f`, `~f` to `~a` returns `INVALID` with counterexample row `a=T, f=F`. The step from *no fact* to *no meaning* therefore needs the conditional *a* → *f* as a premise; a sceptical solution, in Kripke's definition below (p. 66), concedes the sceptic's negative assertions, i.e. here ~*f*. The tool does not represent the infinitely many candidate facts or any modal content.

## Why it matters

- **Meaning and content.** Glüer, Wikforss & Ganapini: "Kripke presents us with a meaning skeptic who challenges the very idea that there are facts in virtue of which our terms have a meaning." (SEP, §2).
- **Private language.** Kripke: "The impossibility of private language emerges as a corollary of his sceptical solution of his own paradox, as does the impossibility of ‘private causation’ in Hume." (p. 68). Wittgenstein's next section: "Hence it is not possible to obey a rule ‘privately’: otherwise thinking one was obeying a rule would be the same thing as obeying it." (§202).
- **Normativity of meaning.** Miller & Sultanescu: "Kripke’s discussion has resulted in a vigorous debate about whether meaning really is normative, as well as about how the normativity of meaning is best understood." (§2.2).
- **Naturalism.** "Many have construed Kripke’s Wittgenstein as saying exactly that: it is part of his skeptical campaign against semantic facts in general that such facts cannot be reduced to whatever precisely is allowed in a naturalistic supervenience base for meaning/content." (Glüer, Wikforss & Ganapini, §4).
- **Theories of content.** "As Boghossian notes (1989 [2002: 164–165]), the general form of dispositionalism targeted by the sceptic covers both conceptual role theories and causal/informational theories." (Miller & Sultanescu, §4).
- **Induction.** Kripke asks: "should not the sceptical problem be obvious to any reader of Goodman?" (p. 20; see [the new riddle of induction](new-riddle-of-induction.md)).
- **Assessments of its weight.** Kripke: "The ‘paradox’ is perhaps the central problem of Philosophical Investigations." (p. 7) and "Personally I am inclined to regard it as the most radical and original sceptical problem that philosophy has seen to date, one that only a highly unusual cast of mind could have produced." (p. 60). Biletzki & Matar: "These considerations lead to PI 201, often considered the climax of the issue:" (SEP "Ludwig Wittgenstein", §3.5).

## Positions taken

Kripke's own grouping: "Call a proposed solution to a sceptical philosophical problem a straight solution if it shows that on closer examination the scepticism proves to be unwarranted; an elusive or complex argument proves the thesis the sceptic doubted." and "A sceptical solution of a sceptical philosophical problem begins on the contrary by conceding that the sceptic’s negative assertions are unanswerable." (p. 66). Miller & Sultanescu follow it (§3) and add responses that dissolve rather than solve (§5). Interpretive positions on what Wittgenstein meant come last. None is ranked here.

- **The sceptical solution (Kripke 1982).** "we can say that Wittgenstein proposes a picture of language based, not on truth conditions, but on assertability conditions or justification conditions" (p. 74); "Our community can assert of any individual that he follows a rule if he passes the tests for rule following applied to any member of the community." (p. 110). Candlish & Wrisley paraphrase it: Wittgenstein says, in effect, "“Unique meaning is unintelligible; rather, someone’s meaning the usual addition function when saying ‘plus’ consists in their being considered by a community to have passed the community’s test for employing that function.”" (SEP §4).
  - *Read as non-factualism:* "the standard view in the secondary literature is that Kripke’s Wittgenstein himself is proposing a form of semantic non-factualism in the sceptical solution outlined in chapter 3 of Kripke (1982). See, e.g., McGinn (1984), Wright (1984), Boghossian (1989), and Hale (2017)." (Miller & Sultanescu §3.2).
  - *Against:* "A prominent general line of argument in the recent literature suggests that irrealist views of any area make presuppositions that irrealist views of meaning and content are bound to deny, so that irrealism about meaning and content is ultimately incoherent (Boghossian 1989, 1990; Hattiangadi 2007, 2017, 2018; Miller 2011, 2015a, 2020)." (§3).
- **Factualism of another kind (Wilson 1994).** "Wilson takes the lesson of the sceptical argument to be not that there are no meaning facts, but rather that a certain conception of such facts, which he calls classical realism, is hopeless, and conceives of the sceptical solution as accommodating meaning facts when conceived in a different way (Wilson 1994; see also Wright 1992: chapter 6)." (§3.3).
- **Reductive dispositionalism (Horwich 1998, 2015; Blackburn 1984; Warren 2020).** "The most widely discussed attempt at a straight solution to the sceptical challenge is reductive dispositionalism." (§4); "(See Horwich 1998, 2010, 2012 for a systematic development of dispositionalism; an answer to Kripke’s challenge is articulated in Horwich 2015.)" On finitude: "Blackburn responds to the finitude problem by pointing out that familiar dispositional properties (such as fragility) are in a sense infinitary: “there is an infinite number of places and times and strikings and surfaces on which it could be displayed” (1984 [2002: 35])." On error: "Jared Warren admits that solving the finitude problem, thus construed, turns on solving the error problem (2020: 268), and proceeds to offer an attempted solution to that problem."
  - *Against:* the sceptic's three problems as the entry lists them: "The sceptic argues that dispositionalist theories face three problems. The first problem—the finitude problem—is that there is a sense in which, much like the totality of our previous linguistic behaviour, our dispositions are finite." "The second problem—the error problem—is that someone might be systematically disposed to make mistakes." "The third problem—the normativity problem—is that the dispositionalist view seems unable to capture the normativity of meaning." (§4). Kripke: "The relation of meaning and intention to future action is normative, not descriptive." (p. 37). Miller & Sultanescu, following Boghossian (2015: 341), assess Blackburn's reply: "Jones has no extended disposition of the sort adumbrated by Blackburn." (§4); of Warren: "it can be argued that the dispositionalist account offered by Warren either fails to resolve the indeterminacy problem or does so only at the expense of deploying semantic and intentional notions" (§4).
- **Meaning is normative (Boghossian 1989; Whiting 2007, 2009, 2016).** "The classic defense of ME normativity can be found in Paul Boghossian (1989a). According to Boghossian the normativity of meaning derives from the fact that meaningful expressions have correctness conditions." (Glüer, Wikforss & Ganapini §2.1.1). Miller & Sultanescu: "For a defence of the claim that meaning is normative, see Whiting 2007, 2009, 2016" (§2.2).
  - *Against:* "Opponents of ME normativity do not challenge (CM) which, again, seems trivially true. Rather, they deny that (CM) has normative consequences just by itself." (§2.1.1); "For criticism of the view that meaning is normative, see Fodor 1990, Glüer and Pagin 1998, Glüer 1999, Wikforss 2001, Boghossian 2005, Miller 2006, Hattiangadi 2006, 2007, and Glüer and Wikforss 2009." (Miller & Sultanescu §2.2).
- **Non-reductionism (Stroud 2000; Boghossian 1989, 2015; Child 2019; Wright; Ginsborg).** "The apparently very serious problems we outlined for the dispositionalist conception of meaning have been taken by a number of philosophers to show that we ought to resist the temptation to explain meaning and content in more basic terms." (§5); "Boghossian relies on the finitude problem to argue that, if meaning facts are determinate, then they cannot supervene on non-semantic facts (Boghossian 2015)." (§5).
  - *Against:* Kripke on a primitive state of meaning, as Miller & Sultanescu report: it "leaves the nature of this postulated primitive state … completely mysterious" (1982: 51).
- **Dissolution (McDowell 1984; Stroud 1990).** "some of the proponents of non-reductionism think that Kripke’s sceptical challenge is based on confusion, and that our task is to unearth that confusion. Thus, on their view, the proper response is not to solve the sceptical problem by showing that the sceptic failed properly to acknowledge some set of facts (or some features of some such facts), but to dissolve it by showing that there is, in fact, no problem." (§5). "McDowell, for instance, argues that Kripke misunderstands the dialectic pursued by Wittgenstein in Philosophical Investigations." and "This involves renouncing the problematic assumption that understanding an expression requires interpreting that expression." "Similarly, Stroud thinks that the paradox is “an expression of an unsatisfiable demand” (1990 [2000: 88])," (§5). The text these readings draw on: "What this shews is that there is a way of grasping a rule which is not an interpretation, but which is exhibited in what we call “obeying the rule” and “going against it” in actual cases." (PI §201).

**Interpretation of Wittgenstein.** Biletzki & Matar: "One of the influential readings of the problem of following a rule (introduced by Fogelin 1976 and Kripke 1982) has been the interpretation, according to which Wittgenstein is here voicing a skeptical paradox and offering a skeptical solution." and "This reading has been challenged, in turn, by several interpretations (such as Baker and Hacker 1984, McGinn1984, and Cavell 1990), while others have provided additional, fresh perspectives (e.g., Diamond, “Rules: Looking in the Right Place” in Phillips and Winch 1989, and several in Miller and Wright 2002)." (§3.5). Candlish & Wrisley's assessment: "Wittgenstein himself immediately brushed this “paradox” aside in his very next paragraph: ‘That there is a misunderstanding here …’; but Kripke takes the paradox to pose a genuine and profound sceptical problem about meaning." and "Kripke’s account of the private language argument is thus vitiated by his unargued reliance on ideas which Wittgenstein argued against." (SEP §4). Kripke's own disclaimer: the work expounds "neither ‘Wittgenstein’s’ argument nor ‘Kripke’s’: rather Wittgenstein’s argument as it struck Kripke, as it presented a problem for him." (p. 5). On the community view: "even the most careful, insightful and sympathetic of Wittgenstein’s commentators have divided on this matter (for example, Malcolm for the community view, and Baker and Hacker against it)." (Candlish & Wrisley §4.1).

**Distribution.** No survey figure is recorded in the sources read.

## Arguments in play

(none recorded as separate argument pages yet). Kripke's elimination of candidate facts is listed by Miller & Sultanescu: "Kripke then considers a variety of other candidates, which are the kernel of various philosophical theories, and argues, on behalf of the sceptic, that none of them fit the bill." (§2); its propositional shape is checked under The question.

## Thinkers who addressed it

- **Ludwig Wittgenstein** (PI I §§185–242, 1953) — states the paradox (§201) and the "misunderstanding" (§201); practice (§202); "bedrock" (§217); "I obey the rule blindly." (§219); agreement "in form of life" (§241).
- **Fogelin** (1976) — sceptical reading (Biletzki & Matar §3.5).
- **Saul Kripke** (1982, pp. 5–110) — quus; sceptical solution; private language as corollary.
- **Blackburn** (1984) — infinitary dispositions (Miller & Sultanescu §4).
- **McDowell** (1984, [doi:10.1007/BF00485246](https://doi.org/10.1007/BF00485246)) — dissolution (§5).
- **McGinn**, **Wright** (1984) — non-factualist reading of the sceptical solution (§3.2); McGinn also among critics of the sceptical reading (Biletzki & Matar).
- **Baker & Hacker** (1984) — against the sceptical reading and the community view.
- **Paul Boghossian** (1989, [doi:10.1093/mind/XCVIII.392.507](https://doi.org/10.1093/mind/XCVIII.392.507); 2005; 2015) — normativity of meaning; incoherence of irrealism; non-supervenience.
- **Stroud** (1990, 2000) — "unsatisfiable demand"; non-reductionism.
- **George Wilson** (1994) — classical realism rejected, meaning facts retained.
- **Horwich** (1998, 2015) — dispositionalism.
- **Kathrin Glüer, Åsa Wikforss** (2009), **Hattiangadi** (2006, 2007), **Alexander Miller** (2006, 2011) — critics of meaning normativity and of irrealism (Miller & Sultanescu §§2.2, 3).
- **Jared Warren** (2020) — dispositional reply to the error problem.

## Framings and reframings

- **Not interpretation but practice.** Wittgenstein: "Interpretations by themselves do not determine meaning." (§198); "And hence also ‘obeying a rule’ is a practice. And to think one is obeying a rule is not to obey a rule." (§202).
- **Agreement.** "It is what human beings say that is true and false; and they agree in the language they use. That is not agreement in opinions but in form of life." (§241); "If language is to be a means of communication there must be agreement not only in definitions but also (queer as this may sound) in judgments." (§242).
- **A Humean sceptical problem.** Kripke: "It may be regarded as a new form of philosophical scepticism." (p. 7), with the solution modelled on Hume's (pp. 62–69, per Miller & Sultanescu §2).
- **Rational explanation.** "The paradox has also been interpreted as belonging to the philosophy of rational explanation, of explanations that account for what people do or think by citing their reasons for doing or thinking so. (Bridges 2014: 249; see also Bridges 2016)" (Miller & Sultanescu §2).
- **A figure in his own right.** Candlish & Wrisley: "Kripke’s Wittgenstein, real or fictional, has become a philosopher in his own right, and for many people, it is not an issue whether the historical Wittgenstein’s original ideas about private language are faithfully captured in this version." (§4).

Not in the excerpts held: the texts of McDowell 1984, Boghossian 1989, Wright, Ginsborg and Lewis's natural-properties reply (SEP postscript to §4); they are left out until a source is read.

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — see The question.
- [Validity](../vocabulary/validity.md) and [classical logic](../methods/classical-logic.md) — the propositional check.
- [Knowledge](../vocabulary/knowledge.md) — first-person knowledge of what one means (Kripke 1982: 51, as reported).
- *Rule*, *meaning*, *disposition*, *normativity*, *non-factualism*, *assertability conditions* — open work in [vocabulary](../vocabulary/index.md).
