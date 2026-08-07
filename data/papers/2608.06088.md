# IcFuzz: Fuzzing Isaac Sim with Semantic Stage Guidance and Multi-level Mutation

- arXiv ID: `2608.06088v1`
- Authors: Zhixiang Chen, Zhuangbin Chen, Ruoxi Jia, Zeqin Liao, Wei Li, Jinyang Liu, Zibin Zheng
- Published: 2026-08-06
- Primary category: `cs.RO`
- Categories: `cs.RO`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.06088v1) | [pdf](https://arxiv.org/pdf/2608.06088v1)

## Abstract

Robotics simulators serve as a foundational infrastructure for embodied AI, facilitating safe and scalable robotic system development. NVIDIA Isaac Sim has emerged as one of the most popular simulators, distinguished by its GPU-accelerated physics engine and photorealistic rendering, which enable high-fidelity modeling of complex environments. However, its inherent complexity inevitably introduces software bugs that can compromise simulation reliability. Existing fuzzing approaches struggle to test Isaac Sim effectively due to challenges of context-aware object semantics, hierarchical simulation control, and a vast simulation state space.
  In this paper, we propose IcFuzz, the first fuzzing approach for Isaac Sim. IcFuzz first performs an LLM-based semantic stage segmentation, decomposing simulation programs into structured stages that capture context-aware object semantics. Guided by this information, IcFuzz designs multi-level mutation operators to systematically exercise the simulator across hierarchical granularities. To efficiently navigate the vast simulation state space, IcFuzz employs a multi-armed bandit algorithm to adaptively schedule mutation operators. Experimental results show that IcFuzz outperforms the baselines in terms of both code coverage and bug detection. Specifically, IcFuzz achieves approximately 190\%--205\% of the code coverage of the baselines and detects an average of 3.7 unique crashes over three rounds of 12-hour tests, while no crashes are detected by the baselines. Moreover, IcFuzz has uncovered 11 bugs over approximately four months, 9 of which have been confirmed or fixed by the developers.
