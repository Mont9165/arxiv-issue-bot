# POSTCONDBENCH: Benchmarking Correctness and Completeness in Formal Postcondition Inference

- arXiv ID: `2605.03356v1`
- Authors: Gehao Zhang, Juan Zhai
- Published: 2026-05-05
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.03356v1) | [pdf](https://arxiv.org/pdf/2605.03356v1)

## Abstract

Formal postconditions precisely characterize program behavior and support debugging, testing, and verification, but writing them requires substantial expertise and effort. This has motivated recent work on automatically generating postconditions from code and natural-language artifacts using large language models (LLMs). However, evaluation remains a key bottleneck. Existing benchmarks primarily emphasize correctness under limited evaluation settings, often relying on surface-form matching or manual assessment on small or synthetic datasets.
  We introduce POSTCONDBENCH, a multilingual benchmark for evaluating method-level postcondition generation from real-world software. POSTCONDBENCH comprises 420 Python and Java tasks drawn from 121 open-source projects, each paired with a high-quality ground-truth postcondition set constructed with expert involvement. To enable automatic evaluation, POSTCONDBENCH provides a runnable execution environment and operationalizes completeness via defect discrimination: a postcondition set is more complete if it is violated by more defective implementations while remaining satisfied on correct executions. Using POSTCONDBENCH, we formulate three generation settings and evaluate five SOTA LLMs. Our results reveal a substantial gap between correctness and completeness, and show that repository-level dependencies and method complexity exacerbate this gap.
