# Unsaid, Unsafe? Implicit Security Obligations in LLM-Based RTL Code Generation

- arXiv ID: `2608.26588v1`
- Authors: Guang Yang, Xing Hu, Xiang Chen, Xin Xia
- Published: 2026-08-27
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.26588v1) | [pdf](https://arxiv.org/pdf/2608.26588v1)

## Abstract

Large Language Models (LLMs) generate register-transfer-level (RTL) code with rapidly improving functional correctness. Security of LLM-generated code, however, has been studied mainly for software, where flaws can still be patched after deployment. Insecure RTL offers no such remedy once taped out into silicon. We construct SECRTL-GEN, a multi-language resource-access security benchmark grounded in real SoC IP: 392 tasks over five CWE families and four HDLs (Verilog, SystemVerilog, VHDL, and Python), each with black-box functional and security testbenches. Functional specifications intentionally omit security obligations, matching how obligations are often kept out of functional docs in practice. An empirical study of five frontier LLMs shows a sharp gap: under vanilla prompts they pass functional tests in about 73-79% of cases but security tests in only 14-35%, and stronger functional models are not safer. Adding CWE knowledge raises security, while unaided self-thinking helps less and both security-oriented prompts cut functional pass rates, showing that the bottleneck is missing weakness awareness in the specification, not an inability to write defensive RTL. We present RTL-Obliger, a neuro-symbolic framework that infers these implicit obligations. An LLM extracts a functional-semantic graph from the specification; a symbolic engine then matches it against a CWE pattern ontology to surface mitigation-evidence gaps and signal-level obligations; the LLM finally revises RTL under those obligations in a functionality-preserving two-stage generation. Across five models and four languages, RTL-Obliger raises mean all-pass from 49.6-51.4% (SecV/RESCUE) to 61.6%, with higher security and functional rates than these secure-generation baselines.
