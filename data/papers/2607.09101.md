# Multi-Agent LLM Collaboration for Unit Test Generation via Human-Testing-Inspired Workflows

- arXiv ID: `2607.09101v1`
- Authors: Quanjun Zhang, Ye Shang, Siqi Gu, Jianyi Zhou, Chunrong Fang, Zhenyu Chen, Liang Xiao
- Published: 2026-07-10
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.09101v1) | [pdf](https://arxiv.org/pdf/2607.09101v1)

## Abstract

Recently, the emergence of Large Language Models (LLMs) has spurred a surge of research into automated unit test generation, yielding impressive performance and reducing manual effort. However, existing LLM-based approaches still suffer from two major limitations: (1) they follow rigid, procedural workflows that underutilize the autonomous reasoning potential of LLMs, making it difficult to dynamically adapt testing strategies based on real-time feedback; and (2) they rely on rule-based context extraction that is not tailored to test generation, failing to capture fine-grained code dependencies and test-specific knowledge required for deriving test requirements. In this paper, we propose TestAgent, an LLM-based test generation approach that addresses the above limitations by emulating human testing practices via a multi-agent collaboration mechanism. Particularly, TestAgent designs three specialized agents, namely a requirement planner, a test generator, and a test reviewer, to simulate how developers understand, construct, and validate unit tests. To unleash the autonomous capabilities of LLMs, we equip TestAgent with a set of tool APIs that can be invoked dynamically in an on-demand and adaptive manner. To further support repository-level reasoning, TestAgent constructs a test-specialized knowledge graph via static analysis, which captures code entities and their dependencies across the project and persistently stores testing artifacts (e.g., test reports and failure analyses) produced during generation. Experimental results show that TestAgent achieves 97.46% execution rate, 92.34% line coverage, 90.24% branch coverage, and 83.69% mutation score on six Java projects, outperforming LLM-based baselines across all metrics and achieving substantially higher mutation scores than search-based tools.
