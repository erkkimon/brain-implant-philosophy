---
type: article
about: concept
title: "The paradox of fiction"
description: "How can we be moved by what we know does not exist? Radford's 1975 Anna Karenina paper and the inconsistent triad (emotion requires existence belief; readers lack it; readers are moved), with the responses on record — Radford's irrationalism, Walton's make-believe and quasi-emotions, the thought theory (Lamarque, Carroll, Smith), surrogate objects and beliefs, the illusion or suspension-of-disbelief view, counterpart theory — each with its owner and its objectors."
tags: [problem, paradox, aesthetics, philosophy-of-mind, philosophy-of-emotion]
timestamp: 2026-10-01T19:53:21Z
---

# The paradox of fiction

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Primary paper: Radford, "How Can We Be Moved by the Fate of Anna Karenina?",
*Aristotelian Society Supplementary Volume* 49 (1975), pp. 67–80 per the IEP
([doi:10.1093/aristoteliansupp/49.1.67](https://doi.org/10.1093/aristoteliansupp/49.1.67));
Walton, "Fearing Fictions", *Journal of Philosophy* 75 (1978), pp. 5–27
([doi:10.2307/2025831](https://doi.org/10.2307/2025831)); Lamarque, "How Can
We Fear and Pity Fictions?" (1981, [doi:10.1093/bjaesthetics/21.4.291](https://doi.org/10.1093/bjaesthetics/21.4.291))
(records: `raw/paradox-of-fiction-crossref-records.md`). None of these was
read here; they are reported through three maps: Schneider, [IEP "The Paradox of Fiction"](https://iep.utm.edu/fict-par/)
(excerpt: `raw/iep-paradox-of-fiction-schneider.md`); Kroon & Voltolini,
[SEP Fall 2024 "Fiction"](https://plato.stanford.edu/archives/fall2024/entries/fiction/)
§4 (excerpt: `raw/sep-fiction-fall-2024-paradox-of-fiction.md`); Liao & Gendler,
[SEP Fall 2024 "Imagination"](https://plato.stanford.edu/archives/fall2024/entries/imagination/),
supplement [§2](https://plato.stanford.edu/archives/fall2024/entries/imagination/puzzles.html)
(excerpt: `raw/sep-imagination-fall-2024-emotional-response-to-fictions.md`).
Quotations of Radford, Walton, Carroll and others are the encyclopedias' quotations, with their page numbers.

## The question

Schneider's opening question: "How is it that we can be moved by what we know does not exist, namely the situations of people in fictional stories?" (IEP, intro).
Kroon & Voltolini's case: "But the claim that we pity Anna Karenina is deeply puzzling: we know there is no Anna Karenina, and that it is only true in Tolstoy’s novel that Anna Karenina is suffering, so how can there be genuine pity for Anna?" (SEP "Fiction", intro).

Three formulations of the triad are on record:

- **IEP (Schneider).** "These premises are (1) that in order for us to be moved (to tears, to anger, to horror) by what we come to learn about various people and situations, we must believe that the people and situations in question really exist or existed; (2) that such “existence beliefs” are lacking when we knowingly engage with fictional texts; and (3) that fictional characters and situations do in fact seem capable of moving us at times." He calls it "an argument for the conclusion that our emotional response to fiction is irrational" containing "an inconsistent triad of premises, all of which seem initially plausible."
- **SEP "Fiction" (Kroon & Voltolini, §4).** "(A) People experience emotions for fictional objects and situations, knowing them to be fictional (B) People do not believe that fictional objects and situations exist (C) In order to experience an emotion for an object or situation, one must believe that it exists". "The question is how best to resolve the inconsistency among these claims; that is, which of (A)–(C) to give up so that consistency is restored, and why these and not others."
- **SEP "Imagination" (Liao & Gendler, supplement §2, after Friend 2016).** "Response Condition: People experience (genuine, ordinary) emotions toward fictional characters, situations, and events. Belief Condition: People do not believe in the existence of fictional characters, situations, and events. Coordination Condition: People do not experience (genuine, ordinary) emotions when they do not believe in the existence of the objects of emotion." They add: "Each of the three statements seem intuitively true, and yet they are jointly inconsistent."

**Two versions.** Liao & Gendler: "The descriptive version of the paradox (originating in Walton 1978) is concerned with the question of whether emotional responses to fictions are to be classified as the same kind of emotions we experience in other contexts. The normative version of the paradox (originating in Radford 1975) is concerned with the question of whether emotional responses to fictions are irrational or inappropriate."

**Propositional check (this implant, 2026-10-01; logic, not a position).**
Let *m* be *the reader is moved by the character* and *b* *the reader believes
the character exists*. Then (C)/(1) is *m* → *b*, (B)/(2) is ~*b*, (A)/(3) is *m*.
`logic.py check --premises "m -> b" "~b" "m" --conclusion "m & ~m"` outputs
`VALID` with `premises are jointly inconsistent — argument is vacuously valid`.
Each pair is consistent: dropping *m* gives `INVALID` with counterexample row
`b=F, m=F`; dropping ~*b* gives row `b=T, m=T`; dropping *m* → *b* gives row
`b=F, m=T`. So exactly one of the three must go for the rest to be jointly
satisfiable, which is the shape of the families below. The tool treats
*believes* and *is moved* as unanalysed atoms; whether *moved* in (A) means the
same as in (C) — the issue the quasi-emotion and thought theories raise — is
outside it.

## Why it matters

- **Theory of emotion.** Schneider: thought theories deny "the old and established thesis, traceable as far back as Aristotle and central to the so-called “Cognitive Theory of emotions,”" (IEP §4). Kroon & Voltolini: "(C) strikes many as a piece of articulated theory (the so-called cognitive theory of emotion) rather than a commonsense claim (cf. Gendler 2008)." (§4).
- **Imagination and cognitive architecture.** Liao & Gendler: "Given the central role of imagination in engagement with fictions, this paradox has been used to clarify the cognitive architectural connection between imagination and emotions." (supplement §2). "Gregory Currie and Ian Ravenscroft (2002) and Doggett and Egan (2012) argue the best explanation for people’s emotional responses toward non-existent fictional characters call for positing conative imagination." (§2.2).
- **Fictional entities.** On Walton's view, per Kroon & Voltolini: "No relational claims of this kind can be genuinely true for Walton, since he denies that there are any fictional characters." (§4).
- **Neighbouring paradoxes.** "The paradox of tragedy and the paradox of horror examine psychological and normative differences between affective responses prompted by imaginings versus affective responses by reality-directed attitudes." (Liao & Gendler §3.4). Kroon & Voltolini call the paradox of fiction "a relative newcomer to the set of problems that involve our engagement with works of fiction" (§5).
- **Volume of discussion, as reported.** Schneider: "To date, three basic strategies for resolving the paradox in question have turned up again and again in the philosophical literature, each one appearing in a variety of different forms (though it should be noted, other, more idiosyncratic solutions can also be found)." (IEP §1).

## Positions taken

Groupings on record: the IEP's three strategies (pretend, thought, illusion) plus Radford's own; Kroon & Voltolini's classification, which they say "follows Levinson 1997", by which member of (A)–(C) is given up. They are listed below in the order: deny none, deny (A)/(3), deny (C)/(1), deny (B)/(2); the order is the triad's, not a ranking.

- **Irrationalism (Radford 1975, 1977).** Radford holds that our ability to respond emotionally to fictional characters and events is "“irrational, incoherent, and inconsistent” (p. 75)" (as quoted by Schneider, IEP §1, and by Kroon & Voltolini §4). His case for premise (1): "“It would seem that I can only be moved by someone’s plight if I believe that something terrible has happened to him. If I do not believe that he has not and is not suffering or whatever, I cannot grieve or be moved to tears” (p. 68)." Kroon & Voltolini's summary: "They regard (C) as a normative constraint on rational agents, but their actual behavior and beliefs, as described in (A) and (B), show that they fail to conform to this constraint." Radford in 1977, per the IEP: "our response to the appearance of the monster is a brute one that is at odds with and overrides our knowledge of what he is" (p. 210).
  *Against:* Schneider: "It is interesting to note that while virtually all of those writing on this subject credit Radford with initiating the current debate, none of them have adopted his view as their own." (IEP §1). Kroon & Voltolini: "Dissatisfaction with Radford’s account resulted in numerous publications that have kept discussion of the problem alive." On the normative version, Liao & Gendler report: "Tamar Szabó Gendler and Karson Kovakovich (2005) argue that emotions in response to the merely imagined are essential to rational decision making; so, emotional response to fictions might be instrumentally or evolutionarily rational."
- **Make-believe / pretend theory (Walton 1978, 1990, 1997; see also Currie 1990).** Schneider: "Pretend theorists, most notably Kendall Walton, in effect deny premise (3), arguing that it is not literally true that we fear horror film monsters or feel sad for the tragic heroes of Greek drama." Walton's premise: "“It seems a principle of common sense, one which ought not to be abandoned if there is any reasonable alternative, that fear must be accompanied by, or must involve, a belief that one is in danger” (1978, pp. 6-7)." His example: "“Charles believes (he knows) that make-believedly the green slime [on the screen] is bearing down on him and he is in danger of being destroyed by it. His quasi-fear results from this belief” (p. 14)." Liao & Gendler: quasi-emotions "differ from genuine emotions in their source (they are generated by beliefs about what is fictionally rather than actually true), and, typically, in their behavioral consequences (though we may pity Ophelia, we make no effort to console her in her sorrow.)". Kroon & Voltolini: "Walton clarifies his view in Walton 1997, where he emphasizes that he regards fictional emotions not so much as special kind of states, but as emotions that are merely felt in the context of engaging with fiction rather than actuality."
  *Against:* Carroll: "“if it [the fear produced by horror films] were a pretend emotion, one would think that it could be engaged at will. I could elect to remain unmoved by The Exorcist; I could refuse to make believe I was horrified." (1990, p. 74) and "Surely a game of make-believe requires the intention to pretend. But on the face of it, consumers of horror do not appear to have such an intention” (pp. 74-75)."; Novitz: "“many theatre-goers and readers believe that they are actually upset, excited, amused, afraid, and even sexually aroused by the exploits of fictional characters." (1987, p. 241); Hartz: "how could anything as cerebral and out-of-the-loop as ‘make believe’ make adrenaline and cortisol flow?” (1999, p. 563)"; Säätelä: "“fear is easy to confuse with being shocked, startled, anxious, etc." (1994, p. 29) — all as quoted in IEP §3. Kroon & Voltolini: "Walton’s view has been subject to much criticism (for a survey, see Neill 2005)."
  *For, in reply:* Neill (1991, pp. 49–50, as quoted in IEP §3): "On his view, we can actually be moved by works of fiction, but it is make-believe that we are moved to is fear." Schneider calls this "a powerful reply to objections which cite phenomenological disanalogies" (IEP §3).
- **Non-intentionalist (Charlton 1970).** "According to the Non-Intentionalist solution the affective states in question are not emotions but more akin to object-less states like moods or reflex reactions (Charlton 1970: 97)" (Kroon & Voltolini §4).
  *Against:* none recorded in the excerpts held.
- **Surrogate object (Lamarque 1981 on one formulation; Charlton 1984).** Kroon & Voltolini: "for the more popular Surrogate-Object solution (A) misidentifies the target of emotional responses to fiction: they really have as their objects (parts of) the fictional work itself; or perhaps the descriptions or thought contents afforded by the fiction (Lamarque 1981); or on another formulation real individuals or phenomena that resemble the persons or events of the fiction (see, for example, Charlton 1984)." The IEP's **counterpart theory** is the last variant, in Currie's statement: "“we experience genuine emotions when we encounter fiction, but their relation to the story is causal rather than intentional; the story provokes thoughts about real people and situations, and these are the intentional objects of our emotions” (1990, p. 188)."
  *Against:* none recorded in the excerpts held.
- **Thought theory / anti-judgmentalism (Lamarque 1981; Carroll 1990; Moran 1994; Smith 1995; Feagin 1996; Gendler 2008).** Schneider: "all we need do is “mentally represent” (Peter Lamarque), “entertain in thought” (Noel Carroll), or “imaginatively propose” (Murray Smith) it to ourselves." (IEP §4). Kroon & Voltolini describe the anti-judgmentalist solution as one "which denies that emotional responses to objects logically require beliefs concerning the existence and emotion-prompting features of objects". Liao & Gendler's version: "Broad cognitivists hold that emotions must be triggered by a cognitive mental state, but (cognitive) imagination can play that role as well as belief". Smith's example, as quoted in IEP §5: "If you shuddered in reaction to the idea, you didn’t do so because you believed that your hand was being cut by a knife” (1995, p. 116)."
  *Against:* Radford (1982, pp. 261–62, as quoted in IEP §5): "So the fact that we are frightened by fictional thoughts does not solve the problem but forms part of it." Turvey (1997, p. 433) objects to "“mental entity as the primary causal agent of the spectator’s emotional response”" (IEP §5). Kroon & Voltolini: "But note that such views face the problem that the objects of the emotions mobilized by fiction are either understood in some nonstandard way, for example as thought contents (cf. the objection in Walton 1990 to Lamarque 1981) or, more generally, as abstract rather than concrete entities; or they are understood as nonexistent objects, a category many philosophers find ontologically problematic." Schneider's own assessment: "where the Thought theorist seems to run into trouble is in explaining just why it is the mere entertaining in thought of a fictional character or event is able to generate emotional responses in audiences."
- **Noncognitivism (Robinson 2005).** "Noncognitivists hold that emotions do not need to be triggered by any cognitive mental state (Robinson 2005)." (Liao & Gendler).
  *Against:* none recorded in the excerpts held.
- **Surrogate belief (Neill 1993).** "One way of rejecting (C) is the Surrogate-Belief solution, which maintains that an emotional response to a fictional character requires no more than the belief that the character exists in the world(s) of the fiction (cf. Neill 1993)." (Kroon & Voltolini §4).
  *Against:* none recorded in the excerpts held.
- **Illusion / suspension of disbelief (Coleridge 1817 as a possible historical advocate).** Schneider: "Illusion theorists, of whom there seem to be fewer and fewer these days, deny Radford’s second premise." The mechanisms he lists include "Samuel Taylor Coleridge’s famous “willing suspension of disbelief,” Freud’s notion of “disavowal” as adapted by psychoanalytic film theorists such as Christian Metz". Liao & Gendler: "a possible historical advocate is Coleridge 1817".
  *Against:* Walton (1978, p. 7, as quoted in IEP §6): "If he half believed, and were half afraid, we would expect him to have some inclination to act on his fear in the normal ways." Currie (1990, pp. 188–89, as quoted): "Hardly anyone ever literally believes the content of a fiction when he knows it to be a fiction". Radford already argued that we do not "“try to do something, or think that we should” (p. 71)" (IEP §1).
  *For, in reply:* Schneider asks whether everyday talk of "believability" and of being "absorbed by" fictions can be "explained away" without belief (IEP §6), without endorsing the theory.

**Distribution, as reported (no survey figure recorded).** Kroon & Voltolini: "Most, in fact, favor a rejection of (A) or (C)."; "Far more popular are views that reject (C) and hold that we have real emotions towards fictional objects despite believing that they don’t exist."; they call the anti-judgmentalist solution "possibly the most widely accepted of all", and report Stecker (2011) treating it as in some sense the default. Liao & Gendler: "By far, the orthodoxy is to reject Coordination Condition." and "The Belief Condition is rarely challenged." Schneider: "Somewhat surprisingly, the Thought Theory has generated relatively little critical discussion, a fact in virtue of which it can be said to occupy a privileged position today." These are the encyclopedia authors' reports, not counts.

## Arguments in play

(none recorded as separate argument pages yet). The argument from
counterfactual withdrawal (learning a moving story was false ends the feeling;
Radford, IEP §1), the behavioural-disanalogy argument (Radford p. 71; Walton
1978, p. 7) and the voluntariness and phenomenology objections to make-believe
(Carroll 1990, pp. 74–75; Novitz; Hartz) are quoted above.

## Thinkers who addressed it

- **Samuel Taylor Coleridge** (1817, ch. 14, per Kroon & Voltolini, who say he "coined the term") — suspension of disbelief; a possible historical advocate of rejecting (B).
- **Charlton** (1970: 97; 1984) — non-intentionalist; surrogate object (Kroon & Voltolini).
- **Colin Radford** (1975, 1977, 1982; replies over two decades, per Schneider) — states the paradox; irrationalism.
- **Kendall Walton** (1978; 1990; 1997) — make-believe, quasi-emotions; originates the descriptive version (Liao & Gendler).
- **Eva Schaper** (1978) — evaluative beliefs about fictional characters suffice (IEP §4).
- **Peter Lamarque** (1981) — first explicit thought theory (IEP §4).
- **R. T. Allen** (1986), **David Novitz** (1987), **Noel Carroll** (1990, *The Philosophy of Horror*), **Gregory Currie** (1990, *The Nature of Fiction*).
- **Alex Neill** (1991; 1993; 2005) — reply on quasi-fear; surrogate belief; survey of criticism.
- **Richard Moran** (1994), **Simo Säätelä** (1994), **Murray Smith** (1995), **Feagin** (1996), **Levinson** (1997, classification), **Malcolm Turvey** (1997), **Glenn Hartz** (1999), **Richard Joyce** (2000).
- **Currie & Ravenscroft** (2002) — conative imagination; **Robinson** (2005) — noncognitivism; **Gendler & Kovakovich** (2005/2006) — normative version; **Gendler** (2008); **Stecker** (2011); **Friend** (2010, 2016).

## Framings and reframings

- **Not a paradox.** Schneider: "It isn’t even clear whether what we have here really qualifies as a “paradox” at all." He cites Moran (1994, p. 79): "“our paradigms of ordinary emotions exhibit a great deal of variety., and.the case of fictional emotions gains a misleading appearance of paradox from an inadequate survey of examples”(p. 79)." (ellipses as printed in the IEP).
- **No theory needed (film).** Turvey, as Schneider reports, holds that because we respond to the concrete cinematic image indifferently to its existence, "no theory at all is needed" for fiction film (IEP §5, paraphrase).
- **Descriptive versus normative.** Liao & Gendler separate the question of what kind of state the response is (Walton) from whether it is rational (Radford); on the normative side "The normative version of the paradox treats Coordination Condition as a norm governing emotional responses to fictions." Others "appeal to fittingness norms of emotions (D’Arms & Jacobson 2000), distinctive norms for fictions (Friend 2010; Gilmore 2011), or even moral norms for engaging with fictional narratives".
- **Fiction as the central case.** Schneider reports that the thought theorist treats emotional response to fiction as "a central case of emotional response in general" rather than an exception (IEP §4, paraphrase).

Not in the excerpts held: the text of Radford 1975, Walton 1978 and 1990,
Lamarque 1981, Carroll 1990 and Levinson 1997; Friend 2016; Weston's
contribution (Crossref lists Weston beside Radford on the 1975 DOI record). They are left out
until read.

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — see The question and Framings.
- [Validity](../vocabulary/validity.md) and [classical logic](../methods/classical-logic.md) — the propositional check above.
- [Knowledge](../vocabulary/knowledge.md) — "knowing them to be fictional" in (A).
- *Existence belief*, *quasi-emotion*, *make-believe*, *cognitive theory of emotion*, *suspension of disbelief* — open work in [vocabulary](../vocabulary/index.md).
