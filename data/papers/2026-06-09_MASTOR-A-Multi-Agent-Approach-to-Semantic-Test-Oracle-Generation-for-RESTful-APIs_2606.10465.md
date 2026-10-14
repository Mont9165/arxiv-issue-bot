# MASTOR: A Multi-Agent Approach to Semantic Test Oracle Generation for RESTful APIs

- arXiv ID: `2606.10465v1`
- Authors: Sida Deng, Rubing Huang, Zhenzhen Yang, Man Zhang, Xuan Xie, Rongcun Wang
- Published: 2026-06-09
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.10465v1) | [pdf](https://arxiv.org/pdf/2606.10465v1)

## Abstract

Existing automated RESTful API testing approaches commonly rely on simple checks (e.g., HTTP status codes, schema conformance), which are insufficient for detecting semantic faults, business logic violations, and state-dependent inconsistencies. To address this, we propose MASTOR, a Multi-Agent approach for generating Semantic Test Oracles for RESTful APIs based on implementation source code. MASTOR consists of two phases: source analysis and oracle generation. The former employs a source extraction agent to construct a source context for each endpoint operation by analyzing a transitive import closure of relevant source files. The latter employs two parallel oracle-generation paths over the collected contexts: a single-operation path producing status and field oracles per operation, and a multi-operation path generating behavioral consistency oracles for operation sequences by leveraging cross-operation semantic associations. Both paths apply a challenger-agent review, where a dedicated reviewer identifies weaknesses and issues improvement hints to guide targeted regeneration, followed by oracle normalization to filter out structurally invalid oracles. We evaluated MASTOR on a benchmark of 13 open-source RESTful API projects (296 operations, 251,303 lines of code) from the WFD and PRAB datasets. MASTOR achieved an average mutation score of 75.4%, generating 10,022 oracles. These oracles were translated into executable assertions via ToJUnit and ToPostmanAssertify, and into human-readable descriptions via ToReadable. In a baseline comparison on 50 selected operations, MASTOR outperformed Direct Prompting by 30.1 percentage points (69.9% vs. 39.8%) and SATORI by 49.4 percentage points (69.9% vs. 20.5%).
