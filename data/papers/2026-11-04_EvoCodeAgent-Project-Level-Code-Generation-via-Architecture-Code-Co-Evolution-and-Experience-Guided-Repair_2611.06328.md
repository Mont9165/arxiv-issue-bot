# EvoCodeAgent: Project-Level Code Generation via Architecture-Code Co-Evolution and Experience-Guided Repair

- arXiv ID: `2611.06328v1`
- Authors: Qianhui Zhao, Li Zhang, Fang Liu
- Published: 2026-11-04
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.06328v1) | [pdf](https://arxiv.org/pdf/2611.06328v1)

## Abstract

Project-level code generation aims to automatically synthesize complete software repositories from high-level requirements, producing coherent multi-file systems with well-structured modules and consistent cross-file dependencies. Despite the strong capabilities of large language models (LLMs) in specification understanding and code synthesis, existing approaches still exhibit several critical limitations. First, many methods rely on static architectural designs that cannot adapt during iterative generation, leading to a growing misalignment between architecture and implementation. Second, they lack mechanisms to accumulate and reuse experience across iterations, resulting in recurring errors and reduced efficiency. Third, they often depend on standalone LLM-based evaluation of intermediate artifacts, which suffer from limited transparency and potential unreliability under long-context reasoning. To address these challenges, we propose EvoCodeAgent, a state-centric framework for project-level code generation. EvoCodeAgent maintains an evolving architectural state initialized from structured project specifications and continuously reconciles predicted relations from architecture and skeletons with realized relations extracted from generated code. It further uses tool-grounded verification evidence to support reliable state updates and abstracts reusable repair experiences from previous revision attempts to guide subsequent generation. Extensive experiments on project-level benchmarks of different scales, including DevBench and CodeProjectEval, demonstrate that EvoCodeAgent consistently outperforms baseline approaches. Under the GPT-5 setting, it achieves unit test pass rates of 60.48% and 27.73%, respectively, yielding up to a 53.5% improvement over the strongest baseline.
