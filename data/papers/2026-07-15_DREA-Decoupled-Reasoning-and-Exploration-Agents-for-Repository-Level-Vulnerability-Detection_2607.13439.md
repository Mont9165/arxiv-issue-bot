# DREA: Decoupled Reasoning and Exploration Agents for Repository-Level Vulnerability Detection

- arXiv ID: `2607.13439v1`
- Authors: Mingyang Sun, Guozhu Meng
- Published: 2026-07-15
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.13439v1) | [pdf](https://arxiv.org/pdf/2607.13439v1)

## Abstract

Large language models (LLMs) are increasingly applied to vulnerability detection due to their strong code comprehension capabilities, but most existing approaches rely on isolated functions or context extracted by fixed program-analysis rules. These methods cannot adaptively explore repository-level dependencies to gather sufficient context when vulnerabilities span multiple functions or files, compromising detection reliability. We present DREA (Decoupled Reasoning and Exploration Agents), a hypothesis-driven framework for repository-level vulnerability detection. DREA decouples reasoning from exploration through two collaborating agents: a planning agent backed by an advanced LLM that forms vulnerability hypotheses and directs the investigation, and an explorer agent powered by a lightweight model that retrieves repository-level context on demand. Goal-directed context acquisition is the primary source of detection improvement in this design, while offloading token-heavy exploration to the local model keeps inference economically tractable. To support evaluation, we construct RepoPairBench, a repository-grounded benchmark of validated Python vulnerability-fix pairs from real-world projects. Beyond binary detection accuracy, we introduce a reasoning correctness evaluation to assess whether a model's rationale matches the documented vulnerability mechanism. Across three LLMs, DREA improves Pair-Correctness from 19-26% to 30-42% while offloading over 93% of tokens to the explorer, reducing estimated billable API cost by a factor of 16-48. Reasoning correctness analysis further reveals that 26-55% of true positives, for both DREA and the function-only baseline, are correct predictions supported by flawed rationales, identifying security reasoning quality as a shared bottleneck for current LLMs.
