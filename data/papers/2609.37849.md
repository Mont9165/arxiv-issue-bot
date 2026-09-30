# Is manual software optimization a thing of the past?

- arXiv ID: `2609.37849v1`
- Authors: Pavlin G. Poličar, Martin Špendl, Tomaž Hočevar
- Published: 2026-09-29
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.37849v1) | [pdf](https://arxiv.org/pdf/2609.37849v1)

## Abstract

Scientific software is increasingly required to process larger datasets while maintaining acceptable execution times. Software optimization traditionally requires substantial expertise in programming, algorithms, and numerical methods. Recent advances in large language models (LLMs) offer the possibility of automating much of this process. We investigate whether LLM-based agents can autonomously achieve substantial performance improvements in scientific software, including mature implementations that have already been extensively optimized by human developers. We tasked an LLM-based agent with optimizing software for three computational problems: t-SNE, single-sample gene set enrichment analysis (ssGSEA), and graphlet counting. Humans defined the scope, correctness criteria, and a verification mechanism, after which the agent worked autonomously, in some cases for several hours. Code maintainers reviewed each resulting implementation and verified its correctness. The optimized implementations were faster in all tested configurations, by up to two orders of magnitude over the fastest existing tools. The improvements included low-level code optimizations, mathematical reformulations, and an entirely new algorithm for graphlet counting. Software optimization can increasingly be delegated to autonomous agents, with the human role shifting from implementing optimizations to deciding which software to optimize, defining objectives, providing verification mechanisms, and ensuring the correctness of the final software. For well-scoped, verifiable problems, we argue that manual software optimization may be a thing of the past.
