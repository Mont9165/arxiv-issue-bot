# From Metrics to Improvement: A Lifecycle-Aware LLM Feedback Framework for Research Software Quality

- arXiv ID: `2608.23118v1`
- Authors: Nafis Tanveer Islam, Nafiseh Soveizi, Yutong Li, Zhiming Zhao
- Published: 2026-08-24
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.23118v1) | [pdf](https://arxiv.org/pdf/2608.23118v1)

## Abstract

Research software is increasingly central to scientific workflows, yet it is often developed by researchers with limited software engineering expertise. This can lead to quality issues that hinder maintainability, reproducibility, reuse, and sustainability. Existing static analysis tools can identify such issues, but their outputs often require expert interpretation and provide limited support for translating quality assessments into actionable improvements. To address this gap, we propose a lifecycle-aware framework that integrates quantitative software quality assessment with Large Language Model (LLM)-based code refinement. The framework comprises two stages. First, a lifecycle-aware Quality Model is developed from established software quality standards and practitioner requirements. The model defines five quality dimensions and 25 candidate metrics, of which 14 are operationalized using existing analysis tools and custom measurements. Second, the resulting quality diagnostics are used as structured feedback within an iterative LLM-based refinement process, enabling generated improvements to be repeatedly reassessed against the Quality Model. We evaluate the framework on notebook-centric research software using multiple LLMs and compare iterative structured feedback with single-step feedback and unstructured prompting. The results show improvements in specific quality attributes, particularly code duplication and structural quality, while also revealing trade-offs among maintainability, code size, documentation, and complexity. These findings demonstrate the potential of metric-driven LLM feedback for research software quality improvement while highlighting its inherently multi-objective nature \footnote{The source code and experimental data are publicly available at https://github.com/QCDIS/Software_Quality_Control_LLM . }
