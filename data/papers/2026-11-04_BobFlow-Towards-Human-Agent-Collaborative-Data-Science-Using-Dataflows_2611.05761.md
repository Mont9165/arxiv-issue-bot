# BobFlow: Towards Human-Agent Collaborative Data Science Using Dataflows

- arXiv ID: `2611.05761v1`
- Authors: Jiadong Bai, Yicong Huang, Chen Li
- Published: 2026-11-04
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`, `cs.HC`
- Links: [abs](http://arxiv.org/abs/2611.05761v1) | [pdf](https://arxiv.org/pdf/2611.05761v1)

## Abstract

Recent advances in large language models (LLMs) have established human-agent collaboration as a promising paradigm for data science. Effective collaboration requires a shared computational abstraction that enables agents to reason about processing logic while allowing human analysts to understand, guide, and refine the analysis. Although scripts written in Python or SQL provide precise control, their syntax and execution details can be difficult for analysts to understand and modify. In this paper, we argue that dataflows are an effective abstraction for human-agent collaboration in data science. We introduce BobFlow, a system that combines the dataflow abstraction with the ReAct paradigm. It enables agents to iteratively construct and execute dataflows for data science tasks while allowing analysts to inspect the analysis and provide feedback. Our user study shows that BobFlow helps analysts understand, inspect, and verify agent-generated analyses. A thorough experimental evaluation across proprietary and open-weight LLMs shows accuracy score gains of up to 18.6 points at just over 1/3 of a script-based ReAct agent's inference cost.
