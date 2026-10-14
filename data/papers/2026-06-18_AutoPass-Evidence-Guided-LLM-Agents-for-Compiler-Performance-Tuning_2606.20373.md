# AutoPass: Evidence-Guided LLM Agents for Compiler Performance Tuning

- arXiv ID: `2606.20373v1`
- Authors: Zepeng Li, Jie Ren, Zhanyong Tang, Jie Zheng, Zheng Wang
- Published: 2026-06-18
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.20373v1) | [pdf](https://arxiv.org/pdf/2606.20373v1)

## Abstract

Large Language Models (LLMs) show promise for code compilation tasks, but applying them to runtime performance tuning is difficult due to complex microarchitectural effects and noisy runtime measurements. We present AutoPass, a multi-agent framework for compiler performance tuning that uses compiler and runtime evidence to guide LLM-generated optimization decisions. Rather than treating the compiler as a black box like prior auto-tuning schemes, AutoPass opens up the compiler to the LLM, enabling it to query compiler-internal optimization states and analyze the intermediate representation to orchestrate compiler options. The search process iteratively refines optimization configurations using measured runtime feedback to diagnose regressions and guide latency-improving edits. AutoPass operates in an inference-only, training-free setting and requires no offline training or task-specific fine-tuning, making it readily applicable to new benchmarks and platforms. We implement AutoPass on the LLVM compiler and evaluate it on server-grade x86-64 and embedded ARM64 systems. AutoPass outperforms expert-tuned heuristics and classical autotuning methods, achieving geometric-mean speedups of 1.043x and 1.117x over LLVM -O3 on x86-64 and ARM64, respectively.
