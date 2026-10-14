# A Fair Benchmarking of Deep Relational Database Learning Models

- arXiv ID: `2607.03659v1`
- Authors: Kazi F. Akhter, Bharath Ajendla, Manar D. Samad
- Published: 2026-07-04
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.03659v1) | [pdf](https://arxiv.org/pdf/2607.03659v1)

## Abstract

Relational databases (RDBs) are the primary data infrastructure in many enterprises, yet recent deep learning methods designed for RDBs have been evaluated under inconsistent experimental protocols, making fair comparison difficult. We present one of the first systematic benchmarking studies of recently released deep learning methods for RDBs, evaluating them across five relational databases, with one classification and one regression task for each. We refactor all deep RDB models to allow the full range of experimental procedures to be applied consistently across all methods. Our findings indicate that the relational transformer (RT) approach delivers the strongest overall performance on both classification and regression tasks compared to the state-of-the-art graph-based modeling and learning of RDBs. Even for single-table learning tasks, deep learning methods designed for RDBs outperform the leading tabular foundation model, TabPFN 2.5. Extending learning from a single table (hop = 0) to multiple tables (hop = 1, 2) by connecting neighboring tables in relational databases enhances performance, but the additional benefit from higher hops diminishes as computational overhead grows. Deep RDB learning methods have the potential to challenge state-of-the-art tabular foundation models, especially on large-scale enterprise data. The source code for this benchmarking study is publicly available.
