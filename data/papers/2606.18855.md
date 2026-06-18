# Toward Semantically-Seeded, Graph-Propagated Impact Analysis Across Software Artifacts: A Vision

- arXiv ID: `2606.18855v1`
- Authors: Momil Seedat
- Published: 2026-06-17
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.18855v1) | [pdf](https://arxiv.org/pdf/2606.18855v1)

## Abstract

When a single software artifact changes - a requirement, a configuration value, or a function - engineers must determine what else is impacted. Existing change-impact-analysis (CIA) tooling tends to rely on one of two signals in isolation: semantic similarity recovered from text (information-retrieval traceability, code search, embeddings), or structural dependency following (call graphs, IDE "find usages", test-impact selection). Each has a characteristic blind spot. A semantically driven tool misses an impacted artifact whose text shares no vocabulary with the change; a structurally driven tool misses artifacts related in meaning but not joined by an edge, and most operate only over code rather than the Requirement-Config-Service-Test chain. We argue for a training-free and interpretable analyzer that fuses both signals over the same embeddings. We model the system as a heterogeneous artifact graph with typed edges recovered by static analysis, compute a semantic prior by cosine similarity to the changed artifact, propagate impact multi-hop with decay over a row-normalized propagation matrix, and blend the two with a single tunable weight lambda. A small but complete proof-of-concept on a payment subsystem (5 labelled change scenarios) shows the mechanism we care about: artifacts with zero textual overlap with the change are still recovered through propagation, and helper functions that propagation alone cannot reach are recovered through the semantic layer. The fusion is the only configuration that covers both blind spots, and lambda acts as an explicit precision/recall control. Drawing on four publicly documented production failures, we argue that the same formulation extends to operational artifacts (images, metrics, dashboards, data schemas) that code-only analysis cannot reach.
