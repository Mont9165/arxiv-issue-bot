# ArcadeDB in Python: An In-Process Multi-Model Database

- arXiv ID: `2611.07971v1`
- Authors: Taewoon Kim
- Published: 2026-11-05
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2611.07971v1) | [pdf](https://arxiv.org/pdf/2611.07971v1)

## Abstract

Some Python workflows need transactional reads and writes over documents, traversals over a graph, and similarity search over vector embeddings. In practice these are split across separate systems (a document store, a graph engine, and a vector index), and the data is copied between them and kept consistent by application code. ArcadeDB is an open-source multi-model database engine, written in Java, that supports all three access patterns and can be embedded in a host process. We present arcadedb-embedded, a Python package that runs ArcadeDB inside the Python process via JPype, using a Java Runtime Environment bundled in the wheel. One pip install gives a database with documents, a property graph, and vector search, and needs no Java installation. Query results can be returned as Python lists, NumPy arrays, pandas DataFrames, or Arrow tables. We demonstrate a hybrid retrieval workflow that chains vector search, SQL filtering, and graph traversal over one dataset. We benchmark arcadedb-embedded against SQLite, DuckDB, LadybugDB, and Chroma, and report its costs.
