# A Validated Dataset and Benchmark for Coherent Multi-Diagram SysML Models

- arXiv ID: `2610.07356v1`
- Authors: Ardalan Aryashad, Yan Jin
- Published: 2026-10-05
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2610.07356v1) | [pdf](https://arxiv.org/pdf/2610.07356v1)

## Abstract

Systems engineers use several diagrams to describe the structure and behavior of systems. Engineers create these diagrams together to make sure that they use the same elements and remain consistent with one another. Large language models can generate diagrams as text or code, which makes it possible to create system diagrams automatically. However, their ability to generate coherent sets of diagrams is not well understood, and existing datasets and benchmarks do not directly measure this ability at scale. We introduce SEMAADB (Systems Engineering Modeling Assistant with AI Dataset and Benchmark), a dataset of 3,000 engineering contexts and 15,000 diagrams. Each context contains five connected SysML views: Requirement, Block Definition, Activity, State Machine, and Sequence. Here, a view is a diagram that presents one aspect of a system. We checked the diagram sets for consistency and valid rendering. A set of 100 contexts is also human-verified and forms the benchmark test set. We evaluate three language models on two tasks. In diagram repair, the strongest model repairs 64.3% of semantic errors . In cross-diagram update the best propagation F1 is 80.7% when a model applies one change across related diagrams. The results show that syntax repair is nearly solved, but semantic repair and consistency across diagrams are still challenging tasks for models. SEMAADB therefore provides both a large diagram resource and a set of benchmarks for measuring coherent multi-diagram SysML generation.
