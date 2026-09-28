# SEP "Simpson's Paradox" (Sprenger & Weinberger) — definition, varieties, causal analysis, explanations of the paradoxicality, applications

Source: Jan Sprenger and Naftali Weinberger, "Simpson's Paradox", The
  Stanford Encyclopedia of Philosophy (Fall 2024 Edition), Edward N. Zalta
  & Uri Nodelman (eds.); first published 2021-03-24 (the archived page
  shows no later revision date; copyright line "© 2021 by Jan Sprenger,
  Naftali Weinberger"). Preamble, §§1, 2, 2.1, 2.2, 3, 3.1, 3.2, 3.4, 3.5,
  4, 5.1, 5.3, 5.5, 6.
Original: https://plato.stanford.edu/archives/fall2024/entries/paradox-simpson/
  (copyrighted; excerpts only)
Retrieved: 2026-09-27 (fetched the archived HTML and read it in a text
  extraction; every quotation below was copied from that extraction.
  Mathematical notation is rendered as plain text where it was LaTeX.)

## Preamble — definition

> "Simpson’s Paradox is a statistical phenomenon where an association between two variables in a population emerges, disappears or reverses when the population is divided into subpopulations."  (preamble)

> "Cases exhibiting the paradox are unproblematic from the perspective of mathematics and probability theory, but nevertheless strike many people as surprising."  (preamble)

> "Additionally, the paradox has implications for a range of areas that rely on probabilities, including decision theory, causal inference, and evolutionary biology."  (preamble)

> "Within the units of selection debate, Simpson reversals have played an important role in explaining the possibility of group-level selection."  (§5.4)

## §1 — Table 1 (Simpson's numbers) and the history

Table 1 as printed (success / failure / success rate):

| | Full population N=52 | Men N=20 | Women N=32 |
|---|---|---|---|
| Treatment (T) | 20 / 20 / 50% | 8 / 5 / ≈ 61% | 12 / 15 / ≈ 44% |
| Control (¬T) | 6 / 6 / 50% | 4 / 3 / ≈ 57% | 2 / 3 / ≈ 40% |

> "Table 1: Simpson's Paradox: the type of association at the population level (positive, negative, independent) changes at the level of subpopulations. Numbers taken from Simpson’s original example (1951)."  (§1, caption)

> "Should we use the treatment or not? When we know the gender of the patient, we would presumably administer the treatment, whereas it does not look like the right thing to do when we don’t know the patient’s gender—although we know that the patient is either male or female!"  (§1)

> "This phenomenon was first pointed out in papers by Karl G. Pearson (1899) and George U. Yule (1903), but it was Simpson’s short paper “The interpretation of interaction in contingency tables” (1951), discussing the interpretation of such association reversals, that led to the phenomenon being labeled as “Simpson’s Paradox”."  (§1)

> "Nagel and Cohen (1934: ch. 16) provide an example of such a reversal as part of a exercise for logic students."  (§1; "a exercise" sic)

> "early data revealed that the case fatality rate for Covid-19 was higher in Italy than in China overall. Yet within every age group the fatality rate was higher in China than in Italy."  (§1, reporting Kügelgen, Gresele & Schölkopf, listed under Other Internet Resources)

## §2 — why the reversal happens (weighted averages)

> "Second, while the treatment group is majority female (27 vs. 13), the control group is majority male (7 vs. 5)."  (§2)

> "Speaking informally, the lack of population-level correlation between treatment and recovery results from men being both (i) more likely to recover from the treatment, and (ii) less likely to be in the treatment group."  (§2)

> "Since these weights can be different, the treatment may raise the probability of success among males and females without doing so in the combined population."  (§2)

## §2.1 — varieties: AR, YAP, AMP

> "Applying all this to our dataset in Table 1, we see that α(D) = 0 although α(D_1) > 0 and α(D_2) > 0. This is a special case of what Samuels (1993) calls Association Reversal (AR)."  (§2.1; notation rendered)

> "Association reversal is the standard variety of Simpson’s Paradox (Bandyopadhyay et al. 2011; Blyth 1972, 1973) and also the one that is most frequently investigated in the psychology of reasoning, or by philosophers analyzing the paradox (e.g., Cartwright 1979; Eells 1991; Malinas 2001)."  (§2.1)

> "Referring to the pioneering work of the statistician George U. Yule (1903: 132–134), Mittal (1991) calls this Yule’s Association Paradox (YAP)."  (§2.1; "this" = no association in any subpopulation but an association in the whole)

> "For example, sleeping in one’s clothes is correlated with having a headache the next morning. However, once we stratify the data according to the levels of alcohol intake on the previous night, the association vanishes"  (§2.1)

> "Finally, the most general version of Simpson’s Paradox is the Amalgamation Paradox (AMP) identified by Good and Mittal (1987). This paradox occurs when the overall degree of association is bigger (or smaller) than each degree of association in the subpopulations"  (§2.1)

> "The logical strength of the paradoxes is inversely related to their generality and frequency of occurrence: YAP ⇒ AR ⇒ AMP."  (§2.1; notation rendered)

## §2.2 — conditions

> "Theorem 1 (Lindley & Novick 1981; Mittal 1991)"  (§2.2; the theorem: if the whole shows positive association and reversal occurs in the subpopulations M and ¬M, then M is related to both S and T)

> "As Theorem 1 makes clear, the lack of correlation between M and T is sufficient to rule out association reversals (and thus YAP as well)."  (§2.2; notation rendered)

> "Theorem 2 (Good & Mittal 1987): If a dataset D = ∑ D_i satisfies row uniformity, then the Amalgamation Paradox is avoided for the measures π_D,"  (§2.2; the list continues, and ends "not avoided for the log-odds ratio π_O")

> "Simulations by Pavlides and Perlman (2009) suggest that it should not occur frequently: the confidence interval for the probability of AR is a subset of the interval [0;0.03] for both the uniform prior and the (objective) Jeffreys prior."  (§2.2)

## §3 — causal inference

> "Within the philosophical literature, Simpson’s Paradox received sustained attention due to its implications for accounts of causality that posit systematic connections between causal relationships and probability-raising."  (§3)

> "Strategies for treating the paradox and answering these questions have contributed substantially to the development of theories of probabilistic causality (Cartwright 1979; Eells 1991)."  (§3)

> "Cartwright interprets this case as follows: causes always raise the probability of their effects, but this can be “concealed” by the correlation between the cause and some other variable"  (§3.1)

> "Simpson’s Paradox should not be conflated with causal interaction, however. What is distinctive of the paradox is not that the probabilistic relationship reverses upon partitioning, but rather that it reverses in all of the resulting subpopulations."  (§3.2)

> "Dupré (1984) argues for abandoning the requirement that K include all causes of E, and thus for allowing average effects."  (§3.2; notation rendered)

> "Only causal knowledge enables us to decide how we shall deal with the association reversal, and whether we need to condition upon Z when estimating the causal effect"  (§3.2, Debate 3: Mediators)

> "Simpson’s Paradox emerges on this account due to confounding by the third variable."  (§3.4; "this account" = the graphical, identifiability account)

> "The causal approach makes it easy to see why one should."  (§3.4; the preceding sentence: "Should one approve the drug or not?")

> "It is worth emphasizing that there is no basis for distinguishing the two causal structures in Figure 3 using statistics alone."  (§3.4; Figure 3 = gender as confounder vs. pregnancy as mediator, Hesslow 1976)

> "So Pearl’s explanation of the paradox is that people conflate causal and non-causal expressions, and if the conditional probabilities in the examples are interpreted causally, Simpson’s reversals are impossible."  (§3.4)

> "Whether Pearl provides the correct causal explanation of Simpson’s Paradox remains a topic of continued debate (Armistead 2014 see also Section 4)."  (§3.5)

> "this fact vindicates Dupré’s (1984) liberal attitude toward average effects against critics such as Eells and Sober (1983: 54) who dismiss it as a “sorry excuse for a causal concept”"  (§3.5)

> "This brings us to the issue of whether Simpson’s Paradox threatens the objectivity of causal relationships. Properly understood, it does not."  (§3.5)

## §4 — what makes it paradoxical

> "Simpson’s Paradox is not a paradox in the sense of presenting an inconsistent set of plausible propositions of which at least one must be rejected."  (§4)

> "Why or in what sense is Simpson’s Paradox a paradox? What is the proper analysis of the paradox? How one should proceed when confronted with a typical case of the paradox?"  (§4; Bandyopadhyay et al.'s (2011) three questions as the SEP lists them, numbered (i)–(iii) in the original)

> "On Pearl’s causal analysis, the appearance of a paradox results from a conflation between causal and probabilistic reasoning."  (§4)

> "Bandyopadhyay et al. (2011) reject Pearl’s causal analysis of the paradox, and defend an alternative mathematical explanation."  (§4)

> "If there are cases of the paradox that still exhibit surprise despite having nothing to do with causality, then the general explanation of the paradox cannot be causal."  (§4; the marbles-in-two-bags example)

> "Bandyopadhyay et al. conducted a survey with university students on this matter: only 12% give the correct answer that equations (6), by themselves, do not constrain the truth value of equation (7)."  (§4)

> "Yet Bandyopadhyay et al. do not specify what this error is."  (§4 — the SEP authors' assessment)

> "Recently, Fitelson (2017) has proposed a confirmation-theoretic explanation of Simpson’s Paradox."  (§4)

> "Fitelson’s confirmation-theoretic explanation of Simpson’s Paradox is that reasoners are not attentive to the difference between the suppositional and conjunctive readings of confirmation statements when considering the evidential relevance of learning an individual’s gender."  (§4)

> "Both Bandyopadhyay et al. and Fitelson claim that because the formulation of Simpson’s paradox does not itself appeal to causal considerations, it is a preferable to find a non-causal explanation for the paradox."  (§4; "a preferable" sic)

> "Ultimately, it is an empirical question whether the paradox can be accounted for exclusively by errors in probabilistic reasoning, or, as Pearl suggests, due to a conflation of causal and probabilistic reasoning."  (§4 — the SEP authors' assessment)

> "The empirical evidence on the paradox shows that reasoners find trivariate reasoning (i.e., with a causally relevant third variable) generally hard and fail to take its role properly into account, even if salient cues to its relevance are provided (Fiedler, Walther, Freytag, & Nickel 2003)."  (§4)

## §5 — applications

> "the overall SAT average rises from 1992 to 2002, but for each GPA group (A+/A/…), SAT averages are falling."  (§5.1, Table 4 from Rinott & Tam 2003)

> "Blyth (1972) argued that Simpson’s Paradox also constitutes a counterexample to the sure-thing principle of decision theory, or at least restricts its scope substantially."  (§5.3)

> "the Sure-Thing Principle […] seems not applicable to situations in which any action taken within f or g […] is allowed to be based sequentially on events dependent with [B]"  (§5.3, block-quoting Blyth 1972: 366; the SEP's ellipses and bracket; f, g, B are italic/roman symbols in the original)

> "To the extent that (conditional) degrees of belief just represent (conditional) dispositions to bet, Blyth’s reasoning is compelling."  (§5.3 — the SEP authors' assessment)

> "Pearl (2016) considers this response an “overkill” and notes that probabilistic associations are not a good means of expressing causal tendencies."  (§5.3; "this response" = Jeffrey's (1982) restriction of the sure-thing principle to acts probabilistically independent of states)

> "A distinct concern is that an agent may not be sure whether her action counts as an intervention (e.g., in Newcomb scenarios), since it might not be clear whether she can manipulate a variable to render it independent of its prior causes (Stern 2019)."  (§5.3)

> "Bickel et al. (1975) present a classic example of Simpson’s Paradox involving a study of gender discrimination at Berkeley."  (§5.5)

> "But assuming that gender is a cause here, then the department variable is a mediator, and one should not condition on mediators in evaluating the mediated causal relationship. So what is the justification for conditioning on department?"  (§5.5)

> "The answer is that in evaluating discrimination, what often matters are path-specific effects, rather than the net effect along all paths (Pearl 2000 [2009: 4.5.3]; Zhang & Bareinboim 2018)."  (§5.5)

## §6 — conclusions

> "Pearl’s account renders certain debates from the earlier literature moot, while opening up new debates about the proper interpretation of the paradox."  (§6)

> "There is perhaps nothing paradoxical about Simpson’s Paradox, but since we often struggle to understand it, our reasoning about association reversals may be entangled with various forms of reasoning that are susceptible to bias and error."  (§6)

## Bibliographic data from the entry (checked)

- Pearson, Karl, 1899, Phil. Trans. R. Soc. A 192 — the SEP gives pages
  "260–278"; Crossref (DOI 10.1098/rsta.1899.0006, authors Pearson, Lee,
  Bramley-Moore) gives 257–330, as does Pearl 2014's reference list.
- Simpson 1951, doi:10.1111/j.2517-6161.1951.tb00088.x; Yule 1903,
  doi:10.1093/biomet/2.2.121; Bickel et al. 1975,
  doi:10.1126/science.187.4175.398; Blyth 1972,
  doi:10.1080/01621459.1972.10482387; Armistead 2014,
  doi:10.1080/00031305.2013.807750; Bandyopadhyay et al. 2011,
  doi:10.1007/s11229-010-9797-0; Pearl 2016 doi:10.1515/jci-2016-0005 —
  all resolved by DOI content negotiation on 2026-09-27 (titles, authors,
  volumes, pages matched).

Relied on for: the definition, Table 1, the history as the SEP gives it,
the AR/YAP/AMP varieties and Theorems 1–2, the probabilistic-causality
debates, the graphical/confounding account, Pearl's explanation as the SEP
reports it, Bandyopadhyay et al. and Fitelson as reported, Blyth/Jeffrey/
Pearl on the sure-thing principle, the Berkeley mediator question, and
the authors' own assessments (each attributed on the page).
Context: the entry is a survey written after Pearl commented on a draft
(acknowledgements: "Judea Pearl for extensive comments on a previous
draft"); §4 is where the authors assess the rival explanations; §6 is
their conclusion.
