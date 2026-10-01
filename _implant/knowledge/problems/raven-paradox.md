---
type: article
about: concept
title: "The raven paradox (Hempel's paradox of confirmation)"
description: "Hempel's (1945) 'paradoxes of confirmation': Nicod's criterion plus the equivalence condition make a non-black non-raven — a red pencil, a white shoe — confirm 'all ravens are black'. The responses on record, each with its owner: accept the conclusion (Hempel, Goodman), restrict to natural kinds (Quine), hypothetico-deductive blocking, and the Bayesian comparative and quantitative answers (Hosiasson-Lindenbaum, Good, Maher, Vranas, Fitelson & Hawthorne)."
tags: [problem, paradox, epistemology, philosophy-of-science, logic]
timestamp: 2026-10-01T19:53:21Z
---

# The raven paradox (Hempel's paradox of confirmation)

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
claim grades as in [How claims are graded](../../conventions/how-claims-are-graded.md).
Part of the [problems](./index.md) branch. Map: Vincenzo Crupi,
[SEP Fall 2024 "Confirmation"](https://plato.stanford.edu/archives/fall2024/entries/confirmation/)
(revised 2020-01-28; excerpt: `raw/sep-confirmation-fall-2024-ravens-paradox.md`).
Primary: Hempel, "Studies in the Logic of Confirmation (I.)", *Mind* 54, 1945
([doi](https://doi.org/10.1093/mind/LIV.213.1); excerpt: `raw/hempel-1945-studies-logic-of-confirmation-ravens.md`);
Goodman, *Fact, Fiction, and Forecast*, 1955 ([scan](https://archive.org/details/fact-fiction-and-forecast); excerpt: `raw/goodman-1955-fact-fiction-forecast-ravens-and-grue.md`);
Good 1960 ([doi](https://doi.org/10.1093/bjps/XI.42.145-b); excerpt: `raw/good-1960-paradox-of-confirmation-white-shoe.md`).
Survey: Fitelson & Hawthorne 2010 ([doi](https://doi.org/10.1007/978-90-481-3615-5_11); excerpt: `raw/fitelson-hawthorne-2010-bayesian-ravens.md`).
Works cited but not read: `raw/raven-paradox-bibliographic-records.md`.
"Confirmation" here is evidential support, not the [confirmation bias](../biases/confirmation-bias.md).

## The question

Hempel names Nicod's condition: "We shall refer to this criterion as Nicod’s criterion." (1945, p. 10). In his words: "In other words, an object confirms a universal conditional hypothesis if and only if it satisfies both the antecedent (here: ‘ P(x).’) and the consequent (here: ‘ Q(x) ’) of the conditional ; it disconfirms the hypothesis if and only if it satisfies the antecedent, but not the consequent of the conditional ; and (we add this to Nicod’s statement) it is neutral, or irrelevant, with respect to the hypothesis if it does not satisfy the antecedent." (p. 10).
He adds a second condition: "Equivalence condition : Whatever confirms (disconfirms) one of two equivalent sentences, also confirms (disconfirms) the other." (p. 12).
Take S1 "All ravens are black" and S2 "Whatever is not black is not a raven". Then:
"Consequently, any red pencil, any green leaf, and yellow cow, etc., becomes confirming evidence for the hypothesis that all ravens are black." (p. 14);
"This implies that any non-raven represents confirming evidence for the hypothesis that all ravens are black." (p. 14);
"We shall refer to these implications of the equivalence criterion and of the above sufficient condition of confirmation as the paradoxes of confirmation." (p. 14).

Fitelson & Hawthorne set it out as a three-step "canonical derivation" (2010, pp. 247–248) from the Nicod Condition (NC) and the Equivalence Condition (EC) to the "Paradoxical Conclusion (PC): The proposition that a is both non-black and a non-raven, [~Ba · ~Ra], confirms the proposition that every raven is black, [(∀x)(Rx ⊃ Bx)]." (p. 248).
Crupi's version asks whether the black raven and the non-black non-raven confirm alike: "One would want to say no, but Hempel’s theory is unable to draw this distinction." (SEP §1.2).
The white shoe is Good's example: "The hypothesis, H, that all crows are black is the same as that all non-black things are not crows, and this is supported by the observation of a white shoe. Which seems paradoxical." (1960, p. 146).

**Logic check (this implant, 2026-09-27).** Propositional skeleton of the
instance step, with `r` for *a is a raven* and `b` for *a is black*
(`python3 _implant/skills/tools/logic.py check --premises … --conclusion …`):

```
  P1: r -> b    [(r -> b)]
  C:  ~b -> ~r    [(~b -> ~r)]

VALID
```
```
  P1: ~b -> ~r    [(~b -> ~r)]
  C:  r -> b    [(r -> b)]

VALID
```
```
  P1: ~r    [~r]
  C:  r -> b    [(r -> b)]

VALID
```
```
  P1: r -> b    [(r -> b)]
  C:  b -> r    [(b -> r)]

INVALID
Counterexamples (premises true, conclusion false):
  b=T, r=F
  (1 counterexample row)
```

The first two checks give the equivalence of the conditional and its
contrapositive that step 2 of the derivation uses (F&H: "2. By Classical Logic, [(∀x)(~Bx ⊃ ~Rx)] is equivalent to [(∀x)(Rx ⊃ Bx)]."; Crupi: "But h* ⊨ h (h and h* are just logically equivalent)."). The third is the
instance-level fact behind Crupi's remark that h "is (directly) Hempel-confirmed by the observation of any object that is not a raven" (§1.2): a non-raven satisfies the conditional. The fourth shows that the contrapositive
is not the converse. These are checks on the propositional form only; the
quantified sentences and the confirmation relation are not what logic.py
evaluates.

## Why it matters

- **Formal confirmation theory.** Crupi: "Nicod’s work was an influential source for Carl Gustav Hempel’s (1943, 1945) early studies in the logic of confirmation." (§1); the entry returns to the ravens in its hypothetico-deductive and Bayesian sections (§§2.2, 3.6).
- **A charge against instance confirmation.** Crupi: "The above, widely known “paradoxes” then suggest that Hempel’s analysis of confirmation is too liberal: it sanctions the existence of confirmation relations that are intuitively very unsound" (§1.2, citing Earman and Salmon 1992 and Sprenger 2011a).
- **A literature.** F&H: "For a nice taste of this voluminous literature, see the bibliography in Vranas (2004)." (2010, n. 1); Chihara, as F&H quote him: "there is no such thing as the Bayesian solution. There are many different ‘solutions’ that Bayesians have put forward using Bayesian techniques" (n. 9).

## Positions taken

Grouped by this page according to which step of the canonical derivation
each response accepts or denies, following the order of F&H 2010,
pp. 248–256. No position is ranked here; assessments by
Crupi and by F&H are marked as theirs.

- **Accept (PC); the paradox is an illusion — Hempel, Goodman.** F&H: "Hempel (1945) and Goodman (1954) didn’t view (PC) as paradoxical. Indeed, Hempel and Goodman viewed the argument above from (1) and (2) to (PC) as sound." (p. 248).
  Hempel: "The impression of a paradoxical situation is not objectively founded ; it is a psychological illusion." (1945, p. 18). Goodman: "The trouble this time, however, lies not in faulty definition, but in tacit and illicit reference to evidence not stated in our example." (1955, p. 71).
  - *Case against:* F&H: "As it turns out, Hempel’s official theory of confirmation is logically incompatible with his intuitive characterization of what is going on." (p. 251).
- **Keep the equivalence condition.** Hempel: "Renouncing the equivalence condition would not represent an acceptable solution, as is shown by the considerations presented in section 4." (p. 14). F&H report that "not all contemporary commentators are so sanguine about (EC) and (2)", citing Sylvan and Nola (1991) on non-classical logics and Gemes (1999) for "a probabilistic approach that also denies premise (2)" (n. 2).
- **Reject (PC) and restrict Nicod to natural kinds — Quine.** F&H: "Unlike Hempel and Goodman, Quine rejects the paradoxical conclusion (PC)." (p. 249); "To summarize, Quine thinks (PC) is false, and that the (valid) canonical argument for (PC) is unsound because (NC) is false." (p. 249). Quine, "Natural Kinds" (Crossref 1969, [doi](https://doi.org/10.1007/978-94-017-1466-2_2); SEP cites "Quine 1970"), was not read here.
  - *Case against:* Crupi: "Yet this point turns out be very difficult to pursue coherently and it has not borne much fruit in this discussion (Rinard 2014 is a recent exception)." (§1.2).
- **Hypothetico-deductive confirmation.** Crupi: "One attractive feature of HD-confirmation is that it largely eludes the ravens paradox." (§2.2); "The derivation of the paradox, as presented above, is thus blocked." (§2.2). A non-raven HD-confirms h "but only relative to k = ¬black(a)" (§2.2).
- **Deny Nicod's condition: Good's counterexample.** From Good 1967 as F&H paraphrase it: "Hence, Good has described a background corpus K relative to which [Ra · Ba] disconfirms [(∀x)(Rx ⊃ Bx)]." (p. 253). Crupi lists Good 1967 as "another famous counterexample to Nicod’s condition" (§2.2). F&H: "Hempel (1967) responded to Good by claiming that [(NC_s)] is not what he had in mind, since it smuggles too much “unkosher” (a posteriori) empirical knowledge into K." (p. 253). Of Maher: "More recently, Maher (2004) has convincingly argued (contrary to what he had previously argued in his (1999)) that, within a proper neo-Carnapian Bayesian framework, Hempel’s [(NC_⊤)] is false, and so is its Quinean “restriction” [(QNC_⊤)]." (F&H p. 254), adding: "While Maher’s neo-Carnapian analysis is very illuminating, it is by no means in the mainstream of contemporary Bayesian thought." (p. 254).
- **Accept (PC), soften it by degree — the Bayesian comparative/quantitative line.** F&H: "Perhaps somewhat surprisingly, almost all contemporary Bayesians implicitly assume that the paradoxical conclusion is true. And, they aim only to “soften the impact” of (PC) by trying to establish certain comparative and/or quantitative confirmational claims." (p. 255).
  Hosiasson-Lindenbaum (1940), as Hempel reports her: "it consists in the suggestion that the finding of one non-black object which is no raven, while constituting confirming evidence for the hypothesis, would increase the degree of confirmation of the hypothesis by a smaller amount than the finding of one raven which is black. This is said to be so because the class of all ravens is much less numerous than that of all non-black objects" (1945, p. 21, n. 2).
  Good: "(i) The observation of a white shoe does support H (provided that the number of non-black objects that might be observed is known to be large compared with the number of crows), and the result appears paradoxical because the support given to the hypothesis is negligible." (1960, p. 146).
  F&H list Mackie (1963) and many others among "the variety of Bayesian approaches" (n. 9); Mackie's paper ([doi](https://doi.org/10.1093/bjps/XIII.52.265)) was not read here.
  - *Case against:* Hempel's question to Hosiasson-Lindenbaum: "But is this last numerical assumption actually warranted in the present case and analogously in all other “ paradoxical” cases ?" (p. 21, n. 2). On the canonical assumptions (1)–(3), F&H: "Assumptions (2) and (3) are more controversial." (p. 256). Vranas, as F&H report: "Vranas then argues that Bayesians have given no good reason for assuming this (necessary and sufficient) condition." (p. 257; [doi](https://doi.org/10.1093/bjps/55.3.545)).
  - *F&H's own result:* "Theorem 1 and its Corollaries show that for a very wide range of probabilistic confirmation functions P, a black raven is more confirming of ‘All ravens are black’ than is a non-black non-raven." (p. 261). Crupi: "(A much broader analysis is provided by Fitelson and Hawthorne 2010, Hawthorne and Fitelson 2010 [Other Internet Resources]. Notably, their results include the full specification of the sufficient and necessary conditions for the main inequality C_P(h, e) > C_P(h, e*).)" (§3.6).

## Arguments in play

- **Hempel's sodium-salt case.** "Suppose that in support of the assertion “ All sodium salts burn yellow ” somebody were to adduce an experiment in which a piece of pure ice was held into a colourless flame and did not turn the flame yellow." (p. 19). His diagnosis: "the seemingly paradoxical cases of confirmation, we are often not actually judging the relation of the given evidence, E alone to the hypothesis H (we fail to observe the “ methodological fiction’, characteristic of every case of confirmation, that we have no relevant evidence for H other than that included in E) ; instead, we tacitly introduce a comparison of H with a body of evidence which consists of E in conjunction with an additional amount of information which we happen to have at our disposal" (p. 20). Conclusion: "the “ paradoxes of confirmation’, as formulated above, are due to a misguided intuition in the matter rather than to a logical flaw in the two stipulations from which the “ paradoxes” were derived." (pp. 20–21).
- **Goodman on the contrary hypothesis.** "And the prospects for indoor ornithology vanish when we notice that under these same conditions, the contrary hypothesis that no ravens are black is equally well confirmed." (1955, p. 71).
- **Two readings of the conclusion.** F&H separate (PC) from "(PC*) If one observes that an object a – already known to be a non-raven – is non-black (hence, is a non-black non-raven), then this observation confirms that all ravens are black." (p. 250), after Maher 1999 ([doi](https://doi.org/10.1086/392676)).
- **Good's exceptions.** "For example, suppose that all objects ever seen in the past were black. Then the observation of a white shoe would undermine the hypothesis H." (1960, p. 148); "For example, the observation of a white raven undermines H." (p. 146).
- **Sampling.** Crupi: "But of course, to have h confirmed, sampling ravens and finding a black one is intuitively more significant than failing to find a raven while sampling the enormous set of the non-black objects." (§3.6). With (i) "the size of the ravens population does not depend on their color" and (ii) the same for black non-ravens, a black raven confirms and a non-black non-raven does not: "(this observation is due to Mat Coakley)" (§3.6).

**Arithmetic check (this implant, 2026-09-27; mathematics, not a position).**
Good's 1967 corpus as F&H paraphrase it (p. 253): under H, 100 black ravens,
no non-black ravens, 1 million other birds; under not-H, 1,000 black ravens,
1 white raven, 1 million other birds; one bird drawn at random. F&H print
P[Ra·Ba | H·K] = 100/1000100 and P[Ra·Ba | ¬H·K] = 1000/1001000. Computed
with Python `fractions`: 100/1000100 = 1/10001 ≈ 0.0000999900;
1000/1001000 = 1/1001 ≈ 0.000999001; their ratio is 1001/10001 ≈ 0.10009,
below 1, so by Bayes' theorem a black raven lowers the probability of H in
that corpus. (Counting the one white raven, the not-H total is 1,001,001
birds; the ratio is then 1001001/10001000 ≈ 0.10009 — the same verdict.)
Whether such a corpus bears on (NC) is the Good–Hempel dispute above.

## Thinkers who addressed it

- **Jean Nicod** (1924) — the criterion, via Hempel (p. 10) and Crupi (§1).
- **Carl G. Hempel** — 1937 *Theoria* (difficulty "pointed out, in substance", 1945 p. 11 n. 2), 1943, 1945; reply to Good 1967.
- **Janina Hosiasson-Lindenbaum** (1940) — Hempel: "To my knowledge, hers has so far been the only publication which presents an explicit attempt to solve the problem" (1945, p. 21, n. 2).
- **Nelson Goodman** — Hempel: "The basic idea of sect. (b) in the above analysis of the ‘‘ paradoxes of confirmation ’’ is due to Dr. Nelson Goodman" (p. 21, n. 1); Goodman 1955, ch. III.
- **W. V. Quine** — "Natural Kinds" (1969/1970).
- **I. J. Good** — 1960, 1961, 1967, 1968; **J. L. Mackie** — 1963.
- **Patrick Maher** (1999, 2004); **Peter Vranas** (2004); **Branden Fitelson & James Hawthorne** (2010); **Mat Coakley** (via Crupi §3.6); **Samir Okasha** (2011, via Crupi §2.2).

## Framings and reframings

- **Paradox or not.** Hempel's section title puts the word in quotation
  marks — "5. The “Paradoxes” of Confirmation" per the scan's heading
  (p. 13) — and F&H report that Hempel and Goodman "didn’t view (PC) as paradoxical" (p. 248). Goodman calls it "the infamous paradox of the ravens" (1955, p. 70).
  Whether it is a [paradox](../vocabulary/paradox.md) in this implant's sense depends on the reading (structural note, [manifest](../../vision/manifest.md) G4).
- **Related puzzle, not this problem: grue.** Goodman's next section: "It is the predicate “grue” and it applies to all things examined before t just in case they are green but to other things just in case they are blue." (1955, p. 73); Crupi pairs it (as "blite") with the ravens under "Two paradoxes and other difficulties" (§1.2).
- **Background knowledge.** Hempel locates the impression in "an additional amount of information which we happen to have at our disposal" (1945, p. 20); Goodman in "tacit and illicit reference to evidence not stated in our example" (1955, p. 71); F&H's (PC*) concerns an object "already known to be a non-raven" (p. 250); Crupi's HD and Bayesian treatments state such knowledge as an auxiliary assumption k (§§2.2, 3.6). For the updating rule the Bayesian answers use see [Bayesian updating](../methods/bayesian-updating.md). See also [Simpson's paradox](simpsons-paradox.md).

## Vocabulary

- [Paradox](../vocabulary/paradox.md); [validity](../vocabulary/validity.md);
  [classical logic](../methods/classical-logic.md) (the contrapositive step).
- *Confirmation*, *instance*, *Nicod's criterion*, *equivalence condition*,
  *natural kind*, *likelihood ratio*, *background knowledge* — no pages yet
  in [vocabulary](../vocabulary/index.md).

Related problems: [Goodman's new riddle of induction](new-riddle-of-induction.md).
