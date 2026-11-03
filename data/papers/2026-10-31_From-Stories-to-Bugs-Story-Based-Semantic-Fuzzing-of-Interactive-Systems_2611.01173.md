# From Stories to Bugs: Story-Based Semantic Fuzzing of Interactive Systems

- arXiv ID: `2611.01173v1`
- Authors: Yeshayahu Weiss, Achiya Elyasaf, Gera Weiss
- Published: 2026-10-31
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.01173v1) | [pdf](https://arxiv.org/pdf/2611.01173v1)

## Abstract

Complex interactive systems hide business-logic failures along two complementary axes: deep state-dependent behaviors that require long valid prefixes and concurrency-sensitive failures that depend on the ordering of otherwise legal operations. We present story-based semantic fuzzing, a methodology that treats semantically constrained compositions of behavioral stories as primary search objects. Implemented through Behavioral Programming, semantic binding and state constraints preserve legal prefixes, while event eligibility, schedule selection, and replay expose failure-relevant interleavings. We evaluate the methodology on Magento and four stateful REST APIs. On Magento, overlap-aware ranking increased reproduction of a sporadic Shipping Fee race from 3.6% to 41.2%; a controlled ordering intervention reduced a second failure signature from 100/100 initial executions to 0/200 constrained executions. For the REST study, a versioned end-to-end pipeline took each frozen public OpenAPI contract as its sole benchmark-specific model-generation input and automatically generated the Basic and Complex stories, dependency structure, and interface bindings. Under a shared black-box task and sequence-local evaluation contract, Basic and Complex confirmed 0/11 and 11/11 semantic fault classes, while RESTler and EvoMaster confirmed 2/11 and 0/11. A paired binding ablation produced 250/250 valid dependent operations with binding and 0/250 without it, while supplementary prefix controls localized the difference to preservation of legal relational state. Together, the studies show that searching admissible semantic compositions provides a unified and effective representation for reaching deep states and exposing concurrency-sensitive business-logic failures.
