# Discovery-Driven Integration of Disjoint Tables via Text

- arXiv ID: `2609.26658v1`
- Authors: Md Ataur Rahman, Dimitris Sacharidis, Oscar Romero, Sergi Nadal
- Published: 2026-09-22
- Primary category: `cs.IR`
- Categories: `cs.IR`, `cs.CL`, `cs.DB`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2609.26658v1) | [pdf](https://arxiv.org/pdf/2609.26658v1)

## Abstract

Integrating heterogeneous datasets within data lakes is a critical challenge, particularly for semantically related tables that lack the explicit attributes needed to be joined. We study Discovery-Driven Integration, where the relevant sources and their missing relational structure must be discovered before integration. In this setting, unstructured text provides the evidence that connects otherwise disjoint tables. The fundamental challenge is to discover the relationships at a fine-grained level that connect individual rows from different tables through specific sentences. We formalize this task as Text-Mediated Join Path Discovery and propose a horizontal bidirectional cross-attention architecture called LOKI Latent-space Optimization for Knowledge Integration) that learns contextualized representations of table rows and sentences. Through a global table-text contrastive objective, fine-grained row-sentence associations emerge without explicit local supervision. Existing multi-modal discovery methods largely retrieve coarse-grained column-text associations, whereas integration systems assume supplied row-text links, schemas, or queries. LOKI instead transforms these implicit associations into explicit, interpretable join paths, organizes them into relation-consistent groups, and materializes them as typed integrated tables with sentence-level provenance. Comprehensive evaluations on real-world benchmarks demonstrate that LOKI consistently outperforms state-of-the-art multi-modal data discovery approaches, and materializes typed integrated tables with 0.982 macro typed-pair precision while being up to 40 times cheaper in LLM API cost than direct prompting.
