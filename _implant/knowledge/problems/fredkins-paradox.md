---
type: article
about: concept
title: "Fredkin's paradox"
description: "Why can a choice between two equally attractive options be hard when, to the same degree, it can only matter less? Minsky's 1986 statement of an observation he credits to Edward Fredkin (The Society of Mind §5.5, p. 52), his habit-and-style reply, Lombrozo's (2017) expected-versus-actual-utility reading, Burkeman's (2018) tie to Buridan's ass, and the optimisation regress Wikipedia reports via Klein (2001)."
tags: [problem, paradox, decision-theory, rationality, choice]
timestamp: 2026-10-08T20:29:06Z
---

# Fredkin's paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Primary text: Marvin Minsky, *The Society of Mind* (New York: Simon & Schuster,
1986; ISBN 0-671-60740-5), §5.5 "Fashion and Style", p. 52
([scan of the 1988 Touchstone printing](https://archive.org/details/marvin-minsky-the-society-of-mind);
excerpt: `raw/minsky-1986-society-of-mind-5-5-fredkins-paradox.md`).
Later discussions read: Tania Lombrozo,
["Why Hard Decisions Should Be Easy (But Aren't)"](https://www.npr.org/sections/13.7/2017/04/17/524386548/why-hard-decisions-should-be-easy-but-aren-t),
NPR 13.7, 17 April 2017 (excerpt: `raw/lombrozo-2017-npr-why-hard-decisions-should-be-easy.md`);
Oliver Burkeman,
["Find it hard to make a big decision? Don't overthink it"](https://www.theguardian.com/lifeandstyle/2018/oct/19/this-column-will-change-your-life-oliver-burkeman),
*The Guardian*, 19 October 2018 (excerpt: `raw/burkeman-2018-guardian-fredkins-paradox.md`).
Admitted from Wikipedia's [List of paradoxes, revision 1376699902](https://en.wikipedia.org/w/index.php?title=List_of_paradoxes&oldid=1376699902),
"Decision theory"; Wikipedia's article
([rev. 1329161308](https://en.wikipedia.org/w/index.php?title=Fredkin%27s_paradox&oldid=1329161308))
is used as a pointer to sources and cited as such
(excerpt: `raw/wikipedia-fredkins-paradox-rev-1329161308-and-list-entry.md`).
No Stanford Encyclopedia entry was found to discuss it (SEP search for "Fredkin", 2026-10-08, returned entries on computation and cellular automata only).

## The question

Minsky's statement: "Fredkin’s Paradox: The more equally attractive two alternatives seem, the harder it can be to choose between them—no matter that, to the same degree, the choice can only matter less." (§5.5, p. 52).
Wikipedia's list paraphrases it as: "Fredkin's paradox: The more similar two choices are, the more time a decision-making agent spends on deciding." (rev. 1376699902).
Wikipedia's article draws the consequence: "Thus, a decision-making agent might spend the most time on the least important decisions." (rev. 1329161308, lead; the sentence follows the Minsky citation and has no source of its own).
The question the sources pose is how difficulty of choice and importance of choice can move in opposite directions, and what a deliberating agent should do about it.

**On the label.** Minsky introduces it as an "observation by my associate, Edward Fredkin" that "seems important enough to deserve a name" (p. 52); the name "Paradox" is Minsky's.
Lombrozo calls it "a compelling paradox" (2017). Whether it is a paradox in the sense of the implant's [vocabulary](../vocabulary/paradox.md) is not argued in any source read.

**Propositional check (this implant, 2026-10-08; logic, not a position).**
Let *E* stand for *the two alternatives seem equally attractive*, *H* for
*the choice is hard*, *M* for *the choice matters much*. Reading Minsky's
sentence as two conditionals (a simplification: his are comparatives),
`logic.py check --premises "E -> H" "E -> ~M" --conclusion "E & ~E"` outputs
`INVALID` with counterexample rows including `E=T, H=T, M=F`: the two clauses
are jointly satisfiable, so as stated they are not a contradiction. Adding a
third premise *H -> M* (a choice is hard only if it matters — a premise
supplied here for the check, not found stated in the sources read) gives
`logic.py check --premises "E -> H" "E -> ~M" "H -> M" --conclusion "~E"`:
`VALID`. The tension the sources describe therefore turns on some link between
difficulty and importance of this kind; the tool is propositional and does not
model degrees.

## Why it matters

- **Saving mental work.** Minsky's context is the economy of thought: "It can save a lot of mental work if one makes each arbitrary choice the way one did before. The more difficult the decision, the more this policy can save. The following observation by my associate, Edward Fredkin, seems important enough to deserve a name:" (p. 52).
- **Taste, style and art.** Minsky draws from it an account of taste: "No wonder we often can’t account for “taste”—if it depends on hidden rules that we use when ordinary reasons cancel out!" (p. 52).
- **Instrumental rationality.** Wikipedia's article: "Developed further, the paradox constitutes a major challenge to the possibility of pure instrumental rationality." (rev. 1329161308, lead). The sentence carries no citation; it is the article's assessment, and no read source develops it.
- **Life decisions.** Lombrozo applies it to choices of "life partners or surgical procedures" and to moving to Los Angeles or New York: "And so Fredkin's paradox applies: the decision will be hard but maybe shouldn't be; the decision "doesn't matter" in the sense that it doesn't affect your expected utility." (2017).

## Positions taken

No grouping of responses was found in the sources read; the responses on
record are listed by owner, unranked.

- **Minsky (1986): fall back on habit and style when reasons cancel out.** "It can save a lot of mental work if one makes each arbitrary choice the way one did before." and "When should we quit reasoning and take recourse in rules of style? Only when we're fairly sure that further thought will just waste time." (p. 52). He adds a limit, of the guilt felt for "just liking" art: "Perhaps they’re how our minds remind themselves not to abandon thought too recklessly." (p. 52).
- **Lombrozo (2017): the coin settles the process but not the outcome.** She proposes and then qualifies a decision rule: "We might be so bold as to propose "Fredkin's formula" for hard decisions: Just flip a coin. The choice doesn't matter much anyway." Her qualification: "Their expected utilities could be the same, and yet their actual utilities could diverge." and "What's true of the decision process — that our choice "doesn't matter" — isn't true of the decision outcome." Her conclusion: "What matters for hard decisions, then, isn't only a decision procedure that will maximize the odds of choosing the (perhaps marginally) better choice, but also one that will minimize future regret." and "Hard decisions are hard because the process keenly matters, not just the choice or its outcome."
- **Burkeman (2018): deliberation cannot change expected utility.** "Yet to the extent that you’re unable to know how things will turn out, overthinking is futile: it can’t affect what economists call your “expected utility”." (Guardian, 2018). His column's standfirst suggests one "could just flip a coin".
- **Calibrate deliberation to importance — and its regress (reported by Wikipedia).** "An intuitive response to Fredkin's paradox is to calibrate decision-making time with the importance of the decision: to calculate the cost of optimizing into the optimization, a version of the value of information. However, this response is self-referential and spawns a new, recursive paradox: the decision-maker must now optimize the optimization of the optimization, and so on." (rev. 1329161308, "Responses"). Wikipedia cites Gary Klein's chapter for this and quotes it: "Thus, if I want to optimize, I must also determine the effort it will take to optimize; however, the subtask of determining this effort will itself take effort and so forth into the tangle that self-referential activities create." (Klein 2001, pp. 111–112, as quoted by Wikipedia; Klein's text was not read here, and the quoted passage does not mention Fredkin).

## Arguments in play

- **From equal attraction to low stakes.** Lombrozo: "It seems to follow that hard decisions should be easy, because our choice matters so very little" is the step from near-equality of appeal to a small cost of error; she bounds it by "the "difference" between the value of the best option and the value of the alternative that we find nearly indistinguishable" (2017).
- **Expected versus actual utility.** Lombrozo's illustration: two bets paying $5, one on a quarter and one on a dime landing heads, have equal expected utility, "but in fact, it might be that only one of these bets yields a win" (2017). This is the ground of her reply above.
- **Two sources of difficulty.** Lombrozo: "These decisions are hard for two reasons: because no single option clearly dominates the alternatives, and because we expect our choice to have significant consequences. It's these two elements that explain why hard decisions should be easy — but are not." (2017).
- **The regress of meta-deliberation.** The Wikipedia/Klein passage quoted under *Positions*; the article frames it as a "recursive paradox" (rev. 1329161308).
- No argument page in this implant addresses the paradox yet: (none recorded).

## Thinkers who addressed it

- **Edward Fredkin** — originator of the observation, per Minsky ("observation by my associate, Edward Fredkin", p. 52); Lombrozo ("he attributes it to Edward Fredkin", 2017) and Burkeman ("proposed by the computer scientist Edward Fredkin", 2018) follow Minsky. Wikipedia calls him "American physicist Edward Fredkin" (rev. 1329161308). No text by Fredkin himself stating it was found.
- **Marvin Minsky** (*The Society of Mind*, 1986, §5.5, p. 52) — named and stated it; the habit-and-style reply.
- **Tania Lombrozo** (NPR 13.7, 2017) — "Fredkin's formula" and the expected/actual-utility and regret reading; the author line describes her as "a psychology professor at the University of California, Berkeley". The essay cites no study.
- **Oliver Burkeman** (*The Guardian*, 2018) — popular restatement following Lombrozo; tie to Buridan's ass.
- **Gary Klein** ("The Fiction of Optimization", in Gigerenzer & Selten (eds.), *Bounded Rationality: The Adaptive Toolbox*, MIT Press, [doi:10.7551/mitpress/1654.003.0009](https://doi.org/10.7551/mitpress/1654.003.0009)) — cited by Wikipedia for the optimisation regress. The DOI record (checked 2026-10-08) gives the title, container and publisher, print year 2002, but no author or pages; Wikipedia gives 2001 and pp. 111–112. The archive.org copies are lending-restricted; the chapter was not read.

## Framings and reframings

- **A case of Buridan's ass.** Burkeman links the two: "In the worst case, we end up choosing none of the potentially good options, but a definitively bad one – paralysis – instead. That is the fate of “Buridan’s ass”, the hypothetical donkey, positioned equidistantly between hay and water, that is hungry and thirsty in equal measure and stays rooted to the spot, thus starving to death." (2018). Wikipedia's article lists [Buridan's ass](buridans-ass.md) under "See also" (rev. 1329161308), and the list's "Decision theory" section is illustrated with the caption "Buridan's ass, unable to choose between two equally good options" (rev. 1376699902).
  *Structural note (this implant):* Buridan's case is put with exactly equal goods; Minsky's sentence is comparative in form (it begins "The more equally attractive two alternatives seem"), so it is not restricted to exact equality.
- **A question about style and fashion.** In Minsky the paradox sits in a section on fashion; he gives "Predictability: It makes no difference whether a single car drives on the left or on the right. But it makes all the difference when there are many cars! Societies need rules that make no sense for individuals." (p. 52) as one of the practical reasons for choosing by convention.
- **A problem of bounded deliberation.** The Wikipedia/Klein framing above places it among problems about the cost of optimising.
- **Related entries named by Wikipedia** (rev. 1329161308, "See also"; no reason given there): Decision theory, Cybernetics, Law of triviality (bicycle shedding), Tyranny of small decisions, and "What the Tortoise Said to Achilles" (see [the tortoise and Achilles](tortoise-and-achilles.md)).

Not in the excerpts held: Klein's chapter at first hand; any text by Fredkin;
any experimental study tying the paradox to research on choice difficulty or
near-indifference — none of the sources read cites one, so no empirical
findings are reported here. Search results from video and AI-generated
encyclopedia sites were not used.

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — Minsky's name for the observation; see *On the label* above.
- [Validity](../vocabulary/validity.md) — the propositional check above.
- [Dilemma](../vocabulary/dilemma.md) — the two-option choice.
- [Classical logic](../methods/classical-logic.md) — the logic of the check.
- *Expected utility* (Lombrozo; Burkeman, "what economists call your “expected utility”"), *value of information* and *instrumental rationality* (Wikipedia), *regret* (Lombrozo) — open work in [vocabulary](../vocabulary/index.md).
