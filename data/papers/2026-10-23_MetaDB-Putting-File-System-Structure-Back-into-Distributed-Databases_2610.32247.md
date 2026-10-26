# MetaDB: Putting File-System Structure Back into Distributed Databases

- arXiv ID: `2610.32247v1`
- Authors: Zebin Ren, Biao Cao, Kang Chen, Zhihui Yin, Qiushi Chen, Jielong Jian, Jiwei Xiong, Xinxing Wang, Yan Xing, Liguo Duan, Ran Zheng, Xianjun Meng, Zhenyu Hou
- Published: 2026-10-23
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.DC`
- Links: [abs](http://arxiv.org/abs/2610.32247v1) | [pdf](https://arxiv.org/pdf/2610.32247v1)

## Abstract

Storage systems in production increasingly rely on distributed databases for metadata management, yet our experience at Baidu shows that treating a general-purpose database as a black box leaves substantial performance and efficiency untapped. File-system metadata exhibits directory-tree locality, differentiated consistency requirements, and clustered deletions that general-purpose databases largely ignore. We thus propose MetaDB, a metadata-aware distributed transactional database that serves as the shared metadata layer for Baidu's large-scale storage systems. MetaDB addresses three key mismatches between general-purpose databases and metadata workloads: Data Model Mismatch, Transaction Model Mismatch, and Storage Implementation Mismatch. To bridge these gaps, MetaDB combines (1) tree-topology-induced sharding and execution, (2) semantic-aware off-critical-path processing, and (3) a lifecycle-aware storage engine with in-memory MVCC and locality-aware compaction. MetaDB achieves 2.2x-4.1x the throughput of our previous general-purpose database and halves the number of metadata machines. Deployed in production at Baidu for over five years, MetaDB unifies metadata management across the company's storage fleet and scales to over 1,000 metadata nodes, tens of trillions of metadata records, and exabyte-scale storage in a single cluster.
