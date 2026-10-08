---
type: article
about: concept
title: "The preparedness paradox: does a disaster averted look like a threat that was never real?"
description: "When preparation limits a disaster, the small damage can make the preparation look needless: Kayyem's 2022 statement and her Y2K example, Quiggin's 2005 case that most Y2K spending was wasted against Thomas's 2017 list of failures prevented, COVID-19-era statements (Reder & Doyle Cooper, Hamblin, Armstrong-Hough), the levee version (Gissing et al. 2018), Meyer & Kunreuther's six biases, and the other senses the phrase carries in journals."
tags: [problem, paradox, decision-theory, risk, emergency-management]
timestamp: 2026-10-08T21:37:56Z
---

# The preparedness paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Admitted from Wikipedia's List of paradoxes, revision 1376699902, "Decision theory", in list order;
Wikipedia's article ([rev. 1332614333](https://en.wikipedia.org/w/index.php?title=Preparedness_paradox&oldid=1332614333))
was used as a pointer to sources (excerpt: `raw/wikipedia-preparedness-paradox-rev-1332614333-and-list-entry.md`).
**Sources are thin.** No philosophical treatment, encyclopedia entry outside Wikipedia, or
peer-reviewed paper devoted to the phrase in the sense below was found; the record is an
interview, commentary, a policy brief, and a few journal papers that use the phrase in passing
or in other senses. The page is short for that reason.

## The question

