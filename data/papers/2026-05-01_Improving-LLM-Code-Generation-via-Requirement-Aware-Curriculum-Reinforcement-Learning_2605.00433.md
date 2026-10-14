# Improving LLM Code Generation via Requirement-Aware Curriculum Reinforcement Learning

- arXiv ID: `2605.00433v1`
- Authors: Shouyu Yin, Zhao Tian, Junjie Chen, Shikai Guo
- Published: 2026-05-01
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.00433v1) | [pdf](https://arxiv.org/pdf/2605.00433v1)

## Abstract

Code generation, which aims to automatically generate source code from given programming requirements, has the potential to substantially improve software development efficiency. With the rapid advancement of large language models (LLMs), LLM-based code generation has attracted widespread attention from both academia and industry. However, as programming requirements become increasingly complex, existing LLMs still exhibit notable performance limitations. To address this challenge, recent studies have proposed training-based curriculum reinforcement learning (CRL) strategies to improve LLM code generation performance. Despite their effectiveness, existing CRL approaches suffer from several limitations, including misaligned requirement difficulty perception, the absence of requirement difficulty optimization, and suboptimal curriculum sampling strategies. In CRL-based code generation, programming requirements serve as the sole input to the model, making their quality and difficulty critical to training effectiveness. Motivated by insights from software requirements engineering, we propose RECRL, a novel requirement-aware curriculum reinforcement learning framework for enhancing LLM-based code generation. RECRL automatically perceives model-specific requirement difficulty, optimizes challenging requirements to improve training data utilization, and employs an adaptive curriculum sampling strategy to construct training batches with smoothly varying difficulty. Extensive experiments on five state-of-the-art LLMs across five widely-used code generation benchmarks by comparing with five state-of-the-art baselines, demonstrate the significant effectiveness of RECRL. For example, RECRL achieves an average Pass@1 improvement of 1.23%-5.62% over all state-of-the-art baselines.
