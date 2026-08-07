# LLM-Guided Runtime Parameter Optimization for Energy-Efficient Model Inference

- arXiv ID: `2604.27032v1`
- Authors: Katelyn Crumpacker, Dimitrios Nikolopoulos
- Published: 2026-04-29
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2604.27032v1) | [pdf](https://arxiv.org/pdf/2604.27032v1)

## Abstract

Large Language Models (LLMs) have become an integral part of many real-world workflows. However, LLMs consume a lot of energy, which becomes a large concern in the scale of the demand for these tools. As LLMs become integrated into different workflows, different applications have arisen to deal with the challenge of running inference for these tools. This raises another issue of choosing the runtime parameter values for these services in order to minimize the energy consumption. Oftentimes this requires deep knowledge of the application or traditional optimization methods that can take days to find optimal values. In this work, we created a human-in-the-loop flow with LLM-assisted runtime parameter optimization in order to solve this issue. With human-created, specific feedback prompting methods, chat-based LLMs can iteratively find energy-efficient inference parameters faster than traditional search methods. LLMs can also tailor their solutions to different hardware setups and easily take into account other system constraints. The enhanced prompt template was able to converge below the threshold at an average of 3.4 prompts compared to the baseline, which converged in an average of 5.2 prompts, and consistently achieved lower final energy per token. The enhanced prompt template also outperformed Sobol sampling in convergence speed.
