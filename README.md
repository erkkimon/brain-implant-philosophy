# Philosophy Brain Implant for brainpick

**Philosophy skills and a cited knowledge graph for AI agents** — Claude
Code, Codex, OpenCode, Cursor, Gemini CLI, Copilot, or any agent that can
read a folder of markdown. Mount it and your agent stops reciting
philosophy from training-data memory and starts reasoning from receipts:
every claim carries its source, every position has its strongest case for
and against, and every persuasion technique and cognitive bias is catalogued
with who says what about it.

It is a **brain implant**: a shared, version-controlled half of a brain that
an agent plugs in beside its own memory (its *cortex*). Clone it and point
your agent at it, and you have a philosophy skill pack. Install
[brainpick](https://github.com/benquemax/brainpick) and register it as an
implant, and the same files become a searchable, link-walkable graph your
agent can query in the middle of any task. Both paths are below.

> Pull requests are welcome, including from agents. This is a public,
> CC BY-SA knowledge base; the rules it follows are machine-checked on
> every commit.

## Skills included

Each skill is a procedure your agent follows, with the deterministic tools
it drives. They form a dependency tree; the agent reads the one that
matches before it improvises.

| Skill | What it does |
| --- | --- |
| [Analyse an argument](_implant/skills/analyse-an-argument.md) | Reconstructs any argument into numbered premises and a conclusion, names its form, checks validity with a truth-table tool (`logic.py`) instead of intuition, and finds the counterexample when it is invalid. |
| [Steelman a position](_implant/skills/steelman-a-position.md) | Builds a position's strongest form from its cited proponents and passes it through the ideological Turing test — would an adherent sign it? |
| [Compare thinkers](_implant/skills/compare-thinkers.md) | Puts any thinkers from any era or tradition on the same problem page — Hume and Parfit on personal identity, Nāgārjuna and Wittgenstein on the limits of language — so the comparison is structural, not impressionistic. |
| [Spot persuasion and bias](_implant/skills/spot-persuasion-and-bias.md) | Produces a systematic, cited inventory of the persuasion techniques and cognitive biases in a text — with the replication record of each bias and every theory's classification of each technique — instead of "this looks like an appeal to emotion". |
| [Write persuasively](_implant/skills/write-persuasively.md) | Asks the user which persuasion techniques are allowed, writes with only those, and annotates where each was used, so the persuasion is chosen and auditable. |
| [Debate](_implant/skills/debate.md) | Sparring partner, hole-poker, or search for the most defensible position; the user chooses the format and how dirty the agent may fight, and every move is disclosed at the end. |
| [Write a page](_implant/skills/write-a-page.md) | The one authoring procedure for contributing to the graph: admission rule, claim kinds, receipts, neutrality lint, review checklist. |
| [Using the brain implant](_implant/skills/using-the-brain-implant.md) | How to read and write an implant: consult before answering from memory, ground every claim, keep opinions in the cortex. |

Credences — turning "probably" into a stated, replayable Bayesian model —
come from the companion
[cognitive-tools brain implant](https://github.com/erkkimon/brain-implant-cognitive-tools),
which is meant to be mounted alongside this one. This implant supplies the
factors, base rates and bias pages that make such a model educated; it has
no probability machinery of its own.

## What the knowledge graph holds

`_implant/knowledge/` is problem-centric: a **problem** page is the room in
which every thinker who addressed the question is listed with the position
they took and where they took it. Around the problems sit **positions**
(each with a case for and a case against that each side would sign),
**arguments** (reconstructed, validity-checked), **thinkers**, **works**,
**schools**, **persuasion techniques**, **cognitive biases**, a
**vocabulary** that separates descriptive from normative definitions, and
**methods**. Every tradition and period enters under the same rule.

The benchmark is Wikipedia — on neutrality, amount and quality — with each
of the three made checkable:

- **Neutrality, including selection.** The implant proves that a named
  thinker, school or text said something and never says in its own voice
  that it is true, false, fallacious, fringe or settled; a lint catches the
  words that carry such verdicts before every commit. Admission is a
  mechanical rule — a named proponent in a citable published place — never
  an editor's judgement of prominence.
- **Quality.** Every claim carries its receipt at the sentence: primary
  texts by canonical locator (Stephanus, Bekker, A/B page, chapter and
  verse), articles by DOI, reference works pinned to an archive edition,
  empirical findings with their evidence grade and replication record.
- **Amount.** Coverage is counted against Wikipedia's own lists, so "more"
  is a number and not an impression.

The implant does not tell you what is true — nobody knows, including its
authors. It gives your agent the tools to find out. The ten givens it stands
on are in [`_implant/vision/manifest.md`](_implant/vision/manifest.md).

## Quick start

### Option A — clone it and point your agent at it

```bash
git clone https://github.com/erkkimon/brain-implant-philosophy
```

Tell your agent to read `_implant/skills/index.md` first, then the skill it
needs. The skills are plain markdown with YAML frontmatter; the tools are
standard-library Python 3.10+ with no network access:

```bash
cd _implant/skills/tools
python3 selftest.py
python3 logic.py check --premises "P -> Q" "~Q" --conclusion "~P"   # VALID, modus tollens
python3 neutrality-lint.py ../../knowledge                          # verdicts without owners
```

This works. It also leaves most of the value on the table, because an agent
reading a folder finds only what it thinks to open.

### Option B — mount it as a brain implant with brainpick

[brainpick](https://github.com/benquemax/brainpick) compiles a folder like
this one into a link graph, a keyword index and a vector index, and exposes
them to your agent as MCP tools: `brain_overview`, `brain_search`,
`brain_read`, `brain_neighbors`. The agent asks "what does the implant hold
on the problem of induction" and gets the problem page, its neighbours and
the skills that apply — in one call, mid-task, without knowing the file
layout. Skills are listed first and boosted in search, so the right
procedure reaches the agent before it decides anything. Several implants
and the agent's own brain federate into one address space.

```bash
uv tool install "brainpick[vectors]"      # or: pipx install "brainpick[vectors]"
git clone https://github.com/erkkimon/brain-implant-philosophy && cd brain-implant-philosophy
brainpick compile --root .                # builds the graph and indexes
brainpick register "$PWD" --implant --alias philosophy
brainpick integrate claude-code           # or: opencode | dsh | agents-md
```

`brainpick integrate` writes the Agent Skill into your harness and prints
the MCP snippet to paste. Mount the companion implant the same way:

```bash
git clone https://github.com/erkkimon/brain-implant-cognitive-tools
brainpick register "$PWD/brain-implant-cognitive-tools" --implant --alias cognitive-tools
```

Without an agent, the same graph is on the command line:

```bash
brainpick overview --root .
brainpick search --root . "appeal to authority"
brainpick read --root . knowledge/biases/anchoring.md
brainpick neighbors --root . knowledge/persuasion/appeal-to-authority.md
```

If `brainpick` is not found after installing, it is in `~/.local/bin`.
brainpick **≥ 0.7.0** is required (brain format 3 — the conventions that
make this repository what it is are invisible to older engines);
**≥ 0.8.1** to serve it with `brainpick serve`. No install at all:
`uvx brainpick overview --root .`

## How the repository is organised

`_implant/` is the bundle. Its folders are memory types, one job each:

| Folder | Holds |
| --- | --- |
| `skills/` | The procedures above and the tools they drive (`skills/tools/`) |
| `knowledge/` | The graph: `problems/ positions/ arguments/ thinkers/ works/ schools/ persuasion/ biases/ vocabulary/ methods/`, each with its page template in its index |
| `conventions/` | Standing rules: reporting-not-endorsing, selection, words-as-contracts, claim grades, receipts, evidence before authority, publication, excerpts |
| `vision/` | The manifest: the givens, what follows from each, the benchmark |
| `journals/` | What happened, one file per day |
| `plans/` | Decided work |
| `todo/` | The live work queue and the coverage ledger |
| `raw/` | Citation excerpts, never copies, excluded from search results |

Read `conventions/` first — a rule constrains what every other read is for —
then `skills/`, then `knowledge/`.

## Contract

This repository is governed by a [henxels](https://pypi.org/project/henxels/)
contract — machine-checked rules in `henxels.yaml`, digested for agents into
`AGENTS.md`. It runs on commit: the implant must compile fresh, every link
must land, every page must carry its grounding, the neutrality lint must be
clean, the tools must pass their self-test. Install it before contributing:

```bash
uv tool install henxels && henxels init
henxels check --all
```

## Contributing

Contributions arrive as pull requests. Before writing a page, read
[`_implant/skills/write-a-page.md`](_implant/skills/write-a-page.md); it is
the whole procedure, ending in a review checklist. In one line: admitted by
the stated rule, every sentence one of the six claim kinds with what that
kind needs, every receipt verified to resolve, lint clean, case-for and
case-against each passing the ideological Turing test, linked in and out.

There is no peer review here and no gatekeeping by standing. Logic is
evaluated by individuals; the admission test for a thought is that a
stranger can check it. Opinions — including the maintainers' — do not enter;
they belong to the reader.

## How the content is produced — and a disclaimer

All information in this repository is **distilled by AI agents** from the
cited sources, under the contract above, and reviewed by humans only to the
extent the maintainers and contributors have had time for. The contract
checks what can be checked mechanically — that links land, that citations
are present, that no verdict is uttered in the implant's own voice — but it
cannot check that a source was read correctly or that a quotation is
accurate. Errors of transcription, attribution and interpretation are
therefore possible on any page, and every receipt is there precisely so
that you can verify the claim yourself before relying on it.

The content is provided **as is**, without warranty of any kind, express or
implied. Nothing here is professional advice of any kind, and nothing here
is a statement of the maintainers' own views: the implant reports what named
sources have said, and any error in such a report is an error of the
implant, not a claim of the source. If you find one, open an issue or a pull
request.

## Licensing

Content is **CC BY-SA 4.0**; tooling and configuration are **MIT**. Quoted
material remains under its own rights and is held to the excerpt rule in
`_implant/conventions/raw-holds-excerpts-not-copies.md`. See `LICENSE`.
