# Mandol: An Agglomerative Agent Memory System for Long-Term Conversations

- arXiv ID: `2606.29778v1`
- Authors: Yuhan Zhang, Zhiyuan Guo, Ziheng Zeng, Wei Wang, Wentao Wu, Lijie Xu
- Published: 2026-06-29
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`, `cs.CL`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2606.29778v1) | [pdf](https://arxiv.org/pdf/2606.29778v1)

## Abstract

Long-term conversational agents need to remember and query cross-session, multi-typed information with complex correlations. Existing agent memory systems rely on heterogeneous vector and graph databases, which fragment memory information and cause high cross-database I/O latency. For retrieval, common RAG-style methods tend to introduce noise, miss correlated clues, and lack token budget control, degrading LLM accuracy and efficiency.
  We propose Mandol, an agglomerative memory system that consolidates fragmented memory representations and storage into a unified memory-native architecture. Its core components include: (1) a hierarchical memory model that organizes memory into a basic layer representing raw memory information and a high-level abstract layer that agglomerates basic memories into traceable abstract memories, both uniformly represented as structured semantic graphs; (2) an agglomerative semantic data structure combining SemanticMap and SemanticGraph, which natively fuses key-value, vector, and graph structures and provides unified hybrid retrieval operators to eliminate cross-database I/O; and (3) a quantitative query mechanism with query-adaptive routing, quantitative denoising and conflict resolution, and token-constrained context generation, all without involving LLMs during retrieval. Experiments on two widely used long-term conversation benchmarks, LoCoMo and LongMemEval, show that Mandol achieves the best overall accuracy among representative agent memory systems. For performance comparison, Mandol also obtains a 5.4x retrieval speedup and a 4.8x insertion speedup under 10 QPS concurrent load, while still maintaining low latency on consumer-grade hardware.
