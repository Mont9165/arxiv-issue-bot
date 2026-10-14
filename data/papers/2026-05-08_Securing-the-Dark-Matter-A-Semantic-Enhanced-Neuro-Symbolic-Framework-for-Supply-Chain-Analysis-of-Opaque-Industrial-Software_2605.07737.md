# Securing the Dark Matter: A Semantic-Enhanced Neuro-Symbolic Framework for Supply Chain Analysis of Opaque Industrial Software

- arXiv ID: `2605.07737v1`
- Authors: Bowei Ning, Xuejun Zong, Lian Lian, Kan He, Yifei Sun, Yuxiang Lei, Plamen Vasilev
- Published: 2026-05-08
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.07737v1) | [pdf](https://arxiv.org/pdf/2605.07737v1)

## Abstract

Automated vulnerability detection in critical-infrastructure software confronts a fundamental barrier: industrial software is routinely deployed as stripped, symbol-free binaries that deprive conventional Software Composition Analysis of the source-level transparency it requires. Existing binary analysis techniques close this Semantic Gap only partially -- graph-based detectors preserve structural syntax but discard behavioral semantics, while large language models supply rich semantic cues at the cost of unstable, hallucination-prone inference. To address this gap, we present a semantic-enhanced neuro-symbolic framework that reconstructs behavioral semantics directly from opaque binaries and performs tractable global risk reasoning. Three tightly coupled mechanisms drive this capability: (1) abstract interpretation combined with a reflexive prompting pipeline that structurally constrains a local LLM agent, effectively suppressing hallucinations; (2) a surjective transformation that compresses raw Code Property Graphs into typed Software Supply Chain Knowledge Graphs amenable to scalable reasoning; and (3) a domain-adapted Graphormer that captures long-range vulnerability propagation, augmented by embedding-space subgraph matching to uncover zero-day and APT-style attack patterns. Evaluated across three benchmarks of increasing domain specificity, the framework consistently outperforms all baselines on detection accuracy, semantic lifting fidelity, and APT fingerprint matching. Deployment on a hybrid virtual-physical testbed incorporating production-grade hardware from five ICS vendors further confirms strong detection coverage of high-impact CVEs while substantially reducing false-positive rates relative to leading commercial tools.
