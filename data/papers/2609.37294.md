# SafeLLM4SE: Statistical Evaluation and Reporting for LLM-based Software Engineering Systems

- arXiv ID: `2609.37294v1`
- Authors: Francisco Ortin
- Published: 2026-09-29
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2609.37294v1) | [pdf](https://arxiv.org/pdf/2609.37294v1)

## Abstract

Large language models (LLMs) are increasingly used for software engineering tasks, yet their stochastic behavior challenges the validity, reproducibility, and comparability of their evaluations. Conventional practices such as reporting a single output, an average score, best-of-N, or pass@k performance can obscure variability and estimation uncertainty, potentially leading to misleading conclusions about system reliability. This article presents SafeLLM4SE, a practical methodology and reporting standard for statistically principled evaluation of LLM-based software engineering systems. Rather than treating generated outputs as deterministic artifacts, SafeLLM4SE treats them as realizations of a stochastic process and distinguishes quality, stability, and estimation uncertainty. It combines adaptive sampling with confidence intervals, distribution-aware statistical comparisons, effect sizes, and a minimum reporting standard covering model configuration, reproducibility, evaluation procedures, and resource usage. SafeLLM4SE is also provided as an open-source software package available on PyPI, enabling researchers and practitioners to reproduce and extend the methodology. We illustrate its application by comparing two LLMs on HumanEval, a benchmark of programming problems assessed through functional tests.
