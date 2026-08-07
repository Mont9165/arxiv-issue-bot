# TCellAlign: Cross-study T-cell Populations Alignment with Nomenclature-Guided Multi-Agent Workflow

- arXiv ID: `2607.24093v1`
- Authors: Pengyu Xie, Rongjia Zhou, Zhilin Ou, Junyuan Zhang, Xiang Zhou, Xiaobo Sun, Jiaying Lu, Wenjing Ma
- Published: 2026-07-27
- Primary category: `q-bio.QM`
- Categories: `q-bio.QM`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.24093v1) | [pdf](https://arxiv.org/pdf/2607.24093v1)

## Abstract

Cell type standardization plays a central role in integrating biological knowledge across single-cell studies. While standardized resources (e.g., Cell Ontology, Nomenclature Frameworks) provide unified vocabularies of cell populations, scientific publications and public datasets continue to use heterogeneous study-specific labels, making cross-study comparison difficult even when biologically equivalent cell populations are described. In this work, we are the first to formulate this challenge as an evidence-grounded cell population alignment problem and propose TCellAlign, a multi-agent framework that includes literature retrieval, information extraction, nomenclature-guided label alignment, and evidence-based adjudication. This modular design preserves the original terminology and supporting evidence reported by each study while producing standardized labels that can be compared across studies. We further construct a manually validated benchmark dataset linking study-specific labels, CZ CELLxGENE annotations, and standardized T-cell nomenclature across 44 manually curated, published studies (including over seven million cells) spanning four biological categories: healthy, cancer, infectious disease and inflammatory diseases. Across the evaluated tasks, TCellAlign achieves stronger semantic agreement than ontology-based baselines and maintains transcriptomic coherence with both open-source and closed-source large language models (LLM) backbones. By connecting literature, datasets, and expert's nomenclature, TCellAlign enables consistent interpretation of T-cell subtypes and states across studies, facilitating biological knowledge integration and the development of future foundation models built upon standardized cellular representations.
