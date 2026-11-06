# An LLM-Orchestrated Neuro-Symbolic Framework for Verifying Diagnostic Signal Reachability in Electronic Systems

- arXiv ID: `2611.07040v1`
- Authors: Heba Jaradat, Mohammed-Khalil Ghali, Saurabh Kulkarni, Rohan Kulkarni, Sangwon Yoon
- Published: 2026-11-04
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.07040v1) | [pdf](https://arxiv.org/pdf/2611.07040v1)

## Abstract

Diagnostic Signal Reachability (DSR) captures whether board-level health signals are observable by management controllers, including baseboard management controllers (BMCs), complex programmable logic devices (CPLDs), and other smart controllers. Verifying DSR is essential for field diagnosability in datacenter fleets, where one design is deployed at massive scale, yet it remains largely manual, since each signal is traced by hand across schematic sheets, renamed nets, series components, and monitoring devices. Large language models (LLMs) are attractive but unreliable at structural connectivity reasoning, where over-claiming can silently hide a rare coverage gap. We present NetFlow-DSR, a neuro-symbolic framework in which an LLM orchestrates the DSR pipeline and resolves device roles mainly from part-name families and library pin names, consulting specifications only for ambiguous parts. Pin directionality is read from the design library, and deterministic graph engines verify connectivity over the authoritative netlist. The pipeline detects diagnostic nets, canonicalizes renamed net fragments, and performs controller-seeded, power-aware breadth-first search over an admissibility graph that credits device-mediated monitoring. Each verdict carries an auditable trace card whose proof path is the witness. Across five production boards from an AI platform, covering 421 expert-graded signals, a three-stage ablation improves pooled F1 from 0.578 to 0.944. Because a monitored verdict is emitted only with a proof path, the verifier is sound by construction, and precision and specificity were 100% in the evaluated data. In a cross-model study on the system-controller module, precision remained 100% across three LLMs while recall tracked each model's device-semantic extraction. Precision therefore depends on the netlist-grounded verifier and correct device semantics rather than on any single LLM.
