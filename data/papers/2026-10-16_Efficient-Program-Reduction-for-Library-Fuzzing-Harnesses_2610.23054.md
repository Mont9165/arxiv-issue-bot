# Efficient Program Reduction for Library Fuzzing Harnesses

- arXiv ID: `2610.23054v1`
- Authors: Haiying Li, Yunlong Lyu, Peng Chen, Hao Chen
- Published: 2026-10-16
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.23054v1) | [pdf](https://arxiv.org/pdf/2610.23054v1)

## Abstract

Library fuzzing harnesses translate generated inputs into API calls. When a complex harness triggers a crash, developers must determine whether the cause is a library defect or invalid harness usage. A smaller reproducer can simplify this investigation, but obtaining one requires repeatedly building and executing modified harnesses and analyzing their crashes, making manual or even automatic minimization time-consuming. Moreover, data-dependent statements prevent the reducer to remove unnecessary code and the heavy stack trace symbolization in libraries also slows down the candidate execution. To address these challenges, we present HarnessMinimizer, a system for efficient minimization of C/C++ library fuzzing harnesses. Its optimized pipeline reuses header analysis and prepared libraries and runtimes to reduce the work required to build and execute each simplified harness during the reduction process. It records and replays input values so that unnecessary input operations can be removed without changing the values supplied to surviving calls. It also uses a fast method to check whether each simplified harness preserves the original crash, avoiding repeated stack trace symbolization. We evaluate HarnessMinimizer with four reduction engines on 200 crash cases from 21 open source libraries. Compared with the unoptimized pipeline, HarnessMinimizer achieves speedups of 3.46-4.51 times in average total wall time. Average harness size decreases from 1,352 original tokens to 143-263 remaining tokens after minimization. In crash triage using a large language model, accuracy in identifying harness bugs increases from 28% with the original harnesses to 44-51% with the minimized harnesses, while accuracy for library bugs remains at 100%.
