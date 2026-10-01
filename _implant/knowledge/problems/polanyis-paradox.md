---
type: article
about: concept
title: "Polanyi's paradox (tacit knowledge)"
description: "Can we know more than we can tell, and if so, can a task whose rules nobody can state be automated? Polanyi's 1966 sentence, Autor's 2014 naming of 'Polanyi's paradox' for computerisation, Ryle's knowing-how, the intellectualist debate on articulability (Pavese, SEP), and the machine-learning responses (Autor, Susskind), with their owners."
tags: [problem, paradox, epistemology, philosophy-of-mind, economics]
timestamp: 2026-10-01T19:53:21Z
---

# Polanyi's paradox (tacit knowledge)

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Polanyi's *The Tacit Dimension* (1966) was not read for this page; its
sentence is quoted as Autor and Susskind quote it. Sources read: Autor,
[NBER w20485 (2014)](https://doi.org/10.3386/w20485) (excerpt:
`raw/autor-2014-polanyis-paradox-shape-of-employment-growth.md`); Autor,
[JEP 29(3), 2015](https://doi.org/10.1257/jep.29.3.3) (excerpt:
`raw/autor-2015-why-are-there-still-so-many-jobs-polanyis-paradox.md`);
Susskind, [Oxford Economics DP 825 (2017)](https://web.archive.org/web/20170626123455/https://www.economics.ox.ac.uk/materials/papers/15127/825-susskind-capabilities-of-machines.pdf)
(excerpt: `raw/susskind-2017-rethinking-capabilities-of-machines-polanyi.md`);
Ryle, *The Concept of Mind* (1949), ch. II §3 (excerpt:
`raw/ryle-1949-concept-of-mind-knowing-how-unformulated-rules.md`); Pavese,
[SEP Fall 2024 "Knowledge How"](https://plato.stanford.edu/archives/fall2024/entries/knowledge-how/)
(excerpt: `raw/sep-knowledge-how-fall-2024-ryle-and-articulability.md`);
three further SEP entries (excerpt: `raw/sep-fall-2024-tacit-knowledge-kuhn-collins-chomsky.md`).

## The question

Polanyi's sentence, as Autor quotes it: "In 1966, the philosopher Michael Polanyi observed, “We can know more than we can tell... The skill of a driver cannot be replaced by a thorough schooling in the theory of the motorcar; the knowledge I have of my own body differs altogether from the knowledge of its physiology.”" (2014, abstract).
Susskind gives the page numbers of *The Tacit Dimension* through Autor, Levy & Murnane (2003, p. 1283): "“We can know more than we can tell [p. 4] . . . The skill of a driver cannot be replaced by a thorough schooling in the theory of the motorcar;" (Susskind 2017, §2.2, p. 4).

Two questions are asked under the name, by different literatures:

- **Epistemological.** Is there knowledge that its possessor cannot put into words, and is knowing how to do something a different kind of knowledge from knowing that something is the case? Pavese frames the second as "is knowledge-how an altogether distinct kind of knowledge, different from knowledge-that?" (SEP, preamble). Term contract: [knowledge](../vocabulary/knowledge.md).
- **Economic and computational.** If programming is telling a machine the rules, can a task be automated when no one can state its rules? Autor: "Polanyi’s paradox—“we know more than we can tell”—presents a challenge for computerization because, if people understand how to perform a task only tacitly and cannot “tell” a computer how to perform the task, then seemingly programmers cannot automate the task—or so the thinking has gone." (2015, p. 24).

**Where the name comes from.** Autor, 2014: "I refer to this constraint as Polanyi’s paradox, following Michael Polanyi’s (1966) observation that, “We know more than we can tell.”" (p. 8). In 2015 he writes "I have referred to this constraint as Polanyi’s paradox, named after the economist, philosopher, and chemist who observed in 1966, “We know more than we can tell” (Polanyi 1966; Autor 2015)." (p. 11). Autor states the content of the paradox as "that our tacit knowledge of how the world works often exceeds our explicit understanding" (2014, abstract). The sentence is quoted in two wordings in Autor's own texts ("We can know" in the abstract, "We know" on p. 8); Polanyi's text was not checked.

**Propositional check (this implant, 2026-10-01; logic, not a position).**
Why "paradox"? Let *k* be *we know how to do it* and *t* *we can tell how*.
`logic.py check --premises "k & ~t" --conclusion "k & ~k"` returns `INVALID`
with counterexample row `k=T, t=F`: knowing without telling does not entail a
contradiction in propositional logic. The tool treats *k* and *t* as
unanalysed atoms; whether knowledge requires the ability to tell is exactly
what the intellectualist debate below contests, and the tool does not decide it.

## Why it matters

- **Automation and employment.** Autor: "Following Polanyi’s observation, the tasks that have proved most vexing to automate are those demanding flexibility, judgment, and common sense—skills that we understand only tacitly." (2014, p. 8); "At a practical level, Polanyi’s paradox means that many familiar tasks, ranging from the quotidian to the sublime, cannot currently be computerized because we don’t know “the rules.”" (p. 8). His examples: breaking an egg over a bowl, identifying a bird species from a glimpse, writing a persuasive paragraph, developing a hypothesis (p. 8).
- **Task models in labour economics.** Susskind: "In Autor et al. (2003), the distinction between ‘routine’ and ‘non-routine’ tasks is based on the work of Michael Polanyi, a philosopher – in particular Polanyi (1966)." (§2.2, p. 4; [Autor, Levy & Murnane 2003](https://doi.org/10.1162/003355303322552801), not read).
- **Philosophy of mind and epistemology.** The knowledge-how debate concerns, in Pavese's words, "a psychological question: what kind of psychological state is knowledge-how?" (SEP, preamble); the articulability argument (SEP §7.3, below) turns on whether some knowledge cannot be verbalised.
- **Philosophy of science.** Nickles: Kuhn's "emphasis on skilled practice may have been influenced by Michael Polanyi’s Personal Knowledge (1958), with its “tacit knowing” component, although Kuhn denied that he found Polanyi’s account appealing (see, e.g., Baltas et al., 2000, pp. 296f)." ([SEP "Scientific Revolutions"](https://plato.stanford.edu/archives/fall2024/entries/scientific-revolutions/), §3.3). Fidler & Wilcox report that "much of the knowledge that scientists require to execute experiments is tacit and “cannot be fully explicated or absolutely established” (Collins 1985: 73)." ([SEP "Reproducibility of Scientific Results"](https://plato.stanford.edu/archives/fall2024/entries/scientific-reproducibility/), §3.1).
- **Linguistics.** Bermúdez & Cahen: "It is a fundamental tenet of a broadly Chomskyan approach to syntax that speakers are credited with tacit knowledge of a grammar for their language and that this tacit knowledge is deployed in understanding spoken language." ([SEP "Nonconceptual Mental Content"](https://plato.stanford.edu/archives/fall2024/entries/content-nonconceptual/), §4.2).

## Positions taken

No source read groups positions on Polanyi's paradox as such. Two groupings
exist in the sources: Pavese's intellectualism vs. anti-intellectualism
about knowledge-how (SEP), and, for automation, Autor's two paths and
Susskind's two explanations. They are listed in that order; none is ranked here.

**On whether knowing how is knowing that (Pavese, SEP "Knowledge How").**

- **Anti-intellectualism (Ryle 1949).** Pavese: "Ryle instead advocated an “anti-intellectualist” view of knowledge-how according to which knowledge-how and knowledge-that are distinct kinds of knowledge, and manifestations of knowledge-how are not necessarily manifestations of knowledge-that. This anti-intellectualism has been the received view among philosophers for a long time." (preamble). Ryle's own words: "First, there are many classes of performances in which intelligence is displayed, but the rules or criteria of which are unformulated." (1949, p. 30); of the wit, "He knows how to make good jokes and how to detect bad ones, but he cannot tell us or himself any recipes for them." (p. 30); "Efficient practice precedes the theory of it; methodologies presuppose the application of the methods, of the critical investigation of which they are the products." (p. 30).
- **Anti-intellectualism from articulability (Schiffer 2002; Devitt 2011; Adams 2009; Wallis 2008).** Pavese: "Opponents of intellectualism often uses C3 in a novel argument against intellectualism: if propositional knowledge has to be verbalizable, then knowledge-how cannot be propositional knowledge, for often subjects know how to perform tasks even though they cannot explain how they do it (Schiffer 2002; Devitt 2011; Adams 2009; Wallis 2008)." (§7.3; [Schiffer 2002](https://doi.org/10.2307/3655616)).
- **Intellectualism (Stanley & Williamson 2001; Stanley 2011b).** "According to orthodox intellectualism, knowledge-how is a species of propositional knowledge." (§8.1); "Strong intellectualism (SI): For an action Φ, knowing how to Φ consists in knowing some proposition p." (§1.1; [Stanley & Williamson 2001](https://doi.org/10.2307/2678403)). On articulability: "Stanley (2011b: 161) points out that there is a sense in which knowledge-how is always verbalizable." (§7.3), by demonstratives such as a boxer's "This is the way I fight against a southpaw" (§7.3). A second intellectualist reply: "practical concepts for tasks differ from “semantic” concepts for the same tasks precisely in that, even if propositional, they are not necessarily verbalizable." (§7.3).

**On whether the paradox blocks automation (Autor 2014, 2015; Susskind 2017).**

- **A binding constraint (Autor 2014, 2015).** "engineers cannot program a computer to simulate a process that they (or the scientific community at large) do not explicitly understand." (2014, p. 8). Autor's assessment of the outlook: "Is Polanyi’s paradox soon to be at least mostly overcome, in the sense that the vast majority of tasks will soon be automated?8 My reading of the evidence suggests otherwise." (2015, p. 23).
- **Circumventing it by environmental control (reported by Autor).** "The first path circumvents Polanyi’s paradox by regularizing the environment, so that comparatively inflexible machines can function semi-autonomously." (2015, p. 23).
- **Inverting it by machine learning (reported by Autor).** "The second approach inverts Polanyi’s paradox: rather than teach machines rules that we do not understand, engineers develop machines that attempt to infer tacit rules from context, abundant data, and applied statistics." (2015, p. 23). Autor reports both expectations: "Some researchers expect that as computing power rises and training databases grow, the brute force machine learning approach will approach or exceed human capabilities. Others suspect that machine learning will only ever “get it right” on average while missing many of the most important and informative exceptions." (2014, p. 36).
- **Machines need not follow human rules (Susskind 2017).** "The ALM hypothesis has a clear implication – machines cannot perform ‘non-routine’ tasks. Yet in practice this no longer holds." (§2.3, p. 6). He separates two explanations: "The first explanation argues that new technologies allow us to uncover more of the tacit rules that human beings follow in performing ‘non-routine’ tasks; the second explanation argues that new technologies allow us to perform tasks with systems and machines that follow rules which do not need to reflect the rules that human beings follow at all, tacit or otherwise." (§2.5, p. 10). He finds the second point already in a footnote of Autor et al.: "a fallacy to assume that a computer must reproduce all of the functions of a human being to perform a task traditionally done by workers." (as quoted, §2.5, p. 10).

**Distribution, as reported.** Pavese calls Ryle's anti-intellectualism "the received view among philosophers for a long time" (preamble) and reports that "new versions of intellectualism and anti-intellectualism have been developed and argued for" in the last twenty years (preamble). No survey figure is recorded.

## Arguments in play

(none recorded as separate argument pages yet).

- **The articulability argument** against intellectualism (Pavese §7.3, quoted above). *Against it*, Pavese reports: "Moreover, it is not clear that the anti-intellectualist demand that propositional knowledge be always verbalizable is motivated. In fact, it seems to conflate knowing how to perform a task with knowing how to explain how the task is performed (cf. Fodor 1968: 634; Stalnaker 2012)." ([Fodor 1968](https://doi.org/10.2307/2024316)). *Against the demonstrative reply*, Pavese: "This reply assumes that ways to execute tasks are ostensible and as such can be picked up by a demonstrative. This does not need to be so: on any single occasion, one may only act on parts of a way." (§7.3).
- **The cognitive-science argument** (Pavese §7.1): the patient HM "tuned his motor skill to trace the outline of a five-pointed star based only on looking at reflection in a mirror. Since he could not store new memories, HM’s declarative knowledge of the means of performing the task did not change from one trial to the next. But his performance improved." Pavese reports the objection that HM's case supports a combination of procedural and declarative systems (Pavese 2013; Stanley & Krakauer 2013).
- **Ryle's regress** (1949, p. 30): "The crucial objection to the intellectualist legend is this. The consideration of propositions is itself an operation the execution of which can be more or less intelligent, less or more stupid." Pavese: "Exactly how to reconstruct Ryle’s argument is a matter of controversy (Stanley & Williamson 2001; Stanley 2011b; Bengson & Moffett 2011a; Cath 2013; Fantl 2011; Kremer 2020)." (§1).
- **The automation argument** (Autor 2015, p. 24, quoted in The question). **Propositional check (this implant, 2026-10-01; logic, not a position).** Let *t* be *people can tell how the task is done* and *c* *programmers can automate it*. With the bridge premise, `logic.py check --premises "~t -> ~c" "~t" --conclusion "~c"` returns `VALID` (`matches schema: modus ponens`); without it, `--premises "~t" --conclusion "~c"` returns `INVALID` with row `c=T, t=F`. The conclusion therefore rests on the conditional premise. Autor's "or so the thinking has gone" (2015, p. 24) and Susskind's second explanation (§2.5) are both addressed to that premise; the tool does not say which way it should be judged.

## Thinkers who addressed it

- **Michael Polanyi** — *Personal Knowledge* (1958), "tacit knowing" (per Nickles, SEP §3.3); *The Tacit Dimension* (1966; Doubleday per Autor's bibliography), pp. 4 and 20 per Autor, Levy & Murnane as quoted by Susskind. Also *The Logic of Tacit Inference*, *Philosophy* 41(155), 1966, pp. 1–18, [doi:10.1017/s0031819100066110](https://doi.org/10.1017/s0031819100066110) (bibliographic data only; not read).
- **Gilbert Ryle** (1949, ch. II; 1946, ["Knowing How and Knowing That"](https://doi.org/10.1093/aristotelian/46.1.1), *Proc. Aristotelian Society* 46: 1–16, bibliographic data only) — knowing how vs. knowing that.
- **Thomas Kuhn** — case-based tacit knowledge of exemplars (Nickles, SEP §5.1).
- **H. M. Collins** (1985) — tacit knowledge in experiment (Fidler & Wilcox, SEP §3.1).
- **Jerry Fodor** (1968), **Stephen Schiffer** (2002), **Jason Stanley** & **[Timothy Williamson](../thinkers/williamson.md)** (2001), **Stanley** (2011b), **Michael Devitt** (2011), **Robert Stalnaker** (2012), **Carlotta Pavese** (2013, 2021) — the knowledge-how debate as reported in SEP.
- **David Autor** (with Levy & Murnane 2003; 2014; 2015) — named the paradox and applied it to automation.
- **Daniel Susskind** (2017) — machines need not follow human rules.

## Framings and reframings

- **Polanyi's paradox vs. Moravec's paradox.** Autor: "I prefer the term Polanyi’s paradox to Moravec’s paradox because Polanyi’s observation also explains why high-level reasoning is straightforward to computerize and sensorimotor skills are not." (2014, p. 8, n. 10).
- **Machines that cannot tell either.** Autor: "A lovely irony of machine learning algorithms is that they also cannot “tell” programmers why they do what they do." (2014, p. 36, n. 38).
- **Tacit knowledge as what people struggle to articulate.** Susskind: "Put simply, ‘non-routine’ tasks are those that rely on what Polanyi called ‘tacit’ knowledge – knowledge that people struggle to articulate when called upon to do so." (§2.2, p. 5).
- **Executing vs. demonstrating.** Fidler & Wilcox report that "Franklin (1994) further claims that Collins conflates the difficulty in successfully executing experiments with the difficulty of demonstrating that experiments have been executed" (SEP §3.1).
- **Rules vs. exemplars.** Nickles: "In Carnap’s frameworks these were explicit systems of logical rules, whereas Kuhn’s account of normal science largely jettisoned rule-based knowledge in favor of a kind of case-based tacit knowledge, the cases being the concrete exemplars." (SEP §5.1).

Not in the excerpts held: the text of *The Tacit Dimension* and *Personal
Knowledge*, Polanyi 1966 in *Philosophy*, Ryle 1946, Autor, Levy & Murnane
2003 beyond Susskind's quotations, and any encyclopedia entry on Polanyi
(IEP returned no entry at the URLs tried); they are left out until read.

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — see the propositional check in The question.
- [Knowledge](../vocabulary/knowledge.md) — knowledge-how vs. knowledge-that (Pavese, SEP).
- [Validity](../vocabulary/validity.md) and [classical logic](../methods/classical-logic.md) — the two `logic.py` checks.
- *Tacit knowledge*, *knowledge-how*, *intellectualism*, *routine task* — open work in [vocabulary](../vocabulary/index.md).
