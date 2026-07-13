# SCATE: Learning to Supervise Coding Agents for Cost-Effective Test Generation

- arXiv ID: `2607.08983v1`
- Authors: Sijia Gu, Noor Nashid, Ali Mesbah
- Published: 2026-07-09
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.08983v1) | [pdf](https://arxiv.org/pdf/2607.08983v1)

## Abstract

While autonomous coding agents have significantly advanced automated test generation, they remain fundamentally limited by lazy generation, a phenomenon where agents prematurely terminate tasks and systematically avoid complex programmatic logic, resulting in inadequate code coverage. Currently, mitigating this premature termination requires continuous human-in-the-loop supervision. This heavy reliance on human intuition creates a bottleneck that negates the efficiency gains of automated generation. We propose SCATE, a framework for adaptive, automated supervision of coding agents that replaces human intervention during test generation. By formulating supervision as a contextual bandit problem, SCATE learns to select the most promising testing actions based on the current coverage and class testability metrics, maximizing coverage gains while minimizing wasted generation effort. Our empirical evaluation demonstrates that SCATE integrates seamlessly with different coding agents. When applied to GEMINI-CLI, it achieves 32.3% higher line coverage and 30.9% higher branch coverage than the agent-only baseline. A comparison with CLAUDE CODE confirms the framework dynamically adapts its policy to optimize each agent's unique strengths. SCATE also consistently outperforms state-of-the-art non-agentic approaches across all metrics.
