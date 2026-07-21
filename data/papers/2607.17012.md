# Schema-Bound LLM Control of Scientific Instrumentation through Model Context Protocol Skills

- arXiv ID: `2607.17012v1`
- Authors: Roberto dos Reis, Vinayak P. Dravid
- Published: 2026-07-19
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cond-mat.mtrl-sci`, `physics.ins-det`
- Links: [abs](http://arxiv.org/abs/2607.17012v1) | [pdf](https://arxiv.org/pdf/2607.17012v1)

## Abstract

Large language models (LLMs) can plan tool-mediated scientific work, but scientific instruments remain difficult to connect to such agents: vendor APIs may load only inside acquisition host processes, facilities may prohibit cloud-hosted agents, and natural-language interfaces can emit physically unreasonable arguments. We present a method for connecting local LLMs to scientific instruments through the Model Context Protocol (MCP). It combines: (1) a schema-bound tool surface that validates requests against physical bounds before adapter dispatch; (2) a vendor-neutral, host-process adapter pattern separating language-side reasoning from instrument-side execution; (3) a persistent lifecycle for long-running live-processing jobs; and (4) MCP-prompt-registered skills that compose typed tools into reusable multi-step protocols. Our open-source reference server exposes 30 typed tools, 5 live-job types, and 6 skills through a physics-plausible simulator implementing the same protocol surface. Validation is software-only: all 120 hardware-independent tests pass deterministically, while 15 local-LLM integration tests pass 12-15 of 15 across runs because of model nondeterminism. A preliminary single-run probe across five open tool-calling LLMs indicates that the schema-bound interface can be driven locally by small open-weight models without cloud dependency; it is not a benchmark and has no confidence intervals. The method provides a bounded, testable, and reproducible foundation for closed-loop agentic instrumentation research.
