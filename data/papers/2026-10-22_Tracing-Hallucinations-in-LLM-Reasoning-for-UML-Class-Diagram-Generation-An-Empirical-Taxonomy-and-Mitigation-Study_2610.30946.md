# Tracing Hallucinations in LLM Reasoning for UML Class Diagram Generation: An Empirical Taxonomy and Mitigation Study

- arXiv ID: `2610.30946v1`
- Authors: Mojdeh Rahmanian, Foutse Khomh, Ashkan Sami, Yanchao Yu
- Published: 2026-10-22
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2610.30946v1) | [pdf](https://arxiv.org/pdf/2610.30946v1)

## Abstract

Large Language Models (LLMs) can generate UML class diagrams from natural language requirements, but hallucinations may compromise the correctness and completeness of the resulting diagrams. Existing evaluations mostly assess the final diagram, without examining the intermediate traces of reasoning-capable LLMs, which can reveal where these hallucinations arise. We develop an empirical taxonomy of eleven hallucination sub-types organised into three dimensions: Prompt Faithfulness (deviations between requirements and reasoning), Code Faithfulness (discrepancies between reasoning and generated PlantUML code), and Reasoning Quality (problems within the reasoning). The taxonomy was derived from 60 manually annotated DeepSeek-R1 traces, applied to 120 further DeepSeek-R1 traces through a dual-LLM annotation pipeline, and examined on 20 DeepSeek-V4-Pro traces. Code Faithfulness was the most frequent dimension for DeepSeek-R1 in both datasets, whereas Prompt Faithfulness dominated for DeepSeek-V4-Pro, suggesting model-dependent failure patterns. In the manually annotated traces, reasoning-trace length showed no significant monotonic association with hallucination frequency, whereas requirement complexity was negatively associated with it, particularly for Prompt Faithfulness errors. In a mitigation experiment on 13 Golden UML ModelSet cases with three Qwen3-based models, adding Prompt Faithfulness and Reasoning Quality constraints to the generation prompt raised the pooled mean F1 score by 4.0 percentage points, whereas a post-hoc Code Faithfulness review provided no consistent further benefit. Relationship modelling remained the lowest-scoring element throughout. These results suggest that localising hallucinations within the generation process can inform targeted, prompt-based mitigation. Whether these findings generalise beyond the DeepSeek and Qwen3 model families remains to be tested.
