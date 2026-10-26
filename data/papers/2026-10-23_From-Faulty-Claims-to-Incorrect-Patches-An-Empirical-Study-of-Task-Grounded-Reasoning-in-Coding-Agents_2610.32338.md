# From Faulty Claims to Incorrect Patches: An Empirical Study of Task-Grounded Reasoning in Coding Agents

- arXiv ID: `2610.32338v1`
- Authors: You Wang, Jinjun Huang, Zhonghao Jiang, Jialun Cao, Jiachi Chen, Zhongxin Liu
- Published: 2026-10-23
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.32338v1) | [pdf](https://arxiv.org/pdf/2610.32338v1)

## Abstract

Large language model (LLM)-based coding agents increasingly resolve real-world software engineering tasks, yet still fail on many of them. Prior trajectory studies characterize these failures through task-agnostic patterns of agent behavior, such as repeated actions. However, an agent may follow a sound workflow yet act on a faulty understanding of the existing code, the task requirements, or a candidate fix. Reasoning models, which power most state-of-the-art coding agents, reveal this understanding in their native chain-of-thought (CoT), whose claims about the task can be checked against the facts. Yet it remains unclear how many such checkable claims the CoT contains, how many are faulty, and whether faulty claims actually cause incorrect patches. We present the first empirical study of such claims, which we term task-grounded reasoning, analyzing 400 trajectories of four open-weight reasoning models on SWE-bench Pro. We extract atomic claims from the CoT with an LLM, assess them against evidence gathered by an LLM agent, and manually trace the defects of incorrect patches back to faulty claims, confirming each link with a claim-corrected replay. Task-grounded reasoning covers only 18.5% of the CoT tokens, yet yields 191 atomic claims per trajectory, at least 9.6% of which are faulty. Faulty claims also occur in 96.7% of the resolved trajectories, so their mere presence is a weak signal of failure. Yet two thirds of the 188 incorrect patches trace back to faulty claims. Correcting such a claim makes the agent fix the linked defect in 89.0% of the cases, and correcting all such claims resolves 11.7% of the failed tasks. Our findings show that the CoT carries task-specific signals for diagnosing and repairing agent failures, but exploiting them requires pinpointing the few faulty claims that actually cause patch defects.
