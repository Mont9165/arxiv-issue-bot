# Automated Classification of Human Code Review Comments with Large Language Models

- arXiv ID: `2604.23667v1`
- Authors: Semih Çağlar, Şükrü Eren Gökırmak, Eray Tüzün
- Published: 2026-04-26
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.23667v1) | [pdf](https://arxiv.org/pdf/2604.23667v1)

## Abstract

Context: Code reviews are essential for maintaining software quality, yet many human review comments suffer from issues such as redundancy, vagueness, or lack of constructiveness. These types of comments may slow down feedback and obscure important insights. Prior work on code review comments mostly explore the detection and categorization of useful comments, while fine-grained categorization of comment issues remains underexplored.
  Objective: This work aims to design and evaluate an automated system for classifying code review comments according to specific categories of issues.
  Methodology: We introduced a nine-label taxonomy for code review comments, covering six review comment smells and three common useful intents, and manually labeled 448 comments from a publicly available dataset. We benchmarked zero-shot and one-shot single-label classification over each comment and its associated unified diff hunk, comparing GPT-5-mini, LLaMA-3.3, and DeepSeek-R1. We reported macro-F1 as the primary metric.
  Results: Zero-shot performance was moderate under class imbalance (macro-F1 0.360 to 0.374). One-shot exemplar conditioning had model-dependent effects: GPT-5-mini and DeepSeek-R1 macro-F1 scores improved, however LLaMA-3.3 suffered a slight decrease. Exemplars most consistently helped intent-boundary labels, whereas classification of evidence-sensitive labels remain challenging.
  Conclusion: Our results indicate that comment--diff evidence is sufficient for some labels but limited for evidence-sensitive smells. Future work includes adding thread context, improving intent-preserving rewrites, and validating robustness across platforms.
