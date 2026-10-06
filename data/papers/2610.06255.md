# LLM Non-Determinism in Deterministic Processes: A Controlled Variation Space for Constraining the Propagation of Non-Determinism

- arXiv ID: `2610.06255v1`
- Authors: Paul Darius Mandl, Peter Mandl, Martin Häusl
- Published: 2026-10-05
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.06255v1) | [pdf](https://arxiv.org/pdf/2610.06255v1)

## Abstract

Large Language Models are increasingly used in software development processes that rely on defined states, rules, and approvals. This creates a tension between the flexibility of LLMs and the need for reliable and traceable process states. We introduce Controlled Non-Determinism, a process-oriented approach that allows variation without letting it directly determine the authoritative process state. We place LLM-based processing within a controlled variation space that is bounded by a Deterministic Envelope. Before execution, we define the process-relevant properties of the result and the exit conditions. We also record the task configuration. These elements remain fixed during execution. At the end of the variation space, an exit check determines whether the result satisfies the predefined conditions and may become the next authoritative state. Different runs may produce different admissible results while the transition to an authoritative state remains controlled. We illustrate the approach with regulated software development and derive design guidelines for LLM-based changes whose results can be checked before they become part of the authoritative software state.
