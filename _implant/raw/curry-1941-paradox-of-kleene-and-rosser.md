# Curry 1941 — the paradox of Kleene and Rosser: two completeness notions, Richard paradox, the later simplification

Source: Haskell B. Curry, "The paradox of Kleene and Rosser", Transactions
  of the American Mathematical Society 50(3), 1941, pp. 454–516 (§1,
  Introduction, pp. 454–456, with footnotes 1, 2, 5, 9).
Original: https://doi.org/10.1090/S0002-9947-1941-0005275-6
  (open PDF at https://www.ams.org/journals/tran/1941-050-03/S0002-9947-1941-0005275-6/S0002-9947-1941-0005275-6.pdf;
  copyrighted; excerpts only)
Retrieved: 2026-10-02 (PDF fetched with curl, text extracted with
  pdftotext; DOI verified by content negotiation: title "The paradox of
  Kleene and Rosser", Curry, Transactions of the American Mathematical
  Society 50(3), 454–516, 1941; line breaks and hyphenation of the
  extraction joined, footnote markers omitted)

> "In 1935 Kleene and Rosser published a proof that certain systems of formal logic are inconsistent, in the sense that every formula which can be expressed in their notation is also demonstrable"  (p. 454)

> "the argument of Kleene and Rosser represents a theorem of great importance for the guidance of future research. It is a theorem of the same general character as the famous incompleteness theorems of Löwenheim, Skolem, and Godel"  (p. 454; "Godel" as in the extracted text)

> "The proof of Kleene and Rosser is long and intricate"  (p. 454)

> "the proof depends on results in a whole series of previous papers (viz., Church's C 359.4 and 6, Kleene's C 497.1 and 2, and Rosser's 546.1), totalling 162 pages."  (p. 454, note 5)

> "I shall call these combinatorial completeness and deductive completeness respectively."  (p. 455)

> "A theory is deductively complete if whenever we can derive a proposition B on the hypothesis that another proposition A holds then we can derive without hypothesis a third proposition"  (p. 455; the sentence continues with an example implication "expressing this deducibility")

> "The essence of the Kleene-Rosser theorem is that it shows that these two kinds of completeness are incompatible—i.e., that any system which possesses both of them is inconsistent."  (p. 455)

> "The argument is essentially a refinement of the Richard paradox; it shows, in fact, that the Richard paradox can be set up formally within the system"  (p. 455)

> "In any formal system of arithmetic the number of definable numerical functions of natural numbers is enumerable"  (p. 456; the text then defines f(x) = φx(x) + 1 and, if f is φn, derives φn(n) = φn(n) + 1, "which is a contradiction.")

> "which is a contradiction."  (p. 456)

> "Since this was written, I have discovered a much simpler way of deriving the contradiction for a system which is combinatorially complete in the strong sense"  (p. 455, note 9, "Added in proof, August 21, 1941")

> "This new derivation which is based on the Russell paradox is contained in a paper, The inconsistency of certain formal logics, now in preparation."  (p. 455, note 9)

Relied on for: the 1935 result and its sense of "inconsistent"; Curry's
assessment of its importance and comparison with incompleteness theorems;
the two completeness notions; the Richard-paradox core; the note announcing
the simpler Russell-based derivation (Curry 1942).
Context: Curry says the inconsistency proof applies to "only two systems in
the literature": Church's of 1932–1933 and his own combinatory system of
1934 (p. 454; the symbol naming Curry's system is garbled in the
extraction, so that sentence is not quoted). Note 9 adds that the
significance of most of the paper's developments "is quite different from
what it seemed to be when this introduction was written".
