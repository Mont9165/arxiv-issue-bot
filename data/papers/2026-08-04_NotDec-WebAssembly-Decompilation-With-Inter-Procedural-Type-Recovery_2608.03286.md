# NotDec: WebAssembly Decompilation With Inter-Procedural Type Recovery

- arXiv ID: `2608.03286v1`
- Authors: Jikai Wang, Ningyu He, Tianming Liu, Junhai Wang, Haoyu Wang
- Published: 2026-08-04
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.03286v1) | [pdf](https://arxiv.org/pdf/2608.03286v1)

## Abstract

With WebAssembly widely supported in browsers, containers, IoT devices, and serverless platforms and increasingly adopted as a universal low-level bytecode standard, auditing its hidden vulnerabilities and malicious intentions has become critical. Decompiling existing WebAssembly modules can help security researchers and end users understand binary behavior, but current tools suffer from verbose result, poor readability, and limited type recovery.
  We present NotDec, an advanced WebAssembly decompilation framework. NotDec extends the WebAssembly type checking algorithm to lift bytecode into an SSA-based IR, applies the inter-procedural type recovery algorithm Retypd with pointer and numeric value differentiation methods to recover complex data structures, and leverages Memory SSA alongside semantics-preserving structured control-flow analysis to emit readable, semantically consistent C code.
  NotDec achieves 100% recompilation success rate on all 5,241 Juliet samples and all Howard dataset programs, significantly outperforming baselines including Ghidra (45.95% success rate). On type recovery accuracy, NotDec recovers 85.33% of struct member accesses in real-world programs, vastly exceeding Ghidra's 9.24%. While the full inter-procedural version faces scalability challenges on large binaries, the intra-procedural variant NotDec_F demonstrates superior efficiency, consuming less than half of Ghidra's memory and up to 97% less execution time on unoptimized binaries.
