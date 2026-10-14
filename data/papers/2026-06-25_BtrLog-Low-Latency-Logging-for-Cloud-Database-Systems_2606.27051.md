# BtrLog: Low-Latency Logging for Cloud Database Systems

- arXiv ID: `2606.27051v1`
- Authors: Maximilian Kuschewski, Lam-Duy Nguyen, Matthias Jasny, Tobias Ziegler, Viktor Leis, Muhammad El-Hindi
- Published: 2026-06-25
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.DC`
- Links: [abs](http://arxiv.org/abs/2606.27051v1) | [pdf](https://arxiv.org/pdf/2606.27051v1)

## Abstract

Cloud database systems cannot rely on instance-local disks for write-ahead logging (WAL) durability, forcing WAL onto remote storage. Existing options are unsatisfying: remote block storage like EBS is easy to adopt but adds substantial write latency and cost, while object storage offers excellent durability and low storage cost but is impractical for OLTP due to high latency and per-append cost. Many cloud-native databases, therefore, depend on purpose-built logging backends, which are typically proprietary and tightly coupled to engine-specific replication and recovery protocols, limiting reuse. We present BtrLog, a reusable cloud logging service that combines low-latency durable appends with low-cost archival for the common single-writer architecture. BtrLog replicates log records across a quorum of SSD-backed log nodes in a single network round trip, reducing sensitivity to stragglers in commit latency. To minimize storage cost, log nodes archive records to object storage as large segments, which are written asynchronously and off the latency-critical write path. In our evaluation, BtrLog achieves lower latency than EBS and enables higher end-to-end transaction throughput when integrated into a DBMS.
