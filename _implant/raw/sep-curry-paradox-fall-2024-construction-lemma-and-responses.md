# SEP "Curry's Paradox" (Shapiro & Beall) — the informal argument, the Curry-Paradox Lemma, the response families and why negation-free matters

## A. Main entry

Source: Lionel Shapiro & Jc Beall, "Curry's Paradox", The Stanford
  Encyclopedia of Philosophy (Fall 2024 Edition), Edward N. Zalta & Uri
  Nodelman (eds.); first published 2017-09-06, substantive revision
  2018-01-19. Preamble and §§1.1, 1.2, 2, 2.2, 3.1, 3.2, 4, 4.1, 4.2,
  4.2.1, 4.2.2, 4.2.3, 5.1, 5.1.1, 5.1.2, 5.2, 6, 6.3.
Original: https://plato.stanford.edu/archives/fall2024/entries/curry-paradox/
  (copyrighted; excerpts only)
Retrieved: 2026-09-27 (read at the URL above; HTML fetched with curl and
  compared byte-for-byte with the saved extraction; authors read from the
  entry's copyright block)

> "“Curry’s paradox”, as the term is used by philosophers today, refers to a wide variety of paradoxes of self-reference or circularity that trace their modern ancestry to Curry (1942b) and Löb (1955)."  (preamble)

> "Curry’s paradox differs from both Russell’s paradox and the Liar paradox in that it doesn’t essentially involve the notion of negation. Common truth-theoretic versions involve a sentence that says of itself that if it is true then an arbitrarily chosen claim is true, or—to use a more sinister instance—says of itself that if it is true then every falsity is true."  (preamble)

> "Suppose that your friend tells you: “If what I’m saying using this very sentence is true, then time is infinite”."  (§1.1)

> "Under the supposition that \(k\) is true, we have thus derived a conditional together with its antecedent. Using modus ponens within the scope of the supposition, we now derive the conditional’s consequent under that same supposition"  (§1.1, before step 3)

> "The rule of conditional proof now entitles us to affirm a conditional with our supposition as antecedent"  (§1.1, before step 4)

> "We seem to have established that time is infinite using no assumptions beyond the existence of the self-referential sentence \(k\), along with the seemingly obvious principles about truth that took us to (1) and also from (4) to (5)."  (§1.1)

> "Finally, putting (4) and (5) together by modus ponens, we get (6) Time is infinite."  (§1.1, steps 4–6)

> "But starting with Curry’s initial presentation in Curry 1942b (see the supplementary document on Curry on Curry’s Paradox), discussion of Curry’s paradox has usually had a different focus. It has concerned various formal systems —most often set theories or theories of truth. In this setting what poses the paradox is a proof that the system has a particular feature. Typically, the feature at issue is triviality."  (§1.2)

> "A theory is said to be trivial, or absolutely inconsistent, when it affirms every claim that is expressible in the language of the theory."  (§1.2)

> "Informally, a Curry sentence is a sentence that is equivalent, by the lights of some theory, to a conditional with itself as antecedent."  (§1.2)

> "Troubling Corollary Every Curry-complete theory is trivial."  (§1.2)

> "As it is standardly presented today, Curry’s paradox afflicts “naive” truth theories (those featuring a “transparent” truth predicate) and “naive” set theories (those featuring unrestricted set abstraction)."  (§2)

> "Geach (1955) and Löb (1955) were the first to show, Curry sentences can be obtained using semantic principles alone, without any reliance on property abstraction."  (§2.2)

> "The referee, now known to have been Leon Henkin (Halbach & Visser 2014: 257), suggested that the method Löb used in his proof “leads to a new derivation of paradoxes in natural language”"  (§2.2)

> "To start, here is a very general limitative result, a close variant of the Lemma in Curry 1942b."  (§3.1; the Lemma assumes a Curry sentence, Id, MP and Cont — in the entry's notation, Cont: if α ⊢ α → β then ⊢ α → β — and concludes ⊢ π)

> "Here MP is a version of modus ponens, and Cont is a principle of contraction: two occurrences of the sentence \(\alpha\) are “contracted” into one."  (§3.1)

> "The Curry-Paradox Lemma entails that any Curry-complete theory must violate one or more of Id, MP or Cont on pain of triviality."  (§3.1)

> "Probably the most common version replaces the rules Id and Cont with corresponding laws"  (§3.2; ContL: ⊢ (α → (α → β)) → (α → β))

> "Curry-incompleteness responses accept the Troubling Corollary. However, they deny that the target theories of properties, sets or truth are Curry-complete. Curry-incompleteness responses can, and usually do, embrace classical logic."  (§4)

> "Curry-completeness responses reject the Troubling Corollary; they insist that there can be nontrivial Curry-complete theories. Any such theory must violate one or more of the logical principles assumed in the Curry-Paradox Lemma. Since classical logic validates those principles, these responses invoke a non-classical logic."  (§4)

> "There is also the option of advocating a Curry-incompleteness response to Curry paradoxes arising in one domain, say set theory, while advocating a Curry-completeness response to Curry paradoxes arising in another domain, say property theory (e.g., Field 2008; Beall 2009)."  (§4)

> "Examples of prominent theories of truth that supply Curry-incompleteness responses to Curry’s paradox include Tarski’s hierarchical theory, the revision theory of truth (Gupta & Belnap 1993) and the contextualist approaches (Burge 1979, Simmons 1993, and Glanzberg 2001, 2004). These theories all restrict the “naive” transparency principle (Truth)."  (§4.1)

> "In the context of set theory Curry-incompleteness responses include Russellian type theories and various theories that restrict the “naive” set abstraction principle (Set)."  (§4.1)

> "Since the rule Id has generally been left unquestioned (but see French 2016 and Nicolai & Rossi forthcoming), this has meant denying that the conditional \({\rightarrow}\) of a nontrivial Curry-complete theory satisfies both MP and Cont."  (§4.2)

> "The most common strategy has been to accept that such a theory’s conditional obeys MP, but deny that it obeys Cont. Since Cont is a contraction principle, such responses can be called contraction-free. This strategy was first proposed by Moh (1954), who is cited approvingly by Geach (1955) and Prior (1955)."  (§4.2, (I))

> "A second and much more recent strategy is to accept that such a theory’s conditional obeys Cont, but deny that it obeys MP (sometimes called the rule of “detachment”). Such responses can be called detachment-free. This strategy is advocated, in different ways, by Ripley (2013) and Beall (2015)."  (§4.2, (II))

> "A strongly contraction-free response denies that \({\rightarrow}\) obeys MP′ (e.g., Mares & Paoli 2014; Slaney 1990; Weir 2015; Zardini 2011)."  (§4.2.1, (Ia))

> "A weakly contraction-free response accepts that \({\rightarrow}\) obeys MP′, but denies that it obeys CP (e.g., Field 2008; Beall 2009; Nolan 2016)."  (§4.2.1, (Ib))

> "They typically present their own form of that rule in a “substructural” framework, specifically one that lets us distinguish between what follows from a premise taken once and what follows from the same premise taken twice."  (§4.2.1)

> "the failure of CP has sometimes been motivated using “worlds” semantics of the sort that involve a distinction between logically possible and impossible worlds (e.g., Beall 2009; Nolan 2016)."  (§4.2.1)

> "A strongly detachment-free response denies that \({\rightarrow}\) obeys CCP (Goodship 1996; Beall 2015)."  (§4.2.2, (IIa))

> "A weakly detachment-free response accepts that \({\rightarrow}\) obeys CCP, but rejects Trans (Ripley 2013)."  (§4.2.2, (IIb))

> "One strategy for replying to the charge that detachment-free responses are counterintuitive has been to appeal to a connection between consequence and our acceptance and rejection of sentences."  (§4.2.2)

> "A strongly contraction-free response corresponds to blocking step (3) of that argument, since it rejects MP′. A weakly contraction-free response instead blocks step (4), since it rejects CP."  (§4.2.3)

> "However, both kinds of detachment-free response find fault with the final move by MP to (6)."  (§4.2.3)

> "Starting with Church (1942), Moh (1954), Geach (1955), Löb (1955) and Prior (1955), discussion of Curry’s paradox has emphasized that it differs from Russell’s paradox, and the Liar paradox, in that it doesn’t “involv[e] negation essentially” (Anderson 1975: 128)."  (§5.1)

> "The problem, he says, is that Curry’s paradox “cannot be resolved merely by adopting a system that contains a queer sort of negation”. Rather, “if we want to retain the naive view of truth, or the naive view of classes …, then we must modify the elementary rules of inference relating to ‘if’” (1955: 72)."  (§5.1, reporting Geach 1955)

> "They conclude that Curry’s paradox frustrates those who had “hoped that weakening classical negation principles” would resolve Russell’s paradox."  (§5.1, reporting Meyer, Routley & Dunn 1979: 127)

> "Yet a number of prominent paraconsistent logics can’t serve as the basis for Curry-complete theories on pain of triviality. Such logics are sometimes said to fail to be “Curry paraconsistent” (Slaney 1989)."  (§5.1.1)

> "Hence, as long as there is a \(\kappa\) that is intersubstitutable with \(\kappa \Rightarrow \pi\) according to \(\mathcal{T}\), then \(\vdash _{\mathcal{T}} \pi\). Consequently Ł\(_{3}\) won’t underwrite a response to Curry’s paradox."  (§5.1.2; the Ł3 point "was first noted by Moh (1954)")

> "As a result, the need to evade Curry’s paradox has played a significant role in the development of non-classical logics (e.g., Priest 2006; Field 2008)."  (§5.1.2)

> "We can … say not only that Curry’s paradox does not involve negation but that even Russell’s paradox presupposes only those properties of negation which it shares with implication."  (§5.2, quoting Prior 1955: 180)

> "Definition 3 (Curry connective) Let \(\pi\) be a sentence in the language of theory \(\mathcal{T}\). The unary connective \(\odot\) is a Curry connective for \(\pi\) and \(\mathcal{T}\) provided it satisfies two principles"  (§5.2)

> "Definition 4 (Generalized Curry paradox) We have a generalized Curry paradox in any case where the assumptions stated in the Generalized Curry-Paradox Lemma appear to hold."  (§5.2)

> "If that is right, the desideratum that generalized Curry paradoxes be resolved uniformly needn’t discriminate between the various logically revisionary solutions that have been pursued."  (§5.2)

> "According to this principle, paradoxes that belong to the “same kind” should receive the “same kind of solution”."  (§5.2, on Priest 1994's "principle of uniform solution")

> "On this approach, ECQ and Cont fail, while Red and MP hold (Priest 1994, 2006)."  (§5.2)

> "On this approach, Red and Cont fail, while ECQ and MP hold (Field 2008; Zardini 2011)."  (§5.2)

> "On this approach, ECQ and MP fail, while Red and Cont hold (Beall 2015; Ripley 2013)."  (§5.2)

> "This would be the case despite the fact that Priest evaluates Liar sentences as both true and false, whereas he rejects the claim that Curry sentences are true."  (§5.2)

> "The last decade (as of the date of this version of this entry) has witnessed a boom in attention to Curry paradoxes, and perhaps especially to what have been called validity Curry or v-Curry paradoxes (Whittle 2004; Shapiro 2011; Beall & Murzi 2013)."  (§6)

> "But this is a rule that has seemed difficult to resist for a consequence connective (Shapiro 2011; Weber 2014; Zardini 2013)."  (§6.1, on CP)

> "Still, what seems inescapable is the converse of CP, the rule CCP that is the other direction of the single-premise deduction theorem."  (§6.1)

> "For this reason, v-Curry paradoxes have sometimes been taken to motivate substructural consequence relations (e.g., Barrio et al. forthcoming; Beall & Murzi 2013; Ripley 2015a; Shapiro 2011, 2015)."  (§6.3)

Relied on for: the definition of a Curry sentence and of triviality; the
informal argument (MP, conditional proof, naive truth); the Lemma (Id, MP,
Cont); the two response classes and four subfamilies with their named
proponents; the negation-free point (Geach 1955, Meyer–Routley–Dunn 1979,
Prior 1955); uniform solution (Priest 1994); v-Curry.
Context: The entry's running example is "time is infinite" and "all
numbers are prime", not the popular "Santa Claus exists"; the entry frames
the paradox mainly as a constraint on formal theories (§1.2) and says it
will "focus on Curry-completeness responses" (§4.1). Formulae are kept in
the entry's LaTeX notation.

## B. Supplement "Curry on Curry's Paradox"

Source: same entry, supplementary document "Curry on Curry's Paradox".
Original: https://plato.stanford.edu/archives/fall2024/entries/curry-paradox/supplement.html
  (copyrighted; excerpts only)
Retrieved: 2026-09-27 (read at the URL above with curl)

> "When Curry (1942b) introduced the paradox to demonstrate the inconsistency of “certain systems of formal logic”, the systems he had in mind were theories of functional application, specifically Church’s untyped lambda calculus and Curry’s own combinatory logic"  (Curry's Target Systems)

> "Curry regarded his paradox as a constraint on an adequate theory of functional application."  (Curry's Response)

> "According to him, the term in question is a meaningful denoting expression, but it fails to “denote a proposition” (Curry 1942a: 62)."  (Curry's Response)

> "Curry also criticized attempts to resolve the paradox by embracing a non-classical logic for the conditional. He claimed that the logics available to play this role were either ad hoc or failed to be “adequate for mathematics” (Curry & Feys 1958: 261)."  (Curry's Response)

> "Several remarks by Kripke (1975; esp. pp. 699–700) suggest that this is one way to understand his response to truth-theoretic paradox. For a more recent defense of this approach, which is one example of what section 4 calls a Curry-incompleteness approach, see Goldstein 2000."  (Curry's Response; "this approach" = meaningful sentences that "fail to express propositions")

> "Curry remarks that “the central idea” of his derivation of the paradox was “suggested by some work of R. Carnap” (Curry 1942b)."  (Curry's Professed Debt to Carnap)

Relied on for: Curry's own targets and response; the no-proposition
approach (Kripke 1975 as read by the authors; Goldstein 2000); Carnap.
Context: Curry used Curry *terms*, not sentences; the authors say his
approach "isn’t available" for the sentence versions, but a counterpart is.

## C. Notes to the entry

Source: same entry, "Notes to Curry's Paradox", notes 1, 2, 4, 14.
Original: https://plato.stanford.edu/archives/fall2024/entries/curry-paradox/notes.html
  (copyrighted; excerpts only)
Retrieved: 2026-09-27 (read at the URL above with curl)

> "The term “Curry’s paradox” appears to originate in Fitch 1952; other influential early formulations include Moh 1954, Geach 1955, and Prior 1955."  (note 1)

> "Precursors to Curry’s paradox are also found in the work of medieval and late scholastic logicians: for references and discussion, see Ashworth 1974: 125, Read 2001 and Hanke 2013."  (note 1)

> "Curry’s paper is entitled “The Inconsistency of Certain Formal Logics” (1942b). By “inconsistency”, he means absolute inconsistency, i.e., triviality."  (note 2)

> "Some discussions (e.g., Restall 1994: vii; Humberstone 2006) demarcate the relevant notion using a biconditional rather than intersubstitutability, namely as any \(\kappa\) such that \(\vdash_{\mathcal{T}} \kappa {\leftrightarrow}(\kappa {\rightarrow}\pi)\)."  (note 4)

> "Zardini (2015), who calls Cont the rule of “absorption”, notes that given MP it entails there can be no Curry sentence for an “unacceptable sentence” \(\pi\)."  (note 14)

Relied on for: origin of the name; medieval precursors; "absorption";
the biconditional form used in the implant's logic check.

## D. Primary sources — bibliographic verification only (texts not read)

No open copy of these was fetched; DOIs verified 2026-09-27 by DOI content
negotiation (CSL JSON), Curry 1942b also via api.crossref.org/works:

- Curry, Haskell B. 1942. "The inconsistency of certain formal logics".
  Journal of Symbolic Logic 7(3): 115–117. https://doi.org/10.2307/2269292
  (Crossref: Cambridge University Press, issued 1942-09).
- Church, Alonzo 1942. Review of Curry 1942b. JSL 7(4): 170.
  https://doi.org/10.2307/2268117
- Moh Shaw-Kwei 1954. "Logical paradoxes for many-valued systems". JSL
  19(1): 37–40. https://doi.org/10.2307/2267648
- Geach, P. T. 1955. "On Insolubilia". Analysis 15(3): 71–72.
  https://doi.org/10.1093/analys/15.3.71
- Löb, M. H. 1955. "Solution of a problem of Leon Henkin". JSL 20(2):
  115–118. https://doi.org/10.2307/2266895
- Prior, A. N. 1955. "Curry's paradox and 3-valued logic". Australasian
  Journal of Philosophy 33(3): 177–182. https://doi.org/10.1080/00048405585200201
- Meyer, Routley & Dunn 1979. "Curry's paradox". Analysis 39(3): 124–128.
  https://doi.org/10.1093/analys/39.3.124
- Kripke, Saul 1975. "Outline of a Theory of Truth". Journal of Philosophy
  72(19). https://doi.org/10.2307/2024634
- Slaney, John 1990. "A general logic". AJP 68(1): 74–88.
  https://doi.org/10.1080/00048409012340183
- Priest, Graham 1994. "The Structure of the Paradoxes of Self-Reference".
  Mind 103(409): 25–34. https://doi.org/10.1093/mind/103.409.25
- Goodship, Laura 1996. "On dialethism". AJP 74(1): 153–161.
  https://doi.org/10.1080/00048409612347131
- Priest, Graham 2006. In Contradiction (expanded ed.). OUP.
  https://doi.org/10.1093/acprof:oso/9780199263301.001.0001
- Field, Hartry 2008. Saving Truth from Paradox. OUP.
  https://doi.org/10.1093/acprof:oso/9780199230747.001.0001
- Beall, Jc 2009. Spandrels of Truth. OUP.
  https://doi.org/10.1093/acprof:oso/9780199268733.001.0001
- Shapiro, Lionel 2011. "Deflating Logical Consequence". Philosophical
  Quarterly 61(243): 320–342. https://doi.org/10.1111/j.1467-9213.2010.678.x
- Zardini, Elia 2011. "Truth without contra(di)ction". Review of Symbolic
  Logic 4(4): 498–535. https://doi.org/10.1017/S1755020311000177
- Ripley, David 2013. "Paradoxes and Failures of Cut". AJP 91(1): 139–164.
  https://doi.org/10.1080/00048402.2011.630010 (Crossref dates the online
  issue 2012; the SEP cites 2013).
- Beall, Jc & Julien Murzi 2013. "Two Flavors of Curry's Paradox". Journal
  of Philosophy 110(3): 143–165. https://doi.org/10.5840/jphil2013110336
- Mares, Edwin & Francesco Paoli 2014. "Logical Consequence and the
  Paradoxes". Journal of Philosophical Logic 43(2–3): 439–469.
  https://doi.org/10.1007/s10992-013-9268-4
- Beall, Jc 2015. "Free of Detachment: Logic, Rationality, and Gluts".
  Noûs 49(2): 410–423. https://doi.org/10.1111/nous.12029
- Nolan, Daniel 2016. "Conditionals and Curry". Philosophical Studies
  173(10): 2629–2647 (Crossref; the SEP prints 2629–2649).
  https://doi.org/10.1007/s11098-016-0666-7

Relied on for: DOI links on the page; no claim about these texts beyond
what the SEP authors report.
Context: Semantic Scholar lists Curry 1942b, Prior 1955 and Meyer et al.
1979 as closed access; the open copies it lists for Beall 2015 and Zardini
2011 could not be downloaded.
