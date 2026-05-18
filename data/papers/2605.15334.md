# From I/O to Code with Discovery Agent

- arXiv ID: `2605.15334v1`
- Authors: Yihong Dong, Jiaru Qian, Haoran Zhang, Peixu Wang, Binhua Li, Zhi Jin, Yongbin Li, Ge Li, Xiaokang Yang, Xue Jiang
- Published: 2026-05-14
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.AI`, `cs.CL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.15334v1) | [pdf](https://arxiv.org/pdf/2605.15334v1)

## Abstract

The automatic synthesis of a program from any form of specification is regarded as a holy grail of computer science. Fueled by LLMs, NL2Code has achieved tremendous success, yet the fundamentally more challenging task of synthesizing programs from input-output behavior, which we refer to as IO2Code, remains largely unsolved. Whereas NL2Code can exploit the semantic alignment between natural language and code acquired during pretraining, IO2Code requires recovering underlying principles from concrete computational behavior, navigating a vast and underspecified hypothesis space. To address this, we propose DIO-Agent, a discovery agent for IO2Code. Our method frames IO2Code as an evolutionary search over discrete program space, in which an LLM serves as the mutation operator and concrete error signals from execution guide each mutation. To prevent the search from wandering into structurally complex yet incorrect dead ends, we introduce the Transformation Priority Premise as a mutation prior that biases the LLM toward the simplest hypothesis consistent with current evidence, progressively escalating from constants to conditionals to iteration only when simpler constructs are insufficient. To facilitate systematic study, we further construct an IO2CodeBench spanning multiple difficulty levels. Extensive experiments show that DIO-Agent consistently outperforms both traditional program-by-example method and SOTA evolution-agent baselines across all difficulty levels and various LLMs, while substantially surpassing test-time scaling strategies with equivalent sampling budgets.
