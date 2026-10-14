# QCATS: Query Context-Aware Transformer Slicing for Efficient Predictive Query Processing

- arXiv ID: `2610.09894v1`
- Authors: Yueying Li, Zhongle Xie, Ke Chen, Lidan Shou
- Published: 2026-10-07
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2610.09894v1) | [pdf](https://arxiv.org/pdf/2610.09894v1)

## Abstract

In-database predictive query processing increasingly applies Transformer-based models within relational pipelines. However, existing in-database inference typically exposes only tuple-level model inputs to the inference runtime, leaving relational predicates and metadata statistics invisible to neural execution planning. In this paper, we propose QCATS, a query context-aware transformer slicing framework that enables efficient sparse inference inside database systems. QCATS executes at query granularity: instead of routing individual tokens or tuples during inference, it uses query predicates and metadata statistics to pre-select context-aligned FFN slices before model execution. The framework comprises offline expert construction and lightweight query-level routing that dynamically selects experts during execution. QCATS further introduces system optimizations, including asynchronous CPU-GPU pipelines and routing-aware batching. Experiments on four predictive-query workloads with BERT-base and Qwen-0.6B show that QCATS achieves up to 4.42x latency reduction while preserving prediction accuracy comparable to dense baselines.
