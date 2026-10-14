# VeriScale: Adversarial Test-Suite Scaling for Verifiable Code Generation

- arXiv ID: `2605.22368v1`
- Authors: Yifan Bai, Xiaoyang Liu, Zihao Mou, Guihong Wang, Jian Yu, Shuhan Xie, Yantao Li, Yangyu Zhang, Jingwei Liang, Tao Luo
- Published: 2026-05-21
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.22368v1) | [pdf](https://arxiv.org/pdf/2605.22368v1)

## Abstract

As large language models (LLMs) are increasingly deployed for software engineering, constructing high-quality benchmarks is crucial for evaluating not just the functional correctness, but also the formal verifiability of generated code. However, existing benchmarks are limited by the quantity and quality of positive and negative test cases, leading to an overestimation of model capabilities in generating specifications and implementations. To address this, we propose VeriScale, a novel framework driven by the adversarial implementations. It consists of two stages: test-suite expansion to construct diverse and challenging test cases, and test-suite reduction to distill them into compact yet discriminative suites. While VeriScale is general, we instantiate it on Verina to construct VerinaPlus, which expands the original test suites by over 83$\times$, and VerinaLite, a lightweight 14$\times$ variant. Our experiments across eight state-of-the-art LLMs demonstrate that VerinaPlus exposes substantial model weaknesses hidden by the original benchmark, evidenced by sharp score drops on both SpecGen and CodeGen tasks, whereas VerinaLite maintains this discriminative power at a fraction of the evaluation cost. The enhanced benchmarks and source code are publicly available at https://github.com/XiaoyangLiu-sjtu/VeriScale.
