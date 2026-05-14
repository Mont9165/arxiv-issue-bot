# Primal Generation, Dual Judgment: Self-Training from Test-Time Scaling

- arXiv ID: `2605.11299v2`
- Authors: Yizhu Jiao, Ruixiang Zhang, Richard Bai, Jiawei Han, Ronan Collobert, Yizhe Zhang
- Published: 2026-05-11
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.CL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.11299v2) | [pdf](https://arxiv.org/pdf/2605.11299v2)

## Abstract

Code generation is typically trained in the primal space of programs: a model produces a candidate solution and receives sparse execution feedback, often a single pass/fail bit. Test-time scaling enriches the inference procedure by sampling multiple candidates and judging among them, but the comparative information this process reveals is discarded after inference. We argue that this information defines a dual judgment space that provides a far richer training signal: the model learns not from an isolated success or failure, but from the relative correctness structure across its own plausible attempts, identifying which succeed, which fail, and what distinguishes them. We introduce DuST (Dual Self-Training), a framework for self-training from the dual judgment space. DuST samples candidate programs from the model's own distribution, labels them through sandbox execution, retains groups containing both successes and failures, and trains the model to rank candidates by execution correctness using GRPO. The objective is purely discriminative: the model is never directly rewarded for generating correct programs. Dual self-training improves both judgment and generation. Across five models spanning two families and three scales (4B to 30B), DuST consistently improves Best-of-4 test-time scaling on LiveCodeBench. For Qwen3-30B-Thinking on LiveCodeBench v6, judgment quality improves by +6.2 NDCG, single-sample pass@1 improves by +3.1, and Best-of-4 accuracy improves by +4.1. The trained model's single rollout matches the base model's Best-of-4 performance. SFT on the same ranking data improves judgment without improving generation, confirming that on-policy RL is the mechanism that transfers dual-space learning back into primal generation.
