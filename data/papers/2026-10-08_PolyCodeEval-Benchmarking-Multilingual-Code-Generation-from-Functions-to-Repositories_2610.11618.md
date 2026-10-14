# PolyCodeEval: Benchmarking Multilingual Code Generation from Functions to Repositories

- arXiv ID: `2610.11618v1`
- Authors: Bowen Yang, Jiajun Jiang, Luxue Yu, Yihao Wang, Fengjie Li, Dong Wang
- Published: 2026-10-08
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.11618v1) | [pdf](https://arxiv.org/pdf/2610.11618v1)

## Abstract

As large language models increasingly move toward repository-level software engineering, existing code-generation benchmarks remain fragmented across language coverage, task granularity, and evaluation protocols, impeding systematic comparison. To address this gap, we present PolyCodeEval, a unified multilingual and multi-granularity benchmark for code generation. It comprises 2,590 code generation tasks spanning functions to repositories, derived from 58 real, executable open-source repositories in five programming languages. All tasks are evaluated under a unified execution-based protocol with integration procedures tailored to their generation targets. Building on this benchmark, we evaluate frontier large language models, state-of-the-art specialized methods, and general coding agents. Our results show that existing approaches still struggle to correctly generate complete code fragments across granularities and languages. Specifically, the studied methods generate at most 71.7%, 76.7%, and 31.0% correct functions, files, and repositories, respectively, with performance varying widely across languages. Paired experiments further show that implementation context from related functions in the same file improves the executable correctness of function generation. Method rankings also vary across task granularities and programming languages, highlighting the importance of multilingual, multi-granularity evaluation for comprehensively assessing code generation capabilities.
