# Q&A on Any Spreadsheet Requires Interpreting Its Grid Structure

- arXiv ID: `2609.20732v1`
- Authors: Zofia Smoleń
- Published: 2026-09-17
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.20732v1) | [pdf](https://arxiv.org/pdf/2609.20732v1)

## Abstract

Semantic cell annotation improves chunking interpretability for spreadsheets in LLM-driven RAG systems, aiding answer generation through enriched context rather than improved retrieval accuracy. We propose a novel framework of splitting any spreadsheet into interpretable chunks using cell role annotation. Our framework beats the state of the art, yet it faces a hard ceiling. Spreadsheets are fundamentally two-dimensional unstructured data with continuous relationships and infinite potential cell roles. Because classification models are restricted to finite, pre-defined classes, they cannot perfectly capture this structural nuance, even with human-level annotation. We show that addressing the spreadsheet-to-LLM bottleneck requires moving beyond discrete cell classification. Instead, the field must develop dimensionality-reduction techniques to directly flatten 2D unstructured spreadsheets into 1D unstructured text. Text chunks would be easier for downstream RAG to interpret and generate from.
