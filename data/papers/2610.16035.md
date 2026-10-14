# SemReuse: Certified Reuse of Cached Natural-Language Views for Semantic Operators

- arXiv ID: `2610.16035v1`
- Authors: Phat T. Tran-Truong, Tung Kieu, Xuan-Bach Le, Son X. Ha, Duc Kieu, Bin Yang, Christian S. Jensen
- Published: 2026-10-12
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.16035v1) | [pdf](https://arxiv.org/pdf/2610.16035v1)

## Abstract

Semantic operators allow users to filter unstructured data using conditions expressed in natural language, but existing systems typically invoke an LLM for every input tuple. Analytical workloads often contain repeated or related filters whose results could be reused. Such reuse is risky because it requires inferring whether filter conditions are equivalent, whether one implies another, or whether they are mutually exclusive. An incorrect judgment can omit qualifying tuples or include nonqualifying ones. We introduce SemReuse, a system for safely reusing previous semantic-filter results. SemReuse stores each result as a materialized view and compares new filters with existing views to identify tuples that can provisionally be accepted or skipped without another LLM call. Because these decisions rely on a fallible language reasoner, SemReuse audits every rewritten result. Its pooled stratified audit uses exact finite-population bounds to provide jointly valid per-query recall and precision guarantees. If the requested guarantees cannot be established, SemReuse evaluates additional tuples and progressively approaches full evaluation. Thus, incorrect relation judgments affect efficiency rather than the validity of the reported guarantees. Experiments on large labeled corpora and real LLM executions show reductions of up to 15.4x. They also identify cross-filter inconsistency as the main source of repair cost.
