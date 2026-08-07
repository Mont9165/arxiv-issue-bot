# Multi-Channel Spread-Spectrum Code Watermarking

- arXiv ID: `2607.06009v1`
- Authors: Soohyeon Choi, Debin Gao, Yue Duan
- Published: 2026-07-07
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.06009v1) | [pdf](https://arxiv.org/pdf/2607.06009v1)

## Abstract

Attributing code to the large language model that produced it is essential for provenance, licensing, and misuse accountability, yet no deployed watermark meets this need. Generation-time schemes require access to the producing model and cannot be applied to third-party code, while post-hoc schemes work on any code but carry at most 4 bits of payload, far too few to distinguish the many deployed model configurations. We present multi-channel spread-spectrum watermarking, the first post-hoc, training-free code watermark with a 24-bit payload and formal robustness guarantees. The scheme encodes bits in variable naming conventions and in eight pairs of semantically equivalent code patterns, and a keyed pseudo-random permutation maps every site to a codeword bit so that each bit receives multiple independent votes. Majority voting absorbs distributed corruption, while an outer Reed-Solomon code recovers the identifier when concentrated channel attacks defeat the vote, yielding provable robustness bounds for formatting, syntactic, and structural attacks. Across 1,750 Python files from CodeNet and from GPT-4.1 and Llama-4 generations, the watermark achieves 100% clean-detection accuracy with zero false positives. Under 17 attack types, it recovers the identifier at 97.6% accuracy under 8 variable renames and 94.1% under 10% random per-site corruption, while the strongest post-hoc baseline collapses to 0% under any single-transform attack. Embedding and detection together take under 200 ms on CPU without training data or GPU.
