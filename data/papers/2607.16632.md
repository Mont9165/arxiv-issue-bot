# CLOSER-Bench: Evaluating Budgeted Cross-Stage Design Closure for Hardware Agents

- arXiv ID: `2607.16632v1`
- Authors: Peilong Zhou, Zhirong Chen, Cangyuan Li, Haoyu Gao, Kaiyan Chang, Ziming Qu, Ying Wang
- Published: 2026-07-18
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.16632v1) | [pdf](https://arxiv.org/pdf/2607.16632v1)

## Abstract

Hardware engineering exposes coding agents to a form of long-horizon work that is difficult to capture with pass-at-k: progress is continuous, tool feedback is delayed and heterogeneous, and a backend failure may require revising RTL rather than tuning another physical-design parameter. Existing benchmarks measure RTL generation, repository repair, verification, PPA evolution, or physical implementation, but their different designs and oracles make it hard to determine where an agent succeeds or fails across abstraction boundaries. We introduce CLOSER-Bench, a controlled evaluation protocol for budgeted cross-stage design closure. For one design and one hidden objective, it pairs spec-to-RTL, RTL-to-GDS, and spec-to-GDS tasks, records every simulator, synthesis, STA, and place-and-route invocation, and measures final quality, anytime progress, tool cost, and cross-stage recovery. The benchmark is built on open-source Verilator, Yosys, OpenROAD, KLayout, Sky130, and the Harbor agent harness. A ten-task pilot spanning RTL repair, mutation-based verification, coverage, PPA optimization, design-space exploration, cross-model debugging, and security establishes the executable harness and exposes a sharp completion--closure gap: three agents solve a localized AXI repair task, while the matched verification-closure task separates a frontier agent from two otherwise successful baselines. We further validate a full RTL-to-GDS flow and construct a macro-based AXI/DMA streaming accelerator for the stage-paired evaluation. These results motivate treating hardware closure as a budgeted sequential decision problem rather than a collection of independent code generation tasks.
