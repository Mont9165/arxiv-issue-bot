# WaRP: Workload-Aware Request Planning for Vector Retrieval on Object Storage

- arXiv ID: `2610.29689v1`
- Authors: Ruipeng Wan, Xinyu Zeng, Yiming Qiao, Huanchen Zhang
- Published: 2026-10-21
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.29689v1) | [pdf](https://arxiv.org/pdf/2610.29689v1)

## Abstract

Modern vector search systems keep payload vectors in cloud object storage and only a compact routing index on fast local storage, typically using cluster-based ANN indexes. This design inherits a problem existing systems do not address. On object storage, small Range-GETs have latency dominated by fixed per-request overhead and are billed per request. Existing readers either issue one request per probed cluster, or coalesce adjacent ranges with hand-tuned gap or span thresholds that do not transfer across datasets or query workloads.
  We formulate the grouping of probed-cluster byte intervals into object-store requests as a global per-query optimization problem and present WaRP, a workload-aware request planner that solves it efficiently. Given the sorted byte intervals, a limit on the number of requests per query, and an estimate of how many object-store requests from one query can proceed concurrently under the target serving configuration, WaRP searches for a merge plan that minimizes a concurrency-aware latency surrogate while satisfying the request limit. Using an optimized dynamic program and adaptive frontier search, WaRP returns a plan within $(1{+}ε)$ of the optimum, with per-query planning overhead under $10$ms even in the most demanding tested settings. A lightweight offline reordering pass further improves request mergeability without changing the semantics of ANN search.
  We implement WaRP inside Lance's I/O scheduler and evaluate it on AWS S3. We build IVFPQ indexes on seven datasets, including SIFT100M and DEEP100M at the 100M-vector scale. WaRP + Reorder improves QPS by $1.09--3.48\times$ and reduces GETs by $2.12--5.19\times$ relative to Lance, while preserving Lance's recall.
