# LeanReviewBench: Semantic Alignment Review in Mathematical Lean Projects

- arXiv ID: `2611.30361v1`
- Authors: Ruichen Qiu, Hao Shen, Lihong Zhi, Xiao-Shan Gao
- Published: 2026-11-23
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.30361v1) | [pdf](https://arxiv.org/pdf/2611.30361v1)

## Abstract

Lean verifies that a proof establishes its formal proposition, but whether that proposition preserves the mathematical content of an informal source requires separate review. In project-scale formalizations, this correspondence can depend on definitions and constraints distributed across many declarations. We introduce LeanReviewBench, a benchmark for project-level semantic alignment review containing 197 versioned inputs collected from 18 real Lean projects, with 87 aligned and 110 misaligned reference judgments. Each input binds an informal mathematical target to selected formal declarations and an extracted dependency context. Construction combines development-history discovery, independent target binding, reconstruction under a common Lean environment, and Astra annotation with human review of uncertain cases. The collection spans diverse mathematical domains and includes 69 historical pairs. We evaluate six language models with Direct and ReForm prompts on all 197 inputs against final human-reviewed reference labels. GPT-6.1 Sol with Direct prompting achieves the highest reported accuracy of 0.827 and misalignment-detection F1 of 0.844; the effects of prompting vary across models. LeanReviewBench provides a testbed for reviewing semantic correspondence in existing mathematical formalization projects. LeanReviewBench is available at https://github.com/MechMath/LeanReviewBench.
