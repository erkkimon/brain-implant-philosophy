# brain-implant-philosophy

A **brainpick brain implant** for philosophy — a public, machine-navigable
knowledge graph that an AI agent mounts beside its own memory to reason
about philosophy with receipts instead of recollection. Problems, positions,
arguments, thinkers, works, schools, persuasion techniques, cognitive biases,
a vocabulary contract and methods, from every tradition and period, on one
playground.

It is built against one benchmark: **Wikipedia — on neutrality, amount and
quality of information — with each of the three made checkable.**

- **Neutrality, including selection.** The implant proves that a named
  thinker, school or text said something and never says, in its own voice,
  that it is true, false, fallacious, fringe or settled. A lint catches the
  words that carry such verdicts before every commit. And because what gets
  *told* biases as much as how it is told, admission is a mechanical rule —
  a named proponent in a citable published place — never an editor's
  judgement of prominence. Every position page carries a case for and a
  case against that each side would sign.
- **Quality.** Every claim carries its receipt at the sentence: primary
  texts by canonical locator (Stephanus, Bekker, A/B page, chapter and
  verse), articles by DOI, reference works pinned to an archive edition,
  empirical findings with their evidence grade and replication record.
- **Amount.** Coverage is counted against Wikipedia's own lists, so "more"
  is a number and not an impression.

The implant does not tell you what is true — nobody knows, including its
authors. It gives you the tools to find out: argument reconstruction with a
validity checker, symmetric steelmanning, thinker comparison that meets on
the problem page, a systematic and cited inventory of persuasion techniques
and biases, a persuasive-writing skill where *you* choose which techniques
are allowed, and a debate skill where you choose how dirty the opponent may
fight — and it discloses every move at the end.

The ten givens it stands on — what it assumes, what it refuses to assume —
are in `_brain/vision/manifest.md`. Everything else should follow from them.

**Pull requests are welcome**, including from agents. See *Contributing*.

---

## Using this with an agent

### If brainpick is already installed

```bash
git clone <this-repo> && cd brain-implant-philosophy
brainpick compile --root .          # --root is where brainpick.toml lives
brainpick overview --root .         # start here
```

Then `brainpick search`, `brainpick read`, `brainpick neighbors`. To mount it
as an implant in an agent harness:

```bash
brainpick register "$PWD" --implant --alias philosophy
brainpick integrate                 # writes harness config (Claude Code, opencode, …)
```

Credences — turning "probably" into a stated, replayable Bayesian model — are
driven by the shared **cognitive-tools implant**, mounted beside this one:

```bash
git clone https://github.com/erkkimon/brain-implant-cognitive-tools
brainpick register "$PWD/brain-implant-cognitive-tools" --implant --alias cognitive-tools
```

This implant holds no probability machinery of its own; it supplies the
factors, base rates and bias pages that make a model educated.

### If brainpick is not installed

brainpick is a Python CLI on PyPI. Install the `[vectors]` extra, otherwise
the vector tier is silently off and search degrades to keyword only:

```bash
uv tool install "brainpick[vectors]"      # recommended
# or: pipx install "brainpick[vectors]"
```

If `brainpick` is not found afterwards it is almost certainly in
`~/.local/bin`. Without installing anything: `uvx brainpick overview --root .`

Source and documentation: <https://github.com/benquemax/brainpick>

**brainpick >= 0.7.0 is required** (brain format 3 — `type: convention`
pages are invisible to older engines, and the conventions are the point of
this repository); **>= 0.8.1 to serve it** with `brainpick serve`.

## Running the tools without an agent

Pure standard-library Python 3.10+; nothing reaches the network.

```bash
cd _brain/skills/tools
python3 selftest.py
python3 logic.py check --premises "P -> Q" "~Q" --conclusion "~P"   # VALID, modus tollens
python3 neutrality-lint.py ../../knowledge                          # verdicts without owners
```

## How this repository is organised

`_brain/` is the bundle. Its folders are memory types, one job each:

| Folder | Holds |
| --- | --- |
| `vision/` | The manifest: the givens, what follows from each, the benchmark |
| `conventions/` | Standing rules: reporting-not-endorsing, selection, words-as-contracts, claim grades, receipts, evidence before authority, publication, excerpts |
| `skills/` | Procedures an agent follows — analyse, steelman, compare, spot, write persuasively, debate, write a page — and the tools they drive (`skills/tools/`) |
| `knowledge/` | The graph: `problems/ positions/ arguments/ thinkers/ works/ schools/ persuasion/ biases/ vocabulary/ methods/`, each with its page template in its index |
| `journals/` | What happened, one file per day; the founding decisions are the first entry |
| `plans/` | Decided work |
| `todo/` | The live work queue and the coverage ledger |
| `raw/` | Citation excerpts, never copies, excluded from search results |

Read `conventions/` first — a rule constrains what every other read is for —
then `skills/`, then `knowledge/`.

The graph is **problem-centric**: a problem page is the room in which every
thinker who addressed the question is listed with the position they took and
where they took it, so Nyāya and Gettier, Hume and Parfit, meet on the page
rather than in an agent's memory.

## Contract

This repository is governed by a [henxels](https://pypi.org/project/henxels/)
contract — machine-checked rules in `henxels.yaml`, digested for agents into
`AGENTS.md`. It runs on commit: the brain must compile fresh, every link must
land, every page must carry its grounding, the neutrality lint must be clean,
the tools must pass their self-test. Install it before contributing:

```bash
uv tool install henxels && henxels init
henxels check --all
```

## Contributing

Contributions arrive as pull requests. Before writing a page, read
`_brain/skills/write-a-page.md`; it is the whole procedure, ending in a
review checklist. In one line: admitted by the stated rule, every sentence
one of the six claim kinds with what that kind needs, every receipt verified
to resolve, lint clean, case-for and case-against each passing the
ideological Turing test, linked in and out.

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
`_brain/conventions/raw-holds-excerpts-not-copies.md`. See `LICENSE`.
