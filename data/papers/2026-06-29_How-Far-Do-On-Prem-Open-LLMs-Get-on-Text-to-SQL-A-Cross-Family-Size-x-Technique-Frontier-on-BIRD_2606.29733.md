# How Far Do On-Prem Open LLMs Get on Text-to-SQL? A Cross-Family Size x Technique Frontier on BIRD

- arXiv ID: `2606.29733v1`
- Authors: Vladimir Beskorovainyi
- Published: 2026-06-29
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.DB`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2606.29733v1) | [pdf](https://arxiv.org/pdf/2606.29733v1)

## Abstract

Organizations that cannot send data to a cloud API increasingly ask: how good is Text-to-SQL if the model must run on-premises on open weights, and which popular accuracy "recipes" are worth their compute? We answer with an honest, fully reproducible benchmark on the BIRD development split (n=1534, Execution Accuracy), evaluating three open model families across two generations -- Qwen2.5-Coder (7B/14B/32B), CodeLlama-Instruct (7B/13B/34B), and Llama-3.x (8B, 70B) -- under one matched protocol, ablating a model-agnostic recipe (schema linking, self-correction, self-consistency) component by component, with every difference tested by the paired McNemar test. Four findings stand out. (i) Generation matters more than raw size, and the recipe is family-robust: Qwen2.5-Coder dominates the older CodeLlama at matched size (39.1 vs 20.9 at 7B), but a modern non-Qwen model (Llama-3.3-70B, 49.2 on a matched serving) is competitive, so CodeLlama's weakness reflects its 2023 generation, not "non-Qwen = weak". (ii) Self-correction is a robust, near-free win, significant on all three families where there is room to improve. (iii) Schema linking does not help, and a stronger linker does not rescue it: a retrieval/embedding linker with 96.5% gold-table recall is statistically indistinguishable from no linking, ruling out the "weak lexical strawman" objection across three families. (iv) Self-consistency is poor value (+0.13 pp for ~5x tokens, not significant). We report real per-stage cost ($/1k queries) and release all code, predictions, and summaries; archived code and data: https://doi.org/10.5281/zenodo.20952794
