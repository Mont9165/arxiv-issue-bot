# The Correctness Illusion in LLM-Generated GPU Kernels

- arXiv ID: `2606.20128v1`
- Authors: Dipankar Sarkar
- Published: 2026-06-18
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.DC`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2606.20128v1) | [pdf](https://arxiv.org/pdf/2606.20128v1)

## Abstract

Benchmarks for LLM-generated GPU kernels (KernelBench, TritonBench, GEAK) score correctness through fixed-shape, small-sample allclose-style checks. The number of inputs varies between benchmarks. The shape, dtype, and tolerance are fixed for each kernel. We test that oracle empirically. We construct a controlled corpus of 24 Triton and CPU stand-in kernels (15 correct controls and 9 LLM-style buggy variants seeded with documented transcription errors) and re-evaluate it under op-schema-aware seeded fuzzing with a high-precision (fp64) CPU reference and per-(op, dtype) absolute tolerances. The seeded oracle flags 9 of 9 buggy kernels and passes 15 of 15 correct controls, at zero precision cost on controls. We extend the corpus to 26 ops (adding a flash-attention pair) and re-run the same protocol on five GPU classes (RTX 3060, A10, L40S, A100 SXM4, H100 NVL). The verdicts are identical across all five GPUs: 10 of 10 illusions caught and 16 of 16 controls clean. The corpus result is about LLM-style transcription bugs that the allclose-on-one-shape oracle certifies as correct, not about the bug rate of any specific deployed LLM. Every flagged failure replays byte-for-byte from a stored seed.
