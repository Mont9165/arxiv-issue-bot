# Diversity-Guided Search-Based Testing of Large Language Model Applications

- arXiv ID: `2609.23209v1`
- Authors: Lev Sorokin, Ivan Vasilev, Ken E. Friedl, Andrea Stocco
- Published: 2026-09-19
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.23209v1) | [pdf](https://arxiv.org/pdf/2609.23209v1)

## Abstract

Large Language Model (LLM)-based applications are increasingly deployed across domains including customer service, education, and mobility. These systems are prone to inaccurate, fictitious, or harmful responses, and their vast, high-dimensional input space makes systematic testing particularly challenging. In this paper, we present a search-based testing framework for LLM-based applications that incorporates failure diversity as an explicit optimization objective. Building on a discretization along stylistic, content-related, and perturbation dimensions, our framework maintains an archive of generated tests and rewards distance from that archive, while a repopulation operator periodically replaces non-failing tests in the population to sustain exploration. The repopulation operator is parameterized by its sampling strategy: replacement candidates are drawn either uniformly or by greedy distance maximization, two settings we compare empirically.
  We evaluate both against several baselines across three case studies---LLM safety, in-car navigation, and in-vehicle function control---covering five systems under test, eight LLMs, and 18 distinct test configurations, with over one million executed tests. Our results show that all guided variants detect substantially more failures than random and combinatorial search in nearly all configurations. Among them, diversified search detects fewer failures, but covers a broader range of failure types in all case studies, with greedy repopulation offering the best tradeoff.
