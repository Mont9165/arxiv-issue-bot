# Code-as-Auditor: Executable Compliance Reasoning via Regulation-to-Code

- arXiv ID: `2609.19199v1`
- Authors: Jisoo Kim, Taeyoon Kwack, Jinwoo Jang, Woo Kyung Kim, Honguk Woo
- Published: 2026-09-16
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.19199v1) | [pdf](https://arxiv.org/pdf/2609.19199v1)

## Abstract

Large Language Models (LLMs) are increasingly adopted for compliance and legal reasoning tasks, yet their outputs often lack explicit grounding in legal logic and evidence. We present Code-as-Auditor, an LLM-based framework that extends the model's reasoning capability toward structured and evidence-grounded compliance assessment. The framework translates regulatory information into (1) formalized checklists and executable decision trees, encoding regulations and conditions as interpretable code structures. During inference, each checklist item is (2) dynamically expanded into factual and counterfactual questions, guiding the model to reason over case-specific evidence and potential violations. This process establishes a reasoning pipeline that proceeds from evidence identification, through rule application, to final decision-making, while a self-verification loop improves the logical consistency of the generated code and the traceability of outcomes. Experiments on privacy and data protection scenarios demonstrate that Code-as-Auditor delivers more accurate and evidence-backed evaluations, enabling automated compliance regulation checking grounded in explicit regulatory criteria.
