# The Nuts and Bolts of Natural Language to SQL Translation: A Systematic Analysis of Model Pipeline Optimisation Approaches and their Interactions

- arXiv ID: `2607.10911v1`
- Authors: Filip Klubicka, Vasudevan Nedumpozhimana, Sneha Rautmare, Bora Caglayan, Mingxue Wang, John D. Kelleher
- Published: 2026-07-12
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.10911v1) | [pdf](https://arxiv.org/pdf/2607.10911v1)

## Abstract

In the age of large language models, Natural Language to SQL (NL2SQL) translation remains an open problem with many useful applications. We explore interactions between several NL2SQL pipeline extensions to inspire development of more lightweight models. Specifically, we integrate the NatSQL intermediate representation, include a preprocessing step and a fine-tuning step based on synthetic data, and develop a novel reranker model to improve SQL selection in the final beam. We perform an ablation study supplemented by a Shapley analysis of these different components integrated with two backbone architectures, SmBoP and RASAT. We find that simply combining all of them does not lead to best results, but that their impact depends on their interactions with the baseline system, as well as each other.
