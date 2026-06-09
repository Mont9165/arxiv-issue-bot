# Structuring agentic AI for HPC code modernization

- arXiv ID: `2606.08710v1`
- Authors: Anthony Marinov, Igor Sfiligoi
- Published: 2026-06-07
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.08710v1) | [pdf](https://arxiv.org/pdf/2606.08710v1)

## Abstract

Modernization of legacy scientific codes is often necessary to keep up with the ever-evolving changes in the compute resource ecosystem. Parallelization and migration from poorly supported software ecosystems are two of the most time-consuming activities in the research software engineering field. This paper presents our experience in the successful, two-phase AI-assisted modernization of NMAP-RKPM, a roughly 60,000-line, 3D explicit solid mechanics physics engine based on the Reproducing Kernel Particle Method (RKPM). We converted this single-threaded, Fortran based MPI application into a OpenMP-parallel C++ based MPI tool in the span of a few months. While Large Language Model (LLM) based tools on their own proved inadequate, we developed a highly structured "hand-holding" agentic AI methodology, like providing manually created examples, ensuring continuous buildability and limiting session scope, that was instead highly effective. The paper provides both the AI-assisted steps that were successful and the problems that we had to overcome, alongside the reasoning behind the chosen path.
