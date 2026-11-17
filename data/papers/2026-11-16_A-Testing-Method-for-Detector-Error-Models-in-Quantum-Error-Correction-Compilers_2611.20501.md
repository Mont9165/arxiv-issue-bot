# A Testing Method for Detector Error Models in Quantum Error Correction Compilers

- arXiv ID: `2611.20501v1`
- Authors: Junjie Luo, Yasunari Suzuki
- Published: 2026-11-16
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.20501v1) | [pdf](https://arxiv.org/pdf/2611.20501v1)

## Abstract

A quantum error correction (QEC) compiler produces, from a code and a noise model, both the physical circuit to execute and a detector error model (DEM). The DEM lists the probability of each error mechanism and the measurements it flips. Decoders consume the DEM without verification, so a defect that describes the noise incorrectly calibrates the decoder against wrong rates and silently degrades the logical error rate. Existing techniques for testing quantum software judge correctness by crashes or by statistics of sampled outputs. DEM defects that only distort rates lie below what sampling can resolve at the error rates where QEC operates. We present DEMVal, a testing method that validates each model the compiler emits against a reconstructed reference, with rates obtained from outside the compiler under test. It compares the two models exactly, so its sensitivity is independent of the physical error rate. The reference can be built in three ways that jointly cover the pipeline from source program to emitted model. Applied to NVIDIA's CUDA-Q QEC, Riverlane's Deltakit, and the deq component of Microsoft's QDK-EC, DEMVal found six defects, all confirmed by the developers and fixed. Sampling could have exposed only the four defects that drop, merge, or misplace mechanisms, and exposing all four requires millions of samples per experiment. Even analytically optimal moment tests miss the two rate-level defects, while exact model comparison detects all six with no samples. To our knowledge, DEMVal is the first systematic testing method for the error-model semantics of QEC compilers.
