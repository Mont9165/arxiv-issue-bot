# PyMETA: A Benchmark Dataset for Hierarchical Student Code Error Classification with Python-Interpreter-Based Labels

- arXiv ID: `2606.30610v1`
- Authors: Chuyue Li, Ziqi Tang, Jingyi Wang, Yu Wu, Kazuma Hashimoto, Lingyu Gao
- Published: 2026-06-29
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.30610v1) | [pdf](https://arxiv.org/pdf/2606.30610v1)

## Abstract

With the advancement of Large Language Models (LLMs), code error detection has extended beyond traditional IDE diagnostics to context-sensitive debugging in educational scenarios. However, existing approaches lack large-scale datasets, multi-error analysis, and unified error taxonomies. To address this, we introduce PyMETA, a large-scale Python code error classification dataset of 48,646 student submissions, with single-error labels for all samples and a diagnostic subset of 97 expert-annotated multi-error samples. The dataset uses a three-level hierarchical taxonomy, from a binary error/no-error split down to 14 fine-grained error types grounded in Python's official exception hierarchy. We evaluate multi-level classification tasks on two finetuned models and four LLMs with prompting, comparing their classification performance and runtime cost. For multi-error prompting, the best model, Gemini 2.5 Pro, achieves 81.8% macro F1 under the "contains" criterion. We observe that: 1) prompted LLMs still underperform finetuned smaller models; 2) models exhibit significant disparities across error types; 3) most LLMs over-classify code as Logic Error, with GPT-3.5 showing the highest Logic Error Overprediction Rate and Gemini 2.5 Pro the lowest. Our work establishes a data foundation and provides insights for LLM-based code error research.
