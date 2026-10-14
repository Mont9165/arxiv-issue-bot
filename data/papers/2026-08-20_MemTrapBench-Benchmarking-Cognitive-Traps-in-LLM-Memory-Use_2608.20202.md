# MemTrapBench: Benchmarking Cognitive Traps in LLM Memory Use

- arXiv ID: `2608.20202v1`
- Authors: Mengru Wang, Haozhe Luo, Zhenqian Xu, Zhixiang Cui, Haoming Xu, Qu Yang, Jizhan Fang, Junfeng Fang, Ningyu Zhang
- Published: 2026-08-20
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.CL`, `cs.CY`, `cs.DB`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2608.20202v1) | [pdf](https://arxiv.org/pdf/2608.20202v1)

## Abstract

Memory has become a key component of large language models, enabling them to retain information and learn from long-term interactions. However, existing memory benchmarks mainly evaluate whether information is correctly extracted, stored, and retrieved, while largely overlooking how retrieved memories reshape model reasoning and affect performance on the current task. We identify memory-induced cognitive traps: even faithfully recorded and semantically relevant memories can distort model reasoning or beliefs and degrade current task performance. To systematically evaluate these failure modes, we introduce MemTrapBench, which covers two forms of cognitive traps: Reasoning Fixation and Belief Distortion. Experiments across two model families and five representative memory frameworks show that MemTrapBench is challenging: all evaluated memory strategies underperform the no-memory setting, with even the strongest methods suffering drops of more than 10%. To mitigate these cognitive traps, we propose AdaptiveMem, a simple yet effective inference-time method that instructs LLMs to avoid memory traps. AdaptiveMem mitigates cognitive traps on MemTrapBench while preserving or improving performance on standard memory benchmarks across diverse memory frameworks.
