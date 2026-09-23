# FeatLens: Feature-Guided Dynamic Code Graph Construction and Retrieval for Repository-Level Code Generation

- arXiv ID: `2609.26480v1`
- Authors: Xutian Li, Bo Xiong, Yifeng Zhu, Kunze Li, Xianlin Zhao, Runbang Yan, Yanzhen Zou, Lu Zhang, Bing Xie
- Published: 2026-09-22
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.26480v1) | [pdf](https://arxiv.org/pdf/2609.26480v1)

## Abstract

Recent code generation research has moved from isolated function completion toward repository-level generation in existing codebases. To implement a target function correctly, an LLM must identify reusable repository dependencies such as existing functions, APIs, and cross-file definitions. Existing retrieval methods provide such context through code similarity search, persistent whole-repository graphs, or LLM-driven graph exploration, but often incur high graph construction, reasoning, and token costs. Feature-oriented methods offer a natural view of software functionality, yet they mainly support requirement decomposition, planning, or feature editing rather than code dependency retrieval. This paper presents \textbf{FeatLens}, a feature-guided dynamic code graph construction and retrieval approach for repository-level code generation. FeatLens builds a feature index that links natural-language feature descriptions to function-level code entities. Given a generation task, it dynamically constructs a task-specific seed graph from the feature index and applies semantic-structural graph reasoning with personalized PageRank to select a compact reasoning graph. This design replaces persistent whole-repository graph maintenance and LLM exploration with deterministic and lightweight dependency retrieval. Experiments on DevEval and EvoCodeBench show that FeatLens achieves the best DR@15 among sparse, dense, and graph-based baselines (0.501 and 0.460). On DevEval generation, it obtains the highest DIR@1, reaching 52.91\% with DeepSeek-V3.2 and 53.58\% with GPT-5-mini, while maintaining competitive Pass@1 and producing shorter code. Compared with the strongest graph-based baseline, FeatLens reduces graph nodes by 61.0\%, edges by 86.2\%, and total token overhead by 45.9\%, with no LLM tokens used during retrieval.
