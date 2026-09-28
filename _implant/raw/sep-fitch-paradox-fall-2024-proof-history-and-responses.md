# SEP "Fitch's Paradox of Knowability" (Brogaard & Salerno) — the proof, its history, and the responses the entry records

Source: Berit Brogaard and Joe Salerno, "Fitch's Paradox of Knowability",
  The Stanford Encyclopedia of Philosophy (Fall 2024 Edition), Edward N.
  Zalta & Uri Nodelman (eds.); first published Mon Oct 7, 2002;
  substantive revision Thu Aug 22, 2019 (copyright line: "Copyright © 2019
  by Berit Brogaard ... Joe Salerno"). Preamble, §§1, 2, 3.1–3.5, 4.1–4.4,
  5.1–5.3 (only the passages the page relies on).
Original: https://plato.stanford.edu/archives/fall2024/entries/fitch-paradox/
  (copyrighted; excerpts only)
Retrieved: 2026-09-27 (read at the archive URL above; HTML saved and
  converted to text; each quotation below checked against that text;
  authors and dates read from the page header and copyright line.
  Formulas are given in the entry's own LaTeX source, as served.)

## Preamble

> "Fitch’s paradox of knowability (aka the knowability paradox or Church-Fitch Paradox) concerns any theory committed to the thesis that all truths are knowable."  (preamble)

> "Historical examples of such theories arguably include Michael Dummett’s semantic antirealism (i.e., the view that any truth is verifiable), mathematical constructivism (i.e., the view that the truth of a mathematical formula depends on the mental constructions mathematicians use to prove those formulas), Hilary Putnam’s internal realism (i.e., the view that truth is what we would believe in ideal epistemic circumstances), Charles Sanders Peirce’s pragmatic theory of truth (i.e., that truth is what we would agree to at the limit of inquiry), logical positivism (i.e., the view that meaning is giving by verification conditions), Kant’s transcendental idealism (i.e., that all knowledge is knowledge of appearances), and George Berkeley’s idealism (i.e., that to be is to be perceivable)."  (preamble)

> "The middle way, what we might call moderate antirealism, can be characterized logically somewhere in the ballpark of the knowability principle:"  (preamble; followed by `\forall p(p \rightarrow \Diamond Kp)`)

> "It is the proof that shows (in a normal modal logic augmented with the knowledge operator) that “all truths are knowable” entails “all truths are known”:"  (preamble; followed by `\forall p(p \rightarrow \Diamond Kp) \vdash \forall p(p \rightarrow Kp)`)

> "As such the proof does the interesting work in collapsing moderate anti-realism into naive idealism."  (preamble)

> "What’s the paradox? Timothy Williamson (2000b) says the knowability paradox is not a paradox; it’s an “embarrassment”––an embarrassment to various brands of antirealism that have long overlooked a simple counterexample. He notes it’s “an affront” to various philosophical theories, but not to common sense. Others disagree."  (preamble)

> "The paradox, as articulated in Kvanvig (2006) and Brogaard and Salerno (2008), is that moderate antirealism appears not to be expressible as a distinct thesis, logically weaker than naive idealism."  (preamble)

## §1 Brief History

> "The literature on the knowability paradox emerges in response to a proof first published by Frederic Fitch in his 1963 paper, “A Logical Analysis of Some Value Concepts.” Theorem 5, as it was there called, threatens to collapse a number of modal and epistemic differences."  (§1)

> "For it shows that the existence of truths in fact unknown entails the existence of truths necessarily unknown."  (§1; followed by `\exists p(p \wedge \neg Kp) \vdash \exists p(p \wedge \neg \Diamond Kp)`)

> "It is however the contrapositive of Theorem 5 that is usually referred to as the paradox:"  (§1)

> "The earliest version of the proof was conveyed to Fitch by an anonymous referee in 1945. In 2005 we discovered that Alonzo Church was that referee (Salerno 2009b). His reports are published in their entirety in Church (2009). Fitch apparently did not take the result to be paradoxical. He published the proof in 1963 to avert a kind of “conditional fallacy” that threatened his informed-desire analysis of value."  (§1)

> "The analysis roughly says: \(x\) is valuable to \(s\) just in case there is a truth \(p\) such that were \(s\) to known \(p\) then she would desire \(x\)."  (§1; typo "to known" as in the source)

> "Rediscovered in Hart and McGinn (1976) and Hart (1979), the result was taken to be a refutation of verificationism, the view that all meaningful statements (and so all truths) are verifiable."  (§1)

> "Mackie (1980) and Routley (1981), among others at the time, point to difficulties with this general position but ultimately agree that Fitch’s result is a refutation of the claim that all truths are knowable, and that various forms of verificationism are imperiled for related reasons."  (§1)

> "Since the early eighties, however, there has been considerable effort to analyze the proof as paradoxical."  (§1)

> "Hence, the Church-Fitch proof has come to be known as the paradox of knowability."  (§1)

> "There is no consensus about whether and where the proof goes wrong."  (§1)

## §2 The Paradox of Knowability (the proof)

> "Let \(K\) be the epistemic operator ‘it is known by someone at some time that.’ Let \(\Diamond\) be the modal operator ‘it is possible that’."  (§2)

Steps as the entry gives them (LaTeX source, labels as in §2):

    (KP)   \forall p(p \rightarrow \Diamond Kp)
    (NonO) \exists p(p \wedge \neg Kp)
    (1)    p \wedge \neg Kp
    (2)    (p \wedge \neg Kp) \rightarrow \Diamond K(p \wedge \neg Kp)
    (3)    \Diamond K(p \wedge \neg Kp)
    (A)    K(p \wedge q) \vdash Kp \wedge Kq
    (B)    Kp \vdash p
    (C)    If \vdash p, then \vdash \Box p.
    (D)    \Box \neg p \vdash \neg \Diamond p
    (4)    K(p \wedge \neg Kp)            Assumption [for reductio]
    (5)    Kp \wedge K\neg Kp             from 4, by (A)
    (6)    Kp \wedge \neg Kp              from 5, applying (B) to the right conjunct
    (7)    \neg K(p \wedge \neg Kp)       from 4-6, by reductio, discharging assumption 4
    (8)    \Box \neg K(p \wedge \neg Kp)  from 7, by (C)
    (9)    \neg \Diamond K(p \wedge \neg Kp)  from 8, by (D)
    (10)   \neg \exists p(p \wedge \neg Kp)
    (11)   \forall p(p \rightarrow Kp)

> "Now consider the instance of KP substituting line 1 for the variable \(p\) in KP:"  (§2)

> "The independent result presupposes two very modest epistemic principles: first, knowing a conjunction entails knowing each of the conjuncts. Second, knowledge entails truth."  (§2)

> "Also presupposed are two modest modal principles: first, all theorems are necessary. Second, necessarily \(\neg p\) entails that \(p\) is impossible."  (§2)

> "Line 9 contradicts line 3. So a contradiction follows from KP and NonO. The advocate of the view that all truths are knowable must deny that we are non-omniscient:"  (§2)

> "The ally of the view that all truths are knowable (by somebody at some time) is forced absurdly to admit that every truth is known (by somebody at some time)."  (§2)

## §3 Logical revisions

> "Though some have argued that knowing a conjunction does not entail knowing the conjuncts (Nozick 1981), Williamson (1993) and Jago (2010) have shown that versions of the paradox do not require this distributive assumption."  (§3.1)

> "related paradoxes emerge replacing the factive operator “It is known that” with a non-factive operators, such as ‘It is rationally believed that’ (Mackie 1980: 92; Edgington 1985: 558–559; Tennant 1997: 252–259; Wright 2000: 357)."  (§3.1)

> "Williamson (1982) argues that Fitch’s proof is not a refutation of anti-realism, but rather a reason for the anti-realist to accept intuitionistic logic."  (§3.2)

> "Without double negation elimination one cannot derive Fitch’s conclusion ‘all truths are known’ (at line 11) from ‘there is not a truth that is unknown’ (line 10)."  (§3.2)

> "The intuitionist is however committed, by conditional introduction, to"  (§3.2; followed by `p \rightarrow \neg \neg Kp`)

> "Williamson responds that the intuitionist anti-realist may naturally express our non-omniscience as “not all truths are known”:"  (§3.3; followed by `(12) \neg \forall p(p \rightarrow Kp)`)

> "In effect, the anti-realist admits both that no truths are unknown and that not all truths are known. The satisfiability of this claim on intuitionistic grounds is demonstrated by Williamson (1988, 1992)."  (§3.3)

> "The above argument is given by Percival (1990: 185). Since it is intutionistically acceptable, it is meant to show that the intuitionist anti-realist is still in trouble."  (§3.4; the undecidedness argument from `\exists p(\neg Kp \wedge \neg K\neg p)`)

> "What about the reconstrual of our epistemic intuitions? Is it well motivated? According to Kvanvig (1995) it is not."  (§3.4)

> "But \(\neg Kp \rightarrow \neg p\) appears to be false for empirical discourse. Why should the fact that nobody ever knows \(p\) be sufficient for the falsity of \(p\)?"  (§3.4)

> "DeVidi and Solomon (2001) disagree. They argue that the intuitionistic consequences are not unacceptable to one interested in an epistemic theory of truth—indeed they are central to an epistemic theory of truth."  (§3.4)

> "For these reasons an appeal to intuitionist logic, by itself, is generally taken to be unsatisfying in dealing with the paradoxes of knowability. Exceptions include Burmüdez (2009), Dummett (2009), Rasmussen (2009) and Maffezioli, Naibo & Negri (2013)."  (§3.4; "Burmüdez" as in the source)

> "Another challenge to the logic of Fitch’s paradox is mentioned in Routley (1981) and defended by Beall (2000). The thought is that the correct logic of knowability is paraconsistent."  (§3.5)

> "Beall concludes that Fitch’s reasoning, without a proper reply to the knower, is ineffective against the knowability principle."  (§3.5)

> "If this is right then the inference from \(\Box \neg p\) to \(\neg \Diamond p\) has counterexamples and may not be employed to infer \(\neg \Diamond K(p \wedge \neg Kp)\) from \(\Box \neg K(p \wedge \neg Kp)\)."  (§3.5)

> "But compare with Wansing (2002), where a paraconsistent constructive relevant modal logic with strong negation is proposed to block the paradox."  (§3.5)

## §4 Semantic restrictions

> "The remainder of proposals are restriction strategies. They reinterpret KP by restricting its universal quantifier."  (§4)

> "Edgington (1985) offers a situation-theoretic diagnosis of Fitch’s paradox. She claims that the problem lies with the failure to distinguish between ‘knowing in a situation that \(p\)’ and ‘knowing that \(p\) is the case in a situation’."  (§4.1)

> "Edgington requires of knowability the less general thesis: if \(p\) is true in an actual situation \(s\) then there is a possible situation \(s^*\) in which it is known that \(p\) is true in \(s\). Call this E-knowability or EKP:"  (§4.1; followed by `\A p \rightarrow \Diamond K\A p`)

> "where A is the actuality operator which may be read ‘In some actual situation’, and \(\Diamond\) is the possibility operator to be read ‘In some possible situation’."  (§4.1)

> "EKP appears to be a very limited thesis failing to specify an epistemic constraint on contingent truth (Williamson 1987a)."  (§4.2)

> "Moreover, since there is no causal link between the actual world \(w_1\) and the relevant non-actual world \(w_2\), it is unclear how non-actual thought in \(w_2\) can be uniquely about \(w_1\) (Williamson, 1987a: 257–258)."  (§4.2)

> "Kvanvig (1995) accuses Fitch of a modal fallacy. The fallacy is an illicit substitution into a modal context."  (§4.3)

> "Kvanvig maintains that \(p \wedge \neg Kp\) is not rigid. So Fitch’s result is fallacious owing to an illicit substitution into a modal context. But we may reconstrue \(p \wedge \neg Kp\) as rigid. And when we do, the paradox evaporates."  (§4.3)

> "Kvanvig proposes that quantified expressions are non-rigid."  (§4.3)

> "Williamson (2000b) defends Fitch’s reasoning against Kvanvig’s charge."  (§4.4)

> "To think that this is sufficient for non-rigidity, Williamson complains, is to confuse non-rigidity for indexicality."  (§4.4)

> "Kvanvig (2006) replies and develops other interesting themes in the Knowability Paradox, which is the only monograph to date dedicated to the topic."  (§4.4)

## §5 Syntactic restrictions

> "Tennant (1997) focuses on the property of being Cartesian: A statement \(p\) is Cartesian if and only if \(Kp\) is not provably inconsistent. Accordingly, he restricts the principle of knowability to Cartesian statements."  (§5.1)

> "Dummett (2001) agrees that the knowability theorist’s error lies in providing a blanket, rather than a restricted, knowability principle. And he agrees that the restriction should be syntactic. Dummett restricts the principle of knowability to “basic” statements and characterizes truth inductively from there."  (§5.2)

> "For Dummett’s case, the problematic Fitch conjunction, \(p \wedge \neg Kp\), being compound, and so not basic, cannot replace the variable in \(p \rightarrow \Diamond Kp\)."  (§5.2)

> "The relative merits of these two restrictions are weighed by Tennant (2002). Tennant’s restriction is the less demanding of the two, since it bars only the substitution of those statements that are logically unknowable, and so, only those statements that are responsible for the paradoxes."  (§5.3)

> "From the first camp Hand and Kvanvig (1999) protest that TKP has not been restricted in a principled manner—in effect, that we have been given no good reason, other than the threat of paradox, to restrict the principle to Cartesian statements."  (§5.3)

> "By drawing analogies between his own restriction and others that are clearly admissible, he maintains that the Cartesian restriction is not ad-hoc."  (§5.3; Tennant 2001b)

> "Williamson (2000a) asks us to consider the following paradox."  (§5.3; the conjunction `p \wedge(Kp \rightarrow En)`)

> "Either way, Tennant argues, Williamson has not shown that TKP is an inadequate treatment of Fitch’s paradox."  (§5.3; Tennant 2001a)

> "The debate continues in Williamson (2009) and Tennant (2010)."  (§5.3)

> "Brogaard and Salerno (2002) develop other Fitch-like paradoxes against the restriction strategies."  (§5.3)

> "A response to Brogaard and Salerno appears in Rosenkranz (2004)."  (§5.3)

> "Dummett takes \(\forall p(p \rightarrow \neg \neg Kp)\) to be the best expression of his brand of anti-realism and embraces its intuitionistic consequences with open arms."  (§5.3)

> "Hand defends anti-realism by pointing to the distinction between a verification-type and its token performances, and argues that the existence of a verification-type doesn’t entail its performability."  (§5.3)

> "As for the knowability proof itself, there continues to be no consensus on whether and where it goes wrong."  (§5.3, closing)

> "Niche discussions of the paradox that don’t fit well into any of the above sections include Salerno’s (2018) new paradox of happiness; Kvanvig’s (2010) argument that the paradox threatens Christianity itself owing to its doctrine of the incarnation of Christ; and Cresto’s (2017) argument that the knowability paradox raises doubts about Reflection Principle as a requirement on rationality."  (§5.3)

## Additional passages (§§3.5, 4.2, 5.1, 5.3)

> "The independent evidence lies in the paradox of the knower (not to be mistaken with the paradox of knowability)."  (§3.5; whitespace normalised)

> "More recent developments of the paraconsistent approach appear in Beall (2009) and Priest (2009)."  (§3.5)

> "Related and additional criticisms of Edgington’s proposal appear in Wright (1987), Williamson (1987b; 2000b) and Percival (1991). Formal developments on the proposal, including points that address some of these concerns appear in Rabinowicz and Segerberg (1994), Lindström (1997), Rückert (2003), Edgington (2010), Fara (2010), Proietti and Sandu (2010), and Schlöder (forthcoming)."  (§4.2)

> "But \(p \wedge \neg Kp\) is not Cartesian, since \(K(p \wedge \neg Kp)\) is provably inconsistent (entailing the contradiction at line 6 of Fitch’s result)."  (§5.1)

> "Tennant (2001b) replies to Hand and Kvanvig with general discussion about the admissibility of restrictions in the practice of conceptual analysis and philosophical clarification."  (§5.3)

> "He also points out that TKP, rather than the unrestricted KP, serves as the more interesting point of contention between the semantic realist and anti-realist."  (§5.3; Tennant 2001b)

> "Fitch’s reasoning, at best, shows us that there is structural unknowability, that is, unknowability that is a function of logical considerations alone."  (§5.3; in the report of Tennant 2001b)

> "Other complaints that Tennant’s restriction strategy is not principled appear in DeVidi and Kenyon (2003) and Hand (2003). Hand offers a way of restricting knowability in a principled manner."  (§5.3)

> "and contends that it is Cartesian."  (§5.3; Williamson 2000a, of the conjunction `p \wedge(Kp \rightarrow En)`, with p "There is a fragment of Roman pottery at that spot" and n the number of books on his desk)

> "Unlike the undecidedness paradoxes of Wright (1987), Williamson (1988), and Percival (1990), the reasoning provided by Brogaard and Salerno does not violate Tennant’s Cartesian restriction."  (§5.3; Brogaard & Salerno's derivation uses the KK-principle `\Box(Kp \rightarrow KKp)`)

## Bibliography entries relied on (as the entry prints them)

- "Fitch, F., 1963. “A Logical Analysis of Some Value Concepts,” The Journal of Symbolic Logic, 28: 135–142; reprinted in Salerno (ed.) 2009, 21–28."
- "Hart, W. D. and McGinn, C., 1976. “Knowledge and Necessity,” Journal of Philosophical Logic, 5: 205–208."
- "Church, A., 2009. “Referee Reports on Fitch’s ‘A Definition of Value’,” in Salerno (ed.) 2009, 13–20."
- "–––, 2009b. “Knowability Noir: 1945–1963,” in Salerno (ed.) 2009, 29–48."

Relied on for: the whole map of fitchs-paradox-of-knowability.md — the
names of the paradox, the K principle and the proof steps, the history
(Church as referee, Fitch's value analysis, Hart & McGinn's
rediscovery, Mackie and Routley), and every response and objection
with its owner; the authors' own assessments ("very modest", "forced
absurdly", "generally taken to be unsatisfying", "less demanding") are
reported as theirs.
Context: the entry is organised as §3 logical revisions (epistemic,
intuitionistic, paraconsistent), §4 semantic restrictions (Edgington,
Kvanvig) and §5 syntactic restrictions (Tennant, Dummett) with the
counter-paradoxes of Williamson and Brogaard & Salerno. The authors are
themselves parties to the debate (Brogaard & Salerno 2002, 2006, 2008;
Salerno 2009b discovered the referee's identity).
