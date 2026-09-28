# A Framework for Identifying, Categorizing, and Explaining Bias in AI-Generated Code

- arXiv ID: `2609.30642v1`
- Authors: Manaal Basha, Aimee M. Ribeiro, Gema Rodriguez-Perez
- Published: 2026-09-25
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.30642v1) | [pdf](https://arxiv.org/pdf/2609.30642v1)

## Abstract

As Large Language Models (LLMs) become integrated into software development workflows, concerns regarding unintentional biases in AI-generated code. Although evidence suggests these biases exist, limited research has systematically identified, categorized, and explained them. This study investigates bias in AI-generated code and evaluates whether LLMs can reliably identify and explain it through a taxonomy-driven framework. We extended an existing dataset of biased AI-generated Python code and manually annotated snippets with bias categories and human-authored justifications to establish a ground-truth dataset. Using this dataset, we evaluated proprietary and open-source LLMs as automated bias detection and justification systems through ICL. Finally, we analyzed similarity between LLM-generated explanations and human-authored justifications using structured justification and code identification metrics.
  Our findings demonstrate that LLMs can effectively support code bias identification and explanation. Gemini achieved 80.14% classification accuracy, with 84.0% precision and 95.7% recall, while the best open-source alternative, Qwen3-coder, achieved 82.45% accuracy, 68.64% precision, and 80.22% recall. Additionally, the models achieved justification similarity scores of 80.4% and 80.14%, respectively, relative to human-authored reasoning, and code identification similarity scores of 86.0% and 87.82%. These results suggest that LLMs can detect biased logic in generated Python code and produce explanations that substantially align with expert interpretations.
