---
type: article
about: concept
title: "Fitch's paradox of knowability"
description: "If every truth is knowable, is every truth known? The Church–Fitch proof (Church's 1945 referee report, Fitch 1963 Theorem 5) derives 'all truths are known' from 'all truths are knowable' by principles the SEP authors call modest; taken after Hart & McGinn's (1976) rediscovery as a refutation of verificationism, it drew intuitionistic, paraconsistent, semantic and syntactic responses — Williamson, Beall, Edgington, Kvanvig, Tennant, Dummett — each with its owner."
tags: [problem, paradox, epistemology, logic, metaphysics]
timestamp: 2026-09-28T07:01:48Z
---

# Fitch's paradox of knowability

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
claim grades as in [How claims are graded](../../conventions/how-claims-are-graded.md).
Part of the [problems](./index.md) branch. Map: Berit Brogaard and Joe Salerno,
[SEP Fall 2024 "Fitch's Paradox of Knowability"](https://plato.stanford.edu/archives/fall2024/entries/fitch-paradox/)
(first published 2002-10-07, revised 2019-08-22; excerpt:
`raw/sep-fitch-paradox-fall-2024-proof-history-and-responses.md`). Fitch's
paper: [doi:10.2307/2271594](https://doi.org/10.2307/2271594) (excerpt:
`raw/fitch-1963-value-concepts-theorems-1-5-referee-note.md`). The SEP
authors are parties to the debate (Brogaard & Salerno 2002, 2006, 2008);
their assessments are marked as theirs.

## The question

If every truth can be known, does it follow that every truth is known?
The entry: the paradox "concerns any theory committed to the thesis that all truths are knowable" and is "aka the knowability paradox or Church-Fitch Paradox" (preamble).
The thesis is the **knowability principle** (KP), ∀p(p → ◇Kp), with *K*
read "it is known by someone at some time that" and ◇ "it is possible
that" (§2). The paradox "is the proof that shows (in a normal modal logic augmented with the knowledge operator) that “all truths are knowable” entails “all truths are known”" (preamble).

**Fitch's Theorem 5.** In Fitch's words: "THEOREM 5. If there is some true proposition which nobody knows (or has known or will know) to be true, then there is a true proposition which nobody can know to be true." (1963, p. 139).
Its proof is "Similar to proof of Theorem 4" (p. 139), which runs: "Suppose that p is true but not known by the agent. Then, since knowing is a truth class closed with respect to conjunction elimination, we conclude from Theorem 2 that there is some true proposition which cannot be known by the agent." (p. 139).
Brogaard & Salerno: "It is however the contrapositive of Theorem 5 that is usually referred to as the paradox:" (§1), namely ∀p(p → ◇Kp) ⊢ ∀p(p → Kp).

**The proof as the entry gives it (§2).** Transcribed from the entry's
formulas; rule labels quoted from §2.

| Line | Formula | Justification (§2) |
|---|---|---|
| KP | ∀p(p → ◇Kp) | knowability principle |
| NonO | ∃p(p ∧ ¬Kp) | there is an unknown truth |
| 1 | p ∧ ¬Kp | instance of NonO |
| 2 | (p ∧ ¬Kp) → ◇K(p ∧ ¬Kp) | instance of KP, "substituting line 1 for the variable" |
| 3 | ◇K(p ∧ ¬Kp) | from 1, 2 |
| 4 | K(p ∧ ¬Kp) | "Assumption [for reductio]" |
| 5 | Kp ∧ K¬Kp | "from 4, by (A)" |
| 6 | Kp ∧ ¬Kp | "from 5, applying (B) to the right conjunct" |
| 7 | ¬K(p ∧ ¬Kp) | "from 4-6, by reductio" |
| 8 | □¬K(p ∧ ¬Kp) | "from 7, by (C)" |
| 9 | ¬◇K(p ∧ ¬Kp) | "from 8, by (D)" |
| 10 | ¬∃p(p ∧ ¬Kp) | 3 and 9 conflict, so NonO is denied |
| 11 | ∀p(p → Kp) | from 10 |

(A) K(p ∧ q) ⊢ Kp ∧ Kq; (B) Kp ⊢ p; (C) if ⊢ p then ⊢ □p; (D) □¬p ⊢ ¬◇p.
The entry calls (A) and (B) "two very modest epistemic principles" and (C) and (D) "two modest modal principles" (§2) — the authors' description.

**Logic check (this implant, 2026-09-27; logic, not a position).** The
proof is in quantified modal epistemic logic; `logic.py` checks only
propositional validity and does not cover ◇, □, *K* or the quantifiers.
Treating each modal or epistemic formula as an unanalysed atom, the
propositional skeleton checks out: with a = K(p ∧ ¬Kp), kp = Kp,
kk = K¬Kp, the premises a → (kp ∧ kk) (rule A) and kk → ¬kp (rule B)
give ¬a — `VALID` (lines 4–7); p ∧ ¬kp, (p ∧ ¬kp) → d and ¬d, with
d = ◇K(p ∧ ¬Kp), are reported "premises are jointly inconsistent"
(lines 1–3 against 9); ¬(p ∧ ¬kp) ⊢ p → kp is `VALID` classically
(the step from 10 to 11, instance-wise). Rules (C) and (D), and the
quantifier steps, are outside what the tool checks.

## Why it matters

- **A threat to anti-realist theories of truth.** The entry lists as "Historical examples" of theories committed to knowability, "arguably", Dummett's semantic antirealism, mathematical constructivism, Putnam's internal realism, Peirce's pragmatic theory of truth, logical positivism, Kant's transcendental idealism and Berkeley's idealism (preamble).
- **Refutation of verificationism, as first read.** "Rediscovered in Hart and McGinn (1976) and Hart (1979), the result was taken to be a refutation of verificationism, the view that all meaningful statements (and so all truths) are verifiable." (§1; [Hart & McGinn 1976](https://doi.org/10.1007/BF00248729)). "Mackie (1980) and Routley (1981), among others at the time, point to difficulties with this general position but ultimately agree that Fitch’s result is a refutation of the claim that all truths are knowable, and that various forms of verificationism are imperiled for related reasons." (§1; [Mackie 1980](https://doi.org/10.1093/analys/40.2.90)).
- **Why "paradox".** "Since the early eighties, however, there has been considerable effort to analyze the proof as paradoxical." (§1). Brogaard & Salerno: "As such the proof does the interesting work in collapsing moderate anti-realism into naive idealism." (preamble). "The paradox, as articulated in Kvanvig (2006) and Brogaard and Salerno (2008), is that moderate antirealism appears not to be expressible as a distinct thesis, logically weaker than naive idealism." (preamble).
- **Not a paradox?** "Timothy Williamson (2000b) says the knowability paradox is not a paradox; it’s an “embarrassment”––an embarrassment to various brands of antirealism that have long overlooked a simple counterexample." (preamble). "Others disagree." (ibid.).
- **State of the debate, as the entry reports it.** "There is no consensus about whether and where the proof goes wrong." (§1); "there continues to be no consensus on whether and where it goes wrong" (§5.3).
- **Further applications.** The entry records Salerno's (2018) "new paradox of happiness", Kvanvig's (2010) "argument that the paradox threatens Christianity itself owing to its doctrine of the incarnation of Christ", and Cresto's (2017) argument on the Reflection Principle (§5.3).

## Positions taken

In the entry's own grouping: logical revisions (§3), semantic restrictions
(§4), syntactic restrictions (§5), plus acceptance of the result (§1). No
position is ranked here. No survey figure is recorded.

- **Accept the result: KP is false.** After Hart & McGinn (1976) and Hart (1979) rediscovered the proof, it "was taken to be a refutation of verificationism"; Mackie (1980) and Routley (1981) "ultimately agree that Fitch’s result is a refutation of the claim that all truths are knowable" (§1; full quotations under *Why it matters*).
- **Drop a premise of the epistemic reasoning.** Nozick (1981) is reported as arguing that "knowing a conjunction does not entail knowing the conjuncts"; *Against:* "Williamson (1993) and Jago (2010) have shown that versions of the paradox do not require this distributive assumption" (§3.1 — the SEP authors' wording). On factivity: "related paradoxes emerge replacing the factive operator “It is known that” with a non-factive operators, such as ‘It is rationally believed that’ (Mackie 1980: 92; Edgington 1985: 558–559; Tennant 1997: 252–259; Wright 2000: 357)." (§3.1). Church's 1945 report, per the OUP abstract, "offers a number of potentially promising ways to block the proof. He is most sympathetic to a rejection of closure principles for knowledge and belief, and a fortiori the principle that knowledge is closed under conjunction-elimination." (excerpt: `raw/church-2009-salerno-2009-knowability-noir-referee-reports.md`).
- **Intuitionistic revision (Williamson 1982).** "Williamson (1982) argues that Fitch’s proof is not a refutation of anti-realism, but rather a reason for the anti-realist to accept intuitionistic logic." (§3.2; [doi:10.1093/analys/42.4.203](https://doi.org/10.1093/analys/42.4.203)). "Without double negation elimination one cannot derive Fitch’s conclusion ‘all truths are known’ (at line 11) from ‘there is not a truth that is unknown’ (line 10)." (§3.2). The intuitionist is committed instead to p → ¬¬Kp (§3.2). Non-omniscience is re-expressed as ¬∀p(p → Kp): "Williamson responds that the intuitionist anti-realist may naturally express our non-omniscience as “not all truths are known”:" (§3.3), and "The satisfiability of this claim on intuitionistic grounds is demonstrated by Williamson (1988, 1992)." (§3.3).
  - *Against:* Percival's undecidedness argument (1990: 185; [doi:10.1093/analys/50.3.182](https://doi.org/10.1093/analys/50.3.182)) "is meant to show that the intuitionist anti-realist is still in trouble" (§3.4); "What about the reconstrual of our epistemic intuitions? Is it well motivated? According to Kvanvig (1995) it is not." (§3.4). The SEP authors: "But \(\neg Kp \rightarrow \neg p\) appears to be false for empirical discourse." — i.e. ¬Kp → ¬p (§3.4).
  - *For:* "DeVidi and Solomon (2001) disagree. They argue that the intuitionistic consequences are not unacceptable to one interested in an epistemic theory of truth—indeed they are central to an epistemic theory of truth." (§3.4).
  - *Standing, as the SEP authors report it:* "For these reasons an appeal to intuitionist logic, by itself, is generally taken to be unsatisfying in dealing with the paradoxes of knowability. Exceptions include Burmüdez (2009), Dummett (2009), Rasmussen (2009) and Maffezioli, Naibo & Negri (2013)." (§3.4).
- **Paraconsistent revision (Routley 1981, Beall 2000).** "Another challenge to the logic of Fitch’s paradox is mentioned in Routley (1981) and defended by Beall (2000). The thought is that the correct logic of knowability is paraconsistent." (§3.5; [Beall 2000](https://doi.org/10.1080/00048400012349521)). The evidence is the knower: "The independent evidence lies in the paradox of the knower (not to be mistaken with the paradox of knowability)." (§3.5), and "Beall concludes that Fitch’s reasoning, without a proper reply to the knower, is ineffective against the knowability principle." (§3.5). The SEP authors locate the pressure point at rule (D): on this view "the inference from \(\Box \neg p\) to \(\neg \Diamond p\) has counterexamples" — □¬p to ¬◇p (§3.5). Also Wansing (2002), "a paraconsistent constructive relevant modal logic with strong negation" (§3.5), and "More recent developments of the paraconsistent approach appear in Beall (2009) and Priest (2009)." (§3.5).
- **Semantic restriction: actuality (Edgington 1985).** "Edgington (1985) offers a situation-theoretic diagnosis of Fitch’s paradox. She claims that the problem lies with the failure to distinguish between ‘knowing in a situation that \(p\)’ and ‘knowing that \(p\) is the case in a situation’." (§4.1; [doi:10.1093/mind/xciv.376.557](https://doi.org/10.1093/mind/xciv.376.557)). Her principle EKP is A*p* → ◇KA*p*, "where A is the actuality operator which may be read ‘In some actual situation’" (§4.1).
  - *Against:* "EKP appears to be a very limited thesis failing to specify an epistemic constraint on contingent truth (Williamson 1987a)." (§4.2; [doi:10.1093/mind/xcvi.382.256](https://doi.org/10.1093/mind/xcvi.382.256)); "it is unclear how non-actual thought in \(w_2\) can be uniquely about \(w_1\) (Williamson, 1987a: 257–258)" (§4.2). "Related and additional criticisms of Edgington’s proposal appear in Wright (1987), Williamson (1987b; 2000b) and Percival (1991)." (§4.2); among "Formal developments on the proposal, including points that address some of these concerns" the entry lists Edgington (2010) (§4.2).
- **Semantic restriction: rigidity (Kvanvig 1995, 2006).** "Kvanvig (1995) accuses Fitch of a modal fallacy. The fallacy is an illicit substitution into a modal context." (§4.3; [doi:10.2307/2216283](https://doi.org/10.2307/2216283)). "Kvanvig maintains that \(p \wedge \neg Kp\) is not rigid. So Fitch’s result is fallacious owing to an illicit substitution into a modal context. But we may reconstrue \(p \wedge \neg Kp\) as rigid. And when we do, the paradox evaporates." (§4.3).
  - *Against:* "Williamson (2000b) defends Fitch’s reasoning against Kvanvig’s charge." (§4.4); "To think that this is sufficient for non-rigidity, Williamson complains, is to confuse non-rigidity for indexicality." (§4.4). Kvanvig's [2006](https://doi.org/10.1093/0199282595.001.0001) book replies; the SEP authors call it "the only monograph to date dedicated to the topic" (§4.4).
- **Syntactic restriction: Cartesian statements (Tennant 1997).** "Tennant (1997) focuses on the property of being Cartesian: A statement \(p\) is Cartesian if and only if \(Kp\) is not provably inconsistent. Accordingly, he restricts the principle of knowability to Cartesian statements." (§5.1; the restricted principle is called TKP; [book](https://doi.org/10.1093/acprof:oso/9780199251605.001.0001)). "But \(p \wedge \neg Kp\) is not Cartesian, since \(K(p \wedge \neg Kp)\) is provably inconsistent (entailing the contradiction at line 6 of Fitch’s result)." (§5.1) — p ∧ ¬Kp and K(p ∧ ¬Kp).
  - *Against:* "Hand and Kvanvig (1999) protest that TKP has not been restricted in a principled manner" (§5.3; [doi](https://doi.org/10.1080/00048409912349191)); Williamson (2000a; [doi](https://doi.org/10.1111/1467-9329.00113)) builds the conjunction p ∧ (Kp → En) "and contends that it is Cartesian" (§5.3); "Other complaints that Tennant’s restriction strategy is not principled appear in DeVidi and Kenyon (2003) and Hand (2003)." (§5.3); Brogaard & Salerno (2002; [doi](https://doi.org/10.1093/analys/62.2.143)) "develop other Fitch-like paradoxes against the restriction strategies" (§5.3), using the KK-principle; "Unlike the undecidedness paradoxes of Wright (1987), Williamson (1988), and Percival (1990), the reasoning provided by Brogaard and Salerno does not violate Tennant’s Cartesian restriction." (§5.3).
  - *For:* Tennant (2001b) "maintains that the Cartesian restriction is not ad-hoc" (§5.3); against Williamson, "Tennant argues, Williamson has not shown that TKP is an inadequate treatment of Fitch’s paradox" (§5.3; [2001a](https://doi.org/10.1111/1467-9329.00162)); "The debate continues in Williamson (2009) and Tennant (2010)." (§5.3); "A response to Brogaard and Salerno appears in Rosenkranz (2004)." (§5.3).
- **Syntactic restriction: basic statements (Dummett 2001).** "Dummett (2001) agrees that the knowability theorist’s error lies in providing a blanket, rather than a restricted, knowability principle. And he agrees that the restriction should be syntactic. Dummett restricts the principle of knowability to “basic” statements and characterizes truth inductively from there." (§5.2; [doi:10.1093/analys/61.1.1](https://doi.org/10.1093/analys/61.1.1)). Tennant (2002; [doi](https://doi.org/10.1093/analys/62.2.135)) weighs the two; the SEP authors: "Tennant’s restriction is the less demanding of the two" (§5.3). Later, "Dummett takes \(\forall p(p \rightarrow \neg \neg Kp)\) to be the best expression of his brand of anti-realism and embraces its intuitionistic consequences with open arms." (§5.3) — ∀p(p → ¬¬Kp).
- **Other reformulations of anti-realism.** The entry lists proposals by Chalmers (2012), Dummett (2009), Edgington (2010), Fara (2010), Hand (2009, 2010), Jenkins (2005), Kelp & Pritchard (2009), Linsky (2009), Hudson (2009), Restall (2009), Tennant (2009), Alexander (2013), Dean & Kurokawa (2010), Proietti (2016) (§5.3). Hand, for one, "argues that the existence of a verification-type doesn’t entail its performability" (§5.3).

## Arguments in play

(none recorded as separate argument pages yet). The Church–Fitch proof is
laid out under *The question*; the undecidedness argument (Percival 1990),
the knower (Beall 2000), Williamson's p ∧ (Kp → En) and Brogaard &
Salerno's KK-based derivation are reported in SEP §§3.4, 3.5 and 5.3.

## Thinkers who addressed it

- **Alonzo Church** (1945) — anonymous referee; first version of the proof. "The earliest version of the proof was conveyed to Fitch by an anonymous referee in 1945. In 2005 we discovered that Alonzo Church was that referee (Salerno 2009b). His reports are published in their entirety in Church (2009)." (§1). Salerno's archive catalogue lists the first report as "Handwritten by Alonzo Church to Ernest Nagel, coeditor of JSL" and a Nagel letter of 13 April 1945 that "Notes that Fitch has withdrawn his paper owing to a defect in his definition of value." (excerpt: `raw/church-2009-salerno-2009-knowability-noir-referee-reports.md`).
- **Frederic B. Fitch** (1963) — Theorem 5, crediting the referee for Theorem 4: "This theorem is essentially due to an anonymous referee of an earlier paper, in 1945, that I did not publish." (p. 138, n. 5). The paper grew from "a retiring presidential address to the Association for Symbolic Logic" of 1961 (p. 135, n. 1). "Fitch apparently did not take the result to be paradoxical. He published the proof in 1963 to avert a kind of “conditional fallacy” that threatened his informed-desire analysis of value." (Brogaard & Salerno §1).
- **W. D. Hart & Colin McGinn** (1976), **Hart** (1979), **J. L. Mackie** (1980), **R. Routley** (1981) — rediscovery (Hart & McGinn, Hart); acceptance of the result as a refutation of KP (Mackie, Routley) (§1).
- **[Timothy Williamson](../thinkers/williamson.md)** (1982, 1987a, 1988, 1992, 1993, 2000a, 2000b, 2009) — intuitionistic response; critic of Edgington, Kvanvig and Tennant.
- **Dorothy Edgington** (1985, 2010) — actuality operator.
- **C. Wright** (1987), **P. Percival** (1990, 1991) — undecidedness paradoxes (§§3.4, 5.3); criticisms of Edgington (§4.2).
- **Jonathan Kvanvig** (1995, 2006, 2010) — rigidity; with **Michael Hand** (1999), the restriction critique; Hand (2003, 2009, 2010) — principled restriction, verification-types (§5.3).
- **Neil Tennant** (1997, 2001a, 2001b, 2002, 2009, 2010) — Cartesian restriction.
- **J. C. Beall** (2000, 2009), **G. Priest** (2009), **H. Wansing** (2002) — paraconsistent approaches.
- **Michael Dummett** (2001, 2009) — basic statements; ∀p(p → ¬¬Kp).
- **Berit Brogaard & Joe Salerno** (2002, 2006, 2008; Salerno 2009b) — counter-paradoxes; the archival history; the SEP entry.

## Framings and reframings

- **Not a paradox but a lesson about value analyses (Fitch's context).**
  Salerno, per the OUP abstract of "Knowability Noir": "If this is right, then Fitch does not take the knowability proofs to be paradoxical, but instead takes them to be a lesson about how intensional operators interact, surprisingly, to thwart the efforts of conditional analyses." Fitch's definition of value is glossed by him as: "This means that a situation p is a value for an agent if (and only if) there is an actual situation q and situation r such that if the agent knows q then he will strive for the conjunction of p and r." (1963, p. 141).
- **An embarrassment, not a paradox** (Williamson 2000b) versus a collapse, in Brogaard & Salerno's words, "collapsing moderate anti-realism into naive idealism" (preamble; with Kvanvig 2006 and Brogaard & Salerno 2008) — both quoted under *Why it matters*.
- **Structural versus substantial unknowability.** Tennant (2001b), as the SEP authors report him: "He also points out that TKP, rather than the unrestricted KP, serves as the more interesting point of contention between the semantic realist and anti-realist." In the same report: "Fitch’s reasoning, at best, shows us that there is structural unknowability, that is, unknowability that is a function of logical considerations alone." (§5.3).
- **Name.** The entry records "Church-Fitch Paradox" and "the Church-Fitch proof has come to be known as the paradox of knowability" (§1). Edgington's 1985 paper already bears the title "The Paradox of Knowability" ([doi](https://doi.org/10.1093/mind/xciv.376.557)).
- **Related paradox pages:** [the surprise examination
  paradox](surprise-examination-paradox.md) (whose page reports the
  Kaplan–Montague knower), [the liar paradox](liar-paradox.md), [the lottery and
  preface paradoxes](lottery-and-preface-paradoxes.md),
  [Moore's paradox](moores-paradox.md), [Meno's paradox](menos-paradox.md).

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — whether this is one in the
  normative sense is itself disputed (Williamson 2000b, above).
- [Knowledge](../vocabulary/knowledge.md) — *K* here is "known by someone
  at some time"; the epistemic principles the proof uses are (A) and (B)
  (§2).
- [Validity](../vocabulary/validity.md); [classical
  logic](../methods/classical-logic.md) — the intuitionistic response turns
  on double negation elimination.
- *Knowability principle*, *anti-realism*, *verificationism*, *factivity*,
  *necessitation*, *rigid designation*, *actuality operator*, *Cartesian
  statement*, *KK principle* — open work in [vocabulary](../vocabulary/index.md).
