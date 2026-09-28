# When the Model Retires: An Empirical Study of LLM Migration in Open-Source Applications

- arXiv ID: `2609.31288v1`
- Authors: Hyungjin Lukas Kim
- Published: 2026-09-25
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.31288v1) | [pdf](https://arxiv.org/pdf/2609.31288v1)

## Abstract

Applications built on commercial large language model (LLM) APIs depend on model versions that providers retire on their own schedule, with notice periods ranging from one year to two weeks. We ask what actually happens to applications when a model is retired. We mine GitHub for commits that migrate away from officially deprecated models and endpoints of OpenAI, Anthropic, and Google, matching each commit to the provider's published announcement and shutdown dates. From 22,555 commits in 17,703 non-fork repositories (2024-2026), 5,139 are matched to an official event; two independent coders validated a stratified sample of 300 (kappa = 0.89-0.95), and we reweight all estimates by their labels. We find that an estimated 82% (95% CI 79-84) of migrations away from retired models were committed after the shutdown date - after the application had started failing - regardless of repository popularity, prior retirement experience, or the presence of a provider-abstraction layer. The share tracks the provider's notice policy: 89% for Anthropic's 60-114-day notices versus 13% for OpenAI's one-year Assistants API notice, and each e-fold increase in notice length reduces the odds of post-shutdown migration by about three quarters. Model identifiers are hard-coded in 94% of migrating applications, migration effort scales from a median of 6 added lines for prompt-only applications to nearly 700 for fine-tuned ones, and only 8% of migrations switch provider. We release the dataset and pipeline and discuss implications for deprecation policy, dependency-risk assessment of LLM products, and tooling.
