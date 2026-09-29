# WeaveData: A Multimodal Data Analysis System with Self-Critiquing and Self-Evolving LLM Plans

- arXiv ID: `2609.34764v1`
- Authors: Min Jia, Shihao Zhou, Jun-Peng Zhu, Peng Cai, Kai Xu, Chao Zhang, Li Li, Aoying Zhou, Heng Long, Qiu Cui, Liu Tang, Qi Liu
- Published: 2026-09-28
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.34764v1) | [pdf](https://arxiv.org/pdf/2609.34764v1)

## Abstract

Multimodal data analysis, which answers questions over relational tables, text, and images, has attracted growing attention in the data management community. Large language models (LLMs) enable such analysis in natural language by generating analysis plans over relational and semantic operators. However, LLM-generated plans are error-prone: a plan may silently compute something other than what was asked, fail during execution, or return a result that misses the question. This paper presents WeaveData, a multimodal data analysis system with self-critiquing and self-evolving LLM plans. First, WeaveData generates a typed logical plan for each question and critiques it step by step before execution, and it checks the executed result against the question afterwards. Second, WeaveData evolves a plan that fails or misses the question: it diagnoses the failure with the actual data, reuses the results that remain valid, and accumulates planning experience for later questions. Third, WeaveData grounds planning in a metadata knowledge graph of all modalities, clarifies ambiguous questions with the user, and backs every model judgment with evidence in an interactive notebook. We demonstrate WeaveData on two public multimodal datasets.
