# DataFlow-Harness: A Grounded Code-Agent Platform for Constructing Editable LLM Data Pipelines

- arXiv ID: `2607.16617v1`
- Authors: Runming He, Zhen Hao Wong, Hao Liang, Zimo Meng, Chengyu Shen, Xiaochen Ma, Wentao Zhang
- Published: 2026-07-18
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.16617v1) | [pdf](https://arxiv.org/pdf/2607.16617v1)

## Abstract

Large language models (LLMs) are increasingly used to automate data-processing workflows, yet coding agents typically produce scripts that are not automatically materialized as persistent, editable platform artifacts. We call this disconnect the \textit{NL2Pipeline gap}. To bridge it, we introduce \textsc{DataFlow-Harness}, a platform that guides an LLM agent to construct platform-native directed acyclic graphs (DAGs) through typed, incremental mutations rather than free-form scripts. The platform combines \textsc{DataFlow-Skills} for procedural guidance, a Model Context Protocol (MCP) layer that exposes the live operator registry and current pipeline state, and \textsc{DataFlow-WebUI}, which synchronizes conversational authoring with a visual DAG editor. On a 12-task data-engineering benchmark, \textsc{DataFlow-Harness} achieves a 93.3\% observed end-to-end pass rate. Relative to Vanilla Claude Code, it reduces measured monetary cost by 72.5\% and generation latency by 49.9\%; its observed pass rate is within 0.9 percentage points of the Context-Aware Claude Code baseline while its cost is 42.8\% lower. Per-task analysis indicates that Skills are most useful when construction depends on implicit procedural knowledge. These results show that live platform grounding can produce persistent, editable workflow artifacts with an observed reliability close to script-generation baselines and with lower measured construction cost and latency.
