# DSL-Bench: Evaluating and Explaining LLM Code Generation Across Domain-Specific Languages

- arXiv ID: `2611.05168v1`
- Authors: Zihan Zhou, Mingxi Ye, Yan Gao, Guipeng Wei, Zibin Zheng
- Published: 2026-11-03
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.05168v1) | [pdf](https://arxiv.org/pdf/2611.05168v1)

## Abstract

Large language models (LLMs) are increasingly used in software-engineering workflows, but code-generation benchmarks largely focus on general-purpose languages. Domain-specific languages (DSLs) have distinct syntax, semantics, and validation requirements, making results from individual DSL benchmarks difficult to compare. We present DSL-Bench, an executable benchmark and analysis framework for cross-DSL code generation. Starting from 13,045 DSL-related papers, LLM-assisted open card sorting identifies 18 representative application domains. For each domain, we select an evaluable DSL and provide a syntax checker and task-level semantic oracle. Evaluating 7 LLMs on 18 DSLs, we observe mean syntax and semantic pass rates of 31.37% and 11.64%, respectively, revealing a substantial gap between syntax acceptance and semantic correctness. A variance decomposition attributes 76.99% of semantic pass-rate variation to differences among DSLs and 7.86% to differences among models. Among four DSL-level factors, Knowledge Demand has the strongest negative association with semantic correctness (r = -0.508). We evaluate prompt engineering across all 18 DSLs and study five improvement methods on five targeted DSLs. Prompt engineering yields uneven gains; RAG-Refinement, the strongest targeted method, improves semantic correctness by 16.29 percentage points on average over matched baselines. We further derive capability profiles and DSL-Profiler summaries for interpreting data-scarce DSLs. These results highlight toolchain-specific semantic bottlenecks and the need to evaluate DSL code generation beyond syntax acceptance.
