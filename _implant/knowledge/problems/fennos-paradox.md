---
type: article
about: concept
title: "Fenno's paradox"
description: "Why do Americans, in the surveys political scientists report, rate the US Congress poorly while rating their own member of Congress well? Fenno's 1975 essay and Home Style (1978); explanations from different standards of judgment (Fenno, Parker & Davidson 1979), national versus local support (Cook 1979), linked evaluations (Born 1990, McDermott & Jones 2003), members' messages (Lipinski, Bianco & Work 2003), no spillover from responsiveness (Butler, Karpowitz & Pope 2017) and polarization (Bae & Algara 2023)."
tags: [problem, paradox, political-science, decision-theory, public-opinion]
timestamp: 2026-10-08T20:29:06Z
---

# Fenno's paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
This is an empirical claim of political science: every finding below is its
named researchers' finding, from their own summary, not the implant's.
Admitted from Wikipedia's List of paradoxes, revision 1376699902, section
"Decision theory", where it is listed between the Ellsberg paradox and
Fredkin's paradox (excerpt: `raw/wikipedia-fennos-paradox-rev-1292933960-and-list-entry.md`).
Sources: Butler, Karpowitz & Pope 2017 ([doi:10.1017/psrm.2015.83](https://doi.org/10.1017/psrm.2015.83);
excerpt: `raw/butler-karpowitz-pope-2017-who-gets-the-credit-fennos-paradox.md`);
abstracts of six journal articles, 1979–2023 (`raw/fennos-paradox-journal-abstracts-1979-2023.md`);
Knispel, [University of Rochester obituary of Fenno](https://www.rochester.edu/newscenter/remembering-pioneering-rochester-political-scientist-richard-fenno-427532/), 2020
(excerpt: `raw/knispel-2020-rochester-fenno-obituary-fennos-paradox.md`);
Wikipedia, ["Fenno's paradox", rev. 1292933960](https://en.wikipedia.org/w/index.php?title=Fenno%27s_paradox&oldid=1292933960), used as a pointer.
Neither of Fenno's own texts — the 1975 essay in Ornstein (ed.), *Congress in Change: Evolution and Reform* (Praeger), pp. 277–287, and *Home Style: House Members in Their Districts* (1978; ISBN 0673394409 for the Scott, Foresman printing held, lending-restricted, at [archive.org](https://archive.org/details/homestylehousem00fenn)) — was read here; Fenno's words appear only as quoted by others.

## The question

Wikipedia's list: "Fenno's paradox: The belief that people generally disapprove of the United States Congress as a whole, but support the Congressman from their own Congressional district." (rev. 1376699902, "Decision theory").
Fenno's sentence, as quoted by Butler, Karpowitz & Pope: "Fenno (1975) famously wrote, “We do, it appears, love our congressmen. On the other hand, it seems equally clear that we do not love our Congress.”" (2017, p. 363).
Parker & Davidson put it as a puzzle: "This paper provides some evidence for answering the puzzle posed by Richard Fenno (1975, p. 286): we love our congressmen so much more than our Congress." (1979, abstract).
Bae & Algara: "Fenno (1975) famously posited that the mass public’s assessments of the U.S. Congress are rooted in a paradox, with citizens holding negative evaluations of the collective Congress while holding favorable views of their individual members of Congress." (2023, abstract).
Cook states a related version in terms of elections: "The paradox of low public evaluation of Congress and high re-election rates for its members is often explained by the advantages of incumbency." (1979, abstract).

The question the literature asks is then why the two evaluations differ,
and whether they are connected at all.

**Propositional check (this implant, 2026-10-08; logic, not a position).**
Let *A* stand for *most constituents approve of their own member* and *C*
for *most constituents approve of Congress*. The observations alone,
`logic.py check --premises "A" "~C" --conclusion "A & ~A"`, output `INVALID`
with the row `A=T, C=F`: the two findings are jointly consistent. Adding a
bridging premise such as `"A -> C"` makes the output `VALID` with
`premises are jointly inconsistent — argument is vacuously valid`. Whatever
contradiction the word "paradox" names therefore lies in a premise of that
bridging kind, not in the two observations. Butler, Karpowitz & Pope give
one such ground for the name: "This observation has rightly come to be known as Fenno’s paradox because Congress is merely the aggregation of its individual members." (2017, p. 363; their assessment).

## Why it matters

- **Approval of Congress.** Butler, Karpowitz & Pope: "Voters in the United States are highly dissatisﬁed with Congress. In November 2013, Gallup reported that approval had fallen to single digits for the ﬁrst time since tracking began in 1974." (2017, p. 351; the Gallup figure as they report it, not read at Gallup). They add: "Such low levels of approval, which have become a perennial issue for Congress (Patterson and Magleby 1992), have important consequences for both the members of Congress (MCs) and the democratic process." (p. 351).
- **Accountability.** Born ties his finding to "an important ideal of democratic accountability" and cautions against "any temptation to read into these results confirmation that an important ideal of democratic accountability is successfully being realized in this country" (1990, abstract; see Positions taken).
- **Elections.** Whether attitudes to Congress reach individual races is the subject of McDermott & Jones (2003) and Lipinski, Bianco & Work (2003), below.
- **Beyond Congress.** Wikipedia's article: "Fenno's paradox has also been applied to areas other than politics, such as the public school system." (rev. 1292933960); its sources (Gallup, Pew, a study.com lesson) were not read here.

## Positions taken

No published grouping of the explanations was found in the sources read;
they are listed by owner in date order, unranked. Each is the authors'
finding as stated in their abstract or text.

- **Different standards of judgment (Fenno 1975, as reported by Butler, Karpowitz & Pope 2017).** "Indeed, the heart of Fenno’s famous paradox is that constituents evaluate their individual representative and the institution differently because constituents use “different standards of judgment,” holding MCs to a less exacting standard than they do for the broader institution (Fenno 1975, 278; see also Cook 1979; Parker and Davidson 1979; Ripley et al. 1992)." (p. 353).
- **Different criteria, measured (Parker & Davidson 1979).** From two national surveys of 1968 and 1977: "They show that Congress isjudged, increasingly in unfavorable terms, on the basis of its performance on domestic policy, legislative-executive relations, and the style and pace of the legislative process. Congressmen, on the other hand, are judged-usually favorably-primarily on the basis of their service to constituents and their personal characteristics." (abstract, as indexed; [doi:10.2307/439603](https://doi.org/10.2307/439603)).
- **National institution, state-like politicians (Cook 1979).** Against the usual incumbency explanation, from factor analysis of 1968 election data: "Members of Congress seem to be regarded as state politicians, deriving support from their local activities, while Congress is regarded as a national institution, dependent on different sources of support." (abstract; [doi:10.2307/439602](https://doi.org/10.2307/439602)).
- **The incumbency explanation (reported by Cook 1979 and Wikipedia).** Cook calls it the frequent explanation ("often explained by the advantages of incumbency", abstract). Wikipedia's article: "This discrepancy is often attributed to the advantages of incumbency, which include increased visibility, personal connections with constituents, and the ability to deliver benefits to their districts." (rev. 1292933960; no source given there for the sentence).
- **The two evaluations are linked (Born 1990).** Born disputes the "legislature-legislator dichotomy": "In reality, the supporting evidence cited by proponents of the idea is insufficient; neither substantial disparities between the overall positivity of the two evaluations, nor differences in the way they are structured, foreclose the possibility of direct interevaluation linkage." and finds "that judgments of Congress's performance indeed serve as strong predictors of members' reputations from 1978 to 1986." (abstract; [doi:10.2307/2131689](https://doi.org/10.2307/2131689)). His qualification: "it is constituents with lower levels of cognitive sophistication who are more prone to link together personal assessments of Congress and their own legislator." (abstract).
- **Evaluations of Congress reach the majority party (McDermott & Jones 2003).** Against the view that "individual members are largely insulated from public judgments of Congress": "Specifically, voters hold the congressional majority party responsible for Congress’s performance, punishing House candidates from this party when they disapprove of Congress and rewarding them when they approve, regardless of incumbent status." (abstract; [doi:10.1177/1532673x02250291](https://doi.org/10.1177/1532673x02250291)).
- **Members' messages vary and matter (Lipinski, Bianco & Work 2003).** "We show that, for the contemporary House, there is variation in these messages—not all incumbents in the contemporary House “run for Congress by running against Congress.” Moreover, we show that these messages can, under the right conditions, have significant electoral consequences, even after controlling for party affiliation and district political factors." (abstract; [doi:10.3162/036298003x200944](https://doi.org/10.3162/036298003x200944)).
- **No spillover from responsiveness (Butler, Karpowitz & Pope 2017).** "Overall, we ﬁnd that constituents who received a response from their own MC evaluate that representative more positively than those who did not receive a response, but legislator responsiveness does not predict evaluations of the MC’s political party or the Congress." (abstract, p. 351); "There is no spillover effect from member responsiveness." (p. 363). Limits they state: the cross-sectional data show "a small spillover effect" (abstract) which the panel design does not, and "Our research focused on one issue area—immigration." (p. 364).
- **Polarization lowers both ratings (Bae & Algara 2023).** From "over 45 years of new data measuring the monthly approval of Congress and legislators": "we find that greater polarization lowers the approval rating of both over time, suggesting that greater polarization weakens Fenno’s Paradox by considerably lowering legislator approval." (abstract; [doi:10.1080/07343469.2022.2110995](https://doi.org/10.1080/07343469.2022.2110995)).

Side by side (structural note, this implant): Born (1990) and McDermott &
Jones (2003) report links between evaluations of Congress and of members or
their party; Butler, Karpowitz & Pope (2017) report no effect in the other
direction, from a member's responsiveness to evaluations of Congress. The
studies differ in period, data and direction of effect, so the sources read
do not set them against each other directly.

## Arguments in play

(none recorded as separate argument pages). The argument the name rests on
is the aggregation premise examined in the propositional check under The
question. Butler, Karpowitz & Pope's spillover hypothesis is stated as a
conditional: "If citizens use their individual member’s actions as a heuristic to form evaluations of Congress or the party institutions, then we should expect to see member’s positive actions exerting some inﬂuence on citizens’ evaluations of those institutions." (2017, p. 363) — reported here; its consequent is what their panel tested.

## Thinkers who addressed it

- **Richard F. Fenno Jr.** (died April 2020, per Knispel) — the 1975 essay, listed by Butler, Karpowitz & Pope as "Fenno, Richard. 1975. ‘If, As Ralph Nader Says, Congress is the Broken Branch, How Come We Love Our Congressmen So Much?’. In Norman J. Ornstein (ed.), Congress in Change: Evolution and Reform, 277–87. New York: Praeger." (2017, references) and *Home Style* (1978). Knispel: "He was the first to point out the apparent disconnect between low congressional approval and high incumbency in his 1978 book" *Home Style* (Rochester obituary, 2020) — the university's attribution; the scholarly sources read date the claim to the 1975 essay.
- **Timothy E. Cook** (1979) — national versus state-level sources of support.
- **Glenn R. Parker & Roger H. Davidson** (1979) — the different bases of judgment, from 1968 and 1977 surveys.
- **Richard Born** (1990) — the "legislature-legislator dichotomy" disputed.
- **Monika L. McDermott & David R. H. Jones** (2003) — approval of Congress and majority-party candidates.
- **Daniel Lipinski, William T. Bianco & Ryan Work** (2003) — members' messages of loyalty or disloyalty to Congress.
- **Daniel M. Butler, Christopher F. Karpowitz & Jeremy C. Pope** (2017) — the spillover test.
- **Byengseon Bae & Carlos Algara** (2023) — polarization and the long series.

## Framings and reframings

- **Running against Congress.** Wikipedia's article: "Fenno claimed that congressmen would often run against Congress." (rev. 1292933960, citing Mansfield & Sisson without page; not read). Lipinski, Bianco & Work quote the phrase "run for Congress by running against Congress" in their abstract (2003) without attribution there. Butler, Karpowitz & Pope cite *Home Style* for the idea of "getting members to campaign for the institution (Fenno 1978)" (p. 353) and write: "Even if legislators never ran for Congress by running against the institution, perhaps we would still observe Fenno’s paradox because there is no spillover effect and because members have little incentive to proactively promote Congress as a whole." (p. 364).
- **Paradox, puzzle or dichotomy.** The same phenomenon is called a "paradox" (Cook 1979; Butler, Karpowitz & Pope 2017; Bae & Algara 2023), a "puzzle" (Parker & Davidson 1979) and the "so-called legislature-legislator dichotomy" (Born 1990), each in the quoted abstracts or text.
- **1975 or 1978.** Parker & Davidson (1979), Butler, Karpowitz & Pope (2017) and Bae & Algara (2023) cite the 1975 essay; Wikipedia's article and the Rochester obituary name *Home Style* (1978). Page locators also differ: p. 286 (Parker & Davidson) and p. 278 (Butler, Karpowitz & Pope, for "different standards of judgment").
- **A decision-theory paradox?** Wikipedia's list files the entry under "Decision theory", and the article sits in its category "Decision-making paradoxes"; none of the political-science sources read files it so (structural note, this implant).

Left out until read: Fenno's own texts; Ripley et al. 1992 and Patterson
and Magleby 1992 (cited by Butler, Karpowitz & Pope); Hibbing and
Theiss-Morse 1995; the Mansfield & Sisson volume; *The Hill* story Wikipedia
cites (access denied on 2026-10-08); Gallup and Pew data at first hand.

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — here applied to an empirical pattern; see the propositional check.
- [Validity](../vocabulary/validity.md) and [classical logic](../methods/classical-logic.md) — the check above.
- *Incumbency advantage*, *spillover effect*, *home style*, *legislature-legislator dichotomy* — the literature's terms, not yet vocabulary pages ([vocabulary](../vocabulary/index.md)).

Related problems: [the Ellsberg paradox](ellsberg-paradox.md) and [Fredkin's paradox](fredkins-paradox.md) — its neighbours in Wikipedia's "Decision theory" list (rev. 1376699902).
