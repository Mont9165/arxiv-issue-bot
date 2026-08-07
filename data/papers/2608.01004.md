# Who Belongs in the Eval Set? A Capability-Taxonomy-Driven Pipeline for Curating Regression Eval Sets in Agent-Extensibility Platforms

- arXiv ID: `2608.01004v1`
- Authors: Tezan Sahu, Aritra Das, Pankaj Mittal, Sudipta Das
- Published: 2026-08-02
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.01004v1) | [pdf](https://arxiv.org/pdf/2608.01004v1)

## Abstract

Platform teams hosting agent-extensibility surfaces face a regression-economics paradox: every onboarding customer ships an evaluation set tuned to their domain, but the platform's regression set must live under a hard query-count ceiling bounded by release cadence. To our knowledge, no published industrial pipeline addresses this platform-side curation problem: existing evaluation frameworks are customer-side, and benchmark-compression work treats benchmarks as fixed pools rather than streams of incoming sets. We describe a capability-taxonomy-driven curation pipeline applied to declarative agents with custom actions in Microsoft 365 Copilot. It takes an agent specification and a customer's eval set as input, projects each query into a platform-owned capability taxonomy, and outputs per-query decisions (admit, drop, swap, or human review), under the philosophy that a healthy regression set is the minimal set of queries capturing the maximal spread of capability signatures -- distinct combinations of capabilities a query exercises together. Three components instantiate this: a classifier producing per-(query, capability) verdicts via a hybrid of deterministic specification-based extraction and large-language-model (LLM) semantic inference; an Invocation Quality (IQ) rater scoring how thoroughly a query exercises each capability, so a new query sharing a signature with an existing entry can still be recognized as a better test and displace it; and a consolidator comparing incoming queries against the regression set on coverage and quality through a rule-based decision cascade, backed by a conservative curator that only suggests evictions. The mechanism is taxonomy-agnostic and applies to any regression eval-set curation problem with a typed capability taxonomy, including taxonomies that evolve in response to the very evidence the pipeline surfaces.
