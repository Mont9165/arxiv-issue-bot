# Less Is More? When Dataset Context Hurts LLM-Generated Dataset Descriptions

- arXiv ID: `2606.02334v1`
- Authors: Lisa-Yao Gan, Arunav Das, Johanna Walker, Klaus Diepold, Elena Simperl
- Published: 2026-06-01
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.02334v1) | [pdf](https://arxiv.org/pdf/2606.02334v1)

## Abstract

Dataset search and reuse are strongly constrained by the quality of metadata such as natural language descriptions, which are often sparse or inconsistent. Although large language models (LLMs) can generate such descriptions automatically, little empirical guidance exists on what makes a good dataset description and what dataset context LLMs actually need. We study these questions through a literature-grounded framework of dataset description quality and a large-scale ablation study using 252 datasets (1,336 CSV files) from the European data portal data.europa.eu. We generate descriptions with LLMs in a baseline scenario and two ablation scenarios: (1) using only dataset titles, (2) titles and schema, and (3) titles, schema and representative data, and evaluate them with an LLM-as-a- judge framework and a semantic descriptive attribute analysis grounded in our quality dimensions. Our results reveal a consis- tent schema penalty: table-schemas alone often degrade narrative quality, while representative data partially restores grounding without improving overall human-facing quality. We further show that different LLMs exhibit stable descriptive personas. These findings provide practical guidance for LLM-supported data publishing workflows.
