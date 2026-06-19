# FAPO: Fully Autonomous Prompt Optimization of Multi-Step LLM Pipelines

- arXiv ID: `2606.19605v1`
- Authors: Paul Kassianik, Baturay Saglam, Huaibo Zhao, Blaine Nelson, Supriti Vijay, Aman Priyanshu, Amin Karbasi
- Published: 2026-06-17
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.19605v1) | [pdf](https://arxiv.org/pdf/2606.19605v1)

## Abstract

Multi-step LLM pipelines fail through interactions among retrieval, reasoning, and formatting steps, so prompt-only optimization can miss bottlenecks in the chain. We present FAPO (Fully Autonomous Prompt Optimization), a framework that lets Claude Code optimize an LLM pipeline inside a standardized codebase. FAPO evaluates a pipeline, inspects intermediate steps, diagnoses failures, proposes scoped changes, and validates variants repeatedly to optimize against a score function. It first tries prompt edits and, only when prompt optimization appears insufficient, changes chain structure within the permitted scope when attribution identifies a structural bottleneck. Across six benchmarks and three task models, FAPO beats the baseline GEPA in 15 of 18 model-benchmark comparisons. In 11 model-benchmark comparisons, FAPO wins with non-overlapping mean $\pm$ trial-standard-deviation ranges, and the mean FAPO-GEPA gain is +14.1 pp. In the six HoVer and IFBench comparisons where prompt-first search escalated to structural changes, FAPO wins all six with a mean gain of +33.8 pp. FAPO also improves performance on security tasks: on CTIBench-RCM, a security CVE-to-CWE task, prompt-only FAPO lifts test accuracy by +4.0 pp on GPT-5, +7.1 pp on Foundation-Sec-8B-Instruct, and +2.0 pp on Foundation-Sec-8B-Reasoning. These results position FAPO as a state-of-the-art pipeline optimization technique for both general-purpose and security-focused tasks.
