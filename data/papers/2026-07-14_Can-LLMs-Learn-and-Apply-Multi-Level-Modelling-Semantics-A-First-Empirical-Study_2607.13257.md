# Can LLMs Learn and Apply Multi-Level Modelling Semantics? A First Empirical Study

- arXiv ID: `2607.13257v1`
- Authors: Yuhong Fu, Weixing Zhang, Bowen Jiang, Haowei Cheng, Karamjti Kaur, Markus Stumptner
- Published: 2026-07-14
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.13257v1) | [pdf](https://arxiv.org/pdf/2607.13257v1)

## Abstract

Industry 5.0 emphasises human-centric industrial system design, placing additional demands on modelling tools. Multi-level modelling (MLM) can directly represent three or more abstraction levels, but this comes at the cost of more complex semantic constraints that model correctness depends on. Large Language Models (LLMs) have been increasingly studied in model-driven engineering, but this evidence rests entirely on two-level modelling tasks, and whether it generalises to MLM, whose semantics differ in kind, remains untested. This paper presents the first empirical study of this question. We have three commercial LLMs (GPT-5.4, Claude Opus 4.6, and Gemini 3.1 Pro) generate multi-level models for the MULTI Warehouse Challenge in the SLICER language under six prompting strategies, yielding 90 generated models compared against a manually validated reference using fourteen metrics. Syntactic correctness is within reach, but semantic correctness is only partially achieved, with Instantiation/Specialisation Correctness ranging from 52% to 79%. Models reproduce content stated explicitly in the task text, but rarely complete structure and constraints the text implies without stating. Prompting strategies trade off precision against completeness, and self-checking functions mainly as a rule checker rather than reliably improving alignment with the reference design. Among the three LLMs, Claude shows the most balanced profile. These results clarify the boundaries of current LLM capability for MLM and inform the design of human-centred, AI-assisted modelling workflows for Industry 5.0.
