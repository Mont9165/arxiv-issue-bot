# Archer: Towards Agentic Review for Compiler Optimizations

- arXiv ID: `2607.01808v1`
- Authors: Yunbo Ni, Shaohua Li
- Published: 2026-07-02
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.01808v1) | [pdf](https://arxiv.org/pdf/2607.01808v1)

## Abstract

Modern compilers are frequently updated, but expert review capacity is highly limited, leading to delayed integration and, in some cases, subtle semantic bugs entering the compiler codebase. Automating the code review process with modern general code review agents may be feasible, but it faces critical challenges due to compiler complexity. In this paper, we use LLVM as our target compiler and present Archer, the first automated agentic code review tool for compiler optimizations. Archer constrains the agentic review process from both ends by using obligations to guide analysis and a deterministic validation guard to admit only findings backed by executable evidence.
  We evaluated Archer on 70 open PRs and 328 closed PRs in LLVM from the last two months. The review results are shocking and concerning: Archer discovers that 21% of open PRs and 11% of closed PRs are buggy, i.e, introducing semantic bugs such as miscompilations in LLVM. Our findings expose a critical gap in the capacity for critical review in large compiler projects and demonstrate the practical value of Archer as an additional reviewer.
