# UXBench: Measuring the Actionability of LLM-Generated UX Critiques

- arXiv ID: `2606.16262v1`
- Authors: Wenjie Wang, Yue Huang, Zipeng Ling, Han Bao, Hang hua, Xiaonan Luo, Yu Jiang, Shiyi Du, Yuexing Hao, Xiaomin Li, Yuchen Ma, Dianzhuo Wang, Yanfang Ye, Xiangliang Zhang
- Published: 2026-06-15
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.16262v1) | [pdf](https://arxiv.org/pdf/2606.16262v1)

## Abstract

Large language models (LLMs) are increasingly deployed as UX judges that inspect interfaces, diagnose usability problems, and propose repairs. Yet no controlled benchmark measures whether the resulting critiques are reliable and actionable across heterogeneous product surfaces. We introduce UXBench, a benchmark for evaluating LLMs as interaction-grounded UX judges. UXBench comprises local-first runnable web fixtures spanning ten product-surface families, paired with coverage-gated browser exploration that forces models to collect interaction evidence before reporting. Each judge model produces a structured UX report over seven rubric dimensions; report quality is measured by whether a fixed downstream repair agent can improve the interface based on the critique. We evaluate eight frontier models under both an automated repair-lift protocol and a blind human validation study. Results show that UX judging is neither saturated nor one dimensional: models differ meaningfully in report actionability, exhibit distinct rubric-level repair signatures, vary in fixture-level reliability, and trade leadership across surface categories
