# PreMaQ: Predicting Maintainability-Related Quality of LLM-Generated Code Before Generation

- arXiv ID: `2610.05858v1`
- Authors: Taiki Wakamatsu, Yuta Ishimoto, Masanari Kondo, Yasutaka Kamei
- Published: 2026-10-05
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.05858v1) | [pdf](https://arxiv.org/pdf/2610.05858v1)

## Abstract

As large language models (LLMs) become increasingly capable of code generation, adopting generated code in software development requires assessing not only its functional correctness but also its maintainability-related quality. If such quality could be estimated before generation, developers could avoid the cost of generating, reviewing, and discarding low-quality code. Although prior work has shown that the functional correctness of the LLM-generated code can be predicted in advance, it remains unclear whether maintainability-related quality is similarly predictable. We introduce Pre-Generation Maintainability-Related Quality Prediction (PreMaQ), which predicts the Code Smell Score (CSS) and Maintainability Index (MI) of generated code from the internal representations of LLMs before generation. Our evaluation covers four open-weight LLMs and four Python code generation benchmarks, comprising 2,695 tasks in total. Our results show that predicted CSS and MI consistently correlate with their observed values across all 16 model-benchmark combinations, achieving mean Spearman rank correlations of 0.57 and 0.65, respectively. When used for model selection, PreMaQ achieves 59.5% of the maintainability-related quality improvement attainable by an ideal maintainability-based selector over random selection on tasks for which multiple models generate functionally correct code. Combining predictions from PreMaQ and prompt embeddings increases this proportion to 60.7%, indicating that the two signals are complementary. These findings suggest that PreMaQ can be used to predict and improve the maintainability-related quality of LLM-generated code.
