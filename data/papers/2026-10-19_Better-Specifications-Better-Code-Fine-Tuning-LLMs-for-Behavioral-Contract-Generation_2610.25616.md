# Better Specifications, Better Code: Fine-Tuning LLMs for Behavioral Contract Generation

- arXiv ID: `2610.25616v1`
- Authors:  Brhane Team, Tiantian Yang, Nikta Akbarpour, Simone Bartucci, Francesco Calimeri, Song Wang
- Published: 2026-10-19
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.25616v1) | [pdf](https://arxiv.org/pdf/2610.25616v1)

## Abstract

Large language models (LLMs) demonstrate strong code-generation capabilities but often struggle with functional correctness due to implicit or ambiguous behavioral requirements. We present CG2, a contract-guided code generation framework that translates natural-language tasks into structured behavioral contracts specifying interfaces, preconditions, postconditions, and invariants. CG2 fine-tunes an LLM to generate these contracts and introduces an iterative semantic validation and repair process to identify and correct incomplete, inconsistent, or incorrect specifications before guiding an unchanged downstream code-generation model. We evaluate CG2 on 1,007 held-out tasks using five code LLMs: DeepSeek-Coder-V2-Lite-Instruct, Ministral-3-14B-Instruct-2512, Qwen2.5-Coder-14B-Instruct, Qwen2.5-Coder-32B-Instruct, and Qwen3.5-27B. Results show that CG2 consistently improves pass@1 over direct code generation by 1.49-3.27 percentage points (7.58%-22.45% relative improvement) and over contract guidance without fine-tuning by 1.19-2.38 percentage points (7.04%-14.65% relative improvement). Manual analysis further reveals that semantically correct contracts are associated with higher code-generation accuracy. These findings demonstrate that explicitly specifying and validating behavioral requirements can improve functional correctness without modifying downstream code-generation models.
