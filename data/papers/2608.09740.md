# Security Tests as Executable Specifications for LLM Code Generation: Benefits, Trade-offs, and Coverage Limits

- arXiv ID: `2608.09740v1`
- Authors: Yunhao Liang, Chengguang Gan, Ruixuan Ying
- Published: 2026-08-10
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.09740v1) | [pdf](https://arxiv.org/pdf/2608.09740v1)

## Abstract

Large language models (LLMs) can generate functionally useful code that remains vulnerable, while security-focused interventions may break intended behavior. We investigate security tests as executable specifications both before generation and during iterative repair. We develop SecTDD, a controlled test-feedback scaffold that separates three factors: whether tests are shown upfront, whether failed executions trigger revision, and how failures are selected and represented. The evaluation uses behavior-partitioned visible and hidden tests and byte-identical initial candidates for repair comparisons. Across 2,705 trajectories, 31 task instances, three secure-code benchmarks, 16 CWE categories, and two model families, showing all visible tests upfront increases hidden functional-and-security joint success by 19.3 percentage points on average, but improves only seven of nine benchmark-model conditions and harms two. In shared-candidate comparisons, structured feedback repairs 80 initially unsuccessful candidates with no joint regressions; fixed raw feedback repairs 83 but causes three regressions. Structured and raw feedback are otherwise nearly indistinguishable head-to-head (six wins, six losses, and 453 ties). Candidates that pass all visible tests still fail hidden behavior families under every common regime. These results show that executable feedback can repair secure-code generation, but its benefits depend on the model, task, feedback entry point, and especially test coverage.
