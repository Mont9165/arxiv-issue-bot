# Closed-loop evaluation of LLM agents for embedded software development

- arXiv ID: `2610.11447v1`
- Authors: Jorge García-Carrasco, Sergio García-Carrasco, Alejandro Maté, Juan Trujillo
- Published: 2026-10-08
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.AR`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2610.11447v1) | [pdf](https://arxiv.org/pdf/2610.11447v1)

## Abstract

Large language models (LLMs) are increasingly deployed as coding agents that edit files, run builds and tests, inspect execution results, and repair software iteratively. Embedded firmware is a demanding target because correctness depends on closed-loop behavior under sensing, timing, and safety constraints, not only on static source quality. Yet embedded-agent evaluation remains limited and often emphasizes one-shot synthesis or offline correctness.
  We present a benchmark for closed-loop evaluation of embedded coding agents. Each task provides a plain-text engineering description, constrained workspace, and visible build-and-runtime surface. The agent must translate requirements into implementation and self-verification steps, then iterate until the required device behavior is achieved. The suite contains five embedded-control tasks and four feedback scenarios: one-shot generation, realistic self-verification, CI-style red/green feedback, and oracle-style detailed feedback.
  The implementation targets simulated ESP32 firmware for reproducibility. We evaluate seven GPT-family and Qwen-family configurations across five tasks and four scenarios, with three repetitions per condition for 420 runs. gpt-5.4 has the highest pass rate among evaluated configurations but does not saturate the benchmark; qwen3.5-27B is the strongest observed local model; and smaller local models degrade sharply in pass rate and search efficiency. These results suggest that capable local embedded coding agents are emerging.
