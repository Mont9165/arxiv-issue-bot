# ANCHOR: A Vision for Secure Persistent Key-Value Stores in Disaggregated Data Centers

- arXiv ID: `2608.27819v1`
- Authors: Viraj Thakkar, Dongha Kim, Hokeun Kim, Zhichao Cao
- Published: 2026-08-28
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2608.27819v1) | [pdf](https://arxiv.org/pdf/2608.27819v1)

## Abstract

Persistent key-value stores (PKVS) are increasingly deployed in disaggregated settings that split compute, memory, and storage across separate server pools. This shift redraws the trust boundary: data that would remain within a single machine is now transported, cached, and rewritten across multiple hosts, expanding exposure to both network attackers and intra-infrastructure adversaries.
  This paper presents ANCHOR, a vision for end-to-end integrity and freshness in disaggregated PKVS. ANCHOR proposes a two-part semantics-aware architecture: 1) Persistence path: ANCHOR outlines encrypting and authenticating PKVS persistent files and preventing rollback with manifest versioning. 2) Volatile path: ANCHOR treats caches, indexes, and filters as untrusted hints unless accompanied by verifiable provenance, enforced by a TEE-resident policy. Finally, we outline key invariants and discuss enclave-friendly batching and asynchronous I/O to amortize verification without undermining disaggregation's performance and elasticity benefits.
