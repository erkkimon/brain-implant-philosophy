---
type: article
about: concept
title: "The paradox of nihilism"
description: "Does a thesis of the form 'nothing is true', 'nothing exists' or 'nothing has meaning' undermine itself when applied to itself? Wikipedia lists the name for several distinct paradoxes (metaphysical, existential, ethical); the self-application charge is argued in the sources read under other names — Plato's peritrope against Protagoras, Mackie's self-refutation, Baldwin's subtraction argument — with replies by Burnyeat, Hales and Comesaña & Klein, each with its owner."
tags: [problem, paradox, metaphysics, epistemology, ethics]
timestamp: 2026-10-01T19:53:21Z
---

# The paradox of nihilism

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Sources: Wikipedia, "List of paradoxes" ([rev. 1376699902](https://en.wikipedia.org/w/index.php?title=List_of_paradoxes&oldid=1376699902))
and "Paradox of nihilism" ([rev. 1328169716](https://en.wikipedia.org/w/index.php?title=Paradox_of_nihilism&oldid=1328169716))
(excerpt: `raw/wikipedia-paradox-of-nihilism-article-and-list-entry.md`);
Pratt, [IEP "Nihilism"](https://iep.utm.edu/nihilism/) (excerpt: `raw/iep-nihilism-pratt-definition-and-nietzsche.md`);
Baghramian & Carter, [SEP Fall 2024 "Relativism"](https://plato.stanford.edu/archives/fall2024/entries/relativism/)
(excerpt: `raw/sep-relativism-fall-2024-self-refutation.md`);
Sorensen, [SEP Fall 2024 "Nothingness"](https://plato.stanford.edu/archives/fall2024/entries/nothingness/)
(excerpt: `raw/sep-nothingness-fall-2024-subtraction-and-self-defeat.md`);
Comesaña & Klein, [SEP Fall 2024 "Skepticism"](https://plato.stanford.edu/archives/fall2024/entries/skepticism/)
(excerpt: `raw/sep-skepticism-fall-2024-is-pyrrhonian-skepticism-self-refuting.md`);
Plato, *Theaetetus* 171a–b, Jowett tr. ([Gutenberg #1726](https://www.gutenberg.org/ebooks/1726);
excerpt: `raw/plato-theaetetus-171a-jowett-peritrope.md`).

**Scope note (structural, this implant).** The sources read are thin for
the name itself. No SEP or IEP entry read here uses the phrase "paradox of
nihilism"; the IEP entry "Nihilism" contains no discussion of
self-refutation. The phrase occurs in the Wikipedia article and in three of
its references (Hegarty 2006, Bornemark 2006, Wright), none of which was
read. The self-application charge (a thesis that nothing is true, or that
nothing has meaning, applied to itself) is discussed in the encyclopedias under
*self-refutation* of global relativism and global scepticism and under the
*subtraction argument* for metaphysical nihilism; those discussions are
reported below as what they are, not as discussions of a paradox of that
name.

## The question

Wikipedia's list entry (rev. 1376699902): "Paradox of nihilism: Several distinct paradoxes share this name."
The article (rev. 1328169716): "The paradox of nihilism is a family of paradoxes regarding the philosophical implications of nihilism, particularly situations contesting nihilist perspectives on the nature and extent of subjectivity within a nihilist framework. There are a number of variations of this paradox."
It names two basic forms: "The two basic paradoxes are reflective of the philosophies of nihilism that created them; metaphysical nihilism and existential nihilism."
Their shared root, per the article: "Both paradoxes originate from the same conceptual difficulty of whether, as Paul Hegarty writes in his study of noise music, "the absence of meaning seems to be some sort of meaning"."

- **Metaphysical form (Wikipedia).** "The paradox arises from the logical assertion that if no concrete or abstract objects exist, even the self, then that very concept itself would be untrue because it itself exists."
- **Existential form (Wikipedia).** "Existential nihilism is the philosophical theory that life has no inherent meaning whatsoever, and that humanity, both in an individual sense and in a collective sense, has no purpose." The article's section carries "citation needed" and "According to whom" tags (August 2025).
- **Ethical form (Wikipedia).** "According to Jonna Bornemark, "the paradox of nihilism is the choice to continue one's own life while at the same time stating that it is not worth more than any other life"." The article adds: "Richard Ian Wright sees relativism as the root of the paradox." — tagged "Clarify" with the reason "Which paradox exactly?".

The whole article carries a "Cleanup rewrite" tag dated October 2020.

**The self-application form.** The thesis being turned on itself, in the
IEP's definition: "Nihilism is the belief that all values are baseless and that nothing can be known or communicated." (Pratt, IEP, introduction).
Pratt quotes Nietzsche: "“Every belief, every considering something-true,” Nietzsche writes, “is necessarily false because there is simply no true world” (Will to Power [notes from 1883-1888])." (§2).
The charge that such a global thesis undermines itself is stated, for global
relativism, by Baghramian & Carter: "As we will see, global relativism is open to the charge of inconsistency and self-refutation, for if all is relative, then so is relativism. Local relativism is immune from this type of criticism, as it need not include its own statement in the scope of what is to be relativized." (SEP "Relativism", §1.4.1).

**Propositional check (this implant, 2026-10-01; logic, not a position).**
Let *n* be the sentence *nothing is true* and suppose, as the self-application
charge does, that if *n* is true then *n*, being something, is not true:
*n* → ~*n*. `logic.py check --premises "n -> ~n" --conclusion "~n"` returns
`VALID`; with conclusion `n` it returns `INVALID` with counterexample row
`n=F`. So that one premise yields only that *n* is not true; it does not
yield a contradiction, and it says nothing about whether the negation of
*n* ("something is true") is true by any further route. The tool treats *n*
as an unanalysed atom: the premise *n* → ~*n* is the charge's assumption,
not something the tool derives, and truth-relative readings (Hales, below)
lie outside propositional logic.

## Why it matters

- **Relativism.** Baghramian & Carter: "The strongest and most persistent charge leveled against all types of relativism, but (global) alethic relativism in particular, is the accusation of self-refutation." (§4.3.1). They quote Siegel (2011: 203): "This incoherence charge is by far the most difficult problem facing the relativist."
- **Scepticism.** Comesaña & Klein ask of absolute scepticism: "Is Pyrrhonian Skepticism so understood self-refuting? It is certainly formally consistent" (SEP "Skepticism", §2); see [Agrippan trilemma](agrippan-trilemma.md).
- **Metaphysics of nothing.** Baldwin's argument, as Wikipedia reports it: "Therefore, it is entirely possible that a world with no objects exists." Sorensen: "Parmenides maintained that it is self-defeating to say that something does not exist." (SEP "Nothingness", §10).
- **Postmodern theory.** Pratt: "Postmodern antifoundationalists, paradoxically grounded in relativism, dismiss knowledge as relational and “truth” as transitory, genuine only until something more palatable replaces it (reminiscent of William James’ notion of “cash value”)." (§4).

## Positions taken

No source read groups positions on a "paradox of nihilism". The groupings
below follow the sources that discuss the self-application charge, in their
own sequence; none is ranked here. For the self-refutation charge against
relativism Baghramian & Carter distinguish an original argument (Plato), "A
second strand of the self-refutation argument focuses on the nature and role
of truth", and "operational"/"conversational" self-refutation (§4.3.1).

- **Peritrope: the measure doctrine refutes itself (Plato, *Theaetetus* 171a–b).** Socrates: "And the best of the joke is, that he acknowledges the truth of their opinion who believe his own opinion to be false; for he admits that the opinions of all men are true." Baghramian & Carter: "Plato’s attempted refutation of Protagoras, known as peritrope or “turning around”, is the first of the many attempts to show that relativism is self-refuting." (§3). Their reconstruction ends: "Therefore, Protagoras must believe that his own doctrine is false (see Theaetetus: 171a–c)" (§4.3.1).
  *Against:* "Plato’s argument, as it stands, appears to be damaging only if we assume that Protagoras, at least implicitly, is committed to the universal or objective truth of relativism. On this view, Plato begs the question on behalf of an absolutist conception of truth (Burnyeat 1976a: 44)." ([Burnyeat 1976](https://doi.org/10.2307/2184254), as reported). "Protagoras, the relativists counter, could indeed accept that his own doctrine is false for those who accept absolutism but continue believing that his doctrine is true for him." (§4.3.1).
- **A denial of absolute truth refutes itself (Mackie 1964).** "J.L. Mackie, for instance, has argued that alethic absolutism is a requisite of a coherent notion of truth and that a claim to the effect that “There are no absolute truths” is absolutely self-refuting (Mackie 1964: 200)." (§4.3.1; [Mackie 1964](https://doi.org/10.2307/2955461), not read).
  *Against:* "But the relativists reject the quick move that presupposes the very conception of truth they are at pains to undermine and have offered sophisticated approaches of defense." (§4.3.1).
- **A consistent relativism (Hales 1997).** "Key to this approach, according to Hales, is that we abandon a conception of global relativism on which the lose thesis “everything is relative” is embraced—a thesis Hales concedes to be inconsistent—for the thesis “everything that is true is relatively true”, which he maintains is not (cf. Shogenji 1997 for a criticism of Hales on this point)." (§4.3.1).
- **Pragmatic, operational or conversational self-refutation (Mackie 1964; Evans 1985; Kölbel 2011).** "It has also been claimed that alethic relativism gives rise to what J.L. Mackie calls “operational” (Mackie 1964: 202) and Max Kölbel “conversational” self-refutation (Kölbel 2011) by flouting one or more crucial norms of discourse and thereby undermines the very possibility of coherent discourse." (§4.3.1). On persuasion: "The relativist cannot make such a commitment and therefore his attempts to persuade others to accept his position may be pragmatically self-refuting." and "In other words, if Protagoras really believes in relativism why would he bother to argue for it?" (§4.3.1).
  *Against:* "The relativists however, could respond that truth is relative to a group (conceptual scheme, framework) and they take speakers to be aiming a truth relative to the scheme that they and their interlocutors are presumed to share." Baghramian & Carter's assessment of that reply: "The difficulty with this approach is that it seems to make communication across frameworks impossible." (§4.3.1).
- **Global scepticism and the Commitment Iteration Principle (Comesaña & Klein 2019).** "If the Commitment Iteration Principle holds, then Pyrrhonian Skepticism is indeed self-refuting." (§2).
  *Against:* "But Pyrrhonian skeptics need not hold the Commitment Iteration Principle." Comesaña & Klein's assessment: "It is not clear, then, that the charge of self-refutation represents an independent indictment of Pyrrhonian Skepticism." (§2).
- **An empty world is possible: the subtraction argument (Baldwin 1996).** Sorensen: "Thomas Baldwin (1996) reinforces the possibility of an empty world by refining the following thought experiment: Imagine a world in which there are only finitely many objects. Suppose each object vanishes in sequence. Eventually you run down to three objects, two objects, one object and then Poof! There’s your empty world." (§7; [Baldwin 1996](https://doi.org/10.1093/analys/56.4.231), not read).
  *Against:* the Tractatus view as Sorensen reports it: "Since every fact requires at least one object, a world without objects would be a world without facts. But a factless world is a contradiction in terms. Therefore, the empty world is impossible." (§7). Wikipedia: "Critics often point to the ambiguity of Baldwin's premises as proof both of the paradox and of the flaws within metaphysical nihilism itself." citing [Efird & Stoneham 2005](https://doi.org/10.5840/jphil2005102614) (not read). Sorensen's own assessment: "Whether or not Armstrong has contradicted himself, he has illustrated the persuasiveness of the subtraction argument." (§7).
- **Negative existentials are self-defeating (Parmenides).** "Parmenides maintained that it is self-defeating to say that something does not exist." (Sorensen, §10).
- **Absence of meaning as meaning (Hegarty 2006).** Quoted only as Wikipedia quotes it: "noise is only ever defined against something else, operating in the absence of meaning, but caught in the paradox of nihilism – that the absence of meaning seems to be some sort of meaning." (Hegarty, *Semiotic Review of Books* 16(1–2): 2; not read).
- **Choosing to live while denying life's greater worth (Bornemark 2006).** As quoted above from Wikipedia ([Bornemark 2006](https://doi.org/10.1515/SATS.2006.63), p. 64, not read).
- **Relativism as the root (Wright).** Quoted only as Wikipedia's reference quotes it: "And herein lies the crux of the paradox of nihilism. If nihilism is the basis of human existence then all values are relative, and as such, particular values can only be maintained through a "will to power."" ([Wright](https://doi.org/10.14288/1.0089007), p. 97, not read; the DOI record gives 2009, the Wikipedia reference "April 1994").

**Distribution.** No survey figure is recorded in the sources read.

## Arguments in play

(none recorded as separate argument pages yet). Plato's peritrope as
reconstructed by Baghramian & Carter (§4.3.1), the Commitment Iteration
argument (Comesaña & Klein, §2) and the subtraction argument (Sorensen, §7)
are quoted above. The propositional shape of the self-application charge is
checked under The question.

## Thinkers who addressed it

- **Parmenides** — negative existentials self-defeating (Sorensen, §10).
- **Plato** (*Theaetetus* 171a–c) — peritrope against Protagoras.
- **Protagoras** — the measure doctrine (*Theaetetus* 152a, per Baghramian & Carter §3).
- **Victor Hugo** (*Les Misérables*, 1862, 439) — "Nihilism has no substance." (as quoted by Sorensen, §1).
- **Friedrich Nietzsche** (*Will to Power*, notes 1883–1888, per Pratt §2).
- **J. L. Mackie** (1964: 200, 202) — absolute and operational self-refutation.
- **M. F. Burnyeat** (1976a: 44) — question-begging reply on Protagoras' behalf.
- **Gareth Evans** (1985: 346–63), **Steven Hales** (1997), **Tomoji Shogenji** (1997), **Max Kölbel** (2011), **Harvey Siegel** (2011: 203) — per Baghramian & Carter §4.3.1.
- **Thomas Baldwin** (1996) — subtraction argument; **David Efird & Tom Stoneham** (2005, 2009); **David Armstrong** (2004) — per Sorensen §7 and Wikipedia.
- **Richard Rorty** (1986, 1989), **Jean-François Lyotard**, **Jacques Derrida** — antifoundationalism, per Pratt §4.
- **Juan Comesaña & Peter Klein** (SEP, 2019) — Commitment Iteration Principle.
- **Paul Hegarty** (2006), **Jonna Bornemark** (2006), **Richard Ian Wright** — per Wikipedia only.

## Framings and reframings

- **Global versus local.** Baghramian & Carter: "Local relativism is immune from this type of criticism, as it need not include its own statement in the scope of what is to be relativized." (§1.4.1).
- **A matter of simplicity, not refutation.** Sorensen: "As far as simplicity is concerned, there is a tie between the nihilistic rule ‘Always answer no!’ and the inflationary rule ‘Always answer yes!’. Neither rule makes for serious metaphysics." (§1). Hugo, as Sorensen quotes him: "All roads are blocked to a philosophy which reduces everything to the word ‘no.’ To ‘no’ there is only one answer and that is ‘yes.’ Nihilism has no substance." (§1).
- **Nihilism as a cultural condition.** Pratt reports Rorty: "American antifoundationalist Richard Rorty makes a similar point: “Nothing grounds our practices, nothing legitimizes them, nothing shows them to be in touch with the way things are” (“From Logic to Language to Play,” 1986)." (§4); and "In the 20th century, nihilistic themes–epistemological failure, value destruction, and cosmic purposelessness–have preoccupied artists, social critics, and philosophers." (introduction).
- **Several paradoxes, one name.** Wikipedia treats the name as covering distinct paradoxes (list entry and article lead, quoted above).

Not in the excerpts held: Mackie 1964, Burnyeat 1976a, Hales 1997,
Baldwin 1996, Efird & Stoneham 2005, Hegarty 2006, Bornemark 2006 and
Wright's thesis; Nietzsche's *Will to Power* itself. They are cited only as
the sources above report them, until a text is read.

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — see The question.
- [Validity](../vocabulary/validity.md) and [Classical logic](../methods/classical-logic.md) — the propositional check.
- [Knowledge](../vocabulary/knowledge.md) — "nothing can be known" in the IEP definition.
- *Self-refutation*, *peritrope*, *global/local relativism*, *metaphysical nihilism*, *subtraction argument* — open work in [vocabulary](../vocabulary/index.md).
