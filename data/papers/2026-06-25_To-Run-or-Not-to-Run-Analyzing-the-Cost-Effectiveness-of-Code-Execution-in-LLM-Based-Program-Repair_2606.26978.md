# To Run or Not to Run: Analyzing the Cost-Effectiveness of Code Execution in LLM-Based Program Repair

- arXiv ID: `2606.26978v1`
- Authors: Zhihao Lin, Junhua Zhu, Mingyi Zhou, Xin Wang, Zhensu Sun, Renyu Yang, David Lo, Li Li
- Published: 2026-06-25
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.26978v1) | [pdf](https://arxiv.org/pdf/2606.26978v1)

## Abstract

LLM-based agents for program repair are increasingly built on a "generate-run-revise" paradigm, iteratively executing tests to evaluate and refine patches. This execution-based approach has become standard practice in state-of-the-art systems. However, executions can be time-consuming and expensive, yet their impact on these agents remains underexplored. In this paper, we conduct a two-stage empirical study over execution behavior in LLM-based program repair. To characterize execution behavior at scale, we first analyze 7,745 agent traces from SWE-bench leaderboard submissions. Second, we evaluate 3,000 end-to-end repair attempts across 200 SWE-bench instances and three agents (Claude Code, Codex, and the open-source OpenCode) under four execution paradigms, which allows for a fine-grained comparison of performance and cost. Our analysis reveals three key observations: (1) Code execution is used across all agents and models analyzed, with an average of 8.8 test runs per task. Execution behavior varies substantially across agents and models, with frequency ranging from 2 to 19 per task, and late-stage executions consistently achieve higher success rates than early-stage ones. (2) Execution restrictions have little effect on repair success: on commercial agents with SOTA models the resolve-rate gap between Prohibited and Unrestricted is only 1.25 percentage points and not statistically significant, while Prohibited saves substantial token and wall-clock cost. (3) Execution benefit is concentrated rather than uniform. These patterns suggest that current agents apply execution indiscriminately, paying its cost on instances where it provides little benefit. Execution, therefore, should be treated as a resource with an explicit cost-benefit tradeoff, not a default capability.
