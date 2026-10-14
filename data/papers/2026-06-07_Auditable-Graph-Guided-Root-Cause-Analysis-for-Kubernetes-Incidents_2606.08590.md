# Auditable Graph-Guided Root Cause Analysis for Kubernetes Incidents

- arXiv ID: `2606.08590v1`
- Authors: Anastasiia Kuvshinova, Seungmin Jin
- Published: 2026-06-07
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.DC`
- Links: [abs](http://arxiv.org/abs/2606.08590v1) | [pdf](https://arxiv.org/pdf/2606.08590v1)

## Abstract

Kubernetes incidents are diagnosed reliably only when a root-cause system's reported gains come from incident evidence rather than scenario-specific shortcuts. We present Graph Traversal Agent, a graph-guided RCA agent that combines LLM reasoning with specialized tools. The model reasons over a typed evidence graph, while deterministic graph and tool operations collect evidence, bound the search, and check proposed verdicts. We map operational constraints, including read-only evidence collection, propagation-aware diagnosis, bounded execution, and independently validated verdicts, to a typed incident graph, a LangGraph traversal state machine, and a separate validation stage. On ITBench snapshots scored by one fixed qwen-plus judge, the audited system raises root-cause-entity F1 over an earlier iteration of the same system from 0.6087 to 0.9130 on a 23-scenario common subset. A prompt-level ablation separates prompt-tuned gains from gains that survive once scenario-specific hints are removed: the stripped-prompt configuration retains 0.6958 F1 on a 19-scenario subset. The surviving gain concentrates on ChaosMesh scenarios whose ground-truth root cause is the injected fault object already present in the evidence graph, so we report it as benchmark-coupled rather than broad cross-cluster RCA evidence. Lightweight checks, including same-judge comparison, prompt-level ablation, cascade-source checking, and a telemetry no-leak test, mark claims as supported, pending, or out of scope. We scope the work to ITBench OpenTelemetry-demo snapshots. Live-cluster trials served as an engineering stress test, but alert state and trace availability did not stay stable enough for controlled scoring, so we make no production-readiness or mean-time-to-repair claim.
