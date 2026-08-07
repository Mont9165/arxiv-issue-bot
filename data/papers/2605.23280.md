# BCTuner: LLM-Guided Monte Carlo Tree Search for Efficient Blockchain Knob Tuning

- arXiv ID: `2605.23280v1`
- Authors: Yaoyi Deng, Chongyang Tao, Mingxuan Li, Xuelian Lin, Han Sun, Mingchao Wan, Shuai Ma
- Published: 2026-05-22
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.23280v1) | [pdf](https://arxiv.org/pdf/2605.23280v1)

## Abstract

Knob tuning plays a critical role in improving the performance of permissioned blockchains. However, efficient tuning remains challenging due to the architectural complexity of blockchains and the semantic gap between knob-specific logic and the numerical optimization requirements of tuning tools. In addition, configuration changes are often coupled across different stages of the transaction pipeline, making their performance impact difficult to isolate and predict. Since each trial requires deployment and distributed benchmarking, ineffective exploration incurs substantial cost. These challenges motivate BCTuner, a Large Language Model (LLM)-guided framework that combines knowledge-guided reasoning with structured search. BCTuner organizes multi-source tuning knowledge to support LLM-based reasoning over knob semantics, constraints, and deployment context. It formulates tuning as a Monte Carlo Tree Search (MCTS) process over structured action trajectories, where configurations are incrementally constructed, validated, evaluated, and refined rather than generated in one step. BCTuner further applies adaptive pruning to discard infeasible or low-potential branches before system evaluation. We evaluate BCTuner on Hyperledger Fabric and ChainMaker under diverse workloads and network settings. Experimental results show that BCTuner achieves up to 211.38% throughput improvement over default configurations and outperforms the state-of-the-art blockchain tuning method by up to 20% in performance, while requiring up to 8x fewer interactions with the blockchain system.
