# A Jagged Frontier: Evaluating Robustness of Code Agents to Semantics-Preserving Transformations

- arXiv ID: `2608.18389v1`
- Authors: Hasan Najib Mahmud, Shreya Gupta, Isha Chaudhary, Nathaniel Enis, Ravi Mangal, Gagandeep Singh, Corina Pasareanu
- Published: 2026-08-18
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.18389v1) | [pdf](https://arxiv.org/pdf/2608.18389v1)

## Abstract

AI code agents are increasingly deployed to resolve real software issues, yet their reliability under superficial code variations remains poorly understood. We evaluate whether coding agents that repair repository-level issues remain reliable when the surrounding codebase is rewritten into a semantically equivalent form. We introduce a random variant sampler that applies common semantics-preserving transformations (SPTs) - spanning control-flow rewrites, dead-code injection, and identifier renaming - to produce perturbed variants. We evaluate two agentic scaffolds (mini-SWE agent and OpenCode) each backed by one of four frontier models (Claude Opus 4.5, Kimi K2.5, MiniMax M2.5, and Qwen 3.6-27B) across instances drawn from SWE-bench Verified and SWE-bench Pro. For each instance, the agent is run multiple times on the unperturbed and perturbed variants, yielding paired resolve-rate estimates that isolate the perturbation effect from intrinsic stochasticity. We find small degradation in most configurations: up to 6.7 percentage points mean resolve-rate drop in the most affected configurations with statistically significant degradations in 6 of 16 configurations of model, scaffold, and dataset. Crucially, no single model ranking by robustness holds across scaffolds - Qwen is among the most robust under mini-SWE agent on SWE-bench Verified yet the most brittle under OpenCode - revealing a jagged robustness frontier. The simpler scaffold (mini-SWE agent) is more robust to perturbation. Our results demonstrate that even top frontier models are susceptible to semantics-preserving perturbations although the effect is not uniform, raising concerns about the deployment reliability of AI code agents in diverse real-world codebases.
