# Think Before You Code: A Benchmark for Testing LLMs on Software Engineering Deliberation

- arXiv ID: `2611.22905v1`
- Authors: Ashman Mehra
- Published: 2026-11-17
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.22905v1) | [pdf](https://arxiv.org/pdf/2611.22905v1)

## Abstract

Think Before You Code (TBYC) is a benchmark pipeline for studying whether code-focused language models can reason about software issues in ways that resemble human engineering deliberation. The benchmark curates GitHub issue discussions into structured records, extracts human discussion artifacts such as problems, solutions, constraints, rationales, and trade-offs, and then prompts models to generate issue-level "thoughts" using retrieved code context and few-shot examples. It converts model responses back into the same artifact space and evaluates them against human annotations using complementary metrics for artifact type detection, metadata matching, tag overlap, and semantic summary similarity. Beyond scoring, this study includes visualization, leaderboard, and baseline tools that make it possible to compare models, prompting strategies, and extraction methods across repositories and issues. Think Before You Code is an end-to-end evaluation environment for measuring how closely LLM software reasoning aligns with human strategic judgment.
