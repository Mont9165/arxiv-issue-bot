# Test Case Prioritization for DNNs via Neural Collapse Instability

- arXiv ID: `2607.20046v1`
- Authors: Chunyu Liu, Mingyuan Li, Yang Li, Wenmin Li, Fei Gao, Tengfei Tu, Su-Juan Qin
- Published: 2026-07-22
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.20046v1) | [pdf](https://arxiv.org/pdf/2607.20046v1)

## Abstract

With the widespread deployment of deep neural networks (DNNs) in safety-critical domains, reducing the cost of model validation under limited testing budgets has become increasingly important. Existing test case prioritization techniques often rely on single-checkpoint confidence signals derived from output probabilities. However, DNNs can be confidently wrong, and the confidence margin between the predicted and competing classes is frequently small, which weakens early fault discovery. To address this limitation, we propose a Neural-Collapse-Inspired Prioritization (NCIP) framework that replaces absolute confidence with cross-checkpoint prediction variability in the terminal training regime, where model geometry becomes highly structured. NCIP introduces two key components. First, it selects an NC-guided representative subset of training checkpoints using an equiangularity score of classifier weights, quantified as the standard deviation of pairwise cosine similarities among class weight vectors. Second, it prioritizes test inputs by their prediction variability across the selected checkpoints, surfacing boundary-adjacent and failure-prone samples that are unstable under checkpoint-induced decision boundary shifts. Extensive experiments across multiple datasets and architectures show that NCIP achieves strong performance in early fault discovery compared with competitive baselines, with 1.5 to 16.6 percent RAUC-ALL gains and 4.9 to 20.6 percent RAUC-500 gains under the same testing budget. NCIP further attains the best average performance across all dataset-model pairs.
