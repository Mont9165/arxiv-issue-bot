# Mining Workflow Graphs for Black-Box Boundary Testing of Conversational LLM Agents

- arXiv ID: `2607.06873v1`
- Authors: Liting Lin, Boxi Yu, Yuzhong Zhang, Lionel Briand, David-Paul Niland, Emir Muñoz
- Published: 2026-07-08
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.06873v1) | [pdf](https://arxiv.org/pdf/2607.06873v1)

## Abstract

Conversational LLM agents can cause real-world harm when their internal workflows fail, such as completing a transaction without confirmation. Testing these state-dependent failures is difficult because critical boundaries, such as identity checks and confirmation gates, are hidden behind multi-turn conversational prerequisites, rendering them inaccessible to standard tests. We present AgentEval, a black-box testing framework that discovers and stresses these stateful boundaries. AgentEval interacts with an agent to mine a \emph{conversational workflow graph}, a model of its behavior. Instead of prompting blindly, AgentEval uses this graph's structure to enumerate specific guards and prerequisites as test targets, replaying the conversational path to a boundary before applying a perturbation. AgentEval then executes each test, determining whether it passes or fails using only the conversation turns. We benchmark AgentEval against a privileged, white-box auditor with access to the agent's underlying source code, which AgentEval never sees. On four $τ^3$-bench agents, AgentEval successfully generates tests covering $23$--$38$ distinct boundaries per agent; ablation studies attribute the gain to the graph's structure: $23$ distinct boundaries versus $12$ with a prompt-only baseline, at lower duplicate and false-alarm rates.
