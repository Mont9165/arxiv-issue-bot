# Multi-level Code Optimization via Mixture of Prompts

- arXiv ID: `2607.23665v1`
- Authors: Yun Peng, Jun Wan, Jiakun Liu, Shuzheng Gao, David Lo, Xiaoxue Ren
- Published: 2026-07-26
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.23665v1) | [pdf](https://arxiv.org/pdf/2607.23665v1)

## Abstract

Runtime efficiency is a critical factor that impacts both software quality and user satisfaction. There are many approaches proposed for code optimization to improve runtime efficiency. Traditional code optimization methods operate on intermediate representations (IRs) during compilation for static languages. They are effective but struggle to handle dynamic languages that do not require compilation. Recently, large language models (LLMs) have been leveraged to directly optimize source code in dynamic languages. However, these methods fail to identify suitable optimization targets and usually conduct incomprehensive single-level optimization.
  To address these challenges, we propose Optimo, a multi-level LLM-based code optimization approach built on a novel Mixture-of-Prompts (MoP) architecture. In the MoP architecture, Optimo identifies time-critical code structures as performance bottlenecks via differential profiling. These structures are then routed to some optimization strategies, akin to expert models in MoE, each tailored to optimize specific code patterns. Unlike traditional approaches that focus only on statement-level optimizations, Optimo operates at four levels of abstraction, ranging from coarse-grained algorithmic improvements to fine-grained optimizations in API usage. We evaluate Optimo on two code efficiency benchmarks, COFFE and Effibench. Our results demonstrate that Optimo achieves an up to 57.48% opt%, i.e., the percentage of optimized programs that are correct and at least 10% faster than the original programs, and an up to 3.97x speedup when optimizing human-written code, and it consistently outperforms the best baseline by up to 96.51% in terms of opt%. Furthermore, Optimo achieves an up to 42.42% opt% and an up to 13.51x speedup when optimizing LLM-generated code.
