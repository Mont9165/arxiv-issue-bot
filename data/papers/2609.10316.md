# Ensembling LLMs for AI-Augmented Cybersecurity Software Requirements Generation

- arXiv ID: `2609.10316v1`
- Authors: Santiago Perez-Acuna, Yod-Samuel Martín, Juan C. Yelmo
- Published: 2026-09-09
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.10316v1) | [pdf](https://arxiv.org/pdf/2609.10316v1)

## Abstract

Translating high-level controls from security standards into concrete, system-specific requirements is central to cybersecurity requirements engineering. Large language models (LLMs) can accelerate this labor-intensive, recall-sensitive task, but any single run is unreliable: it misses valid safeguards while introducing plausible hallucinations, and outputs shift across runs and models. We reframe this variability as a resource: rather than selecting one output, we study post-generation ensembling, aggregating stochastic runs with information-retrieval data-fusion operators. We propose two strategies: Uniform fusion rewards mere cross-run agreement, whereas Naive-Bayes fusion weights each run by its estimated reliability. We evaluate both over 24 runs from 12 configurations across four model families, generated for ten ISO/IEC 27002:2022 controls and expert-judged against a gold standard of 72 valid requirements. Pooling every run's output recovers all 72 (whereas single configurations recover on average under half) but also 111 hallucinations. Fusion separates the wheat from the chaff, ranking valid requirements well ahead of hallucinations. In the areas under the precision-recall and ROC curves, Uniform fusion alone largely surpasses every original run and configuration by 0.142 and 0.118 over the best configuration. Naive-Bayes weighting adds a further 0.039 and 0.052, reaching 0.864 and 0.869 while attaining useful operating points earlier. Internal validation confirms the stability of these gains: they stay positive in at least 92% of out-of-bag bootstrap resamples and every structured-perturbation sample. Post-generation fusion thus turns apparent noise into a practical asset: a lightweight layer giving analysts broader coverage and a better prioritized review queue, using affordable, below-frontier models alone.
