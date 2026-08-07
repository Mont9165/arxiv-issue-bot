# Cost-Aware Optimization for Agentic Query Execution

- arXiv ID: `2606.03152v1`
- Authors: Lunyiu Nie, Yilin Xia, Yiren Liu, Christopher Jermaine, Swarat Chaudhuri
- Published: 2026-06-02
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.03152v1) | [pdf](https://arxiv.org/pdf/2606.03152v1)

## Abstract

Classical query optimization searches over algebraically equivalent plans that differ only in cost. This assumption breaks once LLM-backed operators enter the picture: their placement, ordering, and granularity jointly determine both dollar cost and answer quality, and the right choice among the alternatives is often revealed only at runtime. We formalize this setting as agentic query execution, a query execution paradigm in which agent-based planning is interleaved with execution, and agent workflow optimization becomes the analogue of classical query optimization. We then present EnumGRPO, a self-improving optimizer for this setting. During a learning stage, EnumGRPO enumerates query plans over decisions such as execution paradigm, operator type, operator placement, selectivity scope, and projection width, then distills quality-cost feedback into reusable planning heuristics via in-context reinforcement learning. Across four databases in SWAN, EnumGRPO achieves 35.4% execution accuracy at $0.011 per query in LLM-operator cost, a ~317x cost reduction over the hybrid query baseline with an 18% relative improvement in answer accuracy.
