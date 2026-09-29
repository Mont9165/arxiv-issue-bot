# Faultless: A Program Equivalence Technique for Validating and Evaluating Neural Decompilers

- arXiv ID: `2609.34089v1`
- Authors: Luke Dramko, Claire Le Goues, Edward Schwartz
- Published: 2026-09-28
- Primary category: `cs.PL`
- Categories: `cs.PL`, `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.34089v1) | [pdf](https://arxiv.org/pdf/2609.34089v1)

## Abstract

Neural decompilers are machine learning models which perform the process of decompilation, lifting code from a lower-level language to a higher one. Neural decompilers offer substantial utility relative to traditional deterministic decompilers because they can probabilistically recover information discarded during lowering, like variable names, types, and control flow structuring. However, they can also make mistakes, producing code that is not equivalent to the original, making it difficult to trust their output.
  In this work, we introduce Faultless, a program equivalence technique for performing translation validation on neural decompilers. Faultless compares code produced by a deterministic decompiler, which has stronger correctness properties, with that of a neural decompiler. Faultless is also useful for model evaluation, a highly related task, in which the neural decompilers' prediction is compared with a reference solution. Neural decompilation introduces significant challenges to the task of program equivalence which existing techniques are not equipped to handle, including limited extrafunctional context and systematic semantic inconsistencies in decompiled code. Faultless takes a static symbolic execution-based approach with an execution model and memory model designed to handle these challenges.
