# SymLift: Neural Semantic Lifting for Compile-Free Vulnerability Detection in Context-Incomplete Code Fragments

- arXiv ID: `2610.34431v1`
- Authors: Xiarun Chen, Jiaxing Xu, Bozhi Wu, Chenhui Cui, Chunrong Fang, Weiping Wen, Tao Li, Rubing Huang, Tsong Yueh Chen
- Published: 2026-10-25
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2610.34431v1) | [pdf](https://arxiv.org/pdf/2610.34431v1)

## Abstract

Missing project context can prevent build-dependent analyzers from constructing program relations required for vulnerability detection, while neural predictions alone do not establish auditable derivations. We present SymLift, a compile-free framework centered on Vulnerability-Oriented Neural Semantic Lifting for context-incomplete code fragments. A fine-tuned large language model reconstructs vulnerability-relevant control-flow, data-flow, memory, and resource relations in a constrained LLVM-like intermediate representation (IR), without reconstructing the full project context or directly predicting vulnerability labels. A deterministic parser validates the IR and maps its supported operations and relations into normalized evidence facts. Explicit Datalog rules derive findings with supporting facts and derivation traces, ensuring deterministic reasoning for fixed facts and rules. We evaluate SymLift on FormAI, Juliet, and MegaVul. Reducing complete Juliet programs to function-level fragments lowers Clang compilation success from 100% to 12.00%, whereas SymLift's analysis completion rate decreases by only 1.17 percentage points. After task-specific fine-tuning, the lifter achieves a control-flow intersection over union (IoU) of 96.85% on FormAI. SymLift-Qwen-7B achieves a Target-F1 of 94.41% on FormAI and, across six vulnerability families on MegaVul, a micro-averaged precision of 98.24% and a micro-averaged Target-F1 of 91.66%. These results support accurate and auditable detection in the evaluated context-incomplete settings, even with partial program relations.
