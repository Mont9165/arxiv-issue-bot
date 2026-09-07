# Integrating Crash Report Mining and LLMs for Bug Localization and Repair: An Industrial Report

- arXiv ID: `2609.04483v1`
- Authors: Marcos Medeiros, Uirá Kulesza, Christoph Treude, Daniel Lucena, Rafael Gomes, Roberta Coelho, Eiji Adachi, Rodrigo Bonifacio
- Published: 2026-09-03
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.04483v1) | [pdf](https://arxiv.org/pdf/2609.04483v1)

## Abstract

Analyzing crash-report bugs in large-scale industrial software systems requires substantial maintenance effort, particularly in production environments where developers must handle large volumes of crash reports and source code artifacts to localize and fix their root causes. While recent studies have shown that Large Language Models (LLMs) can assist with maintenance tasks, little is known about their effectiveness in supporting developers in analyzing crash-report bugs and repairing bugs associated with groups of crash reports in industrial settings. To address this gap, we investigate whether integrating crash report mining techniques---specifically stack trace clustering and suspicious file and method ranking---with LLMs can support crash localization and repair in production environments. We conduct a retrospective evaluation of five LLMs under four prompt configurations. After that, we chose the best model to run on 38 crash bugs collected from two large Java enterprise systems. We further analyze the structural characteristics and explanatory patterns of LLM-generated responses and assess localization and repair effectiveness through manual validation. Our results show that the best-performing configuration localizes up to 71% and correctly repairs 52% of crash bugs on the full dataset. These findings provide empirical evidence that combining crash report mining with LLM-based repair can effectively support debugging activities in industrial maintenance workflows.
