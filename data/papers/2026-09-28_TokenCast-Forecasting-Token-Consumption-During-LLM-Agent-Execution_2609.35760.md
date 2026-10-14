# TokenCast: Forecasting Token Consumption During LLM Agent Execution

- arXiv ID: `2609.35760v1`
- Authors: Chaoqian Ouyang, Ling Yue, Libin Zheng, Huanghui Guo, Shengxiang Xu, YiShu Wang, Ran Li, Jian Yin, Shaowu Pan, Shimin Di
- Published: 2026-09-28
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.35760v1) | [pdf](https://arxiv.org/pdf/2609.35760v1)

## Abstract

When a large language model (LLM) agent executes the same task, token consumption can vary by over an order of magnitude across runs. The agent chooses its next steps based on tool feedback and intermediate results, while the growing context steadily inflates the input size of every subsequent call. The total consumption of a task is therefore hard to predict before execution and the prediction must be revised as the run unfolds. In this paper, we propose TokenCast, which learns a composable cost representation for each execution segment, recording its own consumption and the context growth it introduces. Composing adjacent segments yields a cumulative estimate that captures the extra input cost incurred when context from earlier segments is re-read by every later call. As execution unfolds, newly observed evidence refreshes the forecast, requiring no additional LLM calls and incurring a mean cumulative prediction time of 32.8 ms per run on SWE-bench Verified. Across 4 task suites and 6 agent models, TokenCast's mean absolute error reduction against the strongest comparator averages 14.5% over 96 evaluated combinations. In offline budget-control replay, TokenCast uses 21.3% fewer tokens on average than a fixed-budget policy at matched trace completion. The code is available at https://github.com/DEFENSE-SEU/TokenCast.
