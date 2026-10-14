# FastContext: Training Efficient Repository Explorer for Coding Agents

- arXiv ID: `2606.14066v1`
- Authors: Shaoqiu Zhang, Maoquan Wang, Yuling Shi, Yuhang Wang, Xiaodong Gu, Yongqiang Yao, Rao Fu, Shengyu Fu
- Published: 2026-06-12
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.14066v1) | [pdf](https://arxiv.org/pdf/2606.14066v1)

## Abstract

Large Language Model (LLM) coding agents have achieved strong results on software engineering tasks, yet repository exploration remains a major bottleneck: locating relevant code consumes substantial token budget and pollutes the agent's context with irrelevant snippets. In most agents, the same model explores the repository and solves the task, leaving exploratory reads and searches in the solver's history. We present FastContext, a dedicated exploration subagent that separates repository exploration from solving. Invoked on demand, FastContext issues parallel tool calls and returns concise file paths and line ranges as focused context. FastContext is powered by specialized exploration models spanning 4B--30B parameters. We bootstrap them from strong reference-model trajectories and refine them with task-grounded rewards for broad first-turn search, multi-turn evidence gathering, and precise citation generation. Across SWE-bench Multilingual, SWE-bench Pro, and SWE-QA, integrating FastContext into Mini-SWE-Agent improves end-to-end resolution rates up to 5.5\% while reducing coding-agent token consumption up to 60\%, with marginal overhead. These results show that repository exploration can be separated from solving and handled effectively by specialized models. Code and data: https://github.com/microsoft/fastcontext
