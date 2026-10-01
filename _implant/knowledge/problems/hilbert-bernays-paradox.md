---
type: article
about: concept
title: "The Hilbert–Bernays paradox"
description: "A term that denotes 'the successor of the denotation of this term' seems to force some number to equal its successor — the paradox of denotation in Hilbert and Bernays' Grundlagen der Mathematik II (1939), which they took to show a consistent arithmetic cannot represent its own denotation function; Priest (1997, 2005, 2006) on its distinctive difficulties for non-classical solutions, and Read's (2019) Bradwardinian reply."
tags: [problem, paradox, logic, self-reference, denotation, philosophy-of-mathematics]
timestamp: 2026-10-01T22:52:16Z
---

# The Hilbert–Bernays paradox

Written under [Reporting, not endorsing](../../conventions/reporting-not-endorsing.md);
evidence levels per [How claims are graded](../../conventions/how-claims-are-graded.md).
One of the [problems](./index.md) filed as a [paradox](../vocabulary/paradox.md).
Primary text: Hilbert and Bernays, *Grundlagen der Mathematik* II (Springer,
1939; 2nd ed. [doi:10.1007/978-3-642-86896-2](https://doi.org/10.1007/978-3-642-86896-2)),
pp. 262–268 (1st ed.) / 271–277 (2nd ed.) per Dean — not read; reported
here through the secondary sources below (records:
`raw/hilbert-bernays-paradox-bibliographic-records.md`).
Sources read: Read, "Denotation, Paradox and Multiple Meanings" (2019,
[doi:10.1007/978-3-030-25365-3_20](https://doi.org/10.1007/978-3-030-25365-3_20),
author's [preprint](https://www.st-andrews.ac.uk/~slr/Denotation_Paradox.pdf) §6;
excerpt: `raw/read-2019-denotation-paradox-hilbert-bernays.md`); Dean,
"Incompleteness via Paradox and Completeness" (*Review of Symbolic Logic* 13(3),
[doi:10.1017/S1755020319000212](https://doi.org/10.1017/S1755020319000212),
[accepted manuscript](http://wrap.warwick.ac.uk/117760) §2 and n. 10; excerpt:
`raw/dean-2019-hilbert-bernays-denotation-function-paradox.md`); Wikipedia,
["Hilbert–Bernays paradox", revision 1339045069](https://en.wikipedia.org/w/index.php?title=Hilbert%E2%80%93Bernays_paradox&oldid=1339045069).
Admitted from Wikipedia's [List of paradoxes, revision 1376699902](https://en.wikipedia.org/w/index.php?title=List_of_paradoxes&oldid=1376699902),
"Logic" (both: `raw/wikipedia-hilbert-bernays-paradox-rev-1339045069-and-list-entry.md`).
Priest, "On a Paradox of Hilbert and Bernays", *Journal of Philosophical Logic*
26(1), 1997, pp. 45–56, [doi:10.1023/A:1017900703234](https://doi.org/10.1023/A:1017900703234),
was verified bibliographically only; what it says is reported as Read reports it.

## The question

Read (2019, §6) states it as a definite description: "Consider the definite description, ‘the successor of the denotation of this description’. Given that no number is its own successor, it seems that this description cannot possibly denote. For if it denoted some number n, then it would also denote n + 1. Given that the denotation of definite descriptions is unique (if it exists), it follows that n = n + 1. Contradiction. The only possible solutions seem to be that the description does not denote, or denotes more than one thing."

The Wikipedia list (rev. 1376699902): "Hilbert–Bernays paradox: If there was a name for a natural number that is identical to a name of the successor of that number, there would be a natural number equal to its successor."
The Wikipedia article (rev. 1339045069) runs it from a reference
schema, "(R) If a exists, the referent of the name ′a′ is identical with a",
and a self-naming term, "(H) <h> is identical with ′(the referent of <h>)+1′";
from "(1) The referent of <h> is identical with n" it reaches
"(3) The referent of h is identical with (the referent of h)+1" and
"(4) n is identical with n+1", adding: "But (4) is absurd, since no number is identical with its successor."

In Hilbert and Bernays' setting, per Dean (§2), the assumption is "that there exists a definable denotation function d(x) which provably satisfies" d of the code of t equals t for every closed term t; "Hilbert & Bernays denote this function with the symbol e(x) rather than d(x)." (n. 10).

The term contracts are [paradox](../vocabulary/paradox.md) and
[validity](../vocabulary/validity.md).

**Logic check (this implant, 2026-10-02; logic, not a position).** Let `d` =
*the description denotes a number*, `s` = *some number equals its successor*.
Read's reasoning gives `d -> s`; arithmetic gives `~s`.
`logic.py check --premises "d -> s" "~s" --conclusion "~d"` outputs "VALID"
and "matches schema: modus tollens"; with the added premise `d` and
conclusion `s` it outputs "premises are jointly inconsistent — argument is vacuously valid".
With conclusion `d` it outputs "INVALID" (counterexample "d=F, s=F").
The tool does not model "denotes more than one thing" or a logic other than
the classical one it runs; the positions below differ on exactly that.

## Why it matters

- **A limit on formal arithmetic.** Read (§6) reports: "Hilbert and Bernays’ response is to conclude that the denotation function is not arithmetic, and so cannot be represented in arithmetic (if arithmetic is consistent), any more than arithmetic truth can, as recorded in Tarski’s Theorem." (citing Hilbert and Bernays 1939, pp. 268–9). The Wikipedia article: the paradox "is used by them to show that a sufficiently strong consistent theory cannot contain its own reference functor."
- **Natural language.** Read reports Priest's 1997 point: "Priest [1997a, p. 47] observes, however, that, sound as this conclusion may be for formal arithmetic, it still leaves open the paradox in natural language, just as Tarski’s Theorem cuts no ice with the Liar paradox."
- **Any function, not only successor.** "Priest [2006b, p. 147] also observes that mention of successor in the above paradox is only one special case." (Read §6), so that "One can develop the paradox for any number-theoretic function, f : N → N, and show formally that any such function has a fixed point—though many functions, such as successor, clearly do not."
- **A test for uniform solutions.** The Wikipedia article says the paradox "has recently been rediscovered and appreciated for the distinctive difficulties it presents" (citing Priest 2005, pp. 156–178); Read (§6) writes that "The paradox does not seem readily to fit his common Inclosure schema." — Priest's — and "If this is right, by the Principle of Uniform Solution the Hilbert-Bernays paradox is different in kind from the other paradoxes, of denotation and of truth."

## Positions taken

Not ranked; each is reported with the source that records it.

- **No arithmetical denotation function (Hilbert and Bernays 1939).** As reported by Read (§6, pp. 268–9 of the Grundlagen) and quoted under Why it matters. Dean (n. 10): "as Hilbert & Bernays themselves observe, the underlying argument is similar to their prior demonstration (1934, p. 330/335) that the denotation function for primitive recursive terms cannot itself be primitive recursive."
- **The description denotes more than one thing (Priest 2005).** "Priest [2005, §§8.5-8.6] explores the latter possibility, that the description ‘the successor of the denotation of this description’ denotes more than one thing, namely, both what it denotes and its successor." (Read §6); "Priest [2005, §8.7] avoids the consequence that some number is its own successor, from which it would follow that 0 = 1, by denying the substitutivity of identicals." (n. 30). The Wikipedia article files this with solutions "that reject the law of noncontradiction (which is likewise not used by the Hilbert–Bernays paradox)", which "have claimed that h refers to more than one object." Read reports that Priest's solutions in 2005 and 2006 "differ from his dialetheic solution to the other paradoxes".
- **The description does not denote (Field 2008, as the article reports).** Solutions "that reject the law of excluded middle (which is not used by the Hilbert–Bernays paradox) have denied that there is such a thing as the referent of h" (Wikipedia, citing Field, *Saving Truth from Paradox*, 2008, pp. 291–293; not read). Read reports Priest's argument against this option: "But the other option, that the description does not denote, is not open to us either, as Priest shows." (citing Priest 1997, §7; 2005, §8.4; 2006, §6).
- **Restrict naive reference, as for the liar (Simmons 2003, as the article reports).** "On the first approach, typically whatever one says about the Liar paradox carries over smoothly to the Hilbert–Bernays paradox." (Wikipedia, citing Simmons, "Reference and Paradox", in *Liars and Heaps*, 2003, pp. 230–252; not read). The article frames the choice as "either by rejecting the principle of naive reference (R) or by rejecting classical logic".
- **It denotes the contradictory object (Read 2019).** Read adapts Thomas Bradwardine's "multiple-meanings" account: "we can already see that the description at the heart of the paradox is inherently contradictory, and so likely to submit to the standard Bradwardinian solution." and concludes: "Consequently, since, as we saw, every description denotes, ‘σ’ must denote something, namely, ιx⊥." Read states his commitments: "I remain firmly committed to the law of Contravalence (that nothing can be both true and false) as much as to the laws of Non-Contradiction and Excluded Middle."

**Cases for and against.** Recorded only as the sources above report them:
Priest against the non-denoting option (as Read reports, details in Priest
1997 §7, not read); Read's note that Priest's 2005 option "not only runs counter to the natural presumption in the theory of singular terms that their" denotation is unique; and the Wikipedia article's
claim that both non-classical options face "distinctive difficulties". No
objection to Read's or to Hilbert and Bernays' conclusion was found in the
sources read; none is recorded here. No survey figure is recorded.

## Arguments in play

(none as separate argument pages yet). Related problems:
[the liar paradox](liar-paradox.md), which the Wikipedia article's two-way
division of solutions starts from; [the Berry paradox](berry-paradox.md),
which Read lists with it among "the paradoxes of denotation, such as Berry’s, König’s and Richard’s" (abstract) and treats by the same principles (§7);
[Richard's paradox](richards-paradox.md), which Dean (§2) says Hilbert and
Bernays liken it to; [Russell's paradox](russells-paradox.md) and
[Curry's paradox](currys-paradox.md), other self-reference items of the
same list.

## Thinkers who addressed it

- **David Hilbert** and **Paul Bernays** — *Grundlagen der Mathematik* II (1939), pp. 262–268 / 271–277 per Dean; they "ultimately group these paradoxes together as semantische" (Dean §2).
- **Hao Wang** (1955) — per Dean (n. 10), "later showed how this result can be transformed into an incompleteness theorem".
- **[Graham Priest](../thinkers/priest.md)** — "On a Paradox of Hilbert and Bernays" (1997); *Towards Non-Being* (2005), ch. 8; "The paradoxes of denotation", in *Self-Reference* (CSLI 2006), pp. 137–50 (all per Read's references; not read). Read: "Priest [2005, §8.3] reminds us of a paradox due to Hilbert and Bernays".
- **Keith Simmons** (2003) and **Hartry Field** (2008) — cited by the Wikipedia article; not read.
- **Stephen Read** (2019; manuscript 2016 per Dean) — Bradwardinian solution.
- **Walter Dean** (2019) — places it in Hilbert and Bernays' treatment of the paradoxes and incompleteness.

## Framings and reframings

- **A sui generis antinomy, or a diagonal argument.** Dean (n. 10): "Subsequent authors (e.g. Priest, 1997a; Read, 2016) have tended to view the inconsistency resulting from the assumption that such a function is definable as a sui generis antinomy – the so-called denotational paradox." Dean contrasts this with Hilbert and Bernays' own comparison to a diagonal proof (quoted under Positions).
- **A paradox of reference.** The Wikipedia article: "The Hilbert–Bernays paradox is a distinctive paradox belonging to the family of the paradoxes of reference."
- **Does anything satisfy (1)?** A Wikipedia editor's clarify tag (May 2015) on the article's Solutions section asks: "Why should (1) be true, i.e. why should a number exist that satisfies the property h? For example, no natural number is designated by the name 'The number whose square is 2', but this isn't called a paradox." Read (§6) reports Priest's argument that taking a description "to denote even when there is no unique φ" can be forced (Priest 1997 §7).
- **Paradox to incompleteness.** Dean (n. 10) reports Wang 1955 using "the Arithmetized Completeness Theorem" on the denotation function for arithmetical terms.

## Vocabulary

- [Paradox](../vocabulary/paradox.md); [Validity](../vocabulary/validity.md);
  [Classical logic](../methods/classical-logic.md), in which the logic check
  above is run.
- Denotation, definite description, denotation function, diagonal lemma,
  fixed point, substitutivity of identicals, Principle of Uniform Solution,
  Inclosure schema — open work in [vocabulary](../vocabulary/index.md).
