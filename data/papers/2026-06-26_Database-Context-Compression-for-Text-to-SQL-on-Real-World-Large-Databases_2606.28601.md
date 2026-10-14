# Database Context Compression for Text-to-SQL on Real-World Large Databases

- arXiv ID: `2606.28601v1`
- Authors: Jingwen Liu, Weibin Liao, Xin Gao, Junfeng Zhao, Yasha Wang
- Published: 2026-06-26
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.28601v1) | [pdf](https://arxiv.org/pdf/2606.28601v1)

## Abstract

Recent progress in Text-to-SQL has been driven by stronger language models and prompting strategies, yet performance on real enterprise benchmarks such as Spider 2.0 and BIRD remains far below that on classical academic datasets. We argue that the main bottleneck is no longer reasoning, but database representation. Real databases contain repeated audit columns, large groups of similar tables, opaque identifiers whose meanings are stored only in documentation, and extensive data dictionaries with little query-relevant information. Existing query-aware methods, including schema linking and retrieval-based schema selection, filter this raw context but still operate on redundant and verbose representations. We reformulate the problem as database context compression, a query-agnostic transformation that rewrites schemas, semantic descriptions, and external documentation into a compact representation. We formalize this transformation with the SGCF (Support-Gain Component Factorization) principle, which unifies repeated column extraction, isomorphic table templating, semantic componentization, and evidence purification under a single coverage objective. Based on SGCF, we propose DBCC, a database-side middleware that performs offline structural and semantic compression together with lightweight online evidence purification. DBCC is model-agnostic and can be integrated into existing Text-to-SQL pipelines. On Spider 2.0-Snow and BIRD, DBCC reduces input context by up to two orders of magnitude (from 2.6M to 34.7K tokens on the largest Spider 2.0-Snow subset), improves schema-linking strict recall from 0% to 56.5% under DeepSeek-V3.2 (63.1% under Claude Opus 4.7), and consistently increases end-to-end execution accuracy by 1.8-1.9% over three recent Text-to-SQL systems. Our code is open-sourced at https://github.com/MrBlankness/SchemaCompression.
