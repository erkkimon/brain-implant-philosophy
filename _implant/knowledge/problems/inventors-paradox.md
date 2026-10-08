---
type: article
about: concept
title: "Inventor's paradox"
description: "Why can a more general or stronger problem be easier to solve than the special one it covers? Pólya's 1945 dictionary entry ('The more ambitious plan may have more chances of success'), his octahedron and sum-of-cubes examples, his own claim that 'The paradox disappears' on inspection, and the later use of the name for strengthening the induction hypothesis in algorithm design and automated proof (Manber 1988, Waldinger 2022; generalisation in Bundy 2001)."
tags: [problem, paradox, decision-theory, heuristics, mathematics, induction]
timestamp: 2026-10-08T20:29:06Z
---

# Inventor's paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
sources graded as in [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Primary text: George Pólya, *How to Solve It*, 1945, 2nd ed. 1957, entry "Inventor's paradox",
pp. 121–122 ([doi:10.1515/9781400828678-042](https://doi.org/10.1515/9781400828678-042);
scan read: [archive.org](https://archive.org/details/how-to-solve-it-a-new-aspect-of-mathematical-method-george-polya);
excerpt: `raw/polya-1957-how-to-solve-it-inventors-paradox.md`).
Later uses: Manber 1988 ([doi:10.1145/50087.50091](https://doi.org/10.1145/50087.50091);
excerpt: `raw/manber-1988-using-induction-to-design-algorithms-inventors-paradox.md`),
Waldinger 2022 ([arXiv:2211.09923](https://arxiv.org/abs/2211.09923);
excerpt: `raw/waldinger-2022-unification-synthesis-inventors-paradox.md`),
Bundy 2001 ([Edinburgh Research Explorer](https://www.research.ed.ac.uk/en/publications/the-automation-of-proof-by-mathematical-induction/);
excerpt: `raw/bundy-2001-automation-of-induction-generalisation.md`).
Admitted from Wikipedia's [List of paradoxes, revision 1376699902](https://en.wikipedia.org/w/index.php?oldid=1376699902),
"Decision theory"; the article [rev. 1292932298](https://en.wikipedia.org/w/index.php?oldid=1292932298)
was used as a pointer to sources
(excerpt: `raw/wikipedia-inventors-paradox-rev-1292932298-and-list-entry.md`).

## The question

Pólya's entry: "Inventor’s paradox. The more ambitious plan may have more chances of success." (*How to Solve It*, p. 121).
He continues: "This sounds paradoxical. Yet, when passing from one problem to another, we may often observe that the new, more ambitious problem is easier to handle than the original problem. More questions may be easier to answer than just one question. The more comprehensive theorem may be easier to prove, the more general problem may be easier to solve." (p. 121).
*More ambitious* is defined in his entry "Auxiliary problem", §8, by
unilateral reduction between two unsolved problems A and B: "If we could solve A we could hence derive the full solution of B. But not conversely" (p. 55); "Let us call A the more ambitious, and B the less ambitious of the two problems." (p. 55).
Wikipedia's list gives: "Inventor's paradox: It is easier to solve a more general problem that covers the specifics of the sought-after solution." (rev. 1376699902).
Structural note (this implant): the list says "It is easier"; Pólya says "may" and "may often".

Whether "paradox" fits is addressed by Pólya himself, who writes that it
"sounds paradoxical" and that "The paradox disappears if we look closer at a few examples (GENERALIZATION, 2; INDUCTION AND MATHEMATICAL INDUCTION, 7)." (pp. 121–122).
For his own induction example Pólya states the direction of implication: "The second assertion is stronger; it implies immediately the first, whereas the somewhat “hazy” first assertion can hardly imply the more “clear-cut’’ second one." (p. 121).

**Propositional check (this implant, 2026-10-08; logic, not a position).**
`logic.py check --premises "P & Q" --conclusion "P"` outputs `VALID`: the stronger
conjunction yields the weaker conjunct. The check says nothing about which is easier
to *find* a proof for, which is what Pólya's heuristic concerns.

## Why it matters

- Pólya places it inside his account of auxiliary problems: a step to a
  more or less ambitious problem is a "unilateral reduction", and "Unilateral reduction to a more ambitious problem may also be successful." (p. 56); of the less ambitious kind he says "with some luck, we may be able to use a less ambitious auxiliary problem as a stepping stone" (p. 56).
- In algorithm design, Manber (1988) calls the related technique central to
  induction proofs: "Strengthening the induction hypothesis is one of the most important techniques of proving mathematical theorems with induction." (p. 1307).
- In program synthesis and automated proof: Waldinger (2022) and Bundy (2001), quoted under the arguments below.
- Wikipedia's article (rev. 1292932298, lead) says the name "has been used to describe phenomena in mathematics, programming, and logic, as well as other areas that involve critical thinking." — its summary, citing works not read here.

## Positions taken

No position page exists, and no survey was found. On record:

- **Heuristic, with a proviso** — Pólya: the more ambitious plan may succeed
  "provided it is not based on mere pretension but on some vision of the things beyond those immediately present." (p. 122).
- **The appearance of paradox dissolves on examples** — Pólya: "The more general problem may be easier to solve. This sounds paradoxical but, after the foregoing example, it should not be paradoxical to us." (Generalization §2, p. 109).
- **"Sometimes", as a proof technique** — Manber: "The combined theorem [P and Q] is a stronger theorem than just P, but sometimes stronger theorems are easier to prove (Polya [14] calls this principle the inventor’s paradox)." (p. 1307).
- **Generalisation can overshoot** — Bundy reports that an automated prover
  can generalise a theorem into a non-theorem (§6.3.2, p. 25), and that
  "it is not always possible to modify the non-theorem into a theorem which still subsumes the original conjecture." (p. 25).
  Bundy does not use Pólya's name in this chapter; Manber and Waldinger,
  not Bundy, attach the label to strengthening or generalising in induction.
- Wikipedia's article lists under "See also" "Architecture astronaut, related to the converse problem where abstraction is taken too far." (rev. 1292932298); no source is given there for that link.

## Arguments in play

(no argument page yet)

Pólya's examples, as he gives them:

1. **The octahedron** (Generalization §2). The problem: "A straight line and a regular octahedron are given in position. Find a plane that passes through the given line and bisects the volume of the given octahedron." (p. 108).
   The more general problem: "A straight line and a solid with a center of symmetry are given in position. Find a plane that passes through the given line and bisects the volume of the given solid." (p. 109).
   Its solution: "The plane required passes, of course, through the center of symmetry of the solid, and is determined by this point and the given line." (p. 109).
   Pólya: "The reader will not fail to observe that the second problem is more general than the first, and, nevertheless, much easier than the first. In fact, our main achievement in solving the first problem was to invent the second problem." (p. 109).
2. **The plane figure** (Part IV, problem 6): a point and a plane figure with
   a centre of symmetry; the solution reads "The required line passes, of course, through the center of symmetry. See INVENTOR’S PARADOX." (p. 243).
3. **Sums of cubes** (Induction and mathematical induction, §§1–2 and the closing comment on p. 121). From a
   table of cases Pólya conjectures "The sum of the first n cubes is a square." (p. 115), then the more precise 1³ + 2³ + ··· + n³ = (1 + 2 + ··· + n)² (p. 117), which he proves by passage from n to n + 1; he concludes "Thus, the stronger theorem is easier to master than the weaker one; this is the INVENTOR’S PARADOX." (p. 121), because "Dealing with the first assertion, and ignoring the precision added to it by the second one, we should scarcely have been able to find such a proof." (p. 121).
   Arithmetic (this implant, 2026-10-08): for n = 5, 1 + 8 + 27 + 64 + 125 = 225 = (1 + 2 + 3 + 4 + 5)², Pólya's last table row (p. 115).

The induction schema, as Manber gives it: the hypothesis P(n − 1) does not
suffice, but with an added assumption Q "the proof becomes easier"; "The trick is to include Q in the induction hypothesis (if it is possible)." (p. 1307); one then proves (P and Q)(n − 1) ⇒ (P and Q)(n), in Manber's bracket notation.
His example computes balance factors of binary trees: "Stronger induction hypothesis: We know how to compute balance factors and heights of all nodes in trees with <n nodes." (p. 1307); "In many cases, solving a stronger problem is easier. This is especially true for induction." (p. 1307).

**Propositional check (this implant, 2026-10-08; logic, not a position).**
For one inductive step with atoms P0, Q0, P1, Q1:
`logic.py check --premises "P0 & Q0" "(P0 & Q0) -> (P1 & Q1)" --conclusion "P1"`
outputs `VALID`. The step Manber calls "the most common error" — proving
P(n) from [P(n − 1) and Q] while forgetting that Q was assumed, "which is to ignore the fact that an additional assumption was added and forget to adjust the proof." (p. 1307) —
corresponds to `--premises "P0" "(P0 & Q0) -> P1" --conclusion "P1"`, which
outputs `INVALID` with counterexample `P0=T, P1=F, Q0=F`.

Waldinger (2022, PDF p. 14): "To conduct a proof by mathematical induction, it is often necessary to generalize the theorem to obtain the benefit of a stronger induction hypotheses. (This observation is an instance of the [Polya 57] Inventor’s Paradox and was famously exploited in the [Boyer Moore 79] theorem prover.)"
His own case: "we have found it necessary to strengthen the specification by requiring that the most-general unifier be idempotent" (PDF p. 14).

Bundy (2001) on mechanising the move: "The cut rule is frequently required for two tasks: generalising the induction formula; and introducing an intermediate lemma." (§6, p. 17); for rev(rev(l)) = l, replacing a sub-term by a new variable yields a formula of which he writes "This generalised conjecture is much easier to prove." (§6.3.2, p. 23); on checking candidates, "over-generalisations are rarely false in any subtle way." (p. 25).

## Thinkers who addressed it

- **George Pólya** (1945; 2nd ed. 1957) — names the inventor's paradox in *How
  to Solve It*, pp. 121–122, with examples at pp. 55–56, 108–109, 114–121, 243.
  His *Mathematics and Plausible Reasoning* (1954): vol. I not readable here;
  vol. II (1968 ed. text) has no "inventor's" + "paradox" passage — nothing reported.
- **Udi Manber** (1988) — *CACM* 31(11), p. 1307: strengthening the induction hypothesis, tied to Pólya's name.
- **Alan Bundy** (2001) — *Handbook of Automated Reasoning*, §6: generalisation as a search problem (no use of Pólya's label).
- **Richard Waldinger** (2022) — LPOP paper, PDF p. 14: generalising an induction theorem as an instance of Pólya's paradox.
- Further items carrying the name, bibliographically verified only (titles
  by DOI content negotiation; contents not read): Man-Keung Siu, *Inventor's
  Paradox*, *Two-Year College Mathematics Journal* 12(4), 1981, p. 267
  ([doi:10.2307/3027074](https://doi.org/10.2307/3027074)); Philip Ording, *99
  Variations on a Proof*, 2019, ch. 58, *Inventor’s Paradox*, pp. 137–138
  ([doi:10.1515/9780691185422-060](https://doi.org/10.1515/9780691185422-060));
  Ruan, Anslow, Marshall & Noble, *Exploring the inventor's paradox: applying
  jigsaw to software visualization*, 2010
  ([doi:10.1145/1879211.1879226](https://doi.org/10.1145/1879211.1879226)).
- Jon Bentley, *Programming Pearls*, 2nd ed., 2000, p. 29 (index entry
  "Inventor's Paradox 29"; page text not read) — Wikipedia cites it for the
  "23-case problem" versus "n-case problem" example.

## Framings and reframings

- **From paradox to heuristic** — Pólya writes that the paradox "disappears" on examples
  (pp. 121–122); in his reading, the work lies in inventing the general
  problem: "The main achievement in solving the special problem was to invent the general problem." (p. 109).
- **From mathematics to algorithms** — Manber reframes induction proofs as an
  algorithm-design method, with strengthening the hypothesis as one variation
  among "choosing the induction sequence wisely, strengthening the induction hypothesis, strong induction, and maximal counterexample." (p. 1301).
- **From heuristic to search control** — Bundy lists generalising the conjecture among choices that "can introduce infinite branching points into the search space" (§1, p. 3), calling for heuristics (§6, p. 17).
- **Filed under decision theory** — Wikipedia's list places the entry in
  "Decision theory" and the article carries the category "Decision-making
  paradoxes" (rev. 1292932298); none of the sources read here frames it as a
  decision-theoretic problem (structural note, this implant).

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — Pólya's own label, which he says
  "disappears" on inspection.
- [Validity](../vocabulary/validity.md) — used in the checks above.
- Not yet in the vocabulary: *mathematical induction*, *induction hypothesis*, *generalisation*, *heuristic*, *auxiliary problem*, *unilateral reduction* (Pólya, pp. 55–56).
