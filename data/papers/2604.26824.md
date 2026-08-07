# A Test Taxonomy and Continuous Integration Ecosystem for Dynamic Resource Management in HPC

- arXiv ID: `2604.26824v1`
- Authors: Petter Sandås, Íñigo Aréjula-Aísa, Sergio Iserte, Antonio J. Peña
- Published: 2026-04-29
- Primary category: `cs.DC`
- Categories: `cs.DC`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.26824v1) | [pdf](https://arxiv.org/pdf/2604.26824v1)

## Abstract

High-performance computing (HPC) systems are increasingly exploring dynamic resource management and malleable MPI applications to better adapt to heterogeneous architectures, fluctuating workloads, and energy constraints. However, the correctness of the libraries that support these techniques is often evaluated through ad hoc experiments that can be difficult to reproduce and maintain. This article introduces methodology for testing dynamic resource management frameworks that combines a taxonomy of tests for MPI malleable libraries with an HPC-oriented continuous integration (CI) ecosystem. The taxonomy structures functional and non-functional tests at both component-integration and system levels. The CI ecosystem instantiates this taxonomy in a containerized virtual cluster enabling automated validation. The approach is instantiated and evaluated using the Dynamic Management of Resources (DMR) framework as a representative case study. Results show that the proposed methodology improves early fault detection, simplifies maintenance under evolving dependencies, and transfers to other malleability solutions that expose analogous primitives for initialization, readiness checking, and reconfiguration.
