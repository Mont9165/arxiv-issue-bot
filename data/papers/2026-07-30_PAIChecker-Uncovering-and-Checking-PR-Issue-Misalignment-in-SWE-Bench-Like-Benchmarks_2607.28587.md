# PAIChecker: Uncovering and Checking PR-Issue Misalignment in SWE-Bench-Like Benchmarks

- arXiv ID: `2607.28587v1`
- Authors: Manyi Wang, Junjielong Xu, Pinjia He
- Published: 2026-07-30
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.28587v1) | [pdf](https://arxiv.org/pdf/2607.28587v1)

## Abstract

SWE-bench-like benchmarks are widely used for evaluating LLM's issue resolution capability. They typically follow a common construction pipeline: each PR (Pull Request) is paired with its linked issue by extracting issue references from the PR description; the issue description is used as the problem statement, and the PR patch serves as the test oracle. However, due to the inherent complexity of developing and maintaining large repositories, such PR-Issue pairings are often misaligned in practice. In this work, we systematically study SWE-bench Verified instances, finding that 13.6% exhibit misalignment across five patterns in eleven fine-grained scenarios. To enable reliable and scalable construction of those benchmarks in the future, we propose PAIChecker, a multi-agent system for checking PR-Issue misalignment in SWE-bench-like benchmarks. Specifically, PAIChecker adopts a three-phase design that combines specific pattern identification, cross-agent label synthesis, and code-level validation, thereby enabling more accurate, generalizable, and progressively verified detection. Experiments on SWE-Gym and SWE-bench Multilingual show that PAIchecker achieves the best performance across all four LLM backbones, reaching up to 92.12% and 91.67% binary accuracy, respectively.
