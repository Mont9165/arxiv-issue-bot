# On the Road to Personalized Code Intelligence: Portraiting and Assisting Developers Based on Their In-IDE Behaviors

- arXiv ID: `2605.29372v1`
- Authors: Yuhong Liu, Yunhe Su, Zhipeng Peng, Zhiwen Luo, Lin Shi, Zhi Jin, Li Zhang
- Published: 2026-05-28
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.29372v1) | [pdf](https://arxiv.org/pdf/2605.29372v1)

## Abstract

With the advent of large language models, research in automated software engineering has increasingly focused on leveraging these models to achieve a deeper semantic understanding of code or to engineer sophisticated agent-based processes. However, this research trajectory has largely overlooked a critical factor: the developers themselves. Programming is a deeply individualized activity; developers exhibit significant variation in their tool-chain preferences, domain-specific expertise, and problem-solving strategies. Consequently, the current paradigm of one-size-fits-all code intelligence systems struggles to accommodate the needs of individual developers. To address this gap, we introduce VirtualME, a novel IDE-embedded data infrastructure designed to model the developer by continuously capturing and interpreting their dynamic programming behaviors and preferences. VirtualME contains three components. (1) Log-level Behavior Extraction: it captures and extracts developers' log-level behaviors from IDE. (2) Task-level Behavior Recognition: it aggregates log-level behaviors into task-level behaviors via a multi-agent pipeline. (3) Developer-personality Measurement: it builds a rule engine to distill a four-dimensional developer persona: technology stack, ability, behavioral habits, and learning style. On top of VirtualME, we propose a solution for personalized repository-level knowledge Q&A by integrating the developer persona into the Q&A agent. We evaluated VirtualME by building a multi-repository benchmark with real-world developer trajectories, balancing correctness and personalization. Experimental results show that VirtualME-enhanced answers outperform generic baselines on five dimensions, yielding an average 33.80% improvement. Our results demonstrate that abundant, continuous developer-behavior data can pave the new way for adaptive and personalized code intelligence.
