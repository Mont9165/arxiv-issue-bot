# Learning Generalizable Multimodal Representations for Software Vulnerability Detection

- arXiv ID: `2604.25711v1`
- Authors: Zeming Dong, Yuejun Guo, Qiang Hu, Yao Zhang, Maxime Cordy, Hao Liu, Mike Papadakis, Yongqiang Lyu
- Published: 2026-04-28
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2604.25711v1) | [pdf](https://arxiv.org/pdf/2604.25711v1)

## Abstract

Source code and its accompanying comments are complementary yet naturally aligned modalities-code encodes structural logic while comments capture developer intent. However, existing vulnerability detection methods mostly rely on single-modality code representations, overlooking the complementary semantic information embedded in comments and thus limiting their generalization across complex code structures and logical relationships. To address this, we propose MultiVul, a multimodal contrastive framework that aligns code and comment representations through dual similarity learning and consistency regularization, augmented with diverse code-text pairs to improve robustness. Experiments on widely adopted DiverseVul and Devign datasets across four large language models (LLMs) (i.e., DeepSeek-Coder-6.7B, Qwen2.5-Coder-7B, StarCoder2-7B, and CodeLlama-7B) show that MultiVul achieves up to 27.07% F1 improvement over prompting-based methods and 13.37% over code-only Fine-Tuning, while maintaining comparable inference efficiency.
