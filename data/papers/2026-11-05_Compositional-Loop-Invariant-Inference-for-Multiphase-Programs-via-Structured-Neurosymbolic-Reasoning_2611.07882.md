# Compositional Loop Invariant Inference for Multiphase Programs via Structured Neurosymbolic Reasoning

- arXiv ID: `2611.07882v1`
- Authors: Mingxiu Wang, Jiawei Wang, Shuangxiang Kan, Angela Huo, Yuekang Li, Xi Zheng, Xiao Cheng
- Published: 2026-11-05
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.07882v1) | [pdf](https://arxiv.org/pdf/2611.07882v1)

## Abstract

Loop invariants are essential for deductive program verification, yet automatically inferring them for {multiphase programs}, whose loops contain conditional branches that induce multiple execution phases with distinct behaviors, remains an open problem. Existing LLM-based methods either reason about loops as a whole or use explicit branch information to generate atomic assertions jointly across branches, without maintaining complete candidate sub-invariants for independent generation and targeted repair. We present CLOVER, a structured neurosymbolic reasoning framework for multiphase invariant inference built on two interlinked mechanisms. First, compositional inference: CLOVER statically decomposes a loop into symbolic {loop branch sequences}, conjunctions of the loop guard and branch conditions that characterize distinct execution scenarios, and guides the LLM to generate candidate sub-invariants for each one independently, so that each LLM query focuses on a single execution scenario rather than the entire loop. Second, counterexample-guided localized refinement: when SMT verification rejects a composed disjunctive invariant, CLOVER traces the counterexample back through the branch structure to identify which specific loop branch sequence caused the failure and repairs only that sub-invariant, preserving all correct components. Both mechanisms are unified by a shared symbolic structure derived from the loop's branch semantics, which guides what the LLM generates, how candidates are composed, and where refinement is directed. We evaluate CLOVER on 316 linear arithmetic, 50 nonlinear arithmetic, and 54 multiphase benchmarks. CLOVER solves 35 of 54 multiphase benchmarks, outperforming the best LLM-based baseline (29) by 20.7\% and the best traditional method (22) by 59.1\%. On linear/nonlinear benchmarks, CLOVER remains competitive, solving 355 of 366 programs overall.
