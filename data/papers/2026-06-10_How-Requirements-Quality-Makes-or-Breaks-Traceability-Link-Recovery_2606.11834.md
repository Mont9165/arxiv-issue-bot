# How Requirements Quality Makes (or Breaks) Traceability Link Recovery

- arXiv ID: `2606.11834v1`
- Authors: Tobias Hey, Julian Frattini
- Published: 2026-06-10
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.11834v1) | [pdf](https://arxiv.org/pdf/2606.11834v1)

## Abstract

Traceability information between requirements and source code greatly benefits the maintenance of a software system. Since manually establishing trace links is cumbersome and error-prone, previous research explored automated traceability link recovery (TLR) approaches to support this task. However, quality defects in requirements impact subsequent activities such as TLR, yet evidence about this remains scarce. Our objective is to contribute empirical evidence on this impact. At the same time, we aim to understand how the performance of TLR approaches varies given these quality defects. To this end, we annotated 28 types of quality defect in 189 use case descriptions from two datasets. Then, we executed five distinct TLR approaches on the dataset and measured their performance in recovering trace links. Finally, we performed statistical tests to quantify the defects' effect strength on this performance. Our results show that some quality defects harm TLR performance, e.g., sentences that do not start with noun phrases, while others actually benefit performance, e.g., use cases that include implementation details. Moreover, different types of approaches respond differently to these defects. As a consequence, the performance-optimizing choice of a TLR approach depends on the quality of the dataset.
