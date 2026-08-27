# From General Agents to RCA Experts: A Self-Evolving Harness for Root Cause Analysis

- arXiv ID: `2608.25661v1`
- Authors: Haiyu Huang, Jiewei Lyu, Zhihan Jiang, Jinyang Liu, Xiao He, Tieying Zhang, Wu Xiang, Michael R. Lyu
- Published: 2026-08-26
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2608.25661v1) | [pdf](https://arxiv.org/pdf/2608.25661v1)

## Abstract

Automated root cause analysis (RCA) with large language models (LLMs) has drawn growing attention. Today, SREs typically automate RCA with LLMs in one of two ways: directly using a general-purpose agent (e.g., Codex or Claude Code) for diagnosis, or building a specialized RCA agent from scratch. As mainstream general agents grow more capable and iterate quickly, our quantitative study finds that the former now often surpasses the latter. Its accuracy, however, still falls short of production needs, and this gap stems mainly from the external adaptation layer outside the agent's general capabilities, namely the harness. We therefore argue that LLM-based RCA should focus on this external harness, reusing the strong general capabilities of a modern agent rather than rebuilding an agent from scratch. A key capability of such a harness is to self-evolve, accumulating system-specific experience from past diagnoses so that it gets better the more it is used. We introduce OpsHarness, a self-evolving RCA harness that turns diagnosis experience into reusable expertise. Its data plane combines layered operational knowledge with an idea-card tool library, while its control plane coordinates setup, diagnosis, evolution, and verification. During evolution, OpsHarness contrasts successful and failed trajectories, converts their evidence into atomic proposals, and admits updates only through a dual-gate verification process designed to prevent overfitting and regression. Across two public benchmarks and an industrial deployment, OpsHarness achieves 59.0\% top-1 accuracy, improving over a bare general agent by 63.4\% and over baseline RCA agents by 4.02$\times$.
