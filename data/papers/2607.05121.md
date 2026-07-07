# From Failing to Passing: Evolving Natural Language Prompt Optimization Rules for LLM Code Generation

- arXiv ID: `2607.05121v1`
- Authors: Amal Akli, Melissa Akli, Cedric Richter, Mike Papadakis, Yves Le Traon
- Published: 2026-07-06
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.05121v1) | [pdf](https://arxiv.org/pdf/2607.05121v1)

## Abstract

Large language models are known to be sensitive to prompt formulation. Even minor variations in wording can substantially degrade performance. This sensitivity reveals an opportunity: if prompt phrasing can harm performance, can it be used to improve it? To investigate this question, we introduce a search-based approach that identifies and evolves a set of natural language transformation rules with strong downstream effects on coding performance. We then propose DUALFIX, a staged repair pipeline that combines the evolved transformation rules with execution-feedback repair, addressing both specification-level and implementation-level failures. A key strength of our approach lies in its generality: the evolved rules are error-agnostic, reusable across problems, and transferable across models. We evaluate DUALFIX against execution-feedback repair baselines across three models on two challenging benchmarks, LiveCodeBench and APPS. Our results show that the evolved transformations fix from 10-30% of failing cases, including 12-17% of failures that execution-based repair alone cannot resolve. Overall, DualFix recovers up to 30% of baseline failures and fixes 3-5 times more failing cases than Self-Fix across all evaluated settings. Furthermore, we also show that rules evolved on one model transfer zero-shot to other models, outperforming execution-feedback repair without any re-optimization.
