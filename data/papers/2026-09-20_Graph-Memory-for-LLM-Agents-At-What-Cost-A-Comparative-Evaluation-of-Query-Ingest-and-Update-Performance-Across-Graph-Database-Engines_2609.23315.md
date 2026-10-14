# Graph Memory for LLM Agents: At What Cost? A Comparative Evaluation of Query, Ingest, and Update Performance Across Graph Database Engines

- arXiv ID: `2609.23315v1`
- Authors: Donald Nguyen, Gurbinder Gill, Hadi Ahmadi, Christopher J. Rossbach
- Published: 2026-09-20
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.23315v1) | [pdf](https://arxiv.org/pdf/2609.23315v1)

## Abstract

Graph databases are frequently positioned as categorically necessary for connected-data workloads, yet the systems dimension along which they actually differ - query planning, indexing, and data-readiness cost - is rarely isolated from vendor framing. We construct a synthetic, biomedical-shaped property graph (1.02 million nodes, 5.34 million total node and edge rows) and a twenty-query workload spanning neighborhood lookups, bounded paths, set intersections, anti-joins, grouped aggregation, top-k ranking, temporal filters, full scans, and relational joins. We benchmark Corvic AI - a purpose-built columnar query engine underlying Corvic's ontology management layer ("memories")- against seven purpose-built or graph-extension database systems (LoraDB, Ladybug, DuckPGQ, Memgraph, Neo4j, HugeGraph, and FalkorDB) at three graph scales spanning three orders of magnitude. We report query latency geomeans, bulk-ingest throughput, point-update latency, and answer correctness for each system, and we derive a simple total-cost-of-ownership model that expresses the ingest/query trade-off as a function of query volume. Our central finding is that no system in this sample is categorically fastest: a native graph engine (Ladybug) outperforms Corvic AI on narrow, bounded-neighborhood shapes, while Corvic AI is faster on shapes that scan or join a large fraction of the graph, and a system implementing graph query syntax via SQL/PGQ (DuckPGQ) is measurably slower purely due to query-plan choice. The dominant cost differential in our data is not query latency but the cost of making data queryable at all: bulk-ingest throughput varies by three orders of magnitude across engines (5.0k-4.3M rows/s), a gap that a simple crossover-point calculation shows dominates total cost for any workload with fewer than roughly 105 queries per data refresh.
