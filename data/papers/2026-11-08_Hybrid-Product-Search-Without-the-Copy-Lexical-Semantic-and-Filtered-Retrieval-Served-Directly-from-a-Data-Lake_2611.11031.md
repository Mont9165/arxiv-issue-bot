# Hybrid Product Search Without the Copy: Lexical, Semantic and Filtered Retrieval Served Directly from a Data Lake

- arXiv ID: `2611.11031v1`
- Authors: Raghvendra Yadav, Xiang Fu, Chinmay Soman
- Published: 2026-11-08
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.DB`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2611.11031v1) | [pdf](https://arxiv.org/pdf/2611.11031v1)

## Abstract

E-commerce catalogs increasingly live in lakehouse tables: Apache Iceberg metadata over Parquet files in object storage. Product search, however, still runs on copies of that catalog, in a lexical engine and a vector database, each with its own ingestion pipeline, schema, staleness window and bill. We show that search applications can be hosted directly on the data lake, with the lakehouse table as the single system of record. We extend Apache Pinot, a real-time OLAP engine that already serves Iceberg tables in place, with BM25 relevance scoring over its Lucene text index, corpus-wide term statistics so that scores are comparable across files, and reciprocal rank fusion in plain SQL; a real-time table fed by a stream can sit behind the same table, merged by the broker. On the Amazon ESCI benchmark (1.2M US products, 22,458 test queries), hybrid search served from the lake matches exact retrieval (nDCG@10 .361). The lake table is queryable 149 s after its files are registered, and a lake commit is searchable in 3.8 s, close to indexing directly into a search engine. On a brand-sorted lake of 277M products (0.8 TB), one 16-vCPU node answers brand-scoped vector, BM25 and client-fused hybrid searches in 6.5-9 ms (p50), sustains 1,100 vector and 635 BM25 searches per second at under 180 ms p99, and makes a commit searchable in 4.3 s. Search adds only its indexes: no copy of the catalog, no sync pipeline and no second schema, which cuts storage, rebuild time and the operational work of keeping copies consistent.
