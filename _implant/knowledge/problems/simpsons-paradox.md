---
type: article
about: concept
title: "Simpson's paradox"
description: "An association between two variables that holds in every subpopulation can vanish or reverse in the pooled population. What is disputed is not the arithmetic but why it surprises and which table to trust — Yule 1903, Simpson 1951, the Berkeley admissions data of Bickel, Hammel & O'Connell 1975, Pearl's causal analysis, and the non-causal explanations of Bandyopadhyay et al. and Fitelson, each with its owner."
tags: [problem, paradox, philosophy-of-statistics, causation, decision-theory]
timestamp: 2026-09-28T07:01:48Z
---

# Simpson's paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
claim grades as in [How claims are graded](../../conventions/how-claims-are-graded.md).
Part of the [problems](./index.md) branch. Map: Jan Sprenger and Naftali
Weinberger, [SEP Fall 2024 "Simpson's Paradox"](https://plato.stanford.edu/archives/fall2024/entries/paradox-simpson/)
(first published 2021-03-24; excerpt: `raw/sep-paradox-simpson-fall-2024-reversal-causation-and-explanations.md`).
Also read: Pearl, [2014](https://doi.org/10.1080/00031305.2014.876829), preprint
[R-414](https://ftp.cs.ucla.edu/pub/stat_ser/r414.pdf) (excerpt: `raw/pearl-2014-understanding-simpsons-paradox.md`);
Yule, [1903](https://doi.org/10.1093/biomet/2.2.121) (excerpt: `raw/yule-1903-mixing-of-distinct-records.md`);
Bickel, Hammel & O'Connell, [1975](https://doi.org/10.1126/science.187.4175.398)
(excerpt: `raw/bickel-hammel-oconnell-1975-berkeley-admissions.md`). Works
held only as verified bibliographic records are listed in
`raw/simpsons-paradox-bibliographic-simpson-1951-blyth-1972-and-critics.md`.

## The question

Sprenger & Weinberger's definition: "Simpson’s Paradox is a statistical phenomenon where an association between two variables in a population emerges, disappears or reverses when the population is divided into subpopulations." (SEP, preamble).
They add: "Cases exhibiting the paradox are unproblematic from the perspective of mathematics and probability theory, but nevertheless strike many people as surprising." (preamble).
Sprenger & Weinberger (§4) organise the problem by
Bandyopadhyay et al.'s (2011) three questions — in what sense it is a
[paradox](../vocabulary/paradox.md), how to analyse it, and how to proceed: "Why or in what sense is Simpson’s Paradox a paradox? What is the proper analysis of the paradox? How one should proceed when confronted with a typical case of the paradox?"

**Worked table (Pearl 2014, Fig. 4; recovered / not recovered).**

|            | drug      | rate | no drug  | rate |
|------------|-----------|------|----------|------|
| males      | 18 / 12   | 60 % | 7 / 3    | 70 % |
| females    | 2 / 8     | 20 % | 9 / 21   | 30 % |
| combined   | 20 / 20   | 50 % | 16 / 24  | 40 % |

**Arithmetic check (this implant, 2026-09-27; mathematics, not a
position).** In each row the drug's rate is lower (3/5 < 7/10; 1/5 < 3/10);
pooled it is higher (1/2 > 2/5). The pooled rate is a weighted average of
the subgroup rates, weighted by each arm's composition:
P(E|C) = 3/5 · 30/40 + 1/5 · 10/40 = 1/2, and
P(E|¬C) = 7/10 · 10/40 + 3/10 · 30/40 = 2/5.
The drug arm is 75 % male, the no-drug arm 25 % male, and males recover more
often in both arms. With equal weights (1/2, 1/2) in both arms the same
subgroup rates give 2/5 against 1/2, the subgroup ordering. A Python check
with exact fractions printed `males drug>none: False`, `females drug>none:
False`, `combined drug>none: True`, `P(E|C) = 1/2`, `P(E|~C) = 2/5`,
`balanced: drug 2/5 none 1/2`. The general condition is Theorem 1 in
Sprenger & Weinberger (§2.2, credited to Lindley & Novick 1981 and Mittal
1991): "the lack of correlation between M and T is sufficient to rule out association reversals (and thus YAP as well)."

Simpson's own numbers (SEP Table 1: men 8/5 treated vs 4/3 control,
women 12/15 vs 2/3; pooled 20/20 vs 6/6) are positive in each subgroup and
zero pooled, which the authors class as "a special case" of association
reversal (§2.1). Sprenger & Weinberger ask: "Should we use the treatment or not? When we know the gender of the patient, we would presumably administer the treatment, whereas it does not look like the right thing to do when we don’t know the patient’s gender—although we know that the patient is either male or female!" (§1).

**Varieties** (SEP §2.1). Association reversal (AR), in Samuels's (1993)
name, "is the standard variety"; Yule's association paradox (YAP), Mittal's
(1991) name, is no association in any subgroup but one in the whole; the
Amalgamation Paradox (AMP) of Good & Mittal (1987) "occurs when the overall degree of association is bigger (or smaller) than each degree of association in the subpopulations".
The authors order them "YAP ⇒ AR ⇒ AMP" (§2.1). Row-uniform design rules
out AMP for most association measures but not for the log-odds ratio
(Theorem 2, Good & Mittal 1987, as given in §2.2). On frequency: "Simulations by Pavlides and Perlman (2009) suggest that it should not occur frequently" (§2.2).

## Why it matters

- **Scope, per Sprenger & Weinberger:** "the paradox has implications for a range of areas that rely on probabilities, including decision theory, causal inference, and evolutionary biology." (preamble).
- **Discrimination data.** Bickel, Hammel & O'Connell (1975, p. 398) report
  for Berkeley's fall-1973 graduate applications: "There were 8442 male applicants and 4321 female applicants. About 44 percent of the males and about 35 percent of the females were admitted."
  Department by department they found four departments biased against women
  (a deficit of 26) and "six departments biased in the opposite direction, at the same probability levels; these account for a deficit of 64 men." (p. 399).
  Their diagnosis: "We have stumbled onto a paradox, sometimes referred to as Simpson's in this context (1) or "spurious correlation" in others (2)." (p. 399),
  with "almost two-thirds of the applicants to English but only 2 percent of the applicants to mechanical engineering" women (p. 399).
  Their summary: the aggregate "shows a clear but misleading pattern of bias against female applicants", and "If the data are properly pooled, taking into account the autonomy of departmental decision making, thus correcting for the tendency of women to apply to graduate departments that are more difficult for applicants of either sex to enter, there is a small but statistically significant bias in favor of women." (p. 403).
  **Arithmetic check (this implant):** Table 1 (p. 399) gives 3738 of 8442
  men admitted (44.3 %) and 1494 of 4321 women (34.6 %); 8442 + 4321 = 12,763.
  In their hypothetical "machismatics" (400 men, 200 women; half of each
  admitted) and "social warfare" (150 men, 450 women; a third of each)
  (p. 400), pooled rates are 250/550 (45.5 %) for men and 250/650 (38.5 %)
  for women, with equal rates inside each department.
- **Causal inference and philosophy of causation.** "Within the philosophical literature, Simpson’s Paradox received sustained attention due to its implications for accounts of causality that posit systematic connections between causal relationships and probability-raising." (SEP §3).
- **Decision theory.** "Blyth (1972) argued that Simpson’s Paradox also constitutes a counterexample to the sure-thing principle of decision theory, or at least restricts its scope substantially." (SEP §5.3). The same section links it to [Newcomb's problem](newcombs-problem.md) via Stern (2019): an agent "may not be sure whether her action counts as an intervention (e.g., in Newcomb scenarios)".
- **Biology.** "Within the units of selection debate, Simpson reversals have played an important role in explaining the possibility of group-level selection." (SEP §5.4).
- **Other cases the SEP reports:** Covid-19 case fatality, higher in Italy
  than China overall but higher in China in every age group (§1, citing
  Kügelgen, Gresele & Schölkopf); US verbal SAT averages rising 1992–2002
  while falling within each GPA group (§5.1, Rinott & Tam 2003).

## Positions taken

Grouped by this page along the SEP entry's sections: what explains the
appearance of paradox (§4, with §3.4), probabilistic causality (§§3.1–3.5),
and which data should guide a decision (§§3.4, 5.3). Not ranked; no survey
of philosophers' views on it is known to this implant.

**Is it a paradox at all?**

- **Not in the logical sense — Sprenger & Weinberger (§4):** "Simpson’s Paradox is not a paradox in the sense of presenting an inconsistent set of plausible propositions of which at least one must be rejected." Their conclusion (§6): "There is perhaps nothing paradoxical about Simpson’s Paradox, but since we often struggle to understand it, our reasoning about association reversals may be entangled with various forms of reasoning that are susceptible to bias and error."
- **Reversal vs. paradox — Pearl (2014, §2.1, p. 4):** "we must first distinguish between “Simpson’s reversal” and “Simpson’s paradox”; the former being an arithmetic phenomenon in the calculus of proportions, the latter a psychological phenomenon that evokes surprise and disbelief."

**What explains the surprise** (the three analyses SEP §4 discusses):

- **Causal conflation — Pearl.** "Pearl’s explanation of the paradox is that people conflate causal and non-causal expressions, and if the conditional probabilities in the examples are interpreted causally, Simpson’s reversals are impossible." (SEP §3.4). Pearl's own statement: "it is hard, if not impossible, to explain the surprise part of Simpson’s reversal without postulating that human intuition is governed by causal calculus together with a persistent tendency to attribute causal interpretation to statistical associations." (2014, p. 4). He rests it on a "sure-thing" theorem (Causality 2009, p. 181, quoted 2014, p. 4): "An action A that increases the probability of an event B in each subpopulation (of C) must also increase the probability of B in the population as a whole, provided that the action does not change the distribution of the subpopulations." His conclusion: "we can safely title it “resolved.”" (2014, p. 8).
- **Error about ratios — Bandyopadhyay, Nelson, Greenwood, Brittan & Berwald (2011)**, as reported: they "reject Pearl’s causal analysis of the paradox, and defend an alternative mathematical explanation" (SEP §4), with the argument, as the SEP states it, "If there are cases of the paradox that still exhibit surprise despite having nothing to do with causality, then the general explanation of the paradox cannot be causal.", and a student survey in which "only 12% give the correct answer" (§4). Sprenger & Weinberger's assessment: "Yet Bandyopadhyay et al. do not specify what this error is." (§4).
- **Confirmation-theoretic — Fitelson (2017):** "reasoners are not attentive to the difference between the suppositional and conjunctive readings of confirmation statements when considering the evidential relevance of learning an individual’s gender." (SEP §4). His abstract: "I propose a new rationalizing explanation of its (apparent) paradoxicality." (Episteme 14(3), via Crossref).
- **Common ground and the open question.** "Both Bandyopadhyay et al. and Fitelson claim that because the formulation of Simpson’s paradox does not itself appeal to causal considerations, it is a preferable to find a non-causal explanation for the paradox." (SEP §4). Sprenger & Weinberger's own assessment: "Ultimately, it is an empirical question whether the paradox can be accounted for exclusively by errors in probabilistic reasoning, or, as Pearl suggests, due to a conflation of causal and probabilistic reasoning." (§4). They record that Pearl's explanation "remains a topic of continued debate (Armistead 2014 see also Section 4)." (§3.5); Armistead's paper is titled "Resurrecting the Third Variable: A Critique of Pearl's Causal Analysis of Simpson's Paradox" (DOI record; text not read).

**Probabilistic causality** (SEP §§3.1–3.2, 3.5):

- **Cartwright (1979):** "causes always raise the probability of their effects, but this can be “concealed” by the correlation between the cause and some other variable" (SEP §3.1).
- **Dupré (1984)** "argues for abandoning the requirement that K include all causes of E, and thus for allowing average effects" (§3.2). Sprenger & Weinberger judge that the graphical framework "vindicates Dupré’s (1984) liberal attitude toward average effects against critics such as Eells and Sober (1983: 54) who dismiss it as a “sorry excuse for a causal concept”" (§3.5).

**Which table to use:**

- **Context decides — Simpson (1951), as Pearl reports him.** For the treatment example, "The treatment can hardly be rejected as valueless to the race when it is beneficial when applied to males and to females."; for a deck-of-cards example, "it is the combined table which provides what we would call the sensible answer." (Pearl 2014, p. 2, quoting Simpson).
- **No statistical criterion — Lindley & Novick (1981), as Pearl reports them:** they showed "that there was no statistical criterion that would warn the investigator against drawing the wrong conclusions or indicate which data represented the correct answer" and "with the very same data, we should consult either the combined table or the disaggregated tables, depending on the context." (Pearl 2014, p. 2).
- **The causal model decides — Pearl (back-door criterion).** Condition on Z when "1. Z is not a descendant of X, and 2. Z blocks every path that ends with an arrow into X." (2014, p. 7). Sprenger & Weinberger: "It is worth emphasizing that there is no basis for distinguishing the two causal structures in Figure 3 using statistics alone." (SEP §3.4; confounder vs. mediator). Pearl adds that "every statistical relationship between two variables may be reversed by including additional factors in the analysis" (2014, p. 8).
- **Design, not choice — Yule (1903, p. 134):** "it is only necessary to administer the antitoxin to the same proportion of patients of both sexes."
- **Decision principles.** Blyth (1972: 366, as quoted in SEP §5.3) concludes that "the Sure-Thing Principle […] seems not applicable to situations in which any action taken within f or g […] is allowed to be based sequentially on events dependent with [B]"; Jeffrey (1982) restricts it to acts probabilistically independent of states; "Pearl (2016) considers this response an “overkill”" and proposes a causal sure-thing principle (SEP §5.3). Sprenger & Weinberger's assessment: "To the extent that (conditional) degrees of belief just represent (conditional) dispositions to bet, Blyth’s reasoning is compelling." (§5.3).

## Arguments in play

(none recorded as separate argument pages yet). The propositional core of
the sure-thing reasoning, with *m* for the patient is male and *b* for the
treatment is to be preferred, is `m -> b`, `~m -> b` ⊢ `b`; `logic.py`
reports "VALID". Since the form is valid, a counterexample of the kind
Blyth (1972) offers bears on whether the premises hold, or on how the
principle is stated; Jeffrey's (1982) and Pearl's (2016) restrictions
(SEP §5.3, above) both add a condition to the principle. Logic and a
structural note, not a position.

## Thinkers who addressed it

- **Pearson, Lee & Bramley-Moore (1899)**, Phil. Trans. A
  192 — named with Yule as having "first pointed out" the phenomenon (SEP §1);
  Pearl (2014, pp. 1–2) credits them with "a short remark warns us that correlation is not causation".
- **G. Udny Yule (1903)**, Biometrika 2, §5 "On the fallacies that may be caused by the mixing of distinct records": "a pair of attributes does not necessarily exhibit independence within the universe at large even if it exhibit independence in every sub-universe" (p. 132); a mixed record shows "quite a large but illusory inheritance created simply by the mixture of the two distinct records." (p. 133); association appears "unless either A or B is independent of C." (p. 134).
- **Cohen & Nagel (1934)**, ch. 16 — a reversal "as part of a exercise for logic students" (SEP §1, citing "Nagel and Cohen"); Pearl (2014, p. 1): "Sign reversal was first noted by Cohen and Nagel (1934)".
- **Edward H. Simpson (1951)**, JRSS B 13(2): 238–241 — the paper "that led to the phenomenon being labeled as “Simpson’s Paradox”" (SEP §1); Pearl (2014, p. 2): "the word “causal” does not appear in Simpson’s paper". (Text not read here.)
- **Blyth (1972)**, JASA 67 — "labeled the reversal “paradox,”" (Pearl 2014, p. 1); the sure-thing counterexample (SEP §5.3).
- **Bickel, Hammel & O'Connell (1975)**, Science 187 — the Berkeley data (above).
- **Cartwright (1979)**; **Dupré (1984)**; **Eells (1991)** — probabilistic causality (SEP §§3.1–3.2).
- **Lindley & Novick (1981)**, Annals of Statistics 9 — context decides which table (Pearl 2014, p. 2).
- **Jeffrey (1982)** — restriction of the sure-thing principle (SEP §5.3).
- **Judea Pearl (2000/2009; 2014; 2016)** — back-door criterion, causal analysis, causal sure-thing principle.
- **Bandyopadhyay et al. (2011)**, Synthese 181; **Armistead (2014)**, American Statistician 68; **Fitelson (2017)**, Episteme 14.
- **Jan Sprenger & Naftali Weinberger (2021)**, the SEP entry, with their own assessments quoted above.

## Framings and reframings

- **Is the name apt?** Pearl (2014, p. 4) reserves "paradox" for the
  psychological phenomenon and calls the arithmetic a "reversal"; Sprenger
  & Weinberger (§4) deny it is a paradox "in the sense of presenting an inconsistent set of plausible propositions". This implant's
  [paradox](../vocabulary/paradox.md) page keeps the argument sense apart
  from the everyday "surprise" sense; this page uses the name "Simpson's
  paradox" because its sources do, without filing the case under either
  sense (structural note, manifest [G4](../../vision/manifest.md)).
- **Disappearance vs. reversal.** Pearl (2014, p. 1): Pearson, Yule and
  Simpson "reported associations that disappear, rather than reversing signs upon aggregation."; the SEP's varieties (YAP, AR, AMP) keep the cases apart.
- **Confounding.** On the graphical account "Simpson’s Paradox emerges on this account due to confounding by the third variable." (SEP §3.4), and "Only causal knowledge enables us to decide how we shall deal with the association reversal, and whether we need to condition upon Z when estimating the causal effect" (§3.2).
- **Mediator, not confounder, at Berkeley.** Sprenger & Weinberger: "assuming that gender is a cause here, then the department variable is a mediator, and one should not condition on mediators in evaluating the mediated causal relationship. So what is the justification for conditioning on department?" Their answer: "in evaluating discrimination, what often matters are path-specific effects, rather than the net effect along all paths (Pearl 2000 [2009: 4.5.3]; Zhang & Bareinboim 2018)." (§5.5).
- **Interaction is a different thing.** "What is distinctive of the paradox is not that the probabilistic relationship reverses upon partitioning, but rather that it reverses in all of the resulting subpopulations." (SEP §3.2).
- **Objectivity of causation.** Sprenger & Weinberger ask whether the paradox "threatens the objectivity of causal relationships" and answer "Properly understood, it does not." (§3.5) — their assessment.
- **Other paradox pages:** [Newcomb's problem](newcombs-problem.md),
  [the St. Petersburg paradox](st-petersburg-paradox.md),
  [the raven paradox](raven-paradox.md),
  [the lottery and preface paradoxes](lottery-and-preface-paradoxes.md),
  [the surprise examination](surprise-examination-paradox.md),
  [Zeno's paradoxes](zenos-paradoxes.md), [the sorites](sorites-paradox.md).

Left out until a source is read: Charig et al. (1986, BMJ 292: 879–882,
doi:10.1136/bmj.292.6524.879, DOI checked) — kidney-stone treatment
data; neither the SEP entry nor Pearl 2014 cites it, and no open copy of
the article's table could be fetched (PubMed Central returned a captcha),
so no number from it is given.

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — see Framings; [validity](../vocabulary/validity.md)
  (the sure-thing form); [Bayesian updating](../methods/bayesian-updating.md)
  (conditional probability).
- *Association*, *confounder*, *mediator*, *collider*, *intervention*,
  *back-door criterion*, *sure-thing principle*, *average effect* — open
  work in [vocabulary](../vocabulary/index.md).
