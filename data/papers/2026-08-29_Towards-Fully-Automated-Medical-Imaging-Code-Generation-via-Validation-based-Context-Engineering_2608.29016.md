# Towards Fully Automated Medical Imaging Code Generation via Validation-based Context Engineering

- arXiv ID: `2608.29016v1`
- Authors: Zixiao Zhao, Jing Sun, Zhe Hou, Cheng-Hao Cai, Qian Liu, Mengze Li, Zijian Zhang, Jin Song Dong
- Published: 2026-08-29
- Primary category: `cs.CV`
- Categories: `cs.CV`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.29016v1) | [pdf](https://arxiv.org/pdf/2608.29016v1)

## Abstract

Large language models (LLMs) have demonstrated considerable promise in program generation for small-scale and conventional application development; however, they remain limited when applied to complex, domain-specific tasks such as medical image processing. General-purpose models lack explicit domain knowledge and robust validation mechanisms to ensure correctness, often requiring substantial human intervention to produce reliable processing pipelines. To address these limitations, we propose AutoMedImg, a multi-agent framework for fully automated medical image processing code generation. AutoMedImg orchestrates specialised agents across two phases: a Planning Phase that performs dataset analysis and architecture design with semantic and formal verification, and a Coding Phase that generates modules in parallel with static checking, execution testing, and assembly validation. This multi-stage validation mitigates error propagation throughout generation, while comprehensive auto-context engineering combining domain-specific knowledge bases, shared memory, and validation feedback automates context construction without manual prompting. A cross-project adaptive pipeline synthesis mechanism further accumulates validated pipelines and retrieves proven components for new tasks based on project similarity, enhancing generation efficiency through cross-project learning. Extensive evaluation across six diverse and well-established medical imaging datasets with five backbone LLMs demonstrates that AutoMedImg achieves zero human intervention, with Dice scores of up to 0.90 for segmentation tasks and 99% accuracy for classification.
