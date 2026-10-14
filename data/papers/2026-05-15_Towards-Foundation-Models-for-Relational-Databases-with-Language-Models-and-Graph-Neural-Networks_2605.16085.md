# Towards Foundation Models for Relational Databases with Language Models and Graph Neural Networks

- arXiv ID: `2605.16085v1`
- Authors: Jingcheng Wu, Ratan Bahadur Thapa, Mojtaba Nayyeri, Lucas Etteldorf, Max Finkenbeiner, Fabian Leeske, Steffen Staab
- Published: 2026-05-15
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.16085v1) | [pdf](https://arxiv.org/pdf/2605.16085v1)

## Abstract

Relational databases store much of the world's structured information, and they are essential for driving complex predictive applications. However, deep learning progress on relational data remains limited, as conventional approaches flatten databases into single tables via manual feature engineering, discarding relational context. Relational deep learning (RDL) addresses this by modeling databases as relational entity graphs (REGs) for graph neural networks (GNNs), but remains task- and database-specific. To combine the strengths of both paradigms, we propose a hybrid architecture combining a fine-tuned BART encoder to capture intra-row semantics with a GraphSAGE-based GNN over REGs to inject relational context. Experiments on RelBench show that the GNN substantially enriches BART's row embeddings, achieving a ROC-AUC of 67.40 on the driver-dnf task from the rel-f1 dataset. This performance is competitive with supervised baselines such as LightGBM (68.86) and narrows the gap to RDL (72.62) to within 5.22 points, though a substantial gap remains to state-of-the-art foundation models such as KumoRFM (82.63). These results suggest that lightweight hybrid LM-GNN architectures offer a promising and resource-efficient path towards foundation models for relational databases.
