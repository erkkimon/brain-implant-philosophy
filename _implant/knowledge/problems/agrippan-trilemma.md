---
type: article
about: concept
title: "The Agrippan (Münchhausen) trilemma"
description: "Any reason offered for a claim either calls for a further reason without end, circles back on itself, or stops at an unsupported starting point — the three formal modes of Agrippa (Sextus, PH I.164–177; Diogenes Laertius IX.88–89), reported as a regress already by Aristotle (Post. An. I.3) and called the Münchhausen trilemma after Hans Albert; foundationalism, coherentism, infinitism, positism, Pyrrhonian suspension and critical rationalism each reject a different horn."
tags: [problem, dilemma, epistemology, skepticism, justification]
timestamp: 2026-09-28T07:01:48Z
---

# The Agrippan (Münchhausen) trilemma

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
sources graded as in [How claims are graded](../../conventions/how-claims-are-graded.md).
Ancient texts: Sextus Empiricus, *Outlines of Pyrrhonism* I.164–177, in M. M. Patrick's public-domain translation ([1899, Project Gutenberg](https://www.gutenberg.org/ebooks/17556); excerpt: `raw/patrick-1899-sextus-ph-1-164-177-five-tropes.md`); Diogenes Laertius IX.88–90, Hicks tr. ([Wikisource](https://en.wikisource.org/wiki/Lives_of_the_Eminent_Philosophers/Book_IX); excerpt: `raw/diogenes-laertius-9-88-89-five-modes-of-agrippa-hicks.md`); Aristotle, *Posterior Analytics* I.3, Mure tr. ([MIT Classics](https://classics.mit.edu/Aristotle/posterior.1.i.html); excerpt: `raw/aristotle-posterior-analytics-1-3-72b-regress-and-circular-demonstration-mure.md`).
Maps: Comesaña & Klein, [SEP Fall 2024 "Skepticism"](https://plato.stanford.edu/archives/fall2024/entries/skepticism/) §5 (excerpt: `raw/sep-skepticism-fall-2024-agrippas-trilemma-and-responses.md`); Vogt, [SEP "Ancient Skepticism"](https://plato.stanford.edu/archives/fall2024/entries/skepticism-ancient/) §4.3, and Morison, [SEP "Sextus Empiricus"](https://plato.stanford.edu/archives/fall2024/entries/sextus-empiricus/) §3.5.2 (excerpt: `raw/sep-skepticism-ancient-and-sextus-empiricus-fall-2024-five-modes.md`); Hasan & Fumerton, [SEP "Foundationalist Theories of Epistemic Justification"](https://plato.stanford.edu/archives/fall2024/entries/justep-foundational/) §1, and Olsson, [SEP "Coherentist Theories"](https://plato.stanford.edu/archives/fall2024/entries/justep-coherence/) §2 (excerpt: `raw/sep-justep-foundational-and-coherence-fall-2024-regress-argument.md`); Klein & Turri, [IEP "Infinitism in Epistemology"](https://iep.utm.edu/inf-epis/), and Wettersten, [IEP "Karl Popper: Critical Rationalism"](https://iep.utm.edu/cr-ratio/) §5 (excerpt: `raw/iep-infinitism-klein-turri-and-critical-rationalism-wettersten-regress.md`). Albert's own book was not read (record: `raw/albert-1968-munchhausen-trilemma-bibliographic.md`).

## The question

Sextus lists five modes of suspending judgement: "The later Sceptics, however, teach the following five Tropes of [Greek: epoche]: first, the one based upon contradiction; second, the _regressus in infinitum_; third, relation; fourth, the hypothetical; fifth, the _circulus in probando_." (PH I.164, Patrick tr.). Diogenes Laertius credits them to "Agrippa and his school" (IX.88). Three of them are formal:

- **Regress.** "the proof brought forward for the thing set before us calls for another proof, and that one another, and so on to infinity, so that, not having anything from which to begin the reasoning, the suspension of judgment follows" (PH I.166).
- **Hypothesis.** The Dogmatists "begin from something that they do not found on reason, but which they simply take for granted without proof" (I.168); answered by the rule that "we should in every case be no less worthy of confidence in making a contrary hypothesis" (I.173).
- **Circle.** "the thing which ought to prove the thing sought for, needs to be sustained by the thing sought for" (I.169). Diogenes' example: proving pores from emanations and emanations from pores (IX.89).

Morison states the case for exhaustiveness: "Thus, there are exactly three possibilities for the form an argument propounded by a dogmatist might take: an infinite regress, a reciprocal or circular argument, or one which terminates in a hypothesis." (SEP §3.5.2). Comesaña & Klein say the Pyrrhonian use of these three "has been called “Agrippa’s trilemma”" and reconstruct it as an argument (§5): (1) a justified belief is either basic or inferentially justified; (2) "There are no basic justified beliefs." (mode of hypothesis); (3) so a justified belief is justified by belonging to an inferential chain; (4) every chain is infinite, circular or contains unjustified beliefs; (5) not infinite (mode of regress); (6) not circular (mode of circularity); (7) not with unjustified members; conclusion: "There are no justified beliefs." They add that presenting the Pyrrhonian position as an argument is "at least somewhat misleading", since Pyrrhonists "would suspend judgment" on its premises (§5).

**Logic (this implant, 2026-09-27; checked with `logic.py`).** A propositional skeleton of that reconstruction — `J -> B | K`, `~B`, `K -> KI | KC | KU`, `~KI`, `~KC`, `~KU`, conclusion `~J` (J: justified; B: basic; K: justified by a chain; KI/KC/KU: justified by an infinite / circular / partly unjustified chain) — returns "VALID". Dropping any one of `~B`, `~KI`, `~KC`, `~KU` returns "INVALID" with one counterexample row each, e.g. without `~B`: "B=T, J=T, K=F, KC=F, KI=F, KU=F". This is a structural note only: which premise to drop is the dispute below, and the skeleton does not model premise 4's claim to exhaust the options.

## Why it matters

- Comesaña & Klein: "The importance of Pyrrhonian Skepticism to contemporary epistemology derives primarily from these modes", and "Many contemporary epistemological positions can be stated as a reaction to Agrippa’s trilemma." (§5). Applied to epistemological theories themselves, it yields "what has been called “the problem of the criterion” (see Chisholm 1973)" (§5).
- Vogt: the Five Modes "are among the most famous arguments of ancient skepticism (Barnes 1990, Hankinson 2010)" (§4.3). Morison: "philosophically they are the most interesting of all the modes" (§3.5.2).
- Olsson qualifies the point for coherentism: "Although the regress problem is not a central contemporary issue, it is helpful to explain coherence theories as responses to the problem." (§1).
- Smith & Bueno, on Latin America: "The so-called Agrippan trilemma is an important argument for contemporary skepticism." ([SEP Fall 2024 "Skepticism in Latin America"](https://plato.stanford.edu/archives/fall2024/entries/skepticism-latin-america/), §6; excerpt: `raw/sep-skepticism-latin-america-fall-2024-agrippan-trilemma.md`).

## Positions taken

Comesaña & Klein: "all of premises 2, 5, 6 and 7 have been rejected by different philosophers at one time or another" (§5). Klein & Turri give the same map by chain shape: "Foundationalists opt for non-repeating finite chains. Coherentists (at least linear coherentists) opt for repeating finite chains. Infinitists opt for non-repeating infinite chains." (IEP, intro). Order below follows the reconstruction's premises, not merit.

**Foundationalism (rejects premise 2).** Aristotle reports two schools — one holding "there is no scientific knowledge" because of the regress, one holding "all truths are demonstrable" because "demonstration may be circular and reciprocal" — and rejects both: "Our own doctrine is that not all knowledge is demonstrative: on the contrary, knowledge of the immediate premisses is independent of demonstration." (Post. An. I.3, 72b). Hasan & Fumerton: "any justified belief must either be foundational or depend for its justification, ultimately, on foundational beliefs"; they cite Aristotle's I.3 as "an early version" of the regress argument and Descartes' "secure foundation of indubitable truths" (§1; see [Descartes](../thinkers/descartes.md)). To the question "isn’t it just a blind assertion?", "many foundationalists reply: experience" (Comesaña & Klein §5.1).
- *For:* the regress argument — "finite beings cannot complete an infinitely long chain of reasoning" (Hasan & Fumerton §1); Aristotle: "one cannot traverse an infinite series" (72b).
- *Against:* Hasan & Fumerton themselves say the argument shows "At best" that "if justification is possible ... then that justification must take a foundationalist structure", and that "as with any argument by elimination, it depends on whether the alternatives eliminated really are untenable" (§1). BonJour (1978, 1985), "Inspired by Sellars (1963)", pressed the "Sellarsian Dilemma" against classical foundationalism (Hasan & Fumerton §3.2). Klein & Turri name "the specter of arbitrariness" (IEP §1).

**Infinitism (rejects premise 5).** Defended by Peter Klein (1998, [doi](https://doi.org/10.2307/2653735); 1999, [doi](https://doi.org/10.1111/0029-4624.33.s13.14)), Fantl (2003) and Aikin (2011), per Hasan & Fumerton (§1). Its conditions, in Klein & Turri's words: "No reason can be Q itself" and "No reason is sufficiently justified in the absence of a further reason. That is, there are no foundational reasons." (IEP §1).
- *For:* "infinitists deny that there is any reason which is immune to further legitimate challenge" (Klein & Turri §1); Hasan & Fumerton: "Infinitism is a view that should be seriously considered", since one "arguably does have an infinite number of justified beliefs (e.g., that 2 is greater than 1, that 3 is greater that 1, and so on.)" (§1). Reply to finitude: only "implicit beliefs that are available to the subject" are needed (Comesaña & Klein §5.2).
- *Against:* the Finite Mind Objection, "Our finite minds are not capable of producing or grasping an infinite set of reasons" (Klein & Turri §2), traced to Aristotle; Fumerton (1995) via Klein & Turri §4a; "If the appeal to a single unjustified belief cannot do any justificatory work of its own, why would appealing to a large number of unjustified beliefs do any better?" (Comesaña & Klein §5.2); the proof-of-concept objection, Wright 2011 ([doi](https://doi.org/10.1007/s11229-011-9884-x)), via Klein & Turri §4b. Standing: Comesaña & Klein say it "has received the least attention in the literature" (§5.2); Klein & Turri, a "distinctly minority view" (§2). Klein co-authored both entries.

**Coherentism (rejects the linear picture; Comesaña & Klein file it under premise 3).** Olsson: "nothing prevents the regress from proceeding in a circle", but "justificatory circles are usually thought to be vicious ones"; the holistic coherentist instead denies "that justification should at all proceed in a linear fashion", so "the regress never gets started" — "This, in essence, is Laurence BonJour’s 1985 solution to the regress problem." (§2). Comesaña & Klein: coherentists reject that justification is asymmetrical and that "the unit of justification is the individual belief" (§5.3).
- *For:* Hasan & Fumerton report the reply that "circular inferences can provide justification despite being dialectically ineffective" (§1).
- *Against:* the isolation objection — "how can the mere fact that a system is coherent ... provide any guidance whatsoever to truth and reality?" (Olsson §1). On BonJour's and Lehrer's reply, Comesaña & Klein judge: "It is fair to say that there is no agreement regarding whether this move can solve the problem." (§5.3). Aristotle: upholders of circular demonstration say "that if A is, A must be-a simple way of proving anything" (73a).

**Positism (rejects premise 7).** Traced by Comesaña & Klein to Wittgenstein's *On Certainty* "and, perhaps, also to Ortega’s Ideas y Creencias": chains end in "posits that we have to believe without justification" (§5.4).
- *Against:* "they are transforming a doxastic necessity into an epistemic virtue" (§5.4).

**Combinations.** "more and more epistemologists are arguing that the proper way to reply to Agrippa’s trilemma is to combine some of the positions", e.g. Haack 1993 (Comesaña & Klein §5.5).

**Pyrrhonian suspension of judgement.** Sextus: "it is necessary to suspend the judgment altogether with regard to every thing that is brought before us" (PH I.177). How the modes work is disputed (see Framings).
- *Against:* Vogt reports the objection that the modes "presuppose that everything is subject to proof" (Barnes 1990; Hankinson 1995; Long 2006), and the replies that they are dialectical (Striker 2004) or broader in scope (§4.3). Hasan & Fumerton, their own assessment: "This most radical of all skepticisms seems absurd (it entails that one couldn’t even be justified in believing it)." (§1).

**Critical rationalism (gives up justification).** Wettersten reports that Hans Albert "argues that any attempt at justification faces a three-pronged difficulty that is traceable to Agrippa" — infinite regress, circle, or "some arbitrary starting point" held "dogmatically" — and concludes "we should abandon the quest for justification. Instead we should hold all theories open to criticism, as Popper and Bartley have proposed." (IEP §5).
- *For and against:* Havlík's abstract reports that Popper's students mostly accept critical rationalism "as the only possible solution to the trilemma" and that Albert debated "the so-called transcendental pragmatism of Karl-Otto Apel" (Havlík 2025, [doi](https://doi.org/10.46854/fc.2025.3r.483)); see also Albert, "Münchhausen in transzendentaler Maskerade" (1985, [doi](https://doi.org/10.1007/bf01803680)). Wettersten says the success or failure of substituting critical for justificatory methods "has still to be judged" (IEP, intro). No text of Apel's or Habermas's objection was read.

## Arguments in play

- **Aristotle's report and verdict (Post. An. I.3).** Regress ("wherein they are right, for one cannot traverse an infinite series"), circle ("circular demonstration is clearly not possible in the unqualified sense of 'demonstration'"), immediate premisses (72b). Vogt quotes the related point "It is impossible that there be demonstration for everything. Otherwise demonstration would go on ad infinitum." as one "Scholars often refer to" (§2.3).
- **Diogenes' dilemma against demonstration (IX.90).** "For all demonstration, say they, is constructed out of things either already proved or indemonstrable." — regress on one horn, doubt on the other.
- **The regress argument for foundationalism** and its double regress under both clauses of the Principle of Inferential Justification (Hasan & Fumerton §1).
- **The Sellarsian dilemma** against the given (BonJour after Sellars; Hasan & Fumerton §3.2).
- **The finite-mind, "unjustified beliefs", and proof-of-concept objections** to infinitism, and the "available reasons" reply (Klein & Turri §§2, 4a–b; Comesaña & Klein §5.2).
- **The isolation objection** to coherentism (Olsson §1; Comesaña & Klein §5.3).
- **Plato-inspired dialectic.** José de Teresa's strategy "escapes the three alternatives under consideration", according to de Teresa as reported by Smith & Bueno (SEP "Skepticism in Latin America" §6).

## Thinkers who addressed it

- **Aristotle** (4th c. BCE) — reports the regress and circular-demonstration schools; knowledge of immediate premisses (Post. An. I.3).
- **Agrippa** — Vogt: "Almost nothing is known about Agrippa (1st to 2nd century CE" (§4.3); Morison: "probably lived at the end of the first century BCE" (§3.5.2). The two entries differ.
- **Sextus Empiricus** (PH I.164–177) — "Sextus nowhere mentions the author of these Tropes" (Patrick 1899).
- **Diogenes Laertius** (IX.88–90) — the attribution to Agrippa.
- **Descartes** — foundation of indubitable truths (Hasan & Fumerton §1).
- **Wittgenstein** (1969), **Ortega y Gasset** (1940) — sources of positism (Comesaña & Klein §5.4).
- **Hans Albert** (*Traktat über kritische Vernunft*, 1968; *Treatise on Critical Reason*, 1985, [doi](https://doi.org/10.1515/9781400854929)) — the three-pronged difficulty; with Popper and Bartley, criticism instead of justification (Wettersten §5).
- **Chisholm** (1973) — the problem of the criterion (Comesaña & Klein §5).
- **Laurence BonJour** (1985) — coherentist solution; Sellarsian dilemma (Olsson §2; Hasan & Fumerton §3.2).
- **Jonathan Barnes** (1990), **Gisela Striker** (2004), **Benjamin Morison** (2011, 2018) — readings of the modes (Morison §3.5.2).
- **Susan Haack** (1993) — foundationalist and coherentist elements (Comesaña & Klein §5.5).
- **Richard Fumerton** (1995) — finite-mind objection (Klein & Turri §4a).
- **Peter Klein** (1998, 1999), **Jeremy Fantl** (2003), **Scott Aikin** (2011) — infinitism (Hasan & Fumerton §1).
- **Stephen Wright** (2011) — proof-of-concept objection to Klein.
- **Oswaldo Porchat** (neo-Pyrrhonism), **José de Teresa** (2000, 2013, 2014) — per Smith & Bueno (§6).

## Framings and reframings

- **Five modes or three.** Comesaña & Klein: "There are five modes associated with Agrippa, but three of them are the most important" (§5). Sextus: the later Sceptics set the five forth "not to throw out the ten Tropes" (PH I.177, Patrick tr.); Hicks's note on Diogenes: "The intention of Agrippa was to ''replace'' the ten modes by his five." (IX.88 n.). Smith & Bueno: for Latin American skepticism the most important mode "seems to be diaphonía or disagreement".
- **Condemnation, dialectic, or opposition.** Barnes (1990) reads the modes as condemning "bad arguments"; Morison judges that reading "unsatisfactory" and notes Sextus "merely says that in such an argument, ‘we have no point from which to begin to establish anything’ (PH I 166)"; Striker (2004): "a way of showing his dogmatic opponents that they ought to suspend judgment, given their epistemological standards"; Morison (2011, 2018): devices "for generating equal and opposing arguments" (all Morison §3.5.2). Morison on I.170–177: "That stretch of text remains mysterious."
- **"Undecided" or "undecidable."** Vogt: the mode of disagreement "hangs" on how *anepikriton* is translated, and "It would be dogmatic to claim that matters are undecidable." (§4.3).
- **The Münchhausen name.** Havlík's abstract says Albert, in his *Treatise on Critical Reason*, refers to the problem "as “Münchhausen’s Trilemma”" (2025). Wettersten's IEP account of Albert does not use the name. The claim that Albert coined it in 1968 was not verified here; Gadenne (2013, [doi](https://doi.org/10.30965/9783957439512_015)) and Rath (2017, *Historisches Wörterbuch der Philosophie*, [doi](https://doi.org/10.24894/hwph.2620)) treat the term but were not read.
- **Constructive trilemma form (this implant, `logic.py`).** `I -> S`, `C -> S`, `H -> S`, `I | C | H` ⊢ `S` returns "VALID": if each of regress, circle and hypothesis leads to suspension and they exhaust the cases, suspension follows — the three-horned case of the [dilemma](../vocabulary/dilemma.md) form.

## Vocabulary

- [Dilemma](../vocabulary/dilemma.md) — the argument form; a trilemma has three horns.
- [Knowledge](../vocabulary/knowledge.md), [argument](../vocabulary/argument.md), [validity](../vocabulary/validity.md).
- Basic belief, inferential chain, PIJ, coherence, isolation objection, *epochē*, *diaphōnia*, *anepikriton* — defined in the sources above; open work in [vocabulary](../vocabulary/index.md).

Related problems: [Meno's paradox](menos-paradox.md) (Post. An. I.1),
[moral dilemmas](moral-dilemmas.md). Method: [classical logic](../methods/classical-logic.md). Branch: [Problems](./index.md).
