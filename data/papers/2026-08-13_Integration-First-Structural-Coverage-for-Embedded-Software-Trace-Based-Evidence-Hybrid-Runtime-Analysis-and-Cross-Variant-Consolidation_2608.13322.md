# Integration-First Structural Coverage for Embedded Software:Trace-Based Evidence, Hybrid Runtime Analysis, and Cross-Variant Consolidation

- arXiv ID: `2608.13322v1`
- Authors: Alexander Weiss, Albert Schulz, Michael Wittner
- Published: 2026-08-13
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.13322v1) | [pdf](https://arxiv.org/pdf/2608.13322v1)

## Abstract

Structural coverage is widely used as evidence that testing is complete, yet in embedded projects it is predominantly collected at unit level, simply because that is where instrumentation and observability are inexpensive. This produces a mismatch. The most representative completeness signal would come from integration and system tests executed on the device under test, but classical instrumentation perturbs timing, memory footprint and concurrency behaviour, while purely trace-reconstructed coverage loses reliability for decisions and conditions as soon as the compiler optimizes aggressively. We address this mismatch from both ends. On the process side we describe an integrationfirst coverage strategy that treats integration and system tests as the baseline measurement and drives the residual gaps through an explicit closure loop, so that completeness is established as covered or justified rather than as covered alone. On the technical side we use embedded trace as the observation path and add hybrid runtime analysis (hRA): a minimal, semantics-preserving observability scaffolding that keeps decision and condition boundaries distinguishable in the trace stream of an optimized (-O3) build, while all coverage state and counting remain off-target. This converts object-to-source mapping from a heuristic reconstruction into reviewable evidence and makes branch, condition and MC/DC measurement practical on release-like binaries. Finally we describe Hyper Coverage, a consolidation layer that merges evidence across test levels, test runs, variants and build configurations, and that exposes source lines which remain untested in every relevant variant.
