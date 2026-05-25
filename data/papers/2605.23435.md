# MileStone: A Multi-Objective Compiler Phase Ordering Framework for Graph-based IR-Level Optimization

- arXiv ID: `2605.23435v1`
- Authors: Amirhosein Sadr, Mehran Alidoost Nia
- Published: 2026-05-22
- Primary category: `cs.PL`
- Categories: `cs.PL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.23435v1) | [pdf](https://arxiv.org/pdf/2605.23435v1)

## Abstract

Compiler phase ordering has a strong effect on program performance. Finding an effective sequence of passes is still a difficult task because the search space is large and execution time, code size and energy consumption often conflict. Existing methods usually depend on fixed optimization levels or limited heuristics and they rarely handle multiple objectives at the same time. This paper presents MileStone, a modular framework that models compiler phase ordering as a multi-objective optimization problem. MileStone represents programs as graphs, predicts performance metrics with a graph neural network and explores pass sequences with a reinforcement-learning agent that follows user constraints. The framework also builds a self-evolving database that collects compiler transformations and improves prediction quality. Experiments on standard benchmarks show that MileStone finds strong Pareto-optimal solutions, meets energy limits more accurately than LLVM optimization levels and other related techniques. MileStone reduces execution time by up to 45 percent under the same energy budget using a multi-objective approach. The results show that MileStone provides an effective and scalable solution for multi-objective compiler phase ordering.
