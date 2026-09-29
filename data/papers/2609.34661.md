# Codoku: Renewable Program-Reasoning Challenges for Frontier Coding Agents

- arXiv ID: `2609.34661v1`
- Authors: Cong Li, Hao Sun, Zenan Li, Zhendong Su
- Published: 2026-09-28
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.34661v1) | [pdf](https://arxiv.org/pdf/2609.34661v1)

## Abstract

Existing program-reasoning benchmarks ask large language models to predict a program's behavior on a given input. Coding agents break two assumptions on which these benchmarks rest: an agent can recover the answer by executing the program instead of reasoning about it, and fixed task sets drawn from existing programs are increasingly exposed to contamination, yet costly to renew. We introduce Codoku (code sudoku), a renewable benchmark in which a solver fills typed cells in a partial program to satisfy global static and dynamic constraints, such as a prescribed control-flow graph and execution path. Because a partial program cannot be executed and valid fillings are sparse in an exponentially large space of interdependent choices, neither tool use nor enumeration can substitute for program reasoning. Puzzles are synthesized from scratch via semantic reification, so fresh puzzles of controllable complexity can be generated on demand, each with a witness that guarantees solvability. We evaluate five frontier models on 300 puzzles through a coding agent free to use any tool within a fixed budget. Small puzzles already challenge open-weight models, whereas even proprietary models solve only about half of the large ones. Codoku thus offers a renewable testbed for program reasoning that can keep pace with rapidly improving coding agents. GitHub: https://github.com/connglli/Codoku.
