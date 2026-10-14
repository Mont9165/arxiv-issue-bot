# Kaizen: Metamorphic Fuzzing and Differential Testing for LLM-Translated HPC Applications

- arXiv ID: `2607.04058v1`
- Authors: Oscar Ludwig, Ninad Anklesaria, Zheming Jin, Swaroop Pophale, Kausar Moshood, Christian J. DeVore, Brandon Gill, Cassius Villareal, Keita Teranishi, Manish Motwani
- Published: 2026-07-04
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2607.04058v1) | [pdf](https://arxiv.org/pdf/2607.04058v1)

## Abstract

Large language models (LLMs) are increasingly used to port scientific codes across heterogeneous high-performance computing (HPC) programming models, such as translating CUDA to OpenMP, OpenACC, Kokkos or SYCL. However, current evaluations use compilation success, token-level similarity, or developer-written tests from static benchmarks, which cannot reliably ensure behavioral correctness. We present Kaizen, a metamorphic fuzzing and differential testing framework for evaluating the correctness of LLM-translated HPC code. Kaizen uses metamorphic fuzzing via source-code mutation to generate semantically equivalent programs, grammar-based input fuzzing to explore behavioral diversity, and differential testing to expose semantic divergences between original and translated applications that compile and pass developer-written tests yet produce incorrect scientific results. We evaluate Kaizen on CUDA-to-OpenMP translation of 16 scientific applications from seven domains using three fine-tuned LLMs at kernel-level and full-program granularity. Our evaluation reveals that (1) compilation success is a poor proxy for correctness; (2) LLM-translated programs exhibit systematic compile-time error patterns, with nine categories for kernel-level translation and 27 for full-program translation; (3) semantic errors that survive compilation are often input-dependent and require differential testing to expose; and (4) full-program translation is substantially harder than kernel-level translation. These findings highlight the need for correctness-oriented evaluation of LLM-assisted HPC code translations.
