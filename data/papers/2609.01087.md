# Fine-Tuning Large Language Models to Classify Pull Request-Issue Alignments: Going Beyond Prompting

- arXiv ID: `2609.01087v1`
- Authors: Mustafa Yasir Altunhan, Hüseyin Özgür Kamalı, Eray Tüzün
- Published: 2026-09-01
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.01087v1) | [pdf](https://arxiv.org/pdf/2609.01087v1)

## Abstract

Context: Accurate alignment between pull requests (PRs) and corresponding issues is crucial for efficient software development and maintaining code quality, as misalignments can reduce traceability, hinder defect localization, and decrease maintainability.
  Objective: This study aims to improve automated PR-issue alignment classification by leveraging fine-tuned large language models (LLMs) across multiple alignment categories, and conducts interpretability analysis to investigate the effects of PR-issue fields on the predictions of fine-tuned LLMs.
  Method: Our methodology consists of dataset preparation, LLM fine-tuning, and interpretability analysis. We first extended an existing dataset and applied data augmentation to address class imbalance. GPT-4o was then fine-tuned via instruction tuning, and open-source LLMs including CodeLlama-7B, CodeQwen1.5-7B, StableCode-3B, CodeGemma-7B, and Deepseek-Coder-6.7B were fine-tuned using classification-specific heads. Interpretability analysis using Shapley Additive Explanations (SHAP) was conducted to examine the influence of PR-issue fields on predictions for the best-performing open-source LLM.
  Results: Fine-tuned LLMs outperformed baseline models, achieving average improvements of 6.15% in accuracy and F1-micro, 14.69% in F1-macro, and 6.15% in recall. CodeLlama-7B emerged as the best-performing fine-tuned LLM overall, while interpretability analysis revealed that code diffs together with issue body and PR body contents exert the greatest influence on predictions.
  Conclusions: Fine-tuning substantially enhances PR-issue alignment classification, improving both accuracy and efficiency. Interpretability analysis provides actionable insights into the dataset features driving alignment decisions, deepening understanding of how LLMs reason over software artifacts.
