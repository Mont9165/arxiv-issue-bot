# Beyond Fixed Fault Models: Comparing LLM-Based and Rule-Based Fault Injection in OpenStack

- arXiv ID: `2609.08681v1`
- Authors: Giuseppe De Rosa, Pietro Liguori, Domenico Cotroneo
- Published: 2026-09-08
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.08681v1) | [pdf](https://arxiv.org/pdf/2609.08681v1)

## Abstract

Software Fault Injection (SFI) supports testing of cloud systems by introducing software defects and observing their manifestation. Rule-based injectors such as ProFIPy provide controlled and reproducible source-level mutations but require fault patterns to be encoded manually. Large Language Models (LLMs) offer a data-driven alternative by generating context-dependent software faults. We compare two code LLMs, Qwen2.5-Coder and DeepSeek-Coder, with ProFIPy in OpenStack's Nova and Cinder services. On shared injection targets, activation and observable-failure rates are comparable, but operational profiles differ: LLM-generated faults produce more Catastrophic outcomes on Nova, whereas ProFIPy produces more Silent and Multi-component effects. The sampled LLM outputs also differ in how they manifest failure, while showing greater agreement in their propagation scope. These findings show that LLM-based fault injection extends the behavioral coverage of fixed fault models without establishing general superiority, and that practical adoption still requires controlled generation, runtime validation, system-level oracles, and reproducible experimental provenance.
