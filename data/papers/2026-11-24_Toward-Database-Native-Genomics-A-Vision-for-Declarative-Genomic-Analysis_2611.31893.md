# Toward Database-Native Genomics: A Vision for Declarative Genomic Analysis

- arXiv ID: `2611.31893v1`
- Authors: Dhruv Aron, Danial Saleem, James Christopher Sorenson, Xiangyao Yu
- Published: 2026-11-24
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.31893v1) | [pdf](https://arxiv.org/pdf/2611.31893v1)

## Abstract

In recent years, numerous advancements in relational database management systems (RDBMS), including cloud-native and GPU-native paradigms, have resulted in highly competitive RDBMS performance for analytical workloads. At the same time, the field of genomics has evolved into a data-intensive domain owing to the advent of next-generation sequencing; however, current genomic analysis workflows are often file-based, fragmented, and reliant on disparate tools, limiting their expressiveness, usability, performance, and scalability. This work argues for an incremental adoption of RDBMS and declarative SQL querying in genomic analysis, particularly tertiary analysis. By translating common tasks from widely-used tools like SAMtools and BEDtools into SQL queries executed in DuckDB, we demonstrate that off-the-shelf RDBMS can match or exceed the performance of existing tools while offering significant improvements in expressiveness and usability. We identify current limitations and propose practical paths forward, aiming to position relational databases as a foundational platform for modern bioinformatics workflows.
