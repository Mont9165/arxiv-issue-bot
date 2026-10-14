# DBA-Bench: A Production-Fidelity Benchmark for LLM-Based Database Operations Agents

- arXiv ID: `2607.22165v1`
- Authors: Junming Chen, Junyang Jiang, Xu Chen, Zibo Liang, Kai Zheng
- Published: 2026-07-24
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`, `cs.CL`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2607.22165v1) | [pdf](https://arxiv.org/pdf/2607.22165v1)

## Abstract

LLM-based database agents show promise, but differing task scopes, testbeds, and metrics hinder comparison. We identify four gaps between evaluation and production operations: live-environment fidelity (multi-turn read-write interaction with a running database); observation-space scale and complexity (causal diagnosis across thousands of time series, business logs, and concurrent activity); solution-space openness (multiple remediations with different operational trade-offs); and scenario complexity and coverage (faults cascading across internal mechanisms and operational domains). We present DBA-Bench, a benchmark addressing these gaps through production fidelity, outcome-first evaluation, and controlled scenario reproducibility. It uses instrumented PostgreSQL environments with active workloads, persistent state, and multi-source observations; defines success by measurable recovery or fault elimination under safety constraints; and restores snapshots with scenario-specific checks before each run. The benchmark contains 106 scenarios across seven task domains, with two public difficulty labels based on reference-path diagnostic depth and environmental complexity. We evaluate nine baseline groups, including six foundation-model systems, two GPT-5.5-backed database agents, and a Human DBA reference. Across 848 automated runs, Diagnosis, Outcome, and Safe Pass rates are 32.7%, 19.6%, and 12.4%; the best automated baseline reaches 17.9% Safe Pass versus 93.4% for the Human DBA reference. Automated Safe Pass falls from 19.6% on Easy scenarios to 7.6% on Hard scenarios, underscoring the difficulty of safe end-to-end remediation.
