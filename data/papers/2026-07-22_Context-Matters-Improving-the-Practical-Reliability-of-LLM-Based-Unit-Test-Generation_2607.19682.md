# Context Matters: Improving the Practical Reliability of LLM-Based Unit Test Generation

- arXiv ID: `2607.19682v1`
- Authors: Junjie Chen, Ziqi Wang, Lin Yang, Chen Yang, Xiao Chu, Jianyi Zhou, Guangtai Liang, Qianxiang Wang, Dong Wang
- Published: 2026-07-22
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.19682v1) | [pdf](https://arxiv.org/pdf/2607.19682v1)

## Abstract

Automated unit test generation has recently benefited from advances in large language models (LLMs), yet our industrial deployments reveal a persistent gap between promising research results and practical usability. In real-world projects with complex frameworks and cross-file dependencies, LLM-generated tests frequently fail to compile, require costly manual repair, or provide unstable coverage improvements. This paper reports our experience in designing, deploying, and evaluating CATGen, a context-aware workflow for LLM-based unit test generation, informed by repeated industrial failures and refinements. Rather than relying on LLMs to infer incomplete project context, we found that compilation robustness critically depends on making project-level dependencies explicit, stabilizing test class scaffolding, and replacing iterative LLM-based repair with lightweight static analysis. These experience-driven insights shaped CATGen's multi-stage design, which combines structured context retrieval, deterministic test skeleton construction, and program analysis-based post-processing. We evaluate CATGen on real-world complex focal methods from proprietary industrial projects and additionally on the Defects4J benchmark to assess generalizability. Across both settings, CATGen substantially improves compilation success and structural coverage while significantly reducing generation time and token consumption compared to existing LLM-based approaches. Our results demonstrate that reliable LLM-based unit test generation in practice depends less on prompt engineering alone and more on systematic engineering support grounded in real-world development constraints.
