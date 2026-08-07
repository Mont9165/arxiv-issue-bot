# How Developers Use Relation Chains in Gerrit-Based Review Ecosystems: An Empirical Study Across Three Open-Source Ecosystems

- arXiv ID: `2607.20189v1`
- Authors: Ahmed Belhouchette, Moataz Chouchen, Marouene Chaieb, Mohammad Hamdaqa Abdelwahab Hamou-Lhadj
- Published: 2026-07-22
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.20189v1) | [pdf](https://arxiv.org/pdf/2607.20189v1)

## Abstract

Background. Developers increasingly coordinate dependent review workflows by submitting sequences of related changes rather than monolithic ones. In Gerrit, these dependencies form relation chains: structured review units that link changes together. As chains become more common, they shape review activities through synchronization overhead, CI amplification, and merge-ordering constraints.
  Aim. We investigate how developers adopt relation chains and how these dependency structures influence review dynamics and outcomes.
  Method. We analyze 29,580 relation chains from 15 repositories across three Gerrit ecosystems (OpenStack, Wikimedia, and ONAP), comprising 401,256 changes, using Mann-Kendall trend tests, Mann-Whitney tests with Cliff's delta for chain-vs-solo comparisons, and Spearman correlations for base-descendant dependencies.
  Results. Chain prevalence ranges from 5% to 49% across projects, increasing in 14 of 15. Chain changes take a median of 2.6 times longer to merge than size-matched solo changes, with the gap widening for very large changes. Review effort propagates through dependency-linked review workflows: base-change review activity co-varies with descendant review activity (rho = 0.43-0.61 in 14-15 of 15 projects), and 33.5% of chain members undergo structural evolution during review.
  Conclusions. Relation chains operate as durable, ecosystem-shaped coordination units with internal structure that change-centric analyses cannot capture. Future review analytics, reviewer-assignment systems, and AI-assisted review tools should reason over chains rather than isolated changes.
