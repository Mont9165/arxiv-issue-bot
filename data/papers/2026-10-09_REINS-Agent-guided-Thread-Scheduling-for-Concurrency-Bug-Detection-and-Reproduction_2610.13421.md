# REINS: Agent-guided Thread Scheduling for Concurrency Bug Detection and Reproduction

- arXiv ID: `2610.13421v1`
- Authors: Yu Zhang, Corina S. Pasareanu, Guowei Yang
- Published: 2026-10-09
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.13421v1) | [pdf](https://arxiv.org/pdf/2610.13421v1)

## Abstract

Concurrency bugs manifest only under specific thread interleavings, making them hard to detect and reproduce. Existing controlled concurrency testing techniques take over thread scheduling to explore the interleaving space. As the space grows rapidly with program scale, finding interleavings that can trigger bugs within a limited budget remains challenging. The program's concurrency semantics can reveal which variable accesses and synchronization operations under specific interleavings lead to unexpected program behavior, and thus help focus the exploration on bug-relevant interleavings. However, prior techniques have not fully exploited such semantic information. In this paper, we present REINS, an agentic approach for detecting and reproducing concurrency bugs. At its core, REINS guides thread scheduling with the agent's reasoning about the concurrency semantics and known concurrency bug patterns. REINS starts with runtime observations and combines them with static information to reason about the program's concurrency behavior and formulate hypotheses about potential bugs. A hypothesis translates into a set of constraints on event orders and variable states, guiding a controlled scheduler toward interleavings likely to trigger the bug. REINS draws conclusions from the execution results and keeps refining the constraints until the bug is triggered or the hypothesis is refuted. Compared with existing techniques on three public benchmarks, REINS detects more bugs within the same time budget. Furthermore, REINS found six previously unknown concurrency bugs in real-world projects, three of which have been confirmed by the developers.
