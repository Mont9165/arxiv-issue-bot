# Is Agent Memory a Database? Rethinking Data Foundations for Long-Term AI Agent Memory

- arXiv ID: `2605.26252v1`
- Authors: Abdelghny Orogat, Essam Mansour
- Published: 2026-05-25
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.26252v1) | [pdf](https://arxiv.org/pdf/2605.26252v1)

## Abstract

Long-running AI agents need persistent memory. Memory supports learning across sessions, reduces repeated context injection, and enables auditing of past decisions. Current agent memory systems and database paradigms treat memory as storage. They localize correctness at records, embeddings, or edges. Each supplies only some of the capabilities that long-term memory requires. The result is four recurring failure modes: unregulated growth, missing semantic revision, capacity-driven forgetting, and read-only retrieval. In our vision, long-term agent memory is a new data-management workload. Its correctness is a property of the state trajectory, not of individual records. We formalize this as Governed Evolving Memory (GEM). GEM replaces record-level database operations with four state-level operators: ingestion, revision, forgetting, and retrieval. Six correctness conditions govern how the state evolves. Three structural observations establish that no record-level system can satisfy these conditions, regardless of the storage model. We realize the abstraction in MemState, a prototype on a property-graph backend. MemState validates feasibility and exposes the gap to a native engine. We outline three research directions that define memory-centric data management as a workload.
