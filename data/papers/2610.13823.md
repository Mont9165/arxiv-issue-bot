# Same Query, Different Answer: Run-to-Run Variance in Semantic Query Processing

- arXiv ID: `2610.13823v1`
- Authors: Oktie Hassanzadeh, Dharmashankar Subramanian
- Published: 2026-10-09
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2610.13823v1) | [pdf](https://arxiv.org/pdf/2610.13823v1)

## Abstract

Semantic query engines ask a large language model (LLM) to judge individual rows, and benchmarks compare these engines on the quality of a few executions at temperature 0. We measure how much another execution changes. We re-execute the text and tabular workloads of SemBench, LRO-Bench, and UDA-Bench through their own harnesses, log every one of 1.2 million model calls, and reanalyze SemBench's published executions. At temperature 0, between 0.07% and 10.2% of rows change their operator output over five executions, depending on the model, and up to 24.0% on one task. Plans amplify these changes exponentially in the number of rows an answer exposes, as a possible-worlds model predicts: on UDA-Bench, a few percent of extracted values change, but about two thirds of the answers do. In SemBench's published results, 21% of text results change quality between executions, including on engines whose plans are deterministic. Several per-query system comparisons, and 16 of 28 tests of LRO-Bench's implementation recommendations, are not settled by the executions the benchmarks run. Changing rows are rows on which models disagree with each other; identical requests within one execution disagree as often as across executions; and one execution's decision margin or reasoning length predicts which rows change. Voting reduces the variance but does not remove it, and a calibrated cascade keeps its guarantee while the rows it returns change. We derive reporting rules for benchmarks and design rules for engines.
