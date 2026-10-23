# Automated Enrichment Analysis with GraphRAG: Efficient Multi-Database ORA Extraction and Biological Interpretation

- arXiv ID: `2610.30710v1`
- Authors: Guangcan Li, Shuyuan Zheng, Jiayao Liu, Shigeto Seno, Makoto Onizuka
- Published: 2026-10-22
- Primary category: `cs.IR`
- Categories: `cs.IR`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.30710v1) | [pdf](https://arxiv.org/pdf/2610.30710v1)

## Abstract

Over-representation analysis (ORA) is widely used to interpret gene-expression studies, but its outputs are often fragmented across gene-set databases and presented as flat term lists that obscure gene-level links among related enrichment signals. We propose Graph-Based Over-Representation Retrieval-Augmented Generation (GBOR-RAG), an integrated and traceable framework for ORA interpretation. GBOR-RAG represents heterogeneous gene-set databases as a unified term--gene knowledge graph, where shared genes connect related terms across sources. After graph-based ORA scoring, the framework retrieves a compact connected evidence subgraph that preserves both cross-database relationships and gene-level support. The subgraph conditions an LLM to generate biological interpretations, and we introduce a claim-level faithfulness metric to assess whether generated claims are supported by explicit evidence. Experiments show that graph-based ORA preserves conventional ORA results with high consistency (mean Pearson $r=0.997$) while reducing query time by a median of $37\times$ (up to $48\times$). The retrieved subgraphs average 36.8 nodes and achieve the highest overall integration score (4.12), and GBOR-RAG attains the highest claim-level faithfulness (0.90) among the compared systems. Adding a PubMed literature layer further improves the overall interpretation quality from 4.17 to 4.75.
