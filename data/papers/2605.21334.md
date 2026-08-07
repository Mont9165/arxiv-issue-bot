# RSE of a Quantum Transport Code and its Effects

- arXiv ID: `2605.21334v1`
- Authors: Christoph Conrads, Edoardo Di Napoli
- Published: 2026-05-20
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CE`, `physics.comp-ph`
- Links: [abs](http://arxiv.org/abs/2605.21334v1) | [pdf](https://arxiv.org/pdf/2605.21334v1)

## Abstract

This paper presents our research software engineering (RSE) experiences over two years with libNEGF, a quantum transport code. We describe practical approaches to code quality assurance--including continuous integration, automated testing, and compiler warning correction--and performance engineering through continuous benchmarking. Our systematic application of these practices revealed critical defects: uninitialized memory reads, out-of-bounds writes, and notably, a misunderstood mathematical model in our boundary condition handling. We also document how continuous benchmarking exposed performance regressions caused by HPC system configuration changes. Our findings provide data points suggesting that a dangerous class of defects--equivalent to undefined behavior in C/C++ and processor-dependent behavior in Fortran--is as prevalent in Fortran scientific codes as elsewhere. While libNEGF is implemented in Fortran, most recommendations are applicable to scientific software regardless of implementation language, and they can be implemented selectively or in their entirety for both new and existing projects.
