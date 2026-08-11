# Beyond Tables: Doc2DB-Bench for Relationally Faithful Document-to-Database Construction

- arXiv ID: `2608.08459v1`
- Authors: Zhuowen Liang, Zhengxuan Zhang, Jiayang Wang, Jiazhuo Chen, Nan Tang
- Published: 2026-08-09
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.08459v1) | [pdf](https://arxiv.org/pdf/2608.08459v1)

## Abstract

Practical AI systems increasingly need to turn long, heterogeneous documents into queryable relational databases, not isolated spreadsheets. In domains such as finance, healthcare, education, transportation, and enterprise operations, downstream workflows rely on normalized schemas, entity identities, keys, cross-table relationships, and integrity constraints for analytics, compliance, auditing, and SQL-backed decision making. Existing Document-to-Table benchmarks are insufficient for this setting: flattening evidence into single tables can duplicate entities, obscure many-to-many relationships, create sparse records, and avoid testing whether extracted facts form a valid database instance. This creates an urgent need to evaluate document understanding as database construction rather than field extraction. We introduce Doc2DB-Bench, a benchmark for Document-to-Database construction, containing 203 long-document instances across 42 schemas and seven domain groups, with 117 entity tables, 132 relationship tables, 7,341 rows, and 41,935 cells. Built through a controllable DB-to-Doc synthesis pipeline and organized by a taxonomy of intra-table extraction and inter-table reasoning, the generated documents undergo authenticity verification, proving indistinguishable from real-world references. Doc2DB-Bench thus provides a testbed for reliable, auditable, and relationally faithful LLM-based data systems. The benchmark is publicly available at https://github.com/SetonLiang/Doc2DB-Bench.
