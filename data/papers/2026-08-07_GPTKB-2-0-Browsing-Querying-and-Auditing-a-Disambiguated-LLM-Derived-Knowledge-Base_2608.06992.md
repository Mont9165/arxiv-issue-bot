# GPTKB 2.0: Browsing, Querying, and Auditing a Disambiguated LLM-Derived Knowledge Base

- arXiv ID: `2608.06992v1`
- Authors: Yujia Hu, Tuan-Phong Nguyen, Simon Razniewski
- Published: 2026-08-07
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.06992v1) | [pdf](https://arxiv.org/pdf/2608.06992v1)

## Abstract

We present a web demo for exploring a large-scale disambiguated knowledge base (KB) materialized from a large language model (LLM). GPTKB 2.0 contains 38.4M triples over 1.6M canonical entities, together with 207.6K consolidated relations and 66K consolidated classes. Unlike prior LLM-derived knowledge bases that largely identify entities by surface strings, GPTKB 2.0 performs context-guided disambiguation during recursive KB construction, separating homonyms and merging synonymous mentions as facts are elicited. The demo makes this process inspectable: users can browse entities, follow links across the KB, and audit the provenance of individual facts, including surface forms, candidate matches, source triples, and disambiguation decisions. The interface further supports structured SPARQL queries, natural-language questions translated to SPARQL, and entity linking from user-provided text to canonical GPTKB 2.0 entries. GPTKB 2.0 is available at https://gptkb.org/, with the full KB downloadable for offline use.
