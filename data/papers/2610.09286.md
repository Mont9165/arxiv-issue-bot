# No Trace, No Claim: Two Contracts for Database Agents

- arXiv ID: `2610.09286v1`
- Authors: Xiaofei Zhang
- Published: 2026-10-07
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.09286v1) | [pdf](https://arxiv.org/pdf/2610.09286v1)

## Abstract

LLM agents can generate database operations and explain their results, but current interfaces often leave a gap between generated plans, execution conditions, and claims presented to users. We argue that agent-facing data systems need two enforceable contracts. A plan contract defines what an agent may execute and reference; an evidence contract records the belief state, completeness, and provenance under which a result supports a claim.
  We instantiate these contracts in TGMS, a bi-temporal graph system in which an LLM plans over a fixed temporal operator interface. A static verifier checks plans before execution, and a claim verifier checks typed claims against content-addressed traces. Live model runs exposed two failures missed by input-only schemas and value-only grounding: nonexistent result fields and page-local counts reported as complete-result counts. Result-field checking makes the first a repairable rejection. Completeness propagation detects the second in all 15 controlled cases and misses all 15 when disabled.
  On the frozen CollegeMsg workload, TGMS reaches 0.408 typed-answer accuracy versus 0.064--0.284 for the evaluated baselines. On Bitcoin-OTC, direct SQL over the same bi-temporal store matches TGMS, showing no universal accuracy advantage for the fixed operator interface. On correction probes, TGMS and bi-temporal SQL answer historical-belief questions, while latest-state baselines cannot. Before claim gating, 21 of 220 answers contain an unsupported gated claim; after gating, none of 199 emitted answers does, at the cost of 21 fewer answers. The plan contract makes invalid plans rejectable and execution reproducible under recorded conditions, while the evidence contract makes gated claims faithful to cited evidence. Neither guarantees correct interpretation of user intent.
