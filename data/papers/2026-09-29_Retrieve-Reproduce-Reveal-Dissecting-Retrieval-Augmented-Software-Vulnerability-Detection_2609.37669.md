# Retrieve, Reproduce, Reveal: Dissecting Retrieval-Augmented Software Vulnerability Detection

- arXiv ID: `2609.37669v1`
- Authors: Sabrina Kaniewski, Tim Krämer, Julius Bächle, Markus Enzweiler, Michael Menth, Tobias Heer
- Published: 2026-09-29
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.37669v1) | [pdf](https://arxiv.org/pdf/2609.37669v1)

## Abstract

Retrieval-Augmented Generation (RAG) is increasingly used to enhance Large Language Model (LLM)-based software vulnerability detection by grounding predictions in retrieved vulnerability knowledge, such as vulnerability reports. However, existing RAG-based software vulnerability detection (RAG4SVD) systems are often evaluated using proprietary models, which challenges open science and reproducibility. Further, studies use different datasets, custom knowledge bases, different backbone models, and diverse metrics, which hinders meaningful cross-system comparison. In this work, we study six open-source RAG4SVD systems and address these reproducibility and comparability challenges through (i) reproduction of their experimental settings under an open-weight setting, and (ii) a unified benchmark using a common dataset, metric suite, and pool of open-weight models. Further, RAG4SVD systems typically consist of multiple components, yet are often evaluated only as a whole system, i.e., end-to-end. Therefore, we perform (iii) a component-level analysis that decomposes representative RAG4SVD pipelines into input abstraction, knowledge retrieval, and detection. Our results demonstrate that reproducibility varies substantially across systems. Under the presented unified benchmark, published RAG4SVD performance does not transfer under a controlled open-weight evaluation and depends strongly on the used model. The component analysis shows that effective RAG4SVD depends on the alignment between pipeline stages. For example, oracle knowledge raises retrieval to near-optimal, yet performance remains low (0.51 pairwise accuracy), demonstrating that retrieval effectiveness alone is insufficient for reliable detection. These findings motivate evaluating RAG4SVD not only end-to-end, but at the level of pipeline components, and provide a basis for more standardized, RAG-aware evaluation practices.
