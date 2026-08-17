# SemPlan: Benchmarking Structured Semantic Planning for LLM-Based Queries over Enterprise Data

- arXiv ID: `2608.13612v1`
- Authors: Bruno Santos Teixeira
- Published: 2026-08-12
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.13612v1) | [pdf](https://arxiv.org/pdf/2608.13612v1)

## Abstract

Natural-language interfaces to enterprise data must translate underspecified requests into governed, executable behavior while controlling invalid queries, policy failures, cost, and nondeterminism. SemPlan Benchmark evaluates this architectural design space with a deterministic synthetic bilingual benchmark containing 1,800 cases in English and Brazilian Portuguese; 1,200 cases form the frozen scientific evaluation subset. Four architectures are compared under the same model configuration: direct SQL generation (A1), a bounded tool-agent baseline (A2), structured semantic-request generation followed by deterministic planning and execution (A3), and a clarification/stateful semantic-plan variant (A4). Across 4,800 primary records, answer correctness was low in absolute terms: 22.25% for A1, 22.58% for A2, 25.67% for A3, and 24.25% for A4. A3 had the highest observed correctness and significantly exceeded A1, A2, and A4 in the pre-specified paired correctness analysis, while A1 retained the highest policy-correct rate and the lowest unsafe-or-invalid rate. A4 had the lowest mean API cost and lowest false-refusal rate. On a preselected 150-case stability subset, answer-correct repeatability ranged from 92.00% to 98.67%. The results support a trade-off interpretation rather than a universal ranking: additional structural constraints changed failure modes and efficiency, but did not monotonically improve correctness or solve ambiguity and multi-turn state consistency.
