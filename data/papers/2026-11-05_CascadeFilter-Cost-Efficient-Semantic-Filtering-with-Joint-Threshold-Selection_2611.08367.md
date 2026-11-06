# CascadeFilter: Cost-Efficient Semantic Filtering with Joint Threshold Selection

- arXiv ID: `2611.08367v1`
- Authors: Yanji He, Tao Zhong, Hongyang Chen, Xiaobo Zhang, Mingyu Yang, Wei Wang
- Published: 2026-11-05
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.08367v1) | [pdf](https://arxiv.org/pdf/2611.08367v1)

## Abstract

Semantic filtering selects records that satisfy a natural-language predicate and is an important operation in data analytics based on large language models (LLMs). Executing an expensive model on every document incurs substantial inference cost. Existing approaches reduce this cost by accepting predictions from cheaper models and forwarding uncertain records to an oracle. Task Cascades further varies document portions and operations, and provides an accuracy-guaranteed extension. However, its threshold calibration follows a prescribed adjustment sequence after cascade assembly, rather than minimizing cost over alternative combinations of stage thresholds.
  Motivated by this, we propose CascadeFilter, a three-stage semantic filtering method that jointly searches the thresholds for a small language model operating on extracted evidence and full documents, with unresolved records forwarded to the oracle. For a fixed cascade, we formulate threshold selection as minimizing token-aware cost subject to an oracle-relative error constraint, and select the least-cost certified configuration in a pre-specified grid. A finite-population calibration procedure bounds oracle-relative error after selection, using fixed-sequence tests on threshold tracks to allocate the multiple-testing budget. We further combine lexical and dense retrieval, reranking, and neighborhood-supported confidence to improve evidence extraction and routing. These components enhance the cascade while leaving its certification interface unchanged. Across six datasets and 13 evaluation settings, the reported results have the highest benchmark accuracy and macro-averaged F1 score in 12 settings each. These comparisons describe the reported operating points; the accuracy guarantee concerns agreement with the oracle.
