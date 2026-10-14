# Open-Source LLM-Driven Formal Verification: A Multi-Agent Pipeline for RTL Repair

- arXiv ID: `2607.28877v1`
- Authors: Ha Trung Tran
- Published: 2026-07-30
- Primary category: `cs.AR`
- Categories: `cs.AR`, `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.28877v1) | [pdf](https://arxiv.org/pdf/2607.28877v1)

## Abstract

Verification consumes the majority of modern chip design effort, yet the formal verification tools that provide mathematical guarantees of correctness remain expensive and restrictively licensed. While large language models (LLMs) have shown promise for hardware design, existing approaches to RTL repair validate their results through simulation - which exercises only a subset of inputs - or rely on commercial tools, and few combine formal proof with an entirely open-source toolchain. In this paper, we present a multi-agent pipeline that couples an LLM with an open-source formal backend (Yosys, SymbiYosys, and Z3) to repair RTL through counterexample-guided iteration: the framework generates formal properties, verifies the design, and feeds counterexamples back to the LLM until the design is proved correct by k-induction or an iteration budget is exhausted. Through an ALU case study, we show that the pipeline can detect and repair a real functional bug with a formal proof of correctness. Across a six-benchmark suite, one design is repaired reliably, and we characterize four distinct failure modes: bounded-cover vacuity, specification ambiguity, temporal-logic bugs, and multi-property pressure. We frame this work as a feasibility study with a detailed failure analysis, and additionally report a practical limitation of the Yosys bind directive relevant to the open-source formal verification community.
