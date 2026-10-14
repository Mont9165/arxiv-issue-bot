# Structure then Query: Enabling Precise Analytical Queries over Unstructured Documents

- arXiv ID: `2608.13384v1`
- Authors: Teng Lin, Yuyu Luo, Nan Tang
- Published: 2026-08-13
- Primary category: `cs.IR`
- Categories: `cs.IR`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.13384v1) | [pdf](https://arxiv.org/pdf/2608.13384v1)

## Abstract

Unstructured documents constitute the majority of enterprise and web data. With the rapid development of large language models(LLMs), researchers have started to build data systems that analyze unstructured textual documents like operating on databases. However, because mainstream retrieval methods still relies on fuzzy matching based on vector similarity, accurately obtaining information and performing structured analysis and reasoning remains a major challenge. To address these limitations, AnnoIndex introduces two core fundamental components. The first is Annotation Index. The system uses a module called SchemaLoop to automatically create hierarchical annotation schemas from the raw corpus, and then uses lightweight language model to extract specific values. It turns scattered unstructured text into a materialized, structured index that enables low-cost filtering and querying. The annotation index avoids the black-box matching of vector similarity and amortizes attribute extraction costs from online queries to a one-time build. The second innovation is a Structured Query Engine. It compiles user questions into execution plans based on SQL extension. It first uses the Annotation Index for precise documents filtering, then gradually applies extraction operations in ascending order of cost, resorting to LLMs only for the remaining minimal fraction of the corpus that require deep semantic understanding. The extracted attributions are merged into the annotation index, reducing the cost of future queries. Experiments on three real-world datasets demonstrate that AnnoIndex consistently outperforms state-of-the-art baselines, achieving the highest average F1 score (0.87) while maintaining robust performance on complex multi-hop join and progressive reasoning queries.
