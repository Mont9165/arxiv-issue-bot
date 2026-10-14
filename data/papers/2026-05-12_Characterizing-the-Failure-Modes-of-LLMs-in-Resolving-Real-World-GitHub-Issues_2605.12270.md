# Characterizing the Failure Modes of LLMs in Resolving Real-World GitHub Issues

- arXiv ID: `2605.12270v1`
- Authors: Yanjie Jiang, Yian Huang, Guancheng Wang, Junjie Chen, Hui Liu, Lionel Briand
- Published: 2026-05-12
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.12270v1) | [pdf](https://arxiv.org/pdf/2605.12270v1)

## Abstract

Large Language Models (LLMs) are increasingly deployed to resolve real-world GitHub issues. However, despite their potential, the specific failure modes of these models in complex repair tasks remain poorly understood. To characterize how LLM behavior diverges from human developer practices, this paper evaluates three state-of-the-art models, i.e., Claude 4.5 Sonnet, Gemini 3 Pro, and GPT-5, on the SWE-bench Verified dataset. We conduct a rigorous manual analysis of the symptoms and root causes underlying 243 failed attempts across 900 total trials. Our investigation first yields a unified failure taxonomy encompassing five distinct stages of the repair pipeline, within which we categorize typical failure symptoms and their prevalence. Secondly, our findings reveal that for all evaluated LLMs, strategy formulation and logic synthesis constitutes the most error-prone stage, followed by problem understanding, whereas localization exhibits the lowest failure rate. This suggests that LLMs may excel at fault localization, a task traditionally regarded as one of the most formidable challenges in automated program repair. Furthermore, we observe that robustness and operational costs (particularly in failure scenarios) vary significantly across different models. Finally, we uncover the root causes of these failures and propose actionable strategies to mitigate them. A particularly notable finding is that existing evaluation harnesses occasionally misjudge correct patches due to superficial discrepancies or hidden constraints. Collectively, our insights may provide promising directions for enhancing the effectiveness and reliability of LLM-based issue resolution.
