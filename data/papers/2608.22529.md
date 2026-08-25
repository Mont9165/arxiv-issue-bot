# Benchmarking the Titans: A Multi-Dimensional Empirical Evaluation of LLM Code Generation Quality in the .NET Ecosystem

- arXiv ID: `2608.22529v1`
- Authors: Seyed Mohammad Mahdi Ghalandarian, Majid Bazargani, Masoumeh Taromirad
- Published: 2026-08-23
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.22529v1) | [pdf](https://arxiv.org/pdf/2608.22529v1)

## Abstract

Evaluating Large Language Model (LLM) code generation quality requires examining not just whether the generated code is correct, but whether it is maintainable, efficient, and stylistically sound, all of which are qualities of direct importance to software engineering practitioners. Existing benchmarks reduce evaluation to a single Pass@k metric, which obscures critical trade-offs between functional correctness and structural quality. A further limitation is the near-exclusive focus on Python, leaving enterprise-relevant ecosystems such as C# and .NET without dedicated evaluation. This paper presents an automated, multi-dimensional evaluation framework for C# code generation, applying it to four state-of-the-art LLMs: GPT, Gemini, Claude, and Grok. We conduct a controlled experiment across 85 algorithmic tasks derived from HumanEval, generating and evaluating 340 solutions in total, in which each solution is assessed across three independent dimensions: functional correctness via automated unit testing, static code quality via Roslyn AST analysis, and runtime efficiency via adversarial BenchmarkDotNet profiling. Our central finding reveals a substantial gap between correctness and quality attributes (Pearson r = 0.075), demonstrating that Pass@k rankings systematically misrepresent the full LLM performance profile in software engineering contexts. We further characterize GPT's bimodal failure behavior.
