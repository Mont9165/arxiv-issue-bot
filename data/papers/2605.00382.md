# Social Bias in LLM-Generated Code: Benchmark and Mitigation

- arXiv ID: `2605.00382v1`
- Authors: Fazle Rabbi, Lin Ling, Song Wang, Jinqiu Yang
- Published: 2026-05-01
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.SI`
- Links: [abs](http://arxiv.org/abs/2605.00382v1) | [pdf](https://arxiv.org/pdf/2605.00382v1)

## Abstract

Large Language Models (LLMs) are increasingly deployed to generate code for human-centered applications where demographic fairness is critical. However, existing evaluations focus almost exclusively on functional correctness, leaving social bias in LLM-generated code largely unexamined. Extending our prior work on Solar, we conduct a comprehensive empirical study using SocialBias-Bench, a benchmark of 343 real-world coding tasks spanning seven demographic dimensions. We evaluate four prominent LLMs and find severe bias across all models, with Code Bias Scores reaching up to 60.58%. We further show that standard prompt-level interventions, such as Chain-of-Thought reasoning and fairness persona assignment, inadvertently amplify bias rather than reduce it. We then investigate whether structured multi-agent software process frameworks can improve fairness, finding that structured pipelines reduce bias when early roles correctly scope what the code should and should not consider. However, adding explicit fairness instructions to all agent roles produces worse outcomes than providing none, suggesting that diffused responsibility goes unaddressed. To address these limitations, we propose the Fairness Monitor Agent (FMA), a modular component that plugs into any existing code generation pipeline without modifying it. FMA analyzes the task description to determine which attributes should be considered or restricted, then detects and corrects violations through an iterative review process, without requiring an executable test suite. Evaluated on all 343 tasks, FMA reduces bias by 65.1% compared to a developer agent alone and improves functional correctness from 75.80% to 83.97%, outperforming all other studied approaches.
