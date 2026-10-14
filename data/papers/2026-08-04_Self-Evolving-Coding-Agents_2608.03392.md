# Self-Evolving Coding Agents

- arXiv ID: `2608.03392v1`
- Authors: Hao Zhou, Haichuan Hu, Ye Shang, Quanjun Zhang
- Published: 2026-08-04
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.03392v1) | [pdf](https://arxiv.org/pdf/2608.03392v1)

## Abstract

Large language models are increasingly embedded in software engineering workflows as coding agents that can inspect repositories, invoke tools, execute tests, debug failures, and generate patches. Yet most existing agents remain largely static after deployment, even though software development is a dynamic, feedback-rich process in which repositories evolve, dependencies change, tests fail, and repair attempts leave reusable experience. This tension has motivated a growing body of work on self-evolving coding agents, where the agent improves its future behavior by updating its framework, memory, skills, tools, models, or collaboration structures from prior coding interactions. In this survey, we provide a systematic synthesis of this emerging area. We first define self-evolving coding agents and distinguish them from conventional coding agents and general self-evolving agents. We then develop an object-centered taxonomy that characterizes what evolves in these systems, and complement it with two orthogonal perspectives: when evolution occurs and what software-specific evidence drives it. Across the literature, we find that executable feedback, repository-level context, and coding trajectories give software engineering a distinctive role as a natural domain for agent self-evolution, but also introduce new challenges in feedback reliability, benchmark overfitting, safety, maintainability, cost, and generalization. By organizing existing work around these dimensions, this survey aims to clarify the conceptual boundaries of self-evolving coding agents and provide a foundation for designing more adaptive, reliable, and software-aware agentic systems. The papers we collect can be found at https://github.com/zhouhao1024/Awesome-Self-Evolving-Coding-Agents.
