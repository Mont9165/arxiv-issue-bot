# QuarkDB: A Hybrid Database System for Quantum Data Management

- arXiv ID: `2611.20807v1`
- Authors: Wenrui Zhang, Yu Wang, Xiao Zhang
- Published: 2026-11-16
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AR`
- Links: [abs](http://arxiv.org/abs/2611.20807v1) | [pdf](https://arxiv.org/pdf/2611.20807v1)

## Abstract

Emerging quantum applications like quantum communication generate large volumes of high-dimensional quantum data, requiring efficient data analysis and storage. However, classical database systems often struggle to meet requirements such as quantum processing or version management. This paper presents QuarkDB designed for efficient quantum data management. QuarkDB establishes a unified object model for relational and quantum data and defines the syntax of Quantum Structured Query Language. To support efficient quantum data management, QuarkDB integrates three key components: (1) a Hybrid Query Engine with cost-based hybrid plan selection over classical and quantum operators, (2) an Execution Engine with a three-level instructions intermediate representation, QuarkDB-IR, to support quantum execution and reduce quantum processing costs, and (3) a Storage Engine supporting quantum data version management, state reconstruction and data reuse. Compared with classical databases such as SQLite and PostgreSQL or quantum databases like Qute, our QuarkDB achieves query-latency speedups ranging from 2.14x to 25.86x speedup under extensive real-world workloads.
