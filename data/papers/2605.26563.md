# TrajAudit: Automated Failure Diagnosis for Agentic Coding Systems

- arXiv ID: `2605.26563v1`
- Authors: Minxing Wang, Xiaofei Xie, Yintong Huo
- Published: 2026-05-26
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.26563v1) | [pdf](https://arxiv.org/pdf/2605.26563v1)

## Abstract

Agentic systems have been widely studied to automate software engineering jobs such as bug fixing. As these systems increasingly tackle complex tasks, understanding where and why they fail becomes essential for iterative refinement and operational reliability. Existing automated failure diagnosis approaches leverage task execution trajectories, yet their effectiveness degrades substantially as trajectory length and complexity increase. For repository-level coding tasks specifically, trajectories are laden with noise, such as redundant program structure and verbose code context. Moreover, these trajectories are very long, while long-context reasoning remains a known weakness of LLMs.
  To address these two challenges, we propose TrajAudit, the first failure diagnosis framework for repository-level coding trajectories. TrajAudit employs an investigator agent supported by two modules: one filters failure-irrelevant information through pattern matching and keyword detection, and the other generates a preliminary diagnosis from test failure reports as prior knowledge, helping the agent handle noisy long contexts. The investigator agent can further invoke tools to retrieve filtered content on demand, ensuring that critical information is preserved while noise is minimized. We also introduce RootSE, a benchmark of 93 real-world agentic failure instances sourced from software maintenance tasks, representing the most complex trajectory diagnosis benchmark to date. Experiments on RootSE show that TrajAudit outperforms all existing baselines by over 24.4 percentage points in localization accuracy, while reducing token consumption by at least 18%, demonstrating its practical effectiveness. We hope this work draws community attention to failure management in agentic software engineering and provides a foundational resource for future research.
