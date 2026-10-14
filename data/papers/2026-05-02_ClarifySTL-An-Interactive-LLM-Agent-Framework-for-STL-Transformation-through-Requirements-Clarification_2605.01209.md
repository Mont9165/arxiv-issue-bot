# ClarifySTL: An Interactive LLM Agent Framework for STL Transformation through Requirements Clarification

- arXiv ID: `2605.01209v1`
- Authors: Yue Fang, Zhi Jin, Jie An, Hongshen Chen, Xiaohong Chen, Naijun Zhan
- Published: 2026-05-02
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.FL`
- Links: [abs](http://arxiv.org/abs/2605.01209v1) | [pdf](https://arxiv.org/pdf/2605.01209v1)

## Abstract

Signal Temporal Logic (STL) is a formal language for specifying real-time behaviors of cyber-physical systems (CPS). Automatically transforming natural language requirements into STL specifications has received growing attention. Recent efforts leveraging large language models (LLMs) have demonstrated impressive performance, but some natural language requirements in practice contain vague or ambiguous information, which remains challenging for LLMs to handle. To address these challenges, we propose ClarifySTL, an interactive LLM-agent framework that enhances STL transformation through requirements clarification. ClarifySTL first detects vague expressions that indicate underspecified information in a requirement. If any vagueness is detected, it generates targeted clarification queries to guide users in supplementing the requirement until all necessary details are provided. Subsequently, if ClarifySTL detects ambiguities, it formulates focused ambiguity clarification queries and updates the requirements based on user feedback until all ambiguities are resolved. Finally, the requirements with vagueness and ambiguity clarified are transformed into STL specifications using LLMs. This interactive framework ensures that the resulting STL formulas faithfully capture user intent while reducing the burden on the user. We evaluate ClarifySTL on the representative benchmarks DeepSTL and STL-DivEn, as well as our newly introduced AmbiEval benchmark, which is specifically designed to assess the performance of the agents in handling vagueness and ambiguity, including both detection and query generation. The experimental results show that ClarifySTL is effective.
