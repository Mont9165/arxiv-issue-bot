# Diversifying to Verify: When Task-Equivalent Programs Differ in Verifiability

- arXiv ID: `2607.09366v1`
- Authors: Shirley Yu, Ruben Martins
- Published: 2026-07-10
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.LO`
- Links: [abs](http://arxiv.org/abs/2607.09366v1) | [pdf](https://arxiv.org/pdf/2607.09366v1)

## Abstract

Program verification is crucial for software correctness, but producing fully verified programs remains difficult in practice. This paper studies whether implementation structure affects automated verifiability when multiple generated programs are intended to satisfy the same task-level semantics.
  We present Diversify2Verify, a staged LLM-based pipeline for Why3 that infers representation-specific contracts, generates and tests diverse recursive and imperative array/list implementations, and attempts verification with bounded verifier-guided annotation repair. We also construct a verification-oriented benchmark of 73 tasks over integers, arrays, and lists, yielding 292 implementation variants. Diversify2Verify verifies 96 artifacts initially and 154 after two repair passes, improving artifact-level verification from 32.9% to 52.7%. At the task level, at least one variant verifies for 49 of 73 tasks, a 67.1% success rate. These results show that task-equivalent implementations can differ substantially in verifiability and that implementation diversity helps find verification-friendly artifacts.
