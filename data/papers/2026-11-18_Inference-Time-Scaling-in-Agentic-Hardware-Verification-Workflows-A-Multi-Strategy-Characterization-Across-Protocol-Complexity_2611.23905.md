# Inference-Time Scaling in Agentic Hardware Verification Workflows: A Multi-Strategy Characterization Across Protocol Complexity

- arXiv ID: `2611.23905v1`
- Authors: Vikash Kumar
- Published: 2026-11-18
- Primary category: `cs.AR`
- Categories: `cs.AR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.23905v1) | [pdf](https://arxiv.org/pdf/2611.23905v1)

## Abstract

Inference-time scaling, allocating more compute during generation rather than pre-training, has demonstrated dramatic quality improvements for LLM reasoning tasks. Its behaviour in structured hardware verification code generation, where outputs must satisfy compiler correctness, protocol semantics, and functional coverage constraints simultaneously, is less understood. We present a systematic, simulator-grounded study of inference-time compute scaling for agentic UVM testbench synthesis targeting AMBA protocol bridges. Four inference strategies---zero-shot (\$0.04), raw-feedback iterative (\$0.81), structured inner-loop (\$0.95), and full dual-loop agentic synthesis (\$1.06)---are evaluated across four AMBA targets (Protocol Complexity Index 11.8--22.6) using the Protocol Verification Completeness (PVC) metric, functional coverage, and a six-class UVM error taxonomy (E1--E6). Our central finding is that structured diagnostic feedback acts as an inference-time compute multiplier: the structured inner loop yields roughly $15\times$ more PVC per inference dollar than raw EDA-tool feedback (marginal efficiency, S1$\to$S2 vs. S0$\to$S1). The mechanism is fault targeting, not token reduction: raw compiler feedback drives the testbench to compile but cannot surface functional protocol faults that leave the code syntactically valid, whereas structured E1--E6 bundles diagnose and resolve them. All outputs are judged by a cycle-accurate Mentor Questa toolchain rather than by model self-assessment; the dual-loop strategy reaches PVC $\geq$ 0.95 with zero scoreboard errors on every target, and the generated environments surfaced a latent RTL bug in two of the four reference designs. These results establish a principled compute-quality trade-off curve for LLM-aided verification environment generation and motivate inference-budget-aware deployment strategies for industrial EDA workflows.
