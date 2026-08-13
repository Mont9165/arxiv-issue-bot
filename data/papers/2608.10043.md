# N2NMatcher: Towards Inlining-Resilient Binary Decomposition and Module Matching

- arXiv ID: `2608.10043v1`
- Authors: Ang Jia, He Jiang, Zhipeng Yang, Zhilei Ren, Xiaochen Li
- Published: 2026-08-10
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.10043v1) | [pdf](https://arxiv.org/pdf/2608.10043v1)

## Abstract

Program-level Binary Code Similarity Analysis (BCSA) aims to identify semantically similar code regions across binary programs, serving as a fundamental technique for software plagiarism detection, vulnerability search, and malware analysis. Existing approaches often decompose binaries into modules following the structure of function call graphs (FCGs) and then match these modules by their contained functions. However, function inlining changes both FCG structures and binary function semantics, making existing decomposition and module matching methods less effective.
  In this work, we propose N2NMatcher, an inlining-resilient framework for binary decomposition and module matching. We first conduct an empirical study to examine whether binaries still contain functions that provide stable module boundaries across compilation settings. N2NMatcher learns to predict such functions as anchors using a hierarchical graph neural network that encodes binary ACFG-FCG representations built from opcode sequences, control-flow structures, and FCG calling context. It then performs anchor-bounded decomposition and matches the generated modules using learned module graph embeddings. Experimental results show that N2NMatcher improves both the decomposition quality and module matching accuracy compared to existing works, enabling more effective program-level BCSA.
