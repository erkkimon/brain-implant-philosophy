---
type: article
about: concept
title: The paradox of the court (Protagoras and Euathlus)
description: "Euathlus agrees to pay Protagoras the rest of his fee when he first wins a case; Protagoras sues, arguing he must be paid whether he wins or loses, and Euathlus turns the argument round. Gellius's account (Attic Nights V.10) and Diogenes Laertius IX.56, the convertible argument (antistrephon), the propositional form, and the proposed resolutions side by side: the jurors' postponement, the second suit, legal remedies, burden of proof, Slinin's reading."
tags: [problem, paradox, logic, dilemma, philosophy-of-law, ancient-philosophy]
timestamp: 2026-10-01T21:51:46Z
---

# The paradox of the court (Protagoras and Euathlus)

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md);
its two arguments are each a [dilemma](../vocabulary/dilemma.md).
Primary text: Aulus Gellius, *Attic Nights* V.10, tr. J. C. Rolfe, Loeb, 1927 (rev. 1946), pp. 405–409, public domain via [LacusCurtius](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Gellius/5*.html) (excerpt: `raw/gellius-attic-nights-5-10-protagoras-euathlus-rolfe.md`, which also holds Diogenes Laertius IX.56, tr. Hicks, via [Wikisource](https://en.wikisource.org/wiki/Lives_of_the_Eminent_Philosophers/Book_IX)).
Literature map: Peter Suber, *The Paradox of Self-Amendment* (Peter Lang, 1990), §20.A and notes 2–5, [Wayback snapshot](https://web.archive.org/web/20100817222844/http://www.earlham.edu/~peters/writing/psa/sec20.htm) (excerpt: `raw/suber-1990-paradox-of-self-amendment-protagoras-v-euathlus.md`).
Admitted from Wikipedia's List of paradoxes, revision 1376699902, "Logic" (excerpt: `raw/wikipedia-paradox-of-the-court-list-entry-and-article.md`).

## The question

Gellius's contract: "He paid half of the amount at once, before beginning his lessons, and agreed to pay the remaining half on the day when he first pleaded before jurors and won his case." (V.10.6).
Euathlus takes no cases; "Protagoras formed what seemed to him at the time a wily scheme; he determined to demand his pay according to the contract, and brought suit against Euathlus." (V.10.8).
Protagoras to the jurors: "For if the case goes against you, the money will be due me in accordance with the verdict, because I have won; but if the decision be in your favour, the money will be due me according to our contract, since you will have won a case." (V.10.10).
Euathlus in reply: "For if the jurors decide in my favour, according to their verdict nothing will be due you, because I have won; but if they give judgment against me, by the terms of our contract I shall owe you nothing, because I have not won a case." (V.10.14).
The question, as Smullyan puts it after giving both arguments, is "Who was right?" (*What Is the Name of This Book?*, 1978, no. 252; excerpt: `raw/smullyan-1978-what-is-the-name-of-this-book-252-protagoras-paradox.md`) — and, for a court, how the suit should be decided.
Wikipedia's list entry: "A law student agrees to pay his teacher after (and only after) winning his first case. The teacher then sues the student (who has not yet won a case) for payment." (rev. 1376699902).
The phrase "after (and only after)" in the list, and Lenzen's "if and only if" (below), are readings of the contract; Gellius's wording is "on the day when he first pleaded before jurors and won his case", which Suber calls "much less ambiguous than "when Euathlus won his first case"" (note 2).

**Propositional check (this implant, 2026-10-01; logic, not a position).**
Let *w* stand for *Euathlus wins this suit* and *p* for *Euathlus must pay*.
Protagoras's dilemma has the premises *~w -> p* (by the verdict) and *w -> p* (by the contract);
`logic.py check --premises "w -> p" "~w -> p" --conclusion "p"` outputs `VALID`.
Euathlus's counter-dilemma has *w -> ~p* (by the verdict) and *~w -> ~p* (by the contract);
`--premises "~w -> ~p" "w -> ~p" --conclusion "~p"` outputs `VALID`.
All four premises together against `"p & ~p"` output `VALID` and `premises are jointly inconsistent — argument is vacuously valid`.
The two verdict premises alone (`"w -> ~p" "~w -> p"` against `"p & ~p"`) output `INVALID` with counterexample rows `p=T, w=F` and `p=F, w=T`;
the two contract premises alone (`"w -> p" "~w -> ~p"`) output `INVALID` with rows `p=T, w=T` and `p=F, w=F`.
Each party's reading of the verdict agrees with the other's, and so does each party's reading of the contract; each dilemma mixes one verdict premise with one contract premise.
The tool treats *w* and *p* as timeless atoms; it does not model *before* and *after* the judgment, two different suits, or the difference between owing under a verdict and owing under a contract, on which the resolutions below turn.

## Why it matters

- **A named kind of argument.** Gellius uses the case to define the convertible argument: "On the arguments which by the Greeks are called ἀντιστρέφοντα, and in Latin may be termed reciproca." (V.10, chapter title); "The fallacy arises from the fact that the argument that is presented may be turned in the opposite direction and used against the one who has offered it, and is equally strong for both sides of the question. An example is the well-known argument which Protagoras, the keenest of all sophists, is said to have used against his pupil Euathlus." (V.10.3). His classification of it: "Among fallacious arguments the one which the Greeks call ἀντιστρέφων seems to be by far the most fallacious." (V.10.1; Gellius's assessment).
- **Reflexivity in law.** Suber treats it as "a classical illustration of the reflexive use of the "counter-dilemma" to respond to a "dilemma"." (§20.A), in a section on reflexive paradoxes in law, and reports that "State v. Jones, 80 Ohio App. 269 (1946) is the only American case that has cited Protagoras v. Euathlus, according to the computer search service, Lexis." (§20.B).
- **Self-annulling verdicts.** Gellius's jurors postpone "for fear that their decision, for whichever side it was rendered, might annul itself" (V.10.15).
- **A family of puzzles.** Smullyan calls it "a good prototype of a whole family of paradoxes." (no. 252, Discussion).
- **The sophists and rhetoric.** Gellius closes: "Thus a celebrated master of oratory was refuted by his youthful pupil with his own argument, and his cleverly devised sophism failed." (V.10.16). See [persuasion, rhetoric and dialectic](../vocabulary/persuasion-rhetoric-dialectic.md).

## Positions taken

No grouping of the resolutions was found in the sources read beyond Suber's
survey; they are listed by owner, unranked. Each line gives what the
resolution does with the premises of the check above.

| Resolution | Owner (source read) | What it says | Relation to the check above (structural note, this implant) |
|---|---|---|---|
| Postpone | the jurors in Gellius V.10.15 | "left the matter undecided and postponed the case to a distant day" | gives no verdict, so neither *w* nor *~w* is fixed |
| Postponement favours Euathlus | Suber 1990, §20.A | "By adjourning, the court in effect waits for Euathlus to take another case, which is equivalent to a judgment for Euathlus." | Suber's reading of the postponement |
| Euathlus wins the first suit, Protagoras a second | an unnamed lawyer reported by Smullyan 1978; per Suber, "Most commentators then observe that Protagoras could have sued a second time and won." | the court awards the first case to the student; then "Protagoras should then turn around and sue the student a second time" | dates the contract premise: Euathlus has not won before the first judgment, has won after it |
| Euathlus should win | "a small literature", per Suber | "all of it suggesting that Euathlus should have won" (§20.A) | — |
| The original judge held for Euathlus | Rinaldi 1965, as reported by Suber | "Rinaldi suggests (at p. 324) that the original Greek judge held for Euathlus." (note 2) | — |
| Remedies of law | Suber 1990, §20.A | "Many solutions are available to law that are unavailable to logic." | changes a premise: the contract, the advocate, or what counts as a first case |
| Burden of proof | Suber 1990, §20.A | "If the two arguments are truly equal in weight, then the one with the burden of proof loses; this works against the plaintiff Protagoras." | decides without choosing between the dilemmas |
| No antagonism; any decision but postponement | Slinin, as reported by Lisanyuk 2022 (abstract only) | the parties' "joint decision to go to court was aimed at helping Protagoras to get paid quickly, and Euathlus to pay off his teacher without losing face" | reframes the suit as cooperative |

Details, with the sources' own words:

- **The jurors (Gellius V.10.15).** "Then the jurors, thinking that the plea on both sides was uncertain and insoluble, for fear that their decision, for whichever side it was rendered, might annul itself, left the matter undecided and postponed the case to a distant day." Suber gives another version: "It is said that the court was so puzzled that it adjourned for 100 years." (§20.A).
- **Euathlus's escape route (Gellius V.10.11).** Euathlus himself names one: "I might have met this sophism of yours, tricky as it is, by not pleading my own cause but employing another as my advocate." Suber: "Euathlus would be better off hiring a lawyer because, if he won with a lawyer, his victory would be non-paradoxical, and if he lost with a lawyer, he would not yet have won his first case." (§20.A).
- **The second suit (Smullyan's lawyer).** "The best solution I ever got was from a lawyer to whom I posed the problem. He said: "The court should award the case to the student — the student shouldn't have to pay, since he hasn't yet won his first case. After the termination of the case, then the student owes money to Protagoras, so Protagoras should then turn around and sue the student a second time. This time, the court should award the case to Protagoras, since the student has now won his first case."" Smullyan's own stance: "Discussion. I'm not sure I really know the answer to this dilemma." (no. 252).
  *Against, per Suber:* "By bringing the first suit, even if he is certain to lose it, Protagoras guarantees his victory in the second suit. If equity wants to thwart Protagoras' scheme, then holding for Euathlus in the first case does not suffice; it plays into Protagoras' hands." (§20.A). Suber also reports a third suit: "A few observe that Euathlus might then sue for malicious prosecution, but they divide on who should win that suit." — "Lenzen, op. cit., thinks Euathlus should win the third suit. Schneider, op. cit. thinks he should lose it." (note 4).
- **Remedies of law (Suber §20.A).** "For example, the judge could thwart Protagoras' wily scheme by ordering Euathlus to hire a lawyer in the first case." "For example, the judge could easily decide that this case will not count as Euathlus's first case, except possibly in future cases looking back. Or the judge could decide that no "meeting of minds" occurred if Euathlus meant his first case with someone other than Protagoras and if Protagoras did not. The contract could be positively reformed in equity." "Euathlus could be ordered to pay earnest money while making a reasonable effort to take on another case, or to pay quantum meruit for the time Protagoras had already devoted to his instruction."
- **Slinin's reading and Lisanyuk's three judges (Lisanyuk 2022, abstract; [doi:10.52119/lphs.2022.65.71.014](https://doi.org/10.52119/lphs.2022.65.71.014); excerpt: `raw/lisanyuk-2022-protagoras-v-euathlus-slinin-abstract.md`).** "Slinin suggests that Euathlus was simply unlucky in courts, but there was no antagonism between Protagoras and Euathlus." The abstract: "We consider a thought experiment in which Plato, Aristotle and Slinin act as judges in this lawsuit, and show why Plato would postpone the case, Aristotle would satisfy the claim, and Slinin would be satisfied with any decision other than postponing the case, so he would side with Aristotle." The paper itself was not read.
- **Res judicata.** The brief for this page named *res judicata* as a legal reading of the second suit; no source read here applies the doctrine to this case, so it is not reported.

## Arguments in play

(none recorded as separate argument pages yet). The two dilemmas and the
propositional check are in The question; the second-suit argument and its
objection are in Positions taken.

## Thinkers who addressed it

- **Protagoras of Abdera** (fifth century BCE) — plaintiff and author of the first dilemma, in Gellius and in Diogenes Laertius IX.56: "“Nay,” said Protagoras, “if I win this case against you I must have the fee, for winning it; if you win, I must have it, because you win it.”" (Hicks tr.).
- **Euathlus** — the pupil; Bonazzi lists "Antimoerus of Mende, Carmidas and Euathlus of Athens, and Theodore of Cyrene" as Protagoras's pupils ([SEP Fall 2024 "Protagoras"](https://plato.stanford.edu/archives/fall2024/entries/protagoras/) §1.1; excerpt: `raw/sep-protagoras-fall-2024-trial-with-a-pupil.md`).
- **Aristotle** — per Diogenes IX.54, named Euathlus as Protagoras's accuser: "Aristotle, however, says it was Euathlus." Bonazzi reads the trial in that report as "a controversy with a pupil" and adds: "Moreover, it cannot be excluded that the trial with the student was also a fiction." (§1.1; Bonazzi's assessment).
- **Aulus Gellius** (*Attic Nights* V.10, 2nd c. CE) — the fullest account; classes it as ἀντιστρέφων and in V.11 asks whether Bias's argument on marriage is of the same kind: "Some think that the famous answer of the wise and noble Bias, like that of Protagoras of which I have just spoken, was ἀντιστρέφων." (V.11.1).
- **Diogenes Laertius** (*Lives* IX.56) — the shorter version, with Protagoras's dilemma only.
- **Fiori Rinaldi** ("Dilemmas and Circles in the Law", *Archiv für Rechts- und Sozialphilosophie* 51, 1965, 319–335) — per Suber, "says that Protagoras initiated the contract, not Euathlus" (note 2); not read.
- **E. Schneider** (*Logik für Juristen*, 1965), **Ilmar Tammelo** (*Outlines of Modern Legal Logic*, 1969), **John Bryant** (1976), **W. K. Goossens** ("Euathlus and Protagoras", *Logique et Analyse* 20, 1977, 67–75) — listed by Suber (note 3); not read.
- **Wolfgang Lenzen** ("Protagoras versus Euathlus: Reflections on a So-Called Paradox", *Ratio* 19, Dec. 1977, 176–80, per Suber note 2; no DOI found, bibliographic data from Suber only) — per Suber, "says that Euathlus contracted to pay "if and only if" he wins his first legal case", and "Although Lenzen's source of the paradox is J.L. Mackie, Truth, Probability and Paradox, Oxford University Press, 1973, p. 296, Mackie uses "when", not "if and only if"." Not read.
- **Raymond Smullyan** (1978, no. 252) — reports the second-suit answer.
- **Lennart Åqvist** ("The Protagoras Case: An Exercise in Elementary Logic for Lawyers", in W. Rabinowicz (ed.), *Tankar Och Tankefel*, Uppsala, 1981, pp. 211–24, per Suber note 3; not read). Wikipedia's article lists his "Deontic Logic", *Handbook of Philosophical Logic* II, 1984, pp. 605–714 ([doi:10.1007/978-94-009-6259-0_11](https://doi.org/10.1007/978-94-009-6259-0_11)); not read.
- **Peter Suber** (1990) — legal analysis and literature survey above.
- **Yaroslav Slinin** and **Elena Lisanyuk** (2022) — above, from the abstract.
- **Park Hyun Seok**, *The Protagoras v. Euathlus Case : a Thread of Law to the Labyrinth of Logic* (title as registered with Crossref), *Journal of Hongik Law Review* 14, 2013, pp. 247–272 ([doi:10.16960/jhlr.14.2.201306.247](https://doi.org/10.16960/jhlr.14.2.201306.247)) — bibliographic only.

## Framings and reframings

- **Convertible argument (Gellius).** An argument that "may be turned in the opposite direction and used against the one who has offered it" (V.10.3); see the check above for the two dilemmas side by side.
- **Dilemma and counter-dilemma (Suber).** "the reflexive use of the "counter-dilemma" to respond to a "dilemma"" (§20.A). Wikipedia's article gives the name "counterdilemma of Euathlus" (rev. 1342345476).
- **A puzzle about time (structural note, this implant).** The second-suit answer and Lenzen's "if and only if" both concern what the contract condition means; the check above shows that a single timeless *w* makes the four premises inconsistent, while the second-suit answer evaluates the contract premise at two different times.
- **A question of legal remedy, not logic (Suber).** "Many solutions are available to law that are unavailable to logic." (§20.A).
- **A motive behind the suit (Suber, note 5).** "The only other wily scheme that occurs to me is a design to make vivid a proposition for which he was famous and, indeed, that brought him pupils and income."
- **Kin cases.** Wikipedia files it beside the [crocodile dilemma](crocodile-dilemma.md) in the same "Logic" list; [Buridan's bridge](buridans-bridge.md) is another case in which a conditional promise and the act it governs bear on each other. No source read here compares them with this case; the pairing is the list's placement, not a sourced claim of kinship.

Left out until read: Lenzen 1977, Åqvist 1981 and 1984, Goossens 1977,
Rinaldi 1965, Schneider 1965, Tammelo 1969, Bryant 1976, Mackie 1973,
Park 2013, the body of Lisanyuk 2022, Northrop's *Riddles in Mathematics*,
Hughes & Lavery 2008, and any source on *res judicata* applied to this case.

## Vocabulary

- [Dilemma](../vocabulary/dilemma.md) — each party's argument; Smullyan calls the case "this dilemma".
- [Paradox](../vocabulary/paradox.md) — see The question.
- [Validity](../vocabulary/validity.md) — each dilemma checks `VALID`; the premises of both together are jointly inconsistent.
- Gellius (V.10.1) classifies the convertible argument as a [fallacy](../vocabulary/fallacy.md).
- [Argument](../vocabulary/argument.md) and [persuasion, rhetoric and dialectic](../vocabulary/persuasion-rhetoric-dialectic.md) — the setting, a suit between a teacher of oratory and his pupil.
- [Classical logic](../methods/classical-logic.md) — the propositional check.
- *Antistrephon (ἀντιστρέφων, reciproca)*, *counter-dilemma*, *res judicata*, *quantum meruit*, *burden of proof* — open work in [vocabulary](../vocabulary/index.md).
