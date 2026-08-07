# JETO-Bench: A Reproducible Benchmark for Execution Time Improvement Patches in Java

- arXiv ID: `2606.31767v1`
- Authors: Khashayar Etemadi, Zhendong Su
- Published: 2026-06-30
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.31767v1) | [pdf](https://arxiv.org/pdf/2606.31767v1)

## Abstract

Automated fixing of performance issues is gaining increasing attention. However, existing benchmarks of execution time improvement patches are fixed datasets that target Python, C++, or .NET and cannot be extended to new patches according to user-defined configurations. In this paper, we present JETO-Mine, the first configurable and reusable tool for automatically creating reproducible benchmarks of execution time improvement patches (ETIPs) in real-world Java projects. JETO-Mine employs a three-phase pipeline: a static analysis phase that crawls GitHub repositories and identifies ETIPs using user-defined filters and an LLM-based issue classifier, a dynamic analysis phase that wraps the identified ETIPs in Docker images for fully reproducible execution and performs statistical testing to find objective evidence of execution time improvement, and an evaluation harness that enables quantitative assessment of both generated patches and generated tests. Unlike existing benchmarks, JETO-Mine is designed as a reusable tool that allows researchers continuously collect new benchmarks with their own desired filters and statistical rigor levels. We use JETO-Mine to build JETO-Bench, a benchmark of 660 identified ETIPs and 91 manually verified executable ETIPs collected from 174 open-source Java repositories. To build JETO-Bench, JETO-Mine scans 11 years of open-source development history and nearly 1.8 million commits. We run OpenHands, a leading open-source coding agent, on the 91 manually verified executable ETIPs in JETO-Bench and find that it correctly fixes 14.3% (13/91) of the issues, aligning with results reported by similar studies on other programming languages. Our results also reveal that open-source Java projects largely lack tests that demonstrate execution time improvements, presenting an opportunity for future research in test generation.
