# Experience Graphs: The Data Foundation for Self-Improving Agents

- arXiv ID: `2606.29823v1`
- Authors: Gang Liao, Yujia He, Abdullah Ozturk, Zhouyang Li, Ying Wang, Zhitong Guo, Hongsen Qin, Yaobin Qin, Tao Yang, Zewei Jiang, Dianshi Li, Jort Gemmeke, Jiangyuan Li, Liyuan Li, Nathan Yan, Masha Basmanova, Uladzimir Pashkevich, Matt Steiner, Pedro Pedreira, Rob Fergus, Anirudh Goyal, Carole-Jean Wu, Gaoxiang Liu, Andrew Witten, Daniel J. Abadi
- Published: 2026-06-29
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`, `cs.MA`
- Links: [abs](http://arxiv.org/abs/2606.29823v1) | [pdf](https://arxiv.org/pdf/2606.29823v1)

## Abstract

The database community has repeatedly advanced the state of the art by recognizing that new workloads demand new system architectures. We argue that long-horizon agentic tasks -- code generation, scientific discovery, hardware design -- are such a workload. These agents explore: they generate artifacts, execute tools, observe failures, branch, and repair over hundreds of steps. This search produces a structured object we call an experience graph: executable artifacts, tool outputs, rewards, sibling comparisons, and causal lineage. Yet existing agent frameworks treat this experience as disposable state -- JSON checkpoints and session logs that cannot be recovered after a crash, queried across users, or materialized into training data. We propose Trellis: a data foundation that treats the experience graph as first-class, governed, queryable database state. The core insight is that search over experience graphs is a database access pattern. Frontier selection is a query, cross-session reuse is vector-seeded graph retrieval, training-data extraction is a materialized view, and reconstructing what an agent knew at any past step is a time-travel query. When the database owns the experience graph, agents become stateless compute, and crash recovery, horizontal scaling, and a closed-loop training flywheel emerge as architectural byproducts. We ground the design in KernelEvolve, a production accelerator-kernel optimizer at Meta, where cross-session reuse reaches a target speedup roughly 10x faster at 52% lower token cost. More broadly, Trellis turns inference-time search from disposable computation into a durable institutional asset: logs made databases reliable; experience graphs may make agents cumulative.
