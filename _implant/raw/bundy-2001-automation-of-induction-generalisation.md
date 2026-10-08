# Bundy 2001 — generalisation as a search-control problem in automated inductive proof

Source: Alan Bundy, "The Automation of Proof by Mathematical Induction", in A. Robinson and
A. Voronkov (eds.), *Handbook of Automated Reasoning*, Elsevier and MIT Press, 2001, pp. 845–911
(ISBN 0-444-50813-9). Read in the accepted author manuscript (Edinburgh Research Explorer,
"Peer reviewed version"), whose own pagination is cited: §1 p. 3, §6 p. 17, §6.3.2 pp. 23–25.
Original: https://www.research.ed.ac.uk/en/publications/the-automation-of-proof-by-mathematical-induction/
(manuscript PDF read via https://web.archive.org/web/2024/https://www.research.ed.ac.uk/files/406061/908_DIA_RESEARCH_PAPER_A_BUNDY.PDF)
  (copyrighted; excerpts only)
Retrieved: 2026-10-08 (scanned manuscript, pdftotext; the OCR mangles formulas, which are therefore not quoted)

> "For instance, it is sometimes necessary to choose an induction rule, generalise the conjecture or to discover and prove an intermediate lemma. Any of these can introduce infinite branching points into the search space."  (§1, p. 3)

> "The cut rule is frequently required for two tasks: generalising the induction formula; and introducing an intermediate lemma."  (§6, p. 17)

> "This generalised conjecture is much easier to prove."  (§6.3.2, p. 23: rev(rev(l)) = l, where the stuck step case is generalised by replacing the sub-term rev(t) by a new variable)

> "Simple checking of this kind works in the majority of cases because over-generalisations are rarely false in any subtle way."  (p. 25)

Over-generalisation example (paraphrase, formulas garbled in OCR): replacing sort(l) by a new variable k turns a theorem about sort into the non-theorem "sort(k) = k" for all lists k (p. 25); Bundy reports two partial remedies — checking with a counter-example finder (Protzen 1992) and modifying the non-theorem back into a theorem, a technique he says "Moore pioneered" (Moore 1974) (p. 25).

> "However, it is not always possible to modify the non-theorem into a theorem which still subsumes the original conjecture."  (p. 25)

Relied on for: generalisation of the conjecture as a named technique and search problem in automated induction; the risk of over-generalisation to a non-theorem and the remedies Bundy reports.
Context: Bundy does not use the phrase "inventor's paradox" or cite Pólya in this chapter (grep for "inventor", "Polya" returned nothing); the page uses him only for the technique, not for the label.
