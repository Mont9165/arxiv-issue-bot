# SoK: Are LLMs Reliable at Source Code Recovery? A Taxonomy and Empirical Evaluation

- arXiv ID: `2610.11556v1`
- Authors: Varun Kohli, Lee Bing Cheng, Nur Hazim Ghazali, Gao Yuze, Daryl Poon, Dinil Mon Divakaran
- Published: 2026-10-08
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.11556v1) | [pdf](https://arxiv.org/pdf/2610.11556v1)

## Abstract

Effective source recovery is critical to security applications such as malware analysis, vulnerability assessment, and legacy maintenance. Large Language Models (LLMs) are reshaping this field, shifting the paradigm away from rule-based heuristics to probabilistic and high fidelity semantic recovery of source code from assembly or classical decompiler-derived pseudo-C. However, despite rapid progress, the field suffers from fragmentation across numerous approaches as well as their non-unified evaluations, limiting objective comparisons. Further, existing works have limited coverage of embedded, IoT architectures and source languages beyond C/C++. In this work, we present the first Systematization of Knowledge (SoK) focused specifically on LLM-assisted binary-to-source recovery. We provide a granular design-centric taxonomy of LLM-assisted source recovery methods and systematic evaluations using seven key metrics along six evaluation dimensions. We evaluate state-of-the-art methods on 45,000 test samples derived from four standard and five embedded architectures, five optimization levels, and symbol stripping. We ablate the impact of design choices on recovery performance, including input representation, contextual enrichment, model scale, iteration and review roles using controlled in-house recovery pipelines and three off-the-shelf models. Finally, we test same-language and cross-language recovery capability covering four mature and two legacy languages. Our systematization and comprehensive evaluations provide key insights that guide future directions in this field.
