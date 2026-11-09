# Logical Scalability in Big Data Architectures: Impact of Data Modeling on the Database Layer

- arXiv ID: `2611.09346v1`
- Authors: Rosario Napoli, Mark Adrian Gambito, Antonio Celesti, Maria Fazio
- Published: 2026-11-06
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.09346v1) | [pdf](https://arxiv.org/pdf/2611.09346v1)

## Abstract

In modern Big Data architectures, scalability is often addressed through infrastructural expansion, involving vertical or horizontal scaling to manage growing data volumes. However, this hardware-centric perspective overlooks the logical scalability of the storage layer. A central challenge lies in how data modeling choices affect the storage layer of big data architectures. Specifically, when the data model is misaligned with the underlying query patterns, performance bottlenecks emerge and persist regardless of the available computational resources. This paper investigates the concept of logical scalability by conducting a comparative performance analysis of Document, Graph and Multi-Model database paradigms under varying workloads, queries and dataset scales. Our results demonstrate that performance degradation caused by model misalignment cannot be mitigated by additional computational resources alone. Increasing the number of machines while retaining a structurally inadequate data model yields performance equivalent to or worse than a single-machine configuration, as distributed coordination overhead compounds the inefficiencies of the underlying logical model. We demonstrate that efficiency is maximized when the logical structure of the database aligns with the inherent nature of the data and the intended analysis scope, a condition that proves to be more decisive than any infrastructural scaling strategy.
