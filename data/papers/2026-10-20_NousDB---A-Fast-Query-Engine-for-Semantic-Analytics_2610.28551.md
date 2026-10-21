# NousDB - A Fast Query Engine for Semantic Analytics

- arXiv ID: `2610.28551v1`
- Authors: Christos Tsapelas, Georgia Koutrika, Yannis Ioannidis
- Published: 2026-10-20
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.28551v1) | [pdf](https://arxiv.org/pdf/2610.28551v1)

## Abstract

Semantic data analytics systems integrate AI-powered operators into query pipelines, enabling declarative queries over structured and unstructured data. However, existing systems rely on per-tuple model invocations, ad hoc operator designs, and lack principled cost models, resulting in poor scalability and limited optimization. We present NousDB, a high-performance semantic analytics engine built on Apache DataFusion\cite{10.1145/3626246.3653368}.Through NousDB we propose an extended relational algebra with three semantic operators and formal algebraic properties that enable principled query rewriting and cross-operator optimization. We further propose a token-based cost model using equi-depth token histograms to optimize batch sizing under context-window constraints and provide statistical guarantees for safe batching. Experiments show that NousDB achieves up to $\times 86$ speedups with both local and enterprise LLMs, while leading competitors in token efficiency and accuracy. These gains extend to complex JOB and Stack workloads augmented with semantic operators, supporting both traditional and semantic analytics.
