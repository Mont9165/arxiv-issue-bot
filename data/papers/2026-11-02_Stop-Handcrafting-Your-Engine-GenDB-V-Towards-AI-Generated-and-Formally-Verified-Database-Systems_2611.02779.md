# Stop Handcrafting Your Engine! GenDB-V: Towards AI-Generated and Formally Verified Database Systems

- arXiv ID: `2611.02779v1`
- Authors: Jiale Lao, Immanuel Trummer
- Published: 2026-11-02
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`, `cs.CL`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2611.02779v1) | [pdf](https://arxiv.org/pdf/2611.02779v1)

## Abstract

For over 50 years, the database community has developed a wide range of successful engines to answer two fundamental questions: how can database systems run faster, and how can we ensure their correctness? Experience with these engines shows that performance depends on hardware and workloads. As both change over time, we repeatedly redesign and rebuild database systems, a time-consuming and expensive process. Correctness remains another long-standing challenge: recent studies continue to uncover wrong-answer bugs even in mature database engines, despite years of development and testing. To address these, we present GenDB-V, a system that enables AI agents to synthesize database engines specialized to hardware and workloads for performance, and formally verified for correctness. GenDB-V supports specialized implementations of SQL templates and general-purpose engines that accept any query within a supported SQL subset. First, we develop SQLSpec to formalize SQL semantics and deterministically construct fixed, implementation-agnostic synthesis targets. Second, we enable joint synthesis of fast code and formal proofs through storage--execution co-optimization, performance-first exploration, and three-layer modular proofs that bridge low-level execution to SQLSpec semantics. Third, we verify the synthesized code and proofs against the fixed synthesis targets in an isolated pipeline, proving SQL correctness and program safety. We evaluate GenDB-V on TPC-H and SEC-EDGAR. For verified template implementations, GenDB-V achieves geometric-mean speedups of 22.0-61.3x over DuckDB and Umbra. For a verified general-purpose engine, GenDB-V also achieves speedups of 1.27-3.4x on TPC-H. GenDB-V also achieves better performance than a testing-based LLM synthesis method, while our audit and tests expose incorrect answers in that method's implementations for 16 of 28 templates.
