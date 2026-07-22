# TraceDev: A Traceability-Driven Multi-agent Framework for Requirement-to-Code Development

- arXiv ID: `2607.18886v1`
- Authors: Mingyu Chen, Yakun Zhang, Zihao Xie, Yixing Luo, Jinrui Xu, Cuiyun Gao, Kaiqi Zhao, Yunming Ye
- Published: 2026-07-21
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.18886v1) | [pdf](https://arxiv.org/pdf/2607.18886v1)

## Abstract

In modern software development, the rapid advancement of Large Language Models (LLMs) has made the end-to-end transformation of Natural Language Requirements (NLRs) into executable repository-level code increasingly feasible. However, existing approaches typically rely on simplified instructions (e.g., single-sentence descriptions), failing to reflect complex software development scenarios. Moreover, they lack explicit requirement traceability mechanisms, making it difficult to precisely align and validate generated code against original requirements. To address these limitations, we propose TraceDev, a multi-agent framework for automated software development grounded in use cases that contain multiple functional points and complex semantics. TraceDev employs five role-specific agents, including a Requirement Refiner, Designer, Developer, Tester, and Validator. Notably, the Validator Agent constructs and maintains a heterogeneous traceability graph that links requirements, design models, and code artifacts for interacting with the preceding four agents. The traceability graph maintains consistency across various artifacts and serves as a structured context for efficient memory management, supporting reliable repository-level code generation. We evaluate TraceDev on two widely used datasets (including 125 use cases) compared with two state-of-the-art approaches. On the ETOUR dataset, TraceDev achieves a success rate of 53.63\%, outperforming baseline approaches by up to 186.63\%. A similar trend is observed on the SMOS dataset, where TraceDev attains a success rate of 56.82\%, exceeding baseline approaches by up to 340.80\%. These results demonstrate the effectiveness of TraceDev in repository-level code generation from requirements.
