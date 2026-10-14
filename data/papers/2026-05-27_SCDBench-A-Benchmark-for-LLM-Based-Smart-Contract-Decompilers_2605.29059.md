# SCDBench: A Benchmark for LLM-Based Smart Contract Decompilers

- arXiv ID: `2605.29059v1`
- Authors: Kaihua Qin, Dawn Song, Arthur Gervais
- Published: 2026-05-27
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2605.29059v1) | [pdf](https://arxiv.org/pdf/2605.29059v1)

## Abstract

Smart contract decompilation aims to recover high-level source code from bytecode, but evaluating decompilers remains difficult because existing studies use narrow datasets, inconsistent metrics, and limited semantic consistency checks. This gap is increasingly important as large language models (LLMs) begin to generate source-like Solidity that may compile and appear plausible, even when its semantics diverge from the original contract. We introduce SCDBench, a dataset and benchmark methodology for LLM-based smart contract decompilation. The dataset contains 600 real-world Solidity contracts with paired bytecode inputs, ground-truth source code, and replayable semantic checkpoints. SCDBench evaluates decompiler outputs through four cumulative stages: format completeness, compilability, Application Binary Interface (ABI) recovery, and semantic consistency via differential replay. We evaluate Claude Opus 4.7, GPT-5.3-Codex, and GLM-5 in a zero-shot decompilation setting, including GLM-5 variants with and without extended reasoning and a zero-shot compilation-repair setting. The results show that frontier LLMs can often produce structured and compilable Solidity, but achieving semantic consistency remains far from solved: the best-performing frontier model perfectly decompiles only 42/600 contracts. We further show that introducing same-model compilation repair substantially improves performance at modest additional cost. SCDBench establishes a common ground for rigorous, reproducible evaluation and aims to accelerate the development of reliable smart contract decompilers for blockchain security and transparency.
