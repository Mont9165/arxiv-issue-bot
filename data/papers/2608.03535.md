# CodeAssay: A Multi-Metric Benchmark with Audited Ground Truth for LLM Code Generation

- arXiv ID: `2608.03535v1`
- Authors: Shahbaz Siddeeq, Muhammad Waseem, Umar Subhan Malhi, Pekka Abrahamsson
- Published: 2026-08-04
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.03535v1) | [pdf](https://arxiv.org/pdf/2608.03535v1)

## Abstract

Large Language Models are increasingly evaluated for code generation using test-based benchmarks. The validity of such evaluations depends on the reliability of their references and tests, while test-based correctness captures only part of the observable properties of generated code. We present CodeAssay, a taxonomy-first benchmark of 185 Python tasks across ten software-engineering categories. It combines audited ground truth, public tests for generation and repair, hidden tests for grading, mutation-based test-suite validation, and selected code-property measures. Regrading fixed model outputs after the audit changed 170 of 1,890 correctness labels (9.0%) and increased the measured best-to-worst model spread from 11.9 to 23.7 percentage points, although aggregate correctness remained nearly unchanged. The complete and hidden test suites achieved mutation scores of 82.6% and 74.8%, respectively. Across seven proprietary LLMs, standard-prompt correctness ranged from 77.3% to 98.9%, with significant differences in 12 of 21 model pairs. On the 120 tasks solved by all 14 model-prompt configurations, no model performed best across all selected code properties. A security-focused prompt produced no significant change in correctness or consistent reduction in the selected static-analysis findings, while increasing program length and cyclomatic complexity across all models. These findings show that reliable evaluation of LLM-generated code requires validated ground truth, protected tests, and multiple explicitly interpreted measures. CodeAssay provides a reproducible basis for evidence-based model evaluation in AI-augmented software development.
