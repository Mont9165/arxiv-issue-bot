# Query-Centric Optimization of AI Workflows via Approximate Query Processing and Proxy Models

- arXiv ID: `2607.00254v1`
- Authors: Huayi Wang, Jun Xu, Gromit Yeuk-Yin Chan
- Published: 2026-06-30
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.00254v1) | [pdf](https://arxiv.org/pdf/2607.00254v1)

## Abstract

Many modern AI workflows, ranging from LLM post-training pipelines to agentic reasoning tasks, can be expressed as declarative queries whose expensive predicate is evaluated by a large model or reward function. We propose a query-centric formulation of these workflows and show that classical database techniques, namely approximate query processing (AQP) and proxy-model (PM) based filtering, can substantially reduce the number of expensive model invocations without requiring changes to the underlying models or pipelines. Our first strategy treats the workflow as an online aggregation problem: it progressively samples records, maintains a running aggregate estimate with a confidence interval, and terminates early once the interval stabilizes, accepting the estimate when it falls within a user-specified error bound. Our second strategy trains a lightweight, CPU-resident decision tree on a small set of oracle-labeled examples and uses it to pre-filter records whose outcome can be predicted with high confidence, routing only uncertain records to the expensive model. We evaluate both strategies on TPC-DS aggregate queries and on real LLM post-training pipelines including math reasoning, general instruction following, and code generation. On TPC-DS, Strategy AQP keeps aggregate error under 10% while reaching its adaptive stopping point at 10-15% of oracle calls under balanced distributions, an 85-90% reduction, and Strategy PM reduces oracle calls by 60-70%. On LLM pipelines, Strategy AQP reaches its adaptive stopping point at 20-50% of oracle calls with less than 5% accuracy loss on the structured math and code tasks; open-ended instruction following, scored by a reward model, shows a larger but bounded reduction. Strategy PM reduces reward-model scoring time by up to 19x on structured tasks with less than 10% accuracy loss.
