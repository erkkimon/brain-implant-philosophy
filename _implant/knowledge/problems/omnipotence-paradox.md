---
type: article
about: concept
title: "The omnipotence paradox (the paradox of the stone)"
description: "Can an omnipotent being make a stone it cannot lift? Either answer seems to name something it cannot do. The dilemma as Savage (1967), Hoffman & Rosenkrantz (SEP) and Pearce (IEP) set it out; its forerunners in Dionysius the Areopagite, Averroes and Aquinas; Mavrodes' 'self-contradictory stone', Frankfurt's Cartesian reply, Cowan's objection, essential vs. accidental omnipotence, act vs. result theories — each with its owner."
tags: [problem, paradox, philosophy-of-religion, metaphysics, logic]
timestamp: 2026-10-02T03:07:33Z
---

# The omnipotence paradox (the paradox of the stone)

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
claim grades as in [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Maps: Joshua Hoffman and Gary Rosenkrantz, [SEP Fall 2024 "Omnipotence"](https://plato.stanford.edu/archives/fall2024/entries/omnipotence/)
(first published 2002-05-21, revised 2022-01-14; excerpt:
`raw/sep-omnipotence-fall-2024-paradox-of-the-stone.md`); Kenneth L. Pearce,
[IEP "Omnipotence"](https://iep.utm.edu/omnipote/) (excerpt:
`raw/iep-omnipotence-pearce-stone-paradox-voluntarism.md`); Wikipedia
["Omnipotence paradox", rev. 1371942568](https://en.wikipedia.org/w/index.php?title=Omnipotence_paradox&oldid=1371942568)
(excerpt: `raw/wikipedia-omnipotence-paradox-rev-1371942568-history-and-stone.md`).
Mavrodes 1963 ([doi:10.2307/2183106](https://doi.org/10.2307/2183106)),
Savage 1967 ([doi:10.2307/2182966](https://doi.org/10.2307/2182966)),
Frankfurt 1964 ([doi:10.2307/2183341](https://doi.org/10.2307/2183341)) and
Cowan 1965 ([doi:10.1093/analys/25.suppl-3.102](https://doi.org/10.1093/analys/25.suppl-3.102))
were verified bibliographically by DOI content negotiation only; their texts
were not read, and what they say is reported through the encyclopedias and
Wikipedia. Both encyclopedia authors also give analyses of their own; those
are marked as theirs.

## The question

Can an omnipotent being make a stone so heavy that it cannot lift it?
Hoffman & Rosenkrantz: "Could an omnipotent agent create a stone so massive that that agent could not move it? Paradoxically, it appears that however this question is answered, an omnipotent agent turns out not to be all-powerful." (§1).
Pearce: "This question is known as the Paradox of the Stone, or the Paradox of Omnipotence." (§1a), and he gives the general form, after Mackie: "More generally, could an omnipotent being make something it could not control (Mackie 1955: 210)?" (§1a; [Mackie 1955](https://doi.org/10.1093/mind/LXIV.254.200)).

**The dilemma.** Pearce's statement: "For suppose that the being cannot create the stone. Then it seems that it is not omnipotent, for there is something that it cannot do. But suppose the being can create the stone. Then, again, there is something it cannot do, namely, lift the stone it has created." (§1a).
Wikipedia, citing Savage (1967): "This question generates a dilemma. The being can either create a stone it cannot lift, or it cannot create a stone it cannot lift." … "In either case, the being is not omnipotent." Hoffman & Rosenkrantz put it in terms of states of affairs, with an agent named Jane: if she can make a stone of mass *m* she cannot move, she cannot bring about (S1) that the stone moves; if not, she cannot bring about (S2) that there is such a stone. "Thus, it seems that whether or not Jane can make the stone in question, there is some possible state of affairs that an omnipotent agent cannot bring about. And this appears to be paradoxical." (§2).

**Logic check (this implant, 2026-10-01; logic, not a position).** With
c for *the being can create a stone it cannot lift* and o for *the being is
omnipotent*, the dilemma's two horns are c → ¬o and ¬c → ¬o.
`python3 _implant/skills/tools/logic.py check --premises "c -> ~o" "~c -> ~o" --conclusion "~o"`
returns `VALID` (a constructive dilemma whose excluded middle, c ∨ ¬c, is a
tautology of [classical logic](../methods/classical-logic.md)). If the first
horn is instead read as Pearce reads it — only *making* the stone, m, would
leave something undone (m → ¬o) — then
`--premises "m -> ~o" "~c -> ~o" --conclusion "~o"` returns `INVALID` with
"Counterexamples (premises true, conclusion false):" `c=T, m=F, o=T` — a
being that can make the stone, does not, and is omnipotent. The tool checks
only the propositional skeleton; "can", time and necessity are outside it.
This is the formal shape of Pearce's remark under *Positions taken*.

## Why it matters

- **A test of the coherence of a divine attribute.** Hoffman & Rosenkrantz: "If the notion of omnipotence were found to be unintelligible, or incompatible with moral perfection, then traditional Western theism would be false." (§1). "The intelligibility of the notion of omnipotence has been challenged by the so-called paradox or riddle of the stone." (§2).
- **Driver of definitions.** Pearce: "The Stone Paradox has been the main focus of those attempting to specify exactly what an omnipotent being could, and could not, do." (§1a). He sorts the resulting definitions into "act theories, which say that an omnipotent being would be able to perform any action; and result theories, which say that an omnipotent being would be able to bring about any result." (§1a).
- **Which God-concept it touches.** Pearce: "Nevertheless, the Stone Paradox is of interest because necessary omnitemporal omnipotence has traditionally been attributed to God." (§1a).
- **Neighbour of the problem of evil.** Pearce cites Mackie's 1955 "Evil and Omnipotence" for the general "make something it could not control" form (§1a); the same paper's argument from evil is reported on the [Epicurean trilemma](epicurean-trilemma.md) page.

## Positions taken

No position is ranked here. No survey figure is recorded. Groupings follow
the two encyclopedias.

- **Omnipotence ranges over the absolutely possible only (Aquinas).** "It remains therefore, that God is called omnipotent because He can do all things that are possible absolutely; which is the second way of saying a thing is possible." (ST I q.25 a.3, Dominican tr. 1920; excerpt: `raw/aquinas-st-1-q25-a3-omnipotence-contradiction.md`). "Therefore, everything that does not imply a contradiction in terms, is numbered amongst those possible things, in respect of which God is called omnipotent: whereas whatever implies contradiction does not come within the scope of divine omnipotence, because it cannot have the aspect of possibility. Hence it is better to say that such things cannot be done, than that God cannot do them." (ibid.). Hoffman & Rosenkrantz report Aquinas and Maimonides as holding the unrestricted sense "incoherent" (§1).
- **The stone is a self-contradictory task (Mavrodes 1963).** As quoted by Wikipedia: "On the assumption that God is omnipotent, the phrase "a stone too heavy for God to lift" becomes self-contradictory. For it becomes "a stone which cannot be lifted by Him whose power is sufficient for lifting anything."" and "...it is the very omnipotence of God which makes the existence of such a stone absolutely impossible, while it is the fact that I am finite in power that makes it possible for me to make a boat too heavy for me to lift." Pearce's summary: Mavrodes "Argues that an omnipotent being could not create a stone so heavy he could not lift it, since the notion of a stone too heavy to be lifted by an omnipotent being is incoherent." (references).
  - *Against:* Pearce: "However, this line of objection fails to recognize that, in addition to the impossible action creating a stone an omnipotent being cannot lift, there are also such possible actions as creating a stone one cannot lift and creating a stone its creator cannot lift." (§2) — Pearce's assessment. Cowan (1965), in Pearce's annotation: "Argues, against Mavrodes 1963, that the Stone Paradox cannot be solved by claiming that God can perform only logically possible tasks."
  - *For:* Hoffman & Rosenkrantz's "first resolution", for an essentially omnipotent agent: "Since, necessarily, an omnipotent agent can move any stone, no matter how massive, (S2) is impossible. But, as we have seen, an omnipotent agent is not required to be able to bring about an impossible state of affairs." (§2).
- **Essential omnipotence makes the stone impossible; accidental omnipotence makes both tasks possible at different times (Hoffman & Rosenkrantz).** "A first resolution of the paradox comes into play when Jane is an essentially omnipotent agent. In that case, the state of affairs of Jane’s being non-omnipotent is impossible." (§2). For the accidental case: "Thus, there is a second solution to the paradox." — "So, Jane can create and move a stone, \(s\), of mass, \(m\), while omnipotent, and subsequently bring it about that she is not omnipotent and powerless to move \(s\). As a consequence, Jane can bring about both (S1) and (S2), but only if they obtain at different times." (§2).
  - *Limit, as reported:* the authors also report an argument that "presupposes traditional Western theism": "Thus, on the assumption that God exists, an accidentally omnipotent being is impossible." (§1).
- **The argument is not valid as usually stated; it bites only on necessary omnitemporal omnipotence (Pearce; Swinburne 1973; Meierding 1980).** Pearce: "Although the argument is usually initially stated in this form, as it stands it is not quite valid. From the fact that a particular being is able to create a stone it cannot lift, it does not follow that there is in fact something that that being cannot do. It only follows that if the being were to create the stone, then there would be something it could not do." (§1a). "As a result, the paradox is a problem only for necessary omnitemporal omnipotence, that is, for the view that there is a being who exists necessarily and is necessarily omnipotent at every time (Swinburne 1973; Meierding 1980)." (§1a). Swinburne, in Pearce's annotation: "Argues that a result theory can, and an act theory cannot, defeat the Stone Paradox. However, it is conceded that the Paradox shows that no temporal being could be essentially omnipotent."
  - *Against act theories, per Pearce:* "The Stone Paradox is most effective against act theories." (§2); "However, the Paradox does show that on the contemplated theory no being could be necessarily omnitemporally omnipotent." (§2).
- **An omnipotent being can do the logically impossible too (Descartes as read by Frankfurt; Frankfurt 1964).** Frankfurt, as quoted by Wikipedia: "But if God is supposedly capable of performing one task whose description is self-contradictory—that of creating the problematic stone in the first place—why should He not be supposedly capable of performing another—that of lifting the stone? After all, is there any greater trick in performing two logically impossible tasks than there is in performing one?" Pearce: "If this doctrine is adopted, then the Stone Paradox is dissolved: If an omnipotent being could make contradictions true, then an omnipotent being could make a stone too heavy for it to lift and still lift it (Frankfurt 1964)." (§1b). Descartes, quoted by Cunning ([SEP Fall 2024 "Descartes' Modal Metaphysics"](https://plato.stanford.edu/archives/fall2024/entries/descartes-modal/), n. 9; excerpt: `raw/sep-descartes-modal-fall-2024-frankfurt-eternal-truths.md`): "I do not think that we should ever say of anything that it cannot be brought about by God. For since every basis of truth and goodness depends on his omnipotence, I would not dare to say that God cannot make a mountain without a valley, or bring it about that 1 and 2 are not 3." (to Arnauld, 29 July 1648, AT 5:224). Among contemporaries, Hoffman & Rosenkrantz report: "Earl Conee (1991) rejects this principle in order to defend the view that an omnipotent being would have the power to bring about any state of affairs whatsoever." (§1).
  - *Against:* Pearce: "However, this doctrine is of questionable coherence." (§1b), via the modal step "In standard modal logics, possibly p and necessarily if p then q together entail possibly q, so it seems to follow that possibly 2 x 4 = 9." (§1b), and "These sorts of absurdities have led to the nearly universal rejection of voluntarism by philosophers and theologians." (§1b) — Pearce's assessment and report. Hoffman & Rosenkrantz: "Many philosophers accept the principle that if an agent has the power to bring about a state of affairs, then this entails that, possibly, the agent brings about that state of affairs. If this principle is correct, then the foregoing absolute sense of ‘omnipotence’ is incoherent." (§1).
- **First- and second-order omnipotence (Mackie 1955).** As Wikipedia reports it: "In a 1955 article in the philosophy journal Mind, J. L. Mackie tried to resolve the paradox by distinguishing between first-order omnipotence (unlimited power to act) and second-order omnipotence (unlimited power to determine what powers to act things shall have)."

## Arguments in play

(none recorded as separate argument pages yet). The stone dilemma is laid
out under *The question* with its propositional check. Wikipedia's reference
note on the 1978 anthology *The Power of God* (Urban & Walton eds.) records
further formal treatments not read here: "Keene and Mayo disagree p. 145, Savage provides three formalizations pp. 138–41, Cowan has a different strategy p. 147, and Walton uses a whole separate strategy pp. 153–63".
Pearce adds a second task: "Another possible task which an omnipotent being can apparently not perform is coming to know that one has never been omnipotent." (§1a). He generalises: "The Stone Paradox provides an example of two tasks (creating a stone its creator cannot lift and lifting the stone one has just created) such that each task is logically possible, but it is logically impossible for one task to be performed immediately after the other." (§1a).
Hoffman & Rosenkrantz list Mele & Smith, "The New Paradox of the Stone" (1998), in their bibliography.

## Thinkers who addressed it

- **Dionysius the Areopagite** (so named in Parker's 1897 title; dated "before 532" by Wikipedia) — Wikipedia: he "has a predecessor version of the paradox, asking whether it is possible for God to "deny himself"." In Parker's 1897 translation (*Divine Names* VIII.6; excerpt: `raw/pseudo-dionysius-divine-names-8-6-elymas-parker.md`): "Yet Elymas, the Magician, says, "if Almighty God is All-powerful, how is He said by your theologian, not to be able to do some thing "? But he calumniates the Divine Paul, who said, "that Almighty God is not able to deny Himself."" His reply: "For, the denial of Himself, is a falling from truth, but the truth is an existent, and the falling from the truth is a falling from the existent."
- **Saadia Gaon** (10th c.) — Wikipedia dates the paradox "at least to the 10th century, when Saadia Gaon responded to the question of whether God's omnipotence extended to logical absurdities." Not read here.
- **Averroes** (Ibn Rushd) — Wikipedia: "It was later addressed by Averroes and Thomas Aquinas.", citing *Tahafut al-Tahafut* "sections 529–536" (Van Den Bergh tr.). In the passage read (excerpt: `raw/averroes-tahafut-al-tahafut-natural-sciences-the-impossible.md`; correspondence to those section numbers unverified), the text Averroes quotes from Ghazali answers "that the impossible cannot be done by God, and the impossible consists in the simultaneous affirmation and negation of a thing", and Averroes reports that "some of the Muslims have even affirmed that there can be attributed to God the power to combine the two opposites", replying: "For such people it follows as a consequence that neither intellect nor existents have a well-defined nature, and that the truth which exists in the intellect does not correspond to the existence of existing things."
- **Thomas Aquinas** — ST I q.25 a.3, above; his objection 2 already raises that God "cannot sin, nor "deny Himself"", answered: "Therefore it is that God cannot sin, because of His omnipotence." (ad 2).
- **Maimonides** — *Guide* I.15, with Aquinas, as Hoffman & Rosenkrantz report (§1).
- **[René Descartes](../thinkers/descartes.md)** — Pearce: "René Descartes, almost alone in the tradition of Western theology, held that God could do anything, even affirming that “God could have brought it about … that it was not true that twice four make eight” (Descartes 1984-1991: 2:294)." (§1b); Hoffman & Rosenkrantz: "Descartes seems to have had such a notion (Meditations, Section 1)." (§1).
- **J. L. Mackie** (1955), **George I. Mavrodes** (1963), **Harry G. Frankfurt** (1964, 1977), **J. L. Cowan** (1965), **C. Wade Savage** (1967), **Richard Swinburne** (1973), **Meierding** (1980), **Earl Conee** (1991), **A. Mele & M. P. Smith** (1998) — modern discussion, as reported above.
- **Joshua Hoffman & Gary Rosenkrantz**; **Kenneth L. Pearce** — encyclopedia authors with analyses of their own (maximal power over states of affairs; result vs. act theories).

## Framings and reframings

- **Universal possibilism (Descartes as read by Frankfurt 1977).** Cunning: "On this interpretation, developed and defended by Harry Frankfurt, all eternal truths are inherently contingent because they could have been false, and they could have been false because God could have made their contradictories true." and "On Frankfurt’s view, Descartes holds that God is omnipotent in the sense that He can do anything at all and has authority over even the eternal truths." ([doi:10.2307/2184161](https://doi.org/10.2307/2184161)). Cunning's assessment: "If Descartes holds that eternal truths are necessary in any robust sense, Frankfurt’s view has an obvious drawback." Pearce reports Curley (1984) suggesting Descartes "may be implicitly committed to the rejection of one or more widely accepted modal axioms" (§1b).
- **Absolute vs. maximal power.** Hoffman & Rosenkrantz distinguish the sense "of having the power to bring about any state of affairs whatsoever, including necessary and impossible states of affairs" from "A second sense of ‘omnipotence’ is that of maximal power, meaning just that no being could exceed the overall power of an omnipotent being." (§1).
- **Act vs. result theories** (Pearce §1a), quoted under *Why it matters*.
- **Name.** "This modern version is referred to as the Paradox of the Stone." (Wikipedia); "the so-called paradox or riddle of the stone" (Hoffman & Rosenkrantz §2); "the Paradox of the Stone, or the Paradox of Omnipotence" (Pearce §1a).
- **Related problem pages:** [the Epicurean trilemma](epicurean-trilemma.md),
  [the Euthyphro dilemma](euthyphro-dilemma.md), [Russell's paradox](russells-paradox.md),
  [the liar paradox](liar-paradox.md), [the argument from free will](argument-from-free-will.md).

## Vocabulary

- [Paradox](../vocabulary/paradox.md); [dilemma](../vocabulary/dilemma.md) — the stone argument is a constructive dilemma (logic check above).
- [Validity](../vocabulary/validity.md); [classical logic](../methods/classical-logic.md) — Pearce's "not quite valid" turns on "can make" vs. "makes".
- *Omnipotence*, *essential vs. accidental omnipotence*, *voluntarism*, *universal possibilism*, *eternal truths*, *state of affairs*, *absolute possibility* — open work in [vocabulary](../vocabulary/index.md).

Related thinkers: [Aquinas](../thinkers/aquinas.md) (ST I q. 25), [Epictetus](../thinkers/epictetus.md) (Graver SEP §4.8).
