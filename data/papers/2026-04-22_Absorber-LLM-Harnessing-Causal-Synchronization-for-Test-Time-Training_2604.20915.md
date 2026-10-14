# Absorber LLM: Harnessing Causal Synchronization for Test-Time Training

- arXiv ID: `2604.20915v1`
- Authors: Zhixin Zhang, Shabo Zhang, Chengcan Wu, Zeming Wei, Meng Sun
- Published: 2026-04-22
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.AI`, `cs.CL`, `cs.SE`, `math.OC`
- Links: [abs](http://arxiv.org/abs/2604.20915v1) | [pdf](https://arxiv.org/pdf/2604.20915v1)

## Abstract

Transformers suffer from a high computational cost that grows with sequence length for self-attention, making inference in long streams prohibited by memory consumption. Constant-memory alternatives such as RNNs and SSMs compress history into states with fixed size and thus lose long-tail dependencies, while methods that memorize contexts into parameters, such as Test-Time Training (TTT), are prone to overfitting token-level projection and fail to preserve the causal effect of context in pretrained LLMs. We propose Absorber LLM, which formulates long-context retention as a self-supervised causal synchronization: after absorbing historical contexts into parameters, a contextless model should match the original model with full context on future generations. We optimize this objective by synchronizing internal behaviors of the updated model with the original one, ensuring context absorption and generalization. Experiments on long-context and streaming benchmarks show that Absorber LLM reduces inference memory and improves accuracy over prior parameter-as-memory baselines.
