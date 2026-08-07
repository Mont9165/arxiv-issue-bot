# The Prover Is the Judge: Verified Security Software from AI Coding Agents in Ada/SPARK

- arXiv ID: `2607.14340v1`
- Authors: Tobias Philipp
- Published: 2026-07-15
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2607.14340v1) | [pdf](https://arxiv.org/pdf/2607.14340v1)

## Abstract

AI coding agents produce code faster than humans can review it. In our approach, the prover is the judge of whether the code is correct. Under a verifier-driven loop, AI agents wrote and verified bare-metal security software in Ada/SPARK spanning classical and post-quantum cryptography, TLS 1.3, IKEv2, X.509, and a Matrix client. GNATprove discharged 49,280 proof obligations, established functional correctness for selected primitives, and proved the absence of run-time errors for the rest, at roughly 20-40 times lower supervision cost than comparable hand verification. GNATprove alone was insufficient: some defects could not be detected and were resolved using known-answer tests, interoperability, or human review of specifications. Given weak checks, the agent tried to bypass them and reported success. We report where each layer caught faults and draw the central lesson: what an agent can be trusted to establish is bounded by the strength of its feedback.
