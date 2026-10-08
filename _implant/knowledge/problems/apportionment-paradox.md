---
type: article
about: concept
title: "Apportionment paradox (Alabama, new states, population paradoxes)"
description: "When seats are divided among states in proportion to population, can a larger house cost a state a seat (Alabama, 1880), a new state move a seat between two others (Oklahoma, 1907), or a faster-growing state lose a seat to a slower one? The cases found under Hamilton's method, and Balinski and Young's impossibility theorem that no method both stays within the quota and avoids the population paradox."
tags: [problem, paradox, decision-theory, social-choice, apportionment, mathematics]
timestamp: 2026-10-08T20:29:06Z
---

# Apportionment paradox (Alabama, new states, population paradoxes)

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
sources graded as in [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Mathematical source: M. L. Balinski & H. P. Young, "The Theory of Apportionment",
IIASA Working Paper WP-80-131, September 1980
([PDF](http://pure.iiasa.ac.at/id/eprint/1338/1/WP-80-131.pdf); excerpt:
`raw/balinski-young-1980-theory-of-apportionment-iiasa.md`). Their book is
*Fair Representation: Meeting the Ideal of One Man, One Vote* (Yale University
Press, 1982, ISBN 0-300-02724-9; 2nd ed. Brookings Institution Press, 2001,
ISBN 0-8157-0111-X; both verified through Open Library, not read here).
History and secondary statements: Joseph Malkevitch, AMS Feature Column
"Apportionment" and "Apportionment II" (Wayback snapshots, excerpt:
`raw/malkevitch-ams-feature-column-apportionment.md`); Alexander Bogomolny,
["The Constitution and Paradoxes"](http://www.cut-the-knot.org/ctk/Democracy.shtml),
2002 (excerpt: `raw/bogomolny-2002-cut-the-knot-constitution-and-paradoxes.md`);
OpenStax, [*Contemporary Mathematics* §11.5](https://openstax.org/books/contemporary-mathematics/pages/11-5-fairness-in-apportionment-methods),
2023, CC BY 4.0 (excerpt: `raw/openstax-2023-contemporary-mathematics-apportionment-paradoxes.md`).
Admitted from Wikipedia's List of paradoxes, revision 1376699902, "Decision
theory", with its three sub-entries; Wikipedia's article
([rev. 1373595632](https://en.wikipedia.org/w/index.php?title=Apportionment_paradox&oldid=1373595632))
is used as a pointer to sources and cited as Wikipedia where quoted (excerpt:
`raw/wikipedia-apportionment-paradox-rev-1373595632-and-list-entry.md`).

## The question

The list entry: "Apportionment paradox: Some systems of apportioning representation can have unintuitive results due to rounding" (List of paradoxes, rev. 1376699902), with three sub-entries:
"Alabama paradox: Increasing the total number of seats might shrink one bloc's seats.";
"New states paradox: Adding a new state or voting bloc might increase the number of votes of another.";
"Population paradox: A fast-growing state can lose votes to a slow-growing state." (same revision).

The general problem, in Balinski & Young's terms: "Any problem in which h objects are to be allocated in non-negative integers proportionally to some numerical criterion belongs to this class, and the theory below applies to it." (1980, §1, PDF p. 3).
Wikipedia's article frames the tension: "Certain quantities, like milk, can be divided in any proportion whatsoever; others, such as horses, cannot—only whole numbers will do. In the latter case, there is an inherent tension between the desire to obey the rule of proportion as closely as possible and the constraint restricting the size of each portion to discrete values." (rev. 1373595632, lead).
OpenStax defines the apportionment paradox as "a situation that occurs when an apportionment method produces results that seem to contradict reasonable expectations of fairness." (§11.5).

**The three sub-paradoxes, in the sources' definitions.**

- *Alabama.* Bogomolny: "The Alabama paradox occurs when an increase in the total number of seats causes a state to lose one of its seats." (2002). Malkevitch: "one can get fewer seats in a larger house, with fixed population" ("Apportionment II", part 2).
- *Population.* Bogomolny: "The population paradox occurs when a state with a higher grows rate loses a seat to a state with a lower growth rate, when the apportionment is recalculated on the basis of new figures." (2002, sic).
- *New states.* Bogomolny: "The new-states paradox occurs when addition of a new state with a parallel increase in a fair amount of seats affects apportionment of other states." (2002).

**The method at issue.** Wikipedia's article gives Hamilton's method in four steps: "First, the fair share of each state is computed, i.e. the proportional share of seats that each state would get if fractional values were allowed." "Second, each state receives as many seats as the whole number portion of its fair share." "Third, any state whose fair share is less than one receives one seat, regardless of population, as required by the United States Constitution." "Fourth, any remaining seats are distributed, one each, to the states whose fair shares have the highest fractional parts." (rev. 1373595632, citing Stein 2008, p. 228, not read here).

**The quota property.** Balinski & Young: "It seems extremely natural to require that no state's apportionment should deviate from its quota by one or more seats; in other words, no state should get less than its quota rounded down" — the sentence goes on to the quota rounded up, and they call the property "staying within the quota" (1980, §6, PDF p. 58). Bogomolny's version: "The Quota Rule stipulates that any fair apportionment should assign to every state either its lower or upper quota." (2002).

**A worked example (Wikipedia's; arithmetic rechecked by this implant, 2026-10-08).** "The following is a simplified example (following the largest remainder method) with three states and 10 seats and 11 seats." (rev. 1373595632): populations 6, 6 and 2 (total 14). With 10 seats the fair shares are 10·6/14 ≈ 4.286, 4.286 and 10·2/14 ≈ 1.429; whole parts 4 + 4 + 1 = 9, so the one remaining seat goes to the largest fraction, 0.429 (state C): 4, 4, 2. With 11 seats the shares are ≈ 4.714, 4.714, 1.571; whole parts 4 + 4 + 1 = 9, and the two remaining seats go to the two largest fractions, 0.714 and 0.714 (A and B): 5, 5, 1. "Observe that state C's share decreases from 2 to 1 with the added seat." (Wikipedia, same section).

## Why it matters

- **US House apportionment.** Malkevitch reports that "In 1850 Vinton's method, in essence Hamilton's method, became law and this method remained on the books until the turn of the 20th century." and that "In 1901 Webster's method was used, reacting in part to the realization that Hamilton's method was subject to allowing a state to lose seats when the House of Representatives increased in size, the so-called Alabama paradox, and strange behavior when a new state was added to the union (known as the new state paradox)." ("Apportionment", part 2). Bogomolny: "Hamilton's method was replaced by Webster's in 1901, which stayed put until 1941, when Huntington-Hill's method was signed into law by President Roosevelt." (2002).
- **Fairness criteria as axioms.** Malkevitch on the Alabama case: it "called to the attention of politicians and others interested in apportionment that one had to worry about the fairness properties of the methods that one might use to solve the apportionment problem." ("Apportionment II", part 2). Wikipedia's article: "The Alabama paradox gave rise to the axiom known as house monotonicity, which says that, when the house size increases, the allocations of all states should weakly increase." and "The New State paradox gave rise to the axiom known as coherence, which says that, whenever an apportionment rule is applied to a subset of the states, with the subset of seats allocated to them, the outcome should be the same as in the overall solution for all states." (rev. 1373595632; the second sentence carries no reference there).
- **Beyond legislatures.** Balinski & Young's class covers any allocation of h objects in whole numbers proportional to a criterion (1980, §1, PDF p. 3, quoted above).
- **A link to social choice.** Malkevitch: "In particular, they followed in the footsteps of Kenneth Arrow's work in understanding fairness in voting and elections by looking in detail at fairness issues growing out of apportionment problems." ("Apportionment II", part 3; see [Arrow's impossibility theorem](arrows-impossibility-theorem.md)).

## Positions taken

No grouping of positions was found in the sources read; the claims on record
are listed by owner, unranked. Mathematical results are given in the
sources' wording.

- **Balinski & Young (1980): the impossibility theorem.** They introduce "the following "impossibility theorem", which says that no method can be population monotone and stay within the quota." (§6, PDF p. 58). Theorem 6.1 (PDF p. 59) states this for at least four states and a house of at least s+3 seats, with the method "population monotone and stays within the quota" excluded (the OCR of the inequality signs is garbled; see the raw file). Related results in the same paper: "Any method that is population monotone avoids the Alabama paradox." (§4, PDF p. 38); "House monotonicity is a weaker property, implied by population monotonicity but not implying it." (§7, PDF p. 66).
- **Balinski & Young (1980): divisor methods as the candidates.** "This is an elementary requirement for any scheme of fair representation, and the only methods that satisfy it are the divisor methods." (§4, PDF p. 38; "it" is population monotonicity), and "The decisive conclusion of the preceding section is that the only realistic candidates for methods of apportionment are the divisor methods." (§5, PDF p. 39). Among divisor methods: "While no population monotone method stays within the quota all of the time, there are population monotone methods that stay within the quota "almost" all of the time; moreover the best from this standpoint is Webster's method." (§6, PDF p. 60).
- **Balinski & Young (1980): doubts about the quota property itself.** "Moreover these same examples suggest that staying within the quota may not be such a reasonable idea after all." and "It can be argued that staying within the quota is not really compatible with the idea of proportionality at all, since it allows a much greater variance in the per capita representation of smaller states than it does for larger states." (§6, PDF p. 58). On methods adapted to always keep quota: "Unfortunately these adaptations suffer acutely from the population paradox, so are not to be recommended." (§7, PDF p. 66).
- **Balinski & Young (1974, 1980): the quota method.** Their 1974 paper, "A New Method for Congressional Apportionment" ([doi:10.1073/pnas.71.11.4602](https://doi.org/10.1073/pnas.71.11.4602); abstract via DOI metadata), gives "Reasons are given for rejecting the presently used method of equal proportions and for accepting a new method, the quota method, which is the unique method satisfying three essential axioms." (abstract via Crossref; record: `raw/balinski-young-1974-pnas-quota-method-bibliographic-record.md`; the paper's text was not read). Malkevitch reports the later turn: "Balinski and Young reject the use of an ingenious method they developed referred to as the quota method. This method, though it obeys quota and is house monotone, does not avoid the population paradox." ("Apportionment II", part 3).
- **Wikipedia's article: mathematicians drop quota.** "In general, the response from mathematicians has been to abandon the quota rule as the less-important property, accepting that apportionment errors may sometimes slightly exceed one seat." (rev. 1373595632; no reference given for the sentence).
- **Bogomolny (2002): against Hamilton's method, for an unfixed house.** "The deficiency is obvious and should have disqualified Hamilton's method from the outset as unconstitutional." — his reason being that the method can split 3 seats 2–1 between two states of equal population. His proposal: "The conclusion that the best way to do what the Constitution requires is to let the number of seats be calculated and not fixed up front seems very natural. The combination of this approach with Webster's or Huntington-Hill's method could never cause the paradoxes nor violate the Quota Rule." (2002).
- **OpenStax (2023): choose by needs, not perfection.** "do not look for a perfect apportionment method. Instead, look for an apportionment method that best meets the needs and concerns of Imaginarians." (§11.5).

## Arguments in play

(none recorded as separate argument pages yet). Two inferences used by the
sources have a propositional core.

**Propositional check (this implant, 2026-10-08; logic, not a position).**
Let *P* = *the method is population monotone*, *Q* = *the method stays within
the quota*, *H* = *the method avoids the Alabama paradox (is house monotone)*.
(1) The impossibility theorem in the form ~(*P* & *Q*), with a method that
stays within the quota: `logic.py check --premises "~(P & Q)" "Q" --conclusion "~P"`
outputs `VALID`. (2) Balinski & Young's "Any method that is population monotone
avoids the Alabama paradox" as *P* -> *H*, with a method that stays within the
quota but shows the Alabama paradox (OpenStax's description of Hamilton's
method): `--premises "P -> H" "Q & ~H" --conclusion "~P"` outputs `VALID`.
(3) The converse direction, which Balinski & Young deny ("implied by
population monotonicity but not implying it"): `--premises "P -> H" "H"
--conclusion "P"` outputs `INVALID`, counterexample `H=T, P=F`, and
`matches schema: affirming the consequent (invalid)`. The tool does not model
the theorem's restriction to four or more states.

**The 1880 Alabama arithmetic (OpenStax; recomputed by this implant,
2026-10-08).** "The 1880 census recorded the population of Alabama as 1,513,401 and that of the U.S. as 62,979,766." (§11.5).
62,979,766 ÷ 299 ≈ 210,634.67 per seat, so Alabama's quota is
1,513,401 ÷ 210,634.67 ≈ 7.1850; 62,979,766 ÷ 300 ≈ 209,932.55, quota ≈ 7.2090
(matching "7.1850" and "7.2090" in §11.5). Alabama's quota rose, yet its
seats fell from 8 to 7; OpenStax's explanation: "It must have been the case that either the fractional part 0.2090 ranked lower amongst the other fractional parts of the state quotas than the fractional part 0.1850 did, or there were fewer remaining seats, or both." (§11.5).

## Thinkers who addressed it

- **Alexander Hamilton** — the method named for him; Wikipedia says it was "originally put forth by Alexander Hamilton, but vetoed by George Washington and not adopted until 1852" (rev. 1373595632, "History", citing Stein 2008); Malkevitch dates the law to 1850 as "Vinton's method, in essence Hamilton's method" ("Apportionment", part 2). The sources differ on the year.
- **Daniel Webster** — his method, per Malkevitch, used in 1901 and in 1911 "with special provision for what to do if a new state entered the Union" ("Apportionment", part 2).
- **C. W. Seaton**, chief clerk of the Census Bureau — named by Wikipedia as computing the 1880 apportionments "for all House sizes between 275 and 350" (rev. 1373595632, citing Stein 2008); OpenStax gives the same range for "The chief clerk of the Census Bureau" (§11.5, citing Caulfield 2010).
- **A. K. Erlang** (1907) — Balinski & Young report a population-monotonicity notion "proposed as early as 1907 by Erlang" (1980, §4, PDF p. 22).
- **Michel L. Balinski & H. Peyton Young** — the quota method (1974), the axiomatic theory and the impossibility theorem (1980 working paper; *Fair Representation*, 1982, 2nd ed. 2001). Malkevitch calls the book "the very important book" ("Apportionment II", part 3, his assessment).
- **Joseph Malkevitch** (AMS Feature Column) — the history and the informal summary of the results quoted above.
- **Alexander Bogomolny** (2002) — the definitions, the critique of Hamilton's method and the unfixed-house proposal above.
- **Michael J. Caulfield** (2010) — cited by Wikipedia and OpenStax for the history ([doi:10.4169/loci003163](https://doi.org/10.4169/loci003163), DOI metadata verified: MAA Mathematical Sciences Digital Library, issued 2008-11-04); the article's page answered 403 and was not read.

## Framings and reframings

- **The historical cases, as each source reports them.**
  *Alabama, 1880:* "Alabama would receive eight seats with a house size of 299, but only receive seven seats if the house size increased to 300." (OpenStax §11.5). Bogomolny: "In 1880, to everyone's surprise a flaw was discovered in Hamilton's method that is now known as the Alabama paradox ." (2002). After the 1900 census, "It was determined that Colorado would receive three seats with a house size of 356, but only two seats with a house size of 357." (OpenStax §11.5).
  *Population, about 1900:* Wikipedia's article: "In 1900, Virginia lost a seat to Maine, even though Virginia's population was growing more rapidly." (rev. 1373595632, citing Stein 2008); Bogomolny: "Close to 1900 Hamilton's method was shown to lead to the Population paradox" (2002).
  *New states, 1907:* "The House size was increased from 386 to 391 to accommodate Oklahoma’s quota of five seats. When the seats were reapportioned using Hamilton’s method, New York lost a seat to Maine despite the fact that their populations had not changed." (OpenStax §11.5). Wikipedia's article reports the aftermath: "This resulted in a crisis of confidence in the apportionment rules procedure as well as a bitter debate within the House, as it was unclear which of these apportionments—the one calculated from scratch, or the one calculated after the previous Census—should be considered the "correct" one." (rev. 1373595632, citing Stein 2008 and Caulfield 2010).
- **"Paradox" as a label.** Bogomolny introduces the topic with dictionary senses, among them Schwartzman's "A paradox is a situation in which, alongside one opinion or interpretation, there is another, mutually exclusive one." (as quoted in Bogomolny 2002), and speaks of "other "paradoxes."" in scare quotes; OpenStax ties the label to what "seem to contradict reasonable expectations of fairness" (§11.5); Malkevitch calls the Alabama case "empirically discovered" ("Apportionment II", part 2). See [paradox](../vocabulary/paradox.md).
- **How the theorem is stated and dated.** The statements differ in scope. Balinski & Young (1980): population monotonicity and staying within the quota. Malkevitch: "(In fact, no method which avoids the population paradox guarantees giving every state its lower or upper quota.)" ("Apportionment II", part 3). Bogomolny: "Any apportionment method that does not violate the quota rule must produce paradoxes, and any apportionment method that does not produce paradoxes must violate the Quota Rule ." (2002, citing Tannenbaum p. 140 and Hoffman p. 270, not read here). OpenStax: "In 1983, mathematicians Michel Balinski and Peyton Young proved that no method of apportionment can simultaneously satisfy all four fairness criteria." (§11.5). Wikipedia's article: "In 1982, two mathematicians, Michel Balinski and Peyton Young, proved that any method of apportionment that does not violate the quota rule will result in paradoxes whenever there are four or more parties (or states, regions, etc.)." (rev. 1373595632). The working paper read here is dated September 1980.
- **Which paradoxes the divisor methods avoid.** OpenStax: "It turns out that, although all three of these divisor methods violate the quota rule, none of them ever causes the population paradox, new-states paradox, or even the Alabama paradox." (§11.5, of Jefferson, Adams and Webster). Malkevitch: "Divisor methods (rounding rule methods) avoid paradoxical results when new states are added to the apportionment mix." ("Apportionment II", part 3). Wikipedia's article says the same of the population paradox — "However, divisor methods such as the current method do not." — with a "citation needed" tag (rev. 1373595632).

Not in the excerpts held: *Fair Representation* itself (archive.org copy
lending-restricted), Stein 2008, Caulfield 2010, the PNAS 1974 full text, and
the Census Bureau history pages (403 on 2026-10-08); claims resting only on
them are given as the citing source's.

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — the label, as discussed above.
- [Validity](../vocabulary/validity.md) — the propositional checks above.
- *Quota*, *staying within the quota* / *quota rule*, *house monotonicity*, *population monotonicity*, *coherence*, *divisor method*, *largest remainder (Hamilton) method* — defined above from Balinski & Young, Bogomolny and Wikipedia; open work in [vocabulary](../vocabulary/index.md).

Related problems: [Arrow's impossibility theorem](arrows-impossibility-theorem.md) (Malkevitch's comparison, above).
