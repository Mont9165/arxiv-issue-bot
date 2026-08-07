# Data Profiling for Change Rules

- arXiv ID: `2606.07860v1`
- Authors: Nishttha Sharma, Fei Chiang
- Published: 2026-06-05
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.07860v1) | [pdf](https://arxiv.org/pdf/2606.07860v1)

## Abstract

Understanding data change is critical towards understanding trends, normal vs. abnormal behaviours, recognizing patterns, and the causes of change. Existing database systems have limited support for change management, relying on statistics, triggers, and constraints. Data quality rules model sequential changes along a restricted set of attributes, quantify change among unordered tuples, and have limited ability to model the context under which attribute changes occur. In this paper, we introduce Change Rules (CRs) that quantify the sequential changes among ordered tuples in both the antecedent and consequent attributes. CRs aim to address the limitations of existing declarative dependencies to support trend analysis and causal relationships that trigger change among attributes. We propose CR-Miner, an automated algorithm for CR discovery that generates candidate change intervals in a level-wise manner. Experimental results show that CR-Miner achieves an average runtime improvement of 40-50% over existing baselines.
