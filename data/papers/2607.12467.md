# Understanding before Naming! Enhancing LLM-based Method Name Prediction with Code Summarization

- arXiv ID: `2607.12467v1`
- Authors: Wei Liu, Weisong Sun, Tingting Xu, Hanwei Qian, Yi Zhao, Chunrong Fang, Xia Feng
- Published: 2026-07-14
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.12467v1) | [pdf](https://arxiv.org/pdf/2607.12467v1)

## Abstract

Method names are critical to software quality, affecting code comprehensibility, maintainability, and developer collaboration. However, manually designing meaningful method names is challenging. Method Name Prediction (MNP), which automatically generates method names from code snippets, has recently attracted attention. Although large language models (LLMs) show promising performance for MNP, two challenges remain. First, existing evaluations mainly rely on token similarity metrics, which often fail to reflect human judgments of semantic quality. Second, current LLM-based MNP methods usually generate names through direct code-to-name mapping, which differs from the human process of understanding functionality before naming. To address these challenges, we conduct empirical studies on LLM-based evaluation and MNP strategies. We compare 6 metric-based evaluators, 5 LLM-based evaluators, and 6 human evaluators. Results show that LLM-based evaluators, especially DeepSeek-based evaluators, are more consistent with human judgments than traditional metrics. We further compare direct generation and summarization-and-refinement strategies. Results indicate that summarization and refinement generally improve the semantic quality of generated names. Case studies reveal three limitations: inaccurate summaries, semantic misalignment, and close semantic scores. Based on these findings, we propose SMNP, an MNP approach combining MNP-oriented summarization and chain-of-thought enhanced refinement. Experiments on 5 LLMs and 2 datasets demonstrate the effectiveness and robustness of SMNP.
