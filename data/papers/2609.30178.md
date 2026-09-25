# NEUROTESTGEN: Neuro-Symbolic Guided Test Generation with Large Language Models

- arXiv ID: `2609.30178v1`
- Authors: Ruixin Zhang, Jiho Shin, Hung Viet Pham, Song Wang
- Published: 2026-09-24
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.30178v1) | [pdf](https://arxiv.org/pdf/2609.30178v1)

## Abstract

Ensuring high structural coverage remains a fundamental challenge in automated test generation, particularly for complex software systems where reaching specific lines or branches requires satisfying intricate control- and data-flow constraints. Large Language Models (LLMs) have recently demonstrated strong capabilities in producing human-like test cases; however, they often struggle to generate inputs that satisfy precise path conditions. Conversely, symbolic execution can systematically derive such constraints, but it often fails to construct realistic, executable test cases and is constrained by scalability limitations.
  In this paper, we introduce NEUROTESTGEN, a hybrid approach that integrates symbolic execution with LLM-driven test synthesis to generate test cases targeting on-demand code coverage. Given a set of target statements within a method, NEUROTESTGEN first employs a symbolic analysis engine (i.e., the Z3 SMT solver) to extract path-specific constraints and construct a symbolic guidance specification for the desired coverage goal. This specification is then used to guide an LLM in synthesizing concrete test cases that are both structurally valid and semantically meaningful. For paths involving complex object-related constraints that are difficult for SMT solvers to handle, NEUROTESTGEN leverages LLMs to infer plausible constraints. Furthermore, NEUROTESTGEN incorporates an iterative feedback loop that validates LLM-generated tests and provides corrective guidance until the target line or branch is covered or a limit is reached. Our empirical evaluation on a widely used benchmark demonstrates that NEUROTESTGEN significantly outperforms the state-of-the-art approach across multiple LLMs, including Llama 3.3 70B1, GPT-4o Mini, Claude 3.5 Haiku3, and Claude Sonnet 4.6.
