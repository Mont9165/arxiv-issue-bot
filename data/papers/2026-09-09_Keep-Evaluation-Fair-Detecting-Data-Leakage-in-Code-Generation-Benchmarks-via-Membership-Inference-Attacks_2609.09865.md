# Keep Evaluation Fair: Detecting Data Leakage in Code Generation Benchmarks via Membership Inference Attacks

- arXiv ID: `2609.09865v1`
- Authors: Dongdong Zhao, Jian Chen, Guancheng Lin, Jianwen Xiang, Jacky Wai Keung, Xiao Yu
- Published: 2026-09-09
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.09865v1) | [pdf](https://arxiv.org/pdf/2609.09865v1)

## Abstract

Code generation benchmarks are widely used to evaluate Large Language Models (LLMs), but benchmark data leakage into training sets can inflate performance and undermine evaluation validity. DetectLeak, a method specifically designed for code generation benchmark leakage detection, relies on perplexity scores to identify likely leaked samples. However, perplexity mainly reflects general familiarity with code patterns and may perform poorly on complex or rare samples. It also overlooks other useful signals, such as code similarity, functional correctness, and semantic representations. To address these limitations, we propose CGMIA (Code-Generation-specific Membership Inference Attack), a method for detecting leakage in code generation benchmarks. CGMIA fine-tunes a shadow model on a subset of benchmark samples to construct labeled member and non-member data. For each sample, it collects the input prompt, generated code, and reference solution, and extracts expert features, including CodeBLEU, edit distance, test pass rate, and perplexity, together with semantic features from CodeBERT embeddings. An integrated learning module combines these features to capture both surface-level memorization signals and deeper behavioral patterns, enabling a classifier to predict whether a sample was included in the target model's training set. Experiments on eight code generation benchmarks show that CGMIA outperforms eight existing membership inference methods in most cases. It also effectively detects known leaked APPS samples in StarCoder-7B's training data.
