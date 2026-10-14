# The Case for Single-Version Concurrency Control in the Cloud

- arXiv ID: `2610.15793v1`
- Authors: Lam-Duy Nguyen, Gabriel Haas, Muhammad El-Hindi, Viktor Leis, Philip A. Bernstein
- Published: 2026-10-11
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.15793v1) | [pdf](https://arxiv.org/pdf/2610.15793v1)

## Abstract

Multi-version concurrency control (MVCC) has been the dominant concurrency protocol in modern database management systems (DBMSs). However, cloud-native HTAP architectures shift many of MVCC's traditional advantages from the primary transaction engine to the deployment architecture. Now, transactional and analytical processing are decoupled into loosely synchronized engines, while cloud deployment primitives provide the workload isolation required for this design. In this paper, we challenge the status quo, arguing that single-version concurrency control (SVCC) is better suited to cloud transaction processing than MVCC. Through a systematic analysis of MVCC's limitations, we show that SVCC avoids these shortcomings through a more lightweight and efficient design. Beyond arguing for a lighter transaction processing, we use this SVCC effort as a blueprint to advocate for a broader rethinking of cloud-native architectures and to outline a research roadmap to shape next-generation DBMSs.
