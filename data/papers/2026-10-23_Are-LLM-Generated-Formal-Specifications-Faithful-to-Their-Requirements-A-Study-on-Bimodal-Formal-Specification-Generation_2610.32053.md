# Are LLM-Generated Formal Specifications Faithful to Their Requirements? A Study on Bimodal Formal Specification Generation

- arXiv ID: `2610.32053v1`
- Authors: Wenhan Wang, Shiming Chen, Zeyu Sun, Shenghua Feng
- Published: 2026-10-23
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2610.32053v1) | [pdf](https://arxiv.org/pdf/2610.32053v1)

## Abstract

Formal specification generation is a critical step towards formal verification and correctness assurance of software. Recently, large language models have been widely adopted in automatic generation of formal specifications. However, existing LLM-based specification generation approaches often assume that the input program is correct, which deviates from the real purpose of formal verification---to figure out whether the program meets its requirements when its correctness is unknown. Therefore, we conduct an empirical study of LLM-based specification generation under the bimodal setting: given both the natural language requirement and its corresponding code implementation, whose correctness is unknown. We construct a benchmark of 1,403 C programs and evaluate ACSL specification generation with Frama-C verification. Our study reaches several interesting findings: first, when the code implementation is correct, providing the natural language requirement does not further improve the pass rate of generated specifications. Second, when the code implementation is incorrect, LLM-based specification generation may erroneously pass verification by producing weak or implementation-misled specifications, and this cannot be fully alleviated by advanced prompting approaches. Compared with the non-formal HoarePrompt approach, LLM-generated formal specifications are less effective in predicting requirement-code consistency. Our study takes a first look at applying LLM-based formal specification generation to verifying program correctness against requirements, and points to requirement-faithful specification generation as a new direction for future LLM-based formal specification research.
