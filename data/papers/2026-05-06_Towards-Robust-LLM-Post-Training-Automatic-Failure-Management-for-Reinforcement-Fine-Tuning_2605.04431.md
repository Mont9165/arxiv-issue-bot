# Towards Robust LLM Post-Training: Automatic Failure Management for Reinforcement Fine-Tuning

- arXiv ID: `2605.04431v1`
- Authors: Lingzhe Zhang, Tong Jia, Yunpeng Zhai, Liancheng Fang, Kening Zheng, Hongyi Liu, Xiaosong Huang, Philip S. Yu, Ying Li
- Published: 2026-05-06
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.04431v1) | [pdf](https://arxiv.org/pdf/2605.04431v1)

## Abstract

Reinforcement fine-tuning (RFT) has become a core paradigm for post-training large language models, yet its training process remains highly fragile. Existing efforts mainly improve reliability at the system level or address specific issues in individual subproblems by modifying RFT algorithms. Despite their effectiveness, they largely overlook the problem of failure management at the training-process level. When training goes wrong, practitioners still rely heavily on expert-driven manual inspection and correction, and automatic failure management for RFT remains largely unexplored. In this paper, we take a first step toward systematic failure management for reinforcement fine-tuning. To understand the empirical structure of RFT failures, we first construct RFT-FaultBench, the first benchmark for fine-grained failures in reinforcement fine-tuning, covering 5 fault families, 16 fault types, 779 training runs, 22,549 train-step records, and 1,457,288 trajectory-level records. Based on this benchmark, we conduct a comprehensive empirical study showing that RFT failures are both observable from training dynamics and distinguishable through their empirical fault fingerprints. Building on these findings, we propose RFT-FM, an automatic failure management framework for reinforcement fine-tuning that unifies anomaly detection, failure diagnosis, and auto remediation in a closed loop. Experimental results show that RFT-FaultBench is neither trivial nor saturated: it exhibits clear anomaly structure while still posing substantial challenges, especially under subtle fault settings. Moreover, RFT-FM shows strong capability in detecting, diagnosing, and mitigating RFT failures.
