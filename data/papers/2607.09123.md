# ReProAgent: Tool-Augmented Multi-Stage Agentic Generation of Bug Reproduction Tests from Issue Reports

- arXiv ID: `2607.09123v1`
- Authors: Quanjun Zhang, Yi Zheng, Ye Shang, Weifeng Sun, Haichuan Hu, Chunrong Fang, Zhenyu Chen, Liang Xiao
- Published: 2026-07-10
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.09123v1) | [pdf](https://arxiv.org/pdf/2607.09123v1)

## Abstract

Reproduction tests help developers confirm reported issues and provide executable feedback for issue resolution, yet issue reports in open-source projects rarely include such tests. Recent studies have explored generating issue reproduction tests from issue reports with large language models, but existing approaches largely rely on prompt-based pipelines that retrieve textual context and generate tests. This limits their ability to understand how reported issues behave in repository-scale codebases and to flexibly organize the construction of reproduction tests. In this paper, we propose ReProAgent, a multi-stage agent framework for reproduction test generation from issue reports. ReProAgent decomposes the task into four agent stages: bug localization, root cause analysis, test planning, and test generation. To support these stages, ReProAgent integrates task-specific tools for task decomposition and reflection, context retrieval from both textual sources and repository graphs, and runtime interaction with the execution environment. Experiments on SWT-bench-lite and SWT-bench-verified show that ReProAgent successfully reproduces 58.43% and 70.30% of issues, outperforming all baselines, with an average cost of $0.14 per instance. For example, when equipped with GPT-5-mini, ReProAgent exceeds OpenHands with the same backbone by 20.43 and 7.90 percentage points, respectively. ReProAgent also generalizes across multiple backbone LLMs and improves downstream issue resolution performance when integrated with existing repair approaches.
