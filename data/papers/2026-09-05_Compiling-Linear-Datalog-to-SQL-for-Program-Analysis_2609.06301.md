# Compiling Linear Datalog to SQL for Program Analysis

- arXiv ID: `2609.06301v1`
- Authors: Amir Shaikhha, Anna Herlihy, Hung Ngo
- Published: 2026-09-05
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2609.06301v1) | [pdf](https://arxiv.org/pdf/2609.06301v1)

## Abstract

Datalog is a declarative query language that has proven highly effective for expressing static program analyses. Although Datalog has deep roots in database theory, most recent advances have largely emerged from the programming languages and compiler communities, with systems such as Soufflé. In contrast, modern relational engines have made significant progress in optimizing recursive SQL.
  This paper revisits the connection between Datalog and relational databases, advocating recursive SQL as a backend for Datalog evaluation. We present a compilation framework that translates Datalog programs, particularly those in the Linear Datalog fragment, into equivalent recursive SQL queries. To bridge the gap between Datalog and SQL, the compiler routes every program through an intermediate language called Midlog. The compiler additionally recovers functional dependencies from the program and exposes them as schema keys, unlocking the engine's standard query optimizations. This approach enables existing database engines to execute a broad class of program analyses, outperforming the Soufflé engine by up to an order of magnitude on the Umbra backend. Umbra achieves a geometric-mean speedup of 5.46$\times$ at 8 threads, whereas DuckDB is competitive with Soufflé single-threaded and is slower at 8 threads (geometric-mean speedup of 0.68$\times$). Furthermore, the generated SQL is portable; it runs on seven database systems without any engine modification. Our results highlight what the relational engines require to fully support Datalog for large-scale program analysis.
