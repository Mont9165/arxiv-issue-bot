# Veritas: A Semantically Grounded Agentic Framework for Memory Corruption Vulnerability Detection in Binaries

- arXiv ID: `2605.15097v1`
- Authors: Xinran Zheng, Alfredo Pesoli, Marco Valleri, Suman Jana, Lorenzo Cavallaro
- Published: 2026-05-14
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2605.15097v1) | [pdf](https://arxiv.org/pdf/2605.15097v1)

## Abstract

Detecting memory corruption vulnerabilities in stripped binaries requires recovering object semantics, interprocedural propagation, and feasible triggers from low-level, lossy representations. Recent LLM-based approaches improve code understanding, but reliable detection still requires grounding in memory-relevant semantics and runtime feasibility evidence. We present Veritas, a semantically grounded framework for binary memory corruption vulnerability detection. Veritas combines a static slicer over RetDec-lifted LLVM IR, a dual-view LLM detector that reasons step by step over grounded flows using decompiled C and selective LLVM IR, and a multi-agent validator that checks hypotheses against debugger-visible artifacts and runtime evidence. The slicer reconstructs value-flow relations from LLVM-IR facts, including def-use, calls, returns, globals, and pointer operations, and emits compact witness-backed flow objects. The detector uses these artifacts to reason about control flow, bounds, and object correspondence without rediscovering whole-binary propagation. The validator confirms or rejects candidates through guided debugging, breakpoint inspection, and memory-checking oracles. We implement Veritas as a modular pipeline and evaluate it on a curated benchmark of real-world binary vulnerability cases. Veritas achieves 90\% recall. For false-positive assessment, we exhaustively validate and manually verify 623 detector candidates and audit additional candidates from larger cases. The exhaustive subset produces no false positives, while the additional audit identifies two confirmed false positives. In a real-world application, Veritas discovered a previously unknown Apple vulnerability that was confirmed and assigned a CVE. These results support semantic grounding as an operational design principle for practical binary vulnerability detection.
