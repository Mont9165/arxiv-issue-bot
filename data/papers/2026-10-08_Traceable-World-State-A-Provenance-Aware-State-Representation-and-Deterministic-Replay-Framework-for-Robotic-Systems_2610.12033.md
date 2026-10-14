# Traceable World State: A Provenance-Aware State Representation and Deterministic Replay Framework for Robotic Systems

- arXiv ID: `2610.12033v1`
- Authors: Zoe Li
- Published: 2026-10-08
- Primary category: `cs.RO`
- Categories: `cs.RO`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.12033v1) | [pdf](https://arxiv.org/pdf/2610.12033v1)

## Abstract

Robotic systems operating over extended tasks must maintain a world state assembled from observations arriving at different times, with varying confidence and potential revisions. Conventional representations emphasize latest estimates, hindering fact provenance, decision reproduction, or execution auditing. We present Traceable World State (TWS), a middleware-neutral semantic representation and reference runtime for provenance-aware robot world state. A TWS snapshot captures entities, relations, observations, confidence, and revision metadata. Validated update operations transform snapshots immutably, ordered updates support deterministic replay, and a canonical SHA-256 hash chain ensures tamper-evident logs. We evaluate TWS through schema conformance, complete state lifecycles, deterministic replay, and fault injection. Passing 38 tests across Python 3.10-3.14, the framework detects record corruptions, broken hash links, sequence discontinuities, and world mismatches. Across ten public BEHAVIOR-1K task definitions, TWS imported 153 entities and 146 relations with successful validation. On 103 NVIDIA Unitree G1 simulated trajectories containing 78,369 frames, TWS achieved exact terminal-state replay in all episodes and detected 412/412 injected corruptions with a 1.72% storage overhead over Plain JSONL.
