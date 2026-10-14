# Bridging Behavior and Implementation: Automated Java Glue Code Generation for Behavior-Driven Development

- arXiv ID: `2607.19703v1`
- Authors: Xinyu Shi, Zhou Yang, An Ran Chen
- Published: 2026-07-22
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.19703v1) | [pdf](https://arxiv.org/pdf/2607.19703v1)

## Abstract

Behavior-Driven Development (BDD) helps technical and non-technical stakeholders share a common understanding of software requirements through natural-language scenarios. Glue code makes these scenarios executable by mapping each step to the corresponding project code. However, developing and maintaining glue code requires knowledge of both the intended behavior and the underlying codebase, making it a labor-intensive part of BDD as requirements evolve. Although large language models (LLMs) have shown strong code generation capabilities, their use for automated glue code generation remains unexplored. This task requires reasoning over underspecified behavior, related BDD artifacts, and large project codebases. We present AutoGlue, a hierarchical multi-agent framework for automated Java glue code generation. AutoGlue follows a behavior-first workflow that separates behavior interpretation, context retrieval, and code generation. A Behavior Interpreter derives the intent of a step from its scenario context, while a Developer agent retrieves relevant BDD artifacts and project code before generating the final glue code. We evaluate AutoGlue on 1,307 steps from eight open-source Java projects. Compared with few-shot prompting, AutoGlue improves API F1 by 58.7% and CodeBLEU by 43.7%. It produces directly usable glue code for 46.1% of the evaluated steps, while most partially correct outputs require only minor revisions, such as adding missing actions or refining parameters. Ablation results show that behavior interpretation and project-aware context retrieval both contribute substantially to generation quality. These findings demonstrate that LLMs can effectively connect natural-language behavior specifications with project code and support specification-driven software development.
