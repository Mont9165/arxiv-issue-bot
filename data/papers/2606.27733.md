# BashCoder-R1: Towards Robust and Explainable Bash Code Generation with Robustness-Aware Group Relative Policy Optimization

- arXiv ID: `2606.27733v1`
- Authors: Lei Yu, Peng Wang, Jia Xu, Jingyuan Zhang, Xin Wang, Jiajia Ma, Li Yang, Changzhi Deng, Zenghua Wang, Fengjun Zhang
- Published: 2026-06-26
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.27733v1) | [pdf](https://arxiv.org/pdf/2606.27733v1)

## Abstract

Bash scripts are the cornerstone of system administration and DevOps automation, where code quality directly impacts system stability and security. In automated Bash script generation using Large Language Models (LLMs), two interconnected failures emerge: unauditable "black box" reasoning and critical robustness vulnerabilities in generated code. To address both, we propose BashCoder-R1, a novel framework for robust and explainable Bash script generation. Our pipeline combines: (1) Continual Pre-training (CPT) to specialize the model on Bash paradigms; (2) Long Chain-of-Thought Supervised Fine-Tuning (L-CoT SFT) on expert-validated reasoning-and-code samples to emulate proactive risk-aware thinking; and (3) Robustness-Aware Group Relative Policy Optimization (R-GRPO), a reinforcement learning phase optimizing a weighted reward for syntax correctness, robustness (via shellcheck), and format correctness. We evaluate on BashBench, a new benchmark of 952 real-world tasks (773 single-line, 179 multi-line). BashCoder-R1 achieves SyntaxPass (100.00%/94.97%), RobustWarnRate (4.01%/16.47%), RobustPass (95.99%/79.33%), FuncRate (93.01%/93.85%), and FullRate (90.04%/73.18%) for single-line/multi-line tasks, outperforming the strongest baseline DeepSeek-V3.2 (Reasoning) by 37.82% and 20.18% in FullRate. Human evaluation on Functionality, Robustness, and Clarity further confirms BashCoder-R1 achieves the highest quality ratings.
