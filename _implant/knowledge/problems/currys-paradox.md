---
type: article
about: concept
title: "Curry's paradox"
description: "A sentence that says 'if I am true, then P' seems to prove any P, with no negation involved — Curry 1942, the principles it uses (modus ponens, conditional proof, contraction, naive truth or comprehension), and the families of response the SEP records (restrict naive principles; contraction-free; detachment-free), each with its proponents."
tags: [problem, paradox, logic, philosophy-of-language, truth]
timestamp: 2026-09-28T07:01:48Z
---

# Curry's paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md)
and [How claims are graded](../../conventions/how-claims-are-graded.md).
Source for the map: Shapiro & Beall,
[SEP Fall 2024 "Curry's Paradox"](https://plato.stanford.edu/archives/fall2024/entries/curry-paradox/)
(substantive revision 2018-01-19; excerpt:
`raw/sep-curry-paradox-fall-2024-construction-lemma-and-responses.md`).
One of the [problems](./index.md); a [paradox](../vocabulary/paradox.md)
in the sense fixed there.

## The question

Shapiro & Beall's example: "Suppose that your friend tells you: “If what I’m saying using this very sentence is true, then time is infinite”." (§1.1).
Call the sentence *k*. The informal argument (§1.1): supposing *k* is true,
we have *k*'s conditional and its antecedent, so "Using modus ponens within
the scope of the supposition" we get "time is infinite" under the
supposition (step 3); "The rule of conditional proof now entitles us to
affirm a conditional with our supposition as antecedent" (step 4) — which
is *k* itself, so *k* is true (step 5), and modus ponens gives "Time is
infinite" (step 6). The authors: "We seem to have established that time is infinite using no assumptions beyond the existence of the self-referential sentence \(k\), along with the seemingly obvious principles about truth that took us to (1) and also from (4) to (5)." (§1.1).
Any claim can replace "time is infinite"; the entry's second example is
"all numbers are prime" (§1.1), and common versions use "an arbitrarily
chosen claim" or "every falsity" (preamble). The form with "Santa Claus
exists" is one such instance; its source is not in the excerpts held.

In general terms: "a Curry sentence is a sentence that is equivalent, by
the lights of some theory, to a conditional with itself as antecedent"
(§1.2). The authors state the paradox as a "Troubling Corollary": "Every
Curry-complete theory is trivial" (§1.2), where a theory is trivial "when
it affirms every claim that is expressible in the language of the theory"
(§1.2). It "afflicts “naive” truth theories (those featuring a
“transparent” truth predicate) and “naive” set theories (those featuring
unrestricted set abstraction)" (§2).

