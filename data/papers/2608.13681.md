# Fine-Tuning Qwen3-27B for C-to-Rust Code Translation: A Three-Stage Curriculum of Pretraining, Debugging-Aware SFT, and Task-Specific SFT

- arXiv ID: `2608.13681v1`
- Authors: Pu Zhao, Changdi Yang, Yixiao Chen, Yi Gao, Yifan Cao, Haochen Zeng, Yanzhi Wang
- Published: 2026-08-13
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.ET`
- Links: [abs](http://arxiv.org/abs/2608.13681v1) | [pdf](https://arxiv.org/pdf/2608.13681v1)

## Abstract

Translating C code into safe, idiomatic Rust is a longstanding software-engineering goal because it can eliminate entire classes of memory-safety vulnerabilities while preserving the functional behavior of legacy systems. Large language models (LLMs) have shown promise for this task but typically underperform when applied off-the-shelf, since general-purpose pretraining rarely emphasizes idiomatic Rust generation, cross-language semantic equivalence, or the ability to reason about and repair compiler/runtime feedback. In this report we describe a three-stage fine-tuning curriculum applied to Qwen3-27B that is designed to progressively specialize the model for the C-to-Rust (C2Rust) translation task: (1) continued pretraining on Rust-centric corpora to strengthen the model's prior over idiomatic Rust syntax and standard-library usage; (2) supervised fine-tuning (SFT) on the microsoft/Verus_Training_Data dataset to instill debugging and self-repair behavior over Rust code; and (3) task-specific SFT on paired C/Rust solutions derived from LeetCode problems to teach direct semantic translation. We evaluate the resulting model using the agentic, static-analysis-guided verification framework of SACTOR, which performs structure-aware, two-phase (unidiomatic to idiomatic) translation with foreign-function-interface (FFI)-based end-to-end (E2E) testing. We report success rate, idiomaticity (Clippy lint counts, unsafe-code fraction), and failure-mode analyses, and compare our fine-tuned model against baseline Qwen3-27B and other LLMs evaluated under the same framework.
