# Caleta: An Evidence-Oriented Trust Layer for Reproducible Local Large Language Model Inference

- arXiv ID: `2611.10324v1`
- Authors: Joan-Marc Fisa
- Published: 2026-11-06
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.10324v1) | [pdf](https://arxiv.org/pdf/2611.10324v1)

## Abstract

Local large language model (LLM) inference is often described as private, verified, or reproducible without separating the technical claims behind those terms. This paper presents Caleta, an Apache-2.0 process supervisor and evidence layer around llama.cpp rather than a new inference engine. Caleta combines versioned manifests, exact-size and SHA-256 verification, controlled backend construction, a restricted OpenAI-compatible proxy, prompt-free execution records, benchmark reports, and a small conformance suite. Its contribution is the composition of these mechanisms into explicit contracts that distinguish integrity from authenticated provenance and privacy controls from operating-system isolation. We evaluate the implementation through static checks, 22 unit tests, deterministic end-to-end tests on Ubuntu, macOS, and Windows, and a pinned real-model experiment on Windows CPU using Qwen2.5-0.5B-Instruct Q4_K_M and llama.cpp b11981. The real experiment validates artifact verification, startup, model listing, non-streaming and server-sent-event chat, and conformance. Three independent benchmark invocations produced fifteen successful warm requests with no failures. In this single configuration, median time to first token was 18.066 ms and median decode throughput was 54.394 tokens/s. These descriptive measurements do not establish cross-engine superiority, output quality, energy efficiency, or hardware-general performance. Raw JSON, commands, and environment metadata are published. Remaining challenges include signed manifests, time-of-check/time-of-use replacement, operating-system containment, proxy-overhead measurement, and broader experimental matrices.
