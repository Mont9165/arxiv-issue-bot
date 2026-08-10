# PACE: Primitive-Aware Code Evolution for Automated Algorithm Design

- arXiv ID: `2608.07395v1`
- Authors: Zhuoliang Xie, Ruihao Zheng, Xiang Xu, Genghui Li, Zhengkun Wang
- Published: 2026-08-07
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2608.07395v1) | [pdf](https://arxiv.org/pdf/2608.07395v1)

## Abstract

Large Language Model (LLM)-based automated algorithm design typically evolves algorithms as complete, indivisible programs. While this whole-program perspective simplifies the search space, it fundamentally couples the useful local logic to its host program. Consequently, valuable code snippets vanish when the overall program is discarded, making it highly difficult to assess the contribution of individual algorithmic components.To address this, we propose Primitive-Aware Code Evolution (PACE), which decouples local logic from complete programs by representing it as persistent units called Executable Algorithmic Primitives (EAPs). To enable code-level transfer, PACE maintains a dynamic set of EAPs. Algorithm evolution is driven by primitive-aware operators that structurally guarantee the retention and cross-program transfer of these components. To evaluate them effectively, PACE leverages Thompson sampling based on parent-relative performance improvements, guiding primitive selection from the set without requiring extra evaluation datasets. Experiments on four tasks demonstrate that PACE effectively discovers competitive algorithms while structurally preserving valuable algorithmic components.
