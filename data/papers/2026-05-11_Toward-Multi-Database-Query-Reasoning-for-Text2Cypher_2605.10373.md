# Toward Multi-Database Query Reasoning for Text2Cypher

- arXiv ID: `2605.10373v1`
- Authors: Makbule Gulcin Ozsoy
- Published: 2026-05-11
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2605.10373v1) | [pdf](https://arxiv.org/pdf/2605.10373v1)

## Abstract

Large language models have significantly improved natural language interfaces to databases by translating user questions into executable queries. In particular, Text2Cypher focuses on generating Cypher queries for graph databases, enabling users to access graph data without query language expertise. Most existing Text2Cypher systems assume a single preselected graph database, where queries are generated over a known schema. However, real-world systems are often distributed across multiple independent graph databases organized by domain or system boundaries, where relevant information may span multiple sources. To address this limitation, we propose a shift from single-database query generation to multi-database query reasoning. Instead of assuming a fixed execution context, the system must reason about (i) relevant databases, (ii) how to decompose a question across them, and (iii) how to integrate partial results. We formalize this setting through a three-phase roadmap: database routing, multi-database decomposition, and heterogeneous query reasoning across database types and query languages. This work provides a structured formulation of multi-database reasoning for Text2Cypher and identifies challenges in source selection, query decomposition, and result integration, aiming to support more realistic and scalable natural language interfaces to graph databases.
