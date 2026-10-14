# FAIR GraphRAG: A Retrieval-Augmented Generation Approach for Semantic Data Analysis

- arXiv ID: `2607.11464v1`
- Authors: Marlena Flüh, Soo-Yon Kim, Carolin Victoria Schneider, Sandra Geisler
- Published: 2026-07-13
- Primary category: `cs.IR`
- Categories: `cs.IR`, `cs.AI`, `cs.CL`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.11464v1) | [pdf](https://arxiv.org/pdf/2607.11464v1)

## Abstract

Retrieval-Augmented Generation (RAG) addresses the limitations of Large Language Models (LLMs) when providing responses to domain-specific questions. Graph-based RAG approaches, such as GraphRAG, enhance retrieval by capturing semantic relationships within knowledge graphs (KGs). While the FAIR principles (Findability, Accessibility, Interoperability, and Reusability) are becoming prevalent for scientific data management, especially in complex domains such as medicine, existing RAG approaches lack a structured FAIRification of the underlying knowledge resources. This lack limits their potential for FAIR information retrieval in these domains. To address this gap, we introduce FAIR GraphRAG, a novel framework that integrates FAIR Digital Objects (FDOs) as the fundamental units of a graph-based retrieval system. Each graph node represents an FDO that incorporates core data, metadata, persistent identifiers, and semantic links. We leverage LLMs to support schema construction and automated extraction of content and metadata from data sources. The framework was co-designed by physicians and computer scientists to ensure technical and clinical relevance. We apply FAIR GraphRAG to a biomedical dataset in gastroenterology, demonstrating its applicability to RNA-sequencing data. Beyond ensuring adherence to the FAIR principles, FAIR GraphRAG significantly improves question answering accuracy, coverage, and explainability, particularly for complex queries involving metadata and ontology links. This work shows the feasibility of combining FAIR data practices with graph-based retrieval techniques. We see potential for applying our approach to other specialized fields such as education and business.
