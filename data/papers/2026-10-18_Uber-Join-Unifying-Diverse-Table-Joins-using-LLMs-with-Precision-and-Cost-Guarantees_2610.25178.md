# Uber-Join: Unifying Diverse Table Joins using LLMs with Precision and Cost Guarantees

- arXiv ID: `2610.25178v1`
- Authors: Guohui Guan, Chang Ge, Yeye He
- Published: 2026-10-18
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.25178v1) | [pdf](https://arxiv.org/pdf/2610.25178v1)

## Abstract

When two tables from different sources are joined, the values that should join often differ in spelling, format, or meaning, and fuzzy-, transformation-, and semantic-joins each handle one type of these differences. Large language models (LLMs) can match values that differ in several ways at once, but every LLM call is billed, and having an LLM compare the rows of two large tables can cost far more than a typical budget allows. This paper studies how to combine these join types with LLMs to join two tables under a dollar budget, maximizing recall while keeping the precision of the result at or above a target, a problem that is NP-hard.
  Our key idea is to use LLMs selectively to create join programs and verify their outputs through sampling, while adaptively deciding which joins to pursue under budget and precision constraints. This combines the scalability of program-based joins with selective LLM verification, while maintaining a statistical precision guarantee on the accumulated result. We develop Uber-Join, which treats creating a join and checking the output of a created join as two levels of arms in a budgeted multi-armed bandit. It commits an output only if the precision of the whole result, estimated from an LLM's judgments of sampled pairs, stays at or above the target with high confidence. Under the same budget, Uber-Join achieves the highest recall at the precision target in nearly all settings on three join benchmarks and Join-Hard, a new benchmark of large tables.
