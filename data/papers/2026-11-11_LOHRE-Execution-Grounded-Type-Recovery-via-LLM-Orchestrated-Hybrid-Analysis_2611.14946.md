# LOHRE: Execution-Grounded Type Recovery via LLM-Orchestrated Hybrid Analysis

- arXiv ID: `2611.14946v1`
- Authors: Hao Jiang, Yujie Yang, Tao Li, Chenhui Cui, Liangfeng Xu, Chengjie Liu, Weiping Wen, Rubing Huang, Tsong Yueh Chen
- Published: 2026-11-11
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.14946v1) | [pdf](https://arxiv.org/pdf/2611.14946v1)

## Abstract

Documenting stripped binary functions for security analysis requires recovering function interfaces and user-defined type (UDT) layouts from machine code. Existing large language model (LLM)-based methods face two limitations: they lack execution-based validation to detect inferred UDTs inconsistent with actual memory layouts, and may overlook evidence about shared UDTs across functions without direct call relationships. We present LLM-Orchestrated Hybrid Reverse Engineering (LOHRE), a framework that treats inferred UDTs as falsifiable hypotheses and tests them against program execution. LOHRE uses a hypothesize-validate-refine loop to test candidate layouts through paired dynamic slice emulation of baseline and mutated inputs. To reduce the cost of processing lengthy execution histories, the Execution-Depth Heuristic (EDH) compresses paired traces into an execution-depth difference and a summary of the tested field's observed uses. A cross-function knowledge base aggregates compatible UDT hypotheses and field-level confidence scores to guide testing and hypothesis refinement. We evaluate LOHRE on RealType at four optimization levels and a Windows remote procedure call (RPC) dataset. LOHRE achieves an average UDT Structural accuracy of 57.85% across RealType's four optimization levels and 35.6% on Windows RPC, outperforming the evaluated static baselines. Disabling dynamic validation reduces accuracy to 19.28% on RealType and 9.2% on Windows RPC. Removing the cross-function knowledge base reduces accuracy to 41.03% on RealType and 10.0% on Windows RPC. Replacing EDH's compressed feedback with full execution traces reduces recovery accuracy while increasing token use by 3.7 times and runtime by 3.0 times. These results indicate that execution-based validation, compact feedback, and cross-function evidence contribute to accurate and efficient UDT recovery.
