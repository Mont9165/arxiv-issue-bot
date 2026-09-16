# TasmScan: Continuation-Aware Taint Analysis for TVM Bytecode with Savelist Abstraction

- arXiv ID: `2609.16987v1`
- Authors: Yixuan Liu, Yin Wu, Yi Li
- Published: 2026-09-15
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2609.16987v1) | [pdf](https://arxiv.org/pdf/2609.16987v1)

## Abstract

The Open Network (TON), with a peak market capitalization exceeding $20 billion and over 175 million activated on-chain addresses, relies on the TVM (TON Virtual Machine) to execute smart contracts. TVM uses first-class continuations with savelists to manage control flow and register state across continuation invocations. Since savelist-captured registers allow data to flow across continuation boundaries without passing through the operand stack, bytecode-level analyses cannot construct complete data flow tracking without explicitly modeling savelist semantics. We present TasmScan, the first bytecode-level static analysis framework for TVM that enables cross-continuation data flow reasoning without requiring source code. TasmScan models savelist semantics via forward register analysis with a formal over-approximation guarantee for exact-resolved save sites and locally tracked register definitions, then lifts bytecode into TASIR, a typed intermediate representation, and performs path-sensitive taint analysis with context-aware sources to detect defects. We evaluate TasmScan on 2,921 contracts from the TON verifier registry and a labeled benchmark of 208 contracts with human-confirmed ground truth. On the full corpus, TasmScan resolves 294,546 dynamic continuation targets with 100% precision; ablation confirms that savelist propagation is essential for resolving indirect register calls that depend on cross-continuation register passing. On the benchmark, TasmScan detects 95.3% of defects across five classes with 96.8% precision. A 366-pair stratified sample from the full corpus estimates 85.8% overall precision. TasmScan offers a 17x median speedup over the state-of-the-art symbolic-execution baseline, and in the path-analysis comparison completes 100% of analyses with zero crashes or timeouts.
