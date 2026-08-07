# RefEvo: Agentic Design with Co-Evolutionary Verification for Agile Reference Model Generation

- arXiv ID: `2604.24218v1`
- Authors: Yifan Zhang, Jianmin Ye, Jiahao Yang, Xi Wang
- Published: 2026-04-27
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2604.24218v1) | [pdf](https://arxiv.org/pdf/2604.24218v1)

## Abstract

As the complexity of System-on-Chip (SoC) designs grows, the shift-left paradigm necessitates the rapid development of high-fidelity reference models (typically written in SystemC) for early architecture exploration and verification. While Large Language Models (LLMs) show promise in code generation, their application to hardware modeling faces unique challenges: (1) Rigid, static workflows fail to adapt to varying design complexity, causing inefficiency; (2) Context window overflow in multi-turn interactions leads to catastrophic forgetting of critical specifications; and (3) the Coupled Validation Failure problem--where generated Testbenches (TBs) incorrectly validate flawed models due to correlated hallucinations--severely undermines reliability. To address these limitations, we introduce RefEvo, a dynamic multi-agent framework designed for agile and reliable reference modeling. RefEvo features three key innovations: (1) A Dynamic Design Planner that autonomously decomposes design specifications and constructs tailored execution workflows based on semantic complexity; (2) A Co-Evolutionary Verification Mechanism, which employs a Dialectical Arbiter to simultaneously rectify the model and verification logic against the specification (Spec) oracle, effectively mitigating false positives; and (3) A Spec Anchoring Strategy for lossless context compression. Evaluated on a diverse benchmark of 20 hardware modules, RefEvo achieves a 95% pass rate, outperforming static baselines by a large margin. Furthermore, our context optimization reduces token consumption by an average of 71.04%, achieving absolute savings of over 70,000 tokens per session for complex designs while maintaining 100% specification recall.
