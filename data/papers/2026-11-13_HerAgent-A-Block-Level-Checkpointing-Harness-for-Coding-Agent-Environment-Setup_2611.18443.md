# HerAgent: A Block-Level Checkpointing Harness for Coding-Agent Environment Setup

- arXiv ID: `2611.18443v1`
- Authors: Xiang Li, Siyu Lu, Federica Sarro, Claire Le Goues, He Ye
- Published: 2026-11-13
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.18443v1) | [pdf](https://arxiv.org/pdf/2611.18443v1)

## Abstract

Modern coding agents rely on establishing executable software environments before they can perform software engineering tasks such as testing, debugging, and patch validation. Existing setup agents typically control progress at either single-command or whole-script granularity, making recovery either too local to remove polluted state or too coarse to preserve useful progress. We present HerAgent (Harness EnviRonment Setup Agent), a block-level harness for coding-agent environment setup. HerAgent's main contribution is semantic setup blocks: a single progress-control abstraction used for execution, validation, checkpointing, repair, and rollback. Evaluated against six prior agents on four environment-setup datasets, HerAgent improves setup success in every comparison, achieving the largest gains on Installamatic-Bench (52.0% to 85.0%) and SetupBench (46.3% to 70.4%). It also reduces setup costs by up to 94.5%, showing that block-level progress control improves reliability and efficiency.
