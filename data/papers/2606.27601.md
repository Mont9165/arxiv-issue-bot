# Test Case Selection for Deep Neural Networks: A Replication Study on LLMs for Code

- arXiv ID: `2606.27601v1`
- Authors: Ali Asgari, Mitchell Olsthoorn, Annibale Panichella
- Published: 2026-06-25
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.27601v1) | [pdf](https://arxiv.org/pdf/2606.27601v1)

## Abstract

Recently, test case selection (TCS) techniques have been explored to support the operational evaluation of deep neural networks (DNNs) under limited testing budgets, where labeling cost is a primary concern and uncovering model failures early is a key objective. Although prior studies report promising results, existing empirical evaluations focus almost exclusively on vision-based DNNs and datasets, leaving it unclear whether prior findings generalize to LLM code models. This paper presents a large-scale replication study of TCS techniques in the context of LLM code models. We re-examine established TCS strategies originally proposed for DNNs and complement them with statistical sampling strategies not previously evaluated for TCS. We assess their effectiveness on three code-related classification tasks: clone detection, vulnerability detection, and technical debt prediction. The study spans 17 task-specific fine-tuned model instances, 7 predictive features, and 13 selection strategies, including 12 feature-aware strategies and simple random sampling (SRS) as a feature-agnostic baseline. We evaluate performance along two dimensions: accuracy estimation and early failure discovery. The results indicate that only a subset of findings reported for vision-based DNNs generalize when TCS is applied to LLMs for code. In particular, uncertainty-based features are effective for early failure discovery, while representation-based features are more robust for accuracy estimation. At the same time, performance varies substantially across tasks and models, indicating that TCS effectiveness is context-dependent. Overall, this study provides empirical evidence on the replicability of TCS techniques beyond vision-based deep learning and offers insights into their use for the operational evaluation of LLMs for code.
