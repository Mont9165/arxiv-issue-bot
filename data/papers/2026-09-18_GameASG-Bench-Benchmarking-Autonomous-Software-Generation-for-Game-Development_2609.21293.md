# GameASG-Bench: Benchmarking Autonomous Software Generation for Game Development

- arXiv ID: `2609.21293v1`
- Authors: Xiuhui Zhang, Yi Chen, Shusheng Xu, Fan Li, Huan Wang, Tongkai Yang, Binhang Yuan
- Published: 2026-09-18
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.21293v1) | [pdf](https://arxiv.org/pdf/2609.21293v1)

## Abstract

Autonomous software generation (ASG) aims to turn human requirements into executable applications, but delivering these applications does not necessarily establish that their interacting components satisfy the specified behavioral requirements. We introduce GameASG-Bench, a benchmark that makes behavioral testability part of the generation task for game development. Our design declares an evaluation interface specification before generation, fixing legal starting scenarios, player-level actions, stable snapshots, rejection behavior, and invariants while leaving private implementations open. Concretely, we include: (i) static L1 checks that assess source-level compliance; and (ii) browser-executed L2 checks that combine semantic observations with real input and runtime evidence. We implement this protocol as 47 browser-native game-generation tasks spanning 12 primary genres and both 2D and 3D interaction, each with executable checks and an independently verified reference implementation. Our experiments answer four key questions about end-to-end agent performance, tool access and nominal turn budget, reasoning effort, and harness choice. Across nine agent stacks, the highest observed mean L2 check pass rate is 93.2%, yet the highest observed strict task success rate, requiring all L1 and applicable L2 prerequisite and core requirement checks, is only 55.3% (26/47 tasks). For DeepSeek-V4-Flash, full tool access and larger nominal turn budgets yield more strict task successes, while the strict task success rate is not monotonic in reasoning effort. Both tested harnesses achieve 18 strict task successes, but only ten tasks succeed under both. These results expose task-level compliance gaps that high average check pass rates actually obscure.
