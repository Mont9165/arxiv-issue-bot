# ClarifyCodeBench: Evaluating LLMs on Clarifying Ambiguous Requirements for Code Generation

- arXiv ID: `2607.00711v1`
- Authors: Zheng Fang, Dongming Jin, Yihong dong, Yongmin Li, Kechi Zhang, Zhi Jin, Ge Li
- Published: 2026-07-01
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.00711v1) | [pdf](https://arxiv.org/pdf/2607.00711v1)

## Abstract

Large Language Models have emerged as programming assistants. However, the efficacy of code generation is constrained by the quality of input requirements, which are frequently ambiguous, incomplete, or underspecified. While LLMs excel at one-shot code synthesis, their ability to proactively clarify intent remains underexplored, as a critical trait for robust software engineering. Existing benchmarks largely overlook this interactive bottleneck, assuming perfectly specified prompts that do not reflect the iterative nature of requirement elicitation. To bridge this gap, we introduce ClarifyCodeBench, a novel interactive benchmark for evaluating LLMs' capability in resolving requirement ambiguity. Constructed from real-world programming tasks, ClarifyCodeBench features high-quality manual annotations, including N unique ambiguity types, associated clarification questions, and corresponding ground-truth answers. Furthermore, we formalize two rigorous metrics to assess the interaction quality: Turn-discounted Key Question Rate, which penalizes inefficient questioning, and Optimal Round Adherence, which measures the precision of the elicitation process. We conduct a systematic evaluation of six state-of-the-art LLMs using ClarifyCodeBench. Our empirical results yield three critical insights: 1) Capability Decoupling: Strong code generation performance does not inherently translate to effective requirement clarification; 2) The Reasoning Paradox: While increased computational thinking enhances code correctness, it yields marginal gains in identifying ambiguities; 3) The Multi-ambiguity Ceiling: LLMs' clarification performance degrades sharply as the density of ambiguities increases, revealing a significant bottleneck in handling complex, real-world specifications. Our work underscores the necessity for future AI4SE research to transition from static synthesis to interactive elicitation.
