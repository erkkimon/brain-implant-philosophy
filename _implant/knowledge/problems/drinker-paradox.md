---
type: article
about: concept
title: "The drinker paradox"
description: "Is there, in any pub, someone such that if they drink, everyone drinks? Smullyan's 'drinking principle' (What Is the Name of This Book?, 1978, problem 250), its two-case classical proof via the material conditional, its dual, its unprovability in intuitionistic and minimal logic (Warren, Diener & McKubre-Jordens 2018), and the non-empty-domain condition (Escardó & Oliva 2010)."
tags: [problem, paradox, logic, philosophy-of-logic, intuitionism]
timestamp: 2026-10-01T21:51:46Z
---

# The drinker paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Primary text: Raymond M. Smullyan, *What Is the Name of This Book?*
(Prentice-Hall, 1978, ISBN 0-13-955088-7), ch. 14, problem 250, pp. 208–211
of the [archive.org scan](https://archive.org/details/WhatIsTheNameOfThisBook)
(excerpt: `raw/smullyan-1978-what-is-the-name-of-this-book-250-drinking-principle.md`).
Formal literature: Warren, Diener & McKubre-Jordens,
["The Drinker Paradox and its Dual"](https://arxiv.org/abs/1805.06216v2) (arXiv, 2018;
excerpt: `raw/warren-diener-mckubre-jordens-2018-drinker-paradox-and-its-dual.md`);
Escardó & Oliva, [*Searchable Sets, Dubuc-Penon Compactness, Omniscience Principles, and the Drinker Paradox*](https://www.cs.bham.ac.uk/~mhe/papers/dp.pdf)
(2010; excerpt: `raw/escardo-oliva-2010-searchable-sets-drinker-paradox.md`).
Admitted from Wikipedia's [List of paradoxes, revision 1376699902](https://en.wikipedia.org/w/index.php?title=List_of_paradoxes&oldid=1376699902),
"Logic" (excerpt: `raw/wikipedia-drinker-paradox.md`).

## The question

Wikipedia's list entry: "In any pub, there is a customer such that if that customer is drinking, everybody in the pub is drinking." (List of paradoxes, rev. 1376699902).
Smullyan's question: "Does there really exist someone such that if he drinks, everybody drinks? The answer will surprise many of you." (problem 250).
In symbols, with *D* for "drinks" and the variables ranging over the people in the pub: ∃x(D(x) → ∀y D(y)).
Warren, Diener & McKubre-Jordens write the scheme as DP(Px) := ∃y(Py → ∀xPx) (§§3–4).

**Smullyan's proof (1978, p. 209).** "Let us look at it this way: Either it is true that everybody drinks or it isn't."
- Case 1: "Since everybody drinks and Jim drinks, then it is true that if Jim drinks then everybody drinks."
- Case 2: "Since it is false that Jim drinks, then it is true that if Jim drinks, everybody drinks."
- Summary: "The upshot of the matter is that if everyone drinks, then anyone can serve as the mysterious person, and if it is not the case that everybody drinks, then any nondrinker can serve as the mysterious person."

Structural note (this implant): the proof uses excluded middle (the first line) and the truth of a material conditional with a true consequent or a false antecedent; see [Classical logic](../methods/classical-logic.md).

**Propositional check (this implant, 2026-10-01; logic, not a position).**
`logic.py` has no quantifiers, so only a finite instance can be checked.
For a pub of exactly two people, let *a* stand for *the first drinks* and *b*
for *the second drinks*; "everyone drinks" is then *a & b*, and "there is
someone such that …" is the disjunction of the two instances.
`logic.py check --premises "a | ~a" --conclusion "(a -> a & b) | (b -> a & b)"`
outputs `VALID` and `conclusion is a tautology — the argument is valid regardless of premises`;
the three-person instance `(a -> a & b & c) | (b -> a & b & c) | (c -> a & b & c)`
gives the same output. A single fixed person, `a -> a & b`, outputs `INVALID`
with the counterexample row `a=T, b=F`: the claim is about *some* person, not
a given one. The tool reads *if … then* as the material conditional, checks
only classical truth tables, and treats each finite pub separately; it says
nothing about infinite domains, the empty domain, or intuitionistic
provability (all below).

## Why it matters

- **A theorem that looks false.** Smullyan files it among principles "which at first seem downright crazy, but turn out to be valid after all." (ch. 14, part C, p. 208). Warren et al.: "Due to its counterintuitive nature it is called a paradox, even though it actually is a classical tautology. However, it is not minimally (or even intuitionistically) provable." (abstract).
- **The material conditional.** Smullyan: "It comes ultimately from the strange principle that a false proposition implies any proposition." (p. 209). Wikipedia's article: "What is important to the paradox is that the conditional in classical (and intuitionistic) logic is the material conditional." (rev. 1366056307).
- **A test case between logics.** It separates classical from intuitionistic and minimal logic (Warren et al., abstract), and its truth depends on the domain being non-empty (Escardó & Oliva, §2).
- **Theorem proving.** Wikipedia reports that it appears in H. P. Barendregt's "The quest for correctness" (1996) "accompanied by some machine proofs" and that "it is sometimes used to contrast the expressiveness of proof assistants." (rev. 1366056307; Barendregt's text was not read here).

## Positions taken

No grouping of responses was found in the sources read; the accounts on
record are listed by owner, unranked. They answer different questions —
whether the principle holds, in which logic, and why it seems odd.

- **It holds classically; the oddity is the material conditional (Smullyan 1978).** "Solution. Yes, it really is true that there exists someone such that whenever he (or she) drinks, everybody drinks. It comes ultimately from the strange principle that a false proposition implies any proposition." (p. 209). Wikipedia's article: "The apparently paradoxical nature of the statement comes from the way it is usually stated in natural language." and adds that the conditional holds in the second case "even though their drinking may not have had anything to do with anyone else's drinking." (rev. 1366056307).
- **It holds classically via a "last drinker" (Warren et al. 2018).** "Classically this is true because there is always a last person to be drinking, and it is true for that person." (§4).
- **It is not intuitionistically or minimally provable (Warren et al. 2018).** "it is not minimally (or even intuitionistically) provable." (abstract); "Due to various non-classical interpretations of “there is”, however, countermodels may be formed (see Figure 1)." (§4). The constructivist objection as they put it: "Notably, the constructivist may object that it is not always clear who is the last to drink—except in the case of a tavern in which the number of patrons is an enumerable positive integer amount." (§4).
  *Background, Moschovakis (SEP 2024):* "Intuitionistic logic can be succinctly described as classical logic without the Aristotelian law of excluded middle" (§1), and "Every intuitionistic proof of a closed statement of the form A ∨ B can be effectively transformed into an intuitionistic proof of A or an intuitionistic proof of B, and similarly for closed existential statements." (§1; excerpt: `raw/sep-logic-intuitionistic-fall-2024-lem-and-existence.md`). The entry does not discuss the drinker paradox; the connection is a structural note of this implant: Smullyan's proof opens with excluded middle and does not name the drinker it proves to exist.
- **It holds exactly for non-empty pubs (Escardó & Oliva 2010).** "In classical logic, a set satisfies this condition if and only if it is non-empty." (§2). Wikipedia: "In the setting with empty domains allowed, the drinker paradox must be formulated as follows:" — "If and only if there is someone in the pub, there is someone in the pub such that, if they are drinking, then everyone in the pub is drinking." (rev. 1366056307). Warren et al. state the scheme "(in every nonempty tavern)" (§4).
- **The temporal reading is set aside (Wikipedia).** The article lists as one source of oddity "that there could be a person such that all through the night that one person were always the last to drink" and answers: "The formal statement of the theorem is timeless, eliminating the second objection because the person the statement holds true for at one instant is not necessarily the same person it holds true for at any other instant." (rev. 1366056307; that sentence carries a "citation needed" tag dated July 2017). Smullyan's epilogue stages the same objection — "Student / But that implies that at some time, everyone was drinking at once. Surely that never happened!" — and the logician's reply turns on the student's not drinking: "Logician I Didn't you tell me that you never drink?" (p. 210; "I" is OCR for "/").
- **Relevance logic as the alternative reading of "if" (Wikipedia).** The article points to relevance logic "for logics that demand relevant relationships between premise and consequent, unlike classical logic assumed here" (rev. 1366056307). No source read here works out the drinker paradox in a relevance logic.

## Arguments in play

(none recorded as separate argument pages yet). The two-case proof and the
propositional check are in The question.

**The empty domain (this implant, 2026-10-01; logic, not a position).**
Step 1: over a domain with no members, an existential claim ∃x(…) has no
instance that could make it true, so it is false. Step 2: the drinker
sentence is existential. Step 3: so over an empty pub it is false — while
∀y D(y) is true there vacuously. This matches Escardó & Oliva's "if and only
if it is non-empty" (§2). Standard classical semantics never meets the case:
an interpretation is ⟨d, I⟩ "where d is a non-empty set, called the domain-of-discourse, or simply the domain, of the interpretation" (Shapiro & Kouri Kissel, [SEP Fall 2024 "Classical Logic"](https://plato.stanford.edu/archives/fall2024/entries/logic-classical/) §4; excerpt: `raw/sep-logic-classical-fall-2024-non-empty-domain.md`).

## Thinkers who addressed it

- **Raymond Smullyan** (1978) — named and popularised it; Wikipedia: "It was popularised by the mathematical logician Raymond Smullyan, who called it the "drinking principle" in his 1978 book What Is the Name of this Book?" Smullyan credits the name: "some of my graduate students have affectionately dubbed "The Drinking Principle."" (p. 208).
- **John Bacon** — source of the variant "Prove that there is a woman on earth such that if she becomes sterile, the whole human race will die out." (Smullyan, p. 209).
- **Linda Wetzel and Joseph Bevando** — Smullyan's students who wrote the epilogue's imaginary dialogue (p. 210).
- **H. P. Barendregt** (1996) — machine proofs, per Wikipedia (not read).
- **Martín Escardó and Paulo Oliva** (2010) — the drinker paradox as a property of sets in constructive settings; "A classical principle that generally fails intuitionistically may hold in particular situations." (§2).
- **Louis Warren, Hannes Diener and Maarten McKubre-Jordens** (2018) — DP and its dual over minimal logic.
- **Milly Maietti** — reported by Warren et al. (§4, n. 9): "Milly Maietti has communicated to us the—currently unpublished—result that Hilbert’s Epsilon operator implies the drinker paradox."
- **Dominik Kirst and Haoyi Zeng** (2025) — a "blurred drinker paradox": "a newly identified fragment of the excluded middle (LEM) that we call the blurred drinker paradox (BDP)" (arXiv:2601.12592v2, abstract; LICS 2025, pp. 926–940, [doi:10.1109/lics65433.2025.00073](https://doi.org/10.1109/lics65433.2025.00073); excerpt: `raw/kirst-zeng-2025-blurred-drinker-paradox.md`; body not read).

## Framings and reframings

- **A joke first.** Smullyan prefaces it with a bar joke — "Gimme a drink, and give everyone elsch a drink, caush when I drink, everybody drinksh!" (p. 208) — whose speaker reads the conditional causally.
- **The dual.** Smullyan: "A dual version of The Drinking Principle is this: Prove that there is at least one person such that if anybody drinks, then he does." (p. 209); his proof again splits cases: "either there is at least one person who drinks or there isn't." (p. 210). Warren et al. write it Hε(Px) := ∃y(∃xPx → Py): "Hε resembles an axiom scheme form of Hilbert’s Epsilon operator [2]." (§4), and the abstract: "The same can be said of its dual, which is (equivalent to) the well-known principle of independence of premise,". Their reading of the pair: "The models are evocative of the intuitions. For, recall the “last drinker in the tavern” reason for accepting DP as true; similarly Hε can be justified by pointing to “the first person to drink”." (§4). Result: "DP and Hε are independent of each other in minimal logic with LEM (and so certainly over decidable predicates)." (Corollary 7). *Propositional check (this implant, 2026-10-01; logic, not a position):* the two-person instance `(a | b -> a) | (a | b -> b)` with premise `a | ~a` outputs `VALID` and `conclusion is a tautology — the argument is valid regardless of premises`; same limitations as above.
- **Logic between minimal, intuitionistic and classical.** "Starting from minimal logic, we can get to intuitionistic logic by adding ex falso quodlibet (EFQ), and to classical logic, by adding double negation elimination (DNE)." (Warren et al., §1); DP is among principles that "are all classically derivable." (§3) and that they show to be "independent of the law of excluded middle and of each other" (abstract).
- **The material conditional more generally.** Structural note (this implant): the principle Smullyan names, "a false proposition implies any proposition", is a property of the material conditional; see [the paradoxes of material implication](paradoxes-of-material-implication.md).

Not in the excerpts held: Barendregt 1996 (scan without text layer),
Cameron 1999 p. 91 and Wiedijk 2001 (cited by Wikipedia), the body of
Kirst & Zeng; left out until read.

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — in Warren et al.'s usage, "called a paradox, even though it actually is a classical tautology".
- [Validity](../vocabulary/validity.md) — Smullyan: principles that "turn out to be valid after all".
- [Classical logic](../methods/classical-logic.md) — the logic in which it is a theorem, with non-empty domains.
- *Material conditional*, *intuitionistic logic*, *minimal logic*, *excluded middle*, *non-empty domain*, *Hilbert's epsilon*, *independence of premise* — open work in [vocabulary](../vocabulary/index.md).
