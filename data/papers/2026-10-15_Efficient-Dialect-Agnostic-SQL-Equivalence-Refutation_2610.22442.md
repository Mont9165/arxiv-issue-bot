# Efficient Dialect-Agnostic SQL Equivalence Refutation

- arXiv ID: `2610.22442v1`
- Authors: Junwen An, Manuel Rigger
- Published: 2026-10-15
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.22442v1) | [pdf](https://arxiv.org/pdf/2610.22442v1)

## Abstract

Identifying semantically inequivalent SQL queries is useful for many applications, such as evaluating Text-to-SQL and dialect translation systems. However, existing approaches often struggle with the diversity of SQL features and dialects, requiring significant manual effort and expertise to extend query feature support across Database Management Systems (DBMSs). To address these limitations, we present SQLWitness, an efficient, DBMS-agnostic query equivalence refutation engine. Our core idea is leveraging the DBMS execution engine to determine whether generated instances constitute counterexamples, thereby faithfully capturing the semantics of the SQL dialect and preventing false counterexamples. To efficiently generate test data, our approach explores a constrained data-generation space and uses an integrity-constraint-aware generation strategy. Furthermore, to guide time-efficient termination of this test-data generation process, we pair predicate-coverage signals with a statistical estimator. We extensively evaluated SQLWitness on six benchmark suites across four SQL dialects. SQLWitness refuted 5.34% to 88.4% more pairs than state-of-the-art baselines, and processed query pairs in 0.12 seconds on average, achieving a speedup from 2.1x to 16.4x over the baselines. Furthermore, in a case study, SQLWitness found 8.4% inconsistent translations within a dialect translation benchmark. We believe SQLWitness could be broadly adopted for many use cases.
