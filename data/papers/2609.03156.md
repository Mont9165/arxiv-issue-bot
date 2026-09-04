# Compound Prompt Constraints in LLM Code Generation: A Factorial Study of Format, Persona, and Urgency

- arXiv ID: `2609.03156v1`
- Authors: Shrenik Jadhav, Nickalsa LaPlaca, Caleb Stone, Ashok Raja, Omar Ochoa, Vidhyashree Nagaraju
- Published: 2026-09-02
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.03156v1) | [pdf](https://arxiv.org/pdf/2609.03156v1)

## Abstract

Large language models (LLMs) are increasingly used in software engineering pipelines for code generation, where production prompts often combine multiple constraints. This paper presents a full-factorial empirical study of how output formatting, persona assignment, and urgency framing jointly affect LLM code-generation reliability. We evaluate all 27 combinations in a controlled 3x3x3 design and decompose each compound condition into an additive prediction and a residual interaction term that captures super-additive degradation. The study uses all 164 HumanEval+ problems across five OpenAI models from the GPT-4o family, GPT-4.1 family, and o3-mini, yielding 22,140 greedy-decoding evaluations. A format-aware extraction pipeline separates formatting failures from reasoning failures, and significance is assessed with McNemar's test, odds ratios, and 95% confidence intervals.
  Results show that compound constraints can produce architecture-dependent degradation not predictable from single-factor experiments. The GPT-4o family exhibits consistent super-additive effects, with pass@1 reductions 3-12 percentage points beyond additive predictions; the largest interaction is -12.2 pp on GPT-4o-mini for JSON + expert persona + moderate urgency. JSON combinations generally produce larger interactions than XML. In contrast, the GPT-4.1 family is largely resistant, while o3-mini shows a qualitatively different pattern in which structured output constraints can improve performance. These findings show that vulnerability is architecture-dependent rather than size-dependent, that individually neutral or beneficial constraints can combine to cause substantial degradation, and that compound-prompt testing should be standard in reliability assessment for LLM-assisted engineering pipelines.
