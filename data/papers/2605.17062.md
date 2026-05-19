# The Range Shrinks, the Threat Remains: Re-evaluating LLM Package Hallucinations on the 2026 Frontier-Model Cohort

- arXiv ID: `2605.17062v1`
- Authors: Aleksandr Churilov
- Published: 2026-05-16
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.17062v1) | [pdf](https://arxiv.org/pdf/2605.17062v1)

## Abstract

Spracklen et al. (USENIX Security '25) showed that code-generating large language models hallucinate package names that do not exist on PyPI or npm at rates ranging from 5.2% on commercial models to 21.7% on open-source models, creating an attack surface for slopsquatting -- the registration of malicious packages under hallucinated names. We replicate their methodology on five frontier code-capable LLMs released between October 2025 and March 2026: Claude Sonnet 4.6, Claude Haiku 4.5, GPT-5.4-mini, Gemini 2.5 Pro, and DeepSeek V3.2. Across 199,845 paired Python and JavaScript prompts validated against PyPI and npm master lists, we measure overall hallucination rates between 4.62% (Claude Haiku 4.5) and 6.10% (GPT-5.4-mini) -- an order-of-magnitude compression of the inter-model spread observed by Spracklen, but not a retirement of the threat. Beyond replication, we identify a set of 127 package names (109 on PyPI, 18 on npm) that all five evaluated models invent identically, constituting a model-agnostic supply-chain attack surface that no single-model study can reveal. We further document a Python-over-JavaScript hallucination asymmetry that inverts Spracklen's 2024 finding, identify a Haiku-below-Sonnet inversion within the Anthropic family, and observe a Jaccard-similarity peak between DeepSeek V3.2 and GPT-5.4-mini (J = 0.343) suggestive of shared training-data origins.
