# SpecSyn: LLM-based Synthesis and Refinement of Formal Specifications for Real-world Program Verification

- arXiv ID: `2604.21570v1`
- Authors: Lezhi Ma, Shangqing Liu, Yi Li, Qiong Wu, Han Wang, Lei Bu
- Published: 2026-04-23
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.21570v1) | [pdf](https://arxiv.org/pdf/2604.21570v1)

## Abstract

Program verification is a formal technique to rigorously ensure the correctness and fault-freeness of software systems. However, constructing comprehensive interprocedural specifications for full verification obligations is time-consuming and labor-intensive, giving rise to automated specification generation approaches. Despite the significant advancements in these approaches brought by Large Language Models (LLMs), existing LLM-empowered approaches still suffer from significant limitations: they lack effective strategies for handling sizable input programs, and are typically equipped with no mechanisms to evaluate and guarantee the strength of the generated specifications. The limitations impair their ability to extract precise specifications from real-world complicated programs to support the verification of target properties, thereby hindering the applicability of existing approaches in verification tasks on real-world programs. To remedy this gap, we propose SpecSyn, a novel LLM-based specification generation method. SpecSyn first decomposes the input program into individual segments, which are handled respectively by the subsequent iterative specification generation process. Innovatively, we incorporate into the process a specification refinement mechanism based on semantic-non-equivalent program mutations and variant discrimination, assessing and enhancing the semantic strength of the generated specifications. Extensive experiments show that SpecSyn maintains high precision over 90% and outstanding recall over 75%, significantly outperforming existing LLM-based approaches. In further evaluations, SpecSyn successfully handles 1071 out of 1365 target properties for open-source programs, proving its applicability on real-world program verification tasks.
