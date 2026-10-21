# MIMOS-Tools: An Integrated Toolchain for Model-Based Design of Embedded Systems

- arXiv ID: `2610.27826v1`
- Authors: Wang Yi, Chengzi Huang, Behnam Khodabandeloo, Duc Anh Nguyen
- Published: 2026-10-20
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.27826v1) | [pdf](https://arxiv.org/pdf/2610.27826v1)

## Abstract

Despite decades of progress in model-based methods and tools for embedded real-time systems, there is still no integrated environment that supports the entire development lifecycle. This paper presents MIMOS-Tools, a comprehensive toolchain spanning the key phases of development, including modeling, simulation, formal verification, real-time scheduling, schedulability and end-to-end latency analysis, and code generation for heterogeneous multicore platforms. All phases are grounded in a single, coherent, and deterministic model of computation, the MIMOS model, for which we present a formal operational semantics and establish both functional and timing determinism. This semantic foundation ensures that properties verified at the model level are preserved throughout the development process and in the generated implementation.
  A distinguishing feature of MIMOS-Tools is its support for not only deterministic but also modular, compositional design. Unlike synchronous design environments such as SCADE and Simulink, which rely on a global base clock and offline static scheduling, MIMOS-Tools supports time-triggered asynchronous communication together with flexible real-time scheduling of computation. This removes the tight global coupling of the synchronous paradigm: components can be added, modified, or updated without recomputing a system-wide schedule, enabling scalable and incremental design and dynamic updates throughout the system lifecycle. However, MIMOS-Tools also supports Simulink models when the deadlines of tasks are set to zero to emulate the zero-time semantics of synchronous design.
  The toolchain is available at uu-mimos.github.io.
