# EvoRepair: Enhancing Vulnerability Repair Agents Through Experience-Based Self-Evolution

- arXiv ID: `2605.30105v1`
- Authors: Haichuan Hu, Guoqing Xie, Quanjun Zhang, Jiawei Liu, Shengcheng Yu, Chunrong Fang, Zhenyu Chen, Liang Xiao
- Published: 2026-05-28
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.30105v1) | [pdf](https://arxiv.org/pdf/2605.30105v1)

## Abstract

Large Language Models (LLMs) have shown promise for automated vulnerability repair (AVR), but they still face several limitations, including the lack of intra-vulnerability experience accumulation and the lack of cross-vulnerability experience reuse. As a result, LLMs may repeatedly make similar mistakes during iterative repair and underutilize valuable repair knowledge from historical vulnerabilities. To address these challenges, we propose EvoRepair, the first experience-based self-evolving AVR agent framework that enables LLMs to accumulate, refine, and leverage domain-specific knowledge across long-horizon vulnerability repairs. EvoRepair follows a cyclic learn-and-repair process that retrieves relevant past experiences to guide repair, extracts new experiences from repair trajectories, and updates an experience bank using quality-aware scoring. We evaluate EvoRepair against 12 representative vulnerability repair baselines on PATCHEVAL and SEC-bench using GPT-5-mini. Results show that EvoRepair achieves the best overall performance, reaching 93.47% on PATCHEVAL, 87.00% on SEC-bench, and 90.46% overall. In particular, EvoRepair outperforms latest LLM-based baseline LoopRepair by 39.56% and 33.50% on PATCHEVAL and SEC-bench, respectively, and surpasses IntentFix by 70.86% and 50.50%. Across both benchmarks, EvoRepair also exceeds the recent self-evolving agent Live-SWE-Agent by 6.98% overall. Additional transfer experiments on VUL4J further demonstrate the robustness of EvoRepair across models, programming languages, and datasets. These findings demonstrate that experience-based self-evolution substantially strengthens agentic AVR and goes beyond existing self-evolving techniques.
