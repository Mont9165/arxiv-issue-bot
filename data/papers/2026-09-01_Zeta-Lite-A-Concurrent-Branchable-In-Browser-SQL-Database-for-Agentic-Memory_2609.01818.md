# Zeta-Lite: A Concurrent, Branchable In-Browser SQL Database for Agentic Memory

- arXiv ID: `2609.01818v1`
- Authors: Gene Zhang
- Published: 2026-09-01
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.01818v1) | [pdf](https://arxiv.org/pdf/2609.01818v1)

## Abstract

The browser has become a first-class database host: applications increasingly want to store, query, and reason over structured data entirely on the client - for privacy, offline operation, local-first collaboration, and, most recently, as durable memory for in-browser AI agents. One way to get SQL in the browser, compiling PostgreSQL to WebAssembly (PGlite), inherits PostgreSQL's process model: a single backend connection that executes one statement at a time and blocks. That model cannot express concurrent transactions, and it leaves richer capabilities - graph queries, database branching - to whatever the compiled server happens to include. We present zeta-lite, the browser form factor of the Zeta database engine: a WebAssembly build that compiles the same Zeta server down to a 2.87 MB gzipped artifact. Zeta-lite keeps the engine's log-centric asynchronous MVCC core, which yields two capabilities no other in-browser SQL engine provides. First, overlapping snapshot-isolated transactions on a single thread: multiple transactions hold distinct read/commit timestamps and interleave, with snapshot-isolation conflict detection between them. Second, copy-on-write database branching - whole-database fork, merge, and rebase - is unique in a browser SQL database and rare even in servers. On top of these, zeta-lite exposes a feature-complete PostgreSQL surface (joins, CTEs, window functions, JSONB with GIN indexes, full-text search, HNSW vector search, SQL/PGQ graph queries, multi-database) and snapshot-to-OPFS durability. Across Chrome, Firefox, and a native reference runtime, zeta-lite sustains 268k-315k point reads/s and holds a mixed read/write workload flat over millions of operations. This small, fully-featured, concurrent SQL database is an especially good fit for agentic memory - where cheap branchable state lets an agent explore, inspect, and commit or discard speculative work.
