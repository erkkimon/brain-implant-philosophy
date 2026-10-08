---
type: article
about: concept
title: "The paradox of analysis"
description: "How can an analysis be both correct and informative? Langford's 1942 dilemma (same meaning, trivial; different meaning, incorrect), Moore's 1942 reply and avowal of no clear solution, Frege's 1894 statement and the sense/reference response, Carnap's intensional structure, Black and White, the content/vehicle proposals and the metaethical use against Moore's open-question argument — each with its owner."
tags: [problem, paradox, philosophy-of-language, metaphilosophy, logic]
timestamp: 2026-10-08T18:20:39Z
---

# The paradox of analysis

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
claim grades as in [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Primary texts: Langford, "The Notion of Analysis in Moore's Philosophy", and
Moore, "A Reply to My Critics", both in Schilpp (ed.), *The Philosophy of G. E. Moore*
(1942), pp. 321–342 and 665–667 ([archive.org scan](https://archive.org/details/in.ernet.dli.2015.46303);
excerpt: `raw/langford-moore-1942-paradox-of-analysis-schilpp.md`); Carnap,
*Meaning and Necessity* (1947), §15, pp. 63–64 ([archive.org scan](https://archive.org/details/in.ernet.dli.2015.46380);
excerpt: `raw/carnap-1947-meaning-and-necessity-15-paradox-of-analysis.md`).
Map: Beaney & Raysmith, [SEP Fall 2024 "Analysis"](https://plato.stanford.edu/archives/fall2024/entries/analysis/)
(main entry §§2, 5; [supplement s6](https://plato.stanford.edu/archives/fall2024/entries/analysis/s6.html) §4;
Frege's 1894 passage in [supplement s1](https://plato.stanford.edu/archives/fall2024/entries/analysis/s1.html);
excerpt: `raw/sep-analysis-fall-2024-paradox-of-analysis.md`); Rey, [SEP "The Analytic/Synthetic Distinction"](https://plato.stanford.edu/archives/fall2024/entries/analytic-synthetic/) §3.1;
Hurka, [SEP "Moore's Moral Philosophy"](https://plato.stanford.edu/archives/fall2024/entries/moore-moral/) §1;
Zalta, [SEP "Gottlob Frege"](https://plato.stanford.edu/archives/fall2024/entries/frege/) §3.2
(excerpt: `raw/sep-analytic-synthetic-moore-moral-frege-fall-2024-paradox-of-analysis.md`).
Later literature is cited from DOI records only (`raw/paradox-of-analysis-literature-crossref.md`).
Beaney is himself a party (Beaney 2005, 2017, cited in the entry); his and Raysmith's assessments are marked as theirs.
Not to be confused with [Moore's paradox](moores-paradox.md), a different problem from the same 1942 volume (structural note).

## The question

Langford's statement: "the paradox of analysis is to the effect that, if the verbal expression representing the analysandum has the same meaning as the verbal expression representing the analysans, the analysis states a bare identity and is trivial; but if the two verbal expressions do not have the same meaning, the analysis is incorrect." (1942, p. 323).
His terms: "Let us call what is to be analyzed the analysandum, and let us call that which does the analyzing the analysans." (p. 323).
Moore's restatement, on "To be a brother is the same thing as to be a male sibling": "The paradox arises from the fact that, if this statement is true, then it seems as if it must be the case that you would be making exactly the same statement if you said: “To be a brother is the same thing as to be a brother,” But it is obvious that these two statements are not the same;" (1942, p. 665).
Beaney & Raysmith's general form: "Then either ‘A’ and ‘C’ have the same meaning, in which case the analysis expresses a trivial identity; or else they do not, in which case the analysis is incorrect. So it would seem that no analysis can be both correct and informative." (SEP "Analysis", s6 §4).
Rey's version of the question: "why should analyses be of any conceivable interest?" (SEP, §3.1).

**Propositional check (this implant, 2026-10-01; logic, not a position).**
Let *s* stand for: analysandum and analysans expressions have the same
meaning; *c*: the analysis is correct; *i*: the analysis is informative. The dilemma
as Langford and Beaney & Raysmith state it has premises `s -> ~i` and
`~s -> ~c`. `logic.py check --premises 's -> ~i' '~s -> ~c' --conclusion '~(c & i)'`
outputs `VALID`. With *same meaning* split into two atoms — *t* for the one
that blocks informativeness, *e* for the one correctness needs (the two-senses
move reported below) — `logic.py check --premises 't -> ~i' '~e -> ~c' --conclusion '~(c & i)'`
outputs `INVALID` with the counterexample row `c=T, e=T, i=T, t=F`. The tool
shows only that the conclusion depends on *meaning* being one and the same
atom in both premises; whether any reading of *meaning* makes both premises
true is what the positions below dispute.

**Where it comes from.** Beaney & Raysmith: "(Although the problem itself goes back to the paradox of inquiry formulated in Plato’s Meno, and can be found articulated in Frege’s writings, too, the term ‘paradox of analysis’ was indeed first used in relation to Moore’s work, by Langford in 1942.)" (s6 §4).
In the main entry they say [Meno's paradox](menos-paradox.md) "anticipates what we now know as the paradox of analysis, concerning how an analysis can be both correct and informative" (§2).
Frege's 1894 review of Husserl, in Beaney's translation as the SEP quotes it: "In the former case it is pointless to equate them by means of a definition: this is ‘an obvious circle’; in the latter case it is wrong." (RH 319–20 / FR 225–6, via s1).
And: "In using the word to be explained, I either think clearly everything I think when I use the defining expression: we then have the ‘obvious circle’; or the defining expression has a more richly articulated sense, in which case I do not think the same thing in using it as I do in using the word to be explained: the definition is then wrong." (same passage).

## Why it matters

- **Moore's open-question argument.** Beaney & Raysmith introduce the paradox as the general form of Moore's argument against defining "good": "But in its general form what we have here is the paradox of analysis." (s6 §4). Their assessment of the consequence: "And if this is so, then it is equally unclear that no definition of ‘good’—whether naturalistic or not—is possible." (s6 §4).
- **Metaethics, the reply side.** Hurka reports an objection to the open-question argument: "One said the argument’s persuasiveness depends on the “paradox of analysis”: that any definition of a concept will, if it is successful, appear uninformative." and "If an analysis does capture all its target concept’s content, the sentence linking the two will be a tautology; but this is hardly a reason to reject all analyses (Langford 1942)." (SEP "Moore's Moral Philosophy", §1). He reports a reply in turn: "Even if we agree that only pleasure is good, no amount of reflection will make us think “Pleasure is good” is equivalent to “Pleasure is pleasure”; Ross, for one, gave this response (1930: 92–94)." (§1).
- **Analyticity and logicism.** Rey files the paradox as the first of the "Problems with the Distinction" (SEP "The Analytic/Synthetic Distinction", §3.1); for Frege's definitions of arithmetic concepts: "In their case, it seems perfectly possible to think the definiendum, say, number, without thinking the elaborate definiens Frege provided (cf. Bealer 1982, Michael Dummett 1991, and John Horty 1993, 2007, for extensive discussions of this problem, as well as of further conditions, e.g., fecundity, that Frege placed on serious definitions)." (§3.1). Moore himself ties his reply to the same distinction: "To raise this question would be to raise the question how an “analytic” necessary connection is to be distinguished from a “synthetic” one — a subject upon which I am far from clear." (1942, p. 667).
- **Philosophical method.** Beaney & Raysmith place the Meno problem "At the heart of all of them" — the ancient methodologies of analysis (§2).

## Positions taken

No source read groups the responses into families; the order below is chronological by first statement, and none is ranked here.

- **Two senses of *meaning* (Langford 1942, first line).** "One is tempted to say that there must be some appropriate sense of “meaning” in which the two verbal expressions do have the same meaning and some other appropriate sense in which they do not." (p. 323). His own version: "The two verbal expressions will therefore not be synonymous; but the analysandum and the analysans will be cognitively equivalent in some appropriate sense." (p. 326), since "The analysans will be more articulate than the analysandum," (p. 326); of "being orange" and "being intermediate in color between red and yellow": "The sense in question is therefore stronger than that of having the same denotation and is yet not so strong that the two verbal expressions can be said to be synonymous." (p. 331).
  *Against:* (none recorded in the sources read).
- **Same meaning without triviality: "formal" analysis (Langford 1942, second line).** "But it is possible to argue that having the same meaning does not entail triviality, owing to important grammatical differences between the verbal expressions involved, and a view to this effect will also be considered." (p. 323); his conclusion: "Considerations like these tend to show that logical analysis is not trivial, even though the analysandum and the analysans have precisely the same meaning." (p. 340).
  *Against:* Moore: "It is these facts, I think, which drive Mr. Langford to say that, in what he calls a “formal” analysis, both analysandum and analysans must be mere verbal expressions and that what is stated in giving the analysis must be merely that two verbal expressions have the same meaning. But I think this solution of his is obviously wrong," (1942, p. 665), giving as his reason that nobody would call an assertion merely about two verbal expressions the giving of an analysis (p. 665, paraphrased).
- **Same concept, different expressions (Moore 1942).** "(a) both analysandum and analysans must be concepts, and, if the analysis is a correct one, must, in some sense, be the same concept, and (b) that the expression used for the analysandum must be a different expression from that used for the analysans." (p. 666); and (c) "the expression used for the analysans must explicitly mention concepts which are not explicitly mentioned by the expression used for the analysandum." (p. 666). His suggestion: "one must suppose that both statements are in some sense about the expressions used as well as about the concept of being a brother. But in what sense they are about the expressions used I cannot see clearly; and therefore I cannot give any clear solution to the puzzle." (p. 666). Beaney & Raysmith's summary: "In his own response, when the paradox was put to him in 1942, Moore talks of the analysandum and the analysans being the same concept in a correct analysis, but having different expressions. But he admitted that he had no clear solution to the problem (RC, 666)." (s6 §4). O'Connor ([1982](https://doi.org/10.1017/s0031819100050786)) is annotated by them as "[offers a Moorean solution]" (bib6); its abstract: "In 1942, replying to a criticism put to him by Langford, G. E. Moore confessed that he was unable to solve the paradox of analysis." (text not read).
  *Against:* Moore himself rejects the reading on which the statement is "merely a conjunction" of a claim about expressions and a claim about the concept: "But I do not think this can possibly be the case: what would the second assertion in this supposed conjunction be?" (p. 666). Further objections: (none recorded in the sources read).
- **Sense and reference (Frege; reported by Beaney & Raysmith).** Their assessment: "At the very least, it seems to cry out for a distinction between two kinds of ‘meaning’, such as the distinction between ‘sense’ and ‘reference’ that Frege drew, arguably precisely in response to this problem (see Beaney 2005; 2017, ch. 3)." (s6 §4). "An analysis might then be deemed correct if ‘A’ and ‘C’ have the same reference, and informative if ‘C’ has a different, or more richly articulated, sense than ‘A’." (s6 §4). Frege, 1894: "What matters to the former is the sense of the words, as well as the ideas which they fail to distinguish from the sense; whereas what matters to the latter is the thing itself: the Bedeutung of the words." (psychological logicians vs. mathematicians; via s1). Zalta: "The sense of an expression accounts for its cognitive significance—it is the way by which one conceives of the denotation of the term." (SEP "Gottlob Frege", §3.2). Book-length treatments: Dummett ([1987, repr. 1991](https://doi.org/10.1093/019823628x.003.0002)), Nelson ([2008](https://doi.org/10.1007/s11098-005-4540-2)), Beaney 2005 (titles only, per bib6).
  *Against:* Rey: "This is “the paradox of analysis,” which can be seen as dormant in Frege’s own move from his (1884) focus on definitions to his more controversial (1892a) doctrine of “sense,” where two senses are distinct if and only if someone can think a thought containing the one but not other, as in the case of the senses of “the morning star” and “the evening star.”" (§3.1); on that criterion, sense-preserving definitions of number face the problem quoted under Why it matters (§3.1).
- **Different propositions (Black 1944).** Carnap's report: "Black tries to show that the two sentences do not express the same proposition;" (1947, p. 63), via a paraphrase with the relation *Conjunct* ([Black 1944](https://doi.org/10.1093/mind/liii.211.263), text not read).
  *Against:* White (*Mind* 1945), per Carnap: "White replies that this is not a sufficient reason for the assertion." (p. 63).
- **Intensional structure (Carnap 1947).** "The difference between the two expressions, and, consequently, between the two sentences is a difference in intensional structure, which exists in spite of the identity of intension." (p. 64); "It seems to me that this cognitive equivalence is explicated by our concept of L-equivalence and that the synonymity, which does not hold for these expressions, is explicated by intensional isomorphism." (p. 64). His diagnosis of the earlier debate: "None of the four authors states his criterion for the identity of “meaning”, “statement”, or “proposition”; this seems the chief cause for the inconclusiveness of the whole discussion." (p. 63).
  *Against:* (none recorded in the sources read; Linsky 1949 and Carnap's 1949 reply are listed in bib6, not read).
- **Content and vehicle; character (Fodor 1990; Horty 1993, 2007; after Kaplan 1989; Russell 2008; Pietroski).** Rey reports: "For example, one might make further distinctions within the theory of sense between an expression’s “content” and the specific “linguistic vehicle” used for its expression, as in Fodor (1990a) and Horty (1993, 2007);" and "Perhaps analyses could be regarded as providing a particular “vehicle,” having a specific “character,” that could account for why one could entertain a certain concept without entertaining its analysis (cf. Gillian Russell 2008, and Paul Pietroski 2002, 2005 and 2018 for related suggestions)." (§3.1).
  *Against:* (none recorded in the sources read).

Other proposals known only by title — Chisholm & Potter, "The Paradox of Analysis: A Solution" ([1981](https://doi.org/10.1111/j.1467-9973.1981.tb00110.x)); Myers ([1971](https://doi.org/10.1111/j.1467-9973.1971.tb00330.x)); Fumerton ([1983](https://doi.org/10.2307/2107643)); King ([2007](https://doi.org/10.1093/acprof:oso/9780199226061.003.0008)); Lewy 1976, chs. 6–7; Ackerman 1981 — are not summarised: no text was read. No survey figure is recorded.

## Arguments in play

(none recorded as separate argument pages yet). The dilemma itself is
checked under The question; the open-question argument it generalises
(Beaney & Raysmith, s6 §4) has no page yet.

## Thinkers who addressed it

- **Plato** — *Meno*, the paradox of inquiry, named as its antecedent by Beaney & Raysmith (§2; s6 §4); see [Meno's paradox](menos-paradox.md).
- **Gottlob Frege** (1884 definitions; 1892 sense; 1894 review of Husserl, RH 319–20) — states the dilemma against Husserl; sense/reference as response (Beaney & Raysmith; Rey §3.1).
- **Edmund Husserl** (*Philosophie der Arithmetik*, 1891) — the objections Frege answers (s1).
- **G. E. Moore** (*Principia Ethica*, 1903, open-question argument, per s6 §4; reply of 1942, pp. 665–667) — same concept, different expressions; no clear solution.
- **W. D. Ross** (1930: 92–94) — reply defending the open-question argument (Hurka §1).
- **R. G. Collingwood** (*An Essay on Philosophical Method*, 1933) — "develops his own response to what is essentially the paradox of analysis (concerning how an analysis can be both correct and informative), which he recognizes as having its root in Meno’s paradox." (Beaney & Raysmith §5; content not read).
- **C. H. Langford** (1942, pp. 321–342) — names and states the paradox; two senses of meaning; formal analysis.
- **Max Black** (1944, 1945), **Morton White** (1945) — different propositions, and the reply (via Carnap).
- **Rudolf Carnap** (1947, §15) — intensional structure; Leonard Linsky (1949) and Carnap's reply (1949), titles per bib6.
- **Casimir Lewy** (1976), **Diana Ackerman** (1981), **Chisholm & Potter** (1981), **David O'Connor** (1982), **Richard Fumerton** (1983), **Michael Dummett** (1987/1991), **Michael Beaney** (2005, 2017), **Jeffrey C. King** (2007), **Michael Nelson** (2008) — titles and DOI records only.
- **Jerry Fodor** (1990), **John Horty** (1993, 2007), **Gillian Russell** (2008), **Paul Pietroski** (2002–2018) — content/vehicle and character proposals (Rey §3.1).

## Framings and reframings

- **A question about interest, not correctness.** Rey: "One problem with the entire program was raised by C.H. Langford (1942) and discussed by G.E. Moore (1942 [1968], pp. 665–6): why should analyses be of any conceivable interest?" (§3.1).
- **Dissolution case by case.** Hurka reports the reply that for some definitions the informativeness is only apparent: "Here it can be replied that in other cases accepting a definition leads us to see that the sentence affirming it, while initially seeming informative, in fact is not; thus “a bachelor is an unmarried man” is not informative." (§1).
- **A version of the paradox of inquiry.** Beaney & Raysmith, and Collingwood as they report him, place the root in the *Meno* (§§2, 5).
- **Concepts versus words.** Moore reframes what an analysis is about: analysandum and analysans "must be concepts" (p. 666), against Langford's verbal expressions (p. 665).

Not in the excerpts held: Black 1944 and White 1945 themselves, Collingwood
1933, Ross 1930, Lewy 1976, Quine's criticisms of analyticity that Rey
turns to after §3.1, and every later paper listed only by DOI; they are left
out until a source is read.

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — see The question.
- [Dilemma](../vocabulary/dilemma.md) — the paradox's two-horned form.
- [Validity](../vocabulary/validity.md) and [Classical logic](../methods/classical-logic.md) — the propositional check above.
- *Analysandum*, *analysans* (Langford 1942, p. 323), *sense/reference (Sinn/Bedeutung)*, *intension*, *intensional isomorphism*, *L-equivalence* (Carnap 1947) — open work in [vocabulary](../vocabulary/index.md).

Related thinkers: [G. E. Moore](../thinkers/g-e-moore.md).
