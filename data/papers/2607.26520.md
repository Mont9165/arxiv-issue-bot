# A Graph-Native Bitemporal Memory Store for Conversational AI Agents

- arXiv ID: `2607.26520v1`
- Authors: Alp Niksarli, Gopesh Baheti
- Published: 2026-07-29
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2607.26520v1) | [pdf](https://arxiv.org/pdf/2607.26520v1)

## Abstract

Conversational AI agents commonly lack persistent memory across sessions. The obvious fixes like injecting full chat histories into the context window, or delegating to a third-party memory service, either exhaust the model's context budget or send personal data through infrastructure the user does not control. We describe a memory store that avoids both problems: an agent-local Neo4j property graph augmented with HNSW vector indexes and a full bitemporal data model. Each memory is stored as an immutable identity node linked to versioned content nodes carrying two closed-open time intervals: valid time (when the fact was true in the world) and transaction time (when the database recorded it). This design supports point-in-time semantic retrieval without physically overwriting history. Semantic edges between related memories are maintained automatically at write time using cosine similarity over 1024-dimensional embeddings. We evaluate the system on LongMemEval, a 500-question benchmark spanning six question types designed to stress long-term memory. Across 60 sampled questions, the current-state semantic search path achieves 46.7% R@10 overall, rising to 80% on knowledge-update questions. The time-travel path yields 80% R@10 on knowledge-update but decreases recall on temporal-reasoning questions (50% to 37.5%), a consequence of post-filter dilution that points directly to a concrete design improvement. We discuss what these results reveal about the limits of pure retrieval for different question types and what each failure mode suggests for future work.
