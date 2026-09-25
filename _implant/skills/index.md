# Skills

Procedures an agent follows here — the most distilled, tested layer of the
implant. Each is `type: skill`; the dependency tree is in
[skilltree.md](skilltree.md) (generated — never edited by hand). Read the
[conventions](../conventions/index.md) first: a rule constrains what a
procedure is for.

Skills say *brain implant*, not *brain*: a brain is the agent's own cortex
plus the implants mounted beside it, and opinions go to the cortex
([Using the brain implant](using-the-brain-implant.md)).

## Reading and reasoning

* [Using the brain implant](using-the-brain-implant.md) — pull first, read
  most-distilled-first, distil upward, ground every claim, route opinions
  to the cortex.
* [Analyse an argument](analyse-an-argument.md) — reconstruct into premises
  and conclusion, check validity with the logic tool instead of by eye,
  separate validity from soundness, map onto the argument pages.
* [Steelman a position](steelman-a-position.md) — the strongest case for
  and against, from cited proponents and opponents, each checked by the
  ideological Turing test; name the exact divergence.
* [Compare thinkers](compare-thinkers.md) — problem-first, so classical and
  modern thinkers meet on the problem page; tabulate positions with
  locators; agreement and divergence as logic; published comparisons
  attributed.
* [Spot persuasion and bias](spot-persuasion-and-bias.md) — a systematic,
  cited inventory of the techniques a text uses and the biases it exhibits
  or exploits, with every classification attributed; no verdict.

## Persuading and practising — the user sets the limits

* [Write persuasively](write-persuasively.md) — present the technique
  menu, have the user choose what is allowed, write with only that,
  annotate every use, self-audit.
* [Debate](debate.md) — sparring, hole-poking, or a search for the most
  defensible position; the user chooses how dirty; every move logged and
  disclosed at the end.

## Authoring

* [Write a page](write-a-page.md) — the one procedure for every knowledge
  page: admission rule, template, six claim kinds, verified receipts,
  neutrality lint, graph links, coverage count.

## Credences

Probability lives in the shared **cognitive-tools implant**, mounted beside
this one: its *Estimate a credence* skill drives the Bayesian appraiser
that turns a gut feeling into a stated, replayable model. This implant
holds no probability machinery of its own (manifest G7) — it supplies the
factors, the base rates and the bias pages that make the model educated.

## Tools

Deterministic scripts the skills drive, in `tools/`: pure
standard-library Python, runnable by anyone who clones the repository,
each with a self-test.

* `logic.py` — propositional validity by truth table; names the schema,
  reports counterexamples, inconsistent premises and redundant premises.
* `neutrality-lint.py` — flags evaluative predicates in the implant's own
  voice; a hit is a verdict without an owner.
* `selftest.py` — checks both against known cases.
