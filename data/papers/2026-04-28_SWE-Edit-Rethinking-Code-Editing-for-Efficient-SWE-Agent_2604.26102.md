# SWE-Edit: Rethinking Code Editing for Efficient SWE-Agent

- arXiv ID: `2604.26102v1`
- Authors: Yikai Zhang, Jiaxin Pei, Kenan Li, Maoquan Wang, Jin Pan, Yu Kang, Shengyu Fu, Elsie Nallipogu, Junjie Hu, Yufan Huang, Zijian Jin
- Published: 2026-04-28
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2604.26102v1) | [pdf](https://arxiv.org/pdf/2604.26102v1)

## Abstract

Large language model agents have achieved remarkable progress on software engineering tasks, yet current approaches suffer from a fundamental context coupling problem: the standard code editing interface conflates code inspection, modification planning, and edit execution within a single context window, forcing agents to interleave exploratory viewing with strictly formatted edit generation. This causes irrelevant information to accumulate and degrades agent performance. To address this, we propose SWE-Edit, which decomposes code editing into two specialized subagents: a Viewer that extracts task-relevant code on demand, and an Editor that executes modifications from high-level plans--allowing the main agent to focus on reasoning while delegating context-intensive operations to clean context windows. We further investigate what makes an effective editing model: observing that the prevalent find-and-replace format is error-prone, we train Qwen3-8B with GRPO to adaptively select editing modes, yielding improved editing efficiency over single-format baselines. On SWE-bench Verified, SWE-Edit improves resolved rate by 2.1% while reducing inference cost by 17.9%. We additionally propose a code editing benchmark that reliably predicts downstream agentic performance, providing practical guidance for editing model selection. Our code is publicly available at https://github.com/microsoft/SWE-Edit.
