# Benchmarking Text-to-SQL under Role-Based Access Control

- arXiv ID: `2607.22115v1`
- Authors: Yang Fei, Yangfan Jiang, Yin Yang, Xiaokui Xiao
- Published: 2026-07-24
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.22115v1) | [pdf](https://arxiv.org/pdf/2607.22115v1)

## Abstract

Given a database S and a natural language question Q, text-to-SQL systems aim to generate an SQL query that correctly answers Q when executed against S. Currently, popular text-to-SQL benchmarks mostly assume unrestricted access to S; in practice, however, user access is often restricted, e.g., through role-based access control (RBAC) policies. This leads to a potential disconnect between benchmarking results and real-world performance: an LLM with high benchmark scores might perform poorly in an access-controlled environment, by frequently violating RBAC, or rejecting a query q that could be answered with only permitted data in S. Motivated by this, we present a comprehensive text-to-SQL benchmarking framework with realistic RBAC constraints, which features an LLM-assisted workflow that augments existing text-to-SQL benchmarks with plausible user roles and access policies. To do so, we formulate the problem of role synthesis as a structured reasoning process over the database schema, in which the LLM first infers the application context from the schema, and then derives role responsibilities and access scopes consistent with this context. This process is audited by human-in-the-loop quality control, in which domain experts perform metric-guided screening on the generated roles. Besides the augmented dataset, the proposed framework also contains evaluation metrics that identify RBAC-specific failure modes, and disentangle SQL utility from access-control compliance. We apply the proposed framework to several widely-used benchmarks, and conduct a systematic empirical study of state-of-the-art text-to-SQL systems. The results show that many solutions (especially open-weight LLMs) with high benchmarking scores under an unrestricted setting suffer sharp performance degradation once access constraints are in place, due to frequent RBAC violations.
