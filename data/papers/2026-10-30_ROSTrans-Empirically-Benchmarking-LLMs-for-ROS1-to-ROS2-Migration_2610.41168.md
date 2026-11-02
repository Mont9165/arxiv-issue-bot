# ROSTrans: Empirically Benchmarking LLMs for ROS1-to-ROS2 Migration

- arXiv ID: `2610.41168v1`
- Authors: Yichen Zhao, Minghao Shao, Zhuoyan Yu, Yijun Shen, Boyuan Chen, Yik-Cheung Tam, Muhammad Shafique
- Published: 2026-10-30
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2610.41168v1) | [pdf](https://arxiv.org/pdf/2610.41168v1)

## Abstract

Although large language models have shown strong capabilities in domain-specific code generation, their performance in robotics software development, especially for the Robot Operating System (ROS), remains largely unexplored. ROS code generation presents distinctive challenges, including complex inter-node coordination, middleware configuration, and lifecycle semantics that go far beyond standard coding benchmarks, and many important correctness properties become observable only once migrated nodes are launched and communicate. We present ROSTrans, a benchmark for evaluating LLMs on ROS1-to-ROS2 code migration, a representative and practically important setting for ROS code generation. ROSTrans comprises 108 scaffolded completion tasks drawn from a diverse set of 70+ open-source ROS1 repositories and organized into a hierarchical taxonomy assessing interface-level, behavioral-level and system-level correctness. For every task we establish an executable reference: a verified ROS2 implementation, a runtime test suite that launches the nodes and exercises their topics, services, actions and parameters, and a container ensuring reproducibility. Candidates are scored by injecting only their target files into an otherwise fixed copy of the reference package, so a candidate can neither supply nor weaken the tests it is judged by. Evaluating six frontier LLMs over five stochastic generations per task, we find pass@1 below 10.9%, and that 56.5% of all samples build successfully and then fail at runtime,and 32.0% fail runtime assertions on the migrated interfaces, a class of error no compile-only oracle can detect. Execution-guided repair further improves task success, reaching 49.1% and 47.2% for Claude Opus 4.6 and GPT-5.5 after three rounds, respectively.
