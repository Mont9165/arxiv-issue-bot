# ALIAS: Evaluating Performance and Memorization in LLM-Written TLA+ Specifications

- arXiv ID: `2610.29767v1`
- Authors: Arslan Bisharat, Mujtaba Nazari, Khushboo Bhadauria, Brian Ortiz, Eric Spencer, Beatriz Santos, TaiNing Wang, George K. Thiruvathukal, Konstantin Laufer, Mohammed Abuhamad
- Published: 2026-10-21
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.29767v1) | [pdf](https://arxiv.org/pdf/2610.29767v1)

## Abstract

Memorization inflates the benchmark scores of large language models (LLMs), since a model can reproduce answers it saw in training. Researchers test for it with consistent identifier renaming (CIR), which gives every identifier in a task a new name, and treat a lower score on the renamed task as evidence of recall. We test this method on the Temporal Logic of Actions Plus (TLA+) language, whose model checker acts as an oracle by confirming whether a renamed task preserves the exact behaviors of the original. Across 111 TLA+-Bench tasks, renaming lowers the correctness of Claude Opus 4.8 from 28% to 18% and of GPT-5 from 9% to 7%. Most of this decrease comes from how the test grades, which requires exact names that most descriptions never state. Grading by behavior shrinks the decrease to about 3 percentage points for Opus 4.8 and to 0 for GPT-5. In two model families fine-tuned on disjoint halves of the tasks, renaming removes about half of the training gain in likelihood and costs 4.9 percentage points (Qwen) and 1.3 percentage points (Gemma) on unseen tasks. A lower score after renaming therefore mixes memorization, name-based grading, and the cost of new names.
