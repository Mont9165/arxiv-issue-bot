# FASE: Fast Adaptive Semantic Entropy for Code Quality

- arXiv ID: `2606.09800v1`
- Authors: Shizhe Lin, Ladan Tahvildari
- Published: 2026-06-08
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.MA`
- Links: [abs](http://arxiv.org/abs/2606.09800v1) | [pdf](https://arxiv.org/pdf/2606.09800v1)

## Abstract

Multi-agent code generation offers a promising paradigm for autonomous software development by simulating the human software engineering lifecycle. However, system reliability remains hindered by LLM hallucinations and error propagation across interacting agents. While semantic entropy provides a principled way to quantify uncertainty without ground-truth answers, current methods often rely on costly LLM-driven equivalence checks. In this work, we introduce Fast Adaptive Semantic Entropy (FASE), a novel metric that approximates functional correctness based on the minimum spanning tree of structural and semantic dissimilarity graphs. Evaluations on HumanEval and BigCodeBench demonstrate that FASE outperforms state-of-the-art semantic entropy by LLM entailment, achieving a 25% average improvement in Spearman correlation and a 19% increase in ROCAUC score against Pass@1 from ground-truth test cases when using the Qwen3-Embedding-8B model. Furthermore, by eliminating costly LLM-driven equivalence evaluation, FASE incurs negligible computational overhead, requiring only approximately 0.3% of the runtime cost of traditional semantic entropy approaches. These results position FASE as a practical, cost-effective solution for optimizing uncertainty quantification in real-world multi-agent workflows.
