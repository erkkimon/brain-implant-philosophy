---
type: article
about: concept
title: "The prevention paradox"
description: "If a preventive measure brings much benefit to a population but little to each person who takes it, should prevention target the few at high risk or shift the risk of the whole population? Geoffrey Rose named the 'prevention paradox' in 1981 and set the high-risk and population strategies side by side in 1985; the page reports his arguments, Kreitman's alcohol test, the lay-epidemiology reading, and the critiques and defences on record (Charlton 1995; McLaren et al. 2010), with their owners."
tags: [problem, paradox, decision-theory, epidemiology, public-health, ethics]
timestamp: 2026-10-08T21:37:56Z
---

# The prevention paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
sources graded as in [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md). Admitted from Wikipedia's
[List of paradoxes, rev. 1376699902](https://en.wikipedia.org/w/index.php?title=List_of_paradoxes&oldid=1376699902),
section "Decision theory", which gives it as "Prevention paradox: For one person to benefit, many people have to change their behavior – even though they receive no benefit, or even suffer, from the change."
(excerpt: `raw/wikipedia-list-of-paradoxes-prevention-paradox-entry.md`).
Primary texts: Geoffrey Rose, "Strategy of prevention: lessons from cardiovascular disease", *BMJ* 282, 1981, pp. 1847–1851
([doi:10.1136/bmj.282.6279.1847](https://doi.org/10.1136/bmj.282.6279.1847); excerpt: `raw/rose-1981-strategy-of-prevention.md`);
Rose, "Sick individuals and sick populations", *International Journal of Epidemiology* 14, 1985, pp. 32–38
([doi:10.1093/ije/14.1.32](https://doi.org/10.1093/ije/14.1.32); read in the 2001 reprint, *IJE* 30, pp. 427–432,
[doi:10.1093/ije/30.3.427](https://doi.org/10.1093/ije/30.3.427); excerpt: `raw/rose-1985-sick-individuals-and-sick-populations.md`).
Pointer used: Wikipedia, ["Prevention paradox", rev. 1372462966](https://en.wikipedia.org/w/index.php?title=Prevention_paradox&oldid=1372462966) (same raw file).
Works verified bibliographically or by abstract only: `raw/prevention-paradox-crossref-records.md`.

## The question

Rose's 1981 statement, after the cardiovascular examples: "We arrive at what we might call the prevention paradox" —
"a measure that brings large benefits to the community offers little to each participating individual." (p. 1850).
His 1985 wording: "This leads to the Prevention Paradox: ‘A preventive measure which brings much benefit to the population offers little to each participating individual’." ("The Population Strategy").
The question it poses, in Rose's 1985 terms, is the choice between two strategies:
"The corresponding strategies in control are the ‘high-risk’ approach, which seeks to protect susceptible individuals, and the population approach, which seeks to control the causes of incidence." (abstract).

**Two glosses on record.** The Wikipedia list glosses the paradox from the
individual's side (quoted above: many change behaviour so that one benefits).
The Wikipedia article glosses it from the distribution of cases:
"The prevention paradox describes the situation where the majority of cases of a disease come from a population at low or moderate risk of that disease, and only a minority of cases come from the high risk population (of the same disease)."
Rose's 1981 article contains both: the distribution of cases, which he calls
"a fundamental principle in the strategy of prevention" (p. 1849; Arguments,
below), and the small benefit to each individual, which he names the paradox
(p. 1850).

**Is it a paradox?** The label is Rose's ("what we might call the prevention paradox", 1981, p. 1850).
Kreitman (1986) calls the alcohol version "the so‐called ‘preventive paradox’" (abstract), and Sinclair & Sillanaukee title their 1993 reply "The preventive paradox: a critical examination" (title only read).
Logic check (this implant, 2026-10-09; logic, not a position): write *B* for
*the measure brings much benefit to the population* and *L* for *it offers
little to each participating individual*. `logic.py check --premises "B" "L" --conclusion "~(B & L)"`
prints `INVALID` with the counterexample `B=T, L=T`: the two clauses of Rose's
sentence are jointly satisfiable in propositional form. This shows only that
the formalised sentence states no contradiction; it takes no side on whether
the label fits. See [paradox](../vocabulary/paradox.md) for this implant's normative sense.

## Why it matters

- **Choosing a preventive strategy.** Rose (1985) lists advantages of the high-risk strategy — intervention appropriate to the individual, motivation of subject and physician, cost-effective use of resources, a favourable benefit/risk ratio — and disadvantages, among them that "it is behaviourally inappropriate" ("The ‘High-Risk’ Strategy"). For the population strategy he reports that it "has also some weighty drawbacks (Table 6)", the paradox being one ("The Population Strategy").
- **Motivation and health education.** Rose's inference from the paradox: "It implies that we should not expect too much from individual health education." (1981, p. 1850); and, 1985: "Their health next year is not likely to be much better if they accept our advice or if they reject it."
  On physicians: "Grateful patients are few in preventive medicine, where success is marked by a non-event." (1985).
- **Safety of mass measures.** Rose draws a counterpart from the same arithmetic: "If a preventive measure exposes many people to a small risk, then the harm it does may readily-as in the case of clofibrate-outweigh the benefits, since these are received by relatively few." (1981, p. 1850).
  His conclusion from it: "Consequently we cannot accept long-term mass preventive medication." (p. 1850); and, 1985: "In mass prevention each individual has usually only a small expectation of benefit, and this small benefit can easily be outweighed by a small risk."
- **Public health history.** Rose: "This has been the history of public health—of immunization, the wearing of seat belts and now the attempt to change various life-style characteristics." (1985).
- **Health inequalities.** McLaren, McIntyre & Kirkpatrick (2010) report a later challenge: "it has been suggested that population strategies of prevention may inadvertently worsen social inequalities in health." (abstract; Positions, below).

## Positions taken

Grouped by the strategy each favours, as the sources frame the choice. Each
line names its owner; none is ranked. Empirical figures are the named
researchers' estimates.

**Rose: the population strategy has priority, both are usually needed.**

- 1981: "Potentially far more effective, and ultimately the only acceptable answer, is the mass strategy, whose aim is to shift the whole population's distribution of the risk variable." With the proviso: "Here, however, our first concern must be that such mass advice is safe." (p. 1851).
- 1985: "The two approaches are not usually in competition, but the prior concern should always be to discover and control the causes of incidence." (abstract). And: "The ‘high-risk’ strategy of prevention is an interim expedient, needed in order to protect susceptible individuals, but only for so long as the underlying causes of incidence remain unknown or uncontrollable; if causes can be removed, susceptibility ceases to matter." ("Conclusions").
- 1985, same section: "Realistically, many diseases will long continue to call for both approaches, and fortunately competition between them is usually unnecessary."
- Book: the chapter abstract of *The Strategy of Preventive Medicine* (OUP; Crossref record dated 1993; [doi:10.1093/oso/9780192624864.003.0007](https://doi.org/10.1093/oso/9780192624864.003.0007)) states "Mass diseases and mass exposures require mass remedies. A targeted approach may assist but it cannot be sufficient." (abstract only read; the book was not fetched).

**Kreitman (1986): the paradox tested for alcohol.** Kreitman's abstract reports that drinkers above "safe limits" are at high risk "yet they contribute only a minority to the total numbers of alcohol casualties" —
"Drinkers in the general population who exceed the ‘safe limits’ advocated by various experts are undoubtedly at high risk of alcohol‐related harm, yet they contribute only a minority to the total numbers of alcohol casualties, This relationship, the so‐called ‘preventive paradox’ was explored in some detail using different criteria for ‘safe limits’ for total consumption, for frequency of drinking and for maximal daily consumption: two population surveys and a study of special groups noted for high intake were used."
His finding as stated there: "Finally it was shown that the gains from the universal adoption of the conventional ‘safe limits’ within a population would be matched by an across‐the‐board per capita reduction to about 70% of current intake." ([doi:10.1111/j.1360-0443.1986.tb00342.x](https://doi.org/10.1111/j.1360-0443.1986.tb00342.x); abstract only read).
*Side by side:* Sinclair & Sillanaukee, "The preventive paradox: a critical examination", *Addiction* 88, 1993, pp. 591–595, indexed by PubMed as a comment on Kreitman ([doi:10.1111/j.1360-0443.1993.tb02068.x](https://doi.org/10.1111/j.1360-0443.1993.tb02068.x)); its argument was not read and is not reported here.

**Critiques of the population strategy.**

- *Charlton (1995).* B. G. Charlton, "A Critique of Geoffrey Rose's ‘Population Strategy’ for Preventive Medicine", *Journal of the Royal Society of Medicine* 88, pp. 607–610 ([doi:10.1177/014107689508801102](https://doi.org/10.1177/014107689508801102)). The text could not be fetched; only its title and the existence of an accompanying commentary ("The population paradox", p. 605) and a 1996 letter are on record here. What Charlton argues is left for a later edit from the text.
- *Better prediction of high risk.* McLaren et al. (2010) report as the first of "two notable challenges": "First, identification of high-risk individuals has improved considerably in accuracy, which some believe obviates the need for population-wide prevention strategies." (abstract; the "some" are not named in the abstract).
- *Inequalities.* Second challenge, same abstract: "it has been suggested that population strategies of prevention may inadvertently worsen social inequalities in health."

**Defence on the inequalities point: McLaren, McIntyre & Kirkpatrick (2010).**
"We argue that population prevention will not necessarily worsen social inequalities in health, and the likelihood of it doing so will depend on whether the prevention strategy is more structural (targets conditions in which behaviours occur) or agentic (targets behaviour change among individuals) in nature."
Their assessment: "Although Rose's ideas need to be continually scrutinized, his population strategy of prevention still holds considerable merit for improving population health and narrowing social inequalities in health." ([doi:10.1093/ije/dyp315](https://doi.org/10.1093/ije/dyp315); abstract only read).
Two commentaries in the same issue (Frohlich & Potvin, on structure and agency; Manuel & Rosella, on assessing population baseline risk) are recorded bibliographically only.

## Arguments in play

(none recorded as separate argument pages yet). The arguments as Rose gives them:

- **Many at small risk produce more cases.** Rose 1981: "A large number of people exposed to a low risk is likely to produce more cases than a small number of people exposed to a high risk." (p. 1849); he compares it to "the mass market" (same page).
  His Framingham illustration: attributable coronary deaths "add up to 34 extra deaths per 1000 of this population over a 10-year" period, of which only three arise at 310 mg/100 ml or above, and "The rest (90%) arise from the many people in the middle part of the distribution who are exposed to a small risk." (p. 1849).
  Arithmetic (this implant, 2026-10-09; arithmetic, not a position): 34 − 3 = 31, and 31/34 ≈ 0.91, matching Rose's "(90%)" to the nearest ten per cent.
  His 1985 example, from Alberman's data: "Mothers under 30 years are individually at minimal risk; but because they are so numerous, they generate half the cases. High-risk individuals aged 40 and above generate only 13% of the cases." He adds: "This situation seems to be common, and it limits the utility of the ‘high-risk’ approach to prevention."
- **The individual gains little.** Rose 1981 (p. 1850): "A measure applied to many will actually benefit few."
  His estimates: for seat belts worn by male British doctors, "399 would have worn a seat belt every day for 40 years without benefit to their survival"; for Framingham men of average risk lowering cholesterol by 10%, "49 out of 50 would eat differently every day for 40 years and perhaps get nothing from it."
  Arithmetic (this implant; arithmetic, not a position): 1 in 50 benefits and 49 of 50 do not, 1 + 49 = 50; for higher-risk men Rose gives "one in 25" (p. 1850).
- **Causes of cases versus causes of incidence.** Rose 1985: "The first seeks the causes of cases, and the second seeks the causes of incidence." His illustration of what within-population studies miss: "If everyone smoked 20 cigarettes a day, then clinical, case-control and cohort studies alike would lead us to conclude that lung cancer was a genetic disease" ("The Determinants of Individual Cases").
- **Everyone at risk of a mass disease.** Rose 1985 on coronary heart disease: "Everyone, in fact, is a high-risk individual for this uniquely mass disease."
- **Social and economic determinants.** Rose 1981: "To influence mass behaviour we must look to its mass determinants, which are largely economic and social." (p. 1850).

## Thinkers who addressed it

- **Geoffrey Rose** (1981; 1985; book) — names the prevention paradox and sets the high-risk and population strategies side by side (*BMJ* 1981, p. 1850; *IJE* 1985; *The Strategy of Preventive Medicine*, OUP, Crossref record dated 1993, [doi:10.1093/oso/9780192624864.001.0001](https://doi.org/10.1093/oso/9780192624864.001.0001), ISBN 9780192624864; and *Rose's Strategy of Preventive Medicine*, OUP 2008, Crossref authors Rose, Khaw and Marmot, [doi:10.1093/acprof:oso/9780192630971.001.0001](https://doi.org/10.1093/acprof:oso/9780192630971.001.0001)).
- **N. Kreitman** (1986) — the "preventive paradox" for alcohol consumption (abstract, above).
- **C. Davison, G. Davey Smith & S. Frankel** (1991) — "Lay epidemiology and the prevention paradox", *Sociology of Health & Illness* 13, pp. 1–19 ([doi:10.1111/j.1467-9566.1991.tb00085.x](https://doi.org/10.1111/j.1467-9566.1991.tb00085.x)); read only as Hunt & Emslie quote it (Framings, below).
- **J. D. Sinclair & P. Sillanaukee** (1993) — a critical examination of the preventive paradox (title only).
- **B. G. Charlton** (1995) — a critique of Rose's population strategy (title only).
- **Kate Hunt & Carol Emslie** (2001) — the paradox in lay epidemiology ([doi:10.1093/ije/30.3.442](https://doi.org/10.1093/ije/30.3.442); excerpt: `raw/hunt-emslie-2001-prevention-paradox-lay-epidemiology.md`).
- **L. McLaren, L. McIntyre & S. Kirkpatrick** (2010) — the population strategy and social inequalities (abstract).

## Framings and reframings

- **Lay epidemiology.** Hunt & Emslie (2001), following Davison et al., read the paradox through how people judge "coronary candidacy"; the anomaly they report is that "The first inexplicable ‘anomaly’ is ‘the unwarranted survivor’, the ‘candidate’ who survives to a ‘ripe old age’ against the odds."
  They quote Davison et al.'s conclusion: "Davison et al. conclude that, ‘It is ironic that such evidently fatalistic cultural concepts should be given more rather than less explanatory power by the activities of modern health education, whose stated goals lie in the opposite direction’."
  Their own conclusion: "In conclusion, we would argue that there are many parallels between lay and professional epidemiology, and that the ‘prevention paradox’ is a key site of disquiet within both."
- **Structural or agentic.** McLaren et al. (2010) recast the inequality question as depending on whether a population measure is "more structural (targets conditions in which behaviours occur) or agentic (targets behaviour change among individuals)" (abstract, quoted in full above).
- **A second use of the name.** The Wikipedia article reports that "Especially in the context of the COVID-19 pandemic, the term "prevention paradox" was also used to describe the apparent paradox of people questioning steps to prevent the spread of the pandemic because the prophesied spread did not occur."
  and, as its own assessment with two cited sources (Spinney, *The Guardian*, 2020; Boudry, *The Conversation*, 2020; neither fetched), "This however is instead an example of a self-defeating prophecy or a preparedness paradox."
  That use is the subject of the sibling page [preparedness paradox](preparedness-paradox.md); the article carries a "Distinguish" note between the two.

Left out: the text of Charlton 1995 and Sinclair & Sillanaukee 1993 (not
fetched; only titles reported), the 1992 book beyond its chapter abstract,
and the alcohol and adolescent studies linked from the Wikipedia article
(not read).

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — see The question, paragraph *Is it a paradox?*.
- [Validity](../vocabulary/validity.md) — the logic check of Rose's sentence.
- Relative risk, absolute risk, population attributable risk, incidence, high-risk strategy, population strategy — open work in [vocabulary](../vocabulary/index.md).

Related problems: [preparedness paradox](preparedness-paradox.md) (Wikipedia
article, rev. 1372462966, hatnote and lead). Branch: [Problems](./index.md).
