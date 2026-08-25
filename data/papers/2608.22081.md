# W-RAG: Source-Aware Retrieval for Enterprise Document Generation from Heterogeneous Knowledge Bases

- arXiv ID: `2608.22081v1`
- Authors: Hridya Dhulipala, Rajesh Ombase, Michael Wang, Tien N. Nguyen
- Published: 2026-08-22
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2608.22081v1) | [pdf](https://arxiv.org/pdf/2608.22081v1)

## Abstract

Retrieval-Augmented Generation (RAG) enables large language models to incorporate external knowledge during generation, improving factual grounding and domain adaptability. However, existing RAG pipelines assume that evidence retrieved from multiple repositories can be ranked globally using a single similarity function. While suitable for open-domain retrieval, this assumption breaks down in enterprise document generation, where heterogeneous knowledge bases (such as policies, regulations, technical documentation, and departmental guidelines) serve distinct roles and must be jointly represented in the generated document. As a result, global ranking often produces unbalanced context dominated by a subset of sources, leading to incomplete enterprise drafts. To address this limitation, we propose W-RAG, a source-aware retrieval framework that performs ontology-guided retrieval, local ranking within each knowledge base, and source-level weighting to regulate evidence composition. We further introduce a new dataset for retrieval-grounded enterprise document generation spanning multiple document types and industry domains. Experiments show that standard RAG pipelines struggle on this task, while W-RAG significantly improves document coverage and generation quality.
