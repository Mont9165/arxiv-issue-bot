# Meta Build Systems as Logic Programs

- arXiv ID: `2611.17672v1`
- Authors: Alex Reinking
- Published: 2026-11-13
- Primary category: `cs.PL`
- Categories: `cs.PL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.17672v1) | [pdf](https://arxiv.org/pdf/2611.17672v1)

## Abstract

Meta build systems such as CMake, Meson and Bazel derive command graphs from project descriptions, user choices and machine facts. Imperative scripts, search paths and special cases make routine decisions interact poorly: search order can choose compatible packages without an explicit project choice, packagers must patch author flag preferences, and cross-builds need annotations or nested build trees for tools run during the build.
  Our central insight is to express configuration as relational inference: objects follow from sources, flags and libraries from dependencies, and language standards from transitive requirements. We introduce buildlog, a meta build system whose stratified logical core isolates build derivation from impure environmental probes. It rejects ambiguity in toolchain or package selection and explains derived facts through provenance. Author constraints and user preferences use distinct, statically checked input relations. Libraries can ship consumer rules, including Qt's moc/rcc rules, using the same facts for installed and built code. Using a compiled program in a build rule lets buildlog infer its build-machine configuration.
  We evaluate buildlog on eleven case studies of ten projects, validating configurations through execution and artifact checks while reporting remaining flag differences and platform limits. In Halide, generators link an LLVM-based compiler and run during the build to emit WebAssembly or Android code; where CMake requires nested builds, buildlog derives build-machine and target-platform configurations in one graph. A supporting formal account establishes termination, within-round probe-order independence, and agreement between fresh and validated cached runs under explicit finiteness and probe obligations. The results show that confining impurity to fact discovery yields a small, uniform and explainable configuration semantics.
