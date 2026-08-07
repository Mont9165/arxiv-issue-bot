# Multi-Source and Cross-Scenario Strategy-Guided Code Optimization

- arXiv ID: `2607.20353v1`
- Authors: Yuwei Zhao, Qianyu Xiao, Ye Cui, Yijun Yu, Yingfei Xiong
- Published: 2026-07-22
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.20353v1) | [pdf](https://arxiv.org/pdf/2607.20353v1)

## Abstract

Automated code optimization improves program performance by refactoring source code, and recent studies use LLMs to generate optimization patches. The newest approaches are strategy-guided: they summarize strategies from historical optimization commits as static analysis rules, and use these rules to match code locations for LLMs to optimize. However, these approaches have two limitations: (1) the strategies may come from other knowledge sources, such as textbooks and web pages, but the existing approaches cannot utilize them; (2) a strategy may be applicable to different scenarios, e.g., different programming languages, but existing approaches can only formalize strategies for the scenario to which the source commit belongs. To address these limitations, we propose MoST, an LLM-based code optimization framework that integrates multiple knowledge sources across scenarios. MoST uniformly represents items in different knowledge sources as evidence objects, clusters them in a cross-source and cross-scenario manner to identify strategies, and transfers them to the target scenario when necessary for generating static analysis rules. To implement this process, MoST employs a novel self-balanced weighted clustering algorithm to balance evidence objects from different knowledge sources, and a novel example transfer procedure to ensure the quality of the generated rules when transferring across scenarios. On a benchmark containing 151 C/C++, 150 Python, and 50 Rust historical optimization tasks, compared with SemOpt, MoST yields 24.44%-180.00% and 21.88%-37.50% more patches that are exactly the same as or semantically equivalent to developer patches, respectively. When optimizing 15 real-world projects, MoST achieves 19.72%-717.42% maximum improvements and 4.44%-258.17% average improvements for the performance tests in the projects, significantly outperforming SemOpt and Codex.
