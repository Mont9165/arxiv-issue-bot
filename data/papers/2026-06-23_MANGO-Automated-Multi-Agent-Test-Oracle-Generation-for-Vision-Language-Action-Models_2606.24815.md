# MANGO: Automated Multi-Agent Test Oracle Generation for Vision-Language-Action Models

- arXiv ID: `2606.24815v1`
- Authors: Pablo Valle, Shaukat Ali, Aitor Arrieta, Lionel Briand
- Published: 2026-06-23
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.24815v1) | [pdf](https://arxiv.org/pdf/2606.24815v1)

## Abstract

Vision-Language-Action (VLA) models are emerging robotic control systems that integrate perception, language understanding, and action generation in a unified architecture. Existing testing approaches for VLA-enabled robots rely on manually constructed symbolic test oracles that determine task success from final environment states. These oracles are costly to construct, require domain expertise, and are often tightly coupled to specific tasks and environments, limiting scalability and reuse. Furthermore, they provide only end-state assessments of task outcomes, offering limited insight into intermediate behavior and fault localization. To address these limitations, we introduce MANGO, a multi-agent framework that automatically generates fine-grained oracles from natural-language descriptions of robotic tasks. MANGO first generates a reusable library of atomic tasks, then generates simulator-grounded oracle definitions for each atomic task, and finally produces executable fine-grained oracles by decomposing complex instructions into ordered sequences of atomic actions and corresponding oracles. The framework uses collaborative Generator, Assessor, and Judge agents that iteratively refine generated artifacts through structured feedback. We evaluate MANGO on the LIBERO_10 and RoboCasa Humanoid Tabletop benchmarks. Results show that MANGO generates executable, fine-grained oracles that detect a similar number of failures as symbolic oracles while accurately localizing them and providing richer diagnostic information. Through ablation studies, we further analyzed component contributions and the effect of initial task set, while preserving oracle quality. Overall, the results show the feasibility and effectiveness of test oracle generation for VLA-enabled robots testing.
