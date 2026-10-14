# When Gradients Collide: Failure Modes of Multi-Objective Prompt Optimization for LLM Judges

- arXiv ID: `2605.26046v1`
- Authors: Parth Darshan, Abhishek Divekar
- Published: 2026-05-25
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.AI`, `cs.LG`, `cs.MA`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.26046v1) | [pdf](https://arxiv.org/pdf/2605.26046v1)

## Abstract

Customizing an LLM judge to a specific task or domain often involves optimizing its prompt across multiple evaluation criteria simultaneously. Textual gradient methods automate this for a single judge criterion, however they produce natural-language critiques, not numerical vectors. Thus, the conflict-resolution toolkit of multi-task learning (PCGrad, MGDA) doesn't apply to the multi-objective textual gradient setting. We test five decomposition modes of textual gradient optimizers by varying how much cross-task information the loss, gradient and optimizer LLMs share. In 6 of 10 configurations, we observe that optimization never improves over the initial prompt. Gradient specificity drops by 59% (from 9.0 to 3.7) when the gradient LLM processes multiple criteria jointly. Separately, we observe that naively combining per-task instructions into a single prompt degrades Spearman's rho by -5.3%. These results identify two separable failure modes: optimization-time gradient dilution and inference-time instruction interference, which together constrain the design space for multi-objective judge customization using textual feedback.
