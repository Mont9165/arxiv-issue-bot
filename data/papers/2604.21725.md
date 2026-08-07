# AEL: Agent Evolving Learning for Open-Ended Environments

- arXiv ID: `2604.21725v1`
- Authors: Wujiang Xu, Jiaojiao Han, Minghao Guo, Kai Mei, Xi Zhu, Han Zhang, Dimitris N. Metaxas
- Published: 2026-04-23
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.AI`, `cs.CE`
- Links: [abs](http://arxiv.org/abs/2604.21725v1) | [pdf](https://arxiv.org/pdf/2604.21725v1)

## Abstract

LLM agents increasingly operate in open-ended environments spanning hundreds of sequential episodes, yet they remain largely stateless: each task is solved from scratch without converting past experience into better future behavior. The central obstacle is not \emph{what} to remember but \emph{how to use} what has been remembered, including which retrieval policy to apply, how to interpret prior outcomes, and when the current strategy itself must change. We introduce \emph{Agent Evolving Learning} (\ael{}), a two-timescale framework that addresses this obstacle. At the fast timescale, a Thompson Sampling bandit learns which memory retrieval policy to apply at each episode; at the slow timescale, LLM-driven reflection diagnoses failure patterns and injects causal insights into the agent's decision prompt, giving it an interpretive frame for the evidence it retrieves. On a sequential portfolio benchmark (10 sector-diverse tickers, 208 episodes, 5 random seeds), \ael{} achieves a Sharpe ratio of 2.13$\pm$0.47, outperforming five published self-improving methods and all non-LLM baselines while maintaining the lowest variance among all LLM-based approaches. A nine-variant ablation reveals a ``less is more'' pattern: memory and reflection together produce a 58\% cumulative improvement over the stateless baseline, yet every additional mechanism we test (planner evolution, per-tool selection, cold-start initialization, skill extraction, and three credit assignment methods) \emph{degrades} performance. This demonstrates that the bottleneck in agent self-improvement is \emph{self-diagnosing how to use} experience rather than adding architectural complexity. Code and data: https://github.com/WujiangXu/AEL.
