# ConCovUp: Effective Agent-Based Test Driver Generation for Concurrency Testing

- arXiv ID: `2605.09573v1`
- Authors: Yuandao Cai, Shuhao Fu, Wensheng Tang, Cheng Wen, Shengchao Qin, Charles Zhang
- Published: 2026-05-10
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.09573v1) | [pdf](https://arxiv.org/pdf/2605.09573v1)

## Abstract

Concurrency testing is essential to improve the reliability and security of multi-threaded programs. Dynamic analysis tools, such as TSan, depend on high-quality test drivers that reach critical shared-memory interactions at runtime. However, current testing practices predominantly focus on sequential logic, leaving a gap in automated concurrent test generation. Recently, large language models (LLMs) have shown promise in generating sequential tests, but they struggle to produce effective concurrent tests without a deep understanding of concurrency semantics. This paper presents ConCovUp, a multi-agent framework that combines LLMs with program analysis. ConCovUp grounds test generation in static analysis to extract shared memory accesses and their calling contexts. To trigger hard-to-reach accesses, it introduces an LLM-driven backward tracing approach, leveraging the model's semantic reasoning to deduce concrete inputs that satisfy complex path constraints, and iteratively refines the generated tests via dynamic execution feedback. Our evaluation on nine real-world C/C++ libraries shows that ConCovUp improves average Shared Memory Access Pair Coverage (SMAP Coverage) from 36.6% to 68.1% over the general Claude Code agent baseline.
