# SQLMorph: Query Mutation and Fine-Grained Metrics for Text-to-SQL Evaluation

- arXiv ID: `2609.08950v1`
- Authors: Mohammadhossein Malekpour, Mohamed Riahi, Maxime Lamothe, Amine Mhedhbi
- Published: 2026-09-08
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.08950v1) | [pdf](https://arxiv.org/pdf/2609.08950v1)

## Abstract

Text-to-SQL systems translate natural language queries into executable SQL, democratizing access to structured data. Despite recent advances driven by large language models (LLMs), evaluation remains a major bottleneck: public benchmarks fail to capture the complexity of enterprise schema, while building private evaluation sets is costly and nondeterministic, making evaluation results difficult to reproduce. To address this issue, we present SQLMorph, a framework for Text-to-SQL evaluation via query mutation. SQLMorph introduces two techniques to automatically generate and expand evaluation sets: Join Query Expansion (JQE), which systematically increases structural complexity through valid join additions, and Textual Query Augmentation (TQA), which generates controlled natural language perturbations to assess robustness to linguistic variation. JQE and TQA create targeted choke points to challenge specific system components. When applied to state-of-the-art systems, JQE increases query coverage and reveals accuracy degradation as the number of joins grows. Meanwhile, TQA shows that linguistic brittleness induced by heavy abbreviation can reduce accuracy by up to 17%.
  Beyond evaluation sets, SQLMorph introduces a family of execution-level metrics that address the limitations of current binary measures, such as Execution Accuracy. We define Execution Precision (EXP) and Execution Recall (EXR) to quantify the fraction of correct and recovered results, respectively, and combine them via F1 for unified scoring. Our experiments show that these relaxed metrics enable fine-grained analysis of over- and under-prediction, revealing differences across systems that binary metrics obscure. Together, SQLMorph's query mutation and fine-grained metrics support debugging and better align Text-to-SQL evaluation practices with real-world deployments.
