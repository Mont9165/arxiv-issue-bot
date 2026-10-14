# Does ISO-Grounded NFR Specification Improve LLM Code Generation? A Comparison of Rich and Structured Interventions against a Natural-Language Baseline

- arXiv ID: `2608.13742v1`
- Authors: Joào Pedro Monteiro Pereira, Vinicius Cardoso Garcia
- Published: 2026-08-13
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2608.13742v1) | [pdf](https://arxiv.org/pdf/2608.13742v1)

## Abstract

In LLM-based code generation, Non-Functional Requirements (NFRs) are often specified as terse one-line phrases. We ask whether grounding those specifications in ISO/IEC 25010 Quality Model, either as rich natural-language prose (NL-rich) or as structured JSON (Structured), improves code generated on HumanEval/HumanEval-ET compared to a RobuNFR-style one-line baseline (NL-simple). We evaluate four NFRs (performance, error handling, code smell, readability) with ten prompt variations per condition under a fixed model snapshot and paired non-parametric analysis. Primary finding: ISO-grounded enrichment improves static quality proxies (unreadability density falls across all four NFRs (e.g., Performance 0.88 -> 0.69 for NL-rich)) and reduces sensitivity to prompt wording, but does not reliably improve functional correctness; for error handling, extended-test pass rate decreases, suggesting tension between defensive coding patterns and exact-output benchmarks. Secondary finding: when ISO content is held constant, NL-rich and Structured differ negligibly in correctness (|delta| <= 0.023), indicating that semantic content matters more than JSON-vs-prose format. Practitioners should invest in standard-grounded NFR content rather than serialization form. A fully traceable replication package is provided.
