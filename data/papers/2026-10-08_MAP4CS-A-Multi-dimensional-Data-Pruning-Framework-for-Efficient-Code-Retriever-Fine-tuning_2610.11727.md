# MAP4CS: A Multi-dimensional Data Pruning Framework for Efficient Code Retriever Fine-tuning

- arXiv ID: `2610.11727v1`
- Authors: Yuxuan Chen, Mingwei Liu, Guangsheng Ou, Zekai Zhang, Zike Li, Yanlin Wang, Pelin Zheng
- Published: 2026-10-08
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2610.11727v1) | [pdf](https://arxiv.org/pdf/2610.11727v1)

## Abstract

Retrieval-Augmented Generation (RAG) has become a cornerstone in software engineering for enhancing Large Language Models (LLMs) with domain-specific knowledge. However, adapting retrievers to evolving code repositories remains challenging due to the noise and redundancy inherent in massive code corpora. Standard fine-tuning on the full corpus is computationally expensive and often leads to sub-optimal performance due to negative transfer from low-quality samples. Conversely, simple random sampling fails to guarantee data representativeness.
  To address these challenges, we propose MAP4CS (Multi-dimensional Awareness Pruning for Code Search), an adaptive data pruning framework. MAP4CS identifies a small, high-quality core subset by integrating syntactic structure, semantic diversity, and distributional representation, followed by a rigorous rule-based filtering pipeline. Extensive experiments on two large-scale datasets demonstrate that MAP4CS consistently outperforms random sampling baselines using only 5% of the training data. Remarkably, it achieves performance comparable to, or even superior to, fine-tuning on the full dataset, validating the ''less is more'' hypothesis in data-centric AI. Furthermore, linguistic analysis reveals an adaptive optimization mechanism: MAP4CS automatically functions as a de-duplicator for redundant corpora and a denoiser for chaotic ones, constructing a training corpus that is both lexically diverse and information-dense.
