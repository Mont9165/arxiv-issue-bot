# TGMS: An Agent-Native Bi-Temporal Graph Management System

- arXiv ID: `2607.10265v1`
- Authors: Xiaofei Zhang
- Published: 2026-07-11
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.10265v1) | [pdf](https://arxiv.org/pdf/2607.10265v1)

## Abstract

Temporal graph questions require reliable handling of time, identifiers, and arithmetic. Large language model (LLM) agents often fail on these tasks, especially when a graph records both ordinary evolution and later corrections. We present TGMS, a bi-temporal property graph management system that exposes thirteen verified temporal operators as agent tools. Each operator is typed, deterministic, bounded, cost-guarded, and bi-temporal by default. The LLM plans operator calls and writes the final response, while the system performs all graph computation. Numeric, entity, ordering, and pattern claims are checked against the content-addressed execution trace.
  TGMS separates valid time from transaction time. It can therefore answer belief-state questions such as ``as of transaction time $T$, what did the system believe?'' Standard latest-state snapshots and retrieval pipelines do not preserve enough information to answer such questions. On a development benchmark built from a real communication network, TGMS with a 14B open-source model reaches 0.409 exact match. Vector-RAG, static-graph RAG, and text-to-Cypher reach 0.045--0.182 under the same serving setup. TGMS reaches 0.67 exact match on correction probes, while the three 14B baselines score zero. The claim verifier detects all 500 injected count and entity errors with no false positives on the clean answers. Two implementation findings were especially important. First, operator output contracts prevent plans from referring to fields that do not exist. Second, verification must track whether the cited evidence is complete, because correct arithmetic over a truncated result is still misleading. The code, benchmark, and trace viewer are open source under Apache-2.0.
