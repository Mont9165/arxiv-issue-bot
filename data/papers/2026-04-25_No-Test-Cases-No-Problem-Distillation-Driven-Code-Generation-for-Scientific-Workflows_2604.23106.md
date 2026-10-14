# No Test Cases, No Problem: Distillation-Driven Code Generation for Scientific Workflows

- arXiv ID: `2604.23106v1`
- Authors: Siddeshwar Raghavan, Tanwi Mallick
- Published: 2026-04-25
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.MA`
- Links: [abs](http://arxiv.org/abs/2604.23106v1) | [pdf](https://arxiv.org/pdf/2604.23106v1)

## Abstract

Existing multi-agent Large Language Model (LLM) frameworks for code generation typically use execution feedback and improve iteratively using Input/Output (I/O) test cases. However, this does not work for scientific workflows, where I/O test cases do not exist, and generating them requires solving the very problem at hand. To address this, we introduce MOSAIC, a training-free multi-agent framework for scientific code generation without I/O supervision. Instead of execution feedback, MOSAIC employs a student-teacher knowledge distillation framework that grounds generation through domain-specific examples and structured problem decomposition. To further mitigate hallucinations across chained subproblems, we introduce a Consolidated Context Window (CCW) for maintaining consistent reasoning across agents. Experiments on the SciCode benchmark show that MOSAIC improves accuracy, executability, and numerical precision over existing approaches while relying on lightweight models.
