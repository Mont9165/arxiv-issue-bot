# Larch: Learned Query Optimization for Semantic Predicates

- arXiv ID: `2606.07923v1`
- Authors: Fuheng Zhao, Pawel Liskowski, Zihan Li, Benjamin Han, Puxuan Yu, Varich Boonsanong, Dimitris Tsirogiannis, Anupam Datta
- Published: 2026-06-06
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2606.07923v1) | [pdf](https://arxiv.org/pdf/2606.07923v1)

## Abstract

With the advent of Large Language Models (LLMs), many database systems introduced semantic operators that enabled analytical queries over unstructured data (e.g. text, images, videos). Semantic operators typically incur high inference costs and latencies making semantic (AI) SQL queries challenging to apply on large scale datasets. At the same time, their semantic nature leads database engines to treat them as black boxes, making AISQL queries difficult to optimize. In this paper, we introduce Larch, a framework for optimizing the execution of semantic filters in AI SQL queries. Larch was inspired by two key observations: i) the high latency of semantic operators leaves significant room for computationally-heavy runtime optimization techniques, ii) unstructured data are typically accompanied by semantic information in the form of embeddings allowing for efficient semantic comparisons between AI_FILTER prompts and data values. Based on these two key observations, we present two Larch variants: Larch-A2C and Larch-Sel. Larch-A2C encodes arbitrary semantic filters expression tree using an embedding-augmented Gated Graph Neural Network and formulates the filter evaluation order as a Markov decision process. In contrast, Larch-Sel leverages a supervised learning model to predict filter selectivities, subsequently applying dynamic programming to find a near-optimal evaluation order for each input row. Evaluated across diverse real-world datasets and comprehensive synthetic workloads, both Larch variants always outperform existing semantic filter optimization techniques in terms of token usage. Our results demonstrate that Larch is robust across diverse workloads, reducing total token cost overhead by 3x-19x compared to Palimpzest and Quest.
