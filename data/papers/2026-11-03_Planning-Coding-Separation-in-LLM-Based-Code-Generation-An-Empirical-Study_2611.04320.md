# Planning-Coding Separation in LLM-Based Code Generation: An Empirical Study

- arXiv ID: `2611.04320v1`
- Authors: Wentao Wang, Zeyu Sun, Ruwei Pan, Yueyi Xiao, Qingyuan Liang, Lu Zhang
- Published: 2026-11-03
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.04320v1) | [pdf](https://arxiv.org/pdf/2611.04320v1)

## Abstract

Planning has been identified as an important factor for improved code generation with Large Language Models (LLMs). However, the interaction between planning capability and coding capability remains largely underexplored, especially when the two capabilities are from different LLMs. In this paper, we conduct the first comprehensive empirical study of planning-coding interaction in LLM-based code generation, where planning and coding are assigned to different LLMs (i.e., planning-coding separation). Specifically, we explore different planner-coder combinations to investigate the effectiveness for coders to utilize planning information from various planners and the impact of further training of coders on planner-coder combinations. Our results demonstrate that almost all planner-coder combinations are as competitive as using the same LLM for planning and coding, and the combination of a stronger planner and a stronger coder typically achieves improved effectiveness. Furthermore, using a large model as the planner paired with a much smaller model as the coder can sometimes be as competitive as using the large model as both the planner and the coder, and further training of the coder can typically boost various planner-coder combinations. These findings provide empirical evidence that planning and coding can be separated to a considerable extent in LLM-based code generation, which may offer a more flexible way to construct code-generation systems.
