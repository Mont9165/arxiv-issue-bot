# When the Application Layer Is Disposable: Putting Integrity Constraints Back in the Database

- arXiv ID: `2610.36418v1`
- Authors: Hasara Kalumin, Amol Deshpande
- Published: 2026-10-26
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.36418v1) | [pdf](https://arxiv.org/pdf/2610.36418v1)

## Abstract

Integrity constraints have been central to the relational model since its inception. However, beyond keys, single-row CHECKs, and referential integrity, most constraints are enforced by application layers today. SQL ASSERTIONs, standardized in SQL-92, remain poorly supported by major RDBMSs. This has become increasingly unacceptable due to two developments. First, LLM-driven applications and agents increasingly issue queries and updates directly against databases, bypassing application layers where invariants reside. Such code may be generated on demand and discarded afterwards, making the database the only durable component that can encode and enforce these invariants. Second, natural constraints in higher-level conceptual models, such as E/R and property graphs, become fragmented across relations under mappings chosen for performance. The resulting multi-relation constraints lack direct database support, and only some can be efficiently enforced using existing mechanisms such as triggers. These developments motivate an overhaul of how constraints are defined, mined, managed, and enforced in data management systems. As a first concrete step, we introduce constraint indexes, which represent constraints spanning multiple relations as transactional access paths, and implement a proof of concept as a PostgreSQL extension. Constraint indexes enforce constraints arising from distributed inheritance hierarchies, folded relationships, and folded weak entities, as well as cardinality bounds and functional dependencies, at low overhead relative to no enforcement. Across these workloads, they outperform the better of the correctness-preserving baselines by up to 2.41 times. We also show that LLM-driven writers frequently violate unenforced constraints and behave erratically when provided with a list of constraints to enforce. We close by discussing a few research challenges raised by this agenda.
