# Backend-Aware Graph Learning for Denoising Outcome Distributions in Quantum Program Testing

- arXiv ID: `2607.23211v1`
- Authors: Ning Ma, Jun Dai, Heng Li
- Published: 2026-07-25
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.23211v1) | [pdf](https://arxiv.org/pdf/2607.23211v1)

## Abstract

Testing quantum programs on NISQ (Noisy Intermediate-Scale Quantum) backends is challenging because the noise disturbs outcome distributions and can affect pass/fail decisions. We present Q-BRIDGE, a graph learning-based approach that converts noisy observations into denoised distributions suitable for oracle-based verification. Q-BRIDGE uses a graph transformer architecture to encode a transpiled quantum circuit, capturing the characteristics of its gates and their connectivity; the physical backend information is encoded together with the logical structure of the circuit. An additional conditioning layer, based on FiLM (Feature-Wise Linear Modulation), takes the encoding as input and integrates noisy observations to produce denoised outcomes. We evaluate Q-BRIDGE on 23 IBM noise backends and 6 circuit families representative of practical workloads. In the first setting, we train a separate Q-BRIDGE model for each backend; in the second setting, we train a single general model shared across all backends. Across both settings, Q-BRIDGE outperforms the state-of-the-art baseline in noise mitigation by a large margin. In testing scenarios with noisy executions, Q-BRIDGE achieves 93.97%-94.90% precision and 82.50%-83.51% recall in detecting bug-induced test failures, significantly outperforming the state-of-the-art baseline. These results indicate that considering the graph structure of the transpiled circuits and the physical characteristics of specific quantum backends is a practical route to more reliable noise-aware quantum program testing.
