# Causal Discovery in the Era of Agents

- arXiv ID: `2606.23608v1`
- Authors: Yujia Zheng, Vishal Verma, Mantej Gill, Haoyue Dai, Peter Spirtes, Kun Zhang
- Published: 2026-06-22
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.LG`, `cs.SE`, `stat.AP`
- Links: [abs](http://arxiv.org/abs/2606.23608v1) | [pdf](https://arxiv.org/pdf/2606.23608v1)

## Abstract

Recent attempts to combine large language models (LLMs) with causal discovery ask models to infer pairwise directions, propose graph structures, or inject language-model outputs as priors and constraints. These approaches promise faster analysis, but they also obscure whether a causal evidence is supported by data and assumptions or by textual associations, prompt artifacts and hallucinated mechanisms. We argue for a different role for agents in causal discovery. Agents should inspect data, retrieve context, explain method assumptions and clarify graph outputs, but they should not supply edges, orientations, priors, constraints or causal conclusions. We propose the principle that agents assist the workflow, while causal claims remain grounded in data, explicit assumptions, formal algorithms, diagnostics and user or domain-expert decisions. We instantiate this principle in causal-learn+, an online platform that coordinates data analysis, preprocessing, method recommendation, expert-knowledge incorporation, formal discovery and interpretation around the algorithmic ecosystem of causal-learn. A case study on Big Five personality data illustrates agent-assisted pipeline of causal discovery without turning language-model unreliability into causal evidence. The platform is available at causallearn.com.
