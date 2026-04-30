# ClassEval-Pro: A Cross-Domain Benchmark for Class-Level Code Generation

- arXiv ID: `2604.26923v1`
- Authors: Yeheng Chen, Chaoxiang Xie, Yuling Shi, Wenhao Zeng, Yongpan Wang, Hongyu Zhang, Xiaodong Gu
- Published: 2026-04-29
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2604.26923v1) | [pdf](https://arxiv.org/pdf/2604.26923v1)

## Abstract

LLMs have achieved strong results on both function-level code synthesis and repository-level code modification, yet a capability that falls between these two extremes -- compositional code creation, i.e., building a complete, internally structured class from a specification -- remains underserved. Current evaluations are either confined to isolated functions or rely on manually curated class-level tasks that are expensive to scale and increasingly susceptible to data contamination. We introduce ClassEval-Pro, a benchmark of 300 class-level tasks spanning 11 domains, constructed through an automated three-stage pipeline that combines complexity enhancement, cross-domain class composition, and integration of real-world GitHub code contributed after January 2025. Every task is validated by an LLM Judge Ensemble and must pass test suites with over 90% line coverage. We evaluate five frontier LLMs under five generation strategies. The best model achieves only 45.6% class-level Pass@1, with a 17.7-point gap between the strongest and weakest models, confirming the benchmark's discriminative power. Strategy choice strongly interacts with model capability: structured approaches such as bottom-up improve weaker models by up to 9.4 percentage points, while compositional generation collapses to as low as 1.3%. Error analysis over 500 manually annotated failures reveals that logic errors (56.2%) and dependency errors (38.0%) dominate, identifying cross-method coordination as the core bottleneck.
