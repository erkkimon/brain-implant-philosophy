# Paielli 2000 — the linear altitude rule and the "navigation paradox" under the discrete rule

Source: Russell A. Paielli (NASA Ames Research Center), "A Linear Altitude Rule
  for Safer and More Efficient Enroute Air Traffic", Air Traffic Control
  Quarterly 8(3), Fall 2000, pp. 195–221; author's PDF (13 pp., dated 9/19/00).
Original: doi:10.2514/atcq.8.3.195 (verified by DOI content negotiation:
  AIAA, ATCQ 8(3), 2000, pp. 195–221); author's copy https://russp.org/altrules.pdf
  (linked from https://russp.org/publist.html) (copyrighted; excerpts only)
Retrieved: 2026-10-09 (the PDF's text layer is an undecodable Type 3 font;
  text read by OCR (rapidocr) of 200/300 dpi page images, column by column;
  word spacing lost by OCR restored below; table figures re-checked at 300 dpi)

> "By concentrating all enroute traffic into a few altitudes, this discrete altitude rule makes the enroute air traffic system less fail-safe and less fault-tolerant than it could be."  (abstract, p. 1)

> "The linear altitude rule proposed in this paper designates cruising altitudes as a linear function of heading or course."  (abstract, p. 1)

> "Although this “hemispheric” or “semi-circular” discrete altitude rule automatically separates easterly traffic from westerly traffic, it does nothing to separate traffic in each of the two categories from itself."  (Introduction, p. 1)

> "If power is lost to the control rods in a nuclear power plant, they fall into a position in which they stop the main fission reaction."  (Introduction, p. 1; followed by railroad crossing gates and elevator brakes as further "fail-safe, fault-tolerant designs")

> "Collins [4] and Patlovany [5] each identified the problem with the current discrete altitude rule and proposed that cruising altitudes should be a linear function of heading."  (Introduction, pp. 1–2; [4] Collins, L. H., "Automatic Altitude and Heading Separation", Air Facts 31(2), Feb. 1968, pp. 31–38; [5] Patlovany 1997)

> "He found that simply letting aircraft fly at random altitudes reduces the collision rate substantially compared to the discrete rule."  (p. 2, of Patlovany)

> "Patlovany's collision results are corroborated in this paper, and the broader implications of the linear altitude rule are also considered."  (p. 2)

> "Under the linear altitude rule, better altitude accuracy means decreased probability of collision, as will be shown later."  (p. 2)

> "Under the discrete rule, however, better altitude accuracy means higher probability of collision between aircraft at the same nominal altitude, because if they lose horizontal separation they are less likely to “accidentally” avoid each other vertically."  (p. 2)

> "For this paper, the region is a 500 by 500 nmi square with 200 aircraft, unless otherwise noted."  ("Simulation", p. 8; 250,000 Monte Carlo runs per parameter set; TVE (total vertical error) modelled as Gaussian with RMS 0, 25, 50, 75 and 100 ft)

> "Note that, for the discrete altitude rule, better altitude accuracy actually causes a higher collision rate."  ("Simulation Results", p. 9)

> "This effect has been called the “navigation paradox,” because pilots are “rewarded” with a higher danger of collision for following the rule more diligently."  (p. 9; no citation in the sentence)

> "Under the linear rule, on the other hand, better altitude accuracy causes a lower collision rate."  (p. 9)

Table 3 (p. 9), collision counts, minimal threshold, 250,000 runs, 200 aircraft
FL300–FL400, 500 by 500 nmi, 30 min window; columns RMS TVE 25 / 50 / 75 / 100 ft:
  discrete 17190 / 10041 / 6323 / 5175; random 3425 / 3013 / 3531 / 3574;
  linear 508 / 721 / 1089 / 1082.
Table 4 (p. 9), collision rate reduction factors relative to the discrete rule
  (minimal threshold): random 5.0 / 3.3 / 1.8 / 1.4; linear 33.8 / 13.9 / 5.8 / 4.8.
Table 5 (p. 9), same, nominal threshold: random 2.8 / 2.9 / 2.2 / 1.7;
  linear 10.3 / 7.9 / 5.6 / 3.8.

> "The linear rule is therefore an order of magnitude more fail-safe than the discrete rule in this simulation."  (p. 9)

> "Although the random altitude rule reduces the collision rates compared to the discrete rule, Tables 6 and 7 show that it substantially increases the mean relative speed of collisions."  (pp. 9–10; OCR line break after "mean relative speed of" joined)

> "Table 8, which is based on the same data used for Figure 12, shows that for the current horizontal separation standard of 5 nmi and the vertical separation standard of 1000 ft, the linear rule yields a conflict rate approximately triple (3.02 times) the baseline rate."  (p. 11)

> "This parabolic form explains the paradoxical fact that the linear rule increases the conflict rate while it decreases the collision rate."  (p. 11)

> "Monte Carlo simulation results for enroute traffic with no air traffic control show that the linear rule greatly reduces both collision rates and the mean relative speed of collisions."  (Conclusion)

Relied on for: the mechanism Paielli gives for the navigation paradox under the
discrete (hemispheric) rule; the label as "has been called"; his proposed
linear rule and its simulation results (as his findings, under his
assumptions: no air traffic control, the stated region, traffic and error
models); the trade-off he reports (conflict rate up, collision rate down);
his attribution of the linear-rule idea to Collins 1968 and Patlovany 1997.
Context: the paper is an engineering proposal; Paielli writes that the rule
"might not be practical under the current regime" of static jet routes
(p. 2) and that heading distributions in Denver Center would make the
reduction factor smaller there than nationally (p. 10). The paper does not
cite Reich or Machol.
