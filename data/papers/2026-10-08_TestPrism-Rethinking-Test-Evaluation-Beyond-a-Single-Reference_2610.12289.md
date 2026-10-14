# TestPrism: Rethinking Test Evaluation Beyond a Single Reference

- arXiv ID: `2610.12289v1`
- Authors: Han Li, Lingxiang Hu, Jiacheng Huang, Ziqian Jiang, Jingkai Luo, Wei Gao, Yunfan Tan, Zun Wang, Jiaheng Liu
- Published: 2026-10-08
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.12289v1) | [pdf](https://arxiv.org/pdf/2610.12289v1)

## Abstract

Large language model (LLM) coding agents have advanced test generation across diverse programming tasks. However, the common practice of evaluating tests against a single reference solution overlooks alternative valid implementations and can overstate test quality. We introduce TestPrism, comprising 300 test tasks from 17 sources and 3000 candidate implementations, evenly split between valid and invalid solutions. Its primary metric, Joint Success Function, requires the generated tests to fail on the initial program state, accept every valid candidate, and reject every invalid candidate. Across fourteen baseline coding agent configurations, Joint Success Function reaches only 28.00%, whereas single reference success reaches 59.67%. Our analysis reveals missed behaviors, unsupported assertions, and faulty test construction. To address these weaknesses, we introduce TestHelix, which combines heterogeneous synthesis of test and repair pairs with peer cross validation and recursive self improvement (RSI). Across two models, TestHelix improves Joint Success Function by 8.67 to 9.00 percentage points over the native harness comparators in the TestHelix evaluation
