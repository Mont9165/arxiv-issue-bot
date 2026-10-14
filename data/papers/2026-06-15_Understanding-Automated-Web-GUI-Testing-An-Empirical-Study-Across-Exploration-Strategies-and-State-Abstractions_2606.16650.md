# Understanding Automated Web GUI Testing: An Empirical Study Across Exploration Strategies and State Abstractions

- arXiv ID: `2606.16650v1`
- Authors: Chenxu Liu, Wei Yang, Ying Zhang, Tao Xie
- Published: 2026-06-15
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.16650v1) | [pdf](https://arxiv.org/pdf/2606.16650v1)

## Abstract

Automated web GUI testing (AWGT) relies on exploration strategies that exercise web applications through GUI actions to maximize code coverage, spanning traditional model-based, reinforcement learning (RL)-based, and emerging large language model (LLM)-based approaches. State abstraction, which detects pages with the same functionality to avoid repeated testing, has long been recognized as critical to guiding exploration. However, how exploration strategies and state abstractions jointly affect testing effectiveness remains underexplored.
  We present an empirical study analyzing both factors from the perspectives of code coverage and failure revelation. We compare representative model-based, RL-based, and LLM-based approaches; investigate how six state abstractions influence model-based and RL-based approaches; examine LLM-based approaches under different history representations, which act as a form of state abstraction; and compare the failures exposed by different approaches.
  Our results show that no single strategy excels across all dimensions; instead, categories exhibit complementary strengths in code coverage, state coverage, and failure discovery. State abstraction is a key factor: strict, fine-grained abstractions favor model-based strategies, while compact ones better support RL-based strategies. History representation substantially affects LLM-based strategies, where concise, functionality-level context performs best. We also find that code coverage is weakly correlated with failure-revealing ability, underscoring the need for multi-dimensional evaluation. These findings offer practical guidance for selecting exploration strategies and designing effective state abstractions for AWGT.
