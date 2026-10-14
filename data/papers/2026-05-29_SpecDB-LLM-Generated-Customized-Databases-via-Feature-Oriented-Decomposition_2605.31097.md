# SpecDB: LLM-Generated Customized Databases via Feature-Oriented Decomposition

- arXiv ID: `2605.31097v1`
- Authors: Yunkai Lou, Longbin Lai, Shunyang Li, Zhengping Qian, Ying Zhang
- Published: 2026-05-29
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.31097v1) | [pdf](https://arxiv.org/pdf/2605.31097v1)

## Abstract

Mainstream relational databases ship a uniform feature set across deployments, although individual workloads exercise only a fraction of the available subsystems. We investigate whether a database can instead be generated on demand with a feature set matched to the target workload. We present SpecDB, a system that uses large language models (LLMs) to synthesize customized relational databases. We survey 9 production systems and decompose them into 10 functional modules, each further divided into implementation variants. To capture cross-module dependencies, including cases where implementations in disjoint subtrees must be co-designed, we adopt the FODA feature model and extend it with a cooperate edge, yielding a dependency graph DBGraph. SpecDB operationalizes DBGraph through a layered module-construction pipeline in which each module is generated, validated, and integrated by a dedicated subagent (driven by three inner agents: Main, Tester, Architect), and a Refining Agent that iteratively repairs and tunes the assembled database against a user-supplied refining harness with read-only access to existing database source code. A companion selection component translates a natural-language workload description into a set of implementation variants, providing an end-to-end pipeline from workload description to deployable database. We evaluate SpecDB on TPC-C with BenchmarkSQL. The generated database (23,779 lines of Rust) completes 60-minute TPC-C at 1 and 10 warehouses with zero errors. At 10 warehouses it reaches tpmC=130, compared to 128 for PostgreSQL and 127 for MySQL, with comparable latency at ~3% of their code size. Because the agent operates at module-specification level rather than product source, it can in principle combine techniques across system boundaries. Paired with falling LLM costs, generating a purpose-built database for a target workload is becoming straightforward.
