# Leveraging Resolved Incident History for LLM-Assisted Software Bug Diagnosis

- arXiv ID: `2607.21911v1`
- Authors: Boyuan Guan, Hailu Xu, Jamie Rogers
- Published: 2026-07-24
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.DL`
- Links: [abs](http://arxiv.org/abs/2607.21911v1) | [pdf](https://arxiv.org/pdf/2607.21911v1)

## Abstract

Effective software bug diagnosis requires two ingredients: the right knowledge source (operational failure history, not just system documentation) and the right retrieval structure (structured records, not unstructured chunks). Current retrieval-augmented generation (RAG) approaches fall short on one or both dimensions. We propose Operational Memory RAG (OM-RAG), which indexes resolved issues as structured symptom-root cause-resolution triples and retrieves the most similar historical precedent via single-hop embedding. OM-RAG powers a purpose-built large language model (LLM) administrator that has operated a production Dataverse instance for over six months, operationalizing the Knowledge component of the Monitor-Analyze-Plan-Execute-Knowledge (MAPE-K) feedback loop with the system's own resolved failure history. In a controlled four-configuration ablation, LLM-based judging covers all 1,172 issues and manual verification a 123-issue subset. OM-RAG achieves Diagnosis Accuracy of 0.931 and Fix Correctness of 0.809, outperforming chunk-based retrieval (+186%) and a documentation-anchored concept graph (+77%). Model-free retrieval metrics (mean similarity 0.880) independently corroborate the ranking.