**The Curry-Paradox Lemma** (§3.1, "a close variant of the Lemma in Curry
1942b"): given a Curry sentence κ for π, the identity rule Id, modus ponens
MP and contraction Cont (if α ⊢ α → β then ⊢ α → β) yield ⊢ π. "Cont is
a principle of contraction: two occurrences of the sentence \(\alpha\) are
“contracted” into one"; Zardini (2015) "calls Cont the rule of
“absorption”" (note 14). What the authors call "Probably the most common version" uses the law form
(α → (α → β)) → (α → β) instead (§3.2). "The Curry-Paradox Lemma entails that any Curry-complete theory must violate one or more of Id, MP or Cont on pain of triviality." (§3.1).

**Logic check (this implant, 2026-09-27).** Some discussions state a Curry
sentence as a biconditional, ⊢ κ ↔ (κ → π) (note 4). With `p` for κ and
`q` for π, `logic.py` reports `p <-> (p -> q)` ⊢ `q` "VALID"; with
conclusion `~q` "INVALID" (p=T, q=T), so the premise is satisfiable,
unlike the liar's `p <-> ~p` ("jointly inconsistent"). The contraction
instance `p -> (p -> q)` ⊢ `p -> q` is "VALID". So in classical
propositional logic the biconditional yields an arbitrary `q` without a
contradiction and without negation. The tool does not check how the
biconditional is obtained (truth or comprehension principles).

**Origin.** Curry 1942b, *Journal of Symbolic Logic* 7(3): 115–117,
[doi:10.2307/2269292](https://doi.org/10.2307/2269292) (Crossref; not read). By "inconsistency" Curry "means absolute
inconsistency, i.e., triviality" (note 2). His targets "were theories of
functional application, specifically Church’s untyped lambda calculus and
Curry’s own combinatory logic" (supplement). "The term “Curry’s paradox”
appears to originate in Fitch 1952" (note 1). "Geach (1955) and Löb (1955)
were the first to show, Curry sentences can be obtained using semantic
principles alone" (§2.2); Löb's referee, "now known to have been Leon
Henkin", saw that the method "“leads to a new derivation of paradoxes in
natural language”" (§2.2). Medieval precursors are referenced in note 1
(Ashworth 1974: 125; Read 2001; Hanke 2013).

## Why it matters

- **No negation.** The paradox "doesn’t essentially involve the notion of
  negation" (preamble); the point is traced to Church (1942), Moh (1954),
  Geach (1955), Löb (1955) and Prior (1955) (§5.1).
- **It survives some liar solutions.** Geach (1955: 72), as reported in
  §5.1, says it "cannot be resolved merely by adopting a system that
  contains a queer sort of negation" and that to keep "the naive view of
  truth, or the naive view of classes" one "must modify the elementary
  rules of inference relating to ‘if’". Meyer, Routley & Dunn (1979: 127)
  say it frustrates those who "hoped that weakening classical negation
  principles" would resolve Russell's paradox (§5.1). On paraconsistent
  logics: "Yet a number of prominent paraconsistent logics can’t serve as the basis for Curry-complete theories on pain of triviality." (§5.1.1, Slaney 1989's "Curry paraconsistent").
  On paracomplete logics: for Łukasiewicz's Ł3, first noted by Moh (1954),
  "Ł\(_{3}\) won’t underwrite a response to Curry’s paradox" (§5.1.2).
- **It shaped non-classical logic.** "the need to evade Curry’s paradox has
  played a significant role in the development of non-classical logics
  (e.g., Priest 2006; Field 2008)" (§5.1.2).
- **A shared structure.** Prior (1955: 180): "even Russell’s paradox
  presupposes only those properties of negation which it shares with
  implication" (§5.2). This bears on Priest's (1994) "principle of uniform
  solution" (§5.2).
- **Validity Curry.** A "boom in attention" to "validity Curry or v-Curry
  paradoxes (Whittle 2004; Shapiro 2011; Beall & Murzi 2013)" (§6), which
  "have sometimes been taken to motivate substructural consequence
  relations" (§6.3).

## Positions taken

Shapiro & Beall's classification (§4), with the proponents they name; not ranked. Id "has generally been left unquestioned (but see French 2016 and Nicolai & Rossi forthcoming)" (§4.2).

**Curry-incompleteness responses** "accept the Troubling Corollary" but
"deny that the target theories of properties, sets or truth are
Curry-complete"; they "can, and usually do, embrace classical logic" (§4).

- **Restrict naive truth.** Tarski's hierarchy, the revision theory (Gupta
  & Belnap 1993), contextualism (Burge 1979, Simmons 1993, Glanzberg 2001,
  2004) — "These theories all restrict the “naive” transparency principle"
  (§4.1). See [the liar paradox](liar-paradox.md).
- **Restrict naive comprehension.** "Russellian type theories and various
  theories that restrict the “naive” set abstraction principle" (§4.1).
  See [Russell's paradox](russells-paradox.md).
- **No proposition expressed.** Curry held his paradoxical term fails to
  "denote a proposition" (supplement, citing Curry 1942a: 62); a
  counterpart for sentences is read into Kripke (1975, pp. 699–700) and
  defended by Goldstein 2000 (supplement).

**Curry-completeness responses** "insist that there can be nontrivial Curry-complete theories" and so "invoke a non-classical logic" (§4).

- **Contraction-free (keep MP, reject Cont)** — "The most common strategy"
  per the authors, "first proposed by Moh (1954), who is cited approvingly
  by Geach (1955) and Prior (1955)" (§4.2).
  - *Strongly contraction-free* (reject MP′; substructural, rejecting
    structural contraction): Mares & Paoli 2014, Slaney 1990, Weir 2015,
    Zardini 2011 (§4.2.1); blocks step (3) (§4.2.3).
  - *Weakly contraction-free* (reject conditional proof CP): Field 2008,
    Beall 2009, Nolan 2016 (§4.2.1), sometimes motivated by possible and
    impossible "worlds" semantics (Beall 2009; Nolan 2016); blocks step (4)
    (§4.2.3).
- **Detachment-free (keep Cont, reject MP)** — "much more recent",
  "advocated, in different ways, by Ripley (2013) and Beall (2015)" (§4.2).
  - *Strongly detachment-free* (reject CCP): Goodship 1996, Beall 2015.
  - *Weakly detachment-free* (reject transitivity): Ripley 2013 (§4.2.2).
  - Both "find fault with the final move by MP to (6)" (§4.2.3).
- **Mixed.** Incompleteness in one domain, completeness in another ("e.g., Field 2008; Beall 2009") (§4).

**Cases for and against, as the sources supply them.**
- For detachment-free, against the charge that it is counterintuitive: an
  appeal to acceptance and rejection (Restall 2005); Ripley (2013) argues
  one may reject β without accepting α; Beall argues a principle weaker
  than CCP does the work (§4.2.2).
- Against weakly contraction-free and strongly detachment-free: for a
  consequence connective, CP "has seemed difficult to resist" (Shapiro
  2011; Weber 2014; Zardini 2013) and CCP "seems inescapable" (§6.1), as
  the authors report the v-Curry debate.
- Curry against non-classical conditionals: he "claimed that the logics
  available to play this role were either ad hoc or failed to be “adequate
  for mathematics” (Curry & Feys 1958: 261)" (supplement).
- Uniform solution (§5.2), three options as the authors list them:
  "On this approach, ECQ and Cont fail, while Red and MP hold (Priest 1994, 2006)."
  "On this approach, Red and Cont fail, while ECQ and MP hold (Field 2008; Zardini 2011)."
  "On this approach, ECQ and MP fail, while Red and Cont hold (Beall 2015; Ripley 2013)."
  The authors say uniformity "needn’t discriminate" among these.

No survey figure is recorded in the excerpts held.

## Arguments in play

(none as separate argument pages yet). Related: [the liar paradox](liar-paradox.md),
[Russell's paradox](russells-paradox.md), [the sorites paradox](sorites-paradox.md).

## Thinkers who addressed it

- **Medieval and late scholastic logicians** — precursors (note 1).
- **Haskell B. Curry** (1942b) — the Lemma; "a constraint on an adequate theory of functional application" (supplement).
- **Alonzo Church** (1942, review, [doi:10.2307/2268117](https://doi.org/10.2307/2268117)) — negation-free point (§5.1).
- **Frederic Fitch** (1952) — the name; set-theoretic version (§2.1, note 1).
- **Moh Shaw-Kwei** (1954, [doi:10.2307/2267648](https://doi.org/10.2307/2267648)) — first contraction-free proposal; Ł3 (§§4.2, 5.1.2).
- **P. T. Geach** (1955, [doi:10.1093/analys/15.3.71](https://doi.org/10.1093/analys/15.3.71)) — semantic version; modify "if" (§§2.2, 5.1).
- **M. H. Löb** (1955, [doi:10.2307/2266895](https://doi.org/10.2307/2266895)) and **Leon Henkin** — semantic version (§2.2).
- **A. N. Prior** (1955, [doi:10.1080/00048405585200201](https://doi.org/10.1080/00048405585200201)) — shared structure with Russell (§5.2).
- **Meyer, Routley & Dunn** (1979, [doi:10.1093/analys/39.3.124](https://doi.org/10.1093/analys/39.3.124)) — paraconsistency frustrated (§5.1.1).
- **Saul Kripke** (1975, [doi:10.2307/2024634](https://doi.org/10.2307/2024634)) — as read in the supplement.
- **[Graham Priest](../thinkers/priest.md)** (1994, [doi:10.1093/mind/103.409.25](https://doi.org/10.1093/mind/103.409.25); 2006) — uniform solution; per §5.2 he "rejects the claim that Curry sentences are true".
- **Hartry Field** (2008, [doi:10.1093/acprof:oso/9780199230747.001.0001](https://doi.org/10.1093/acprof:oso/9780199230747.001.0001)) — weakly contraction-free.
- **Jc Beall** (2009; 2015, [doi:10.1111/nous.12029](https://doi.org/10.1111/nous.12029)) — weakly contraction-free, then strongly detachment-free.
- **Elia Zardini** (2011, [doi:10.1017/S1755020311000177](https://doi.org/10.1017/S1755020311000177)) — strongly contraction-free.
- **David Ripley** (2013, [doi:10.1080/00048402.2011.630010](https://doi.org/10.1080/00048402.2011.630010)) — weakly detachment-free (nontransitive).
- **Beall & Murzi** (2013, [doi:10.5840/jphil2013110336](https://doi.org/10.5840/jphil2013110336)) — validity Curry (§6).

## Framings and reframings

- **A constraint on theories.** Since Curry 1942b, discussion "has usually had a different focus": "a proof that the system has a particular feature", typically triviality (§1.2).
- **A family.** The name "refers to a wide variety of paradoxes of self-reference or circularity" (preamble) — property, set, truth and validity versions (§§2, 6).
- **Negation as a special case.** Shapiro & Beall define a "Curry connective" (§5.2) that both ¬ and the operator α ↦ α → π instantiate, and treat the liar and Russell's paradox as a "generalized Curry paradox".

## Vocabulary

- [Paradox](../vocabulary/paradox.md); [Validity](../vocabulary/validity.md); [Classical logic](../methods/classical-logic.md), which "validates those principles" (§4).
- Curry sentence, triviality, contraction (absorption), modus ponens,
  conditional proof, naive truth (transparency), naive comprehension,
  paraconsistent, paracomplete, substructural logic — open work in
  [vocabulary](../vocabulary/index.md).
