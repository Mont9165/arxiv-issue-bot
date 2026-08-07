# Enhancing LLM-Based Code Translation with Verified Multi-Semantic Representations

- arXiv ID: `2606.11863v1`
- Authors: Yufu Wang, He Jiang, Hao Lin, Peiyu Zou, Ang Jia, Xiaochen Li, Zhilei Ren
- Published: 2026-06-10
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.11863v1) | [pdf](https://arxiv.org/pdf/2606.11863v1)

## Abstract

Large language models (LLMs) have shown great promise for automated code translation, yet existing approaches often rely on token-level statistical patterns rather than sufficient understanding of program semantics. As a result, translated programs may still contain logical and semantic errors. Although high-quality semantic guidance, such as functional descriptions and test cases, can help mitigate these errors, such resources are often unavailable in real-world scenarios. This raises two key challenges: how to construct rich semantic information directly from source code, and how to ensure that such semantics are accurate and reliable enough to guide translation.To address these challenges, we propose Multisage, a multi-semantic augmentation and self-calibration framework for LLM-based code translation. Multisage consists of three modules. First, a semantic representation parsing module extracts structured base semantics from source code, including data-flow graphs, type constraints, and external API information. Second, a multi-semantic augmentation module builds on these representations to generate diverse augmented semantics, including code summaries, function-level test cases, and API-oriented descriptions and tests. Third, a semantic consistency calibration module uses semantics-preserving mutations and cross-semantic consistency verification to filter, calibrate, and refine the generated semantics.Experiments on the HumanEval-X code translation benchmark show that Multisage improves translation success rates by up to 2.22 times across diverse backbone models. It consistently outperforms vanilla prompting, instruction-tuned LLMs, and Chain-of-Thought reasoning, with the largest gains observed on smaller models. These results demonstrate that explicit semantic augmentation can substantially improve the reliability of LLM-based code translation.
