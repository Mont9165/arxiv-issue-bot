# Same Signal, Different Semantics: A Cross-Framework Behavioral Analysis of Software Engineering Agents

- arXiv ID: `2605.18332v1`
- Authors: Wei Ma, Zhi Chen, Jingxu Gu, Tianling Li, Shangqing Liu, Lingxiao Jiang
- Published: 2026-05-18
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.18332v1) | [pdf](https://arxiv.org/pdf/2605.18332v1)

## Abstract

Behavioral studies of LLM-based software engineering agents extract operational rules about which trajectory shapes correlate with higher resolution rates: that a test step follows a code modification, that error cascades are short, or that trajectories are compact. Each rule is typically derived from a single framework, and whether it transfers, in sign as well as magnitude, to structurally different agent designs has not been directly tested.
  We address this at ecosystem scale: 64,380 SWE-bench runs from 126 agent configurations spanning 43 frameworks, where each configuration pairs an LLM with a framework (e.g., SWE-Agent, OpenHands) that supplies its tools and workflow. We separate framework effects from LLM effects by holding each layer fixed in turn, then measure one behavior-outcome effect per configuration and examine how those effects agree or disagree.
  Swapping the framework while the LLM is held fixed produces large behavioral differences in every action feature. On most signals, configurations disagree not merely in magnitude but in direction. Error rate is the cleanest case: 47 configurations resolve more issues when their error rate is lower, while 48 resolve more when it is higher. Five other continuous features and three of seven binary patterns from prior SE literature show similar directional disagreement. Framework identity accounts for more of this variation than LLM family: for mean turns, framework explains 64% of the between-configuration variance against the LLM's 10%.
  The implication is that the same observable behavioral signal can carry opposite meaning for different agent configurations. Behavioral findings from any single framework therefore warrant cross-configuration validation before being claimed as general.
