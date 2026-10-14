# ExplainBench: Evaluating Code Explanations from Agents

- arXiv ID: `2607.26451v1`
- Authors: Zhiyuan Pan, Sungmin Kang, Imam Nur Bani Yusuf, Abhik Roychoudhury
- Published: 2026-07-29
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.26451v1) | [pdf](https://arxiv.org/pdf/2607.26451v1)

## Abstract

Large Language Model (LLM) agents have seen rapid adoption in software engineering. As agents take a greater role in the actual generation of code, they are making larger changes, spanning tens to hundreds of lines. This makes manual review of agent results increasingly infeasible, leading developers to turn to explanations to understand enacted changes. Despite this, there are no benchmarks that evaluate the trustworthiness of agent-generated explanations. To bridge this gap, we propose ExplainBench, a benchmark to automatically evaluate explanations from coding agents. ExplainBench is based on the intuition that informative explanations should enable an LLM to correctly answer questions, allowing quantitative comparison of explanation quality between agents. With this observation, we construct a suite of questions that evaluates whether explanations accurately describe (1) the intended behavior of buggy code and (2) the effect of applying the agent patch itself. Experiments first reveal that explanation quality is a distinct axis of agent evaluation: ExplainBench ranks agents differently from the widely-used SWE-bench Verified benchmark. A deeper breakdown of explanation quality in agents shows frequent problems in explanations, such that explanations often claim that a patch is correct when it is not. Based on this insight, we implement and evaluate an explanation audit agent which runs additional tests to validate and refine explanations. This agent improved the explanations of all evaluated agents, demonstrating agent explanations can be automatically made more trustworthy.
