# Code Is More Than Text: Uncertainty Estimation for Code Generation

- arXiv ID: `2606.09577v1`
- Authors: Yuling Shi, Caiqi Zhang, Yuexian Li, Haopeng Wang, Yeheng Chen, Nigel Collier, Xiaodong Gu
- Published: 2026-06-08
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.09577v1) | [pdf](https://arxiv.org/pdf/2606.09577v1)

## Abstract

Large language models (LLMs) are increasingly deployed as code generators, where silently wrong programs pose real safety and reliability risks. Reliable uncertainty estimation (UE) is essential for selective prediction, human-in-the-loop review, and downstream agentic decisions. Yet most existing code UE methods are inherited from natural language (NL) generation and ignore properties that make code distinct. We argue that code differs from NL in three ways: a single wrong token can break an entire program (token fragility); algorithmic intent and concrete implementation can disagree independently (intent-code gap); and programs can be executed (executability). We instantiate these properties as three orthogonal uncertainty axes: lexical (Top-K token entropy), algorithmic (pseudo-code consistency), and functional (behavioral consistency). Across five code LLMs, our three-axis ensemble improves average AUROC from 0.696 for the strongest NL-derived baseline to 0.776 (+8.1 points). Notably, on Qwen3-14B, our single-pass Top-K token entropy matches the strongest multi-pass baseline while being over 3x cheaper; across models, it remains a competitive low-cost signal. These results suggest that code UE deserves code-specific design rather than direct NL ports.
