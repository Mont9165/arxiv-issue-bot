# LLM-Assisted Verification in Dafny

- arXiv ID: `2611.16886v1`
- Authors: Wieger Wesselink, Kees Huizing, Huub van de Wetering
- Published: 2026-11-12
- Primary category: `cs.LO`
- Categories: `cs.LO`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.16886v1) | [pdf](https://arxiv.org/pdf/2611.16886v1)

## Abstract

Formal verification of complex algorithms requires expertise in program specification, invariant construction, mathematical proof, and the management of automated theorem provers. Although large language models (LLMs) can generate program code and proof fragments, reliably developing complete machine-checked verifications remains challenging: it requires an iterative process of constructing and validating specifications and invariants, building proofs, diagnosing solver failures, and optimizing verification performance. This paper presents a systematic ten-step workflow for LLM-assisted verification of scientific algorithms using the Dafny verification system. The workflow integrates algorithm formalization, contract development, empirical invariant validation, proof construction, bottleneck profiling, and resource-driven proof optimization. We applied the workflow using Antrhopic's Claude Opus 5 and Opus 5.5 models, combining LLM-driven development with automated testing and verification feedback, while retaining human oversight for correctness-critical decisions and strategic interventions. We evaluate the approach on 37 complex algorithms from graph theory and labelled transition systems. Notably, we verified the Hopfcroft-Tarjan triconnectivity test, demonstrating that even highly challenging algorithmic verification tasks can be carried out through a structured LLM-assisted workflow. Many of our machine-checked verifications were obtained within hours to a few days of interactive development. Our results suggest that LLM-assisted workflows can shift the role of the human verifier from detailed proof construction toward supervision, specification review, and strategic guidance.
