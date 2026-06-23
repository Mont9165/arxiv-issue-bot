# Revelio: Cost-Efficient Agentic Memory Safety Vulnerability Detection For Repository-Scale Codebases

- arXiv ID: `2606.22263v1`
- Authors: Yiwei Hou, Hao Wang, Muxi Lyu, Marius Momeu, Eric Nguyen, Taige Yang, Koushik Sen, Dawn Song, David Wagner
- Published: 2026-06-20
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.AI`, `cs.MA`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.22263v1) | [pdf](https://arxiv.org/pdf/2606.22263v1)

## Abstract

Memory safety vulnerabilities remain a significant threat even for projects with extensive fuzzing and manual auditing. Recent results suggest that large language models hold great promise for detecting such vulnerabilities, but they are unreliable, at risk of hallucination, and challenging to scale to repository-size codebases. This paper presents Revelio, a cost-efficient end-to-end agentic framework for memory-safety vulnerability discovery. Revelio addresses the problem of hallucination by generating an executable Proof-of-Vulnerability, which is checked with a deterministic sanitizer. It reduces cost using inexpensive LLMs and lightweight static analysis to help generate and rank vulnerability hypotheses, reporting vulnerabilities only when they can be reproduced and confirmed by a sanitizer. We evaluated Revelio on seven production-quality projects that had been continuously fuzzed for five to eight years, as well as on 100 randomly selected Arvo projects from the CyberGym benchmark. With around one hour per project and a total cost of $300, Revelio discovered 19 previously unknown memory-safety vulnerabilities. On benchmarks, Revelio outperformed frontier coding agents across diverse backbone models at comparable token costs. Our results suggest that Revelio enables scalable and trustworthy end-to-end LLM-based memory-safety vulnerability detection.
