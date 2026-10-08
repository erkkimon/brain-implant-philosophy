# Manber 1988 — strengthening the induction hypothesis and Pólya's inventor's paradox

Source: Udi Manber, "Using Induction to Design Algorithms", *Communications of the ACM* 31(11),
November 1988, pp. 1300–1313; section "Strengthening the Induction Hypothesis", p. 1307
(abstract and list of variations p. 1300–1301). Reference [14] there: "Polya, G. How to Solve It. 2nd ed., Princeton University Press, 1957."
Original: doi:10.1145/50087.50091 (verified by DOI content negotiation 2026-10-08: title,
journal, vol. 31, issue 11, pp. 1300–1313, 1988). Text read in the Wayback copy
https://web.archive.org/web/20240423220259/https://dl.acm.org/doi/pdf/10.1145/50087.50091
  (copyrighted; excerpts only)
Retrieved: 2026-10-08 (PDF through pdftotext; page number from the page footer; line-end hyphens rejoined)

> "Among the variations of induction that we discuss are choosing the induction sequence wisely, strengthening the induction hypothesis, strong induction, and maximal counterexample."  (p. 1301)

> "Strengthening the induction hypothesis is one of the most important techniques of proving mathematical theorems with induction."  (p. 1307)

> "Many times one can add another assumption, call it Q, under which the proof becomes easier."  (p. 1307)

> "The trick is to include Q in the induction hypothesis (if it is possible)."  (p. 1307)

> "The combined theorem [P and Q] is a stronger theorem than just P, but sometimes stronger theorems are easier to prove (Polya [14] calls this principle the inventor’s paradox)."  (p. 1307)

> "which is to ignore the fact that an additional assumption was added and forget to adjust the proof."  (p. 1307, describing "the most common error made while using this technique")

> "Stronger induction hypothesis: We know how to compute balance factors and heights of all nodes in trees with <n nodes."  (p. 1307, balance factors of binary trees)

> "The key to the algorithm is to solve a slightly extended problem. Instead of just computing balance factors, we also compute heights."  (p. 1307)

> "In many cases, solving a stronger problem is easier. This is especially true for induction."  (p. 1307)

Relied on for: the computer-science use of the name, tied explicitly to Pólya 1957; the schema P(n−1) & Q ⇒ P(n) turned into (P and Q)(n−1) ⇒ (P and Q)(n) (Manber writes square brackets); the balance-factor example; the error Manber names.
Context: the article's thesis is an analogy between proving theorems by induction and designing algorithms; earlier examples (polynomial evaluation, interval containment) already use stronger hypotheses, as Manber notes on p. 1307.
