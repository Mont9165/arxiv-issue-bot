# DSEffi-Bench: Demystifying Large Language Models' Capability in Efficient Data Science Code Generation

- arXiv ID: `2608.30248v1`
- Authors: Zhihao Gong, Junzhe Yu, Dong Huang, Zeyu Sun, Jie M. Zhang, Dan Hao
- Published: 2026-08-31
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.30248v1) | [pdf](https://arxiv.org/pdf/2608.30248v1)

## Abstract

Current data science (DS) code generation benchmarks equate correctness with quality, overlooking execution time differences that span orders of magnitude between correct solutions. We introduce DSEffi-Bench, the first benchmark specifically targeting execution efficiency in LLM-generated DS code, comprising 1,000 instances across 10+ DS libraries with stress-testing harnesses and human-validated references. Evaluating 16 models across 3 tiers, we find that correctness alone fails to characterize efficiency: GPT-5.4 leads in correctness (Pass, 66.9\%) but its efficiency score (B$|$P, 71.7\%) nearly matches GPT-5.4-mini (71.6\%), which solves 47 fewer tasks; Kimi-K2.5 ranks lowest in correctness among frontier models (40.2\%) yet achieves the highest efficiency score (73.6\%) across all 16 models. A human-annotated five-category taxonomy reveals that 79.1\% of efficiency deficits extend beyond algorithmic complexity to domain-specific root causes, with distinct failure profiles across model tiers and libraries. Two exploratory experiments provide initial evidence that these diagnostics can guide improvement, yielding up to +14.7\% efficiency gains via taxonomy-guided optimization and approaching Claude-Opus-4.6 Best@3 in efficiency at 13.0$\times$ lower cost via library-conditioned routing.
