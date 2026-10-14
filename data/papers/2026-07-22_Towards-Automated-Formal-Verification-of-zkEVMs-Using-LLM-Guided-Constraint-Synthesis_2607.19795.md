# Towards Automated Formal Verification of zkEVMs Using LLM-Guided Constraint Synthesis

- arXiv ID: `2607.19795v1`
- Authors: Shichen Huang, Zhenghe Jiang, Yi Jiang, Ling-I Wu, Jingyang Li, Guoqiang Li
- Published: 2026-07-22
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.19795v1) | [pdf](https://arxiv.org/pdf/2607.19795v1)

## Abstract

Zero-Knowledge Ethereum Virtual Machines (zkEVMs) secure Ethereum rollups by generating zero-knowledge proofs that guarantee off-chain execution correctness. However, subtle implementation bugs (e.g., incorrect gas accounting) can lead to valid proofs certifying semantically faulty states, thereby silently defeating cryptographic guarantees. Formal verification via SMT solvers can prevent this, but is bottlenecked by specification: current zkEVM development practice lacks automated methods to translate Rust opcode handlers into verification models. Current practices rely on unsustainable manual specifications, while LLM-based approaches suffer from hallucination and lack formal guarantees. To address this, we propose VeriSynth, a framework that synthesizes executable Python/Z3 verification models from Rust zkEVM code. VeriSynth enforces a hybrid paradigm: an LLM acts strictly as a formalization frontend to translate code into symbolic constraints, while an SMT solver serves as the correctness arbiter. To handle complex multi-component state transitions, VeriSynth integrates semantic decomposition, retrieval-grounded prompting, and verification-guided auto-repair into a closed-loop pipeline. We evaluate VeriSynth on the first source-level zkEVM verification benchmark, encompassing both correct and faulty opcode implementations. VeriSynth achieves a bug detection rate of over 90%, substantially outperforming direct and conversational LLM baselines, as well as a production-grade handwritten mutation-testing suite. Ablation studies confirm that each pipeline component is critical to the framework's overall effectiveness.
