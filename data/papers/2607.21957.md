# KaPilot: LLM-Assisted Generation of Kani Specifications for Unsafe Rust Verification

- arXiv ID: `2607.21957v1`
- Authors: Minghua Wang, Yuxi Ling, Mingzhi Gao, Yuwei Liu, Lin Huang
- Published: 2026-07-24
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2607.21957v1) | [pdf](https://arxiv.org/pdf/2607.21957v1)

## Abstract

Rust's ownership and type system provide strong memory safety guarantees, but unsafe code still presents memory safety risks. Formal verification is crucial for ensuring memory safety, but writing precise specifications for unsafe Rust is challenging and largely manual. Large language models (LLMs) have shown promise in generating formal specifications but are often code-centric, prone to inheriting implementation flaws, and lack systematic quality assessment.
  In this paper, we present KaPilot, a multi-agent framework for automatically generating specifications to verify unsafe Rust memory safety using Kani. The process begins with lightweight program analysis and proof harness generation. The SafetyReq agent extracts a concise, refined list of safety requirements from the target Rust function's documentation, which guides the SpecGenerate agent in producing initial specifications that specify memory safety concerns. Then, the specifications are iteratively refined through a generate-precheck-verify loop involving SpecGenerate, SpecPrecheck, and SpecVerify agents, which assess quality and feed errors back. By executing this loop multiple times, KaPilot generates a set of candidate specifications. Finally, the shuffle-and-implication strategy is applied to systematically determine the best specification from these candidates. We evaluated KaPilot on 54 unsafe Rust functions with ground truth and 70 without. KaPilot achieved 88.9% and 71.4% specification generation success, respectively, with 57.4% of generated specifications equivalent to or stronger than the ground truth. Compared with AutoSpec, KaPilot produces 14.8% more verifiable specifications and 25.9% more equivalent-or-better specifications.
