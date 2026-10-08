# Brandt, Geist & Peters 2016/2017 — optimal voter bounds for Moulin's no-show paradox

Source: Felix Brandt, Christian Geist, Dominik Peters, "Optimal Bounds for
  the No-Show Paradox via SAT Solving", Proceedings of AAMAS 2016 (arXiv
  preprint 1602.08063v1, 25 Feb 2016, read here); journal version
  Mathematical Social Sciences 90 (2017) 18–27 (not read).
Original: https://arxiv.org/abs/1602.08063 (arXiv v1);
  doi:10.1016/j.mathsocsci.2016.09.003 (journal version; DOI verified by
  content negotiation: title, authors, MSS 90, pp. 18–27, Nov 2017)
  (copyrighted; arXiv non-exclusive licence; excerpts only)
Retrieved: 2026-10-09 (PDF via pdftotext, passages grepped)

> "There are a number of well-known impossibility theorems—among which Arrow’s impossibility is arguably the most famous—which state that certain axioms are incompatible with each other."  (§1)

> "One impossibility that requires unusually high bounds on the number of voters and alternatives is Moulin’s no-show paradox [28], which states that the axioms of Condorcet-consistency and participation are incompatible whenever there are at least 4 alternatives and 25 voters."  (§1)

> "Another desirable property is participation, which requires that no voter should be worse off by joining an electorate."  (Abstract)

> "A seminal result in social choice theory by Moulin [28] has shown that Condorcet-consistency and participation are incompatible whenever there are at least 4 alternatives and 25 voters."  (Abstract; [28] = Moulin, "Condorcet's principle implies the no show paradox", J. Econ. Theory 45:53–64, 1988)

> "We leverage SAT solving to obtain an elegant human-readable proof of Moulin’s result that requires only 12 voters."  (Abstract)

> "Moulin proves that the bound on the number of alternatives is tight by showing that the maximin voting rule (with lexicographic tie-breaking) satisfies the desired properties when there are at most 3 alternatives."  (§1)

> "While the desirability of Condorcet-consistency—as that of any other axiom—has been subject to criticism, many scholars agree that it is very appealing—if not indispensable—and a large part of the social choice literature deals exclusively with Condorcet-consistent voting rules"  (§1)

> "Participation was first considered by Fishburn and Brams [18] and requires that no voter should be worse off by joining an electorate, or—alternatively—that no voter should benefit by abstaining from an election. The desirability of this axiom in any context with voluntary participation is evident."  (§1)

> "All the more surprisingly, Fishburn and Brams have shown that single transferable vote (STV), a common voting rule, violates participation and referred to this phenomenon as the no-show paradox."  (§1; [18] = Fishburn & Brams, Mathematics Magazine 56(4):207–214, 1983)

> "When assuming that voters have incomplete preferences over sets or lotteries, participation and Condorcet-consistency can be satisfies simultaneously"  (§1; "satisfies" sic)

> "Ray [30] and Lepelley and Merlin [26] investigate how frequently this phenomenon occurs in practice."  (§2 Related work; [30] = Ray 1986, Math. Soc. Sci. 11(2):183–189; [26] = Lepelley & Merlin 2000, Economic Theory 17(1):53–80)

> "This bound was recently brought down to 21 voters by Kardel [23]. Simplified proofs of Moulin’s theorem are given by Schulze [33] and Smith [34]. Holzman [21] and Sanver and Zwicker [32] strengthen Moulin’s theorem by weakening Condorcet-consistency and participation, respectively."  (§2)

> "Definition 2. A voting rule f satisfies participation if all voters always weakly prefer voting to not voting"  (§3)

> "Theorem 3. There is no Condorcet extension that satisfies participation for m ⩾ 4 and n ⩾ 12."  (§6; m = alternatives, n = voters)

> "Theorem 4. There is a Condorcet extension f that satisfies participation for m = 4 and n ⩽ 11."  (§6)

Relied on for: the placing of Moulin's result among impossibility theorems beside Arrow's; the participation axiom; Moulin's bounds (4 alternatives,
  25 voters; tightness at 3 alternatives via maximin); the improvement to 12
  voters and its optimality; the related-work map (Ray, Lepelley & Merlin,
  Kardel, Schulze, Smith, Holzman, Sanver & Zwicker); the positive result
  for set/lottery preference extensions.
Context: The paper encodes the problem in propositional logic and uses SAT
  solvers; it also proves bounds for maximin (Theorem 1: no maximin
  extension with participation for m ⩾ 4, n ⩾ 7) and Kemeny (Theorem 2:
  m ⩾ 4, n ⩾ 4) extensions, and for set-valued and probabilistic rules.
