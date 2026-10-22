# FaultGene: LLM-Assisted Fault-Augmented Test Generation for Hardware-in-the-Loop Validation of Autonomous Driving Systems

- arXiv ID: `2610.29969v1`
- Authors: Chaoran Yuan, Fadi Kurdahi
- Published: 2026-10-21
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2610.29969v1) | [pdf](https://arxiv.org/pdf/2610.29969v1)

## Abstract

Reliable validation of autonomous driving cyber-physical systems requires testing not only nominal driving behavior but also failures arising from faults in sensing and embedded computation. Physical road testing provides realistic system behavior but is costly and difficult to reproduce, while simulation enables scalable evaluation but cannot fully capture hardware-dependent behavior and fault propagation. Hardware-in-the-loop (HIL) validation bridges this gap by executing the driving stack on real embedded hardware within a simulated environment. However, preparing fault-augmented scenarios for HIL testing remains largely a manual process, limiting test coverage, scalability, and efficiency.
  We present FaultGene, an LLM-assisted framework for automated generation of executable fault-augmented tests for HIL fault-resilience validation. Given a baseline Scenic/CARLA scenario and a structured fault specification, FaultGene generates a fault-augmented test case that captures the effects of HIL-level fault injection. During offline refinement, semantic-consistency checks and execution-level feedback are used to correct candidates that fail to preserve the intended scenario context or produce the desired fault-induced degradation, and to construct high-quality supervision for fine-tuning. The resulting generator then produces fault-augmented tests directly at deployment time without requiring manually engineered reference executions or repeated refinement loops.
