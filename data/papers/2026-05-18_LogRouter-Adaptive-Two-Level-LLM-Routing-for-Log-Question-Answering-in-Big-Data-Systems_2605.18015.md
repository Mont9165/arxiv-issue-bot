# LogRouter: Adaptive Two-Level LLM Routing for Log Question Answering in Big Data Systems

- arXiv ID: `2605.18015v1`
- Authors: Mert Coskuner, Merve Zeybel, Melik Mert Dolan
- Published: 2026-05-18
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.DB`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.18015v1) | [pdf](https://arxiv.org/pdf/2605.18015v1)

## Abstract

Production log analytics in self-hosted, resource-constrained environments requires natural-language access to massive log streams without the cost of routing every query through a large language model. We present LogRouter, an end-to-end log question-answering system deployed on TUBITAK BILGEM's national big data platform that combines a PySpark-based Drain3 ingestion pipeline, GPU-accelerated embeddings, and dual-index storage in Apache Druid and PostgreSQL with pgvector. A two-level cost-aware router dispatches each query along one of four execution paths: direct response, Druid keyword search, template lookup with SQL generation, and pgvector semantic retrieval, while a Level-2 router selects either a 14B-class or 32B-class generator for the semantic path. A dedicated coder LLM handles text-to-SQL generation. We evaluate the system on four LogHub datasets (Linux, Apache, Windows, and Mac; 70 questions in total) under both an online full-pipeline configuration and an offline configuration that isolates the generator. The router reaches 88.4% mean accuracy across datasets and 94.7% on Linux, while the full pipeline attains a mean ROUGE-1 of 0.373, BERTScore of 0.879, RAGAS Faithfulness of 0.779, and an end-to-end latency of 18.6 s. In an apples-to-apples offline comparison, the routed system reduces mean latency by 55% versus a Fixed-32B baseline (46.3 s vs. 102.1 s) while preserving Answer Correctness within 5.8 points and exceeding a Fixed-14B baseline on RAGAS Faithfulness across every dataset. Cost-aware dispatching is therefore a practical mechanism for production log QA: routing recovers most of the quality of an always-32B configuration at less than half the latency, and the L1 keyword vocabulary makes that routing decision with high precision without a learned classifier.
