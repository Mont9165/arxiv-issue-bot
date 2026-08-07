# An Empirical Study of Security Calibration in Large Language Models for Code

- arXiv ID: `2606.31159v1`
- Authors: Mohammed Latif Siddiq, Md. Nafiu Rahman, Joanna C. S. Santos
- Published: 2026-06-30
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2606.31159v1) | [pdf](https://arxiv.org/pdf/2606.31159v1)

## Abstract

Large Language Models (LLMs) are rapidly transforming software development, yet their use in security-critical contexts raises a key question: do models know when their generated code is insecure? This property, known as calibration, measures whether a model's confidence aligns with the true correctness of its outputs. We present the first large-scale empirical study of security calibration in LLM-generated code. We evaluate GPT-4o-mini, Gemini-2.0-Flash, and Qwen3-Coder-Next across multiple temperature settings on two complementary benchmarks: self-contained security tasks and multi-language repository-level contexts. Our results suggest that overconfidence is prevalent across the evaluated LLMs. Functional calibration is consistently worse than security calibration, suggesting that models estimate security outcomes more reliably than functional correctness, potentially because functional correctness depends on complex execution behavior. We also examine whether calibration-guided automated repair can help remediate vulnerabilities in LLM-generated code, finding only limited improvements while frequently introducing functional regressions. Moreover, we study different mitigation strategies for reducing False Trust, where models assign high confidence to vulnerable code. The results show that although architectural gating improves calibration on controlled benchmarks, calibration deteriorates in realistic repository-level settings, increasing the risk of high-confidence vulnerable outputs.
