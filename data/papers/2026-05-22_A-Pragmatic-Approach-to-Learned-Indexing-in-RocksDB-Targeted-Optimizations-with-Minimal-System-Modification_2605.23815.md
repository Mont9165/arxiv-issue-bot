# A Pragmatic Approach to Learned Indexing in RocksDB: Targeted Optimizations with Minimal System Modification

- arXiv ID: `2605.23815v1`
- Authors: Shubham Vashisth, Olivier Michaud, Bettina Kemme, Oana Balmau
- Published: 2026-05-22
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.DC`
- Links: [abs](http://arxiv.org/abs/2605.23815v1) | [pdf](https://arxiv.org/pdf/2605.23815v1)

## Abstract

Learned indexes have emerged as a promising alternative to traditional index structures, offering higher throughput and lower memory usage by approximating the cumulative key distribution function with lightweight models. Despite these benefits, adoption in production systems remains limited, partly because learned indexes that support concurrency and persistence as effectively as, e.g., the B+-Tree, do not yet exist, while many research prototypes introduce substantial complexity. In this paper, we investigate whether off-the-shelf learned indexes can be integrated into a production database with minimal storage-engine redesign. Using RocksDB as a case study, we exploit its separation between in-memory Memtables and immutable on-disk files to deploy specialized indexes at each level. We show that directly applying existing learned indexes is insufficient under write-heavy workloads because frequent Memtable replacement prevents models from fully adapting. To address this, we introduce a reuse mechanism that preserves structural knowledge across Memtable instances. At the storage level, we replace RocksDB's disk index with a learned index without modifying the storage layer or read path. We further adapt a read-only learned index to be block-aware, enabling worst-case single-I/O lookups. We implement these techniques in MountDB, an extension of RocksDB. Experiments on large-scale workloads with diverse data distributions and access patterns show up to 1.5X higher write throughput and 2.1X higher read throughput than state-of-the-art systems, demonstrating that established learned indexes can be integrated into production systems with minimal overhead and substantial performance benefits.
