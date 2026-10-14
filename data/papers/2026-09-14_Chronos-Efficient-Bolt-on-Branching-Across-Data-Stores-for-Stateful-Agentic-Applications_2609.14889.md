# Chronos: Efficient Bolt-on Branching Across Data Stores for Stateful Agentic Applications

- arXiv ID: `2609.14889v1`
- Authors: Xinjing Zhou, Jason Mohoney, Samuel Madden, Michael Stonebraker, Lei Cao
- Published: 2026-09-14
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2609.14889v1) | [pdf](https://arxiv.org/pdf/2609.14889v1)

## Abstract

Data-centric applications increasingly use speculative execution to explore multiple candidate paths where each path modifies state distributed across heterogeneous data stores. This trend is intensified by the rise of tool-calling agents. Hence, applications need data systems that can create branches quickly, isolate state-modifying paths, and merge changes consistently across stores without imposing substantial query overhead. Existing systems provide only partial support, forcing applications to coordinate branches and merges manually, which increases overhead and risks inconsistent cross-store state.
  To solve this problem, we introduce Chronos, a bolt-on system that provides branching capability across heterogeneous data stores. We make two contributions. First, Chronos introduces a compact interval-based versioning technique that enables efficient branching and data sharing through simple query rewrite. Second, Chronos introduces a bolt-on architecture that separates branch management from data path within each store. Combined with interval-based versioning, this separation provides atomic cross-store visibility for merges and enables Chronos to support diverse data stores without modifying their engines.
  We implement Chronos for PostgreSQL, SQLite, DuckDB, Qdrant, and a DBMS-backed filesystem. We evaluate it using cross-store agent workflows, MCTS-style exploration, and per-store benchmarks. Chronos runs MCTS-style exploration up to 16.7x faster than existing approaches while maintaining practical query performance across the underlying stores. Under concurrent cross-store workflows, Chronos prevents partially visible merges while substantially outperforming serialized execution.
