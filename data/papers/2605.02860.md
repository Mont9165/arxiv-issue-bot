# Standing on the Shoulders of Giants: Stabilized Knowledge Distillation for Cross--Language Code Clone Detection

- arXiv ID: `2605.02860v1`
- Authors: Mohamad Khajezade, Fatemeh H. Fard, Mohamed Sami Shehata
- Published: 2026-05-04
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.02860v1) | [pdf](https://arxiv.org/pdf/2605.02860v1)

## Abstract

Cross-language code clone detection (X-CCD) is challenging because semantically equivalent programs written in different languages often share little surface similarity. Although large language models (LLMs) have shown promise for semantic clone detection, their use as black-box systems raises concerns about cost, reproducibility, privacy, and unreliable output formatting. In particular, compact open-source models often struggle to follow reasoning-oriented prompts and to produce outputs that can be consistently mapped to binary clone labels.
  To address these limitations, we propose a knowledge distillation framework that transfers reasoning capabilities from DeepSeek-R1 into compact open-source student models for X-CCD. Using cross-language code pairs derived from Project CodeNet, we construct reasoning-oriented synthetic training data and fine-tune Phi3 and Qwen-Coder with LoRA adapters. We further introduce response stabilization methods, including forced conclusion prompting, a binary classification head, and a contrastive classification head, and evaluate model behavior using both predictive metrics and response rate.
  Experiments on Python--Java, Rust--Java, Rust--Python, and Rust--Ruby show that knowledge distillation consistently improves the reliability of compact models and often improves predictive performance, especially under distribution shift. In addition, classification-head variants substantially reduce inference time compared to generation-based inference. Overall, our results show that reasoning-oriented distillation combined with response stabilization makes compact open-source models more practical and reliable for X-CCD detection.
