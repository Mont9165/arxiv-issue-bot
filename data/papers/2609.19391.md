# MAGS: Multi-agent Auto-formalization Guarantees Safety for Agentic Outputs

- arXiv ID: `2609.19391v1`
- Authors: Albert Wu, Nicholas Roberts, Tzu-Heng Huang, Haoran Lin, Gil Friedman, Sungjun Cho, Gabriel Orlanski, Frederic Sala
- Published: 2026-09-16
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.19391v1) | [pdf](https://arxiv.org/pdf/2609.19391v1)

## Abstract

LLM coding agents now generate complex programs at a scale that makes thorough human review increasingly difficult, raising the risk of safety and security failures. Common approaches, including fuzz testing, static analysis, and LLM-as-a-Verifier, can detect many failures but struggle to cover all possible edge cases. Formal verification addresses this by providing machine-checkable guarantees over specified properties, but traditionally demands substantial manual specification and proof engineering. We introduce a unified multi-agent framework, MAGS, that generates executable programs with formal safety guarantees, using Dafny as a verification-aware intermediate representation where safety properties can be mechanically checked. MAGS formalizes and freezes human-audited APIs and safety requirements, translates generated code into Dafny, repairs violations using verifier feedback, and compiles verified programs back into executable code. We evaluate MAGS on 100 CUDA kernels, 100 terminal scripts, and 20 robotic-arm tasks. Across all 220 examples, it achieves a 100% success rate in producing programs with non-trivial safety guarantees against frozen specifications. Independent safety and functional evaluations further show strong performance across all three domains, while revealing failures when the auto-formalized semantics do not fully capture the target behavior.
