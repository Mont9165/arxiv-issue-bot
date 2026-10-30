# Write Once, Instrument Anywhere: Portable, Sandboxed Tooling with WebAssembly Components

- arXiv ID: `2610.38682v1`
- Authors: Elizabeth Gilbert, Chris Fallin, Heather Miller, Ben L. Titzer
- Published: 2026-10-28
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2610.38682v1) | [pdf](https://arxiv.org/pdf/2610.38682v1)

## Abstract

Monitoring and debugging deployed software is crucial for scalability, performance, and robustness. Cross-cutting concerns are pervasive across software ecosystems, yet engineers must address them with a fragmented toolbox. While high-level frameworks exist to offer application-level types and semantics, they often lock a solution into specific languages, runtimes, or hardware architectures. Portability often forces engineers to choose lower-level instrumentation mechanisms. For example, in-language frameworks can trace a request across processes, but multi-language contexts require instrumentation at the boundary, for example using eBPF. While these frameworks provide powerful capabilities, they often result in 1) a tradeoff between application-level types or low-level bytes and packets, 2) non-composable domain-specific tools, 3) feature fragmentation across frameworks, and 4) tools that often run with unrestricted access to the program and its environment.
  We address these problems with Splicer, a WebAssembly component interposition framework that 1) provides semantically rich application-level types, 2) enables pluggable tooling with powerful capabilities, 3) reduces ecosystem fragmentation through porting across languages and hardware, and 4) confines each tool to a sandbox with explicitly granted permissions. We evaluate Splicer on a suite of benchmarks demonstrating the pluggability of non-trivial tooling written in multiple source languages and their performance.
