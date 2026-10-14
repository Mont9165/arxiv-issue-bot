# Large Language Models as Falsifiers for Cyber-Physical Systems

- arXiv ID: `2609.20752v1`
- Authors: Ali ArjomandBigdeli, Jiawei Zhou, Stanley Bak
- Published: 2026-09-17
- Primary category: `eess.SY`
- Categories: `eess.SY`, `cs.AI`, `cs.LO`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.20752v1) | [pdf](https://arxiv.org/pdf/2609.20752v1)

## Abstract

Falsification searches for counterexamples to formal specifications in cyber-physical systems (CPS). With specifications written in Signal Temporal Logic (STL), falsification can be formulated as a robustness optimization problem, traditionally tackled with black-box search algorithms. In parallel, large language models (LLMs) have recently emerged as surprisingly effective optimizers when coupled with iterative prompting. In this work, we connect these ideas and introduce LLM-Falsifier, an LLM-based approach that falsifies specifications by minimizing the STL robustness degree. Beyond generic prompt-based optimization, our key idea is to expose the LLM to semantic information that is natural for language models but absent from standard numerical optimizers, including natural-language input and output names, output trajectories, and critical-time witnesses for the minimum robustness value. These additions enable smarter and more sample-efficient robustness search. On the ARCH-COMP falsification benchmarks, LLM-Falsifier is shown to outperform existing falsification tools based on a range of optimization paradigms, from surrogate-based and Bayesian optimization to search-based testing, on 14 of 21 specifications when measured by the average number of simulations required to find a counterexample.
