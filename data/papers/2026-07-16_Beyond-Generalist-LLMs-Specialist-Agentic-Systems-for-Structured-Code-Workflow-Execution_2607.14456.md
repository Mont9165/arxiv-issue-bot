# Beyond Generalist LLMs: Specialist Agentic Systems for Structured Code Workflow Execution

- arXiv ID: `2607.14456v1`
- Authors: Harris Borman, Herman Wandabwa, Fusun Yu, Sandeepa Kannangara, Justin Liu, Anna Leontjeva, Ritchie Ng
- Published: 2026-07-16
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.14456v1) | [pdf](https://arxiv.org/pdf/2607.14456v1)

## Abstract

Large Language Models (LLMs) have accelerated the adoption of software development agents, now widely available as Integrated Development Environment (IDE) extensions and standalone applications. While these agents are typically general-purpose, it remains unclear whether specialist agents justify their additional development effort. We investigate this question in the context of business process automation, focusing on the transformation of Business Process Model and Notation (BPMN) diagrams into executable agentic workflows. Since BPMN specifies explicit control-flow semantics, we focus on deterministic workflows in which a fixed process model and inputs uniquely determine the executed path. We introduce a specialist workflow for this task and compare it against generalist agents such as Roo and Cline. Our results show that the specialist solution produces agents that outperform generalist baselines by approximately 9-20 percentage points in tool-use exactness, 2-4x in penalty-adjusted latency, and 3x fewer tool-call errors, while reducing generation token cost by over 95% and eliminating repair iterations. We also find that generalist agents generate code inconsistently in both functionality and quality, limiting their suitability for industrial settings where reliability and maintainability are essential.
