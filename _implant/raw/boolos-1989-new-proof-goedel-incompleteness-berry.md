# Boolos 1989 — "A New Proof of the Gödel Incompleteness Theorem" by Berry's paradox

Source: George Boolos, "A New Proof of the Gödel Incompleteness Theorem",
  Notices of the American Mathematical Society 36(4), April 1989,
  pp. 388–390, in the "Computers and Mathematics" column edited by Jon
  Barwise. (Bibliographic data as printed in the issue and as listed in
  SEP "Paradoxes and Contemporary Logic", bibliography; no DOI found.)
Original: full issue PDF at the AMS,
  https://www.ams.org/journals/notices/198904/198904FullIssue.pdf
  (PDF pp. 38–40) (copyrighted; excerpts only)
Retrieved: 2026-10-01 (PDF fetched from ams.org, read through pdftotext;
  the OCR renders "Gödel" as "Godel" and garbles some formula symbols —
  quotations below avoid the garbled passages)

> "In this note we shall give an easy new proof** of the Godel Incompleteness Theorem in the following form: There is no algorithm whose output contains all true statements of arithmetic and no false ones."  (p. 388; ** footnote below)

> "Our proof exploits Berry's paradox. In a number of writings Bertrand Russell attributed to G. G. Berry, a librarian at Oxford University, the paradox of the least integer not nameable in fewer than nineteen syllables. The paradox, of course, is that that integer has just been named in eighteen syllables."  (p. 388)

> "Saul Kripke has informed me that he noticed a proof somewhat similar to the present one in the early 1960s."  (p. 388, footnote **; the OCR has a stray "." between "somewhat" and "similar", dropped here)

> "B(x,y) says that xis named by some formula containing fewer than y symbols."  (p. 389; OCR "xis" = "x is")

> "Thus we have found a true statement that is not in the output of M"  (p. 389; M is the algorithm)

> "In our proof, symbols are the "syllables""  (p. 389, comment 1)

> "Gregory Chaitin once commented that one of his own incompleteness proofs resembled Berry's paradox rather than Epimenides' paradox of the liar"  (p. 389, comment 2; line-break hyphen in "Epi-menides" removed)

> "None of these notions are found in our proof, for which the remarks of Kreisel and Chaitin, which the author read at more or less the same time, provided the impetus."  (p. 389, comment 2; "these notions" = complexity of a natural number and information-theoretic notions)

> "In the usual proof, the number whose name is substituted is the code for the formula into which it is substituted; in ours it is the unique number of which the formula is true. In view of this distinction, it seems justified to say that our proof, unlike the usual one, does not involve diagonalization."  (p. 389, comment 4)

Relied on for: Boolos's form of the theorem; his account of Berry ("a
librarian at Oxford University"); the formula-length version; the claim of
no diagonalization and the credit to Kripke, Kreisel and Chaitin.
Context: the proof defines "a formula F(x) names the (natural) number n"
relative to the algorithm M, observes finitely many formulas of each
length (16 primitive symbols), builds C(x,z), B(x,y), A(x,y) and F(x)
("the least number not named by any formula containing fewer than 10k
symbols") and shows F has 2k + 24 < 10k symbols. Barwise's column
introduction (p. 388) calls it "the most straightforward proof of this
result that I have ever seen". Boolos quotes Russell's "It has the merit
of not going outside finite numbers" from Essays in Analysis (1973), p. 210
(the OCR reads "ment"; not quoted here).
