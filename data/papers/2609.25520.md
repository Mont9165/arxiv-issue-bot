# Dynamic Conformance Testing of WebGPU Through Specification-Driven Mutation

- arXiv ID: `2609.25520v1`
- Authors: Mahya Samdaliri, Zhihao Yao, Kasthuri Jayarajah
- Published: 2026-09-22
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2609.25520v1) | [pdf](https://arxiv.org/pdf/2609.25520v1)

## Abstract

WebGPU is a low-level graphics and compute API that exposes modern GPU functionality to web applications. While the official WebGPU Conformance Test Suite (CTS) focuses on well-formed usage under the WebGPU specification, it is not designed to stress implementations with semantic edge cases or adversarial inputs. General-purpose fuzzers, in contrast, struggle with WebGPU because of its complex graphics stack and multi-process architecture. We introduce LANTERN, a specification-guided dynamic conformance testing framework that mutates CTS tests using constraints extracted from the WebGPU specification. LANTERN extracts explicit syntactic API rules from WebIDL definitions and recovers semantic constraints, such as command ordering and object lifetimes, from natural-language specification text. Selected rules guide AST-located textual transformations that generate both valid and intentionally invalid CTS variants. We execute the resulting tests at scale on AddressSanitizer-instrumented Chromium to discover bugs. Our evaluation discovers three reproducible bugs, including a heap corruption, in Chromium versions current at the time of study. These results demonstrate that syntactically seeded, semantics-aware mutation of conformance tests provides a way to uncover browser bugs during WebGPU testing.
