# A Closed-Loop Control Architecture for Reliable Constraint Satisfaction in LLM Text Generation

- arXiv ID: `2609.19710v1`
- Authors: Quan Zhou, Shahbaz Siddeeq, Mika Saari, Pekka Abrahamsson
- Published: 2026-09-17
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.19710v1) | [pdf](https://arxiv.org/pdf/2609.19710v1)

## Abstract

Software systems increasingly embed a large language model in features that must satisfy a numeric output constraint, that is, a requirement expressible as a number or an interval and checkable by code, such as a target word count or a target readability grade band. Because such a model is non-deterministic, is configured through natural-language instructions rather than a typed interface, and satisfies a stated requirement only approximately, a single prompt neither reliably meets the target nor preserves the source content. This paper presents and evaluates a closed-loop control architecture for this problem. It has five stages: generate, evaluate, adjust, archive, and analyze. The model is called only to write and to edit text, while deterministic code compares a composite readability value against a target band, rejects any edit that drops source entities, numbers, or keywords, and makes every accept decision. Over 114 single-shot generation jobs and 240 closed-loop runs on four commercial models, single-shot prompting met the target in 21.1 to 31.6 percent of cases and the closed loop in 92.5 to 98.8 percent, within two edit rounds on average and at a recall-based fidelity of 0.92 to 0.93; the two models common to both settings show the same effect. Because the controller optimizes the value on which success is scored, the result establishes reproducible control over a declared, computable metric and not validated human difficulty. The transferable practice is to declare the acceptance condition as code, bound the model to local edits, and gate every edit on a content check.
