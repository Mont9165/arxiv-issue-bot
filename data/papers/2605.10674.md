# Step Rejection Fine-Tuning: A Practical Distillation Recipe

- arXiv ID: `2605.10674v1`
- Authors: Igor Slinko, Ilia Zavidnyi, Egor Bogomolov, Yaroslav Zharov
- Published: 2026-05-11
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.AI`, `cs.CL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.10674v1) | [pdf](https://arxiv.org/pdf/2605.10674v1)

## Abstract

Rejection Fine-Tuning (RFT) is a standard method for training LLM agents, where unsuccessful trajectories are discarded from the training set. In the context of SWE-bench tasks, this corresponds to filtering out runs where the submitted patch does not pass the tests. However, this approach discards unresolved trajectories, even though they form a large portion of all trajectories for hard tasks and even then may be partially correct. In this work, we propose Step Rejection Fine-Tuning (SRFT) - a practical way to leverage these unresolved trajectories. For this, we employ a critic LLM to assess the correctness of each step in a trajectory. Consequently, during training, we mask the loss for erroneous steps while retaining them in the context window. This way we ensure the model learns to recover from errors without reproducing them. Evaluation on SWE-bench Verified shows that while RFT improves the resolution rate by 2.4% by excluding unresolved trajectories, SRFT improves it by 3.7% by filtering them instead of discarding completely, reaching the total resolution rate of 32.2%.
