# JetStream: Generating Verified Query Accelerators for Existing Database Systems

- arXiv ID: `2610.20527v1`
- Authors: Akhilesh Balasingam, Amadou Ngom, Geoffrey X. Yu, Tim Kraska
- Published: 2026-10-14
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.20527v1) | [pdf](https://arxiv.org/pdf/2610.20527v1)

## Abstract

Recent work has shown that LLMs can synthesize highly specialized database systems for fixed workloads, but these systems replace the DBMS's native storage and assume static data: users must migrate their data, often give up ad-hoc queries, and lose acceleration once the data changes. We present JetStream, which instead generates query-specific accelerators that extend an existing DBMS. Given a set of parametrized query templates, a staged agentic workflow synthesizes accelerators that run directly over the DBMS's native tables and may maintain custom auxiliary state, while the DBMS remains responsible for storage, transactions, recovery, and all other queries. A fixed, engine-neutral substrate handles engine-specific hooks and keeps auxiliary state transactionally consistent under writes. JetStream generates two kinds of accelerators: tested accelerators, which may use any optimization and are validated by differential testing, and verified accelerators which trade some performance for a machine-checked proof that every answer satisfies a trusted specification derived from the SQL. On TPC-H at SF=20, JetStream achieves a $315 \times$ geomean read speedup over DuckDB ($93 \times$ verified) and retains $120 \times$ under a continuous update stream of 10,000 modified rows per second.
