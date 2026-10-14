# LabelMate: An LLM-Driven Framework for Refined Issue Report Labeling

- arXiv ID: `2609.04055v1`
- Authors: Liam Johnston, Shayan Noei, Maram Assi, Ying Zou
- Published: 2026-09-03
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.04055v1) | [pdf](https://arxiv.org/pdf/2609.04055v1)

## Abstract

Software users often submit issue reports to a product's issue tracking system to report defects, suggest enhancements, or raise other product-related concerns. Labeling these issue reports supports effective planning and improves community engagement. However, many issue reports remain unlabeled due to the substantial manual effort required to design an appropriate label taxonomy, then assign suitable labels from this taxonomy to new issue reports. Existing automated labeling approaches attempt to mitigate these challenges. However, they suffer from key limitations, such as extensive manual intervention, the assignment of generic labels, and a dependence on existing labeled datasets. To address these limitations, we propose LabelMate, a novel Large Language Model (LLM)-driven framework that (1) derives a comprehensive, project-specific label set from historical issue reports and (2) automatically assigns relevant labels to new issue reports without requiring any pre-labeled training data. We evaluate LabelMate on 16,500 issue reports from 30 popular and diverse GitHub repositories. Based on this dataset, our approach generates a coherent list of 275 labels and achieves an average labeling accuracy of 89.84%, a statistically significant improvement over existing generic label assigning approaches. These results demonstrate that LabelMate offers an efficient, domain-adaptive solution to streamline the issue labeling process.
