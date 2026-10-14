# RAPO-Sol: Retrieval-Augmented Preference Optimization for Repository-Level Solidity Code Generation

- arXiv ID: `2610.08429v1`
- Authors: Rongcun Wang, Shi Chen
- Published: 2026-10-06
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.08429v1) | [pdf](https://arxiv.org/pdf/2610.08429v1)

## Abstract

Smart contracts written in Solidity manage assets, permissions, and irreversible state changes, making code generation both useful and security-critical. Repository-level Solidity generation is challenging because models must synthesize complete contracts or libraries while preserving consistency across state variables, modifiers, events, inheritance, external calls, and access-control logic. We present RAPO-Sol, a two-stage training framework for repository-level Solidity code generation. First, Retrieval-Augmented Fine-Tuning (RAFT) augments each training input with similar Solidity examples, helping the model learn recurring contract-level patterns while remaining retrieval-free at inference time. Second, Direct Preference Optimization (DPO) trains the model to prefer reference contracts over close but semantically flawed alternatives. We construct rejected samples using Solidity Semantic-Anchor Perturbation (SAP), which perturbs validation statements, visibility modifiers, data-location keywords, context variables, payment operations, and low-level calls. Experiments on SolidityBench with CodeLlama-7B-Instruct, DeepSeek-Coder-6.7B-Instruct, and Qwen2.5-Coder-7B-Instruct show that RAFT consistently improves over supervised fine-tuning, while SAP-based DPO provides further gains in BLEU and SolidityScore. The full RAFT+DPO pipeline achieves the best performance across all three models, demonstrating complementary benefits from retrieval during training and Solidity-aware preference optimization without adding retrieval cost at inference.
