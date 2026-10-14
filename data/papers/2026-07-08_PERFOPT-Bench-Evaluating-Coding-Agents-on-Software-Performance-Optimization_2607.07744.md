# PERFOPT-Bench: Evaluating Coding Agents on Software Performance Optimization

- arXiv ID: `2607.07744v1`
- Authors: Yingyun Cui, Yi Xie, Piaohong Wang, Jiawei Ma, Bo Liu, Liangliang Cao
- Published: 2026-07-08
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.07744v1) | [pdf](https://arxiv.org/pdf/2607.07744v1)

## Abstract

Coding-agent benchmarks have largely measured whether agents can produce functionally correct patches, but production software also demands measurable speedups on real execution targets. Performance optimization is a distinct agentic task: agents must profile executions, diagnose cross-layer bottlenecks, edit code without breaking correctness, and verify that gains are reproducible rather than measurement artifacts. We introduce PERFOPT-Bench, a benchmark for evaluating this full performance-engineering loop. Each task provides a correct but deliberately suboptimal codebase and asks the agent to improve a target performance metric; scoring requires hidden correctness tests, verified-speedup measurement, and trajectory-level audit. We evaluate 7 agent stacks with different LLMs and agent frameworks on 7 long-horizon optimization tasks. The results show that optimization performance is workload-dependent rather than determined by model identity alone: no single stack dominates, and changing the agent framework can materially change the same LLM's per-task speedup profile. We further find that raw speedup is unsafe as a benchmark score, since some large gains arise from benchmark-specific shortcut exploitation; an exploratory relay pilot suggests that restarting from an externalized optimization summary can recover additional headroom after an initial session stops. The benchmark and our evaluation are available at: https://anonymous.4open.science/r/Dataset-D3CC.
