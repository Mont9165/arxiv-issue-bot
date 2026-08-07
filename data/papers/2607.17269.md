# An Explicit World Model Based on Data-First Ontology: DaoQL Multimodal Storage Validation and Counterfactual Reasoning Evaluation

- arXiv ID: `2607.17269v1`
- Authors: Zhanbo Li, Shifeng Wu, Xiangjin Meng, Wenjie Cai
- Published: 2026-07-19
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.17269v1) | [pdf](https://arxiv.org/pdf/2607.17269v1)

## Abstract

Large language models encode world models implicitly in neural weights, which exposes four structural risks in high-precision domains such as medicine and finance: hallucination, frozen knowledge, poor explainability, and poor modifiability. This paper proposes data-first ontology: LLMs are treated as reasoning and language engines, while deterministic knowledge is moved into an explicit multimodal database, DaoQL. We formalize an explicit world model and show that, under rule independence, deterministic evaluation, and fixed conflict resolution, explicit models provide a sufficient condition for composable counterfactual decomposability; implicit models lack atomic read/delta semantics and therefore provide no comparable architectural guarantee. The implemented system focuses on DaoQL's verified storage layer and explicit Eval path, integrating graph, column, vector, and full-text engines within one process. KVCache graph nodes, expert hot updates, and the DaoQL-Agent runtime remain future work. On an embedded same-machine setup, DaoQL reports graph BFS at 1.20 ms, HNSW at 83.1 us, and a Fluent hybrid query at 105.8 us; these results indicate engineering potential but must be interpreted with deployment-shape differences from client-server systems. Exploratory measurements on LDBC SNB SF1 and ANN-Benchmarks further show 34/34 query coverage with interactive-class queries mostly in the sub-millisecond to millisecond range, but only 1.8 QPS overall due to long-tail BI/IC queries; ANN-Benchmarks reaches Recall@10 >= 99% at thousand-level QPS after a bridge-edge protection fix. In a five-domain counterfactual experiment (n = 1250), DaoQL+GPT-4o achieves 94% composable counterfactual decomposability, 49 percentage points above GPT-4o alone. The paper explicitly separates provable structure, preliminary empirical evidence, and architectural roadmap claims.
