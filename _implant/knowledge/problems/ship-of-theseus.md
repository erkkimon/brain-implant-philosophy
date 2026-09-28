---
type: article
about: concept
title: "The Ship of Theseus"
description: "Plutarch's report of the Athenian ship repaired plank by plank, Hobbes's addition of a second ship rebuilt from the old planks, and the identity puzzles they pose — transitivity, fission and coincident objects — with the responses on record: constitution, mereological essentialism, strict and loose identity, relative identity, four-dimensionalism and stage theory, temporary and indeterminate identity, best candidate, and deflationism, each with its owner."
tags: [problem, paradox, metaphysics, ancient-philosophy, early-modern-philosophy]
timestamp: 2026-09-28T07:01:48Z
---

# The Ship of Theseus

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
claim grades as in [How claims are graded](../../conventions/how-claims-are-graded.md).
Part of the [problems](./index.md) branch. Map: Andre Gallois,
[SEP Fall 2024 "Identity Over Time"](https://plato.stanford.edu/archives/fall2024/entries/identity-time/)
(revised 2016-10-06; excerpt: `raw/sep-identity-time-fall-2024-ship-of-theseus-and-responses.md`);
Ryan Wasserman, [SEP "Material Constitution"](https://plato.stanford.edu/archives/fall2024/entries/material-constitution/)
(revised 2021-09-09; excerpt: `raw/sep-material-constitution-fall-2024-ship-of-theseus-and-five-replies.md`);
Harry Deutsch & Pawel Garbacz, [SEP "Relative Identity"](https://plato.stanford.edu/archives/fall2024/entries/identity-relative/)
(revised 2022-12-06; excerpt: `raw/sep-identity-relative-fall-2024-ship-of-theseus-paradox.md`);
Katherine Hawley, [SEP "Temporal Parts"](https://plato.stanford.edu/archives/fall2024/entries/temporal-parts/)
(revised 2020-05-05; excerpt: `raw/sep-temporal-parts-fall-2024-ship-coincidence-and-conventionalism.md`).

## The question

Is a thing whose parts have all been replaced the same thing? Hawley (SEP
§1) puts it: "What happens to a ship if you replace all of its planks one by one? What if you keep the old planks, then build a new ship out of them?"

**Plutarch** (*Theseus* 23.1, Perrin's 1914 Loeb translation, public domain,
via [LacusCurtius](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Plutarch/Lives/Theseus*.html);
excerpt: `raw/plutarch-theseus-23-1-ship-perrin.md`): "The ship on which Theseus sailed with the youths and returned in safety, the thirty-oared galley, was preserved by the Athenians down to the time of Demetrius Phalereus. They took away the old timbers from time to time, and put new and sound ones in their places, so that the vessel became a standing illustration for the philosophers in the mooted question of growth, some declaring that it remained the same, others that it was not the same vessel."
Perrin's note dates Demetrius: "Regent of Athens for Cassander of Macedon, 317‑307 B.C." Plutarch's text
contains no reassembly. Deutsch & Garbacz (§2.5) quote a second translation,
by Michael Rea (Rea 1995, p. 531, [doi:10.2307/2185816](https://doi.org/10.2307/2185816)):
"a model for the philosophers with respect to the disputed arguments".

**Hobbes** (*De Corpore* II.11.7, 1655; Molesworth, *English Works* I, 1839,
pp. 135–138, [archive.org](https://archive.org/details/englishworksofth0001hobbes);
excerpt: `raw/hobbes-1655-de-corpore-2-11-7-ship-of-theseus-molesworth.md`)
sets the ship inside "a great controversy among philosophers about the beginning of individuation", and adds the second ship: "if some man had kept the old planks as they were taken out, and by putting them afterwards together in the same order, had again made a ship of them, this, without doubt, had also been the same numerical ship with that which was at the beginning; and so there would have been two ships numerically the same, which is absurd."
He names the disputants as "the sophisters of Athens". Deutsch & Garbacz
(§2.5): "Hobbes added the catch that the old parts are reassembled to create another ship exactly like the original. Both the restored ship and the reassembled one appear to qualify equally to be the original."

**Modern statement.** Gallois (§4) names the rebuilt-with-new-planks ship
*Replacement* and the ship built from the old planks *Reassembly*, and writes: "Saying that, in the case of Theseus' ship, Replacement and Reassembly are both identical with the original ship putatively conflicts with the transitivity of identity since Replacement seems to be later clearly distinct from Reassembly."
He classes it as "a fission case", "The best known example of a symmetrical
fission case" (§4.7). Wasserman (§1) runs the story with a museum and a
custodian: "Both answers seems correct, but this means that, at the end of the story, the ship of Theseus is in two places at once."
Working backwards: "at the beginning of the story, there were two ships of
Theseus occupying the same place at the same time". He groups it with the
Debtor's Paradox, Dion and Theon, and the statue and the clay: "These four
puzzles differ in details, but raise a common problem."

**Logic check** (this implant, 2026-09-27; logic, not a position). Read as
four sentences — Replacement is Original; Reassembly is Original; if both,
Replacement is Reassembly (transitivity with symmetry); Replacement is not
Reassembly — `python3 _implant/skills/tools/logic.py check` returns for the
set "VALID / premises are jointly inconsistent — argument is vacuously
valid"; from the last two alone, "~Rep_eq_Orig | ~Reas_eq_Orig" returns
"VALID". Each position below rejects or reinterprets one of the four.

## Why it matters

- Hobbes attaches civil stakes to the matter criterion: the sinner and the punished would not be "the same man", which "were to confound all civil rights" (p. 136).
- Gallois (§4): "Identity is, very plausibly, an equivalence relation"; the ship puts transitivity in question. He adds (§4.7): "The puzzle cases are puzzle cases because they bring into putative conflict intuitions all of which we want to subscribe to."
- Gallois (§5) reports that fission cases like the ship bear on personal
  identity: hemispheric division "is taken by many to show that the
  psychological continuity criterion is, after all, incompatible with the
  transitivity of identity (Nagel 1975)".
- Hawley (§1): "the answers that philosophers give to these questions can often depend upon whether they believe in temporal parts."

## Positions taken

In the order of Wasserman's five replies (§1) and Gallois's §4.7. None is
ranked here.

- **Hobbes: identity depends on the name.** After rejecting individuation by matter alone, form alone and the aggregate of accidents ("a man standing would not be the same he was sitting", p. 137), Hobbes writes: "Wherefore the beginning of individuation is not always to be taken either from matter alone, or from form alone."
  "But we must consider by what name anything is called, when we inquire concerning the identity of it. For it is one thing to ask concerning Socrates, whether he be the same man, and another to ask whether he be the same body" (p. 137); "that will be the same river which flows from one and the same fountain, whether the same water, or other water, or something else than water, flow from thence" (pp. 137–138).
- **Constitution (coincident objects).** Wasserman (§2) describes "The most
  popular reply" as accepting that the statue is not the lump; "In a slogan:
  constitution is not identity (Johnston 1992)"; he lists defenders from
  "Wiggins (1968), Doepke (1982), Lowe (1983, 1995, 2003)" to "Baker (1997,
  2000, 2002)" and "Fine (2003)". Gallois (§4.1): "Defenders of such accounts hold that constitution, unlike identity, is not an equivalence relation (Baker 2002)."
  Applied to the ship: "the reassembly ship is never identical, but only constituted from exactly the same planks as, the original." *Against:* Gallois (§4.1) reports "Some think it engages in metaphysical multiple vision, seeing a multiplicity of things at a given place and time where there is plausibly only one. Others argue that constitution is identity (see Noonan 1993)."
  Gallois (§4.7) judges that "Constitution only delivers a candidate solution in a symmetric fission case."
- **Mereological essentialism (Chisholm).** Wasserman (§4): Chisholm (1973)
  "defends the doctrine of mereological essentialism: for any x and y, if x
  is a part of y then, necessarily, y exists only if x is a part of y";
  "The essentialist’s response to the paradox is to deny this apparent
  truism" that the ship survives replacement of some parts. Gallois (§4.3,
  citing Chisholm 1969a) reports the strict/loose distinction; on the ship
  (§4.7): "Reassembly is strictly identical with Original, but Replacement is only loosely identical with Original."
  *Against:* Wasserman (§4) writes that the picture "seems completely absurd,
  for it implies that if we annihilate a single particle of David, the entire
  statue will be destroyed". Deutsch & Garbacz (§2.5) report the view
  conflicts with "the common sense principle that (1) the material of an object can be totally replenished or replaced without affecting its identity (Salmon 1979)".
- **Relative identity (Geach, Griffin).** Wasserman (§6): "Geach’s central thesis is that there is no relation of absolute identity—identity is always relative to a kind." Gallois (§4.7): "The replacement ship is the same ship as the original, and the original is the same collection of planks as the reassembly ship. Conflict with transitivity is avoided because we need not allow that the reassembly ship is the same ship as the original."
  *Against:* Deutsch & Garbacz (§4.5) say of Griffin (1977): "This simply doesn’t resolve the problem.", since "the reassembled and remodeled ships have, prima facie, equal claim to be the original". Wasserman (§6): denying transitivity "would give us another reason to suspect that relativized identity relations are not really identity relations at all (Gupta 1980)".
- **Deutsch & Garbacz: a further relativity.** "To resolve the problem, we need an additional level of relativity." (§4.5): "\(x\) and \(y\) are the same relative to z, if both \(x\) and \(y\) differ from \(z\) at most by a single part."
  They cite Gupta (1980) and Williamson (1990) as related approaches.
- **Four-dimensionalism / perdurance (Lewis, Sider).** Hawley (§2): "Perdurantists believe that ordinary things like animals, boats and planets have temporal parts (things persist by ‘perduring’)."
  Gallois (§4.7): "Here is what a four dimensionalist such as Lewis will say about Theseus' ship. […] In that case there are two initially indiscernible ships." — "a Y-branching four dimensionally extended object". Sider (2002, per Gallois §4.5) argues from vagueness "that it cannot be vague how many things there are".
- **Stage theory (Sider, Hawley).** Gallois (§4.5): "Sider and Katherine
  Hawley defend an alternative version of Four Dimensionalism which
  identifies objects with what, on the first version, would qualify as their
  stages (Hawley 2001, Sider 2002)"; for fission, "the stage theorist can
  say there is a single present person who will be identical with each of a
  pair of later individuals". Hawley (§2): "when we talk about ordinary objects like boats and people, we talk about brief temporal parts or ‘stages’ of four-dimensional objects."
- **Temporary identity (Myro, Gallois).** Gallois (§4.7): "A temporary identity theorist will hold that Replacement and Reassembly are identical at t1, but distinct ships at t2."
- **Indeterminate identity.** Gallois (§4.7): if the Evans–Salmon argument
  (Evans 1978, Salmon 1981) "can be met", "Each of Replacement and Reassembly is indeterminately identical with Original."
- **Spatio-temporal continuity; best candidate.** Deutsch & Garbacz (§2.5): "Some are convinced that the remodeled ship has the best claim to be the original, since it exhibits a greater degree of spatio-temporal continuity with the original (Wiggins 1967)."
  They add "it is unclear why" that intuition "should take precedence", and report "more sophisticated “best candidate” theories that are not vulnerable to this objection (Nozick 1982)."
- **Identity is not what matters.** Deutsch & Garbacz (§2.5): "Perhaps we should conclude that identity is not what matters." — "Parfit (1984) develops such a response in detail" for persons.
- **Deflationism / conventionalism.** Wasserman (§1): the issues are "in some sense verbal, so that there is no fact of the matter about which premise (if any) is false"; the view "is often associated with Rudolf Carnap (1950), Hilary Putnam (1987) and, more recently, Eli Hirsch (2002a, 2002b, 2005)" (§7). Hawley (§5): "Many believe that we set the standards for how many repairs you can make to your bicycle without destroying it". *Against:* Wasserman (§7) reports the deflationist's translations are "hostile" (Sider 2009), so "the issues involved here are more complicated than those in paradigm verbal disputes".
- **Compatibilism (Sattig).** Gallois (§4.7): "Thomas Sattig argues for a compatibilist view according to which we can hold on to both intuitions without giving up, or modifying, Leibniz's Law. We can do so by relativising identities to different perspectives."

**Survey.** The 2020 PhilPapers Survey has no ship question. On the
coincidence question Wasserman groups with it, "Statue and lump: one thing
or two things?", all respondents: one thing 30.13%, two things 41.84%, other
28.97%, N = 956 (inclusive figures; excerpt:
`raw/philpapers-2020-survey-statue-and-lump.md`).

## Arguments in play

(none recorded as separate argument pages yet). Stated above: the
transitivity argument (Gallois §4), the two-places / two-ships argument
(Wasserman §1), and the Kripkean necessity-of-origin argument applied to the
ship by Deutsch & Garbacz (§2.5), who add: "As indicated, Kripke denies that his argument (for the necessity of origin) applies to the case of change over time: “The question whether the table could have changed into ice is irrelevant here” (Kripke 1972, p. 351)."

## Thinkers who addressed it

- **Plutarch** (*Theseus* 23.1) — the report; **Thomas Hobbes** (1655) — the
  reassembly and the name-relative answer.
- **Roderick Chisholm** (1969, 1973) — strict/loose identity, mereological
  essentialism; **Peter Geach** (1967), **N. Griffin** (1977) —
  relative identity; **David Wiggins** (1967, 1968) — continuity, constitution.
- **David Lewis** (1976) — four-dimensionalism; **T. Sider** (2001,
  2002, 2009), **Katherine Hawley** (2001) — four-dimensionalism, stage theory.
- **Lynne Rudder Baker** (1997–2002), **M. Johnston** (1992), **H.
  Noonan** (1993), **Michael Burke** (1992) — constitution and its critics.
- **George Myro**, **Andre Gallois** (1998) — temporary identity; **Gareth
  Evans** (1978), **Nathan Salmon** (1979, 1981); **Kripke** (1972, 1980); **Robert
  Nozick** (1982); **D. Parfit** (1984); **Thomas Sattig**.
- **Rudolf Carnap** (1950), **Hilary Putnam** (1987), **Eli Hirsch** (2002) —
  deflationism; **Michael Rea** (1995); **Harry Deutsch & Pawel Garbacz**.

## Framings and reframings

- **Growth, not identity.** Plutarch files the ship under "the mooted question of growth"; Hobbes under "the beginning of individuation".
- **Fission.** Gallois (§4.7) treats the ship as symmetrical fission and
  notes "Four Dimensionalism, like the thesis that identities can be temporary, applies to both symmetric and asymmetric cases of fission."
- **Same-kind coincidence.** Hawley (§4.1): "some versions of the ‘ship of Theseus’ problem have this form"; "(The claim that same-kind coincidence is impossible is sometimes called ‘Locke’s thesis’.)"
  Wasserman (§5) writes that since "there is a single kind at issue in that case, the question of dominance does not arise and Burke’s account cannot help."
- **Criteria of identity.** Deutsch & Garbacz (§2.5): "Some have proposed that in a case like this our ordinary “criteria of identity” fail us."
- **No problem about identity.** Lewis (1986), quoted by Gallois (§1): "Identity is utterly simple and unproblematic."
- **Related pages:** [sorites](sorites-paradox.md) (vagueness, cf. Sider's
  argument), [Zeno's paradoxes](zenos-paradoxes.md), [liar](liar-paradox.md).

## Vocabulary

- [Paradox](../vocabulary/paradox.md); [validity](../vocabulary/validity.md);
  [classical logic](../methods/classical-logic.md).
- *Transitivity*, *Leibniz's Law*, *constitution*, *perdurance*,
  *endurance*, *temporal part*, *stage*, *mereological essentialism*,
  *relative identity*, *fission* — open work in
  [vocabulary](../vocabulary/index.md).
