# AiXapply: Fast and Reliable Full-File Code Integration with Specialized Small Models for IDE Workflows

- arXiv ID: `2611.07634v1`
- Authors: Siyuan Jiang, Xiang Cai, Peixu Wang, Yu Han, Yihong Dong, Wei Ning, Xuyuan Guo, Jincheng Wen, Dexin Liu, Wei Zhao, Ge Li
- Published: 2026-11-05
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.07634v1) | [pdf](https://arxiv.org/pdf/2611.07634v1)

## Abstract

Large language models increasingly assist developers by proposing small code edits, yet reliably integrating a partial update snippet into an existing file while preserving unrelated content remains poorly supported by current code-generation workflows. We formalize the Code Integration (Apply) task as follows: given an original file and an update snippet, the system must produce the complete merged file while preserving all content outside the requested edit. We construct a high-quality multi-language dataset from real commits via a structured pipeline that converts code changes into update snippets paired with full-file ground truth and enforces consistency through verification and filtering. We then train a specialized 4B model, aiXapply, using supervised fine-tuning and reinforcement learning (GRPO). The supervised variant achieves 94.4% accuracy under our language-aware comparison, surpassing a strong large-model (Deepseek-V3.2) baseline (91.6%). Speculative decoding enables aiXapply-RL to reach $\sim$2700 tokens/s on a single A100 in a decoding subset; on the full benchmark, it achieves roughly 75$\times$ lower latency than the API-served Deepseek-V3.2 baseline. We further conduct an industrial deployment of aiXapply-RL in the aiXcoder IDE plugin as a dedicated Apply service, reducing mean Apply latency from 50 seconds to 1.89 seconds by offloading full-file generation from the upstream large model. Under time-based capacity planning, replacing one of five upstream serving instances would save 20% of upstream machine cost before the additional shared A100 service cost. Overall, our results demonstrate that treating code integration as a standalone task enables small models to achieve high accuracy, practical efficiency, and concrete industrial benefits in real-world IDE workflows where latency, cost and privacy are critical.
