# EnSI-RAG: Entity-Structure-Indexed Retrieval-Augmented Generation for Long-Document Question Answering

- arXiv ID: `2608.21252v1`
- Authors: Xuanyu Meng, Jiashuo Sun, Jash Rajesh Parekh, Jiawei Han
- Published: 2026-08-21
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.AI`, `cs.DB`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2608.21252v1) | [pdf](https://arxiv.org/pdf/2608.21252v1)

## Abstract

Question answering (QA) over long, connected documents remains challenging because relevant evidence may span multiple entities and their relationships. Existing retrieval-augmented generation (RAG) methods typically index documents as raw chunks and retrieve them through embedding similarity. Their performance degrades when chunk boundaries separate entities from supporting evidence or when a question requires multi-hop reasoning across the corpus. We propose EnSI-RAG (Entity-Structure-Indexed Retrieval-Augmented Generation), a framework that constructs a query-independent, entity-centered index. Each record (e, t, k, v) represents an entity e, its type t, a semantic category k in {property, relation, aspect}, and a value v, while retaining links to the original source passages. At query time, these records serve as retrieval handles, and an LLM synthesizes the retrieved passages into the final answer. This design separates evidence localization from answer synthesis while preserving traceable source evidence. Across Loong and Oolong, EnSI-RAG achieves an average accuracy of 78.24. Relative to the published baseline scores used as references, this is 6.62 points higher, suggesting its effectiveness across these settings. The code is available at https://github.com/RamonMeng/EnSI-RAG.
