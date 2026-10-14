# GRAML: Graph-Grounded Reasoning and Multi-Task Learning for LLM-Based Software Vulnerability Detection

- arXiv ID: `2610.09605v1`
- Authors: Ruohan Li, Miaoqing Tian, Haipeng Qu, Ruobing Jiang
- Published: 2026-10-07
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.09605v1) | [pdf](https://arxiv.org/pdf/2610.09605v1)

## Abstract

Large Language Models (LLMs) have been widely applied to software vulnerability detection. However, their performance is often limited by insufficient use of control-flow and data-flow information. In this paper, we propose GRAML, a framework that combines graph evidence, vulnerability description generation, and multi-task training. GRAML first performs static analysis on C/C++ programs to extract critical source lines and typed line relations as structural evidence. It then uses this evidence to guide GPT-5 through the Tree-of-Thought-guided Vulnerability Reasoning (ToT-VR) process and generate vulnerability descriptions. These descriptions are further combined with Detection, Localization, and Assessment samples to build a unified four-task training dataset. We evaluate GRAML on an in-distribution (ID) test set and six out-of-distribution (OOD) datasets. The results show that GRAML achieves average F1 scores ranging from 66.67% to 68.70%, outperforming state-of-the-art baselines by up to 30.92%. Ablation experiments further show that ToT-VR and graph-guided vulnerability descriptions improve detection performance compared with standard Chain-of-Thought (CoT) reasoning and raw Code Property Graph (CPG) serializations. These findings provide practical guidance for building more reliable and secure software engineering systems with large language models.
