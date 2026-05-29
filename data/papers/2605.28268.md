# Towards Cost-effective LLMs Routing with Batch Prompting

- arXiv ID: `2605.28268v1`
- Authors: Haotian Xu, Kangfei Zhao, Jiadong Xie
- Published: 2026-05-27
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.28268v1) | [pdf](https://arxiv.org/pdf/2605.28268v1)

## Abstract

Large Language Model (LLM) serving systems must balance task performance against monetary cost. Two prominent optimization techniques have emerged independently: LLM routing, which directs each query to the most cost-effective model in a model pool, and batch prompting, which packs multiple queries into a single invocation to amortize the fixed cost of the shared system prompt. These two techniques are logically complementary; i.e., routing optimizes the model assignment dimension while batching optimizes the query aggregation dimension, jointly reshaping the landscape of model utility and monetary cost. However, existing approaches explore only one side of this decision space. On the basis of empirical studies on their impacts, we are motivated to jointly optimize these two dimensions in this paper. We formulate the Route with Batching Problem, which jointly determines the target model and batch size for each query under a total cost budget, and prove it NP-hard. To solve this challenging problem, we propose RoBatch, a unified two-stage framework. In the modeling stage, RoBatch constructs a batch-aware proxy utility model that decomposes combinatorial utility estimation into utility estimation without batching and recalibration of model-specific utility degradation with batching. In the routing stage, RoBatch employs a greedy scheduling algorithm that progressively upgrades the assignment of the target model and batch size for queries along the cost-utility Pareto frontier until the budget is exhausted. Extensive experiments on six benchmarks across two LLM families (Qwen3 and Gemma3) demonstrate that RoBatch consistently achieves a superior cost-performance Pareto frontier compared with LLM routing and batch prompting baselines.
