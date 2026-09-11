# Ecdysis: Efficient and Effective Training of Runtime Harnesses for LLM Agents

- arXiv ID: `2609.11677v1`
- Authors: Ruiqing Yue, Yu Cui, Zhuoyu Sun, Sicheng Pan, Xianhong Xue, Tingyu Li, Ting Li, Wenzhuo Zhu, Yi Chen, Yifei Liu, Baohan Huang, Zhe Cui, Haibin Zhang, Cong Zuo
- Published: 2026-09-10
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.11677v1) | [pdf](https://arxiv.org/pdf/2609.11677v1)

## Abstract

Self-evolving runtime harnesses can substantially improve the capabilities of large language model (LLM) agents and provide a promising paradigm for optimizing agent execution. Existing harness evolution methods typically rely on iterative search, repeatedly evaluating and revising candidate harnesses based on execution feedback from task instances. While this paradigm enables continuous harness optimization, it incurs substantial time overhead due to repeated agent executions and code modifications, and may overfit to observed tasks and specific failure patterns, resulting in degraded generalization to unseen tasks. We identify the lack of principled failure diagnosis as a key bottleneck in harness evolution: an observed failure can reflect either model-specific deficiencies or systematic harness deficiencies, and directly optimizing against individual failures can lead to unnecessary model-specific accommodation. We therefore propose Ecdysis, an efficient and effective framework that distinguishes model-specific accommodation from harness-level repair and biases adaptation toward systematic harness deficiencies by identifying recurring cross-task failure patterns. Ecdysis adopts a batch-level cross-instance failure aggregation paradigm to jointly analyze failure evidence from multiple task instances and further introduces Failure-Driven Collaborative Refinement to diagnose failure causes and iteratively refine harness modification specifications. By combining cross-instance failure analysis with multi-role diagnosis, Ecdysis enables more effective harness evolution with lower training time. Experiments show that Ecdysis achieves up to a 1.84x speedup in harness training compared with existing harness evolution methods, while improving the reasoning accuracy of the resulting harnesses by 18.56%.
