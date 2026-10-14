# GraftDB: Dynamic Folding of Concurrent Analytical Queries

- arXiv ID: `2606.04303v1`
- Authors: Genki Kimura, Kazuo Goda
- Published: 2026-06-03
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.04303v1) | [pdf](https://arxiv.org/pdf/2606.04303v1)

## Abstract

Analytical database systems serve as foundational infrastructure for knowledge discovery across many domains. Day after day, researchers, practitioners, and increasingly AI-driven agents issue analytical queries, inspect their results, and refine their inquiries. An analytical database system thus receives and processes diverse analytical queries that arrive over time and execute concurrently. Such workloads can create redundant execution work across independently issued queries. Exploiting this overlap to optimize query processing as a whole is a critical technical challenge. This paper presents GraftDB, a multi-query execution engine that dynamically folds a later-arriving query into a running execution, reusing previously performed work and sharing subsequently performed work. GraftDB achieves dynamic folding with state-centric execution, which treats operator state accumulated during execution not as owned by a single query, but as shared state that any compatible query can observe or contribute to. Each query observes shared state through a per-query state lens, which lets the query observe that state only after the relevant input has been incorporated and receive only rows or state fragments valid under the query's semantics. For an arriving query, query grafting identifies operator state that already satisfies part of the query's requirements and work that can still be shared to satisfy the rest. Together, these mechanisms let GraftDB share work across overlapping analytical queries and reduce redundant execution work. Experiments using TPC-H-derived instances of dynamic concurrent workloads show that GraftDB achieves up to 2.17 times higher throughput than a same-engine isolated-execution baseline. Under overloaded open-loop arrivals, GraftDB reduces P95 response time to as low as 0.17 times the same baseline's P95 response time.
