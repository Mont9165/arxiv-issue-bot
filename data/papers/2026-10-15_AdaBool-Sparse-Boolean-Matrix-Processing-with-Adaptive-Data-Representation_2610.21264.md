# AdaBool: Sparse Boolean Matrix Processing with Adaptive Data Representation

- arXiv ID: `2610.21264v1`
- Authors: Xiangrui Yang, Yifan Lei, Jiawei Yang, Yekang Zhan, Yuxin Zheng, Lei Mao, Zhaoren Wu, Yibo Huang, Yiming Qiu
- Published: 2026-10-15
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.DC`
- Links: [abs](http://arxiv.org/abs/2610.21264v1) | [pdf](https://arxiv.org/pdf/2610.21264v1)

## Abstract

Many data processing tasks revolve around determining whether logical relationships exist between two sets of entities, a pattern that can be naturally modeled as Sparse Boolean Matrix Multiplication (SpBMM). Under Boolean semantics, matrix representations no longer need to store numerical values and instead focus on encoding the positions of non-zero elements, making it highly amenable to data compression for substantially lower memory access overhead. The key challenge, however, is that the most effective compression depends heavily on sparsity distribution: different methods perform best at different sparsity levels, while real-world matrices often contain sharply varying sparsity across regions. Consequently, forcing the entire matrix into any fixed, monolithic representation leaves considerable optimization opportunities untapped.
  We present AdaBool, a SpBMM framework designed to reconcile this tension through an adaptive data representation. AdaBool partitions matrices into fine-grained element blocks and represents each block with the encoding best matched to its local sparsity. On top of this adaptive encoding, AdaBool introduces a heterogeneous GPU execution model that groups blocks by encoding type and maps them to matching processing paths, enabling efficient execution and scheduling across GPU resources. We implement AdaBool end to end with low-level system optimizations, evaluate it on both production and public workloads, and show that it outperforms representative baselines by over an order of magnitude.
