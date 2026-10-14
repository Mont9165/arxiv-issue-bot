# Repository-Level Solidity Code Generation with Large Language Models: From Prompting to Fine-Tuning

- arXiv ID: `2606.19988v1`
- Authors: Shi Chen, Rongcun Wang, Yuan Tian, Xiaoyuan Xie, Wei Song, Rubing Huang
- Published: 2026-06-18
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.19988v1) | [pdf](https://arxiv.org/pdf/2606.19988v1)

## Abstract

Large Language Models (LLMs) have shown strong capabilities in general-purpose code generation, but their effectiveness in specialized software domains remains underexplored. Solidity smart contracts represent a high-stakes domain where generated code must satisfy strict language-level, security, and software-engineering constraints. Existing benchmarks and metrics remain insufficient for repository-level Solidity generation, where models must synthesize complete contracts from natural language requirements. To address this gap, we introduce SolidityBench, a benchmark of 5,470 repository-level Solidity smart contracts paired with natural language descriptions. We also propose SolidityScore, a Solidity-aware semantic metric that emphasizes domain-critical constructs such as security modifiers, contract declarations, and Solidity-specific keywords. Using this benchmark, we evaluate representative code LLMs, including Qwen2.5-Coder, DeepSeek-Coder, and CodeLlama, across zero-shot prompting, Chain-of-Thought reasoning, in-context learning, retrieval-augmented generation, and supervised fine-tuning. The results show that general-purpose models exhibit systematic structural deficiencies in repository-level Solidity generation. Among non-parametric methods, retrieval-augmented generation performs best, while in-context learning degrades beyond two examples due to context saturation. Supervised fine-tuning achieves the largest improvement by internalizing Solidity-specific constraints into model parameters. Overall, our study provides a comprehensive benchmark for repository-level Solidity code generation and shows that high-quality domain data combined with supervised fine-tuning is the most effective strategy for improving the reliability of LLM-generated smart contracts.
