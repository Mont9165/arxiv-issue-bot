# Natural Language Access to Domain-Specific Metadata: A Reusable Framework for LLM Query Generation

- arXiv ID: `2607.18029v1`
- Authors: Blake G. Fitch, Cato Elia Kurtz
- Published: 2026-07-20
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.18029v1) | [pdf](https://arxiv.org/pdf/2607.18029v1)

## Abstract

Researchers need to answer ad-hoc questions about the contents of domain-specific archives but often lack the expertise to write structured queries on the metadata. We show that when domain vocabulary and semantics are captured in a well-designed Web Ontology Language (OWL) ontology, Large Language Models (LLMs) can generate accurate structured queries zero-shot, without fine-tuning, retrieval augmentation, or multi-agent orchestration. We present the Natural Language Knowledge Graph Query (NLKGQ) system, a framework and development process that enables natural language access to metadata in such archives. The framework includes a web interface that helps researchers pose natural language questions, which a domain-agnostic harness translates to SPARQL via an LLM and executes against a knowledge graph. The development process begins with capturing domain vocabulary and semantics in a formal OWL ontology. Domain-specific code then extracts metadata from archive sources and imports it into a knowledge graph defined by the ontology. Both are designed for reuse across domains. We demonstrate the system on metadata derived from a large-scale neuroimaging research archive, evaluating multiple LLMs and ontology representations. The best configurations achieve 100% accuracy on a competence and regression question set developed with domain experts. An ablation study across eight ontology representations reveals that readable entity names and semantic annotations are the dominant factors in accuracy, more significant than model choice or prompt engineering. We also compare SPARQL to an auto-generated SQL database as query backends, showing that OWL's structural features provide a substantial advantage over SQL DDL for LLM-driven query generation. Our demonstration domain also requires local LLMs on modest institutional hardware to address privacy concerns for human subject data.
