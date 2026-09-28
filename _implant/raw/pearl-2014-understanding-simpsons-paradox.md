# Pearl 2014 — "Understanding Simpson's Paradox": history, reversal vs. paradox, back-door criterion, "resolved"

Source: Judea Pearl, "Understanding Simpson's Paradox", UCLA Cognitive
  Systems Laboratory Technical Report R-414 (December 2013), the author's
  preprint of "Comment: Understanding Simpson's Paradox", The American
  Statistician 68(1) (2014): 8–13. Page numbers below are the preprint's.
Original: https://ftp.cs.ucla.edu/pub/stat_ser/r414.pdf (author's page);
  published version doi:10.1080/00031305.2014.876829
  (copyrighted; excerpts only)
Retrieved: 2026-09-27 (PDF fetched from the author's server and read via
  pdftotext; DOI resolved by content negotiation — title, author, journal,
  volume 68 issue 1, pages 8–13 matched. The preprint header reads
  "Edited version forthcoming, The American Statistician, 2014"; the
  published wording was not compared.)

## §1 History

> "Edward H. Simpson first addressed this phenomenon in a technical paper in 1951, but Karl Pearson et al. in 1899 and Udny Yule in 1903, had mentioned a similar effect earlier. All three reported associations that disappear, rather than reversing signs upon aggregation. Sign reversal was first noted by Cohen and Nagel (1934) and then by Blyth (1972) who labeled the reversal “paradox,” presumably because the surprise that association reversal evokes among the unwary appears paradoxical at first."  (p. 1)

> "The first is Pearson et al. (1899), in which a short remark warns us that correlation is not causation, and the second is Lindley and Novick (1981) who mentioned the possibility of explaining the paradox in “the language of causation” but chose not to do so “because the concept, although widely used, does not seem to be well defined” (p. 51)."  (pp. 1–2; the two exceptions Pearl finds, in his Causality (2009, p. 176) survey, to statistical articles not attributing the reversal to causal interpretations)

> "In particular, the word “causal” does not appear in Simpson’s paper, nor in the vast literature that followed, including Blyth (1972), who coined the term “paradox,”"  (p. 2)

> "His example of the latter involves a positive association between treatment and survival both among males and among females which disappears in the combined population. Here, his “sensible interpretation” is unambiguous: “The treatment can hardly be rejected as valueless to the race when it is beneficial when applied to males and to females.”"  (p. 2; quoting Simpson 1951)

> "Here, claims Simpson, “it is the combined table which provides what we would call the sensible answer.”"  (p. 2; Simpson's deck-of-cards example)

> "Lindley and Novick (1981) elevated Simpson’s paradox to new heights by showing that there was no statistical criterion that would warn the investigator against drawing the wrong conclusions or indicate which data represented the correct answer."  (p. 2)

> "Second, they showed that, with the very same data, we should consult either the combined table or the disaggregated tables, depending on the context."  (p. 2)

## §2 "A Paradox Resolved"

> "First and foremost, the solution must explain why people consider the phenomenon surprising or unbelievable. Second, the solution must identify the class of scenarios in which the paradox may surface, and distinguish it from scenarios where it will surely not surface. Finally, in those scenarios where the paradox leads to indecision, we must identify the correct answer, explain the features of the scenario that lead to that choice, and prove mathematically that the answer chosen is indeed correct."  (p. 3)

> "In explaining the surprise, we must first distinguish between “Simpson’s reversal” and “Simpson’s paradox”; the former being an arithmetic phenomenon in the calculus of proportions, the latter a psychological phenomenon that evokes surprise and disbelief."  (§2.1, p. 4)

> "“An action A that increases the probability of an event B in each subpopulation (of C) must also increase the probability of B in the population as a whole, provided that the action does not change the distribution of the subpopulations.”"  (§2.1, p. 4; Pearl quoting his own "sure-thing" theorem, Causality 2009, p. 181)

> "Thus, it is hard, if not impossible, to explain the surprise part of Simpson’s reversal without postulating that human intuition is governed by causal calculus together with a persistent tendency to attribute causal interpretation to statistical associations."  (§2.1, p. 4)

> "When dealing with a singleton covariate Z, as in the Simpson’s paradox, we need to merely ensure that 1. Z is not a descendant of X, and 2. Z blocks every path that ends with an arrow into X."  (§2.3, p. 7; numbered list run together)

> "This sequential, back and forth reversals demonstrate the disturbing observation that every statistical relationship between two variables may be reversed by including additional factors in the analysis and that, lacking causal information of the context, one cannot be sure what factor should be included in the analysis."  (§2.3, p. 8)

> "I hope that playing the multi-stage Simpson’s guessing game (Fig. 3) would convince readers that we now understand most of the intricacies of Simpson’s paradox, and we can safely title it “resolved.”"  (§3 Conclusions, p. 8)

## Appendix A — seeing vs. doing

> "Modern analysts explain away Simpson’s paradox by distinguishing seeing from doing (Lindley, 2002)."  (App. A, p. 9)

> "In our example, for instance, the drug appears beneficial overall because the males, who recover (regardless of the drug) more often than the females, are also more likely than the females to use the drug."  (App. A, p. 9)

Figure 4 (App. A, p. 10), as printed (recovered / not recovered, rate):
combined — drug 20/20 (50%), no drug 16/24 (40%); males — drug 18/12
(60%), no drug 7/3 (70%); females — drug 2/8 (20%), no drug 9/21 (30%).

Relied on for: the history (Pearson 1899, Yule 1903, Simpson 1951, Cohen &
Nagel 1934, Blyth 1972 coining "paradox"), Simpson's two "sensible"
examples as Pearl quotes them, the reversal/paradox distinction, the three
criteria and the claim "resolved", the causal sure-thing theorem, the
back-door conditions for one covariate, the multi-stage reversal
observation.
Context: a comment printed in The American Statistician 68(1) directly
after Armistead's "Resurrecting the Third Variable: A Critique of Pearl's
Causal Analysis of Simpson's Paradox" (pp. 1–7, doi:10.1080/00031305.2013.807750,
DOI checked; Armistead's text was not fetched). Pearl states his own
position throughout; the history in §1 is his account (his footnote 2
contrasts it with Hernán et al. 2011).
