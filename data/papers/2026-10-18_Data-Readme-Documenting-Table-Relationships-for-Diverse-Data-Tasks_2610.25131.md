# Data.Readme: Documenting Table Relationships for Diverse Data Tasks

- arXiv ID: `2610.25131v1`
- Authors: Jiaming Liang, Yeye He, Haoyu Dong, Zachary Ives, Surajit Chaudhuri
- Published: 2026-10-18
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.25131v1) | [pdf](https://arxiv.org/pdf/2610.25131v1)

## Abstract

Large language models (LLMs) can perform diverse data tasks when given a small set of relevant tables. However, for complex tasks requiring multiple tables over large data lakes, identifying relevant tables for the task becomes a prerequisite, but remains challenging. This is because there are often many tables in a data lake with similar table and schema names, and limited additional semantic context, thereby forcing agents to spend substantial time exploring tables at online query time, greatly affecting models' ability to perform tasks accurately, while increasing cost/latency substantially.
  We present Data.Readme, a novel table documentation approach that uses lightweight offline processing to infer and index rich \emph{table-to-table relationships}, including confusable, joinable, and union-able tables. We further develop a suite of agentic tools for LLMs to work with the index, to help agents retrieve relevant tables and perform tasks much more efficiently and effectively. Finally, we study how to optimize our index construction with a budget constraint. On data lakes containing up to 12K tables, Data.Readme improves task accuracy by as much as 40 percentage points across a range of data discovery, data analysis, and data science tasks, outperforming diverse baselines, including powerful coding agents with unlimited time and monetary budgets. We also show that equipping existing methods (such as coding agents) with Data.Readme can not only lead to consistent quality gains, but also significantly reduce their latency by up to 6x, demonstrating the potential of Data.Readme.
