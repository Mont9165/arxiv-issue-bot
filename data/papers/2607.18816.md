# AgentTrails: Towards Trust and Reuse for Agentic Tasks

- arXiv ID: `2607.18816v1`
- Authors: Eden Wu, Sonia Castelo, Yurong Liu, Cláudio T. Silva, Juliana Freire
- Published: 2026-07-21
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.18816v1) | [pdf](https://arxiv.org/pdf/2607.18816v1)

## Abstract

LLM-powered agents increasingly tackle complex tasks by invoking tools, querying databases, executing code, and manipulating intermediate artifacts. These agents follow trajectories that are typically stored as chronological logs, obscuring the underlying dataflow -- the dependencies between their actions and the artifacts they create and manipulate. This limits developers' ability to understand the agents' trails, compare executions, debug failures, and re-use the computations. We present AgentTrails, a prototype system for agent provenance and sensemaking. AgentTrails converts raw trajectories into structured provenance graphs, where tool calls are modeled as computational actions and inputs and outputs as data artifacts. The system supports the comparison of executions by placing multiple provenance graphs on a shared canvas and constructing a joined quotient graph that aligns recurring tools, artifacts, and dependency structures across trajectories. On top of this representation, AgentTrails supports pattern extraction, downstream analysis, and skill abstraction. We demonstrate AgentTrails on real-world agent trajectories, showing that it reveals hidden dependencies, aligns divergent executions, and surfaces recurring tool-use patterns beyond chronological logs.
