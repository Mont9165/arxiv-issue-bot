# CrackMeBench: Binary Reverse Engineering for Agents

- arXiv ID: `2605.10597v1`
- Authors: Isaac David, Arthur Gervais
- Published: 2026-05-11
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.10597v1) | [pdf](https://arxiv.org/pdf/2605.10597v1)

## Abstract

Benchmarks for coding agents increasingly measure source-level software repair, and cybersecurity benchmarks increasingly measure broad capture-the-flag performance. Classical binary reverse engineering remains less precisely specified: given only an executable, can an agent recover validation logic and produce an input, serial, artifact, or key generator accepted by the program? We introduce CrackMeBench, a benchmark for evaluating language-model agents on educational CrackMe-style reverse-engineering tasks. CrackMeBench focuses on deterministic binary validation problems with executable oracles, symbol-poor binaries, explicit local tool access, and externally scored submissions rather than free-form explanations. The v0 benchmark combines eight public calibration CrackMes with twelve generated main-score tasks built from seeded C, Rust, and Go templates, and agents run through an equal shell interface in a no-network Linux Docker sandbox with standard reverse-engineering tools. In a three-model evaluation with a five-minute budget and three scored submissions per task, pass@3 on the generated split is 11/12 tasks (92%) for GPT-5.5, 7/12 (58%) for Claude Opus 4.7, and 5/12 (42%) for Kimi K2. The harder generated half separates the models more sharply, with pass@3 of 5/6, 2/6, and 1/6, respectively; on the eight-task public calibration split, pass@3 is 3/8, 2/8, and 1/8. CrackMeBench records pass@1 and pass@3, scored submissions, wall-clock time, command traces, tool categories, provider-reported token usage, estimated cost, and qualitative failure labels, providing a reproducible testbed for measuring progress from source-code reasoning toward autonomous binary analysis while restricting scope to educational, purpose-built programs.
