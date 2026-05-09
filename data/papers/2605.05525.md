# Anatomy of a Query: W5H Dimensions and FAR Patterns for Text-to-SQL Evaluation

- arXiv ID: `2605.05525v1`
- Authors: Vicki Stover Hertzberg, Eduardo Valverde, Joyce C. Ho
- Published: 2026-05-07
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2605.05525v1) | [pdf](https://arxiv.org/pdf/2605.05525v1)

## Abstract

Natural language interfaces to databases have gained popularity, yet the theoretical foundations for evaluating and designing these systems remain underdeveloped. We present QUEST (Query Understanding Evaluation through Semantic Translation), a framework resting on two independently motivated components: the FAR structural invariant, which holds that every well-formed query reduces to Filter, Aggregate, and Return operations; and the W5H dimensional framework, which holds that all filtering criteria map to six semantic dimensions (Who, What, Where, When, Why, and How). Validated across five text-to-SQL datasets (n = 120,464), FAR conformance is universal across all domains and schema types, while W5H dimensional profiles vary substantially. Healthcare queries are strongly concentrated in temporal (WHEN: 80.4%) and person-centric (WHO: 73.0%) dimensions far exceeding general-domain benchmarks, and causal (WHY) and mechanistic (HOW) reasoning are near-zero everywhere, with apparent HOW exceptions reflecting quantitative aggregation rather than genuine procedural reasoning. These results identify a frontier that must be crossed for genuine machine reasoning over structured data.
