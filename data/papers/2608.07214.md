# Toward a Causal Data Management Ecosystem for Decision Making and Agentic AI

- arXiv ID: `2608.07214v1`
- Authors: Dazhuo Qiu, Yingli Zhou, Amedeo Pachera, Angela Bonifati, Andrea Mauri
- Published: 2026-08-07
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`, `eess.SY`
- Links: [abs](http://arxiv.org/abs/2608.07214v1) | [pdf](https://arxiv.org/pdf/2608.07214v1)

## Abstract

Modern AI is no longer a single model but an ecosystem: classical ML predictors, deep and multimodal models, large language models, and agents, each trained and tuned over different data sources and each producing outputs at scale that become inputs to the others. Operating such an ecosystem is fundamentally a data integration problem - the knowledge it depends on is fragmented across dozens of heterogeneous, independently governed sources that must be reconciled and continually maintained. Yet integration alone is not enough. The predictions these systems make are shaped by many interacting factors, and the events, decisions, and variables that drive an outcome are routinely entangled with the ones that merely accompany it; treated as a basis for action, such correlational signals invite confounded decisions. This becomes acute once agents act autonomously: to be trustworthy and reliable, an agent must anticipate the consequences of its actions, not merely extrapolate from what has co-occurred before. Causal reasoning is what closes this gap, distinguishing the drivers of an outcome from its correlates, and enabling prescriptive and counterfactual analysis over the ecosystem's data. We therefore argue that the integrated ecosystem needs an explicit causal layer, and we propose to build it as a shared, persistent, queryable Causal World System (CWS).
