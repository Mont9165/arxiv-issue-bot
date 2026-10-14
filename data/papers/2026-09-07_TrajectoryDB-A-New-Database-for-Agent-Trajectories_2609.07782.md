# TrajectoryDB: A New Database for Agent Trajectories

- arXiv ID: `2609.07782v1`
- Authors: Yunjia Zheng, Juncheng Yang
- Published: 2026-09-07
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2609.07782v1) | [pdf](https://arxiv.org/pdf/2609.07782v1)

## Abstract

AI agents generate rich execution trajectories that capture their interactions with large language models, tools, and external environments. These trajectories are increasingly valuable for downstream tasks such as memory extraction, model fine-tuning, runtime optimization, and security and cost monitoring. Yet trajectory data today is fragmented across files, databases, and observability systems, with no persistent data management system designed around its unique structure and access patterns.
  We argue that trajectories should be treated as a distinct data type. A trajectory combines hierarchical execution structure, large volumes of text whose analysis often requires semantic reasoning, and rich dependencies and lineage among events, intermediate states, and derived artifacts. These properties introduce new requirements throughout the data lifecycle. Ingestion must reconstruct and preserve execution structure and lineage; storage must efficiently organize large but highly redundant contexts while maintaining relationships among records; and query processing must jointly reason over structure, temporal order, semantics, and lineage.
  We therefore envision TrajectoryDB, a trajectory-native data management system that co-designs ingestion, storage, and query processing to efficiently manage and analyze agent execution trajectories.
