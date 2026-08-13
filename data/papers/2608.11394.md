# GraphAlignCoder: Aligning Program and Proof Graphs for Code Generation

- arXiv ID: `2608.11394v1`
- Authors: Yueke Zhang, Zihan Fang, Kevin Leach, Yu Huang
- Published: 2026-08-11
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.11394v1) | [pdf](https://arxiv.org/pdf/2608.11394v1)

## Abstract

Code large language models (LLMs) can generate syntactically plausible programs that nevertheless violate hidden semantic constraints. Existing execution-feedback training methods identify whether a completed program fails, but provide limited supervision about how a correct solution should be organized. We introduce GraphAlignCoder, a training framework that transfers explicit correctness structure into code generation.
  GraphAlignCoder constructs an implementation graph that captures control and dependence among program regions. In parallel, a constrained Lean pipeline produces proof traces, from which we extract a formal proof-flow graph. The model first learns executable code together with graph-derived descriptions of why individual program regions are correct, and then consolidates this knowledge into code generation. GraphAlignCoder consistently outperforms the base model, code-only SFT, and CodeRL across all benchmarks. Compared with CodeRL, it increases the solved count from 38 to 50 on LiveCodeBench v6 and from 16 to 23 on BigCodeBench Hard, corresponding to relative gains of 31.6% and 43.8%, while also improving BigCodeBench Full from 359 to 363 tasks. The ablation study further shows that verification-graph injection produces the initial reasoning gain, while verification to code consolidation is essential for robust cross-benchmark transfer.
