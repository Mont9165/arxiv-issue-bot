# Efficiently Linking Unstructured Data for Multi-step Reasoning

- arXiv ID: `2609.19491v1`
- Authors: Jiaming Liang, Haydn Jones, Jacob R. Gardner, Mark Yatskar, Zachary Ives
- Published: 2026-09-16
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.19491v1) | [pdf](https://arxiv.org/pdf/2609.19491v1)

## Abstract

Modern LLMs and AI agents increasingly support data engineering workflows that integrate evidence from unstructured sources. Such pipelines typically do data retrieval, integration, and ranking before proceeding to more complex agentic reasoning or actions, e.g., for scientific discovery. The core retrieval problem in these workflows jointly executes multi-attribute filtering, multi-vector search, exact relational joins, and thresholded embedding-similarity joins. Given a planned query and monotone scoring function, our DASE query engine constructs and ranks candidate evidence tuples. It comprises (i) a multi-step reasoning query model over structured predicates, multiple vectors, and relational links; (ii) SemJI, a sparse materialized embedding-similarity join index for rare near-neighbor pairs; and (iii) a co-designed execution layer that combines predicate-aware ANN traversal, batched access, and threshold-based score aggregation.
  On scientific-discovery workloads, DASE retrieves candidate evidence for multi-step reasoning queries 6x to 46x faster than strong RDBMS, rerank, and vector-database baselines at comparable recall; and for tasks that require semantic-operator post-processing, DASE acts as a high-recall prefilter that makes downstream LLM evaluation both cheaper and more accurate -- e.g., on SemBench E-Commerce it improves BigQuery quality from 0.67 to 0.80 while cutting cost from $2.42 to $0.54.
