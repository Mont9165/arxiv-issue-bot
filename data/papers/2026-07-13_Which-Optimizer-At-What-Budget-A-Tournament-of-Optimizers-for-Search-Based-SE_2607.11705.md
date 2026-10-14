# Which Optimizer, At What Budget? A Tournament of Optimizers for Search-Based SE

- arXiv ID: `2607.11705v1`
- Authors: Kishan Kumar Ganguly, Tim Menzies
- Published: 2026-07-13
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.11705v1) | [pdf](https://arxiv.org/pdf/2607.11705v1)

## Abstract

Configuring and tuning modern software is unavoidable, expensive, and error-prone: a single system can expose hundreds of interacting options, and scoring one setting can mean a full build or test run. The standard response is automated optimization, but the number of available optimizers is large and growing. And some of the guidance for selecting among them is misleading: NSGA-II, for example, is widely recommended, yet other algorithms reach the same results using only 1/20th as many evaluations.
  To help practitioners make better choices about tools to configure their systems, we cluster 20 optimizers, based on six assumptions about the data. Next, we run a tournament across those optimizers, using 106 SE optimization tasks at four labeling budgets (taking 14,000+ CPU hours). We find that no optimizer wins outright. The best one migrates with the budget (from a geometric active learner when labels are scarce to differential evolution when labels are plentiful) so a winner "crowned" at one budget is wrong at another on up to half our tasks.
  Running such a tournament for every new domain is impractical due to its CPU cost. Fortunately, we find that those 14,000 hours can be replaced by a table lookup over two cheap-to-obtain task attributes (plus the labeling budget). Predictions from this table tie or beat a hindsight oracle on $\approx 75%$ of held-out tasks.
  To support open science, our tournament and replication package are open-sourced for SBSE researchers and practitioners at https://github.com/KKGanguly/OptimizerTournament.
