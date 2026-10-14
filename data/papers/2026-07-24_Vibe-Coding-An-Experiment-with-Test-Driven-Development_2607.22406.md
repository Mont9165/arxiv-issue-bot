# Vibe Coding: An Experiment with Test-Driven Development

- arXiv ID: `2607.22406v1`
- Authors: Moritz Mock, Barbara Russo
- Published: 2026-07-24
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.22406v1) | [pdf](https://arxiv.org/pdf/2607.22406v1)

## Abstract

Context: Conversational Large Language Models (CLLMs) can automatically generate code by collaborating with users through natural language. However, poor collaboration can lead to poor quality output.
  Objective: This exploratory study aims to investigate how humans and CLLMs can collaborate as peers through vibe coding, an approach that integrates principles from prompt engineering, agile design, and human-AI co-creation to enhance collaboration.
  Method: We designed four interaction models representing different collaboration patterns in the software development process: the solo model (human-only development), the collaborative model (human-CLLM collaboration), the fully automated model (development autonomously performed by a CLLM), and the agentic model (development autonomously performed by the MetaGPT~X platform). Based on these models, we implemented corresponding Test-Driven Development (TDD) workflows using structured prompts and Python scripts. We then conducted a controlled pre-experimental study with TDD professionals to compare the solo and collaborative workflows. In addition, we performed repeated exploratory executions of fully automated and agentic workflows on the same development tasks to obtain complementary evidence.
  Results: Our findings suggest that the choice of interaction model should depend on the development objective. Agentic workflows are best suited for rapid development and functionally correct production code but may introduce additional implementation complexity. However, they may also introduce additional implementation decisions that are not explicitly required by the functional specifications, resulting in untested decision points. In contrast, collaborative workflows produce higher-quality, better-organized test suites.
  Conclusions: Our work explored how...
