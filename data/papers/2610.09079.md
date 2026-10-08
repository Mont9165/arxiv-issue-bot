# Large-scale Repository Engineering via Agent-Native Reusable Code Primitives

- arXiv ID: `2610.09079v1`
- Authors: Haibo Jin, Peng Kuang, Xucheng Yu, Jerry Wang, Dehao Wu, Haohan Wang
- Published: 2026-10-06
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`, `cs.CV`
- Links: [abs](http://arxiv.org/abs/2610.09079v1) | [pdf](https://arxiv.org/pdf/2610.09079v1)

## Abstract

Large language models equipped with development environments have moved code generation toward repository-scale construction, yet building complete repositories remains difficult because interacting modules, interfaces, configurations, tests, and dependencies must work together. We introduce Code Primitives, agent-native reusable executable components with interface contracts, dependency closures, validation tests, and provenance. Each primitive uses a resident LLM to assess relevance and adapt its implementation, interfaces, and dependencies to the target repository, and we organize 1,424 validated primitives in CodeFace, a searchable library for repository construction. We introduce LEGO (Large-scale repository Engineering via aGent-native reusable cOde primitives), which activates task-relevant primitives, integrates their adapted implementations with task-specific code while resolving cross-component constraints, and revises the result against executed tests. To measure construction end to end, we build LEGO-REPO, a benchmark of 522 executable reconstruction tasks spanning seven software domains, 22 capability tracks, and five difficulty levels, scored against native test suites between an empty-package floor and original-source ceiling. The strongest of 13 evaluated backbones reaches a delivery score of 0.318 and scores zero on 41.0% of tasks; LEGO improves all 13 by 0.1474 on average and raises GPT-5.6-terra from 0.3180 to 0.5134 (+61.4%). In controlled comparisons, adapted primitives outperform retrieved code supplied as context or vendored unchanged. The effect persists against independent repository agents, across three external benchmarks, and with a disjointly re-mined CodeFace; GPT-OSS-20B for adaptation and diagnosis retains 95.1% of the homogeneous score at 24.0% lower cost.
