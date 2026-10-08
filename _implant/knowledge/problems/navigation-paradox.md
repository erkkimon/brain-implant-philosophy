---
type: article
about: concept
title: "Navigation paradox"
description: "Can more precise navigation make collisions more likely? Machol's attribution of the term to Reich (1964/1966, as Wikipedia reports it), Paielli's 2000 simulation of the hemispheric altitude rule against a linear rule, Patlovany's 1997 abstract, and the lateral form that ICAO's strategic lateral offset answers (Werfelman 2007)."
tags: [problem, paradox, decision-theory, aviation-safety, risk]
timestamp: 2026-10-08T21:37:56Z
---

# Navigation paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Every technical and empirical claim below is its named author's claim, from the text or abstract cited.
Primary text read: Russell A. Paielli, "A Linear Altitude Rule for Safer and More Efficient Enroute Air Traffic",
*Air Traffic Control Quarterly* 8(3), 2000, pp. 195–221
([doi:10.2514/atcq.8.3.195](https://doi.org/10.2514/atcq.8.3.195); author's copy
[russp.org/altrules.pdf](https://russp.org/altrules.pdf), read by OCR;
excerpt: `raw/paielli-2000-linear-altitude-rule-navigation-paradox.md`).
Practice report read: Linda Werfelman, "Sidestepping the Airway", *AeroSafety World*, March 2007, pp. 40–45
([PDF](https://flightsafety.org/asw/mar07/asw_mar07_p40-45.pdf);
excerpt: `raw/werfelman-2007-sidestepping-the-airway-lateral-offsets.md`).
Known only bibliographically or by abstract: Machol 1995, Reich 1966, Patlovany 1997
(record: `raw/navigation-paradox-bibliographic-records.md`).
Admitted from Wikipedia's List of paradoxes, revision 1376699902, "Decision theory";
Wikipedia's article ([rev. 1331727373](https://en.wikipedia.org/w/index.php?title=Navigation_paradox&oldid=1331727373))
is used as a pointer to sources and cited as such
(excerpt: `raw/wikipedia-navigation-paradox-rev-1331727373-and-list-entry.md`).

## The question

Wikipedia's list: "Navigation paradox: Increased navigational precision may result in increased collision risk." (List of paradoxes, rev. 1376699902).
The question, in that wording: when two craft lose separation in one dimension, can greater precision in keeping to an assigned path, level or route make a collision more likely rather than less?

Two dimensions appear in the sources read:

- **Vertical (cruising levels).** Paielli: "Under the discrete rule, however, better altitude accuracy means higher probability of collision between aircraft at the same nominal altitude, because if they lose horizontal separation they are less likely to “accidentally” avoid each other vertically." (2000, p. 2).
- **Lateral (route centrelines).** ICAO's Doc 4444, as quoted by Werfelman: "“The use of highly accurate navigation systems, such as the global navigation satellite system (GNSS), by an increasing proportion of the aircraft population has had the effect of reducing the magnitude of lateral deviations from the route centerline and, consequently, increasing the probability of a collision should a loss of vertical separation between aircraft on the same route occur.”" (2007, p. 43; Doc 4444 itself not read here).

**Structural note (this implant, 2026-10-09; logic, not a position).** Both
statements have the same conditional shape. Let *A* stand for *navigation in
one dimension is more accurate*, *V* for *craft that lose separation in the
other dimensions are less likely to miss each other by chance in this one*,
and *C* for *collision is more likely, given a loss of separation elsewhere*.
`logic.py check --premises "A -> V" "V -> C" --conclusion "A -> C"` outputs
`VALID` and `matches schema: hypothetical syllogism`. The converse does not
follow: `"A -> C"` against `"C -> A"` outputs `INVALID` with the counterexample
row `A=F, C=T`. The tool checks the propositional form only; whether the
premises hold is what the simulations and reports below address.

## Why it matters

- **Altitude rules.** Paielli: "By concentrating all enroute traffic into a few altitudes, this discrete altitude rule makes the enroute air traffic system less fail-safe and less fault-tolerant than it could be." (2000, abstract). On the hemispheric rule: "Although this “hemispheric” or “semi-circular” discrete altitude rule automatically separates easterly traffic from westerly traffic, it does nothing to separate traffic in each of the two categories from itself." (p. 1).
- **Fail-safe design.** Paielli sets the question beside engineered systems: "If power is lost to the control rods in a nuclear power plant, they fall into a position in which they stop the main fission reaction." (p. 1), followed by railroad gates and elevator brakes.
- **Route centrelines.** Werfelman reports the challenge to an assumption: "Some voices in the aviation industry are challenging the traditional belief that the centerline of an airway is the safest position for an airplane." (2007, p. 40). Voss (Flight Safety Foundation): "“Where airplanes used to be spread over a mile, they are now within a few feet of the centerline,” Voss said." (p. 41).
- **A case cited in the debate.** Werfelman on the Gol/Embraer collision over the Amazon, 29 September 2006: "The crash occurred while the two airplanes, which were being flown in opposite directions, were on the same airway and at the same altitude." (p. 44).
- **Classification.** Wikipedia files it under "Decision theory" in its list; its article's short description is "Phenomenon in aviation safety" (rev. 1331727373).

## Positions taken

No grouping of responses was found in the sources read; the responses on
record are listed by owner, unranked. They are engineering and operational
proposals, reported as their authors' claims.

- **Spread levels by heading: a linear altitude rule (Collins 1968, Patlovany 1997, Paielli 2000).** Paielli: "Collins [4] and Patlovany [5] each identified the problem with the current discrete altitude rule and proposed that cruising altitudes should be a linear function of heading." (pp. 1–2). His proposal: "The linear altitude rule proposed in this paper designates cruising altitudes as a linear function of heading or course." (abstract). Under it, per Paielli: "Under the linear altitude rule, better altitude accuracy means decreased probability of collision, as will be shown later." (p. 2). Collins's *Air Facts* article (31(2), 1968) is known here only from Paielli's reference list.
- **Random altitudes, as a comparison case (Patlovany 1997, as reported by Paielli; Paielli 2000).** Paielli on Patlovany: "He found that simply letting aircraft fly at random altitudes reduces the collision rate substantially compared to the discrete rule." (p. 2). Paielli's own qualification: "Although the random altitude rule reduces the collision rates compared to the discrete rule, Tables 6 and 7 show that it substantially increases the mean relative speed of collisions." (pp. 9–10).
- **Strategic lateral offsets (ICAO North Atlantic Systems Planning Group, c. 2000; Doc 4444, as reported by Werfelman 2007).** Offsets of 1 or 2 nm to the right of course; Gardilčić (ICAO): "In other words, this would artificially degrade the accuracy of navigation systems so if there was a vertical error, aircraft would not be precisely on the centerline and possibly collide." (p. 42). Peguero (Airways New Zealand): "The offset achieves a controlled degrade of the navigation accuracy so that a small degree of horizontal distancing is created in case vertical application by the ANSP [air navigation services provider] has failed.”" (p. 45).
  *Reservations on record, per Werfelman:* "Others are discouraging wider use as unnecessary." (p. 40); Wright (U.K. NATS) on domestic airspace: "“We will need to consider the risk reduction and whether any new risks might be introduced, especially in busy Terminal Area airspace,” he said." (p. 45); Voss: "“What you don’t want is pilots doing random offsets,” he said." (p. 45).
- **Current systems adequate (Peguero, as reported by Werfelman).** "“These systems seen to work with no problem and are consistent with ICAO … standards for their use,” said Phil Peguero, safety director at Airways New Zealand." (p. 45; "seen" as printed). Werfelman also quotes him on the "irony" (see Framings).

## Arguments in play

(none recorded as separate argument pages yet). The evidence on record is simulation:

- **Paielli 2000 (his findings, under his model).** Setup: "For this paper, the region is a 500 by 500 nmi square with 200 aircraft, unless otherwise noted." (p. 8); 250,000 Monte Carlo runs per case, with no air traffic control. Result: "Note that, for the discrete altitude rule, better altitude accuracy actually causes a higher collision rate." (p. 9). His Table 3 (minimal collision threshold) gives discrete-rule counts of 17190, 10041, 6323 and 5175 at RMS total vertical error 25, 50, 75 and 100 ft; his Table 4 gives collision-rate reduction factors relative to the discrete rule of 5.0 / 3.3 / 1.8 / 1.4 for random altitudes and 33.8 / 13.9 / 5.8 / 4.8 for the linear rule (p. 9). His inference: "The linear rule is therefore an order of magnitude more fail-safe than the discrete rule in this simulation." (p. 9).
  *Arithmetic check (this implant, 2026-10-09; arithmetic, not a position).* Dividing his Table 3 counts: 17190 / 3425 = 5.02 and 17190 / 508 = 33.84, matching his 5.0 and 33.8 at 25 ft; 10041 / 721 = 13.93, matching 13.9 at 50 ft.
  *A trade-off Paielli reports against his own rule:* "Table 8, which is based on the same data used for Figure 12, shows that for the current horizontal separation standard of 5 nmi and the vertical separation standard of 1000 ft, the linear rule yields a conflict rate approximately triple (3.02 times) the baseline rate." (p. 11), and "This parabolic form explains the paradoxical fact that the linear rule increases the conflict rate while it decreases the collision rate." (p. 11).
- **Patlovany 1997 (abstract only, his findings).** "The calculations verify that: (1) federal rules increase collision course probabilities by about four times more than for a chaotic system of aircraft cruising at randomly selected altitudes, (2) risk is directly proportional to the level of compliance, and (3) mean closing velocities resulting from the current rule are slightly less than for random altitudes, while being almost twice as high as for the proposed rules." (*Risk Analysis* 17(2), 1997, abstract; [doi:10.1111/j.1539-6924.1997.tb00862.x](https://doi.org/10.1111/j.1539-6924.1997.tb00862.x)). Wikipedia's article reports his model as showing "six times more mid-air collisions than random cruising altitude" at zero altitude error (rev. 1331727373); the abstract read here says "about four times"; the full paper was not read, so the difference is recorded, not resolved.
- **Reported from practice, not measured.** Valdes (United Airlines, IFALPA/ALPA), as Werfelman reports him: "If the pilots of either airplane involved in the Amazon midair collision had been using offset procedures, he said, the crash wouldn’t have occurred." (p. 45).

## Thinkers who addressed it

Chronological; the field is aviation safety and operations research, and
none of the people below has a page here.

- **Peter G. Reich (1964 RAE reports; *Journal of Navigation* 19, 1966).** Credited with the term by Machol, per Wikipedia: Machol "attributes the term "navigation paradox" to Peter G. Reich, writing in 1964, and 1966, who recognized that "in some cases, increases in navigational precision increase collision risk"." (rev. 1331727373). Reich's papers: [doi:10.1017/s037346330004056x](https://doi.org/10.1017/s037346330004056x), [doi:10.1017/s0373463300047196](https://doi.org/10.1017/s0373463300047196), [doi:10.1017/s0373463300047445](https://doi.org/10.1017/s0373463300047445) — not read here; Crossref page ranges (88–98, 169–186, 331–347) differ from those Wikipedia gives.
- **L. H. Collins (*Air Facts*, 1968).** A heading-linked altitude rule, per Paielli (2000, pp. 1–2).
- **Robert E. Machol (*Interfaces* 25(5), 1995, pp. 151–172, p. 154 per Wikipedia).** A survey of collision risk models; its abstract: "These “collision risk models” were applied in the 1960s to determine safe separation standards between pairs of co-altitude aircraft on parallel courses over the North Atlantic Ocean." ([doi:10.1287/inte.25.5.151](https://doi.org/10.1287/inte.25.5.151)). Wikipedia quotes his p. 154: "that if vertical station-keeping is sloppy, then if longitudinal and lateral separation are lost, the planes will probably pass above and below each other. This is the ‘navigation paradox’ mentioned earlier." (rev. 1331727373; not checked against Machol's text).
- **Robert W. Patlovany (*Risk Analysis*, 1997).** Monte Carlo comparison of U.S. altitude rules, random altitudes and two proposed alternatives (abstract).
- **Russell A. Paielli (NASA Ames; *ATCQ*, 2000).** The linear altitude rule and the simulation above; uses the label "navigation paradox" for the discrete-rule effect (p. 9).
- **ICAO North Atlantic Systems Planning Group; Doc 4444, 15.2.4 (as reported by Werfelman 2007).** The strategic lateral offset procedure, extended to oceanic and remote airspace worldwide.

## Framings and reframings

- **"Has been called" a paradox.** Paielli does not claim the label: "This effect has been called the “navigation paradox,” because pilots are “rewarded” with a higher danger of collision for following the rule more diligently." (2000, p. 9; no citation in the sentence). He uses "paradoxical" also for his own rule's conflict/collision trade-off (p. 11).
- **An "irony", not a paradox.** Peguero, as quoted by Werfelman: "“The irony of the situation is … that the greater the accuracy of navigation without an offset strategy, the greater the chance is these days of a collision if ATC gets it wrong." (2007, p. 45). The article does not use the phrase "navigation paradox".
- **A property of the rule, not of precision.** On Paielli's account the effect depends on the altitude rule: "Under the linear rule, on the other hand, better altitude accuracy causes a lower collision rate." (p. 9). On Gardilčić's account the lateral offset reintroduces "additional ‘randomness’" (Werfelman, p. 42) while keeping accuracy.
- **Wikipedia's article.** It carries "technical" (2013) and "Original research" (2013) maintenance tags; sentences there saying the current rules "institutionalize the navigation paradox on a worldwide basis" and could have saved "342 lives" rest on a Patlovany web page not read here and are not reported as facts (rev. 1331727373). It also places Paielli's model "centered on Denver, Colorado"; the paper gives a 500 by 500 nmi region and mentions Denver Center for heading distributions (p. 10).

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — the label is applied by Machol (as quoted by Wikipedia) and reported by Paielli as "has been called"; Peguero's word is "irony".
- Terms used as the sources define them: *discrete (hemispheric, semicircular) altitude rule*, *linear altitude rule*, *total vertical error (TVE)* (Paielli 2000, pp. 1–2), *strategic lateral offset* (Werfelman 2007, pp. 40–43); no vocabulary pages yet.
