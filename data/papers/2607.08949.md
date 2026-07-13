# SeedSmith: LLM-Driven Seed Synthesis for Directed Fuzzing

- arXiv ID: `2607.08949v1`
- Authors: Junmin Zhu, Siyu Liu, Jie Hu, Fabio Gritti, Ati Priya Bajaj, Hulin Wang, Wenbo Guo, Tiffany Bao, Christopher Kruegel, Giovanni Vigna
- Published: 2026-07-09
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.08949v1) | [pdf](https://arxiv.org/pdf/2607.08949v1)

## Abstract

Directed fuzzing steers fuzzers toward user-defined sink functions to identify vulnerabilities, but it frequently fails to trigger crashes even after long campaigns. We identify two challenges that prevent directed fuzzers from exposing crashes: incomplete static analysis of indirect calls, which leaves reachable paths invisible to distance-based guidance, and lack of semantic guidance for crash preconditions, which blind mutation cannot satisfy within practical time budgets. A natural intervention point is the initial seed corpus: seeds that encode the right control-flow path and satisfy key crash preconditions shift fuzzing from blind exploration to local refinement. Existing seed generation approaches address neither: grammar-based and format-driven methods produce structurally valid inputs with no sink awareness, while LLM-based methods either lack sink targeting or inherit static analysis limitations through one-shot prompting. We present SeedSmith, an agentic LLM pipeline that replicates a security analyst's workflow: starting from a sink, it iteratively explores the codebase, resolves indirect calls, identifies crash preconditions, and synthesizes concrete inputs that satisfy them. Because SeedSmith operates as a seed generation front-end, its seeds are fuzzer-agnostic and improve any downstream mutation-based fuzzer without modification. On Magma, fuzzers using SeedSmith seeds achieve geometric mean crash-time speedups of 11.51 times (AFL++) to 14.66 times (AFLGo) over default seeds. On ARVO, SeedSmith enables fuzzers to trigger 16 previously unreachable bugs spanning 10 projects with diverse input formats.
