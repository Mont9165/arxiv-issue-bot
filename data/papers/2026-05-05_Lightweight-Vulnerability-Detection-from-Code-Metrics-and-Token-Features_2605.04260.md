# Lightweight Vulnerability Detection from Code Metrics and Token Features

- arXiv ID: `2605.04260v1`
- Authors: Chun Yin Chiu
- Published: 2026-05-05
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.04260v1) | [pdf](https://arxiv.org/pdf/2605.04260v1)

## Abstract

Vulnerability detection for C/C++ code increasingly relies on heavy representations such as code graphs and deep models, while many practical workflows still benefit from fast and reproducible ranking baselines for human triage. This preprint studies a lightweight function-level vulnerability triage pipeline that combines sparse token n-grams from raw function text with a small set of inexpensive code metrics, including NLOC, approximate cyclomatic complexity, token count, maximum brace depth, and parameter count. We use TF-IDF token features and a class-weighted logistic regression classifier, avoiding deep learning, transformers, and program graphs.
  Using the Devign function-level labels, we evaluate random and cross-project settings, including a FFmpeg-to-QEMU transfer experiment. We emphasize precision-recall AUC and Recall@10% as ranking-oriented metrics for skewed or triage-oriented workloads. On the random split, the best combined variant reaches PR-AUC 0.642 and Recall@10% 0.161, while cross-project generalization is substantially harder, with PR-AUC around 0.436. We further report ablations, test-only identifier-renaming robustness, and end-to-end efficiency. The results suggest that simple token and metric features provide a useful transparent baseline, but also expose sensitivity to superficial lexical cues and limited cross-project transfer.
