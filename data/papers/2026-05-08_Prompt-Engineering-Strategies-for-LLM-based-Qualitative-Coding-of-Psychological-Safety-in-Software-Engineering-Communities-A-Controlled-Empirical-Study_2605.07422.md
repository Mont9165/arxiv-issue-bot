# Prompt Engineering Strategies for LLM-based Qualitative Coding of Psychological Safety in Software Engineering Communities: A Controlled Empirical Study

- arXiv ID: `2605.07422v1`
- Authors: Moaath Alshaikh, Tasneem Alshaher, Ricardo Vieira, Beatriz Santana, Clelio Xavier, Jose Amancio, Glauco Carneiro, Julio Leite, Savio Freire, Manoel Mendonca
- Published: 2026-05-08
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.07422v1) | [pdf](https://arxiv.org/pdf/2605.07422v1)

## Abstract

Qualitative analysis plays a pivotal role in understanding the human and social aspects of software engineering. However, it remains a demanding process shaped by the subjective interpretation of individual researchers and sensitive to methodological choices such as prompt design. Recent advancements in Large Language Models (LLMs) offer promising opportunities to support this type of analysis, although their reliability in reproducing human qualitative reasoning under varying prompting conditions remains largely untested. This study presents a controlled empirical evaluation of three LLMs -- Claude Haiku, DeepSeek-Chat, and Gemini 2.5 Flash -- across two prompt engineering strategies (zero-shot and multi-shot closed coding), using Cohen's kappa as the primary agreement metric over ten independent runs per configuration. Results suggest that multi-shot prompting significantly improves agreement for Claude Haiku (Delta kappa = +0.034, Wilcoxon p = 0.004) but not for DeepSeek-Chat or Gemini 2.5 Flash. Intra-model stability varies substantially -- DeepSeek-Chat and Claude Haiku exhibit the lowest variance (SD approx. 0.017), while Gemini 2.5 Flash is the least stable (SD = 0.038). A systematic over-prediction of "Sharing Negative Feedback" is identified across all models (bias ratios up to 5.25x), alongside consistent under-prediction of "Expressing Concerns." Collectively, these findings provide empirical evidence for prompt engineering guidelines in LLM-assisted qualitative coding for software engineering research.
