# Real-World Perturbation Testing of Autonomous Driving Systems

- arXiv ID: `2607.04953v1`
- Authors: Stefano Carlo Lambertenghi, Matthias Weil, Andrea Stocco
- Published: 2026-07-06
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.RO`
- Links: [abs](http://arxiv.org/abs/2607.04953v1) | [pdf](https://arxiv.org/pdf/2607.04953v1)

## Abstract

Autonomous Driving Systems (ADS) must operate reliably under diverse conditions, yet representative data for rare or adverse scenarios is difficult to obtain. Perturbation-based testing is widely used to assess robustness, but most studies focus on offline datasets or simulation, leaving open questions about how such results translate to real-world driving. We present a large-scale study of 72 camera and LiDAR perturbations, evaluated across three testing modalities: offline model-level analysis, hardware-in-the-loop execution, and closed-loop system-level testing on a full-scale autonomous vehicle. The study covers both an end-to-end vision-based driving model and a modular LiDAR-based perception and planning stack. Our results reveal a clear gap between testing levels. For camera-based systems, perturbations with limited offline impact can still induce unstable control and failures in real-world driving. For LiDAR-based systems, degradation is more consistent at the perception level but weakly predictive of system-level failures. Across both modalities, model-level metrics alone are insufficient to identify the most harmful perturbations. We further show that real-time feasibility is a key constraint in real-world testing, and that robustness observations obtained from recorded data do not consistently transfer to closed-loop behavior on a physical vehicle, highlighting the importance of complementary real-world, system-level evaluation.
