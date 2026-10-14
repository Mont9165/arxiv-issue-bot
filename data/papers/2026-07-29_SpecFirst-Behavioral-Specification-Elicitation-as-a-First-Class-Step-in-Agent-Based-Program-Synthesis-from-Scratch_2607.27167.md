# SpecFirst: Behavioral Specification Elicitation as a First-Class Step in Agent-Based Program Synthesis from Scratch

- arXiv ID: `2607.27167v1`
- Authors: Yihao Chen, Shi Chang, Feng Lin, Khaled Chawa, Boyuan Chen, Shaowei Wang, Ahmed E. Hassan
- Published: 2026-07-29
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2607.27167v1) | [pdf](https://arxiv.org/pdf/2607.27167v1)

## Abstract

LLM-based agents excel at software engineering tasks where an existing codebase provides context, but constructing a program from scratch remains fundamentally harder. Recent benchmarks such as ProgramBench quantify this gap: given only natural-language documentation and an execute-only binary as a behavioral oracle, even frontier models solve fewer than 1% of instances. Existing frameworks conflate documentation reading, behavioral exploration, and code synthesis into a single pass, causing agents to probe insufficiently, lose behavioral intent as context drifts, and propagate early misinterpretations into the final implementation. Inspired by classical requirements engineering, we argue that behavioral specification elicitation should be a first-class phase that precedes implementation. We present SpecFirst, a two-stage framework that forces the specification elicitation before code synthesis. A dedicated spec agent first probes the binary and combines observations with documentation into a structured specification. Next, a code synthesis agent then uses this specification to drive implementation. This decomposition resolves documentation ambiguities before coding begins and provides a stable behavioral reference throughout synthesis. We evaluate SpecFirst on all 200 ProgramBench instances across four models spanning two families and an order of magnitude of capability. SpecFirst consistently outperforms the single-loop baseline, improving test pass rates by 6.9%-21.3% and binary exploration coverage by 9.4%-18.5%, all statistically significant. Behavioral analysis on code synthesis further shows that a prior specification enables earlier and more sustained code construction. Our results demonstrate that an explicit requirements-engineering phase is an effective paradigm for from-scratch program construction.
