# Compositional Jailbreaking: An Empirical Analysis of Mutator Chain Interactions in Aligned LLMs

- arXiv ID: `2605.15598v1`
- Authors: Reinelle Jan Bugnot, Soohyeon Choi, Hoon Wei Lim, Yue Duan
- Published: 2026-05-15
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.15598v1) | [pdf](https://arxiv.org/pdf/2605.15598v1)

## Abstract

Jailbreaking attacks on large language models pose a significant threat to AI safety by enabling the generation of harmful or restricted content. While prior work has explored both handcrafted and automated jailbreak strategies, the potential for compositional interaction between simple attacks remains underexplored. This paper presents a systematic study of mutator chaining, in which weak jailbreak transformations are applied sequentially to characterize how they interact: whether they reinforce one another, interfere destructively, or produce no meaningful change. We implement twelve baseline mutators and evaluate all ordered pairs on a benchmark of harmful prompts against three popular LLM models. Our framework introduces metrics for completeness and validity that capture both transformation persistence and attack effectiveness. Results reveal that the interaction landscape is highly non-uniform, while most combinations fail to outperform individual mutators, exhibiting destructive interference or structural incompatibility, a small fraction produce synergistic effects that improve attack success rates. Equally important, the prevalent failure modes reveal structural properties of safety alignment that are not apparent from single-strategy evaluations. These findings highlight the nuanced dynamics of adversarial prompt composition and offer new insights for building more robust safety defenses.