- **Wikipedia's list** (rev. 1376699902): "Preparedness paradox: After preparing to avoid a catastrophe and lessening the damage, the perception regarding the catastrophe would be much less serious due to the limited damage caused after."
- **Wikipedia's article** (rev. 1332614333, lead): "The preparedness paradox is the proposition that if a society or individual acts effectively to mitigate a potential disaster such as a pandemic, natural disaster or other catastrophe so that it causes less harm, the avoided danger will be perceived as having been much less serious because of the limited damage actually caused." The article's own assessment, cited to Kayyem: "The paradox is the incorrect perception that there had been no need for careful preparation as there was little harm, although in reality the limitation of the harm was due to preparation."
- **Juliette Kayyem** (former Homeland Security official, interviewed by Steve Inskeep, NPR *Morning Edition*, 31 March 2022; excerpt: `raw/kayyem-2022-npr-preparedness-paradox-y2k.md`): "KAYYEM: Yes, absolutely. And we have a name for it. It's called the preparedness paradox. It is the - you know, the more we prepare for bad things, the less the destruction is, and then everyone wonders, why the heck were we so prepared, or why did we need to get prepared?"
- **Castriota, Delmastro & Tonin** (2023, [doi:10.1007/s10754-023-09350-3](https://doi.org/10.1007/s10754-023-09350-3), citing Kayyem 2022) define it as "a situation that emerges when preventative measures are successful in avoiding damage but are then perceived as unnecessary because the damage never manifested itself." (excerpt: `raw/preparedness-paradox-term-in-journals-2022-2024.md`).

So stated, the question is twofold: a descriptive one (do people judge averted threats
as never serious?) and an evidential one (what does a small outcome after preparation show about
the size of the threat?). This split is a structural note of the implant (manifest
[G4](../../vision/manifest.md)), not a source's.

**Propositional check (this implant, 2026-10-09; logic, not a position).** *N*: the threat
needed preparation; *P*: preparation was made; *H*: serious harm occurred. Assume "N & ~P -> H".
`logic.py check --premises "N & ~P -> H" "P" "~H" --conclusion "~N"` outputs `INVALID`, with the
counterexample row `H=F, N=T, P=T`: after preparation, an absence of harm does not by this premise
alone show the threat was unneeded. `logic.py check --premises "N & ~P -> H" "~P" "~H" --conclusion "~N"`
outputs `VALID`: where nothing was prepared and nothing happened, the premise does yield *~N*.
The second form is the shape of Quiggin's low-remediation comparison below; whether the premise and
the observations hold is the empirical matter the sources dispute.

## Why it matters

- **Future preparation.** Wikipedia's article (rev. 1332614333, lead, cited to Kayyem): "Several cognitive biases can consequently hamper proper preparation for future risks." Kayyem: "So we call that the preparedness paradox because you never can win." (NPR 2022).
- **Funding pandemic preparedness.** Jake Reder and Colleen Doyle Cooper (Celdara Medical; PMLive, 21 January 2021; excerpt: `raw/reder-doyle-cooper-2021-pandemic-preparedness-paradox.md`): "If we do invest, we will have no evidence (no pandemic, no global economic disruption) that we had to make such investments. If we don’t invest, we will once again have more evidence than we can handle. This paradox is anything but subtle." For a firm whose product stops an outbreak early: "This is nothing more than a paradox born of a business model."
- **Political reward for prevention.** Castriota, Delmastro & Tonin (2023) suggest from their Italian news-demand data that following national news may let local politicians be "rewarded for their efforts, even if the local epidemiological situation was not threatening 19 , thus escaping the so-called “preparedness paradox” (Kayyem, 2022 ), a situation that emerges when preventative measures are successful in avoiding damage but are then perceived as unnecessary because the damage never manifested itself." (their interpretation).
- **Flood mitigation and land use.** The levee case below (Gissing et al. 2018).

## Positions taken

No grouping of positions was found in the sources read; the views on record are listed by owner, unranked.

**On the paradox in general**

- **A recurring perception error after successful prevention (Kayyem 2022; Wikipedia rev. 1332614333).** As quoted above; Wikipedia calls the perception "incorrect".
- **Preventive measures look wasteful before and after (Kottke 2020 and those he quotes).** Jason Kottke (kottke.org, 16 March 2020; excerpt: `raw/kottke-2020-paradox-of-preparation-covid.md`): "The paradox of preparation refers to how preventative measures can intuitively seem like a waste of time both before and after the fact." He quotes Chris Hayes ("A doctor I spoke to today called this the “paradox of preparation” and it’s the key dynamic in all this."), James Hamblin ("The thing is if shutdowns and social distancing work perfectly and are extremely effective it will seem in retrospect like they were totally unnecessary overreactions."), the epidemiologist Mari Armstrong-Hough ("When the best way to save lives is to prevent a disease rather than treat it, success often looks like an overreaction."), and Vaughn Tan ("This means that any effective actions taken against coronavirus in the few days before the epidemic curve shoots upward in any country will always look unreasonable and disproportionate.").

**On the Y2K case (contested)**

- **The quiet rollover shows the preparation worked (Kayyem 2022).** "That effort was actually successful because nothing happened on January 1 when the computers changed to the year 2000. Looking back or the narrative of Y2K, it's often described as being an overreaction to a threat. The reality is it was because the preparedness worked." (NPR).
- **Remediation prevented real failures (Thomas 2017).** Martyn Thomas, who "led the Y2K services internationally for Deloitte & Touche Consulting Group" and audited the UK NATS programme (Gresham College lecture, 4 April 2017; excerpt: `raw/thomas-2017-gresham-what-really-happened-in-y2k.md`): "Thousands of errors were found and corrected during the 1990s, avoiding failures that would otherwise have occurred." Among his examples, a 1998 Swedish test: "The reactor’s computers couldn’t recognize the date (1/1/00) and shut down the reactor". His assessment: "Y2K remediation should be seen as a major success, showing that it is possible to deliver major IT systems on time if they have clear objectives, clear timescales, senior management support, and commitment to provide the necessary resources, clear communications and acceptance throughout the affected organisations that the project has the right objectives and deserves the highest priority." He describes the opposing view as "the feeling grew that the whole thing had been a myth or a scam invented by rapacious consultants and supported by manufacturers who wanted to compel their customers to throw away perfectly good equipment and buy the latest version."
- **Most remediation spending was wasted (Quiggin 2005).** John Quiggin, *The Y2K scare: Causes, Costs and Cures*, *Australian Journal of Public Administration* 64(3), 46–55 ([doi:10.1111/j.1467-8500.2005.00451.x](https://doi.org/10.1111/j.1467-8500.2005.00451.x); excerpt: `raw/quiggin-2005-y2k-scare-causes-costs-cures.md`), himself a 1999 Y2K sceptic by his own account: "Most of this expenditure can be seen, in retrospect, to have been unproductive or, at least, misdirected." (abstract); "Most importantly, it became apparent that Y2K-related problems had been insignificant even where little or no remediation effort had been undertaken." (p. 46); "In this paper, it will be argued that, although some relatively minor problems were prevented, and some collateral benefits were realised, most money spent specifically on Y2K compliance exercises was wasted. Moreover, it will be argued, evidence available early in 1999, should have been sufficient to justify the adoption of a less costly strategy of ‘fix on failure’." (p. 46).

Neither Thomas nor Quiggin uses the phrase "preparedness paradox" in the texts read; Kayyem applies it to Y2K.

**On levees**

- **Levees lower preparedness behind them (Gissing, Van Leeuwen, Tofa & Haynes 2018).** *Australian Journal of Emergency Management* 33(3), 38–43 (excerpt: `raw/gissing-et-al-2018-flood-levee-preparedness-paradox.md`), reporting earlier work: "This effect has been referred to as the ‘levee paradox’ (Smith 2002, 2003), the ‘levee effect’ (Tobin 1995) and the ‘safe development paradox’ (Burby 2006)." Their Lismore findings: "Thirty-two per cent overestimated the protection offered by the levee believing they would be flooded less than once in every 10 years on average (note: the overtopping ARI of the levee is 10 years)."; "Following the April 2017 flood, the additional survey of 15 businesses found that 14 of the 15 believed that the community was less prepared since the construction of the levee." Their stated limit: "This paper presents the results of a single case study. Further work is required to establish a firm  empirical basis for the ‘levee paradox’ and how its manifestation might vary in different communities and with different forms of mitigation." The paper does not use the phrase "preparedness paradox"; Wikipedia files it under that heading.

## Arguments in play

(none recorded as separate argument pages yet). On record:

- **The incentive asymmetry (Quiggin 2005).** "The absence of any serious Y2K problems could always be attributed to the success of the remediation program." Quiggin uses this to explain why remediation was favoured. That it runs opposite to Kayyem's "you never can win" is a structural note of the implant, not a source's.
- **The unremediated comparison (Quiggin 2005).** Problems "insignificant even where little or no remediation effort had been undertaken" (form checked above: the `VALID` case).
- **Prevented failures found in testing (Thomas 2017).** Errors found before 2000 as evidence that the threat was real, independent of the quiet rollover.
- **Six biases behind under-preparation (Meyer & Kunreuther).** Robert Meyer and Howard Kunreuther, *The Ostrich Paradox: Why We Underprepare for Disasters* (Wharton Digital Press, 2017; ebook ISBN 978-1-61363-079-2), read in their Wharton Risk Center issue brief, May 2018 (excerpt: `raw/meyer-kunreuther-2018-ostrich-paradox-issue-brief.md`): "In our book The Ostrich Paradox, we characterize six decision-making biases that cause individuals, communities and organizations to underinvest in protection against low-probability, high-consequence events." Two of the six: "Myopia – a tendency to focus on overly short future time horizons when appraising immediate costs and the potential benefits of protective investments." and "Amnesia – a tendency to forget too quickly the lessons of past disasters." The others are optimism, inertia, simplification and herding. Wikipedia cites the book for its "Cognitive biases" section; the brief does not use the phrase "preparedness paradox".
- **Life history (Kruger, Fernandes, Cupal & Homish 2019).** *Life history variation and the preparedness paradox*, *Evolutionary Behavioral Sciences* 13(3), 242–253 ([doi:10.1037/ebs0000129](https://doi.org/10.1037/ebs0000129)); not read here. Wikipedia's summary of it: "However, organisms with slower life histories, such as humans, may have less urgency in dealing with these types of events."

## Thinkers who addressed it

- **Omar Bradley** (1949) — Wikipedia quotes him, from a Senate Armed Services subcommittee hearing (p. 79), as saying "There is a preparedness paradox that continually confronts military planners." — in the sense of the cost of military readiness; the hearing record was not read here.
- **Aino Ruggiero & Marita Vos** (2014, *Journal of Contingencies and Crisis Management* 23(3), 138–148, [doi:10.1111/1468-5973.12065](https://doi.org/10.1111/1468-5973.12065)) — cited by Wikipedia for "A preparedness paradox exists. On the one hand, to prepare the public to be able to act" (CBRN terrorism communication); only the abstract was read, which does not contain the phrase.
- **Robert Meyer & Howard Kunreuther** (2017, 2018) — the six biases.
- **Andrew Gissing, Jonathan Van Leeuwen, Matalena Tofa & Katharine Haynes** (2018) — the levee study.
- **Jason Kottke, Chris Hayes, James Hamblin, Mari Armstrong-Hough, Vaughn Tan, Ian Bogost** (March 2020) — COVID-19 statements; Bogost, quoted by Kottke: "Ultimately, overreaction is a matter of knowledge-an epistemological problem."
- **Jake Reder & Colleen Doyle Cooper** (2021) — the pandemic-investment version.
- **Juliette Kayyem** (2022; book *The Devil Never Sleeps*, PublicAffairs 2022, cited by Castriota et al.; the book was not read) — the statement most cited for the term.
- **John Quiggin** (2005) and **Martyn Thomas** (2017) — the two sides on Y2K.
- **Stefano Castriota, Marco Delmastro & Mirco Tonin** (2023) — application to COVID-19 local politics.

## Framings and reframings

- **As a cousin of the barber paradox.** Reder & Doyle Cooper open with [Russell](../thinkers/russell.md)'s [barber](barber-paradox.md): "A barber is one who shaves those who do not shave themselves. Does the barber shave himself? If he does, he does not. If he does not, he does. This is a pleasing and subtle puzzle made popular by Bertrand Russell. While real-life paradoxes are rarely so tidy, pandemic preparedness is often viewed in this light, by both the lay public and by our elected representatives."
- **Distinct from the prevention paradox.** Wikipedia's article carries a hatnote marking it as distinct from the prevention paradox (rev. 1332614333); see [the prevention paradox](prevention-paradox.md).
- **Other senses of the same phrase.** Rinscheid & Koos (2023, [doi:10.1038/s43247-023-00755-z](https://doi.org/10.1038/s43247-023-00755-z)) use it for "the preparedness paradox, which means that mitigation is less costly than adaptation"; Day & Dennis (2022, [doi:10.1108/sl-05-2022-0051](https://doi.org/10.1108/sl-05-2022-0051)) for organizational inaction ("The corrective to the preparedness paradox: five attention-getting actions that prompt low-cost readiness for potential disruptions."); Rivera-Kientz & Stewart (2024, [doi:10.1080/00380253.2024.2417386](https://doi.org/10.1080/00380253.2024.2417386)) for a partisan finding ("We find a paradox: Republicans are more likely to say they have taken preparedness actions than Democrats."). Bradley's 1949 sense, as Wikipedia reports it, is the cost of readiness. Wikipedia's article (rev. 1332614333): "The term "preparedness paradox" has been used occasionally since at least 1949 in different contexts, usually in the military and financial system."

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — the label is the sources' (Kayyem, Kottke, Reder & Doyle Cooper, Wikipedia); no source read derives a formal contradiction, and Reder & Doyle Cooper contrast it with the "tidy" barber case.
