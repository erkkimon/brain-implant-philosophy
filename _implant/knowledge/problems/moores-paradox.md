---
type: article
about: concept
title: "Moore's paradox"
description: "Why is it absurd to assert 'p, but I don't believe that p' (omissive) or 'I believe that p, but not-p' (commissive), when either may be true? Moore's 1942/1944 sentences, Wittgenstein's PI II.x and letter, and the responses on record (Moore's implication, self-representation, the knowledge norm, Wittgensteinian expressivism, Shoemaker's belief-first account, Hintikka's doxastic logic, Sorensen's blindspots, Smithies' asymmetry) with their owners."
tags: [problem, paradox, epistemology, philosophy-of-language]
timestamp: 2026-10-01T19:53:21Z
---

# Moore's paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Primary texts: Moore, "A Reply to My Critics" (Schilpp ed., 1942, pp. 541–543;
excerpt: `raw/moore-1942-reply-to-my-critics-pictures-last-tuesday.md`) and
"Russell's 'Theory of Descriptions'" (Schilpp ed., 1944, p. 204; excerpt:
`raw/moore-1944-russells-theory-of-descriptions-he-has-gone-out.md`);
Wittgenstein, *Philosophical Investigations* II.x, pp. 190–192 (Anscombe tr.;
excerpt: `raw/wittgenstein-1953-philosophical-investigations-2-x-moores-paradox.md`).
Maps: Sorensen, [SEP Fall 2024 "Epistemic Paradoxes"](https://plato.stanford.edu/archives/fall2024/entries/epistemic-paradoxes/)
§§5.3–5.4 (excerpt: `raw/sep-epistemic-paradoxes-fall-2024-moores-problem.md`);
Pagin & Marsili, [SEP Fall 2024 "Assertion"](https://plato.stanford.edu/archives/fall2024/entries/assertion/)
(excerpt: `raw/sep-assertion-fall-2024-moores-paradox-and-knowledge-norm.md`);
Smithies ([2016](https://doi.org/10.1111/phis.12075), §2, manuscript pages;
excerpt: `raw/smithies-2016-belief-and-self-knowledge-moores-paradox.md`).
Sorensen and Smithies each also report a solution of their own; those are marked as theirs.

## The question

Moore's first sentence: "And this is why to say such a thing as “I went to the pictures last Tuesday, but I don’t believe that I did” is a perfectly absurd thing to say, although what is asserted is something which is perfectly possible logically" (1942, p. 543).
His second: "This, though absurd, is not self-contradictory; for it may quite well be true." (1944, p. 204), said of "I believe he has gone out, but he has not".
Sorensen: "Moore’s problem is to explain what is odd about declarative utterances such as (M). This explanation needs to encompass both readings of (M):" — *p* & B~*p* and *p* & ~B*p* (SEP, §5.3).
Smithies names the two forms: "(3) p, but I don’t believe that p. (The omissive form.) (4) I believe that p, but it’s not the case that p. (The commissive form.)" (2016, §2, ms. p. 6).
Woods reports the terms as the literature's: "Theorists call the second construction “commissive” as opposed to “omissive” versions of Moore’s paradox." (2014, p. 4, n. 13; excerpt: `raw/woods-2014-expressivism-and-moores-paradox.md`).
Smithies states where the paradox lies: "There is a paradox here because asserting Moorean sentences seems absurd or self-defeating in much the same way as asserting a contradiction, and yet Moorean assertions are not contradictions; after all, they can be true." (§2, ms. p. 7).
Sorensen: "The common explanation of Moore’s absurdity is that the speaker has managed to contradict himself without uttering a contradiction." (§5.3). The oddity is first-personal on his account: "There is no problem with third person counterparts of (M)." (§5.3), and the sentence can be "embedded unparadoxically in conditionals" (§5.3).

**Propositional check (this implant, 2026-09-27; logic, not a position).**
Let *p* be the reported fact and *b* the atom *I believe that p* (for the
commissive form, *c*: *I believe that not-p*). `logic.py` finds a row where
*p* & ~*b* is true while *p* & ~*p* is false (output: `INVALID`, counterexample row `b=F, p=T`) and
likewise for *p* & *c* (`INVALID`, row `c=T, p=T`): neither conjunction entails a
contradiction, so each is satisfiable in propositional logic. This matches
Moore's "not self-contradictory" (1944, p. 204). The tool treats "I believe"
as an unanalysed atom; any account of why the conjunctions cannot be
coherently asserted or believed needs a doxastic or epistemic logic (see
Hintikka below), which the tool does not cover.

**Where it comes from.** Stroll: "In October, 1944 G. E. Moore gave a talk to the Moral Science Club in Cambridge that contained a sentence that has become known as “Moore’s paradox”." (2010, Introduction; excerpt: `raw/stroll-2010-moores-paradox-revisited-wittgenstein-letter.md`).
Smithies: "The paradox was named by Wittgenstein 1953: 190." (n. 10), adding that Moore's "most detailed discussion is in Moore 1993" (the *Selected Writings* text, not read here).

## Why it matters

- **Assertion.** Pagin & Marsili: that asserting involves representing oneself as believing "is often claimed to be shown by Moore’s Paradox" (SEP "Assertion", §4.1); Moore's paradox is one of the conversational patterns offered for the knowledge norm of assertion (§5.1.4).
- **Logic.** Wittgenstein's letter to Moore, as Stroll quotes it from Monk (1990: 545): "You have said something about the logic of assertion." and "that contradiction isn’t the unique thing people think it is" (Stroll 2010, Introduction).
- **Self-knowledge.** Shoemaker's argument that a rational thinker cannot be "self-blind" turns on "making irrational Moore-paradoxical judgments" (Gertler, [SEP Fall 2024 "Self-Knowledge"](https://plato.stanford.edu/archives/fall2024/entries/self-knowledge/), §3.6; excerpt: `raw/sep-self-knowledge-and-introspection-fall-2024-shoemaker-moore-paradox.md`).
- **Metaethics.** Woods uses it as a test of expressivism: "we do not find moral versions of Moore’s paradox where we would expect, given the expressivist story about expression" (2014, p. 4). Moore's 1942 illustration itself answers Stevenson on the ethical sense of "right" (1942, p. 541).
- **Other epistemic paradoxes.** Sorensen suggests "Church may have been inspired by G. E. Moore’s (1942, 543) sentence" (§5.3; see [Fitch's paradox](fitchs-paradox-of-knowability.md)); he calls the preface statement "equivalent to a very long disjunction of blindspots" (§5.4; see [lottery and preface](lottery-and-preface-paradoxes.md)) and links blindspots to the [surprise examination](surprise-examination-paradox.md) (§5.4).
- **Epistemic logic.** "Sentences of this form are generally referred to as Moore sentences." (Rendsvig, Symons & Wang, [SEP Fall 2024 "Epistemic Logic"](https://plato.stanford.edu/archives/fall2024/entries/logic-epistemic/), §1; excerpt: `raw/sep-epistemic-logics-fall-2024-moore-sentences.md`).

## Positions taken

Smithies groups solutions as linguistic (§2.1), psychological and epistemological (§2.2): "We can draw a distinction between psychological solutions, which claim that believing Moorean conjunctions is psychologically impossible, and epistemological solutions, which claim that believing Moorean conjunctions is epistemically irrational." Stroll's grouping: "those who find – as apparently Wittgenstein did – that the paradox turns on the concept of assertion, and those who think it turns on the concept of belief" (2010, "Assertion and belief"). Linguistic accounts come first and belief-based ones after, in Smithies' sequence; families from other sources follow. None is ranked here.

- **Moore's implication account (Moore 1942, 1944).** "But nevertheless your saying that you did, does imply (in another sense) that you believe you did; and this is why “I went, but I don’t believe I did” is an absurd thing to say." (1942, p. 543). Moore: the implication "simply arises from the fact, which we all learn by experience, that in the immense majority of cases a man who makes such an assertion as this does believe or know what he asserts" (pp. 542–543); for the commissive case, "people, in general, do not make a positive assertion, unless they do not believe that the opposite is true" (1944, p. 204). Pagin & Marsili's summary: "So by asserting (25) the speaker induces a contradiction between what she asserts and what she implies." (§4.1).
  *Against:* Smithies: "the Moorean solution cannot easily be extended from the omissive form to the commissive form" (§2.1). Baldwin's assessment: "Wittgenstein rightly saw that this explanation was superficial" ([SEP Fall 2024 "George Edward Moore"](https://plato.stanford.edu/archives/fall2024/entries/moore/), §7; excerpt: `raw/sep-moore-fall-2024-legacy-moores-paradox.md`). Stroll reports Monk: Moore held it "an absurdity for psychological, rather than for logical, reasons – an interpretation that Wittgenstein vigorously rejected".
- **Self-representation (Black 1952; Davidson 1984; Unger 1975; Slote 1979).** "in asserting that p the speaker represents herself as believing that p" (Pagin & Marsili, §4.1); Unger (1975: 253–270) and Slote (1979: 185) "made the stronger claim that in asserting that p the speaker represents herself as knowing that p" (§4.1).
- **The knowledge norm of assertion (Williamson 2000).** "(KNA) One must: assert p only if one knows p." Williamson (2000: 253) "claims that an utterance of (26) is just as odd as any ordinary Moorean sentence involving belief" — (26) being "It is raining, but I don’t know that it is raining." Pagin & Marsili give the derivation: "Since knowledge is factive, this generates a contradiction: it follows that an assertion of (26) cannot be proper, and this explains its oddity." (§5.1.4). Supporters they list: "DeRose (2002), Reynolds (2002), Adler (2002: 275), Hawthorne (2004), Stanley (2005), Engel (2008), Schaffer (2008), and Turri (2010), among others."
  *Against:* a justification norm (Kvanvig 2009; Hill & Schechter 2007; Douven 2009; Lackey 2007; McKinnon 2015, per n. 21); Gricean principles (Douven 2006; Maitra & Weatherson 2010; Cappelen 2011, per n. 22); and Sosa ([2009](https://doi.org/10.1007/s11098-008-9255-8)): "(KNA)’s explanation of Moorean assertions fails to generalize as it should" (§5.1.4).
- **Wittgensteinian expressivism (Wittgenstein 1953; Heal 1994).** Smithies: "In contrast, Wittgenstein claims that in asserting that I believe that p, I thereby assert that p. On this view, one asserts a contradiction by asserting a conjunction of the commissive form. Inspired by Wittgenstein, Jane Heal (1994) claims that asserting that I believe that p functions to express and not merely to report the belief that p." (§2.1; [Heal 1994](https://doi.org/10.1093/mind/103.409.5)). Gertler reports the wider family of expressivist accounts of avowals, whose "most radical version" is "sometimes attributed to Wittgenstein" (§3.8).
  *Against:* Smithies: "the Wittgensteinian solution cannot easily be extended from the commissive form to the omissive form" (§2.1); Smithies also holds that if the paradox "is not a purely linguistic phenomenon", this "undermines many of the earliest solutions to Moore’s paradox, including those originally proposed by Moore and Wittgenstein" (§2.1).
- **Belief first (Shoemaker 1994, 1995, 1996).** "An explanation of why one cannot (coherently) assert a Moore-paradoxical sentence will come along for free, via the principle that what can be (coherently) believed constrains what can be (coherently) asserted" (Shoemaker 1996: 76, as quoted by Smithies §2.1). Shoemaker "notes that one cannot self-consciously believe an omissive Moorean conjunction without thereby having contradictory beliefs" (Smithies §2.5), since "if one believes something, and considers whether one does, one must, on pain of irrationality, believe that one believes it" (1996: 77, as quoted). Smithies cites "Hintikka 1962: 67 and Shoemaker 1996: 85-6 for the claim that it’s impossible to believe an omissive Moorean conjunction" (n. 13) — the claim Smithies' psychological solutions make. Schwitzgebel reports Shoemaker's self-blindness dilemma ([SEP Fall 2024 "Introspection"](https://plato.stanford.edu/archives/fall2024/entries/introspection/), §4.1.2; [Shoemaker 1995](https://doi.org/10.1007/BF00989570)).
- **Irrational belief (J. Williams 1994; Williamson 2000; Silins 2020).** "John Williams (1994: 165) argues that it’s always irrational to believe an omissive Moorean conjunction, p and I don’t believe that p, because it is self-falsifying in the sense that believing the conjunction makes it false." (Smithies §2.3). "Timothy Williamson argues that believing omissive Moorean conjunctions is irrational because they cannot be known (2000: 253-4)." (§2.4), with "The knowledge rule: one should believe p only if one knows p. (2000: 255-6)". Silins: in a Moore-paradoxical judgment "you flout the justification given to you by your judgment that p" (2020: 334, per Gertler §3.5).
  *Against:* "Claudio de Almeida (2001: 41) rejects Williams’ proposal on the grounds that one can rationally believe necessary falsehoods." (Smithies §2.3). Smithies: "Like many others, I reject the knowledge rule on the grounds that one can rationally believe that p without knowing that p in deception cases in which it’s false that p or Gettier cases in which it’s accidentally true that p." (§2.4).
- **Blindspots (Sorensen 1988).** Sorensen's own account, in the voice of his SEP entry: "A blindspot for a propositional attitude is a consistent proposition that cannot be accessed by that attitude." (§5.4); "Although I cannot rationally believe ‘Polar bears have black skin but I believe they do not’ you can believe that I mistakenly believe polar bears do not have black skin." and "This is an asymmetry imposed by rationality rather than irrationality." (§5.4). Smithies reports that "Roy Sorensen notes that there are Moorean sentences that have neither omissive nor commissive forms" (§2.2), e.g. "God knows that we are atheists" (Sorensen 1988: 17).
- **Doxastic logic (Hintikka 1962).** Rendsvig, Symons & Wang call Hintikka's *Knowledge and Belief* "the foundational text for the study of epistemic logic" (§1); "Hintikka endorses 4 for belief" (B*φ* → BB*φ*), and the entry states consistency of belief as "captured by the principle \[\neg B_{a}\bot.\]" (§2.6). "The aforementioned Moore sentences, e.g., \(B_{a}(p\wedge B_{a}\neg p)\) express a higher-order attitude." (§2.2). Hintikka 1962 itself was not read (see the excerpt's context note).
- **Asymmetry (Smithies 2016).** "I’ve argued that believing omissive Moorean conjunctions is always irrational. In contrast, I’ll argue that believing commissive Moorean conjunctions is sometimes rational, but only when one has contradictory beliefs." (§2.7). His principle: "The rational biconditional thesis: necessarily, if one is rational, and one has some doxastic attitude towards the proposition that one believes that p, then one believes that p if and only if one believes that one believes that p." (§2.8). He also notes "It is sometimes assumed that a solution to Moore’s paradox should give a unified treatment of omissive and commissive forms." (§2.7, citing Green & Williams 2007).
- **Commitment (Woods 2014).** "The proper explanation of this is that when I assert p, I somehow commit myself to believing that p, but not by asserting that I believe that p." (p. 2).
- **Only apparently paradoxical (Stroll 2010).** Stroll counts himself among "those who think, as I do, that its appearance as paradoxical is apparent only", and of the assertion and belief families: "I think both views are incorrect, and here are some arguments to that effect." (2010, "Annulling the paradox").

**Distribution, as reported.** Stroll: "My sense is that commentators on the paradox have split more or less evenly on this issue" (assertion vs. belief; "Assertion and belief"). No survey figure is recorded.

## Arguments in play

(none recorded as separate argument pages yet). The knowledge-norm
derivation (Pagin & Marsili §5.1.4) and Shoemaker's self-intimation argument
(Smithies §2.5) are quoted above.

## Thinkers who addressed it

- **G. E. Moore** (1942, pp. 541–543; 1944, p. 204; Moral Science Club talk, October 1944, per Stroll) — implication account.
- **Ludwig Wittgenstein** (letter to Moore, per Monk 1990: 545 via Stroll; PI II.x, 1953, pp. 190–192) — names the paradox; assertion and "I believe".
- **Max Black** (1952), **Donald Davidson** (1984) — self-representation (Pagin & Marsili §4.1).
- **Jaakko Hintikka** (1962) — doxastic logic (Rendsvig et al. §§1, 2.6; Smithies n. 13).
- **Peter Unger** (1975), **Michael Slote** (1979) — representing oneself as knowing.
- **Roy Sorensen** (1988) — blindspots; forms that are neither omissive nor commissive.
- **Jane Heal** (1994), **John Williams** (1994), **Sydney Shoemaker** (1994, 1995, 1996).
- **[Timothy Williamson](../thinkers/williamson.md)** (1996; 2000: 253–256) — knowledge norm; knowledge rule.
- **Claudio de Almeida** (2001), **David Sosa** (2009), **Avrum Stroll** (2010), **Jack Woods** (2014), **Declan Smithies** (2016, 2019), **N. Silins** (2020).

## Framings and reframings

- **Assertion and supposition.** Wittgenstein: "Moore’s paradox can be put like this: the expression “I believe that this is the case” is used like the assertion “This is the case”; and yet the hypothesis that I believe this is the case is not used like the hypothesis that this is the case." (PI II.x, p. 190). In an imagined language where belief is shown only by tone, "Moore’s paradox would not exist in this language; instead of it, however, there would be a verb lacking one inflexion." (p. 191).
- **Contradiction is not the only inadmissible form.** Wittgenstein's letter, as Stroll quotes it: "It isn’t the only logically inadmissible form and it is, under certain circumstances, admissible. And to show that seems to me the chief merit of your paper."
- **An identity question.** Baldwin's reading: Moore "had put his finger on a much deeper phenomenon here which concerns our sense of our own identity as thinkers" (SEP §7).
- **Unsuccessful announcements.** Baltag & Renne: "An announcement of a Moore formula is unsuccessful because, after the announcement the agent comes to know the first conjunct p" ([SEP Fall 2024 "Dynamic Epistemic Logic"](https://plato.stanford.edu/archives/fall2024/entries/dynamic-epistemic/), §2.3), a phenomenon "noted early on by Hintikka (1962)".

Not in the excerpts held: Moore's *Selected Writings* text (1993, pp. 207–212)
beyond Smithies' quotation, Hintikka 1962 itself, Green & Williams (eds.)
2007, and the published text of Wittgenstein's letter; they are left out
until a source is read.

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — see The question.
- [Knowledge](../vocabulary/knowledge.md) — factivity, used by the knowledge-norm derivation.
- [Classical logic](../methods/classical-logic.md) — the propositional check above.
- *Assertion*, *omissive/commissive*, *blindspot*, *doxastic logic*, *self-intimation* — open work in [vocabulary](../vocabulary/index.md).

Related problems: [the paradox of analysis](paradox-of-analysis.md) (a different Moore problem, from the same 1942 volume).
