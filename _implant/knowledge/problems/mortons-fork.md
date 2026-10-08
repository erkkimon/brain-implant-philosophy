---
type: article
about: concept
title: "Morton's fork"
description: "Is a dilemma whose two horns both end in the same demand an argument or a trap — and who first used it? Bacon (1622) reports 'a tradition of a dilemma' of Bishop Morton for raising the benevolence; Fowler (DNB 1889) and Pollard (EB 1911) report Erasmus's earlier story of the same dilemma told of Richard Fox; Wikipedia files the name as a 'false dilemma' in which contradictory observations lead to the same conclusion."
tags: [problem, paradox, decision-theory, logic, dilemma, history]
timestamp: 2026-10-08T21:37:56Z
---

# Morton's fork

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
sources graded as in [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md). Admitted from Wikipedia's
[List of paradoxes, rev. 1376699902](https://en.wikipedia.org/w/index.php?title=List_of_paradoxes&oldid=1376699902),
section "Decision theory" (entries taken in list order), which gives it as "Morton's fork: a type of false dilemma in which contradictory observations lead to the same conclusion."
The label "paradox" is that list's; none of the historical sources read
below calls it one (they call it "a dilemma" or "the fork").
Primary text: Francis Bacon, *The Historie of the Raigne of King Henry the Seventh*
(1622), p. 101 ([1622 scan, archive.org](https://archive.org/details/bim_early-english-books-1475-1640_the-historie-of-the-raig_bacon-francis-viscount_1622));
quoted in the modernised spelling of the Devey edition, *Moral and Historical
Works of Lord Bacon* (1877), p. 377 ([archive.org](https://archive.org/details/moralhistoricalw00baco_1);
excerpt: `raw/bacon-1622-history-of-henry-vii-mortons-fork.md`).
Historians: Stubbs, lecture of 1883 ([Wikisource oldid 11395369](https://en.wikisource.org/w/index.php?oldid=11395369);
excerpt: `raw/stubbs-1883-reign-of-henry-vii-mortons-fork.md`); Fowler and
Archbold, *Dictionary of National Biography* ([Foxe, oldid 10747439](https://en.wikisource.org/w/index.php?oldid=10747439);
[Morton, oldid 10742965](https://en.wikisource.org/w/index.php?oldid=10742965);
excerpt: `raw/dnb-1889-1894-morton-and-foxe-mortons-fork.md`); Pollard,
*Encyclopaedia Britannica* 11th ed. ([Morton, oldid 6638856](https://en.wikisource.org/w/index.php?oldid=6638856);
[Fox, oldid 6371893](https://en.wikisource.org/w/index.php?oldid=6371893);
excerpt: `raw/pollard-1911-britannica-morton-and-fox-mortons-fork.md`).
Reference works: *Oxford Dictionary of Phrase and Fable* via
[Encyclopedia.com](https://www.encyclopedia.com/humanities/dictionaries-thesauruses-pictures-and-press-releases/mortons-fork)
(excerpt: `raw/oxford-dictionary-of-phrase-and-fable-mortons-fork.md`);
Wikipedia, ["Morton's fork", rev. 1346281900](https://en.wikipedia.org/w/index.php?title=Morton%27s_fork&oldid=1346281900),
used as a pointer to sources and cited as such
(excerpt: `raw/wikipedia-mortons-fork-rev-1346281900-and-list-entry.md`).

## The question

Bacon's report, the earliest read: "There is a tradition of a dilemma, that bishop Morton the chancellor used, to raise up the benevolence to higher rates; and some called it his fork, and some his crotch." (1877 ed., p. 377).
Its content: "For he had couched an article in the instructions to the commissioners who were to levy the benevolence; That if they met with any that were sparing, they should tell them, that they must needs have, because they laid up: and if they were spenders, they must needs have, because it was seen in their port and manner of living." and "So neither kind came amiss." (p. 377).
Stubbs's paraphrase (1883): "if you spend much you have plenty; if you spend little you must have saved; out of your plenty, or out of your savings, you must pay."

Two questions are on record. A historical one: who used the
[dilemma](../vocabulary/dilemma.md), Morton or Richard Fox (see "Positions
taken"). A logical one, raised by the later use of the name: what is wrong,
if anything, with an argument whose two horns lead to the same conclusion —
Wikipedia's list answers "a type of false dilemma" (rev. 1376699902). The
question depends on the [dilemma](../vocabulary/dilemma.md) contract, which
keeps the argument form (valid as a form) apart from the *false dilemma*
charge against a premise.

**Propositional check (this implant, 2026-10-09; logic, not a position).**
Let *S* stand for *the subject spends much*, *L* for *the subject spends
little* and *C* for *the subject can pay*, following Stubbs's paraphrase.
`logic.py check --premises "S | L" "S -> C" "L -> C" --conclusion "C"`
outputs `VALID`. Without the disjunctive premise,
`--premises "S -> C" "L -> C" --conclusion "C"` outputs `INVALID` with the
counterexample row `C=F, L=F, S=F`. With the second horn written as the
negation of the first, as in Wikipedia's "contradictory observations",
`--premises "S -> C" "~S -> C" --conclusion "C"` outputs `VALID`.
The tool checks form only; whether each conditional is true of a given
subject is, per the [dilemma](../vocabulary/dilemma.md) page, a separate,
factual question.

## Why it matters

- **The history of taxation under Henry VII.** Stubbs ties it to the benevolence of 1491: "It is then to this period that we must fix the application of Morton's fork, and to it Lord Bacon assigns the beginning of the penurious or saving habits which later on grew so strong in the king." Archbold (DNB 1894) records that Morton "assisted in collecting the benevolences in 1491 for the French war".
- **The reputation of two ministers.** Stubbs: "Henry VII is constantly accused of avarice, and Morton to the popular mind is best known as the inventor of the fork, Morton's fork, the dilemma by which he proved the necessity of the benevolences, to the great dissatisfaction of the payers". Pollard (EB 1911, "Fox") calls the attribution to Morton "a curious freak of history" (quoted in full under "Positions taken").
- **A name for an argument pattern.** The *Oxford Dictionary of Phrase and Fable*: "The term is now found in wider allusive use." Wikipedia: "The term in its broad application dates at least to the mid-19th century, although Francis Bacon noted in 1622 that it was established by that point in specific reference to Morton's original argument." (rev. 1346281900, lead, citing that dictionary).

## Positions taken

On the attribution, side by side, unranked; no source read groups them.

- **Morton, as a tradition (Bacon 1622).** "There is a tradition of a dilemma, that bishop Morton the chancellor used" (p. 377 of the 1877 ed.; p. 101 of 1622). Bacon does not name Fox in the passage.
- **Morton, as "the popular mind" has it (Stubbs 1883).** Stubbs states the dilemma as Morton's ("the dilemma by which he proved the necessity of the benevolences") and dates its application to the 1491 benevolence; the attribution is introduced with "to the popular mind".
- **Fox, on the earlier authority, possibly both (Fowler, DNB 1889).** "It is probably to 1504 that we may refer the story told of Foxe by Erasmus (Ecclesiastes, bk. ii. ed. Klein, ch. 150; cp. Holinshed, Chronicles), and communicated to him, as he says, by Sir Thomas More." The story: "Some came in splendid apparel and pleaded that their expenses left them nothing to spare; others came meanly clad, as evidence of their poverty. The bishop retorted on the first class that their dress showed their ability to pay; on the second that, if they dressed so meanly, they must be hoarding money, and therefore have something to spare for the king's service." Fowler's assessment: "It is possible that it may be true of both prelates, but the authority ascribing it to Foxe appears to be the earlier of the two. It is curious that Bacon speaks only of ‘a tradition’ of Morton's dilemma, whereas Erasmus professes to have heard the story of Foxe directly from Sir Thomas More, while still a young man, and, therefore, a junior contemporary of Foxe."
- **Neither as author; both as restrainers of the king (Archbold, DNB 1894).** Morton "has been traditionally known as the author of 'Morton's Fork' or 'Morton's Crutch,' but the truth seems rather to be that he and Richard Foxe [q. v.] did their best at the council to restrain Henry's avarice."
- **Fox (Pollard, EB 1911).** "Morton": "the ingenious method of extortion popularly known as “Morton’s fork” seems really to have been the invention of Richard Fox (q.v.), who succeeded to a large part of Morton’s influence." "Fox": "His financial work brought him a less enviable notoriety, though a curious freak of history has deprived him of the credit which is his due for “Morton’s fork.” The invention of that ingenious dilemma for extorting contributions from poor and rich alike is ascribed as a tradition to Morton by Bacon; but the story is told in greater detail of Fox by Erasmus, who says he had it from Sir Thomas More, a well-informed contemporary authority."
- **Morton (Oxford Dictionary of Phrase and Fable).** "Morton's Fork an argument used by the English prelate and statesman John Morton (c. 1420–1500), as Chancellor in demanding gifts for the royal treasury: if a man lived well he was obviously rich and if he lived frugally then he must have savings."
- **Fox as possible coiner of the phrase (Wikipedia, citing Chrimes).** "The phrase "Morton's fork" may have been coined by another of Henry's supporters, Richard Foxe." (rev. 1346281900, citing S. B. Chrimes, *Henry VII*, Yale University Press, ISBN 978-0-300-21294-5, p. 203; Chrimes not read for this page, ISBN checked at [Open Library](https://openlibrary.org/isbn/9780300212945)).

On the logical question, the one position on record in the sources read is
Wikipedia's label "a type of false dilemma" (list rev. 1376699902; article
rev. 1346281900). No source read argues the opposite or analyses the
argument further.

## Arguments in play

- **The fork itself**, in the two forms on record: Bacon's (sparing → "they laid up"; spenders → "seen in their port and manner of living"; conclusion "neither kind came amiss") and Erasmus's as Fowler reports it (splendid apparel → "ability to pay"; meanly clad → "hoarding money"). The propositional check above gives its form.
- **The argument from the earlier authority** (Fowler, DNB 1889): Erasmus heard the Fox story "directly from Sir Thomas More", whereas "Bacon speaks only of ‘a tradition’" — offered for preferring Fox, while allowing it "may be true of both prelates".

## Thinkers who addressed it

Chronological by date of the work read or reported.

- **Desiderius Erasmus**, *Ecclesiastes* bk. ii — the story told of Fox, from Thomas More (reported by Fowler, DNB 1889 and Pollard, EB 1911; not read for this page).
- **Francis Bacon** (1622), *Historie of the Raigne of King Henry the Seventh*, p. 101 — the "tradition of a dilemma" of Morton; names "fork" and "crotch".
- **William Stubbs** (lecture of 25 April 1883; printed in *Seventeen Lectures*, 1886) — Morton's fork applied to the 1491 benevolence.
- **Thomas Fowler** (DNB vol. 20, 1889, "Foxe, Richard") — the Erasmus story; the authority for Fox "appears to be the earlier".
- **William Arthur Jobson Archbold** (DNB vol. 39, 1894, "Morton, John") — Morton and Foxe tried "to restrain Henry's avarice".
- **A. F. Pollard** (EB 11th ed., 1911, "Morton, John" and "Fox, Richard") — the fork was Fox's invention.
- **S. B. Chrimes**, *Henry VII*, p. 203 — Fox as possible coiner of the phrase (as Wikipedia reports him; not read).

## Framings and reframings

- **From an episode to a name for a pattern.** The *Oxford Dictionary of Phrase and Fable*: "The phrase in this form dates from the mid 19th century, but Francis Bacon in his Historie of the Raigne of King Henry the Seventh (1622) says that, ‘There is a tradition of a dilemma that Bishop Morton…used to raise up the benevolence to higher rates; and some called it his Fork.’" Wikipedia generalises it: "A Morton's fork is a type of false dilemma in which contradictory observations lead to the same conclusion. Its name refers to the rationalising of a benevolence by the 15th century English prelate John Morton." (rev. 1346281900, lead).
- **As a "paradox" of decision theory.** The filing is Wikipedia's list's (section "Decision theory", rev. 1376699902) and the article's category "Decision-making paradoxes" (rev. 1346281900).
- **In card play.** Wikipedia: ""Morton's fork coup" is a manoeuvre in the game of bridge that uses the principle of Morton's fork." (rev. 1346281900, citing Frey et al. 1976, *The Official Encyclopedia of Bridge*, p. 295; not read).
- **Neighbouring names.** Wikipedia's "Morton's fork" lists Catch-22 and Hobson's choice under "See also" (rev. 1346281900), and "Catch-22 (logic)" lists Morton's fork among its own "See also" entries (rev. 1369910046; excerpt `raw/wikipedia-catch-22-logic-and-double-bind.md`); see [Catch-22 (logic)](catch-22-logic.md). Neither article states how the two differ.

## Vocabulary

- [Dilemma](../vocabulary/dilemma.md) — Bacon's and Stubbs's word; the argument-form sense, with the *false dilemma* charge kept apart as a charge against a premise.
- [Paradox](../vocabulary/paradox.md) — the List of paradoxes' filing label, not the historical sources'.
- **Benevolence** — the levy the fork served; Bacon: "This tax, called a benevolence" (1877 ed., p. 377), which he says was "now revived by the king, but with consent of parliament".
- **Fork / crotch / crutch** — Bacon gives "fork" and "crotch"; the DNB articles give "Morton's crutch".
