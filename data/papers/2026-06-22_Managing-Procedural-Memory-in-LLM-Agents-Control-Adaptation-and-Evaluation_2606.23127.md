# Managing Procedural Memory in LLM Agents: Control, Adaptation, and Evaluation

- arXiv ID: `2606.23127v1`
- Authors: Julia Belikova, Rauf Parchiev, Evgeny Egorov, Grigorii Davydenko, Gleb Gusev, Andrey Savchenko, Maksim Makarenko
- Published: 2026-06-22
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.CL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.23127v1) | [pdf](https://arxiv.org/pdf/2606.23127v1)

## Abstract

Procedural memory is increasingly used to improve LLM agents on recurring workplace tasks, yet its ability to produce reusable skills remains poorly understood. We introduce AFTER, a benchmark of 382 realistic enterprise tasks spanning six professional roles and 22 procedural skills, designed to evaluate how skills transfer across tasks, roles, and model backbones. The benchmark includes controlled evaluation settings for local improvement, cross-task transfer, cross-role transfer, and cross-model generalization. Experiments show that procedural memory delivers consistent gains in industrial workflows: a single refinement round improves aggregate performance by 3.7-6.7 points, while skills evolved from diverse multi-model execution traces achieve 73.1% cross-model test accuracy, outperforming all single-model trace sources. We further find that some skills generalize broadly across tasks and models, whereas others become specialized to role-specific workflows and lose effectiveness under transfer. These results provide practical guidance for building, evaluating, and deploying procedural memory systems in production agent platforms.
