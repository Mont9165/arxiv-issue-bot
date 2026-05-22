# Deterministic vs. Probabilistic Summarisation: An Empirical Trade-off Study in Design Pattern Centric Java Code

- arXiv ID: `2605.21943v1`
- Authors: Najam Nazar, Christoph Treude
- Published: 2026-05-21
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.21943v1) | [pdf](https://arxiv.org/pdf/2605.21943v1)

## Abstract

Background: Automated code summarisation supports program comprehension and documentation, yet the relative strengths and limitations of deterministic (heuristic-based) and probabilistic (LLM-based) pipelines remain unclear. Aims: This paper presents a controlled empirical comparison of these paradigms for intent-oriented design-pattern code summarisation. Method: Using design-pattern-centric Java code as a structured testbed (150 files from three open-source repositories covering nine patterns), we compare a rule-based natural language generation (NLG) pipeline, a Software Word Usage Model (SWUM)-based approach, and a probabilistic pipeline based on the Mixtral LLM. Summaries are evaluated against human references using BERTScore and cosine similarity, complemented by rubric-based judgements produced by Llama 3 across five dimensions: accuracy, conciseness, adequacy, code-context awareness, and design-pattern fidelity. Statistical analysis includes Wilcoxon signed-rank tests (with effect sizes), Friedman tests with post-hoc corrections, and Spearman correlation for sensitivity analysis of rubric consistency. Results: Probabilistic summaries show stronger semantic alignment and richer contextual coverage, while deterministic approaches produce more concise and fully reproducible outputs. Prompt-sensitivity and multi-run analyses indicate variability in LLM outputs, though relative trends remain stable. Conclusions: A clear trade-off emerges: probabilistic methods favour semantic depth and contextual accuracy, whereas deterministic pipelines are preferable for brevity and reproducibility. These findings provide practical guidance for selecting code summarisation techniques.
