# Validating LLM-Modernized Scientific Software Through Differential Fault Injection

- arXiv ID: `2608.14527v1`
- Authors: Evan Coleman, Yuzhong Shen, Masha Sosonkina, Peng Xu
- Published: 2026-08-14
- Primary category: `cs.DC`
- Categories: `cs.DC`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.14527v1) | [pdf](https://arxiv.org/pdf/2608.14527v1)

## Abstract

Large language model (LLM) agents are increasingly used to modernize the legacy Fortran underlying production scientific software, but validation of these transformations emphasizes nominal executions and may not test whether a modernization preserves the original code's response to faults, perturbations, and reduced precision. We present a differential fault-injection validation method: a harness instruments the shared self-consistent-field driver of GAMESS at twelve sites and applies identical, deterministic faults to the original and LLM-modernized implementations, isolating the converted integral kernels. Across more than 2,200 runs, transient-fault absorption costs match a contraction-based model (predicted slopes 0.74 and 1.49 iterations per bit; measured 0.82 and 1.50), persistent perturbations halve final-energy error per additional bit, and the campaigns expose phase-dependent parallel deadlocks and false convergence under reduced precision. The original and modernized kernels agree in all 200 paired injections, and a measurement-guided synchronization change composes with the modernization, matching in all 40 pairs.
