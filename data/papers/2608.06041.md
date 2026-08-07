# LangChoiceBench: Measuring and Explaining Programming-Language Choice in LLMs

- arXiv ID: `2608.06041v1`
- Authors: Lukas Twist, Twm Stone, Helen Yannakoudakis, Jie M. Zhang
- Published: 2026-08-06
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2608.06041v1) | [pdf](https://arxiv.org/pdf/2608.06041v1)

## Abstract

Large language models (LLMs) have been shown to exhibit strong Python preferences when generating project-level code, but there is currently no systematic way to measure this behaviour across new models. To bridge this gap, we introduce LangChoiceBench, a project-level code-generation benchmark for measuring Python preference, recommendation-implementation consistency, and language diversity. LangChoiceBench covers 28 projects across seven software areas where Python is often a poor default. We evaluate 25 diverse LLMs and find that Python remains heavily over-selected, recommendation-implementation consistency is low, and smaller open-weight models generally show stronger Python preference and lower language diversity. We further analyse 9,826 reasoning traces and find that most Python choices are automatic or driven primarily by ease, rather than explicit consideration of project requirements. In a smaller but important set of cases, models fabricate contextual support for choosing Python - a failure mode we call phantom evidence - or produce code that contradicts the language selected in their own reasoning.
