# Retrieval Supersedes Scale: Efficient Log Level Prediction via Multiplex Socio-Technical Context

- arXiv ID: `2611.05901v1`
- Authors: Youssef Esseddiq Ouatiti, Mohammed Sayagh, Bram Adams, Ahmed E. Hassan
- Published: 2026-11-04
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2611.05901v1) | [pdf](https://arxiv.org/pdf/2611.05901v1)

## Abstract

Developers insert logging statements in source code to record its execution, and the resulting logs are essential for detecting and troubleshooting system anomalies. A key part of these statements is the log level (e.g., DEBUG, INFO, WARN, ERROR), which determines whether a message is recorded. Choosing it is a trade-off: levels set too low mask important information in production, while levels set too high create noisy logs and extra I/O and storage overhead. Recent work uses Large Language Models (LLMs) with In-Context Learning (ICL) to predict log levels, but typically augments the prompt with randomly sampled examples. We argue that this overlooks the socio-technical nature of logging, where conventions vary by component and development team. Off-the-shelf LLMs using random examples are reported to achieve median AUCs of only 0.56 to 0.76, leaving room for improvement without fine-tuning. In this paper, we propose a retrieval approach for LLM-powered log level prediction that prioritizes context relevance over random selection and basic similarity. Our method retrieves logging examples relevant along two socio-technical dimensions: (i) functionality (code performing similar operations) and (ii) ownership (code maintained by the same developers). Evaluating four LLMs across ten popular Java projects, we find that this retrieval improves AUC over random baselines by 0.07 (median), and combining both signals yields median AUCs of 0.83 to 0.97. Our ablation studies show that each signal improves on random retrieval, and that combining them outperforms the stronger of the two on all ten projects. Our results also significantly exceed state-of-the-art supervised predictors (e.g., DeepLV) by a median AUC of 0.12 to 0.19. Our findings highlight the importance of socio-technical signals such as code functionality and ownership for LLM-powered log level prediction.
