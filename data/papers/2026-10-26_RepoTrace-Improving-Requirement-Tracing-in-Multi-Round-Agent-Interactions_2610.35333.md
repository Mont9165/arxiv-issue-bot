# RepoTrace: Improving Requirement Tracing in Multi-Round Agent Interactions

- arXiv ID: `2610.35333v1`
- Authors: Huanyu Liu, Yezheng Cheng, Jinliang You, Tianxiao Huang, Linyu Li, Zheng Fang, Peng Cao, Ge Li
- Published: 2026-10-26
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2610.35333v1) | [pdf](https://arxiv.org/pdf/2610.35333v1)

## Abstract

Code agents have become increasingly capable of performing software engineering tasks through interaction with software environments. However, agents tend to degrade as the number of interaction rounds increases, making it difficult to maintain existing software during iterative modification. We analyze 2,656 agent trajectories in EvoCode-Bench and identify requirement focus misalignment as a recurring failure pattern, where agents struggle to distinguish the primary modification targets of a requirement from unrelated code.
  We propose Repotrace a requirement-driven repository understanding harness that combines repository structure with requirement semantics to construct a requirement-code correspondence and injects it into the agent context. This correspondence enables code agents to follow the repository architecture, trace requirements across multi-round interactions, and identify the core code elements corresponding to the current requirement. Experiments show that Repotrace improves the mean per-round reward (MPR) across different models (e.g., +19.99 on GLM-5.2) and agent harnesses (e.g., +10.22 on Claude Code). Across rounds, Repotrace increases the average per-round reward from 0.163 to 0.371 on Terminus-2 with DeepSeek-V4-Pro, while reducing average regression errors by 56.78%. We release the source code and agents' trajectories to support future research.
