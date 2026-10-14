# Route-Align-Verify for Functional Correctness in Code Generation

- arXiv ID: `2608.03341v1`
- Authors: Erxue Zhou, Jingxiang Meng, Aofan Liu
- Published: 2026-08-04
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2608.03341v1) | [pdf](https://arxiv.org/pdf/2608.03341v1)

## Abstract

Large language models (LLMs) have substantially improved code generation, yet achieving strong functional correctness remains difficult, especially for heterogeneous programming tasks where a single prompting strategy and a single directly generated output are often insufficient. In this paper, we present RAV, a lightweight and modular framework that improves code generation with a fixed backbone model through three coordinated stages: Route, which applies task-aware prompt routing before generation; Align, which reduces the mismatch between fine-tuning prompts and inference-time prompts through aligned LoRA adaptation; and Verify, which selects the final output by executing multiple candidates against visible public tests.
  We evaluate RAV on the MBPP benchmark under both the sanitized and full settings. The complete RAV pipeline achieves the best performance among all evaluated configurations, reaching 0.8911 on MBPP Sanitized and 0.8520 on MBPP Full. Compared with the base model, these results represent improvements of 6.35 and 9.92 percentage points, respectively. Component-wise ablation experiments further show that task-aware routing and aligned adaptation become substantially more effective when combined with execution-based verification. Additional robustness and contamination analyses support the reliability of the observed improvements. Overall, the results indicate that functional correctness in code generation can be meaningfully improved without modifying the backbone architecture, by jointly optimizing how tasks are prompted, how the model is adapted, and how final outputs are selected.
