---
type: article
about: concept
title: "A white horse is not a horse"
description: "Can 'white horse is not horse' (bái mǎ fēi mǎ 白馬非馬), the thesis of the Gongsunlongzi's 'White Horse Discourse', be defended, and what did Gongsun Long mean by it? The five arguments of the dialogue and the readings on record side by side — universals (Fung Yu-lan), classes (Chmielewski), mass-stuff (Hansen), part-whole (Graham), extension of compounds (Hansen 1992), identity versus predication (Fraser), use/mention (Thompson), plural reference (Yi), semantic overlap (Rošker), salience (Mou), court entertainment (Harbsmeier) — each with its owner."
tags: [problem, paradox, philosophy-of-language, logic, chinese-philosophy]
timestamp: 2026-10-02T03:07:33Z
---

# A white horse is not a horse

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Primary text: *Gongsunlongzi* 公孫龍子 ch. 2, "Bai ma lun" 白馬論, Chinese text from
[Wikisource](https://zh.wikisource.org/wiki/%E5%85%AC%E5%AD%AB%E9%BE%8D%E5%AD%90/2)
(public domain; excerpt: `raw/gongsunlongzi-bai-ma-lun-chinese-text.md`).
Maps: Fraser, [SEP Fall 2024 "School of Names"](https://plato.stanford.edu/archives/fall2024/entries/school-names/)
§§6–6.1 and nn. 17–23 (excerpt: `raw/sep-school-names-fall-2024-white-horse.md`),
whose English rendering of the arguments is used below; Fraser,
[SEP Fall 2024 "Mohist Canons"](https://plato.stanford.edu/archives/fall2024/entries/mohist-canons/)
(excerpt: `raw/sep-mohist-canons-fall-2024-white-horse-compounds.md`); Yi
([2018](https://doi.org/10.1163/9789004368446_003), pp. 49–50; excerpt:
`raw/yi-2018-white-horse-paradox-semantics-chinese-nouns.md`). The SEP Fall 2024
archive has no separate "Gongsun Long" entry; Gongsun Long is treated inside
"School of Names". Fraser reports a reading of his own; it is marked as his.

## The question

The dialogue opens: "「白馬非馬，可乎？」曰：「可。」" (opening) — asked whether "white horse not horse" is admissible (可), the proponent says it is.
Fraser renders the thesis in "pidgin English": "So we will translate the main thesis as “White horse is not horse,” variously interpretable as “a white horse is not a horse,” “white horses are not horses,” “a white horse is not an exemplar of the kind horse,” or “the kind white horse is not identical with the kind horse.”" (SEP §6.1).
Yi states why it is filed as a paradox: "It is usual to take the dialogue to present a paradox, the white horse paradox, for the thesis seems patently false." (2018, p. 49); and "But the arguments he presents to defend the thesis seem to have considerable sophistication and substantial unity. This suggests that a cogent logic might be behind the apparent sophistries." (p. 49).
Indraccolo: "The somewhat disorienting statement at the center of this debate is discussed at length by two anonymous fictive characters, a persuader and their opponent, in the ‘Báimǎ lùn’ 白馬論 (Disquisition on White and Horse)." ([2017](https://doi.org/10.1111/phc3.12434), abstract; excerpt: `raw/indraccolo-2017-white-horse-is-not-horse-debate.md`).
The interpretive question, as Fraser puts it: "The scholarly controversy concerns what theory and implicit premises to ascribe to the text so that the arguments come out as cogent defenses of a reasonable position." (§6).

**The five arguments** (Fraser's numbering and translation, SEP §6.1; Chinese from the Wikisource text):

1. "Argument 1. ‘Horse’ is that by which we name the shape. ‘White’ is that by which we name the color. Naming the color is not naming the shape. So white horse is not horse." — "馬者，所以命形也；白者，所以命色也；命色者，非命形也。故曰白馬非馬。"
2. "If someone seeks a horse, then it’s admissible to deliver a brown or a black horse. If someone seeks a white horse, then it’s inadmissible to deliver a brown or a black horse." — "求馬，黃、黑馬皆可致；求白馬，黃、黑馬不可致。"
3. "White horse is horse combined with white. Is horse combined with white the same as horse?" — "白馬者，馬與白也，白與馬也，馬與白馬也。故曰白馬非馬也。"
4. "Taking brown horse to be not horse while taking white horse to be having horse, this is flying things entering a pond, inner and outer coffins in different places. These are the most contradictory sayings and confused expressions in the world." — "以黃馬爲非馬，而以白馬爲有馬，此飛者入池而棺椁異處，此天下之悖言亂辭也。"
5. "“Horse” selects or excludes none of the colors, so brown or black horses can all answer." … "Excluding none is not excluding some. Therefore white horse is not horse." — opening "白者不定所白，忘之而可也。" and ending "無去者，非有去也。故曰白馬非馬。"

The objector's turn before argument 4: "馬未與白爲馬，白未與馬爲白。合白與馬，復名白馬。是相與以不相與爲名，未可。故曰白馬非馬，未可。" (Wikisource text). Fraser: "We will follow the traditional order of the text. Many interpreters transpose and reconstruct parts of the text in response to suspected textual corruption." and "The translation that follows is indebted in places to both Graham (1989) and Harbsmeier (1998)." (n. 19).

**Propositional check (this implant, 2026-10-01; logic, not a position).**
Let *i* be *white horse is identical to horse*, *s* be *what is sought in
the two cases is the same*, *p* be *white horses are of the kind horse*.
Argument 2's core, *i* → *s*, ~*s*, therefore ~*i*: `logic.py` returns
`VALID` / `matches schema: modus tollens`. The same premises with the
conclusion ~*p*: `INVALID`, counterexample row `i=F, p=T, s=F`. In words: the
premises settle the identity claim but not the predication claim. This is
the structure behind Fraser's remark on argument 4, "The conclusion indeed follows, but only if we allow the sophist to construe “is not” as “is not identical to.”" (§6.1). The tool treats *i*, *s*, *p* as unanalysed atoms; which of them the Chinese 非 expresses is the interpretive question the readings below answer differently.

## Why it matters

- **Its standing.** Indraccolo: "The so‐called “white horse is not horse” ( bái mǎ fēi mǎ 白馬非馬) debate, or “white horse” ( bái mǎ 白馬) dialogical argument, is beyond doubt the most famous case of argumentation ( biàn 辯) in the history of Classical Chinese philosophy." (2017, abstract).
- **Same and different.** Fraser on the Mohist background: "“White horses are horses” would be interpreted as in effect claiming that white horses and horses are “the same,” and “Oxen are not horses” as claiming that oxen and horses are “different.”" (SEP "Mohist Canons").
- **Semantics of compounds.** Fraser: "In classical Chinese, ‘oxen-and-horses’ ( niú mǎ 牛馬) and ‘white horse’ ( bái mǎ 白馬) have a similar formal structure, but the first denotes the sum of two kinds of things, the second a portion of one kind of thing." (SEP "Mohist Canons"); the Mohist parallel "White horses are horses; riding white horses is riding horses. Black horses are horses; riding black horses is riding horses." is quoted there as a case of parallel reasoning.
- **Early reception.** Fraser: "The Xunzi does not criticize him by name but does cite a version of his white horse sophism in a list of incorrect uses of names (22.3)." (SEP §6). Willman: "Xunzi’s reference to this example in particular in Book 22 of the Xunzi is likely his response to the paradoxical statement “White horses are not horses”, famously asserted by the sophist Gongsun Long probably as a foil to the Mohists’ theories of naming and reference" ([SEP Fall 2024 "Logic and Language in Early Chinese Philosophy"](https://plato.stanford.edu/archives/fall2024/entries/chinese-logic-language/); excerpt: `raw/sep-chinese-logic-language-fall-2024-white-horse.md`).
- **Comparative logic.** Fraser (§6.1) and Fung (1948, pp. 87–88) both describe the arguments in Western logical vocabulary — identity, predication, intension, extension; see the readings below.

## Positions taken

Fraser on the field: "The “White Horse Discourse” has spawned nearly as many interpretations as there are interpreters." (§6.1); "The Gongsun Longzi has inspired a vast exegetical literature in both Asian and European languages, with no consensus in sight as to the significance and theoretical basis of its arguments." (§6). His catalogue: "Other interpretations have taken it to deal with kind and identity relations (Cikoski 1975, Harbsmeier 1998), part-whole relations (Hansen 1983, Graham 1989), how the extensions of phrases vary from those of their constituent terms (Hansen 1992), and even the use/mention distinction (Thompson 1995)." (§6.1). Yi groups readings by what *ma* is taken to refer to (2018, pp. 49–50). The readings are listed in rough order of first publication as given by the sources; none is ranked here.

- **Universals (Fung Yu-lan 1948; Hu Shih 1922; Fung Yiu-ming 2007; Cheng 1983).** Fung: "Instead of emphasizing, as did Hui Shih, that actual things are relative and changeable, Kung-sun Lung emphasized that names are absolute and permanent. In this way he arrived at the same concept of Platonic ideas or universals that has been so conspicuous in Western philosophy." (*A Short History of Chinese Philosophy*, p. 87; excerpt: `raw/fung-1948-short-history-chinese-philosophy-white-horse.md`). He reads "three arguments": the first "emphasizes the difference in the intension of the terms “horse,” “white,” and “white horse.”" (p. 87), the second "the difference in the extension of the terms “horse” and “white horse.”" (p. 88), and in the third "Kung-sun Lung seems to emphasize the distinction between the universal, “horseness,” and the universal, “white-horseness.”" (p. 88). Yi places Hu Shih (1922) and Fung Yiu-ming (2007) with Fung (p. 49).
  *Against:* Fraser reports: "There is now a fairly broad consensus, at least among European and American scholars, that the text is unlikely to concern universals, since no ancient Chinese philosopher held a realist doctrine of universals." (§6.1). Yi: "But I do not think there is a good reason to take him to use it to refer to an abstract entity (e.g., a universal, a set) or a kind of whole (e.g., stuff, a collection-whole)." (p. 50).
- **Classes (Chmielewski 1962).** "Janusz Chmielewski (1962) holds that his thesis in the dialogue denies identity between two classes: the class of white horses and that of horses." (Yi, p. 50).
- **Mass-stuff (Hansen 1976, 1983, 1998).** Yi: "While these interpretations take the thesis to concern abstract entities (e.g., attributes, classes), Chad Hansen (1983; 1992; 1998) holds that it is a thesis about concrete particulars." "On his interpretation, which he calls “the Mass-Stuff Interpretation” (1983, 148),3 the thesis concerns mass or stuff:" "(a) the “horse-stuff” (ibid., 141), the stuff of which all horses are parts; and (b) the white-horse-stuff, the stuff of which all white horses are parts." (p. 50). Hansen's first statement is *Mass Nouns and 'A White Horse Is Not a Horse'* ([1976](https://doi.org/10.2307/1398188), *Philosophy East and West* 26(2): 189ff.; not read here). Yi lists "Hansen (1976), Graham (1986), and Krifka (1995)" as "similar interpretations" (n. 3).
  *Against:* Yi on Hansen 1998: "But this interpretation conflicts with passages of the White Horse Dialogue that assumes that the horses, unlike the white horses, include the black (or yellow) horses (see the passage discussed in §3)." (n. 4). Manyul Im's *Horse-parts, White-parts, and Naming* ([2007](https://doi.org/10.1007/s11712-007-9010-4), *Dao* 6(2)) is a reply to Hansen; it was not read here.
- **Part-whole (Graham 1989; Hansen 1983).** Fraser: "This argument can also be read as treating white and horse as two parts of a whole, as Graham suggests (1989)." (n. 20). Graham's own framing of the difficulty, as Fraser quotes it: "the difficulty of finding an angle of approach from which the arguments will make sense.…The arguments are clear, yet the first seems an obvious non sequitur…and the rest seem to assume an elementary confusion of identity and class membership" (1989: 82) and "No one has yet proposed a reading of the dialogue as a consecutive demonstration which does not turn it into an improbable medley of gross fallacies and logical subtleties" (1990: 193).
  *Against:* Fraser: "But doing so does not really enhance the explanatory value of our interpretation, nor make the argument more cogent. If we say that white horse is a whole with two parts, one named by ‘white’ and one by ‘horse’, it’s not clear how that helps us get from ‘naming the color is not naming the shape’ to ‘white horse not horse’." (n. 20).
- **Compounds and one-name-one-thing (Hansen 1992).** Fraser's summary: "The simplest early Chinese model of the language-world relation was “one name, one thing,” according to which all names refer at the same level of generality." "The extension of ‘white horse’ is the intersection, not the sum, of white things and horses." "The approach implied by “White Horse,” Hansen suggests, would address the problem by retaining the one-name-one-thing principle and reforming our language use, so that all names pick out exactly the same portion of reality in all contexts, whether used singly or compounded into phrases." — on which "white horses are neither white nor horse, but a distinct sort of thing." (§6.1). Fraser's assessment of that view: "But moving beyond the one-name-one-thing model and explaining exactly why this is absurd was a legitimate philosophical puzzle at the time." (§6.1).
  *Against:* on Hansen's further claim — "Noting that Gongsun Long cites Confucius in the anecdote about the King of Chu, Hansen (1992) suggests that he is proposing a language reform as a defense of the Confucian theory of “correcting names.”" — Fraser: "This strikes me as far-fetched, given that Gongsun was notorious for twisting people’s words and that his ethical sympathies seem to have lain more with the Mohists than the Confucians." (n. 23).
- **Identity versus predication (Fraser 2024; kind and identity relations: Cikoski 1975, Harbsmeier 1998).** Fraser's own reading: "To sum up, the most natural way to read the text is as repeatedly equivocating between a statement of identity and one that predicates a more general term of the objects denoted by a less general term." "The sophist refuses to distinguish the true statement that “[the kind] white horse is not [identical to the kind] horse” from the false “white horse is not [of the kind] horse.”" (§6.1). On argument 2: "The sophist plainly construes “white horse is horse” as “white horse is identical to horse.”" and "Notice that the sophist implicitly applies a principle roughly like Leibniz’s law of indiscernibility of identicals." (§6.1). Harbsmeier, as Fraser reports: "Harbsmeier also points out that by using the example of seeking a horse, instead of having a horse, the sophist has created an intensional context, making it that much easier to show that “white horse” and “horse” are not intersubstitutable and thus not identical (1998: 306)." (n. 21). Fraser on argument 1: "Hence we should reject the third premise and insist that naming the color is naming the shape." (§6.1).
- **Use/mention (Thompson 1995).** Yi's report: "Thompson holds that Gongsun Long holds a “patently true” thesis about linguistic expressions: “the term ‘white horse’ differs from the term ‘horse’” (1995, 484)." (n. 5; Thompson, *When a 'White Horse' Is Not a 'Horse'*, [*Philosophy East and West* 45(4): 481ff.](https://doi.org/10.2307/1399790); not read here).
  *Against:* Yi: "But it would be hard to take him to deploy the complicated arguments in the dialogue to propose and defend this obviously true thesis." (n. 5).
- **Collection-wholes (Mou 1999, 2006, 2007).** Yi: "He takes the thesis to be about so-called collectionwholes or “wholes each of which itself consists of many countable things”, such as the many horses (1999, 51)." (p. 50).
- **Plural reference (Yi 2018).** Yi's own: "And I think we can take him to use it to refer to concrete individuals: the many horses (i.e., all the horses taken together)." (p. 50).
- **Semantic overlap (Rošker 2021, after Xiang 2000).** "Gongsun Long attempted to eliminate this semantic overlapping, or at least to reduce it to a level on which language could still be overseen and controlled. The famous ‘White horse not horse’ debate was an attempt to deal with these concerns." ([SEP Fall 2024 "Chinese Epistemology"](https://plato.stanford.edu/archives/fall2024/entries/chinese-epistemology/), §3.3; excerpt: `raw/sep-chinese-epistemology-fall-2024-gongsun-long-names.md`). The later Mohists, on her account, differed: "For the Neo-Mohist philosophers, however, the semantic overlapping of different terms was a natural quality of human language and, consequently, they saw no need to eliminate it." (§3.3).
- **Salience (Mou 2016, as Willman reports it).** "For example, the judgment “A white horse is not a horse” may be deemed false if the salient aspect of our mental focus is on the “horse-ness” feature of each entity indicated (white horse and horse). But it may also be deemed true if the salient aspect is “whiteness”, since whiteness is a feature that may be true of some horses but not others." (Willman, SEP "Logic and Language").
- **Performance, not doctrine (Harbsmeier 1998, adopted by Fraser).** Fraser reports Harbsmeier: "He suggests that Gongsun Long probably belonged to a class of entertainers at Chinese courts who performed various skills or tricks." and "His sophistries may have been intended primarily as a kind of light entertainment, not as expressions of a principled philosophical position." (§6). Fraser's assessment: "Building on Harbsmeier’s insight that the historical context of Gongsun Long’s disputations has been insufficiently appreciated, we may suspect Graham’s remarks signal interpretive charity gone too far." He compares the text to something "roughly a Chinese analogue to the subtle, fallacious, and deeply amusing arguments of Lewis Carroll." and adds "We can learn about the serious practice of disputation by studying what is in effect a spoof of disputation, just as an anthropologist can learn about a culture by studying its humor." (§6).
  *Against (on record in the sources read):* Yi's starting point runs the other way: "But the arguments he presents to defend the thesis seem to have considerable sophistication and substantial unity." (p. 49).

**Distribution, as reported.** Fraser: "The interpretation proposed here must be considered only one of several potentially defensible approaches (others are noted below)." (§6). Yi: "Although most Chinese speakers would use (G) to mean a patent falsity, he might use it to state a true or plausible thesis different from the falsity. And most interpretations of the dialogue take him to defend such a thesis." (p. 49). No survey figure is recorded.

## Arguments in play

(none recorded as separate argument pages yet). The five arguments of the
dialogue are quoted under The question; the propositional check there
separates the identity and predication readings.

- **The King of Chu analogy (Gongsunlongzi ch. 1; Kong Congzi 11).** In the later anecdote Fraser translates, Gongsun Long cites Confucius on the King of Chu: "He should simply have said, ‘A person lost a bow, a person will find it,’ that’s all. Why must it be ‘Chu’?"; Kong Chuan's reply in the *Kong Congzi*: "Wishing to broaden the referent of ‘person’, it’s appropriate to omit the ‘Chu’; wishing to fix the name of the color, it’s not appropriate to omit the ‘white’." (SEP §6.1). Fraser, after Harbsmeier: "it suggests that the book’s ancient editors themselves took the theme to be how the scope of the extension of a noun such as ‘person’ or ‘horse’ varies when modified by an adjective such as ‘Chu’ or ‘white’." (§6.1).
- **Xunzi's common names.** Fraser: "Xunzi, whose career largely overlapped with Gongsun Long’s, introduced the concept of a “common name” (gong ming), or general term, which may refer to things at different levels of generality (22.2f)." (§6.1).
- **The Mohist "white all over" contrast.** "But whereas a white horse is white all over, a blind horse is not “blind all over”; only its eyes are blind (B3)." (Fraser, SEP "Mohist Canons").

## Thinkers who addressed it

- **Gongsun Long** (c. 320–250 BCE per Fraser §6) — the dialogue; the frontier anecdote in Fung's telling: "Lung replied: “My horse is white, and a white horse is not a horse.” And so saying, he passed with his horse." (p. 87).
- **Kong Chuan** — opponent in the *Gongsunlongzi* ch. 1 and *Kong Congzi* anecdotes (Fraser §6.1).
- **Xunzi** (*Xunzi* 22) — common names; cites the sophism (Fraser §6; Willman).
- **Hu Shih** (1922), **Fung Yu-lan** (1948, pp. 87–88), **Fung Yiu-ming** (2007, 2020b) — universals (Yi p. 49).
- **Janusz Chmielewski** (1962) — classes; **John Cikoski** (1975) — kinds and identity.
- **A. C. Graham** (1957, reprinted 1990; 1989) — part-whole; dating of the *Gongsunlongzi*: "A. C. Graham argued persuasively that three of the dialogues are not Warring States texts, but much later forgeries pieced together partly from misunderstood bits of the Mohist Dialectics." (Fraser's assessment, §6); Fraser n. 17: "Graham’s conclusions, first published in 1957 and reprinted in his (1990), have been widely accepted by European and American scholars but almost completely ignored by scholars writing in Chinese."
- **Chad Hansen** (1976, 1983, 1992, 1998, 2007) — mass-stuff; one-name-one-thing; *Prolegomena to Future Solutions to 'White-Horse Not Horse'* ([2007](https://doi.org/10.1111/j.1540-6253.2007.00435.x), *Journal of Chinese Philosophy* 34(4): 473–491; not read here).
- **Kirill Ole Thompson** (1995) — use/mention. **Christoph Harbsmeier** (1998) — intensional context; court entertainment.
- **Bo Mou** (1999, 2006, 2007, 2016), **Manyul Im** (2007), **Byeong-uk Yi** (2014, 2018), **Lisa Indraccolo** (2016, 2017), **Jiang Xiangdong** (2020), **Zhou Changzhong** (2020), **Jana Rošker** (2021), **Marshall Willman** (2022), **Chris Fraser** (SEP 2024).

## Framings and reframings

- **Grammar of 非.** Fraser on argument 4: "The conclusion indeed follows, but only if we allow the sophist to construe “is not” as “is not identical to.”" (§6.1) — the copula, not the horse, carries the problem on this framing.
- **Reference of the bare noun.** Yi: "These interpretations have a common feature. They all take the noun ma ‘horse’ in the predicate of (G) to figure as a referential term, one that refers to a universal, a set, stuff, a collection-whole, etc." (p. 50).
- **Fit with reality.** Fraser: "Gongsun Long’s disputation is perceived as plainly not fitting “reality” (shi, also the “stuff” spoken of)." (§6), reporting the *Annals of Lü Buwei* anecdote.
- **Composite text.** Indraccolo: "The Gōngsūn Lóngzǐ is a composite collection of heterogeneous materials in six chapters." (abstract); Fraser: "Probably only the “White Horse,” the essay “Indicating Things,” and a bit of another dialogue are genuine pre-Han texts." (§6).

Not in the excerpts held: Hansen 1976 and 1983, Graham 1989 and 1990
beyond Fraser's quotations, Thompson 1995, Harbsmeier 1998, Im 2007 and
Indraccolo 2017 beyond its abstract. The Chinese Text Project text and its
English translation were not retrieved (the site refused automated access);
the Chinese is quoted from Wikisource, the English from Fraser.

## Vocabulary

- [Paradox](../vocabulary/paradox.md) — see The question.
- [Validity](../vocabulary/validity.md) and [Classical logic](../methods/classical-logic.md) — the propositional check.
- [Fallacy](../vocabulary/fallacy.md) — Graham's phrase, as Fraser quotes it (§6): "an improbable medley of gross fallacies and logical subtleties" (1990: 193).
- *Mass noun*, *identity vs. predication*, *intension/extension*, *use/mention*, *ming* 名 (name), *shi* 實 (stuff, reality) — open work in [vocabulary](../vocabulary/index.md).

Related thinkers: [Confucius](../thinkers/confucius.md) (correcting names, Analects 13.3).
