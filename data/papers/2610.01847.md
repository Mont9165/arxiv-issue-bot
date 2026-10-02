# Detecting Inconsistencies in Model Specifications with LLM-as-Verifier Reasoning

- arXiv ID: `2610.01847v1`
- Authors: Zichen Xie, Mrigank Pawagi, Lize Shao, Yang Hu, Wenxi Wang
- Published: 2026-10-01
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2610.01847v1) | [pdf](https://arxiv.org/pdf/2610.01847v1)

## Abstract

Model specifications define how large language models (LLMs) should behave, guiding alignment training, inference-time behavior, and evaluation. Yet these specifications may themselves contain defects: two individually reasonable principles may prescribe incompatible behavior when applied to the same situation, leaving no response that satisfies both. Detecting such inconsistencies is challenging. Formalizing natural-language specifications risks losing subtle distinctions, while behavior-based testing cannot reliably distinguish specification defects from differences in model behavior. We introduce VeriSpec, the first approach to directly detect inconsistencies in model specifications by auditing the specification text itself. Our key insight is to preserve the specification in natural language while using an LLM as a verifier. VeriSpec extracts structured, context-aware rules, constructs a topic-guided graph to cluster behaviorally related rules at the same authority level, and applies LLM-as-verifier reasoning to detect inconsistencies. Applying VeriSpec to the OpenAI Model Spec, we extract 405 rules and manually validate five inconsistencies, all reported to its developers, who responded positively and have initiated internal discussions. Compared with five baselines, VeriSpec identifies the most validated inconsistencies, achieves the highest precision (38.5%), and incurs the lowest cost per validated inconsistency ($11.12). These results establish direct specification auditing as a practical complement to behavioral alignment evaluation, catching defects at the source before they shape any model. The code is available at https://github.com/HIPREL-Group/VeriSpec.
