# Automated Multi-Line Bug Repair Using Model Checker Aided LLMs: A Case Study on RISC-V Processors

- arXiv ID: `2610.32597v1`
- Authors: Debleena Das, Chandan Kumar Jha, Muhammad Hassan, Rolf Drechsler, Ansuman Banerjee, Subhra K. Das, Amlan Chakrabarti
- Published: 2026-10-23
- Primary category: `cs.AR`
- Categories: `cs.AR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.32597v1) | [pdf](https://arxiv.org/pdf/2610.32597v1)

## Abstract

Functional verification of Register-Transfer Level(RTL) designs has become a critical bottleneck in modern semiconductor development, often consuming the majority of project resources. Debugging, in particular, remains an especially time-consuming task, requiring careful analysis of simulation traces or counterexamples. Recent work has explored applying Large Language Models (LLMs) to RTL debug and repair with great promise. However, the existing approaches typically are for single-line bugs, operate in open-loop, rely heavily on prompts or retrieval, lack scalability, and often produce incorrect fixes. In this paper, we propose a novel automated RTL bug repair methodology that combines LLMs, assertions, and a model checker to provide scalable, trustworthy semantic grounding and formal guarantees. Concretely, the methodology leverages failing assertions to guide the LLM in generating patches for multi-line bugs. Each candidate patch is formally verified using a model checker (JasperGold), ensuring only valid repairs are accepted. We evaluate the efficacy and scalability of our methodology on the BRISC-V RISC-V core using mutation testing, introducing several mutation types, and demonstrate that our methodology can repair up to 98% of single-line RTL bugs and 93% of the multi-line bugs. To the best of our knowledge, this is the first work to show automated, LLM-assisted RTL multi-line bug repair results on a complex RISC-V processor design in a scalable manner.
