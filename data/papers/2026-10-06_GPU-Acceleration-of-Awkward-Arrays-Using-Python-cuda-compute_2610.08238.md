# GPU Acceleration of Awkward Arrays: Using Python cuda.compute

- arXiv ID: `2610.08238v1`
- Authors: Maksym Naumchyk, Ianna Osborne
- Published: 2026-10-06
- Primary category: `cs.DC`
- Categories: `cs.DC`, `cs.PF`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.08238v1) | [pdf](https://arxiv.org/pdf/2610.08238v1)

## Abstract

Awkward Array is a widely used library in high-energy physics (HEP) for representing and manipulating nested, variable-length data in Python. Previous CHEP contributions have explored GPU acceleration for Awkward Array, demonstrating the feasibility and performance benefits of CUDA-based backend while also identifying limitations related to irregular data access, fine-grained kernel launches, and composability of operations. In this contribution, we present recent developments that build directly on these earlier efforts by introducing a CUDA execution model for Awkward Array based on the Python CUDA Core Compute Libraries (CCCL).
  Using CCCL, we eliminate the need for custom CUDA kernels and can instead use a high-level Python interface. The CCCL-based approach also enables fusion of multiple Awkward operations into a reduced number of CUDA kernels, addressing kernel launch overhead observed in earlier GPU implementations. Lazy execution allows expression graphs to be constructed and optimized prior to kernel generation, improving performance for analysis workflows involving jagged arrays, combinatorial operations, and reductions. In contrast to earlier approaches, this design also emphasizes extensibility, allowing user-defined Python code to be incorporated into GPU execution paths with minimal boilerplate and without breaking existing analysis semantics.
  We present performance studies that demonstrate improvements over previously reported eager GPU execution strategies for representative HEP analysis patterns. These developments extend the GPU capabilities of Awkward Array toward a more composable and sustainable backend, aligned with the needs of Python-based analysis at the HL-LHC and beyond.
