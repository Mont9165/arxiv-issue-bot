# AssumptionMiner: Extracting, Tracing, and Revising Implicit Assumptions in LLM Code Generation

- arXiv ID: `2607.22898v1`
- Authors: Jie "JW" Wu
- Published: 2026-07-24
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2607.22898v1) | [pdf](https://arxiv.org/pdf/2607.22898v1)

## Abstract

Large language models (LLMs) generate code from natural-language prompts, yet real-world prompts rarely provide complete specifications. When prompts leave input formats, error handling, or design decisions unspecified, LLMs fill these gaps with implicit assumptions that shape the generated code's behavior and correctness. Because these assumptions remain hidden, generated code may satisfy tests while violating developer intent. We present AssumptionMiner, a framework that makes implicit assumptions a first-class artifact of LLM-based code generation. In addition to code, AssumptionMiner produces an explicit assumption layer, a structured representation of inferred constraints and design decisions that developers can inspect, confirm, or revise. An AST-based dependency graph enables targeted regeneration of only the code affected by a revised assumption. We also introduce a benchmark of 180 ambiguous programming tasks with 676 annotated assumptions, including a human-verified subset for evaluating code localization. We evaluate assumption extraction, code localization, and assumption-guided regeneration. Across open-source LLMs, a confidence-weighted ensemble achieves an F1 score of 0.816 for assumption extraction, improving on the strongest offline baseline by 3.6x. On the human-verified localization benchmark, AST-guided localization identifies more precise code regions than keyword-based and whole-file baselines. During assumption revision, targeted regeneration modifies less code than non-targeted alternatives while exposing challenges in handling cascading edits. These results demonstrate that making assumptions explicit improves the transparency and controllability of LLM-based code generation.
