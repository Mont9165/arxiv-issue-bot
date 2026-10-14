# ScaleBox: Enabling High-Fidelity and Scalable Code Verification for Large Language Models

- arXiv ID: `2604.27467v1`
- Authors: Jiasheng Zheng, Xin Zheng, Boxi Cao, Pengbo Wang, Zhengzhao Ma, Qiming Zhu, Jiazhen Jiang, Yaojie Lu, Hongyu Lin, Xianpei Han, Le Sun
- Published: 2026-04-30
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2604.27467v1) | [pdf](https://arxiv.org/pdf/2604.27467v1)

## Abstract

Code sandboxes have emerged as a critical infrastructure for advancing the coding capabilities of large language models, providing verifiable feedback for both RL training and evaluation. However, existing systems fail to provide accurate verification and efficiency under high-concurrency workloads. We present ScaleBox, a high-fidelity and scalable system designed to address these limitations in large-scale code training. ScaleBox introduces automated special-judge generation and management, fine-grained parallel execution across test cases with seamless multi-node coordination, and a configuration-driven evaluation suite for reproducible benchmarking. A series of experiments demonstrates that ScaleBox significantly enhances code verification accuracy and efficiency. Our further RLVR experiments show that ScaleBox substantially improves both performance on LiveCodeBench and training stability, significantly outperforming heuristic-matching baselines. By providing a reliable and high-throughput infrastructure, ScaleBox facilitates more effective research and development in large-scale code training.
