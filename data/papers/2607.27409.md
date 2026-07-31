# SWE-NFI: Studying and Benchmarking Coding Agents for Non-Functional Improvements

- arXiv ID: `2607.27409v1`
- Authors: Pengyu Xue, He Yang Yuan, Xin Wang, Junkai Chen, Haonan Zhang, Boyuan Chen, Zishuo Ding, Zhenhao Li, Weiyi Shang
- Published: 2026-07-29
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.27409v1) | [pdf](https://arxiv.org/pdf/2607.27409v1)

## Abstract

Although coding agents have achieved impressive performance on correctness-oriented benchmarks, their ability to make behavior-preserving non-functional improvements (NFIs) remains underexplored. In real-world software development, developers continuously improve software quality without changing observable behavior, yet existing benchmarks primarily evaluate functional correctness and provide limited support for assessing these non-functional improvements.
  In this paper, we present SWE-NFI, a benchmark for evaluating coding agents on NFIs beyond functional correctness. Our benchmark contains 188 tasks constructed from real merged pull requests in open-source Python projects. We operationalize developer-oriented NFIs into 92 executable rules and develop a comprehensive evaluation suite that combines functional correctness testing with rule-based NFI evaluation.
  We evaluate state-of-the-art commercial and open-source coding agents. Although the best-performing agent achieves a 70.0\% functional correctness rate, all evaluated agents generally fall short of human developers in overall NFI capability. The gap is particularly evident for structural code improvements, where agents' NFI scores range from 0.0 to 1.3, compared with 1.5 for the human reference. Our benchmark and findings provide a reproducible foundation for evaluating and advancing coding agents beyond functional correctness.
