# TELLER: Non-intrusive Cross-Layer Root-Cause Analysis for LLM Inference

- arXiv ID: `2608.01975v1`
- Authors: Ruilin Xu, Junyi Li, Pengfei Chen, Zongxuan Xie
- Published: 2026-08-03
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`, `cs.LG`, `cs.PF`
- Links: [abs](http://arxiv.org/abs/2608.01975v1) | [pdf](https://arxiv.org/pdf/2608.01975v1)

## Abstract

Large language model (LLM) inference has evolved from an offline workload into a continuously operated software service, yet root-cause analysis remains difficult because a single request spans the inference engine, Python/C++ backend, host CUDA APIs, GPU kernels, and distributed communication. Existing profilers expose raw timelines, while log-based diagnosis often misses cross-layer execution semantics and request-level structure. We present TELLER, a non-intrusive Trace- and Log-aware LLM inference Root-cause analysis framework. TELLER first collects NVTX/CUPTI traces and service logs without modifying model binaries, then reconstructs per-request call-chain trees and aligns log lines with the corresponding execution steps. We introduce a dependency-aware causal-context slice that preserves parent-child structure, temporal order, and communication relations, and a Trace Pair Encoding (TPE) tokenizer that compresses such slices into compact structural token sequences with parent, depth, and duration attributes. On top of these representations, TELLER combines numeric candidate localization with a multimodal root-cause model that jointly predicts abnormal steps, localizes suspicious operators, and generates natural-language explanations. Experiments on multi-node GPU inference workloads show a clear compression-accuracy trade-off: a moderate TPE vocabulary reduces per-step trace length by more than 80% while achieving the best overall performance on both horizontal (cross-node communication) and vertical (within-node execution stack) views, whereas more aggressive compression substantially degrades diagnosis quality. Further analyses under low-fault priors, strengthened baselines, modality ablations, explanation-quality checks, and tracing overhead show that TELLER provides a practical triage and evidence-localization substrate for LLM inference RCA.
