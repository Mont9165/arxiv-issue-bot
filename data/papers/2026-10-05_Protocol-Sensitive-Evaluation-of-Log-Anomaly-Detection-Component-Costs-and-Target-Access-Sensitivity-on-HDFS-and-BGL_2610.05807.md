# Protocol-Sensitive Evaluation of Log Anomaly Detection: Component Costs and Target-Access Sensitivity on HDFS and BGL

- arXiv ID: `2610.05807v1`
- Authors: Hang Xiao, Janet Sung, Zhaoyi Li, Gangzhen Qian, Chuhong Xu
- Published: 2026-10-05
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`, `cs.CE`, `cs.IR`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2610.05807v1) | [pdf](https://arxiv.org/pdf/2610.05807v1)

## Abstract

Protocol choices can change the conclusions drawn from log anomaly detection benchmarks even when detector settings are fixed. We present a joint empirical study of split construction, representation visibility, and component costs using six fixed count, sequence, and semantic configurations on Hadoop Distributed File System (HDFS) and Blue Gene/L (BGL) logs. Random splits place several configurations near the average-precision ceiling, whereas group-disjoint HDFS and chronological BGL evaluation produce lower scores and different observed orderings. At a fixed BGL cutoff, parser choice spans 0.124 in semantic XGBoost mean average precision while preserving its lead over count XGBoost; the earliest rolling period reverses that ordering. A two-factor cross-system ablation contrasts source-only representations with offline transductive access to unlabeled target templates through the representation corpus and inverse document frequency: HDFS-to-BGL mean average precision moves from 0.191 with source-only access to 0.325 with union-corpus, target-IDF access, and the intermediate conditions reveal direction-dependent interactions in average precision and retrieval at fixed review budgets. Component-level profiling separates parsing and representation costs from classifier training, prediction, and storage. Together, these findings connect detector comparisons to the test population, preprocessing state, visible information, and measured pipeline stages, and identify the protocol fields needed alongside a score to support interpretable comparisons of log anomaly detection accuracy and resource use.
