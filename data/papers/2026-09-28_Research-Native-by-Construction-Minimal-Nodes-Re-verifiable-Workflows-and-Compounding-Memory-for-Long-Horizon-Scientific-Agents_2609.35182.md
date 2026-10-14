# Research-Native by Construction: Minimal Nodes, Re-verifiable Workflows, and Compounding Memory for Long-Horizon Scientific Agents

- arXiv ID: `2609.35182v1`
- Authors: Di Wang, Yu Liu, Bing Cui, Chaoqun Ji, Dongyuan Ni, Jingyu Lu, Kunlei Cui, Pu Qin
- Published: 2026-09-28
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.35182v1) | [pdf](https://arxiv.org/pdf/2609.35182v1)

## Abstract

We describe AfS (Agent for Science), a platform built for long-horizon scientific work, where a project runs for tens of hours across dozens of agent runs with a human present only occasionally. Most agents for science are general coding agents with a skills folder attached, and they inherit that lineage's failure mode: under pressure to finish, they fabricate, skip, or smooth over. Our design rests on one claim: most of the credibility of machine-made research can be moved from asking the model to behave to making the non-compliant state unrepresentable. We encode research discipline as mechanically enforced laws (commitment before measurement; unforgeable freezing; reports are not facts; evidence persists but verdicts do not; negative results are first-class; mechanical questions to the framework and semantic judgment to the model), organized around three time horizons: a minimal set of research nodes within a run, an inquiry contract with frozen closure conditions and a hash-chained artifact ledger within a project, and a two-tier knowledge base with promotion by rewriting across projects. This is a system description written under one rule: each mechanism appears in exactly one place, with the invariant it enforces, the failure it prevents, the way it is realized, and the cost it imposes. It covers the node contract, the write-path gates, the two-tier memory, and the runtime substrate. Three traces walk real failure attempts through the mechanisms that catch them, and two closed campaigns are included as worked illustrations rather than as an evaluation. We report no benchmark: a process-integrity suite that would support quantitative comparison is under construction, and what we can measure today is only the operating cost of the machinery.
