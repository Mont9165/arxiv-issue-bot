# DeepRepro: State-Aware Subplanning for Paper-to-Code Reproduction in Evolving Repositories

- arXiv ID: `2608.26557v1`
- Authors: Hongru Song, Ruqing Zhang, Jiafeng Guo, Xueqi Cheng, Maarten de Rijke
- Published: 2026-08-27
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.26557v1) | [pdf](https://arxiv.org/pdf/2608.26557v1)

## Abstract

Recent advances in agentic large language models (LLMs) have enabled increasingly autonomous software engineering workflows, yet automatic machine learning (ML) paper-to-code reproduction remains a challenging long-horizon problem. Unlike conventional code generation, this task requires constructing and maintaining a fully functional repository whose state continuously evolves during execution. Existing systems typically rely on static upfront planning followed by sequential file-level generation, which often leads to inconsistencies as dependencies, interfaces, and execution feedback change over time. We propose DeepRepro, a state-aware framework for paper-to-code reproduction based on execution-state-aware subplanning. DeepRepro dynamically transforms evolving repository states and runtime feedback into fine-grained implementation subplans, keeping planning aligned with execution throughout repository construction. The framework further incorporates repository-aware orchestration and a lightweight process-aware interface for transparent monitoring of long-horizon reproduction. Experiments on PaperBench Code-Dev show that DeepRepro consistently outperforms strong scientific and commercial code-agent baselines.
