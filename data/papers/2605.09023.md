# Using Semantic Distance to Estimate Uncertainty in LLM-Based Code Generation

- arXiv ID: `2605.09023v1`
- Authors: Weilin He, Arindam Sharma, Cristina David
- Published: 2026-05-09
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.09023v1) | [pdf](https://arxiv.org/pdf/2605.09023v1)

## Abstract

LLMs show strong performance in code generation, but their outputs lack correctness guarantees. Sample-based uncertainty estimators address this by generating multiple candidate programs and measuring their disagreement. However, existing estimators make different design choices about how behaviours are identified, aggregated, referenced and compared, making them difficult to assess. We therefore first introduce a taxonomy that disentangles these choices and reveals a missing design point: semantic distance-aware uncertainty estimation, which measures not only whether sampled programs disagree, but how severely their execution behaviours differ. Across LiveCodeBench, MBPP, HumanEval-X and BigCodeBench, spanning Python, Java and C++, our metrics provide strong proxies for correctness, and consistently outperform state-of-the-art sample-based baselines across both closed-source models (GPT-3.5-Turbo, GPT-4o-mini, Gemini-2.5-Flash-Lite, Claude Opus 4.5) and an open-source model (DeepSeek-Coder-V2). The method is practical: it requires neither model internals nor LLM-as-judge calls, remains robust across models, languages, sampling temperatures and fuzzing settings, and reduces runtime by approximately 48-79% relative to existing baselines.
