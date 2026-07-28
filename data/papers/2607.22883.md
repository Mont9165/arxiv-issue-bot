# Evaluating and Mitigating the Misguidance Effect of Buggy Code in LLM-Generated Unit Tests

- arXiv ID: `2607.22883v1`
- Authors: Junda Zhao, Shurui Zhou, Eldan Cohen
- Published: 2026-07-24
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2607.22883v1) | [pdf](https://arxiv.org/pdf/2607.22883v1)

## Abstract

While Large Language Models (LLMs) show great promise for automating unit test generation, recent studies suggest that the quality of generated tests can be negatively impacted when models are prompted with buggy code. This paper presents a new metric to quantitatively measure the "misguidance effect," a phenomenon where buggy code steers LLMs toward generating tests that validate its erroneous behavior rather than expose it. Our analysis reveals that prompting LLMs with buggy code has a severe, twofold impact: it significantly increases "misguided tests" that assert incorrect behavior while simultaneously suppressing the generation of effective, bug-finding tests. We further corroborate this effect from a model-internal perspective, showing that buggy code skews LLMs' preference toward tests that assert the same erroneous behavior. To counter this, we introduce and validate a specification-based unit test generation paradigm that replaces the code under test in the prompt with an LLM-generated specification docstring. Our results show that this paradigm effectively reduces misguided tests while substantially increasing effective tests, improves multi-round, feedback-driven test generation pipelines, and remains applicable to both buggy and bug-free code. Overall, these results suggest that specification-based prompting is a promising strategy for mitigating misguidance from buggy code in LLM-generated unit tests.
