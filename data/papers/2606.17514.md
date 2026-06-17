# Unlocking LLM Code Correction with Iterative Feedback Loops

- arXiv ID: `2606.17514v1`
- Authors: Le Zhang, Suresh Kothari
- Published: 2026-06-16
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.17514v1) | [pdf](https://arxiv.org/pdf/2606.17514v1)

## Abstract

Large Language Models have shown remarkable capabilities in code generation. However, most existing evaluations focus only on single-attempt accuracy and overlook the iterative refinement process that is central to real-world programming. This study presents a systematic investigation of LLMs' ability to rectify their own code through execution feedback. Using real-world programming problems across four models and two major programming languages, this study evaluates performance using iterative refinement framework where LLMs receive compiler error messages and testcase feedback after each attempt. This study introduces metrics to evaluate code failures, analyze rectification patterns, and compare the effectiveness of reasoning and non-reasoning models, offering actionable insights into both the understanding and practical application of feedback loops in LLM-driven code generation systems. Results show that reasoning models consistently improve over iterations, substantially outperforming non-reasoning models in leveraging feedback, while syntactic and runtime errors are far more tractable than logical or algorithmic failures.
