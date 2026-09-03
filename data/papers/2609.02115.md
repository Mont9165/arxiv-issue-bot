# text2ql: Multi-Target Natural Language Querying via a Language-Agnostic Intermediate Representation

- arXiv ID: `2609.02115v1`
- Authors: Ritesh Kumar
- Published: 2026-09-02
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2609.02115v1) | [pdf](https://arxiv.org/pdf/2609.02115v1)

## Abstract

Natural language interfaces to databases have traditionally suffered from three structural limitations: exclusive targeting of relational SQL, unconditional dependence on large language model (LLM) inference at query time, and absence of any runtime signal when generated queries are semantically incorrect. This paper presents text2ql, an open-source Python framework that addresses all three limitations through a language-agnostic Intermediate Representation (QueryIR) and a pluggable renderer architecture. A single seven-stage detection pipeline serves both SQL and GraphQL targets; a zero-LLM deterministic mode delivers 100% execution accuracy at a median latency of 3.2 ms with no API cost; and every generated query carries a runtime confidence score in [0.15, 0.97] computed from an additive signal model. Evaluated on 50-query random samples from the Spider and BIRD benchmarks (indicative results; full-set evaluation is planned), the LLM-backed mode achieves 62-70% exact match and 84-91% execution accuracy; the deterministic mode achieves 100% execution accuracy with zero parse errors across all 100 test cases. An ablation study isolates schema-aware prompting as the dominant accuracy lever, contributing +18.4 percentage points of exact-match gain over the schema-free baseline on both benchmarks. text2ql is publicly available at https://pypi.org/project/text2ql/ under the Apache 2.0 license.
