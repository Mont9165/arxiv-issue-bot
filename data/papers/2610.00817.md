# TabJoinBench: A Benchmark for Joinable Table Discovery

- arXiv ID: `2610.00817v1`
- Authors: Sandipan De, Jin Wang, Vivek Gupta
- Published: 2026-09-30
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`, `cs.CL`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2610.00817v1) | [pdf](https://arxiv.org/pdf/2610.00817v1)

## Abstract

Join discovery aims to identify tables from large data repositories that can augment a query table with complementary information, enabling downstream tasks such as data exploration, feature engineering, and business intelligence. Although numerous join discovery methods have been proposed, existing studies rely on method-specific benchmark construction, making reproducible and fair comparison difficult. We present TabJoinBench, a benchmark for evaluating join discovery methods across semantic, relational, and hybrid data lake scenarios. TabJoinBench constructs query-candidate pairs using source-specific validation strategies, systematically introduces structural, representation, and semantic changes through composable perturbations while preserving reliable ground truth. We evaluate representative join discovery methods spanning set-based, feature-based, and learned approaches, together with general-purpose language-model embedding baselines, and publicly release the processed datasets, ground-truth annotations, and generation pipeline to facilitate reproducible evaluation and future research.
