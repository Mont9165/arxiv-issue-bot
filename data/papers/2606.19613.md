# StaminaBench: Stress-Testing Coding Agents over 100 Interaction Turns

- arXiv ID: `2606.19613v1`
- Authors: Vlad Sobal, Shuo Yang, Yuting Zhang, Wei Xia, Stefano Soatto
- Published: 2026-06-17
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.19613v1) | [pdf](https://arxiv.org/pdf/2606.19613v1)

## Abstract

We introduce StaminaBench, a benchmark that measures the stamina of coding agents: how many consecutive interaction turns (change requests) they can handle before failing. Unlike the prevailing fraction-of-tasks-solved metric, this matches real vibe-coding where sessions run dozens or hundreds of turns. In StaminaBench, agents implement a REST API server and modify it across a tunable number of procedurally generated follow-up change requests - 100 in our experiments, resulting in codebases of up to 6,000 lines. Tests are generated fully programmatically without LLM involvement, ensuring reproducibility and reliability; change sequences are drawn from either a hardcoded or LLM-driven sampler, both constrained to a structured action space to ensure changes are valid. The agent and the server run in an isolated environment and communicate with the benchmark through HTTP, making testing fully black-box and language-agnostic. We evaluate six agent harnesses paired with seven open-source LLMs across 20 scenarios of 100 turns each and find that: (1) all the tested models fail within 5-6 turns, confirming that vibe-coding-style programming without thorough testing produces bugs; (2) passing test feedback back to the agent and allowing it to retry improves passed turn count by up to 12x; and (3) a good harness is required for strong performance: stronger models exhibit up to a 6x gap between their best and worst harness, while weaker models fail with any harness. We release the benchmark and the generated tasks to enable further research into multi-turn coding agent behavior. Benchmark code and data: github.com/amazon-science/StaminaBench.
