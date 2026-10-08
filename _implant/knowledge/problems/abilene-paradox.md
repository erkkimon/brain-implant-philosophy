---
type: article
about: concept
title: "The Abilene paradox: how can a group agree on what none of its members wants?"
description: "Jerry B. Harvey's 1974 case of a family that drives to Abilene though nobody wanted to go: his account of it as a failure to manage agreement rather than conflict, Kanter's link to 'pluralistic ignorance', Kim's nine-point contrast with groupthink, Flores et al.'s voting-game experiment, and Harvey's own 1988 remark that he cannot prove the paradox occurs."
tags: [problem, paradox, decision-theory, social-psychology, organizations]
timestamp: 2026-10-08T20:29:06Z
---

# The Abilene paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Primary text: Jerry B. Harvey, "The Abilene Paradox: The Management of Agreement",
*Organizational Dynamics* 3(1), 1974, pp. 63–80 ([doi:10.1016/0090-2616(74)90005-9](https://doi.org/10.1016/0090-2616(74)90005-9)),
read in the reprint with Harvey's epilogue, *Organizational Dynamics* 17(1), 1988, pp. 17–43
([doi:10.1016/0090-2616(88)90028-9](https://doi.org/10.1016/0090-2616(88)90028-9); page numbers below are the reprint's;
excerpt: `raw/harvey-1974-abilene-paradox-management-of-agreement.md`). Commentaries printed with the reprint:
`raw/kanter-carlisle-1988-abilene-defense-commentaries.md`. Later literature:
`raw/abilene-paradox-later-literature-kim-halbesleben-montgomery-flores.md`.
Admitted from Wikipedia's List of paradoxes, revision 1376699902, "Decision theory", the section's
first entry; Wikipedia's article ([rev. 1368918145](https://en.wikipedia.org/w/index.php?title=Abilene_paradox&oldid=1368918145))
was used as a pointer to sources (excerpt: `raw/wikipedia-abilene-paradox-rev-1368918145-and-list-entry.md`).

## The question

Harvey's anecdote (pp. 17–18), in his words:
- The proposal: "Let’s get in the car and go to Abilene and have dinner at the cafeteria.” (p. 17).
- Harvey's reply: "Since my own preferences were obviously out of step with the rest I replied, “Sounds good to me,”" (p. 17).
- The father-in-law afterwards: "“Listen, I never wanted to go to Abilene. I just thought you might be bored." (p. 18).
- Harvey's summary: they went "when none of us had really wanted to go. In fact, to be more accurate, we’d done just the opposite of what we wanted to do." (p. 18).

Harvey states the paradox twice:
- "Stated simply, it is as follows: Organizations frequently take actions in contradiction to what they really want to do and therefore defeat the very purposes they are trying to achieve." (p. 19).
- "The Abilene Paradox can be stated succinctly as follows: Organizations frequently take actions in contradiction to the data they have for dealing with problems and, as a result, compound their problems rather than solve them." (p. 23).

Wikipedia's list: "Abilene paradox: People can make decisions based not on what they actually want to do, but on what they think that other people want to do, with the result that everybody decides to do something that nobody really wants to do, but only what they thought that everybody else wanted to do." (rev. 1376699902).

**Propositional check (this implant, 2026-10-08; logic, not a position).** A two-member
simplification of the list's wording. *P1*, *P2*: member 1 / member 2 prefers to stay;
*B1*, *B2*: each believes the other wants to go; *V1*, *V2*: each says "go"; *G*: the group goes.
`logic.py check --premises "P1" "P2" "B1" "B2" "B1 -> V1" "B2 -> V2" "V1 & V2 -> G" --conclusion "G"`
outputs `VALID`, with `premise 1 is not needed for validity` and `premise 2 is not needed for validity`.
Adding `"G"` to the premises and testing the conclusion `"X & ~X"` outputs `INVALID` (counterexample
row `B1=T, B2=T, G=T, P1=T, P2=T, V1=T, V2=T`), i.e. *everyone prefers to stay* and *the group goes*
are jointly consistent in this model. The model assumes the conditionals; whether people act on
them is the empirical matter the sources below discuss.

## Why it matters

- **Agreement, not conflict, as the problem (Harvey 1974).** "It also deals with a major corollary of the paradox, which is that the inability to manage agreement is a major source of organization dysfunction." (p. 19); "In fact, it is my contention that the inability to cope with (manage) agreement, rather than the inability to cope with (manage) conflict, is the single most pressing issue of modern organizations." (p. 21).
- **Organizational cases (Harvey 1974).** Harvey applies it to an R&D project and to Watergate, quoting Herbert Porter: "Porter replied, “In all honesty, because of the fear of the group pressure that would ensue, of not being a team player,”" (p. 22, from *The Washington Post*, 8 June 1973).
- **Later applications.** Montgomery (2022) on Hillsborough police officers: "In this regard, the “Abilene paradox” is a useful explanatory mechanism (Harvey, 1974)." ([doi:10.3389/fpsyg.2022.847376](https://doi.org/10.3389/fpsyg.2022.847376)). Wikipedia's article lists further applications (Challenger, information systems development) from papers not read here (rev. 1368918145).
- **Group decision theory.** Flores, Mannahan & Sohn (2025) model it as a voting outcome: "The Abilene paradox (AP) occurs when a group of people vote for an alternative that no one prefers, resulting in an inferior outcome." (abstract, [doi:10.1002/soej.70009](https://doi.org/10.1002/soej.70009)).

## Positions taken

No grouping of accounts was found in the sources read; the explanations on record are listed by owner, unranked.

- **Mismanaged agreement driven by anxiety and fear of separation (Harvey 1974).** Harvey's six subsymptoms include "3. Organization members fail to accurately communicate their desires and/or beliefs to one another. In fact, they do just the opposite and thereby lead one another into misperceiving the collective reality." and "4. With such invalid and inaccurate information, organization members make collective decisions that lead them to take actions contrary to what they want to do, and thereby arrive at results that are counterproductive to the organization’s intent and purposes." (pp. 19–21). His "map" has five landmarks: "(1) Action Anxiety; (2) Negative Fantasies; (3) Real Risk; (4) Separation Anxiety; and (5) the Psychological Reversal of Risk and Certainty." (p. 23). On the first: "The concept of action anxiety says that the reasons organization members take actions in contradiction to their understanding of the organization’s problems lies in the intense anxiety that is created as they think about acting in accordance with what they believe needs to be done." (p. 23).
- **A problem of data plus a problem of risk (Kanter 1988).** "The Abilene Paradox has two parts. The first involves a person's inaccurate assumptions about what others think and believe. This sometimes takes the guise of what social scientists call "pluralistic ignorance"—everybody in a group holds a similar opinion but, ignorant of the opinion of others, believes himself to be the only one feeling that way." (p. 37); "The second part of the paradox involves a person's unwillingness to speak up about what she does think and believe." (p. 37); "Part one, then, is a problem of data. Part two is a problem of risk." (p. 38).
- **A symptom of a management failure (Carlisle 1988).** "They are important symptoms — symptoms that cannot be ignored, because they demonstrate an inability to manage an organization in a truly professional manner. Indeed, they reflect deep-seated organizational problems that go far beyond questions of conflict or agreement." (p. 41); "A failure of management occurs when a climate exists in which organization members are unwilling to express conflicting opinions whether the boss is present or not." (p. 41).
- **Social preferences under incomplete information (Flores, Mannahan & Sohn 2025; their model and findings).** "We show that in a sequential voting game, a combination of social preferences and incomplete information can lead to the AP." "We find evidence suggesting that subjects vote according to the group's preference rather than their selfish preference, potentially leading to the AP." "Moreover, we find a position effect: when subjects are the first to vote in the group, they are more likely to vote according to their selfish preference than when they are the second, third, and so on." (abstract). The full paper was not read.

*Limits on record.* Harvey himself, in 1988: "All this has occurred despite the fact that, to this day, I cannot prove scientifically that the Abilene Paradox actually occurs." and "For example, it is altogether possible that my in-laws really wanted to go on the original trip, but changed their stories once we arrived in Abilene and had such a lousy time." (epilogue, p. 37). No other critic of the concept was found in the sources read; Wikipedia's article names none (rev. 1368918145).

## Arguments in play

(none recorded as separate argument pages yet). Harvey's own "paradox within a paradox": "But therein lies a paradox within a paradox, because our very unwillingness to take such risks virtually ensures the separation and aloneness we so fear." (p. 27), with "In effect, we reverse “real existential risk” and “fantasied risk” and by doing so transform what is a probability statement into what, for all practical purposes, becomes a certainty." (p. 27). On shared responsibility he cites a cliché: "“It takes a real team effort to go to Abilene.”" (p. 27). Remedies on record: Harvey: "I have found one way in particular to be effective—confrontation in a group setting." (p. 31); Kanter recommends that managers "frame every issue as a debate between alternatives —a matter of pros and cons." and "Assign gadflies, devil's advocates, fact checkers, and second guessers." (pp. 38–39).

## Thinkers who addressed it

- **C. S. Lewis** (*The Screwtape Letters*, 1944, pp. 133–134) — named by Carlisle (1988, p. 40) as an earlier statement of the pattern: "In educating his nephew Wormwood in the wiles of temptation, the old devil Screwtape talks of the discord that can be engendered by urging people to argue in favor of what they believe (often incorrectly) other people want to do; this in spite of their own desire to do exactly the opposite." Lewis's text was not read here.
- **Jerry B. Harvey** (1974; epilogue 1988) — coined the term; the idea "was born October 9, 1971 as part of a presentation I gave to the Organization Development (OD) Network" (epilogue, p. 35).
- **Rosabeth Moss Kanter** (1988) — the data/risk analysis and the link to pluralistic ignorance.
- **Arthur Elliott Carlisle** (1988) — the management-failure reading.
- **Yoonho Kim** (2001, *Public Administration Quarterly* 25(2), 168–190, [doi:10.1177/073491490102500204](https://doi.org/10.1177/073491490102500204)) — the nine-point contrast with groupthink (abstract only read).
- **Jonathon R. B. Halbesleben, Anthony R. Wheeler & M. Ronald Buckley** (2007, [doi:10.1108/02683940710721947](https://doi.org/10.1108/02683940710721947)) — pluralistic ignorance in organizations; cited by Wikipedia for its Abilene/groupthink contrast (abstract only read; it does not mention Abilene).
- **Anthony Montgomery** (2022) — application to the Hillsborough cover-up.
- **Lia Flores, Rachel Mannahan & Jin-Yeong Sohn** (2023 working paper, SSRN 4406948; 2025) — voting-game model and online experiment.

## Framings and reframings

- **Paradox, fallacy, or neither?** Harvey: "Like all paradoxes, the Abilene Paradox deals with absurdity." (p. 23), and, after Robert Rapaport, "However, as Robert Rapaport and others have so cogently expressed it, paradoxes are generally paradoxes only because they are based on a logic or rationale different from what we understand or expect." "Discovering that different logic not only destroys the paradoxical quality but also offers alternative ways for coping with similar situations." (p. 23). Wikipedia's article labels it "a collective fallacy" (rev. 1368918145, lead) and files it under the categories "Decision-making paradoxes" and "Fallacies"; the list files it under "Decision theory". The propositional check above finds no contradiction in its simplified core (structural note, this implant).
- **Groupthink reconceived (Harvey 1974).** "Sometimes referred to as Groupthink, it has been damned as the cause for everything from the lack of creativity in organizations" (p. 29); "However, analysis of the dynamics underlying the Abilene Paradox opens up the possibility that individuals frequently perceive and feel as if they are experiencing the coercive organization conformity pressures when, in actuality, they are responding to the dynamics of mismanaged agreement." (p. 29). On Irving Janis's *Victims of Groupthink* (1972): "Specifically, many of the events that Janis describes as examples of conformity pressures (that is, group tyranny) I would conceptualize as mismanaged agreement." (p. 35).
- **Groupthink distinguished (Kim 2001).** "The Abilene Paradox and Groupthink seem very similar and even some researchers confuse the two concepts. To make this vagueness clear, this article seeks to make distinctions between the two concepts." The nine points include "(4) private views vs. group illusion; (5) coerced vs. voluntary; (6) dissatisfaction vs. satisfaction" and "(9) fear of separation vs. cohesiveness"; "This article concludes that the group in the Abilene Paradox is in a state of “low energy” and the group in Groupthink is in a state of “high energy.”" (abstract). Wikipedia's article: "However, while groupthink, to some extent, depends on the ability of individuals to perceive attitudes and desires of others, the Abilene paradox hinges on the inability to gauge true wants and intentions of group members." (rev. 1368918145, citing Halbesleben et al. 2007).
- **Pluralistic ignorance.** Halbesleben et al. define it: "Pluralistic ignorance is defined as a situation in which an individual holds an opinion, but mistakenly believes that the majority of his or her peers hold the opposite opinion." (2007, abstract). Kanter treats it as the first part of the paradox (above). Wikipedia's article, citing Halbesleben et al.: "Some researchers consider pluralistic ignorance to be a wider-ranging concept: while both groupthink and the Abilene paradox are usually discussed as the detriments to successful group decision-making, pluralistic ignorance is sometimes evaluated neutrally." (rev. 1368918145).
- **An existential reading (Harvey 1974).** Harvey's bibliography: "Albert Camus in The Myth of Sisyphus and Other Essays (Vintage Books, Random House, 1955) provides an existential viewpoint for coping with absurdity, of which the Abilene Paradox is a clear example." (p. 35).

Not in the excerpts held: the 1974 printing at first hand (ScienceDirect 403; the 1988 reprint was read), Janis 1972, Harvey's 1988 book, Harvey, Novicevic, Buckley & Halbesleben 2004/2008 ("five components", per Wikipedia), Kim 2001 and Flores et al. 2025 beyond their abstracts, and the case studies Wikipedia reports (Bagire 2010; Chen & Chang 2018; Dimitroff et al. 2005).

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — Harvey's use (p. 23) and the list's filing.
- [Fallacy](../vocabulary/fallacy.md) — the word Wikipedia's article labels it with (revision 1368918145 of 2026, lead), quoted under Framings.
- [Validity](../vocabulary/validity.md) — the propositional check above.
- *Groupthink* (Janis, as cited by Harvey), *pluralistic ignorance* (Kanter; Halbesleben et al.), *management of agreement*, *action anxiety* (Harvey) — open work in [vocabulary](../vocabulary/index.md).

Related problems: [Prisoner's dilemma](prisoners-dilemma.md) (listed under "See also" in Wikipedia's article, rev. 1368918145; no source read draws the relation further).
