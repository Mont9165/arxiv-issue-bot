# Better Understanding, Better Fixes? A Study of Hallucination in LLM-based Automated Program Repair

- arXiv ID: `2609.04909v1`
- Authors: Xuemeng Cai, Jiakun Liu, Linhan Yang, Wei Ma, Lingxiao Jiang
- Published: 2026-09-04
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.04909v1) | [pdf](https://arxiv.org/pdf/2609.04909v1)

## Abstract

Large language models (LLMs) have significantly advanced automated program repair (APR), yet existing evaluations remain largely result-centric and provide limited insight into hallucination during repair. In APR, hallucination may arise not only in final patches but also in the intermediate artifacts that guide patch generation. To address this gap, we perform a multi-layered analysis of hallucination throughout the APR process. Specifically, we characterize hallucination as the production of patches or intermediate artifacts that are not faithfully grounded in the available repair evidence. We examine repair hallucination in final patches and understanding hallucination in intermediate artifacts through three tasks, namely triggering testcase identification, line coverage prediction, and additional testcase generation.We then evaluate three representative LLMs on 832 Defects4J bugs through automatic evaluation and manual analysis. Our results show that both repair and understanding hallucinations remain prevalent. Across models and settings, only 21.0%-55.9% of generated patches pass the developer-written test suite. Moreover, although more accurate intermediate artifacts are generally associated with successful repairs, this relationship does not always hold. Manual analysis of 812 sampled repairs identifies repair hallucinations in 72.7% of cases, including patches that pass all available tests; incorrect causal localization and incorrect repair strategies account for 45.9% and 18.5% of these hallucinations, respectively. Meanwhile, models frequently misidentify triggering testcases, mispredict line coverage involving branching control flow, and generate additional testcases with missing bug-triggering conditions or incorrect expected behavior.
