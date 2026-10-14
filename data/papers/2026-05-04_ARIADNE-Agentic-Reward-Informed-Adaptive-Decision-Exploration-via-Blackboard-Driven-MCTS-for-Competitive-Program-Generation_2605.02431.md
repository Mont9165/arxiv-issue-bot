# ARIADNE: Agentic Reward-Informed Adaptive Decision Exploration via Blackboard-Driven MCTS for Competitive Program Generation

- arXiv ID: `2605.02431v1`
- Authors: Minnan Wei, Xiang Chen, Xiaoshuai Niu, Siyu Chen
- Published: 2026-05-04
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.02431v1) | [pdf](https://arxiv.org/pdf/2605.02431v1)

## Abstract

Competitive program generation aims to automatically produce correct and efficient solutions for programming-contest problems under strict time and memory constraints. Existing LLM-based approaches often fail to perform explicit algorithmic planning and to handle edge cases robustly, leading to unreliable one-shot generation. Moreover, although execution feedback is essential for iterative debugging and refinement, incorporating such feedback effectively within limited computational budgets remains difficult. To overcome these limitations, we propose {\tool}, a blackboard-driven Monte Carlo Tree Search (MCTS) framework that models program generation as a sequential decision process. {\tool} organizes the generation workflow into five coordinated stages (i.e., strategy selection, code generation, test generation, quality evaluation, and code repair) while maintaining a shared blackboard that accumulates structured evidence to guide subsequent decisions. Experiments on four benchmarks (APPS, CodeContests, CodeContests+, and LiveCodeBench) show that {\tool} consistently achieves the best Pass@1 performance across multiple LLM backends. With GPT-4o, {\tool} attains Pass@1 scores of 41.30, 46.67, 27.27, and 20.91, surpassing the strongest baseline CodeSim by up to 26.06 points, while further improvements are observed with DeepSeek-V3.2. These results indicate that combining global search through MCTS with persistent evidence accumulation on a shared blackboard enables systematic exploration and effective feedback utilization, substantially enhancing the capability of LLMs in competitive program generation.
