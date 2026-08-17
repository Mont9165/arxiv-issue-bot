# CoSA: Context-Aware Severity Assessment via Context Analysis with Large Language Models

- arXiv ID: `2608.13928v1`
- Authors: Jinfeng Jiang, Yikun Li, Chengran Yang, Ting Zhang, Wen Bin Leow, Yide Yin, Eng Lieh Ouh, Lwin Khin Shar, David Lo
- Published: 2026-08-14
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.13928v1) | [pdf](https://arxiv.org/pdf/2608.13928v1)

## Abstract

Accurate vulnerability severity assessment is essential for prioritizing remediation, yet manually assessing Common Vulnerability Scoring System (CVSS) base metrics remains labor-intensive. Existing automated approaches often fail to capture the repository-level evidence required for assessing many CVSS base metrics. Such repository-aware assessment is challenging because relevant evidence is scattered across the entire repository under heavy noise.
  To address these challenges, we present CoSA, a Context-aware vulnerability Severity Assessment approach that infers CVSS base metrics from repository artifacts. CoSA constructs a code property graph (CPG) and applies a two-stage repository-pruning strategy: lightweight static pruning to preserve structurally proximal context, followed by an agentic large language model (LLM)-guided pruning step to retain CVSS-relevant context while collecting supporting evidence. The LLM then consolidates the retrieved repository context into compact, CVSS metric-wise textual summaries, which are fed into a lightweight transformer predictor. We also construct a higher-quality repository-level dataset comprising 6,816 CVSS labeled instances spanning 90 Common Weakness Enumeration (CWE) types.
  Experiments on real-world vulnerabilities show that CoSA consistently outperforms function-level and pure-LLM baselines. It improves prediction accuracy by 14.4% and Macro-F1 by 15.3% over the best-performing baseline, suggesting that explicit, metric-oriented repository context retrieval is crucial for practical and reliable automated severity assessment.
