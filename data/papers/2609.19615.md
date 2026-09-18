# Semantic Layer Induction from Raw Telemetry via Hierarchical LLM and RAG Abstraction

- arXiv ID: `2609.19615v1`
- Authors: Yuanzhe Jia, Ali Anaissi
- Published: 2026-09-17
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.AI`, `cs.IR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.19615v1) | [pdf](https://arxiv.org/pdf/2609.19615v1)

## Abstract

Modern applications generate massive volumes of raw telemetry data, but translating those noisy, heterogeneous event streams into actionable business insights remains a fundamental challenge. Data engineers and analysts expend substantial effort reconciling semantic discrepancies, hand-crafting parsing logics, and maintaining fragile mappings between raw data and business KPIs. In this paper, we present an end-to-end framework that fully automates the construction of a business semantic layer from application raw logs. Our approach introduces a two-stage semantic abstraction: first, high-level business features are identified via LLM inference augmented with domain-specific industry knowledge; second, fine-grained business nodes are derived through a structured pipeline comprising data refinement, hybrid retrieval, multi-stage filtering, semantic clustering, and canonical naming. Evaluation on production-scale telemetry demonstrates that our system improves human-assessed semantic quality from 50 to 80+ on a 100-point scale, reduces maintenance effort by 80%, filters out 74% of noise, and achieves 0.87 Cohen's kappa via an integrated LLM-as-Judge evaluation, enabling continuous, scalable quality assurance. Overall, our work distinguishes itself from prior work by addressing the novel problem of business semantic layer induction from raw telemetry, operating without labeled training data or manual rule engineering.
