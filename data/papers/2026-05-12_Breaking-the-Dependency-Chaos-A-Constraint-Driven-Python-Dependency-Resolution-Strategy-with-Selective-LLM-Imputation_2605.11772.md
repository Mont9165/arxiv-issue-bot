# Breaking the Dependency Chaos: A Constraint-Driven Python Dependency Resolution Strategy with Selective LLM Imputation

- arXiv ID: `2605.11772v1`
- Authors: Kowshik Chowdhury, Dipayan Banik, Shazibul Islam Shamim
- Published: 2026-05-12
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.11772v1) | [pdf](https://arxiv.org/pdf/2605.11772v1)

## Abstract

Dependency resolution is the task of selecting package versions that can be installed together without conflicts. It accounts for a significant share of build failures in modern software projects. In the Python ecosystem, this task is especially challenging due to Python 2/3 incompatibilities, deprecated packages, and widespread missing metadata. Recent work, such as PLLM, tackles this problem by using large language models (LLMs) to infer Python and package versions from code and iteratively repairing them based on build errors. We present SMT-LLM, a hybrid system that replaces LLM-only version guessing with formal constraint solving. SMT-LLM uses deterministic import extraction and Python version detection via abstract syntax tree (AST) analysis, the vermin tool to infer minimum Python versions, and a five-tier import-to-package resolver that queries PyPI before any LLM call. We construct a constraint graph from PyPI metadata and LLM-imputed dependencies for packages with missing metadata, then solve for consistent version assignments using a Z3 satisfiability modulo theories (SMT) solver. On the HG2.9K benchmark using Gemma2:9B (10 GB VRAM), SMT-LLM resolves 83.6% of snippets compared to PLLM's 54.8%, while reducing median resolution time from 151.5 s to 23.9 s (6.3x faster) and average LLM calls from ~24.9 to 2.26 per snippet (11x reduction).
