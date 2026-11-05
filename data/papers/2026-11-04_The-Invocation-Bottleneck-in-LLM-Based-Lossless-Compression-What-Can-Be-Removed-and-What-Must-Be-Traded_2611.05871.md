# The Invocation Bottleneck in LLM-Based Lossless Compression: What Can Be Removed and What Must Be Traded

- arXiv ID: `2611.05871v1`
- Authors: Zhe Yan, Yihao Liu, Antonio Boffa, Huanchen Zhang
- Published: 2026-11-04
- Primary category: `cs.IT`
- Categories: `cs.IT`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.05871v1) | [pdf](https://arxiv.org/pdf/2611.05871v1)

## Abstract

Large language models (LLMs) compress text far better than classical compressors, but LLM-based compressors are slow, particularly during decompression. We argue that their decoding time has two fundamentally different sources. Execution redundancy, such as per-token host transfers, CPU-side coding, and token-by-token encoding, is work that the coded output does not require and can be removed without changing a single output bit. Sequential dependency, one model call per decoded token, is inherent to lossless decoding and cannot be removed by better execution, only traded for more calls or for more bits. We remove execution redundancy with a GPU-resident pipeline whose block-parallel encoding is made lossless in half precision by batch-invariant kernels, speeding up arithmetic coding by up to 5.8x in encoding and 3.0x in decoding without changing its compression rate. We then study the two ways of trading sequential dependency, speculative dual-model coding (SDMC) and multi-token single-model coding (MSMC), characterize the compression cost of predicting several tokens from a shared prefix, and identify the workloads in which fewer model calls are worth that cost.
