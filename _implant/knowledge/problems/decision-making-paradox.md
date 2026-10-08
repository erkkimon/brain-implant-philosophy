---
type: article
about: concept
title: "Decision-making paradox"
description: "Which multi-criteria decision-making method is best, if choosing one is itself a multi-criteria decision? Triantaphyllou & Mann (1989) and Triantaphyllou (2000) name the 'decision paradox' and report methods that disagree and rank reversals; Belton & Gear (1983) on the AHP, Saaty's replies (1987, 2008) and Dyer's critique (1990) side by side."
tags: [problem, paradox, decision-theory, multi-criteria-decision-making, rank-reversal]
timestamp: 2026-10-08T20:29:06Z
---

# Decision-making paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
sources graded as in [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Primary sources: Triantaphyllou & Mann, "An examination of the effectiveness of multi-dimensional decision-making methods: A decision-making paradox", *Decision Support Systems* 5(3), 1989, pp. 303–312 ([doi:10.1016/0167-9236(89)90037-7](https://doi.org/10.1016/0167-9236(89)90037-7); abstract only, excerpt: `raw/triantaphyllou-mann-1989-decision-making-paradox-abstract.md`);
Triantaphyllou, *Multi-Criteria Decision Making Methods: A Comparative Study*, Kluwer 2000 ([doi:10.1007/978-1-4757-3157-6](https://doi.org/10.1007/978-1-4757-3157-6); preface and foreword, excerpt: `raw/triantaphyllou-2000-mcdm-comparative-study-preface-decision-paradox.md`).
Rank reversal and the AHP debate: Wang & Triantaphyllou 2006 and 2008 ([doi:10.1016/j.omega.2005.12.003](https://doi.org/10.1016/j.omega.2005.12.003); excerpts: `raw/wang-triantaphyllou-2006-ranking-irregularities-ahp-rank-reversal-debate.md`, `raw/wang-triantaphyllou-2008-electre-ranking-irregularities.md`);
Saaty [1987](https://doi.org/10.1111/j.1540-5915.1987.tb01514.x) and [2008](https://doi.org/10.1504/IJSSCI.2008.017590), Dyer [1990](https://doi.org/10.1287/mnsc.36.3.249) (excerpt: `raw/dyer-saaty-1987-1990-ahp-rank-reversal-abstracts.md`).
Admitted from Wikipedia's List of paradoxes, revision 1376699902, "Decision theory"; the Wikipedia article ([rev. 1374816244](https://en.wikipedia.org/w/index.php?title=Decision-making_paradox&oldid=1374816244)) is used as a pointer and, where quoted, cited as such (excerpt: `raw/wikipedia-decision-making-paradox-rev-1374816244-and-list-entry.md`).
**Source note.** That article is short and carries three maintenance tags in the revision read: "confusing" (June 2015), "citation needed" (June 2017) on its sentence that different methods give different results, and "better source needed" (June 2017) on its six citations for the paradox's recognition. This page grounds only what the sources read say.

## The question

Wikipedia's list: "Decision-making paradox: Selecting the best decision-making method is a decision problem in itself." (List of paradoxes, rev. 1376699902, "Decision theory").
Triantaphyllou's statement: "However, for one to answer the problem of which is the best MCDM method, he/she will first need to use the best MCDM method! Thus, a decision paradox is reached." (2000, Preface, p. xxvi). MCDM is multi-criteria decision making: ranking a discrete set of alternatives in terms of a set of criteria (Preface, p. xxvi).
Zimmermann's foreword puts the question as: "Therefore, the question “Which is the best method for a given problem?” has become one of the most important but also most difficult to answer." (2000, p. xxiii).
Triantaphyllou & Mann's abstract: "The results illustrate the paradox of deciding on a single best decision- making method." (1989, abstract).

**Propositional check (this implant, 2026-10-08; logic, not a position).**
Let *K* stand for *one knows which method is best* and *U* for *one has used the best method*. Triantaphyllou's sentence gives *K* -> *U*.
`logic.py check --premises "K -> U" "U -> K" --conclusion "~K"` outputs `INVALID` with the counterexample row `K=T, U=T`: the two conditionals together form a circle but not a contradiction.
`logic.py check --premises "K -> U" "~U" --conclusion "~K"` outputs `VALID` (with `U -> K` added, the tool reports `premise 2 is not needed for validity`).
So the conclusion that the best method cannot be known needs the further premise that the best method has not been used; the tool is propositional and does not model "first", i.e. the order in which the steps are taken.

## Why it matters

- **Methods disagree on the same data.** Wang & Triantaphyllou: "Often times different MCDM methods may yield different answers to exactly the same problem [Triantaphyllou, 2000]!" (2008, §1). Their 2006 chapter: "There is no exact way to know which method gives the right answer. This situation leads to the question of how to evaluate the performance of different MCDA methods." (abstract).
- **The proliferation of methods.** Triantaphyllou: "In most cases the authors and supporters of these methods have identified some weaknesses of the previous methods and then they propose a new method claiming to be the best method." (2000, p. xxvi).
- **The case for comparison.** From the paradox he draws a programme: "This is the main reason why a comparative approach is needed in dealing with MCDM methods." (2000, p. xxvi). Zimmermann's foreword: "Rather than suggesting another MCDM method without any convincing justification, he concentrates on the best known and most frequently used methods." (p. xxiii).
- **The reliability of the AHP.** Wang & Triantaphyllou report of Belton and Gear's rank-reversal example: "This phenomenon inspired some doubts about the reliability and validity of the original AHP method." (2006, §3). They also report its use: "Thousands of AHP applications have been reported in edited volumes and books (e.g., Golden, et al., 1989, Saaty and Vargas, 2000) and on websites (e.g., www.expertchoice.com). However, the AHP method has also been criticized by many researchers for some of its problems." (§3).
- **Recognition (the article's claim).** Wikipedia's article: "It was first described by Triantaphyllou, and has been recognized in the related literature as a fundamental paradox in multi-criteria decision analysis (MCDA), multi-criteria decision making (MCDM) and decision analysis since then." (rev. 1374816244, lead; the supporting citations are tagged "better source needed" and were not read here).

## Positions taken

No grouping of positions on the paradox itself was found in the sources read. Two connected questions are on record: whether a best method can be determined (the paradox proper), and whether rank reversal is a defect of a method (the AHP debate through which the paradox's tests were framed). Owners are listed, unranked.

*On the paradox proper*

- **Triantaphyllou & Mann (1989): the paradox stands unresolved; comparison still informs.** "While this paradox is not resolved, useful information is presented for comparing the four methods tested." (abstract).
- **Triantaphyllou (2000): no single best method; the goal "seems" out of reach; compare instead.** "What became clear very soon is that there is no single method which outperforms all the other methods in all aspects." "Although the final goal of determining the best method seems to be unattainable and utopian, some useful lessons have been learned in the process and are presented here in a comprehensive and systematic manner." (Preface, p. xxvi).
- **Wang & Triantaphyllou (2006): test criteria as a partial answer.** "To partially answer this question, three test criteria based on some past related studies are presented." (abstract).

*On rank reversal in the AHP*

- **Belton & Gear (1983): a shortcoming of the AHP, remedied by a different normalisation** (as reported by Wang & Triantaphyllou 2006; the Omega paper, [doi:10.1016/0305-0483(83)90047-6](https://doi.org/10.1016/0305-0483(83)90047-6), pp. 228–230, was verified bibliographically only). "According to Belton and Gear the root for this inconsistency is the fact that the relative values of the alternatives for each criterion sum up to one. So instead of having the relative values of the alternatives sum up to one, they proposed to divide each relative value by the maximum value of the relative values." (Wang & Triantaphyllou 2006, §2.1.2).
- **Saaty (1987): rank is preserved or altered for structural reasons.** "In this paper it will be shown that with absolute measurement, rank always is preserved, with relative measurement, rank changes with nspect to scveral criteria only because of the structural dependence (involving both numbers and measurements) of criteria on alternatives." (abstract; misprints as in the DOI metadata). On what a method owes the decision maker, he writes that it must "preserve or alter ranks appropriately when new alternatives are added or deleted" (abstract). Wang & Triantaphyllou's summary of the same paper: "Saaty in [1987] pointed out that rank reversals were due to the inclusion of duplicates of the alternatives. So he suggested that people should avoid the introduction of similar or identical alternatives." (2006, §3).
- **Saaty (1990, 1994, 2008): from criticism to the "ideal mode".** Wang & Triantaphyllou's account: "The revised AHP was sharply criticized by Saaty in [1990]. After many debates and a heated discussion (e.g., [Dyer, 1990a; and 1990b], [Saaty, 1983; 1987; and 1990], and [Harker and Vargas, 1990]), Saaty accepted this variant and now it is also called the ideal mode AHP [Saaty, 1994]." (2006, §2.1.2; Saaty 1990 and 1994 not read). Saaty's own 2008 description: "These priorities may also be expressed in the ideal form by dividing each priority by the largest one, 0.333 for International Company, as given in Table 7. The effect is to make this alternative the ideal one with the others getting their proportionate value." (§5, p. 90), and "The idealised priorities are always used for ratings." (§6).
- **Harker & Vargas (1990): a reply to Dyer in defence of the AHP** (title: "Reply to “Remarks on the Analytic Hierarchy Process” by J. S. Dyer", [doi:10.1287/mnsc.36.3.269](https://doi.org/10.1287/mnsc.36.3.269); verified bibliographically, not read).
- **Dyer (1990): the AHP's rankings are arbitrary.** "The analytic hierarchy process (AHP) is flawed as a procedure for ranking alternatives in that the rankings produced by this procedure are arbitrary." "The key to correcting this flaw is the synthesis of the AHP with the concepts of multiattribute utility theory." (abstract). Wang & Triantaphyllou's summary: "Dyer in [1990a] indicated that the sum to unity normalization of priorities makes each one dependent on the set of alternatives being compared." (2006, §3).
- **Triantaphyllou & Mann (1989), Triantaphyllou (2000, 2001): rank reversal without copies, in the revised AHP too.** "However, even earlier, the revised AHP method was found to suffer of some other ranking problems even without the introduction of identical alternatives [Triantaphyllou and Mann, 1989]." (Wang & Triantaphyllou 2006, §2.1.2); "However, other cases were later found in which rank reversal occurred without the introduction of identical alternatives [Triantaphyllou, 2000; and 2001]." (§3).
- **Wang & Triantaphyllou (2006, 2008): multiplicative methods as immune to most of these irregularities.** "However, the previous multiplicative models are immune to most of these ranking irregularities." (2008, §1); of one class of irregularities, "The only methods that are immune to these ranking irregularities are two multiplicative MCDA methods: the weighted product model (WPM) and the multiplicative AHP." (2006, §3). Wikipedia's rank-reversal article adds that the WPM "does cause rank reversals when it is compared with the weighted sum model (WSM) and under the condition that all the criteria of a given decision problem can be measured in exactly the same unit." (rev. 1352325277, "Type 5").

## Arguments in play

(none recorded as separate argument pages yet). The study design behind the paradox, as its authors report it:

- **The two evaluative criteria (1989).** "Two evaluative criteria were used in an attempt to find the best method. The first criterion was to see if the method when accurate in a multi-dimensional situation remained accurate in a single-dimensional case. The second criterion determined the stability of a method in yielding the same outcome when a nonoptimal alternative was replaced with a worse alternative." (abstract). The four methods: "the weighted sum model, the weighted product model, the analytic hierarchy process, and the revised analytic hierarchy process." Data: "Tests were conducted using simulated decision problems where random numbers were used for the values of the many combinations of alternatives and criteria." (abstract).
- **The benchmark in the first criterion (the article's report).** "For such problems, the weighted sum model (WSM) is the widely accepted approach, thus, their results were compared with the ones derived from the WSM." (Wikipedia, rev. 1374816244, "Description"; the 1989 body was not read, so whose assessment "widely accepted" is could not be checked).
- **The normative premise of the second criterion.** Wang & Triantaphyllou: "However, there is no legitimate reason why the optimal alternative should also be changed and why the original incomparable relation between two equally ranked alternatives should also be changed." (2008, of their ELECTRE example). Saaty's 1987 abstract instead allows that a method may "preserve or alter ranks appropriately" when alternatives are added or deleted.
- **The circle of methods (the article's report).** "It was found that when a method was used, say method X (which is one of the previous four methods), the conclusion was that another method was best (say, method Y). When method Y was used, then another method, say method Z, was suggested as being the best one, and so on." (Wikipedia, rev. 1374816244; it cites the 1989 paper and the 2000 book, neither of whose bodies was read here, and the 1989 abstract does not state this result).
- **The regress.** Its propositional core is checked under The question.

## Thinkers who addressed it

- **Valerie Belton & Tony (A. E.) Gear** (Omega 11(3), 1983, pp. 228–230) — the first rank-reversal example in the AHP and the revised AHP, per Wang & Triantaphyllou 2006, §2.1.2 and §3 (not read at first hand).
- **Thomas L. Saaty** (Decision Sciences 1987; Management Science 1990; 1994; IJSS 2008) — originator of the AHP (Wikipedia, rank-reversal article, rev. 1352325277: "Professor Thomas Saaty (the inventor of the AHP)"); rank preservation and reversal explained by measurement type and structural dependence (1987); the ideal form (2008).
- **Evangelos Triantaphyllou & Stuart H. Mann** (Decision Support Systems 1989) — named the paradox in the paper's title and abstract.
- **James S. Dyer** (Management Science 1990, pp. 249–258 and 274–275) — arbitrary rankings; synthesis with multiattribute utility theory (abstract).
- **Patrick T. Harker & Luis G. Vargas** (Management Science 1990, pp. 269–273) — reply to Dyer (title only).
- **Evangelos Triantaphyllou** (2000; 2001) — the "decision paradox" in the preface; further types of rank reversal.
- **Hans-Jürgen Zimmermann** (Foreword to Triantaphyllou 2000) — the question of the best method for a given problem.
- **Xiaoting Wang & Evangelos Triantaphyllou** (2006; Omega 2008) — ranking irregularities extended to ELECTRE; TOPSIS "according to some unpublished results by the authors" (2008, §1).
- **Thomas L. Saaty & Mujgan Sagir** ("An essay on rank preservation and reversal", 2009, [doi:10.1016/j.mcm.2008.08.001](https://doi.org/10.1016/j.mcm.2008.08.001)) — verified bibliographically only (publisher returned 403).

## Framings and reframings

- **A paradox, or a finding?** Triantaphyllou himself names a class: "Some of the findings of these comparative analyses are so startling and counter intuitive, that are presented as decision making paradoxes." (2000, p. xxvii). The label "paradox" is his and Mann's; the sources read record no author who disputes the label, and no author besides Triantaphyllou and his co-authors who uses it at first hand (the article's six supporting citations were not read).
- **Rank reversal as defect, or as legitimate.** Wikipedia's rank-reversal article: "In decision-making, a rank reversal is a change in the rank ordering of the preferability of alternative possible decisions when, for example, the method of choosing changes or the set of other available alternatives changes." and "It is something that continues to be considered controversial by many and is frequently debated." (rev. 1352325277). The defect reading is Belton & Gear's and Triantaphyllou's as reported above; Saaty's 1987 abstract ties rank change under relative measurement to "structural dependence".
- **Evaluating methods at all.** The rank-reversal article: "Thus the following question emerges: How can one evaluate decision-making methods? This is a very difficult issue and may not be answered in a globally accepted manner." (rev. 1352325277, lead).
- **Who introduced the revised AHP.** Wang & Triantaphyllou: "The revised AHP model was proposed by Belton and Gear in [1983] after they had found a case of ranking abnormality that occurred when the original AHP was used." (2006, §2.1.2). Wikipedia's rank-reversal article instead speaks of "a new variant to it that was introduced by Professor Thomas Saaty (the inventor of the AHP) in response to the previous observation by Belton and Gear" (rev. 1352325277). The two attributions stand side by side.
- **Scope beyond the AHP (the article's claims).** "The following multi-criteria decision-making methods have been confirmed to exhibit this paradox:The analytic hierarchy process (AHP) and some of its variants, the weighted product model (WPM), the ELECTRE (outranking) method and its variants and the TOPSIS method." and "Other methods that have not been tested yet but may exhibit the same phenomenon include the following:" — eleven methods follow, no reference attached (rev. 1374816244). On the WPM, Wang & Triantaphyllou (2006, 2008) report multiplicative methods as immune to most of the irregularities they studied; the article lists the WPM among the methods affected.

Left out until read: the bodies of the 1989 paper (the posted PDF is a scan without text) and of the 2000 book, Belton & Gear 1983, Saaty 1990 and 1994, Harker & Vargas 1990, Saaty & Sagir 2009, Triantaphyllou 2001, and the six papers Wikipedia cites for the paradox's recognition.

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — the label as Triantaphyllou and Mann use it.
- [Validity](../vocabulary/validity.md) — the propositional check above.
- *Multi-criteria decision making (MCDM/MCDA)*, *rank reversal*, *analytic hierarchy process (AHP)*, *revised / ideal mode AHP*, *weighted sum model (WSM)*, *weighted product model (WPM)*, *ELECTRE*, *TOPSIS* — open work in [vocabulary](../vocabulary/index.md).
