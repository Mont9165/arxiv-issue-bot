# Fairness-Aware Retrieval Optimization for Retrieval-Augmented Generation

- arXiv ID: `2605.15790v1`
- Authors: Yingqi Zhao, Vasilis Efthymiou, Jyrki Nummenmaa, Kostas Stefanidis
- Published: 2026-05-15
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2605.15790v1) | [pdf](https://arxiv.org/pdf/2605.15790v1)

## Abstract

Retrieval-Augmented Generation (RAG) improves reliability of large language models by incorporating external knowledge, but the retrieval process can introduce bias that propagates to generated outputs. This issue is particularly challenging in top-k settings, where multiple documents jointly influence generation. We propose a fairness-aware retrieval framework that models and controls this bias. Our approach combines controlled bias injection via reranking, a position-aware model of bias propagation, and an optimization formulation that balances relevance and fairness. We further introduce a scalable solution based on Quadratic Fairness via Dual Hyperplane Approximation (FARO), which enables efficient optimization through problem decomposition. Experimental results show that our method effectively mitigates generation bias while preserving relevance. This work provides a principled approach for fairness-aware retrieval in RAG systems.
