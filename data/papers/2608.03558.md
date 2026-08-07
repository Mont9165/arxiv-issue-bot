# EffiHolmes: Differential Profiling-Guided Repository Level Time Inefficiency Fix Localization

- arXiv ID: `2608.03558v1`
- Authors: Haowen Yang, Yun Peng, Zishuo Ding
- Published: 2026-08-04
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.03558v1) | [pdf](https://arxiv.org/pdf/2608.03558v1)

## Abstract

Large software systems often suffer from time inefficiencies that cause excessive execution time despite functional correctness. Localizing their fix locations is difficult because, unlike functional bugs, they produce neither test failures nor stack-trace clues, making traditional and recent LLM-based fault localization methods unsuitable. Runtime profiling provides alternative evidence but faces three challenges in repository-level settings: single-run profiling cannot reliably distinguish inefficiency hotspots from execution noise; existing profilers struggle to extract relevant execution paths from extensive background execution; and a semantic gap remains between observed hotspots and actual fix locations. We propose EffiHolmes, an LLM-based framework for repository-level time inefficiency fix localization. EffiHolmes uses differential profiling under default and scaled workloads to identify inefficiency hotspots, extracts compact execution paths connecting these hotspots to the reported inefficient function, and employs domain-guided LLM reasoning to locate the underlying inefficiency logic. We also introduce RepoEffi-Bench, the first benchmark for repository-level inefficiency localization, containing 140 high-quality issues collected from popular Python repositories. Experiments show that EffiHolmes consistently outperforms state-of-the-art retrieval-, agent-, and profiling-based baselines, improving file-level Acc@3 by 4.29 percentage points with GPT-5.1 and function-level Acc@5 by 15.00 percentage points with qwen3-4b. It also remains robust across model capacities.
