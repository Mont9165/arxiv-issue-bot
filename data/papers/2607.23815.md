# Kalypso: Relational LLM Serving

- arXiv ID: `2607.23815v1`
- Authors: Hojae Son, Md Ashraful Islam, Huy Gia Cao, Hui Guan, Marco Serafini
- Published: 2026-07-26
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2607.23815v1) | [pdf](https://arxiv.org/pdf/2607.23815v1)

## Abstract

Large language models are increasingly used as semantic operators for filtering, extracting, ranking, joining, and transforming unstructured data. Existing semantic query processing systems invoke request-centric LLM serving systems that are unaware of the query plan, leaving substantial performance opportunities unused. This paper introduces relational LLM serving, an abstraction that makes LLM serving aware of semantic query structure while preserving query semantics and output accuracy. The key opportunity is pipelined execution across semantic operators: when intermediate tuples flow directly from one operator to the next, their KV-cache state can be reused instead of recomputed.
  We present Kalypso, a relational LLM serving system that exposes an API for semantic query plans and executes them using an adaptive, memory-aware scheduling algorithm. Kalypso addresses a new online scheduling problem in which pipelined operator execution is coupled with GPU memory pressure management to reuse KV-cache state in the serving engine before eviction. Its scheduler continuously adjusts memory allocations to balance upstream parallelism, downstream progress, and GPU utilization. Our evaluation shows that Kalypso improves query completion time over baselines using request-centric LLM serving, with speedups up to 4.57x across diverse workloads, demonstrating that query-aware LLM serving can substantially improve the efficiency of semantic query execution.
