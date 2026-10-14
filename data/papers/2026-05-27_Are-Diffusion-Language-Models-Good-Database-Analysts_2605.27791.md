# Are Diffusion Language Models Good Database Analysts?

- arXiv ID: `2605.27791v1`
- Authors: Peixian Ma, Xialie Zhuang, Jiantao Tan, Changlun Li, Ruirui Chen, Chengwei Qin
- Published: 2026-05-27
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.27791v1) | [pdf](https://arxiv.org/pdf/2605.27791v1)

## Abstract

Recent advancements in large language models (LLMs) have significantly improved Natural Language to SQL (NL2SQL) tasks, yet most NL2SQL systems continue to rely on the autoregressive (AR) paradigm. The highly structured nature of SQL makes AR models susceptible to sequential error propagation due to their rigid left-to-right decoding process. Diffusion Language Models~(DLMs) have recently emerged as a promising alternative, replacing unidirectional decoding with iterative denoising to enable global sequence refinement. Nevertheless, the adoption of DLMs in NL2SQL is constrained by a fragmented ecosystem and the absence of a standardized evaluation framework, which obscures their true capabilities and impedes fair comparison with AR baselines. In this paper, we propose a unified evaluation framework that standardizes both generation and execution environments across various DLM architectures. To further improve the performance of DLMs-based NL2SQL systems, we propose \texttt{SQL-D1}, a novel agentic framework that integrates database-aware context engineering, test-time scaling and interactive optimization. Through extensive empirical studies on scaling properties, post-training stability, and primary failure modes, we demonstrate that DLMs offer distinct advantages in structural robustness and facilitate flexible trade-offs between efficiency and accuracy. By distilling these insights into structured takeaways, our work provides a systematic understanding of DLMs-based NL2SQL and lays the foundation for future database analysis agents.
