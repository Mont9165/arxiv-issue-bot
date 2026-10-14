# SolBehave: Evaluating the Behavioural Correctness of LLM-Generated Smart Contracts

- arXiv ID: `2610.18745v1`
- Authors: Giovanni Pio Delvecchio, Stefano Fantazzini, Giacomo Frisoni, Gianluca Moro, Lorenzo Bacchiani, Mario Bravetti, Thomas Troels Hildebrandt
- Published: 2026-10-13
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2610.18745v1) | [pdf](https://arxiv.org/pdf/2610.18745v1)

## Abstract

Large language models increasingly generate Solidity smart contracts that, once deployed, can never be patched, making a single latent fault permanent and exploitable. Yet current evaluations mostly ask only whether generated code compiles. We introduce SolBehave, a benchmark for evaluating the correctness of model-generated contracts at scale, moving beyond ad hoc unit tests. Across 250 real, reproducible Ethereum contracts, we apply three complementary tests of behavioural fidelity: differential fuzzing, historical-transaction replay, and, as our core contribution, synthetic-transaction replay guided by a Dynamic Condition Response (DCR) graph that enumerates the space of legitimate function-call sequences. Differential fuzzing compares each generated function with the original on automatically generated inputs; historical replay compares the whole contract on the transactions it actually received on-chain; DCR-guided replay compares it on sequences of calls that follow its intended usage, including orderings that never occurred on-chain. We evaluate seven state-of-the-art open-weight models after one round of automated repair. Compilation success ranges from 26.4% to 92.7%, but under differential fuzzing only 31.4% of all generated function bodies that compile, pooled over models and samples, are equivalent to the original. Divergence at the contract level is the norm rather than the exception: for six of the seven models, between 13% and 31% of the generated contracts that compile diverge from the original under historical replay, and between 13% and 44% under DCR-guided replay; only Gemma-4-31B stays below 3% on both. Compilation is therefore a necessary condition for correctness and far from a sufficient one.
