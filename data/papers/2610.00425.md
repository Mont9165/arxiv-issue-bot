# Code That Works, Environments That Don't: Measuring Environment Reproducibility in AI-Generated Software

- arXiv ID: `2610.00425v1`
- Authors: Bhanu Prakash Vangala, Tanu Malik
- Published: 2026-09-30
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2610.00425v1) | [pdf](https://arxiv.org/pdf/2610.00425v1)

## Abstract

Code generation has emerged as a central capability of large language models, with coding agents now able to produce functionally correct software projects from natural language prompts. However, functional correctness alone does not capture a critical dimension of generation quality: environment specification, defined as the accurate identification of the dependencies required to execute generated code, is equally critical. We develop an agent protocol for environment specification and introduce a three-layer framework comprising declared, runtime-installed, and necessary-and-sufficient dependencies to systematically assess coding agents for environment specification. Using this protocol, we evaluate the extent to which coding agents systematically misspecify software environment dependencies and how this misspecification varies across three agents, four languages, and fifty programming tasks. Our results show that current coding agents exhibit systematic generalization failures along this dimension, producing dependency specifications that are inconsistent, redundant, or incomplete in ways that functional tests do not detect. Across agents, dependency set agreement is as low as 7% for identical tasks, and newer agents show no meaningful improvement, suggesting the failure is not resolved by scale or recency. The largest divergence occurs between the declared and runtime dependency layers, implicating environment priors learned from the models' training distributions as the primary driver. Our findings establish environment specification as a distinct, measurable axis of code generation quality that current benchmarks do not capture, and motivate training objectives and evaluation protocols that jointly optimize for functional correctness and environmental portability.
