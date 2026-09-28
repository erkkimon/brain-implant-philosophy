---
type: article
about: concept
title: "The lottery and preface paradoxes"
description: "Can it be rational to believe each of many propositions while believing that not all of them are true? Kyburg's (1961) lottery and Makinson's (1965) preface set a high-probability or careful-inquiry standard for belief against closure under conjunction; the responses on record — give up agglomeration, give up the Lockean threshold, add defeaters, stability, statistical evidence, knowledge norms, contextualism — each with its owner."
tags: [problem, paradox, epistemology, formal-epistemology, probability]
timestamp: 2026-09-28T07:01:48Z
---

# The lottery and preface paradoxes

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
claim grades as in [How claims are graded](../../conventions/how-claims-are-graded.md).
Part of the [problems](./index.md) branch. Map: Roy Sorensen,
[SEP Fall 2024 "Epistemic Paradoxes"](https://plato.stanford.edu/archives/fall2024/entries/epistemic-paradoxes/)
(revised 2022-03-03), §§3–4 (excerpt:
`raw/sep-epistemic-paradoxes-fall-2024-lottery-and-preface.md`); Konstantin
Genin & Franz Huber,
[SEP Fall 2024 "Formal Representations of Belief"](https://plato.stanford.edu/archives/fall2024/entries/formal-belief/)
(revised 2020-11-13), §4.2 (excerpt:
`raw/sep-formal-belief-fall-2024-lockean-thesis-and-lottery.md`); Luper,
Rysiew, Pagin & Marsili and Schwitzgebel in SEP Fall 2024 (excerpt:
`raw/sep-closure-contextualism-assertion-belief-fall-2024-lottery.md`).
The primary papers were not read; they are cited from DOI metadata only
(`raw/lottery-and-preface-paradoxes-bibliographic-records.md`).

## The question

Can a rational agent believe each of many propositions and also believe
that at least one of them is false? Two cases force the question.

**The lottery (Kyburg 1961).** Sorensen (§3): "In 1961 Henry Kyburg pointed out that this policy conflicted with a principle of agglomeration: If you rationally believe p and rationally believe q then you rationally believe both p and q."
"This policy" is acceptance at a probability threshold, which Sorensen
traces to science journals: "The threshold for acceptance was acknowledged to be somewhat arbitrary." (§3).
His worked case: "suppose the acceptance rule permits belief in any proposition that has a probability of at least .99. Given a lottery with 100 tickets and exactly one winner, the probability of ‘Ticket n is a loser’ licenses belief." (§3).
With *B* for "I rationally believe" and *p*ₙ for "ticket *n* is a loser",
the entry's four steps are:

1. "B∼(p1 & p2 & … & p100), by the probabilistic acceptance rule."
2. "Bp1 & Bp2 & … & Bp100, by the probabilistic acceptance rule."
3. "B(p1 & p2 & … & p100), from (2) and the principle that rational belief agglomerates."
4. "B[(p1 & p2 & … & p100) & ∼(p1 & p2 & … & p100)], from (1) and (3) by the principle that rational belief agglomerates."

The book is Kyburg, *Probability and the Logic of Rational Belief*
(Wesleyan University Press, 1961); Genin & Huber (§4.2.2) date the paradox
"originally to Kyburg (1961, 1997)" ([Kyburg 1997](https://doi.org/10.2307/2941105)).

**The preface (Makinson 1965).** Sorensen (§4): "In the preface of Introduction to the Foundations of Mathematics, Raymond Wilder (1952, iv) apologizes for the errors in the text."
"D. C. Makinson (1965, 205) quotes Wilder’s 1952 apology and extracts a paradox: Wilder rationally believes each of the assertions in his book. But since Wilder regards himself as fallible, he rationally believes the conjunction of all his assertions is false."
"If the agglomeration principle holds, (Bp & Bq) → B(p & q), Wilder would rationally believe the conjunction of all assertions in his book and also rationally disbelieve the same thing!" (§4).
The paper is Makinson, "The paradox of the preface", *Analysis* 25(6),
205–207 ([doi:10.1093/analys/25.6.205](https://doi.org/10.1093/analys/25.6.205)).
Sorensen marks the difference from the lottery: "The preface paradox does not rely on a probabilistic acceptance rule. The preface belief is organically generated in a qualitative fashion." (§4).

**A knowledge version.** Sorensen (§3) states a second lottery puzzle, about
knowledge rather than rational belief: "Lotteries pose a problem for the theory that a high probability for a true belief suffices for knowledge. Given that there are a million tickets and only one winner, the probability of ‘This ticket is a losing ticket’ is very high. Yet we are reluctant to say this makes the proposition known."
It leads to a skeptical argument: "So no contingent proposition is known (Hawthorne 2004). That is too much to give up! Yet the skeptic’s statistics seem impeccable." (§3).
He reports: "This skeptical paradox was noticed by Gilbert Harman (1968, 166)." (Harman, *American Philosophical Quarterly* 5(3): 164–173.)

**Logic (this implant, 2026-09-27; checked with `logic.py`, not a
position).** In a four-ticket skeleton, the premises `p1`, `p2`, `p3`,
`p4`, `~(p1 & p2 & p3 & p4)` are reported by `logic.py` as "premises are
jointly inconsistent — argument is vacuously valid". Any four of them are
consistent: with `p1` dropped the tool finds the row "p1=F, p2=T, p3=T,
p4=T" (the other ticket premises are symmetric), and without the fifth
premise all-true satisfies the rest. And `p1 & p2 & p3 & p4` follows "VALID" from `p1`–`p4`. So the
beliefs form a set that cannot all be true, though each proper subset can;
agglomeration is what turns that set into belief in one contradictory
proposition. Sorensen puts the same distinction as Kyburg's: "Reason forbids us from believing a proposition that is necessarily false but permits us to have a set of beliefs that necessarily contains a falsehood." (§3).

**Arithmetic (this implant, 2026-09-27; mathematics, not a position).**
Take a fair lottery of 1,000 tickets, exactly one winner, and a threshold
of 0.99. Each "ticket *i* loses" has probability 999/1,000 = 0.999 ≥ 0.99.
Since exactly one ticket wins, "tickets 1 to *k* all lose" has probability
(1,000 − *k*)/1,000: for *k* = 10 that is 0.99 (exactly the threshold),
for *k* = 11 it is 0.989 (below it), and for *k* = 1,000 it
is 0. So the set of propositions at or above 0.99 is not closed under
conjunction. For any threshold *s* < 1, a lottery with *N* tickets where
1 − 1/*N* ≥ *s* repeats this, which is Genin & Huber's general form: "Now think of a fair lottery with N tickets, where N is chosen large enough that 1−(1/N) ≥ s." (§4.2.2).
For the preface, *under an assumed independence* of 100 claims each at
0.99, the conjunction has probability 0.99¹⁰⁰ ≈ 0.366, so its negation
(≈ 0.634) is the more probable; independence is this example's
assumption, not Makinson's or Sorensen's.

## Why it matters

- **Belief and probability.** Genin & Huber (§4.2.2): "The lesson of the Lottery is that the strong thesis is in tension with deductive cogency." The strong thesis is the Lockean thesis (below); deductive cogency is their name for beliefs that are consistent and closed under consequence (§4.2).
- **Closure of justification.** Luper ([SEP "Epistemic Closure"](https://plato.stanford.edu/archives/fall2024/entries/closure-epistemic/), §6) states the multi-premise closure principle for justified belief, GJ, and writes: "However, GJ generates paradoxes (Kyburg 1961)."
- **Skepticism.** Sorensen (§3) traces probabilistic skepticism back: "Probabilistic skepticism dates back to Arcesilaus who took over the Academy two generations after Plato’s death."
- **What a paradox is.** Sorensen (§4) asks: "How can paradoxes change our minds if joint inconsistency is permitted?" — see Framings.
- **Assertion.** Pagin & Marsili ([SEP "Assertion"](https://plato.stanford.edu/archives/fall2024/entries/assertion/), §5.1.4) report lottery assertions as one datum in the debate over the norm of assertion (below).

## Positions taken

The first three entries concern the two horns of Kyburg's dilemma as
Sorensen reports it — "Kyburg poses a dilemma: either reject agglomeration or reject rules that license belief for a probability of less than one." (§3); the rest are grouped by the SEP entry that reports them.
No position is ranked here; assessments by the SEP authors are marked as
theirs.

- **Reject agglomeration (closure under conjunction).** Kyburg: "Kyburg rejects agglomeration. He promotes toleration of joint inconsistency (having beliefs that cannot all be true together) to avoid belief in contradictions." (Sorensen §3). Genin & Huber (§4.2.2): "According to Kyburg, what the paradox teaches is that we should give up on deductive cogency: full belief should not necessarily be closed under conjunction."
  On the preface Sorensen reports: "At this juncture many philosophers join Kyburg in rejecting agglomeration and conclude that it can be rational to have jointly inconsistent beliefs." (§4).
  - *Against:* Genin & Huber (§4.2.3): "For many, sacrificing deductive cogency is simply too high a price to pay for a bridge principle, even one so simple and intuitive as the strong Lockean thesis."
    Sorensen (§4): "The preface paradox pressures Kyburg to extend his tolerance of joint inconsistency to the acceptance of contradictions. For Makinson’s original specimen is a logician’s regret at affirming contradictions rather than false contingent statements." His case, from Sorensen 2001: "Consider a logic student who is required to pick one hundred truths from a mixed list of tautologies and contradictions (Sorensen 2001, 156–158). Although the modest student believes each of his answers, A1, A2, …, A100, he also believes that at least of one these answers is false. This ensures he believes a contradiction."
- **Justified belief is not closed under conjunction, knowledge is** (a position Luper states without naming holders). Luper (§6): "We may “justifiably believe” each conjunct, but not the conjunction, so GJ fails. However, we need not reject GK on these grounds." The route he describes: "We might take the position that if we believe some proposition p on the basis of its probability, nothing less than a probability of 1 will suffice to enable us to know that it is true. In that case GK will not succumb to our objection to GJ, for if the probability of two or more propositions is 1 then the probability of their conjunction is also 1."
  - *Against (a limit case):* "(Martin Smith 2016, 186–196) warns that even a probability of one leads to joint inconsistency for a lottery that has infinitely many tickets.)" (Sorensen §3).
- **Reject the strong Lockean thesis.** "Foley (1993) dubbed this view the Lockean thesis, after some apparently similar remarks in Book IV of Locke’s (1690/1975) Essay Concerning Human Understanding." (Genin & Huber §4.2.2). Its strong form: "(SLT) There is a threshold s∈(1/2, 1) such that all rational ⟨Bel, Pr⟩ satisfy Bel(A) iff Pr(A) ≥ s." "Many others take the lesson of the Lottery to be that the strong Lockean thesis is untenable." (§4.2.2).
  The weak form lets the threshold vary: "(WLT) For every rational ⟨Bel, Pr⟩ there is a threshold s∈(1/2, 1) such that Bel(A) iff Pr(A) ≥ s." and "More recent work, especially Leitgeb (2017), adopts the weaker thesis." (§4.2.2).
  - *Also Lockean:* "Many proposals, such as Easwaran (2015), Dorst (2017), are equivalent to a version of the Lockean thesis, where the threshold is determined by the utility the agent assigns to true and false beliefs. Since these are essentially Lockean proposals, they are subject to Lottery-style paradoxes." (Genin & Huber §4.2.5). Of Levi's epistemic-utility rule: "Levi takes pains to make sure that the result of this operation is deductively cogent and therefore avoids Lottery-type paradoxes." (§4.2.5).
- **High probability plus no defeater.** "Several authors (Pollock (1995), Ryan (1996), Douven (2002)) attempt to revise the strong Lockean thesis by placing restrictions on when a high degree of belief warrants full belief." "For example, Douven (2002) says that it is sufficient except when the proposition is a member of a probabilistically self-undermining set." (Genin & Huber §4.2.2; [Douven 2002](https://doi.org/10.1093/bjps/53.3.391)).
  - *Against:* Genin & Huber (§4.2.2) judge that "All proposals of this kind are vitiated by the following sort of example due to Korb (1992)", concluding "these proposals prohibit full belief in any proposition with degree of belief short of certainty. Douven and Williamson (2006) generalize this sort of example to trivialize an entire class of similar formal proposals." ([Douven & Williamson 2006](https://doi.org/10.1093/bjps/axl022)).
- **Stability (the Humean thesis).** "One proposal, due to Leitgeb (2013, 2014, 2017) and Arló-Costa (2012), holds that rational full belief corresponds to a stably high degree of belief, i.e. a degree of belief that remains high even after conditioning on new information." (Genin & Huber §4.2.3). Its verdict on the lottery: "No matter how many tickets are in the lottery, a Humean agent cannot believe any ticket will lose."
  - *Against:* Genin & Huber (§4.2.3): "In this Lottery situation the agent cannot fully believe any non-trivial proposition. This example also shows how sensitive the Humean proposal is to the fine-graining of possibilities."
- **Statistical evidence does not warrant full belief.** "Buchak (2014) argues that what partial beliefs count as full beliefs cannot merely be a matter of the degree of partial belief, but must also depend on the type of evidence it is based on." (Genin & Huber §4.2.2), with a bus case: "You have only statistical evidence in the first scenario, whereas in the second, a causal chain of events connects your belief to the accident (see also Thomson (1986), Nelkin (2000) and Schauer (2003))." ([Nelkin 2000](https://doi.org/10.2307/2693695)). Applied to the lottery: "If Buchak (2014) is right, no agent should have beliefs in lottery propositions–these beliefs would necessarily be formed on the basis of purely statistical evidence." (§4.2.3).
- **Belief is not high credence.** Schwitzgebel ([SEP "Belief"](https://plato.stanford.edu/archives/fall2024/entries/belief/), §2.3): "Some people also find it intuitive to say that a rational person holding a ticket in a fair lottery may not actually believe that they will lose, but instead regard it as an open question, despite having a “degree of belief” of, say, .9999 that they will lose." He cites "Harman 1986; Sturgeon 2008; Buchak 2014; Leitgeb 2017; Friedman 2019".
- **Lottery propositions are not known.** Luper (§4.2): "several theorists suggest that we do not in fact know that they are true because knowing them requires believing them because of something that establishes their truth, and we (normally) cannot establish the truth of lottery propositions." Among them: "Harman and Sherman (2004, p. 492) say that knowledge requires believing as we do because of something “that settles the truth of that belief.” On all four views, we fail to know that a claim is true when our only grounds for believing it is that it is highly likely." (The four: Dretske, Armstrong 1973, safe-indication theorists, Harman & Sherman.)
- **Knowledge norm of assertion (Williamson 2000).** Pagin & Marsili (§5.1.4) report that "it is intuitively incorrect for A to tell (27) to B (Williamson 2000: 246–249). No probability short of 1 seems to authorize A’s utterance of (27). Since A does not know that (27) is true, (KNA) explains the unacceptability of A’s utterance." — (27) being "Your ticket did not win." ([Williamson 2000](https://doi.org/10.1093/019925656x.001.0001)).
  - *Against:* "several authors argue that the oddity of Moorean Assertions and Lottery Assertions can be explained by appeal to a justification norm"; "it has been argued that Lottery Assertions and Moorean Assertions are improper because they violate more general (Gricean) conversational principles." (§5.1.4).
- **Contextualism.** Rysiew ([SEP "Epistemic Contextualism"](https://plato.stanford.edu/archives/fall2024/entries/contextualism-epistemology/), §3.5): "Several contextualists (e.g., Cohen 1988, 1998; Lewis 1996; Neta 2002; Rieber 1998) have suggested that we can resolve the lottery paradox by means of the same device(s) used to explain both skeptical paradoxes and seeming inconsistencies among everyday “knowledge” attributions:" — "we are reluctant to attribute “knowledge” to the subject in the lottery case just because the possibility of error has been made salient".
- **Causal theory of inferential knowledge (Harman 1968).** Sorensen (§3): "But his views about the role of causation in inferential knowledge seemed to solve the problem (DeRose 2017, chapter 5)." He adds that "the demise of the causal theory of knowledge meant new life for Harman’s lottery paradox."

No survey figure is recorded.

## Arguments in play

(none recorded as separate argument pages yet). Sorensen's four-step
lottery derivation and the preface argument are stated in The question;
their propositional core is checked there.

## Thinkers who addressed it

- **Arcesilaus** — probabilistic skepticism, as Sorensen dates it (§3).
- **John Locke** (1690), *Essay* IV — the "apparently similar remarks" behind the Lockean name (Genin & Huber §4.2.2).
- **Raymond Wilder** (1952, p. iv) — the preface apology (Sorensen §4).
- **Henry Kyburg** (1961, 1997) — the lottery; rejects agglomeration.
- **D. C. Makinson** (1965) — the preface.
- **Gilbert Harman** (1968, p. 166; with Sherman 2004) — the knowledge
  version; grounds that settle the truth (Sorensen §3; Luper §4.2); 1986
  cited by Schwitzgebel §2.3.
- **D. Armstrong** (1973), **F. Dretske** — as Luper §4.2 lists them.
- **[Judith Jarvis Thomson](../thinkers/thomson.md)** (1986), **Dana Nelkin** (2000), **Frederick
  Schauer** (2003), **Lara Buchak** (2014) — statistical evidence (Genin &
  Huber §4.2.2).
- **S. Cohen** (1988, 1998), **D. Lewis** (1996), **S. Rieber** (1998),
  **R. Neta** (2002) — contextualism (Rysiew §3.5).
- **Kevin Korb** (1992), **John Pollock** (1995), **Sharon Ryan** (1996),
  **Igor Douven** (2002), **Douven & Timothy Williamson** (2006) —
  defeater proposals and their trivialisation (Genin & Huber §4.2.2).
- **Richard Foley** (1993) — named the Lockean thesis; **Isaac Levi**;
  **Horacio Arló-Costa** (2012), **Hannes Leitgeb** (2013–2017) — stability;
  **Kenny Easwaran** (2015), **Kevin Dorst** (2017) (Genin & Huber §4.2).
- **[Timothy Williamson](../thinkers/williamson.md)** (2000, pp. 246–249) — lottery assertions and the
  knowledge norm (Pagin & Marsili §5.1.4).
- **John Hawthorne** (2004) — cited by Sorensen for the skeptical argument
  (§3); **Martin Smith** (2016) — the infinite lottery (§3).
- **Roy Sorensen** (2001; SEP 2022) — the logic-student case, the blindspot
  reading (§§4, 5.4).

Held bibliographically only: Hawthorne & Bovens,
[1999](https://doi.org/10.1093/mind/108.430.241), "The preface, the
lottery, and the logic of belief" (listed by Genin & Huber); its content is
not reported here.

## Framings and reframings

- **Is an inconsistent set a paradox?** Sorensen (§4): "If you know that your beliefs are jointly inconsistent but deny this makes for a giant paradox, then you should reject R. M. Sainsbury’s definition of a paradox as “an apparently unacceptable conclusion derived by apparently acceptable reasoning from apparently acceptable premises” (1995, 1)." This implant's [paradox](../vocabulary/paradox.md) uses a definition of the same form (apparently acceptable premises and reasoning, apparently unacceptable conclusion).
- **A scale effect.** "Kyburg might answer that there is a scale effect. Although the sensation of joint inconsistency is tolerable when diffusely distributed over a large body of propositions, the sensation becomes an itch when the inconsistency localizes (Knight 2002)." (Sorensen §4; the suggestion is Sorensen's, on Kyburg's behalf).
- **A disjunction of blindspots.** Sorensen (§5.4): "The author’s preface statement that there is some mistake in his book is equivalent to a very long disjunction of blindspots."
- **Kin to the surprise test.** "The resemblance between the preface paradox and the surprise test paradox becomes more visible through an intermediate case." (Sorensen §4) — see [the surprise examination paradox](surprise-examination-paradox.md).
- **Other paradox pages:** [Moore's paradox](moores-paradox.md),
  [Fitch's paradox of knowability](fitchs-paradox-of-knowability.md),
  [sorites](sorites-paradox.md), [liar](liar-paradox.md),
  [Newcomb's problem](newcombs-problem.md),
  [the St. Petersburg paradox](st-petersburg-paradox.md).

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — see Framings for Sorensen's
  challenge to the definition used there.
- [Knowledge](../vocabulary/knowledge.md) — the knowledge version turns on
  it; [validity](../vocabulary/validity.md) and
  [classical logic](../methods/classical-logic.md) — the four-step derivation.
- [Bayesian updating](../methods/bayesian-updating.md) — the stability
  thesis is stated in terms of conditioning.
- *Agglomeration* (closure under conjunction), *deductive cogency*,
  *Lockean thesis*, *acceptance rule*, *joint inconsistency*, *defeater*,
  *credence* — open work in [vocabulary](../vocabulary/index.md).
