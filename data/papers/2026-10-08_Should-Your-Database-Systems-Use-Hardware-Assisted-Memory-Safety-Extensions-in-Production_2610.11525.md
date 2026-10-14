# Should Your Database Systems Use Hardware-Assisted Memory Safety Extensions in Production?

- arXiv ID: `2610.11525v1`
- Authors: Ilya Meignan--Masson, Martin Fink, Masanori Misono, Dimitrios Stavrakakis, Pramod Bhatotia
- Published: 2026-10-08
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.11525v1) | [pdf](https://arxiv.org/pdf/2610.11525v1)

## Abstract

Database systems are predominantly developed in unsafe languages (e.g., C/C++) to meet performance requirements through low-level memory management, yet this reliance renders them prone to systemic memory-safety issues that compromise reliability, consistency, security, and durability. Through an extensive bug analysis of prominent database systems, we show that these memory-safety issues persist in production environments despite advancements in database testing tools. While emerging hardware-assisted extensions, such as Arm's Memory Tagging Extension (MTE) and CHERI, offer a promising mitigation path for memory safety, their practical applicability and performance overhead within the specialized constraints of database systems remain largely unexplored.
  In this paper, we evaluate hardware extensions through the lens of what we define as the database trilemma: the fundamental trade-off between safety, performance, and portability, to determine their viability for production-grade database systems. We provide the first side-by-side comparison of MTE and CHERI across a database workload suite. Our bottom-up study spans microarchitecture, the compiler/runtime/OS stack, core data structures (ART, B+Tree, hash table, skip list, linked list, and queue), and full database systems (Redis, LevelDB, SQLite, MySQL, DuckDB, and LadyBugDB) to characterize their performance, safety guarantees, and ease of adoption.
  We find that while hardware extensions can offer near-deterministic protection, they introduce non-uniform performance taxes: MTE provides high portability with modest overheads (~10%), while CHERI delivers superior safety guarantees with higher performance penalties (20-60%) and significant porting effort. Our study equips database systems architects with an actionable guide toward building the next generation of reliable, secure databases using hardware-assisted safety mechanisms.
