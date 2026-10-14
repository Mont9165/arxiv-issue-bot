# Cost-Governed RAG: Unified Per-Tenant Cost Attribution Across Retrieval and Generation in Multi-Tenant LLM Systems

- arXiv ID: `2607.12188v1`
- Authors: Navnit Shukla
- Published: 2026-07-13
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.DB`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2607.12188v1) | [pdf](https://arxiv.org/pdf/2607.12188v1)

## Abstract

Enterprise Retrieval-Augmented Generation (RAG) deployments face a critical governance gap: while LLM generation cost is metered per token, the retrieval layer - vector memory, similarity compute, and embedding API calls - remains an unattributed shared cost, enabling invisible cross-subsidization among tenants. We present Cost-Governed RAG, an architecture that integrates a codebook-oblivious vector index (TurboVec) with a multi-tenant LLM governance gateway, creating a unified observability stack where embedding, retrieval, and generation costs are jointly attributable per tenant. The architecture exploits TurboVec's deterministic, closed-form memory formula to enable near-exact per-tenant retrieval cost calculation - a property unavailable in graph-based indexes with non-linear memory overhead. Deployed on Snowpark Container Services within a cloud data platform's governance boundary, the system achieves 99.96% end-to-end cost attribution accuracy across 100 simulated tenants (10M vectors, log-normal size distribution) with telemetry overhead below 0.04% of query latency. The architecture reduces retrieval infrastructure cost by 3.1-9.0x compared to managed vector database services under the pricing assumptions detailed in Section IV. We formalize a three-layer cost model and demonstrate that codebook-oblivious quantization enables deterministic per-tenant cost attribution while also removing the shared-codebook leakage surface present in trained quantizers - the latter observation being exploratory and subject to the limitations described in Section VII.
