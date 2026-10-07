# Mechanizing Transactional Anomalous Patterns for Weak Isolation Levels

- arXiv ID: `2610.07665v1`
- Authors: Long Gu, Si Liu, Hengfeng Wei
- Published: 2026-10-06
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.07665v1) | [pdf](https://arxiv.org/pdf/2610.07665v1)

## Abstract

Recently proposed transactional anomalous patterns (TAPs) provide a semantic characterization of weak isolation levels and serve as the foundation for TAP-based isolation checking. Yet, these characterizations currently exist only as pen-and-paper proofs. We present the first machine-checked formalization of TAPs and their associated weak isolation levels in Rocq. We further establish machine-checked proofs of the corresponding TAP-based characterization theorems. The mechanization process revealed two subtle issues in the original presentation: an underspecified transaction history model and an incomplete TAP characterization of the Read Atomicity isolation level that failed to capture violations of session guarantees. We address these issues by refining the definition of transaction histories and the corresponding TAP definitions, and re-establish all characterization theorems in Rocq. These refinements have further been integrated into the weak isolation checker Plume.
