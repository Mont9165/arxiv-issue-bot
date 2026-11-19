# RefinementGuard: Counterexample-Directed Semantic Qualification for Hidden Agent-Tool Execution

- arXiv ID: `2611.23611v1`
- Authors: Adhyayan Veer Singh, Fanjiang Ye, Yuke Wang
- Published: 2026-11-17
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.23611v1) | [pdf](https://arxiv.org/pdf/2611.23611v1)

## Abstract

Tool runtimes can lower an agent-selected operation into a hidden parallel graph, reducing latency and context while risking semantic mistranslation. We introduce RefinementGuard: translation validation for hidden, effectful agent-tool lowerings, coupled to artifact-bound, fail-closed runtime admission. Qualification compares a candidate graph with an independent reference on isolated state using explicit parent-operation obligations. We evaluate two repository-level contracts, bug localization and patch validation, on controlled repositories. Among 100 activated, non-equivalent development/qualification faults adjudicated by one human, parent-semantic validation rejects 49/100 (operator-cluster bootstrap 95% CI [33.7%, 64.8%]). The objective is selective admission, not maximum mutation rejection: exact equality rejects 100/100 faults but also all 60 valid variants, whereas obligation-based validation accepts 60/60; its 51 residual misses identify concrete specification gaps. On a frozen disjoint input split, the held-out B2-B3 result is localization-only because 21 patch mutants fail structurally; B3 rejects 38/56 localization defects. In a controlled asynchronous-delay regime, the localization serial/guarded median-latency ratio is 4.50x, and hidden execution exposes 74.3% less parent-visible context than visible execution. Patch validation shows no demonstrated speedup; zero-delay runs expose overhead. End-to-end qualification thus detects lower-layer misses while preserving localization's parallelism.
