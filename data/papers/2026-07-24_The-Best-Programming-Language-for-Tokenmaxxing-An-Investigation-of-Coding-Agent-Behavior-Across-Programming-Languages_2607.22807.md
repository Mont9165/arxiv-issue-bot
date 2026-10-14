# The Best Programming Language for Tokenmaxxing: An Investigation of Coding Agent Behavior Across Programming Languages

- arXiv ID: `2607.22807v1`
- Authors: Zixuan Wu, Carolyn Jane Anderson, Arjun Guha
- Published: 2026-07-24
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2607.22807v1) | [pdf](https://arxiv.org/pdf/2607.22807v1)

## Abstract

Although coding agents are now very effective in a variety of programming languages, this paper first shows that the cost (in tokens) can very significantly by programming language. We evaluate five recent models on programming problems in Python, Java, Rust, and OCaml. We carefully control for problem difficulty, and show that there can be stark variation in token consumption that is consistent across models. To understand why, we analyze both the structure and content of agent trajectories. First, we re-execute every intermediate solution and abstract each trajectory as a sequence of test-outcome vectors, then label the work between successive solutions. This reveals agents repeatedly producing noncompiling solutions in unfamiliar languages and revising solutions that already pass. Second, we analyze trajectory text, finding that agents plan solutions in code comments, distrust the provided tests in favor of inputs they invent, and sidestep unfamiliar target languages by prototyping in Python.
  Our results show that by-language token efficiency is a metric that should be considered when benchmarking and developing multilingual agents, and, for the tokenmaxxer, a guide to the most expensive language to work in.
