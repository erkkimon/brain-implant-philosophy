# SEP Fall 2024 "Self-Reference and Paradox" (Bolander) — Grelling's paradox, its structure and the halting problem

Source: Thomas Bolander, "Self-Reference and Paradox", Stanford
  Encyclopedia of Philosophy (Fall 2024 Edition), ed. Edward N. Zalta &
  Uri Nodelman; first published 2008-07-15, substantive revision
  2024-07-19. §1.1 "Semantic Paradoxes", §1.4 "Common Structures in the
  Paradoxes", §2.4 "Consequences Concerning Provability and Computability".
Original: https://plato.stanford.edu/archives/fall2024/entries/self-reference/
  (copyrighted; excerpts only)
Retrieved: 2026-10-02 (archive HTML fetched with curl, tags stripped, grepped;
  line breaks of the HTML joined)

> "Say a predicate is heterological if it is not true of itself, that is, if it does not itself have the property it expresses. Then the predicate “German” is heterological, since it is not itself a German word, but the predicate “deutsch” is not heterological."  (§1.1)

> "Is “heterological” heterological?"  (§1.1)

> "It is easy to see that we obtain a contradiction independently of whether we answer “yes” or “no” to this question (the argument runs more or less like in the liar paradox)."  (§1.1)

> "Grelling’s paradox is self-referential, since the definition of the predicate heterological refers to all predicates, including the predicate heterological itself."  (§1.1)

> "Grelling’s paradox involves the predicate heterological, which is true of all those predicates that are not true of themselves."  (§1.4)

> "The only significant difference between these two sets is that the first is defined on predicates whereas the second is defined on sets."  (§1.4, comparing the extension of "heterological" with the Russell set)

> "We have here two paradoxes of an almost identical structure belonging to two distinct classes of paradoxes: one is semantic and the other set-theoretic."  (§1.4)

> "Thus in many cases it makes most sense to study the paradoxes of self-reference under one, rather than study, say, the semantic and set-theoretic paradoxes separately."  (§1.4)

> "The proof mimics Grelling’s paradox."  (§2.4, proof of the undecidability of the halting problem)

> "We call a Turing machine \(A\) heterological if \(A\) doesn’t halt on input \(\langle A\rangle\), that is, if \(A\) doesn’t halt when given its own Gödel code as input."  (§2.4)

Relied on for: Bolander's statement of the paradox, his "German"/"deutsch"
examples, the self-reference and impredicativity remarks, the comparison
with Russell's set, and the halting-problem proof that "mimics" it, on
problems/grelling-nelson-paradox.md. (The §1.1 sentences on semantic
paradoxes, impredicativity and the §2 "deficient" assessment are already in
sep-self-reference-fall-2024-berry-paradox.md and are reused from there.)
Context: §1.1 follows the liar with Grelling, then Berry. §1.4 sets out the
two chains of equivalences in LaTeX (het ∈ ext(het) ⇔ het ∉ ext(het);
R ∈ R ⇔ R ∉ R) and goes on to Cantor's theorem. §2.4 proves Gödel's first
incompleteness theorem and then the halting theorem; the chain ends
"G is not heterological", and the entry adds that "the paradoxes of
self-reference turn into limitation results".
