# MongoBench: Do LLMs Know What a MongoDB Query Will Do?

- arXiv ID: `2611.09065v1`
- Authors: Qibai Chen, Haoting Qiu, Yezhou Cheng, Mengxiao Qian
- Published: 2026-11-06
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.09065v1) | [pdf](https://arxiv.org/pdf/2611.09065v1)

## Abstract

LLM agents increasingly operate databases on their own: they generate queries and run them against live data. Two checks are commonly used to judge such an agent - whether it produces a valid query, and whether it reaches the right final answer - but neither tells us whether the agent knows what its query will actually do before it runs. We argue that this consequence prediction ability must be evaluated in its own right, and we build MongoBench to measure it: given a collection of documents and a MongoDB find() filter, a model must return the exact set of matching _ids, with ground truth from a real mongod server. The 300 items each compose three or four documented matching pitfalls and are proposed symmetrically by three vendors' models, so results stratify by item source. Evaluating four models - frontier systems from three vendors and one open-weight reasoner - accuracy ranges from 70.1% to 92.1%, a 22-point spread. Each proposer mispredicts 10-31% of the items it wrote itself, so producing a query does not imply predicting its effect. A failure-mode analysis shows errors are better predicted by which semantic pitfall a query exercises - range comparisons and null - than by surface measures such as document count or the number of composed rules. Prepending a verified rule sheet helps unevenly; executing the original filter against the engine yields reliable match sets, but delegation must be checked: on 28% of items (averaged over three runs) one model's executed filters never passed a canonical check against the intended query, and it answered about 22 of them wrong, while the other three passed on every item. We release the benchmark, the mongod oracle, and the evaluation code with all prompts at https://github.com/research-repo-bai/MongoBench.
