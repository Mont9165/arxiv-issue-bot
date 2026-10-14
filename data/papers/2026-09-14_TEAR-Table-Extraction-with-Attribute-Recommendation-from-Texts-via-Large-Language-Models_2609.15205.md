# TEAR: Table Extraction with Attribute Recommendation from Texts via Large Language Models

- arXiv ID: `2609.15205v1`
- Authors: Tong Li, Shuye Ding, Jiachuan Wang, Yongqi Zhang, Shuangyin Li, Lei Chen, Bo Li
- Published: 2026-09-14
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.15205v1) | [pdf](https://arxiv.org/pdf/2609.15205v1)

## Abstract

Table extraction from texts is an important task for information systems, and recent approaches that prompt large language models (LLMs) with instructions have drawn great attention for their strong performance. Existing works have assumed the input texts to be table descriptions or specialized documents. However, these efforts have largely overlooked another prevalent category of texts, commonly found in news reports and social media: naturally occurring texts. Extracting tabular information from such texts poses two distinct challenges. First, high variability and the absence of explicit structural cues make fixed heuristic LLM prompts limited in precisely delineating extraction boundaries. Second, manually predefined schemas cannot capture open-ended, unseen attributes in naturally occurring text. In this paper, we propose a framework, TEAR, to address these challenges. It comprises two synergistic workflows: a Table Extraction Workflow that dynamically adapts instructions to overcome the limitation of heuristic instructions, and an Attribute Recommendation Workflow that discovers new attributes from texts to complement the heuristic schema. To our knowledge, TEAR is the first framework that supports automated text-driven attribute recommendation, enabling exploratory schema design for table extraction. To evaluate TEAR, we establish the benchmark for table extraction and attribute recommendation on naturally occurring texts, including two real-world datasets, manual annotations, appropriate metrics, and baseline comparisons. Experiments show that TEAR achieves state-of-the-art performance on both tasks, and the recommended attributes effectively enhance extraction performance in exploratory scenarios.
