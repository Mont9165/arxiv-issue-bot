# Trace2Tower: Transition-Aware EigenTrace Induction of Multi-Level Skills for LLM Agents

- arXiv ID: `2609.05261v1`
- Authors: Jiazheng Sun, Boyu Yang, Binhao Yuan, Mingxuan Li, Xin Peng
- Published: 2026-09-04
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.05261v1) | [pdf](https://arxiv.org/pdf/2609.05261v1)

## Abstract

Large language model agents increasingly rely on execution traces to master complex interactive tasks. However, current paradigms are bottlenecked by shallow trajectory retrieval and flat skill summarization, fundamentally ignoring the temporal dependencies and outcome-conditioned topology of agent behavior. We introduce Trace2Tower, a transition-aware EigenTrace framework that distills raw trajectories into a robust skill hierarchy. Trace2Tower abstracts step-level interactions into canonical events, constructing a unified graph governed by semantic compatibility, transition dynamics, and outcome evidence. Through a novel contrastive spectral decomposition, it isolates stable, success-aligned behavioral modes while rigorously suppressing failure-prone shortcuts. These modes organically populate a dynamic skill tower of action templates, procedural routines, and overarching task strategies, continuously refined via verifier-guided feedback. On ALFWorld, Trace2Tower achieves 87.31% success requiring only 10.35 steps and 0.26 invalid actions; on WebShop, it reaches 50.67% exact success. Across both benchmarks, Trace2Tower significantly outperforms existing baselines in task mastery and context-efficient experience reuse.
