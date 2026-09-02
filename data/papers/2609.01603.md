# Efficient SWE Agent Benchmarking via Trajectory-Aware Evaluation

- arXiv ID: `2609.01603v1`
- Authors: Kefeng Duan, Dewu Zheng, Yanlin Wang, Xiwen Wang, Ensheng Shi, Xilin Liu, Yuchi Ma, Jiachi Chen, Mingwei Liu, Zibin Zheng
- Published: 2026-09-01
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2609.01603v1) | [pdf](https://arxiv.org/pdf/2609.01603v1)

## Abstract

Evaluating software engineering agents on realistic benchmarks is costly, since each task may require multi-step code exploration, modification, and test execution. Existing efficient evaluation methods select representative subsets to estimate full-benchmark performance, but are largely result-only: they fit historical pass/fail response matrices or static task semantics, discarding how agents solve problems. We propose PTA-IRT, a Privileged Trajectory-Aware Item Response Theory framework that fuses process and outcome signals. Historical execution trajectories supply process-level evidence beyond pass/fail, such as explored context, attempted edits, and solving paths, which PTA-IRT uses as privileged information for calibration subset selection and ability estimation. Under low calibration budgets, PTA-IRT consistently outperforms prior IRT baselines on score and ranking recovery across four SWE benchmarks. Code and data are publicly available at https://github.com/DeepSoftwareAnalytics/PTA-IRT.
