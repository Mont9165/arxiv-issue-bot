# Conceptual Schema Inference for Tabular Datasets using Large Language Models

- arXiv ID: `2605.23105v1`
- Authors: Zhenyu Wu, Jiaoyan Chen, Norman W. Paton
- Published: 2026-05-21
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.23105v1) | [pdf](https://arxiv.org/pdf/2605.23105v1)

## Abstract

Large collections of tabular data from data lakes, web tables and open data portals often originate from heterogeneous sources, leading to representational inconsistencies. Understanding and organizing such repositories therefore remains a major challenge. While prior work has primarily focused on dataset discovery and exploration, this paper addresses the complementary problem of conceptual schema inference: automatically deriving a conceptual schema that captures entity types, attributes and inter-type relationships directly from raw tables. We propose two large language model (LLM)-based approaches that use only column headers and cell values: GeSI uses generative LLMs to infer hierarchical types and their attributes from table- and column-level semantics, and to integrate them into a global schema that also captures relationships across types; EmSI employs LLM-based table embeddings to group tables by column-level semantics, infer attributes within each group, and construct hierarchical structures from shared attribute patterns. Finally, we report an experimental analysis demonstrating the effectiveness of our approaches in terms of the conciseness and structural quality of the inferred schema components, their scalability to large repositories, and a case study illustrating end-to-end schema inference.
