# CoWalk: Cooperative Walks for Agentic Batch Queries on Disk-Resident Graphs

- arXiv ID: `2610.38404v1`
- Authors: Qiao Liang, Zhiguang Chen, Yue Yu, Nong Xiao
- Published: 2026-10-28
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2610.38404v1) | [pdf](https://arxiv.org/pdf/2610.38404v1)

## Abstract

Workloads such as query rewriting, deep research and group-relative policy optimization (GRPO) issue batches of semantically related vector queries. Existing disk-resident approximate nearest neighbor (ANN) systems process these queries independently. On three workloads, 31 to 67 percent of the I/Os of a batch fetch a page that another query of the batch has already fetched. A page cache shared by the batch removes these I/Os, yet it makes a single-thread search only $1.1$ to $1.2{\times}$ faster, because the search time goes to distance computation and the cache does not change the walk of any query. We present CoWalk, which runs the queries of a batch as cooperating walks on one thread. Every query keeps its own candidate list, a page is read once per batch, and the full-precision vector on every fetched page is ranked by every query of the batch. A query therefore reaches the target recall with a shorter candidate list, which computes fewer distances and issues fewer I/Os. At recall@10 of 0.95, CoWalk answers a batch on one thread $1.6$ to $1.9{\times}$ faster than the fastest per-query baseline and issues $2.8$ to $6.9{\times}$ fewer I/Os. On a server it serves $3.0$ to $6.9{\times}$ the throughput of that baseline at a similar batch latency.
