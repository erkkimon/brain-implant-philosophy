---
type: article
about: concept
title: "Hedgehog's dilemma"
description: "Porcupines on a cold day huddle for warmth, prick each other with their quills, and part until they find a tolerable distance: Schopenhauer's parable (Parerga and Paralipomena II, 1851, §396) of the need for company and the friction of it, read by Freud (1921) as the hostility left by lasting intimate ties and tested by Maner, DeWall, Baumeister and Schaller (2007) as the 'porcupine problem' of how people respond to social exclusion."
tags: [problem, paradox, dilemma, decision-theory, social-psychology, schopenhauer]
timestamp: 2026-10-08T20:29:06Z
---

# Hedgehog's dilemma

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md), filed by its sources as a [dilemma](../vocabulary/dilemma.md)
and listed by Wikipedia among [paradoxes](../vocabulary/paradox.md).
Primary text: Arthur Schopenhauer, *Parerga und Paralipomena* II, ch. 31
"Gleichnisse, Parabeln und Fabeln", §396 (Berlin: Hayn, 1851, pp. 524–525;
German text at [Wikisource](https://de.wikisource.org/wiki/Die_Stachelschweine);
English, T. Bailey Saunders, *Studies in Pessimism*, "A Few Parables",
[Gutenberg #10732](https://www.gutenberg.org/ebooks/10732); excerpt:
`raw/schopenhauer-1851-parerga-396-porcupines-saunders-and-german.md`).
Admitted from Wikipedia's List of paradoxes, [revision 1376699902](https://en.wikipedia.org/w/index.php?title=List_of_paradoxes&oldid=1376699902),
section "Decision theory"; the article "Hedgehog's dilemma",
[revision 1377345453](https://en.wikipedia.org/w/index.php?title=Hedgehog%27s_dilemma&oldid=1377345453),
was used as a pointer to the sources below (excerpt:
`raw/wikipedia-hedgehogs-dilemma-rev-1377345453-and-list-entry.md`).
Thinker: [Arthur Schopenhauer](../thinkers/schopenhauer.md).

## The question

Schopenhauer's parable, in Saunders's translation: "A number of porcupines huddled together for warmth on a cold day in winter; but, as they began to prick one another with their quills, they were obliged to disperse. However the cold drove them together again, when just the same thing happened. At last, after many turns of huddling and dispersing, they discovered that they would be best off by remaining at a little distance from one another."
The German original: "Eine Gesellschaft Stachelschweine drängte sich, an einem kalten Wintertage, recht nahe zusammen, um durch die gegenseitige Wärme, sich vor dem Erfrieren zu schützen." (§396, 1851, p. 524).

His application to people: "In the same way the need of society drives the human porcupines together, only to be mutually repelled by the many prickly and disagreeable qualities of their nature. The moderate distance which they at last discover to be the only tolerable condition of intercourse, is the code of politeness and fine manners; and those who transgress it are roughly told--in the English phrase--_to keep their distance_."
The German names the source of the need: "So treibt das Bedürfnis der Gesellschaft, aus der Leere und Monotonie des eigenen Innern entsprungen, die Menschen zu einander" (§396), where the need for company is said to spring from the emptiness and monotony of one's own inner life (this implant's paraphrase of the German clause, not a translation on record; Saunders's version omits the clause).

The question the sources draw from it is how much closeness people can bear when closeness both satisfies a need and causes pain. Maner, DeWall, Baumeister and Schaller (2007, Conclusion) state it as: "Schopenhauer’s parable of the porcupines highlights an essential tension in a social species such as ours: People seek interactions with others in order to satisfy essential needs, and yet these interactions can cause people pain, including the pain of exclusion."

**Naming.** Schopenhauer's animals are *Stachelschweine*, porcupines (§396); Freud (1921) and Maner et al. (2007) keep the porcupine. The name "hedgehog's dilemma" is the one Wikipedia uses: "The hedgehog's dilemma, or sometimes the porcupine dilemma, is a metaphor about the challenges of human intimacy." (rev. 1377345453, lead). Maner et al. call it "the porcupine problem" (title).

**Why "paradox".** The list entry under "Decision theory" reads: "Hedgehog's dilemma: Despite goodwill, human intimacy cannot occur without substantial mutual harm." (rev. 1376699902). That wording is the list's; Schopenhauer's parable ends with the porcupines at "a little distance from one another" (Saunders). The article's lead calls it a "metaphor" and the article is filed in Wikipedia's categories "Dilemmas" and "Paradoxes" (rev. 1377345453). None of the primary sources read calls it a paradox.

**Propositional check (this implant, 2026-10-08; logic, not a position).**
A reading of the two "evils" ("zwischen beiden Leiden hin und hergeworfen",
§396) as a dilemma: let *C* = *the porcupines come close*, *P* = *they are
pricked*, *F* = *they are cold*. `logic.py check --premises "C -> P" "~C -> F" --conclusion "P | F"`
outputs `VALID`; with the conclusion `"P & F"` it outputs `INVALID`
(counterexample rows include `C=T, F=F, P=T`). Writing *D* for *they stay
apart*, `--premises "C -> P" "D -> F" "C | D"` with conclusion `"P | F"`
outputs `VALID` and `matches schema: constructive dilemma`; adding a third
option *M* (`"C | D | M"`) outputs `INVALID` with the row
`C=F, D=F, F=F, M=T, P=F`. Schopenhauer's "mittlere Entfernung" (§396) is
such a third option in his telling; whether it escapes both evils is not a
logical question, and he says it satisfies the need for warmth "only very
moderately" (Saunders) / "nur unvollkommen" (German).

## Why it matters

- **Schopenhauer's own use: sociability and solitude.** The parable ends: "By this arrangement the mutual need of warmth is only very moderately satisfied; but then people do not get pricked. A man who has some heat in himself prefers to remain outside, where he will neither prick other people nor get pricked himself." (Saunders). In *Counsels and Maxims* (Saunders tr.) Schopenhauer points to it: "But a man who has a great deal of intellectual warmth in himself will stand in no need of such resources. I have written a little fable illustrating this: it may be found elsewhere." The translator's note: "The passage to which Schopenhauer refers is _Parerga_: vol. ii. § 413 (4th edition)." The same passage states: "As a general rule, it may be said that a man's sociability stands very nearly in inverse ratio to his intellectual value".
- **Psychoanalysis: ambivalence in close ties.** Freud (1921, ch. VI, Strachey tr. 1922): "According to Schopenhauer's famous simile of the freezing porcupines no one can tolerate a too intimate approach to his neighbour." and next: "The evidence of psycho-analysis shows that almost every intimate emotional relation between two people which lasts for some time--marriage, friendship, the relations between parents and children[35]--leaves a sediment of feelings of aversion and hostility, which have first to be eliminated by repression." (excerpt: `raw/freud-1921-group-psychology-porcupines-footnote.md`).
- **Social psychology: responses to exclusion.** Maner et al. (2007) take the parable as the frame for experiments on what people do after being excluded (see Positions taken). Prochnik (2007), in *Cabinet*, writes: "One could say that the dilemma of the porcupine, as rendered by Schopenhauer, is the Freudian relationship problematic as such." (excerpt: `raw/prochnik-2007-porcupine-illusion-freud.md`).

## Positions taken

No grouping of answers was found in the sources read; the answers on record
are listed by owner, unranked.

- **Keep a mean distance: politeness (Schopenhauer 1851, §396).** The German: "Die mittlere Entfernung, die sie endlich herausfinden, und bei welcher ein Zusammenseyn bestehn kann, ist die Höflichkeit und feine Sitte." with the cost: "Vermöge derselben wird zwar das Bedürfniß gegenseitiger Erwärmung nur unvollkommen befriedigt, dafür aber der Stich der Stacheln nicht empfunden." For the person with inner warmth, staying away: "Wer jedoch viel eigene, innere Wärme hat bleibt lieber aus der Gesellschaft weg, um keine Beschwerde zu geben, noch zu empfangen."
- **The hostility is real and is lifted by group ties (Freud 1921, ch. VI).** After the porcupine passage Freud names the mixed feeling: "When this hostility is directed against people who are otherwise loved we describe it as ambivalence of feeling" and states its counterweight: "But the whole of this intolerance vanishes, temporarily or permanently, as the result of the formation of a group, and in a group." (Strachey tr. 1922).
- **People do both: withdraw and reconnect (Maner, DeWall, Baumeister & Schaller 2007).** Their finding: "Evidence from 6 experiments supports the social reconnection hypothesis, which posits that the experience of social exclusion increases the motivation to forge social bonds with new sources of potential affiliation." (abstract). Limits they report: "Excluded individuals did not seem to seek reconnection with the specific perpetrators of exclusion or with novel partners with whom no face-to-face interaction was anticipated." and "Furthermore, fear of negative evaluation moderated responses to exclusion such that participants low in fear of negative evaluation responded to new interaction partners in an affiliative fashion, whereas participants high in fear of negative evaluation did not." (abstract). Their summary: "There is no simple answer because apparently people do both." (Conclusion). DOI verified: [10.1037/0022-3514.92.1.42](https://doi.org/10.1037/0022-3514.92.1.42) (excerpt: `raw/maner-2007-social-exclusion-porcupine-problem.md`).
  *Their contrast with Schopenhauer:* "Schopenhauer (1851/1964) suggested that people ultimately feel compelled to retain a safe distance from each other." and "So it is not surprising that he resigned his porcupines to a life spent shivering in the cold, fearing pain from other porcupines’ sharp quills. In real life, however, the porcupine problem is often resolved in a far more sociable manner." (Conclusion, pp. 53–54; they support the remark on Schopenhauer's temperament with a quotation from Russell 1945, p. 758).
  *Their own stated limits:* "Although experimental methods were ideal for testing causal hypotheses about rejected individuals’ perceptions and behavioral inclinations, they can only begin to suggest eventual consequences that may unfold dynamically in the course of ongoing social interactions." (p. 53). Study 1's sample: "Participants. Fifty-six undergraduates" (Study 1, method). They note earlier work going the other way: "In fact, much of the previous research in this area has observed antisocial—rather than affiliative—responses to exclusion" (p. 42).
  *A later meta-analysis that includes their study (Gerber & Wheeler 2009):* "This article presents the first meta-analysis of experimental research on rejection, sampling 88 studies." and "The belonging hypothesis is only partially correct. The most important caveat to our needs findings (and the belonging hypothesis) is that people will not always seek to restore belonging following rejection. People will restore both belonging and control if possible but will prioritize restoring control over restoring belonging." (*Perspectives on Psychological Science* 4(5), 468–488; [doi:10.1111/j.1745-6924.2009.01158.x](https://doi.org/10.1111/j.1745-6924.2009.01158.x), verified via Crossref; Maner et al. 2007 is asterisked as included; excerpt: `raw/gerber-wheeler-2009-rejection-meta-analysis.md`). Gerber and Wheeler do not mention the porcupines in the text searched.

## Arguments in play

(none recorded as separate argument pages yet). The structure on record is
Schopenhauer's two "evils" with a third option found by trial (§396); its
propositional form is checked in The question. Freud's ch. VI argument runs
from the simile to the claim that lasting intimate ties leave "a sediment of
feelings of aversion and hostility" (Strachey tr.) and from there to the
libidinal tie of the group.

## Thinkers who addressed it

- **Arthur Schopenhauer** (*Parerga und Paralipomena* II, 1851, ch. 31, §396; §413 in the 4th edition per Saunders) — the parable and politeness as the "mean distance"; see [Schopenhauer](../thinkers/schopenhauer.md).
- **Sigmund Freud** (*Massenpsychologie und Ich-Analyse*, 1921, ch. VI; Strachey tr. 1922, text and note 34) — the simile as an illustration of ambivalence in lasting relations. In the German edition the parable is in the main text; Strachey's translator's note says that "certain passages have been transferred in the English version from the text to the footnotes" at "the author's express desire". Prochnik (2007) reports Freud's 1909 remark "I am going to America to catch sight of a wild porcupine and to give some lectures." and that Freud wrote in 1925 that he came to Schopenhauer's work "very late in life." (as Prochnik quotes him; not checked against Freud's text here).
- **Jon K. Maner, C. Nathan DeWall, Roy F. Baumeister, Mark Schaller** (*JPSP* 92(1), 2007, 42–55) — the "porcupine problem" as a question about exclusion and reconnection.
- **Jonathan Gerber & Ladd Wheeler** (*Perspectives on Psychological Science*, 2009) — meta-analysis of rejection experiments including Maner et al.; reported above, they do not frame it by the parable.
- **George Prochnik** (*Cabinet* 26, 2007) — essay on the porcupine in Freud's circle and Freud's relation to Schopenhauer.

## Framings and reframings

- **Parable of society or of intimacy.** Schopenhauer's text is about "the need of society" and its answer is politeness (§396, Saunders). Freud moves it to "almost every intimate emotional relation between two people which lasts for some time" (1921, ch. VI, Strachey tr.). Wikipedia's article calls it "a metaphor about the challenges of human intimacy" and states: "Despite goodwill, humans cannot be intimate without the risk of mutual harm, leading to cautious and tentative relationships." (rev. 1377345453, lead, citing Veit, *Psychology Today* blog, 2020, not read here).
- **From parable to testable hypothesis.** Maner et al. turn the two pulls into two predicted responses to exclusion — withdraw from the pain or seek new bonds — and report both (2007, Conclusion). Gerber and Wheeler (2009) describe the wider pattern as a puzzle in their field: "Possibly the biggest puzzle in the rejection literature is that rejection makes people act prosocially some of the time and antisocially at other times." and they note that aggressive responses are "considered paradoxical by some" (abstract).
- **Possible or impossible.** The Wikipedia list's wording ("cannot occur without substantial mutual harm") and its article ("this cannot occur, for reasons they cannot avoid") present the closeness as unattainable; Schopenhauer's porcupines find a distance "in der sie es am besten aushalten konnten" (§396), and Maner et al. report that the problem "is often resolved in a far more sociable manner" (Conclusion). Reported side by side, not weighed.

## Vocabulary

- [Dilemma](../vocabulary/dilemma.md) — in the loose sense of a choice between two bad options; the propositional check above uses the argument-form sense.
- [Paradox](../vocabulary/paradox.md) — the label is the Wikipedia list's; see **Why "paradox"** under The question.
