# Chronos Enables Code Agents to Reason over Software Evolution

- arXiv ID: `2610.11578v1`
- Authors: Xin Yin, Yiang Zhang, Zhiyuan Peng, Chao Ni, Zhe Cui, Xiaohua Xin
- Published: 2026-10-08
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2610.11578v1) | [pdf](https://arxiv.org/pdf/2610.11578v1)

## Abstract

Historical pull requests record the design decisions, compatibility constraints, and implementation patterns behind a codebase's current state. Experience relevant to a new task can span related changes whose descriptions emphasize different concerns. We introduce Chronos, a test-time framework that makes this connected history available to large language model (LLM)-based code agents. Chronos distills merged pull requests into structured experience cards and connects them through a typed graph of code-level, developer-intent, and organizational relations. Semantic search identifies entry cards, and weighted multi-hop expansion retrieves connected changes for selective reading. The same memory guides candidate generation and patch selection: a patch-focused change agent and a validation-strategy agent each develop a patch, and an evolution steward consults history to select between them. On SWE-Bench Verified, the full workflow improves SWE-Agent across all six evaluated LLM backbones, raising the mean resolution rate from 69.2% to 72.9% and reaching 79.8% with MiniMax M2.5. With the same backbone, it raises resolution rates from 48.3% to 51.7% on SWE-Bench Pro and from 41.0% to 43.5% on FEA-Bench Lite. Both experience-guided single-agent variants also outperform the base agent. In a human evaluation on 100 tasks with ten cards retrieved per task, graph-grounded retrieval increases the mean number of useful cards from 1.24 to 2.87 over flat semantic retrieval. These results demonstrate the value of PR relations for retrieving useful repository experience and of the evaluated workflows for applying that experience during patch generation and selection.
