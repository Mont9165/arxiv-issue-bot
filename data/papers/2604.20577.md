# Evaluating Assurance Cases as Text-Attributed Graphs for Structure and Provenance Analysis

- arXiv ID: `2604.20577v1`
- Authors: Fariz Ikhwantri, Dusica Marijan
- Published: 2026-04-22
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2604.20577v1) | [pdf](https://arxiv.org/pdf/2604.20577v1)

## Abstract

An assurance case is a structured argument document that justifies claims about a system's requirements or properties, which are supported by evidence. In regulated domains, these are crucial for meeting compliance and safety requirements to industry standards. We propose a graph diagnostic framework for analysing the structure and provenance of assurance cases. We focus on two main tasks: (1) link prediction, to learn and identify connections between argument elements, and (2) graph classification, to differentiate between assurance cases created by a state-of-the-art large language model and those created by humans, aiming to detect bias. We compiled a publicly available dataset of assurance cases, represented as graphs with nodes and edges, supporting both link prediction and provenance analysis. Experiments show that graph neural networks (GNNs) achieve strong link prediction performance (ROC-AUC 0.760) on real assurance cases and generalise well across domains and semi-supervised settings. For provenance detection, GNNs effectively distinguish human-authored from LLM-generated cases (F1 0.94). We observed that LLM-generated assurance cases have different hierarchical linking patterns compared to human-authored cases. Furthermore, existing GNN explanation methods show only moderate faithfulness, revealing a gap between predicted reasoning and the true argument structure.
