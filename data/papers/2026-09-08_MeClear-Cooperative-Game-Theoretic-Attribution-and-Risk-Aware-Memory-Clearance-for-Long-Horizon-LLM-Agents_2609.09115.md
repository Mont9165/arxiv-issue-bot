# MeClear: Cooperative Game-Theoretic Attribution and Risk-Aware Memory Clearance for Long-Horizon LLM Agents

- arXiv ID: `2609.09115v1`
- Authors: Boyu Yang, Jiazheng Sun, Zilong Lu, Zhi Qiu, Xin Peng, Jun Zheng
- Published: 2026-09-08
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.09115v1) | [pdf](https://arxiv.org/pdf/2609.09115v1)

## Abstract

Long horizon Large Language Model (LLM) agents rely on external memory systems to preserve user preferences and task knowledge across extended interactions. Conventional retrieval mechanisms optimize semantic compatibility rather than downstream utility, frequently introducing outdated, misleading, or conflicting evidence into the active context. We present MeClear, a task conditioned memory clearance framework that identifies memories featuring negative downstream utility through cooperative attribution and selectively suppresses them from agent execution. MeClear combines Leave One Out screening with sampled cooperative Shapley attribution to distribute utility across interacting evidence, effectively resolving redundant conflict masking where single removal evaluations fail. Utilizing attribution rankings, MeClear executes a query scoped minimal clearance strategy over a nested filtration, verifying task recovery on the cleared context without permanently altering the persistent memory bank. Comprehensive experimental evaluations across ten long dialogue memory pools demonstrate that MeClear achieves a target recall of 85.9% and an overall task recovery rate of 82.3%, representing a 25.5 percentage point improvement over Leave One Out (LOO) baselines.
