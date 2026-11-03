# APG: Agentic Static-Analysis Infrastructure on LLVM-IR Graph Databases

- arXiv ID: `2611.02349v1`
- Authors: Zexin Zhong, Yanjun Zhang, Yulei Sui, Xiao Cheng
- Published: 2026-11-02
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.02349v1) | [pdf](https://arxiv.org/pdf/2611.02349v1)

## Abstract

LLM-based coding agents increasingly rely on external program knowledge, yet access to static-analysis graphs alone does not ensure appropriate operation selection or evidence interpretation. We present APG, an infrastructure for semantics-grounded static program analysis. Built on SVF and LLVM, it decomposes compiler-derived program analyses into atomic capabilities that LLM agents can select, compose, and orchestrate for goal-directed, cross-graph investigation, with query safeguards and evidence traces preserving inspectable results and provenance. APG provides 38 atomic capabilities. On analysis requests arising during benchmark repair runs, 35 achieve first-attempt query-generation success rates above 50%, including 13 at 100%. Evaluation on 812 C/C++ defects shows higher repair success than the evaluated baselines. Compared with Passive Graph Push, APG improves first-iteration repair success by 17.6 and 18.0 percentage points on the two benchmark collections and reduces average LLM input-token consumption by 90.8%. Our tool is available at https://github.com/JasonZhongZexin/APG-ICSE-Demo and its demonstration video at https://youtu.be/vkuExZUjGnw
