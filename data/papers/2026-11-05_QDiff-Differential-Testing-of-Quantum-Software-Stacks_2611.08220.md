# QDiff: Differential Testing of Quantum Software Stacks

- arXiv ID: `2611.08220v1`
- Authors: Jiyuan Wang, Qian Zhang, Guoqing Harry Xu, Miryung Kim
- Published: 2026-11-05
- Primary category: `quant-ph`
- Categories: `quant-ph`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.08220v1) | [pdf](https://arxiv.org/pdf/2611.08220v1)

## Abstract

Over the past few years, several quantum software stacks (QSS) have been developed in response to rapid hardware advances in quantum computing. A QSS includes a quantum programming language, an optimizing compiler that translates a quantum algorithm written in a high-level language into quantum gate instructions, a quantum simulator that emulates these instructions on a classical device, and a software controller that sends analog signals to a very expensive quantum hardware based on quantum circuits. In comparison to traditional compilers and architecture simulators, QSSes are difficult to tests due to the probabilistic nature of results, the lack of clear hardware specifications, and quantum programming complexity.
  This work devises a novel differential testing approach for QSSes, named QDIFF with three major innovations: (1) We generate input programs to be tested via semantics-preserving, source to source transformation to explore program variants. (2) We speed up differential testing by filtering out quantum circuits that are not worthwhile to execute on quantum hardware by analyzing static characteristics such as a circuit depth, 2 qubit gate operations, gate error rates, and T1 relaxation time. (3) We design an extensible equivalence checking mechanism via distribution comparison functions such as Kolmogorov Smirnov test and cross entropy
