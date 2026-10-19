# ForTress: Bringing Assurance and Determinism for LLM-Driven Fortran-to-Python Translation

- arXiv ID: `2610.22528v1`
- Authors: Qinrun Dai, Ruitong Liu, Chien-Wei Huang, Guanhong Tao, Guannan Wei, Yueqi Chen
- Published: 2026-10-15
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.22528v1) | [pdf](https://arxiv.org/pdf/2610.22528v1)

## Abstract

Modernizing mature scientific software from Fortran to Python can improve accessibility and integration with modern computing tools, but manual rewriting is expensive. Large language models (LLMs) make translation more practical, yet generated code can pass regression tests while violating source-language semantics, and contextual corrections may not persist across subsequent translations. We present ForTress, which solidifies recurring LLM translation decisions into guarded executable rules for deterministic reuse and provides semantic assurance for a non-trivial subset of these rules. Its LLM-assisted auditing process expresses universally quantified preservation obligations over mechanized Fortran and Python semantics in Lean. Human experts review semantic fidelity and correspondence with production rules, and Lean's kernel checks proofs and refutations under explicit assumptions. These audit records expose the conditions either supporting correctness or identifying failure cases. We evaluate ForTress on 17 benchmarks from 15 scientific software spanning diverse domains. The translated programs achieve bitwise-identical with native Fortran on all evaluated tests under the recorded execution and initialization configurations. Against these software, ForTress accumulates 193 executable rules and 188 audit records, of which 121 have checked soundness proofs, including 31 established after counterexample-guided refinement. Cross-software reuse exceeds 90% for 14 of the 15 software. Even with additional assurance and determinism, the LLM usage cost is 44.2% lower than direct LLM translation.
