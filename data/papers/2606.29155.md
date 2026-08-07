# OASIF: An Efficient Obfuscation-Aware Self-Improving Framework for LLM-Based Assembly Code Instruction Following and Comprehension

- arXiv ID: `2606.29155v1`
- Authors: Xinyi Wang, Rongze Chen, Ke Wang, Qiyuan Chen, Yanming Liu, Xiang Li, Chunfu Jia
- Published: 2026-06-28
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.29155v1) | [pdf](https://arxiv.org/pdf/2606.29155v1)

## Abstract

Large Language Models (LLMs) have recently shown promise in automated binary analysis, yet they remain brittle under commercial-grade obfuscation. We present OASIF, an Obfuscation-Aware Self-evolving Instruction-Following framework for obfuscated assembly comprehension. OASIF couples a token-efficient assembly encoder with a lightweight projector to expose long obfuscated code to a pretrained code LLM under a bounded context budget and follows a three-phase training: (i) feature-space alignment, (ii) supervised instruction fine-tuning, and (iii) online self-evolving reinforcement learning with hybrid rewards, enabling continual adaptation with minimal manual verification. On VMISA-Bench, a challenging out-of-distribution suite featuring three commercial VM-based obfuscators, OASIF consistently improves open-source backbones; Qwen2.5-Coder-Instruct-14B attains Success Rate gains of +15.9, +5.8, and +16.9 percentage points (pp) on Code Virtualizer, Themida (v3.0.7), and VMProtect (v3.5), respectively, and improves the OASIF-Bench average by +9.8. OASIF further delivers stable gains across seven standard BCSD benchmarks while preserving general and domain-relevant capabilities on HumanEval, VulBench, and HumanEval-Decompile.
