# Gaussian Relational Graph Transformer

- arXiv ID: `2605.15575v1`
- Authors: Zezhong Ding, Jin Li, Xugang Wang, Xike Xie
- Published: 2026-05-15
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.15575v1) | [pdf](https://arxiv.org/pdf/2605.15575v1)

## Abstract

Relational graph learning models relational databases as graphs and has demonstrated superior performance on a wide range of relational predictive tasks. However, existing methods struggle to capture long-range dependencies due to information decay in their message-passing mechanisms, and recent relational graph transformers remain limited in jointly modeling structural, semantic, and temporal information. In this paper, we propose GelGT, a Gaussian relational graph transformer that explicitly addresses these challenges. GelGT introduces a structure-semantic collaborative sampling strategy to preserve structural connectivity while filtering irrelevant semantic information, and incorporates a Gaussian graph attention mechanism with a learnable Gaussian bias on the sampled subgraphs to dynamically encode temporal dependencies. Extensive experiments on various real-world datasets demonstrate that GelGT achieves state-of-the-art downstream task performance, with up to a 13.8% improvement in predictive performance.
