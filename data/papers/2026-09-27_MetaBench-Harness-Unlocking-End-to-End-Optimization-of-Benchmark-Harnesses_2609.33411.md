# MetaBench-Harness: Unlocking End-to-End Optimization of Benchmark Harnesses

- arXiv ID: `2609.33411v1`
- Authors: Xuanjun Chen, Hua-Hsuan Chen, Wei-Chung Lu, Yinghao Ma, Jyh-Shing Roger Jang, Hung-yi Lee
- Published: 2026-09-27
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.CL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.33411v1) | [pdf](https://arxiv.org/pdf/2609.33411v1)

## Abstract

Rapid progress in Large Language Models (LLMs) is saturating static benchmarks faster than they can be designed. While existing automated evolution frameworks attempt to generate harder questions by perturbing individual tasks, they remain constrained by rigid, hard-coded generation rules. Moving beyond the evolution of isolated tasks, we propose to optimize the benchmark generation workflow itself end to end with MetaBench-Harness, a dual-loop search framework. Specifically, the inner loop utilizes a benchmark harness to generate a new benchmark in each round, while the outer meta-harness orchestration layer iteratively refines and searches over harness implementations based on historical evolution trajectories. By applying MetaBench-Harness to the competitive programming CodeContests and Olympiad mathematics AIME-2024 datasets, we demonstrate that the evolved benchmarks are challenging and discriminative for frontier models. Trajectory and quality analyses verify that MetaBench-Harness enables multi-dimensional evolution, steadily improving evolution reasonableness, benchmark competency, and evaluator robustness across successive rounds. Furthermore, case studies reveal its effective utilization of diverse difficulty levers to reframe problems and elevate required capabilities. Ultimately, this work provides a solution to the pressing challenge of benchmark saturation.
