# TL;QR: Querying Temporal Discursive Patterns in Textual Corpora

- arXiv ID: `2610.15712v1`
- Authors: François Hublet, Vladimir Krsmanovic, Jesus Solano, Ahmed Bouhoula, Ana Oliveira da Costa
- Published: 2026-10-11
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.CY`, `cs.DB`, `cs.LO`
- Links: [abs](http://arxiv.org/abs/2610.15712v1) | [pdf](https://arxiv.org/pdf/2610.15712v1)

## Abstract

Many questions about large textual corpora concern patterns that unfold over time, such as a political group whose stance on a topic drifts from support to criticism over several years of debates. We present TL;QR (Too Long; Query with logical temporal Reasoning), a declarative query language and open-source engine for finding such temporal discursive patterns. In TL;QR, a single query combines natural-language predicates, whose truth is judged by a Large Language Model (LLM), with regular expressions and the operators of a temporal logic. The LLM answers only local questions about individual text passages; a symbolic engine then aggregates these judgments over time and links every match to the recorded passages and predicate decisions behind it. With this division of labor, the temporal and relational reasoning stays exact and auditable even over long time horizons. In addition, when a query includes a regular-expression pre-filter, only a small fraction of the corpus ever reaches the LLM. On a suite of controlled synthetic benchmarks with temporally and semantically complex patterns, TL;QR is substantially more accurate than LLM-only baselines. In a case study on ten years of European Parliament debates (442,593 multilingual speeches), TL;QR identifies candidate shifts in the political groups' stances on the GDPR privacy regulation.
