---
type: article
about: concept
title: "The chainstore paradox: should an incumbent fight entry it would not fight at the last stage?"
description: "Selten's (1978) chain store game: backward induction says every entrant enters and the monopolist always acquiesces, while deterrence by early fighting looks better; Selten's limited-rationality reply, the reputation models of Kreps & Wilson and Milgrom & Roberts (1982), and the 'paradox of backward induction' as SEP reports it."
tags: [problem, paradox, decision-theory, game-theory, rationality]
timestamp: 2026-10-08T20:29:06Z
---

# The chainstore paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
sources graded as in [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Admitted from Wikipedia's List of paradoxes,
[revision 1376699902](https://en.wikipedia.org/w/index.php?title=List_of_paradoxes&oldid=1376699902),
section "Decision theory"
(excerpt: `raw/wikipedia-chainstore-paradox-rev-1314222503-and-list-entry.md`).
Sources for the map: Selten,
[1978](https://doi.org/10.1007/BF00131770), abstract only
(excerpt and records: `raw/selten-1978-chain-store-paradox-abstract-and-records.md`);
Kreps & Wilson, [1982](https://doi.org/10.1016/0022-0531(82)90030-8)
(excerpt: `raw/kreps-wilson-1982-reputation-and-imperfect-information.md`);
Ross, [SEP Fall 2024 "Game Theory"](https://plato.stanford.edu/archives/fall2024/entries/game-theory/)
§§2.3, 2.8 (excerpt: `raw/sep-game-theory-fall-2024-paradox-of-backward-induction.md`);
Pacuit & Roy, [SEP Fall 2024 "Epistemic Foundations of Game Theory"](https://plato.stanford.edu/archives/fall2024/entries/epistemic-game/)
§4.2 (excerpt: `raw/sep-epistemic-game-fall-2024-backward-induction-aumann-stalnaker.md`);
Wikipedia, ["Chainstore paradox"](https://en.wikipedia.org/w/index.php?title=Chainstore_paradox&oldid=1314222503),
rev. 1314222503, used as a pointer to sources and for its statement of the game.

## The question

Wikipedia's list entry: "Chainstore paradox: Even those who know better play the so-called chain store game in an irrational manner." (rev. 1376699902).
Selten's abstract: "The chain store game is a simple game in extensive form which produces an inconsistency between game theoretical reasoning and plausible human behavior. Well-informed players must be expected to disobey game theoretical recommendations." (1978, abstract).

**The stage game**, as Kreps & Wilson restate Selten's: "The entrant moves first, electing either to enter or to stay out. Following entry, the monopolist chooses either to acquiesce or to fight." (1982, p. 254).
Their Fig. 1, "Selten's chain-store game" (p. 255):

| Outcome | Entrant | Monopolist |
|---|---|---|
| entrant stays out | 0 | *a* |
| enters, monopolist acquiesces | *b* | 0 |
| enters, monopolist fights | *b* − 1 | −1 |

with *a* > 1 and 0 < *b* < 1 (p. 255). The game is then played by one
monopolist against *N* successive entrants, each seeing the earlier moves
(p. 255). Wikipedia's 20-town version pays 1/5 (out), 2/2 (cooperative),
0/0 (aggressive) (rev. 1314222503), not checked against Selten's text.

**The induction argument**, in Kreps & Wilson's statement of Selten's: "In the last stage the monopolist will not fight because there are no later entrants to demonstrate for." (p. 255);
"This logic can be repeated, unraveling from the back: In each stage entry and acquiescence will occur. To be precise, this is the unique perfect Nash equilibrium of the game; cf. Selten [22, 23, 24]." (p. 255).

**Logic check (this implant, 2026-10-08; logic, not a position).** For
two stages, with F*n* for: the monopolist fights at stage *n*; E*n* for:
entrant *n* enters (stage 2 last): premises ¬F2; ¬F2 → E2;
¬F2 → ¬F1 (fighting at stage 1 cannot alter stage 2, Kreps & Wilson's
"no later entrants to demonstrate for", applied one step back);
¬F1 → E1. Conclusion E1 ∧ E2 ∧ ¬F1 ∧ ¬F2. `logic.py check` output:
"VALID". The dispute below is over the premises, chiefly the third,
not over the inference.

**The deterrence intuition.** Kreps & Wilson trace it to Scherer's
"demonstration effect" of price cutting (Scherer 1980, p. 338, quoted
p. 253), and write: "The intuitive appeal of this line of reasoning has, however, been called the “chain-store paradox” by Selten [24], who demonstrates that it is not supported in a straightforward game-theoretic model." (p. 253).
Wikipedia's arithmetic for its 20-town version: under induction "A receives a payoff of 40 (2×20) and each competitor receives 2."; under deterrence with the last three stages conceded, "Assuming all 17 are deterred, Player A receives 91 (17×5 + 2×3)." (rev. 1314222503).
**Arithmetic check (this implant, 2026-10-08; mathematics, not a
position):** 2 × 20 = 40; 17 × 5 + 3 × 2 = 91, on Wikipedia's payoffs.

**The label.** "Paradox" is Selten's own name (1978, title and abstract);
Kreps & Wilson report it as what Selten "called" it (p. 253). Wikipedia
adds: "The "deterrence strategy" is not a Subgame perfect equilibrium: It relies on the non-credible threat of responding to in with aggressive." (rev. 1314222503).

## Why it matters

- **Theory against observed reasoning.** Selten: "Well-informed players must be expected to disobey game theoretical recommendations." (1978, abstract).
- **Finite repetition generally.** Selten: "The chain store paradox throws new light on the well-known difficulties arising in connection with finite repetitions of the prisoners’ dilemma game." (abstract). Kreps & Wilson: "But this phenomenon is not observed in some formal game-theoretic analyses of finite games, such as Selten’s finitely repeated chain-store game or in the finitely repeated prisoners’ dilemma." (p. 253). See [the prisoner's dilemma](prisoners-dilemma.md), finitely repeated case.
- **Industrial organisation.** Kreps & Wilson's question is whether reputational effects in predatory pricing, which Scherer predicts, can be modelled: "Apparently, this model is inadequate to justify Scherer’s prediction that reputational effects will play a role." (p. 255).
- **Rationality and common knowledge.** Ross names a "paradox of backward induction" (SEP §2.8, below); Pacuit & Roy: "Aumann (1995) showed that this epistemic condition implies that the players will play according to the backward induction solution while Stalnaker (1998) argued that this is not necessarily true." (SEP §4.2). Neither SEP entry discusses the chain store game by name.

## Positions taken

Grouped by the move each makes (this page's grouping); not ranked.

- **Limited rationality (Selten 1978).** Selten's abstract: "Whereas these difficulties can be resolved by the assumption of secondary utilities arising in the course of playing the game, a similar approach to the chain store paradox is less satisfactory."
  And: "It is argued that the explanation of the paradox requires a limited rationality view of human decision behavior. For this purpose a three-level theory of decision making is developed, where decisions can be made on different levels of rationality." Wikipedia reports the levels: "Selten argues that individuals can make decisions of three levels: Routine, Imagination, and Reasoning." and "The final decision is made on the routine level and governs actual behavior." (rev. 1314222503).
- **Incomplete information; the paradox as an artefact of the model
  (Rosenthal 1981).** Not read here; Kreps & Wilson report his point: "The paradoxical result in Selten’s analysis is due to the complete and perfect information formulation that Selten uses. In a more realistic formulation of the game, the intuitive outcome will be predicted by the game-theoretic analysis." (p. 276).
  Rosenthal ([1981](https://doi.org/10.1016/0022-0531(81)90018-1))
  proposed a Decision Analysis treatment instead, which Macgregor (1979,
  mimeo) carried out (p. 276); Kreps & Wilson: "But, as Rosenthal notes, the weakness in this approach is the ad hoc assessment of entrants’ behavior." (p. 276).
- **Reputation under incomplete information (Kreps & Wilson 1982;
  Milgrom & Roberts 1982).** Kreps & Wilson: "We reexamine Selten’s model, adding to it a “small” amount of imperfect (or incomplete) information about players’ payoffs, and we find that this addition is sufficient to give rise to the “reputation effect” that one intuitively expects." (p. 253);
  "If rivals perceive the slightest chance that an incumbent firm might enjoy “rapacious responses,” then the incumbent’s optimal strategy is to employ such behavior against its rivals in all, except possibly the last few, in a long string of encounters." (p. 254).
  Milgrom & Roberts, "Predation, reputation, and entry deterrence"
  ([1982](https://doi.org/10.1016/0022-0531(82)90031-X)), is their
  companion paper; not read here (only an image scan was found). Kreps &
  Wilson describe it as exploring the same issues "in models that are
  richer in institutional detail" (p. 254) and as having
  "continua of types of monopolists" (p. 276).
  - *Caveats, by the authors themselves:* "The reader may object that in order to obtain the reputation effect, we have loaded the deck." (p. 276); "The power of reputation seems to be positively related to its fragility." (p. 276);
    "If this is so, then the game-theoretic analysis of this type of game comes down eventually to how one picks the initial incomplete information. And nothing in the theory of games will help one to do this." (p. 276);
    "But we have made ad hoc assumptions about their information, and we have found that small changes in those assumptions greatly influence the play of the game." (p. 277).
- **Trembling hands (Selten 1975), for the general backward-induction
  puzzle.** Ross: "A standard way around this paradox in the literature is to invoke the so-called ‘trembling hand’ due to Selten (1975)." (SEP §2.8; [Selten 1975](https://doi.org/10.1007/BF01766400)).
  Ross applies this to his own example game, not to the chain store.

## Arguments in play

(none recorded as separate argument pages yet); both arguments are in The question.

## Thinkers who addressed it

- **F. M. Scherer** (1980, p. 338) — the informal demonstration effect (Kreps & Wilson, p. 253).
- **Reinhard Selten** (1974 working paper; [1978](https://doi.org/10.1007/BF00131770);
  reprinted [1988](https://doi.org/10.1007/978-94-015-7774-8_2)) — the
  game, the name, the three-level limited-rationality theory.
- **M. Macgregor** (1979, mimeo), **Robert W. Rosenthal** (1981) — decision analysis; complete information blamed (as reported, p. 276).
- **David Kreps & Robert Wilson**, **Paul Milgrom & John Roberts** (1982) — reputation models (the latter not read).
- **Robert Aumann** (1995), **Robert Stalnaker** (1998), **Herbert Gintis** (2009) — backward induction and common knowledge (Pacuit & Roy §4.2; Ross §2.8).

## Framings and reframings

- **One case of the "paradox of backward induction".** Ross (SEP §2.8), on his own example: "Both players use backward induction to solve the game; backward induction requires that Player I know that Player II knows that Player I is economically rational; but Player II can solve the game only by using a backward induction argument that takes as a premise the failure of Player I to behave in accordance with economic rationality. This is the paradox of backward induction."
  That the chain store is an instance is this page's structural note
  (manifest G4), resting on Kreps & Wilson's naming of the chain store
  and the finitely repeated PD together (p. 253); Ross does not say so.
- **Knowledge, not rationality, as the premise at issue.** "Gintis (2009a) points out that the apparent paradox does not arise merely from our supposing that both players are economically rational." (Ross §2.8). Pacuit & Roy locate the Aumann–Stalnaker difference in belief revision: "The crucial difference between these two results is the way in which they model the players’ belief change upon (hypothetically) learning that an opponent has deviated from the backward induction path." (§4.2).
- **A problem only for normative readings.** Ross's assessment: "The paradox of backward induction, like the puzzles raised by equilibrium refinement, is mainly a problem for those who view game theory as contributing to a normative theory of rationality (specifically, as contributing to that larger theory the theory of strategic rationality)."
  And his: "The paradox of backward induction is one of a family of paradoxes that arise if one builds possession and use of literally complete information into a concept of rationality." (§2.8).
- **Kin to the surprise examination?** Wikipedia's article lists the
  unexpected hanging paradox under "See also" (rev. 1314222503). Chow
  (1998, §4) reports the suggestion that the surprise exam "may be related
  to the iterated prisoner’s dilemma" and judges the two distinct (see
  [the surprise examination paradox](surprise-examination-paradox.md));
  no source read here compares the surprise exam with the chain store
  directly.

Left out, not fetched: Ordeshook (1992, pp. 247–249); experiments on chain-store play.

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — Selten's label; see The question.
- [Validity](../vocabulary/validity.md) — the induction argument is
  valid as checked above; its premises are what the positions dispute.
- Backward induction, subgame perfection, credible threat, reputation, common knowledge — open work in [vocabulary](../vocabulary/index.md).

Related problems: [the prisoner's dilemma](prisoners-dilemma.md) (finitely
repeated; Selten 1978, Kreps & Wilson 1982),
[the surprise examination paradox](surprise-examination-paradox.md)
(listed by Wikipedia's article; via the iterated PD, Chow 1998). Branch: [Problems](./index.md).
