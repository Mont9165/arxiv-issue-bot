# How Reasoning Shapes Social Bias in LLM-Generated Code?

- arXiv ID: `2608.06829v1`
- Authors: Weifeng Sun, Jieke Shi, Zhou Yang, Yuchen Chen, Hongyan Li, Meng Yan, David Lo
- Published: 2026-08-07
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.06829v1) | [pdf](https://arxiv.org/pdf/2608.06829v1)

## Abstract

Large language models (LLMs) are increasingly used for code generation, yet generated programs may exhibit social bias through unfair or differential treatment of sensitive demographic attributes. While prior work mainly studies direct code generation, bias in reasoning-based generation remains underexplored. We conduct the first systematic study of social bias in reasoning-based code generation, evaluating 9 standard LLMs and large reasoning models (LRMs) on realistic bias-sensitive tasks across three human-centered decision scenarios. We find that reasoning generally reduces bias, lowering the average bias rate from 0.64 to 0.40, but the effect varies substantially across models. Meanwhile, code quality is not consistently preserved, with the average quality dropping from 0.72 to 0.59. Biased reasoning strongly predicts biased code, and adjusting generation configurations alone is insufficient for robust mitigation. Based on these findings, we propose ProbeDebias, a reasoning-aware framework that detects and rewrites biased reasoning traces before code generation. ProbeDebias achieves 87.76% F1 for reasoning-bias detection and reduces code bias by 83.73% on average while largely preserving quality. Compared with SOTA baselines, it further reduces average bias by 52.70%-54.42% and improves quality by 9.79%-36.79%. These results highlight the value of reasoning-stage analysis for trustworthy code generation.
