# AskWise: Execution-Guided Clarification of Intent and Data in Text-to-SQL

- arXiv ID: `2611.27474v1`
- Authors: Yuru Liang, Guangyinan Mei, Miles Fan
- Published: 2026-11-20
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.27474v1) | [pdf](https://arxiv.org/pdf/2611.27474v1)

## Abstract

Two interpretations of a database question can agree on the observed records and diverge after a correction. A single record can therefore determine whether the user needs to clarify their intent. AskWise executes candidate queries across possible repairs. It asks about a choice only when two executions differ in that choice alone and give different answers. Once all surviving combinations give the same known answer, it returns that answer. For Boolean answers on a uniform binary cube, we derive an exact bound on the difference in EC2 gain between two questions from partial execution results. Across 120 sales tasks spanning three query types, the bound reduces mean executions per episode from 14.88 to 13.80 relative to a partition relaxation. Asking at the first sign that a choice matters uses 13.18 executions and 0.025 more questions per episode. On AmbiQT, a controlled value swap separates the reference queries in 424 of 1,206 eligible cases. On 155 sampled questions, pruning the same model candidates across both database states raises recall of reference answer signatures by 8.71 percentage points for Doubao Lite and 10.00 for GPT Sol.
