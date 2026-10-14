# AlgoBench: Benchmarking Algorithmic Adaptation in Code Generation

- arXiv ID: `2607.00062v1`
- Authors: Xinyuan Song, Zekun Cai, Liang Zhao
- Published: 2026-06-30
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2607.00062v1) | [pdf](https://arxiv.org/pdf/2607.00062v1)

## Abstract

High pass rates on established programming benchmarks such as HumanEval and LiveCodeBench do not always show whether a model can reason about algorithms. Many fixed benchmarks eventually become part of the public training ecosystem through released problem statements, editorials, and generated solutions, allowing later models to improve partly by exposure rather than by stronger algorithmic ability. We introduce ALGOBENCH, a framework that automatically builds novel algorithmic problems from known competitive-programming problems through structured constraint-shifting transformations. Each accepted ALGOBENCH variant is traceable to a source problem, but must make the original reference algorithm fail. Beyond pass@$k$, we introduce complexity-aware metrics -- including OPTT, OPTS, TRAPRATE, GAPT, and CONSENS -- to test whether a solution is not only functionally correct but also asymptotically suitable for the generated problem. Experiments across multiple LLMs and prompting strategies show that performance drops sharply on ALGOBENCH variants, retrieval can increase reuse of the old algorithm, and many correct-looking solutions fail to meet the required complexity. Error analysis shows that failures are mainly algorithmic rather than implementation-level, suggesting that ALGOBENCH evaluates adaptation beyond functional correctness.
