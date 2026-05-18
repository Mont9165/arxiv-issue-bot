# BootstrapAgent: Distilling Repository Setup into Reusable Agent Knowledge

- arXiv ID: `2605.15815v1`
- Authors: Sihan Fu, Oucheng Liu, Shiyuan Wang, Jin Shi, Chengkun Wei
- Published: 2026-05-15
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`, `cs.MA`
- Links: [abs](http://arxiv.org/abs/2605.15815v1) | [pdf](https://arxiv.org/pdf/2605.15815v1)

## Abstract

Code agents increasingly help developers work with unfamiliar repositories, but every such task depends on a costly prerequisite: bootstrapping the repository into a usable development state. This process requires substantial trial-and-error exploration, yet the resulting knowledge--resolved dependencies, repair strategies--stays trapped in a single conversation, unavailable to future agents. We therefore formulate repository bootstrapping as a reusable startup knowledge problem and introduce BootstrapAgent, a multi-agent framework that distills the heuristics discovered during bootstrap exploration into a persistent, verifiable, agent-consumable .bootstrap contract. Through evidence extraction, structured planning, deterministic Docker-based verification, and trace-driven repair, BootstrapAgent generates a contract covering environment setup, diagnostic checks, minimal verification, and accumulated repair knowledge. We further propose warm repair with clean replay to accelerate iterative debugging without sacrificing cold-start reproducibility, and a delta repair with sanity check to prevent reward hacking. Experiments on three benchmarks show that BootstrapAgent achieves a 92.9% success rate, outperforming the baseline by over 10% while reducing downstream agent token usage by 25.9% and build time by 22.3%. Our code is available at https://github.com/Vossera/BootstrapAgent.
