# Shoonya: Zero-Socket In-Process Small Language Models for Graph Databases with Schema-Epoch KV Caching, Live Catalog Logit Masking, and Verifier-Advantage Distillation

- arXiv ID: `2611.28502v1`
- Authors: Madhulatha Mandarapu, Sandeep Kunkunuru
- Published: 2026-11-21
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.LG`, `cs.PF`
- Links: [abs](http://arxiv.org/abs/2611.28502v1) | [pdf](https://arxiv.org/pdf/2611.28502v1)

## Abstract

Coupling a property-graph database to an external language-model server imposes a three-part socket tax: serialization overhead dwarfing microsecond graph reads, repeated prefill of verbose schemas, and blind decoding divorced from the live catalog and multi-version concurrency control (MVCC) engine. We present Shoonya, from-scratch commercially clean (0.0% non-commercial or share-alike data) tri-modal (Python, Rust, OpenCypher) small language models (16.8M to 1.07B parameters) co-designed with shoonya-infer, a zero-dependency pure-Rust runtime embedded inside the samyama-graph-enterprise address space. Direct GraphStore references unlock three database-native primitives: (1) an epoch-invalidated SchemaPrefixCache over a copy-on-write PagedKvArena accelerating warm CPU time-to-first-token by 4.91x--13.68x with O(1) DDL invalidation; (2) a 36 us columnar catalog and source-span logit mask enforcing valid ontology identifiers and verbatim spans; and (3) a sub-65 us read-only MVCC gate serving Tier-0 queries inside 389.8 MiB INT8 RSS (59.8--67.9 tok/s) with 0.0% hallucination leak. Rank-factorized tied embeddings (-74.5% vocabulary weights), atomic indentation tokens (0/421 indentation errors), 4:1 grouped-query attention with 2:1 cross-layer KV sharing (-93.75% INT8 KV memory), Warmup-Stable-Decay training, KnOTS SVD merging, Step-GRPO, and Rust Jacobi SVD governance keep 100% of layers heavy-tailed ($α\in [1.88, 2.20]$). Finally, we synthesize nine lessons across v0.1--v1.0, resolving a Reverse-Token-Density Distillation Trap via teacher scaling and zero-VRAM Verifier-Advantage-Gated Knowledge Distillation (AdvKD), recovering +13.61 MBPP points (33.07%) while reaching 100% validity on enrichment, grounded extraction, and tool planning.
