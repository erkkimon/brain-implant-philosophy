# Bender & Koller 2020 — form versus meaning and the octopus test

Source: Emily M. Bender & Alexander Koller (2020), "Climbing towards NLU:
  On Meaning, Form, and Understanding in the Age of Data", Proceedings of
  the 58th Annual Meeting of the Association for Computational
  Linguistics (ACL 2020), pp. 5185–5198; abstract, §1, §3 "What is
  meaning?", §4 "The octopus test".
Original: https://doi.org/10.18653/v1/2020.acl-main.463
  (CC BY 4.0 — ACL Anthology; excerpts only)
Retrieved: 2026-09-25 (DOI verified via Crossref; PDF read at
  https://aclanthology.org/2020.acl-main.463.pdf)

> "In this position paper, we argue that a system trained only on form has
>  a priori no way to learn meaning."  (Abstract, p. 5185)

> "We argue that the language modeling task, because it only uses form as
>  training data, cannot in principle lead to learning of meaning. We take
>  the term language model to refer to any system trained only on the task
>  of string prediction, whether it operates over characters, words or
>  sentences, and sequentially or not. We take (linguistic) meaning to be
>  the relation between a linguistic form and communicative intent."
>  (§1, p. 5185)

> "We take form to be any observable realization of language: marks on a
>  page, pixels or bytes in a digital representation of text, or movements
>  of the articulators. We take meaning to be the relation between the
>  form and something external to language"  (§3, pp. 5185–5186)

The octopus test:

> "Say that A and B, both fluent speakers of English, are independently
>  stranded on two uninhabited islands. [...] Meanwhile, O, a
>  hyper-intelligent deep-sea octopus who is unable to visit or observe
>  the two islands, discovers a way to tap into the underwater cable and
>  listen in on A and B's conversations. O knows nothing about English
>  initially, but is very good at detecting statistical patterns."  (§4,
>  p. 5188)

> "Finally, A faces an emergency. She is suddenly pursued by an angry bear.
>  She grabs a couple of sticks and frantically asks B to come up with a
>  way to construct a weapon to defend herself. Of course, O has no idea
>  what A 'means'. [...] Having only form available as training data, O
>  did not learn meaning."  (§4, p. 5188)

Relied on for: the definitions of "form" and "meaning" on which the
in-principle argument turns; the octopus thought experiment; that the
paper's claim is about *understanding/meaning*, not consciousness — it
does not mention consciousness or sentience.
Context: the paper concedes in §4 that "It is not that O's utterances
make sense, but rather, that A can make sense of them," and in §5–6
offers Java and child-language-acquisition variants; §7 discusses
distributional semantics and grounding. It predates ChatGPT (models
discussed are BERT and GPT-2) and is a "position paper" that the authors
say aims "to advocate for an alignment of claims and methodology". The
octopus is often retold as a claim that LLMs are not conscious; the text
argues only that they cannot learn the form–intent relation from text
alone.
