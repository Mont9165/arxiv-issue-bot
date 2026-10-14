# When Prompt Under-Specification Improves Code Correctness: An Exploratory Study of Prompt Wording and Structure Effects on LLM-Based Code Generation

- arXiv ID: `2604.24712v1`
- Authors: Amal AKLI, Mike PAPADAKIS, Maxime CORDY, Yves Le TRAON
- Published: 2026-04-27
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.24712v1) | [pdf](https://arxiv.org/pdf/2604.24712v1)

## Abstract

Large language models are increasingly used for code generation, yet the correctness of their outputs depends not only on model capability but also on how tasks are specified. Prior studies demonstrate that small changes in natural language prompts, particularly under-specification can substantially reduce code correctness; however, these findings are largely based on minimal-specification benchmarks such as HumanEval and MBPP, where limited structural redundancy may exaggerate sensitivity. In this exploratory study, we investigate how prompt structure, task complexity, and specification richness interact with LLM robustness to prompt mutations. We evaluate 10 different models across HumanEval and the structurally richer LiveCodeBench. Our results reveal that robustness is not a fixed property of LLMs but is highly dependent on prompt structure: the same under-specification mutations that degrade performance on HumanEval have near-zero net effect on LiveCodeBench due to redundancy across descriptions, constraints, examples, and I/O conventions. Surprisingly, we also find that prompt mutations can improve correctness. In LiveCodeBench, under-specification often breaks misleading lexical or structural cues that trigger incorrect retrieval-based solution strategies, leading to correctness improvements that counterbalance degradations. Manual analysis identifies consistent mechanisms behind these improvements, including the disruption of over-fitted terminology, removal of misleading constraints, and elimination of spurious identifier triggers. Overall, our study shows that structurally rich task descriptions can substantially mitigate the negative effects of under-specification and, in some cases, even enhance correctness. We outline categories of prompt modifications that positively influence the behavior of LLM code-generation, offering practical insights for writing robust prompts.
