# Well-Specified and Well-Tested? Assessing SWE-bench-Style Datasets with a Self-Evolving Agent

- arXiv ID: `2610.39417v1`
- Authors: Zhonghao Jiang, Xuyang Zheng, Yanfu Yan, Zhongxin Liu, Lingfeng Bao, Shuiguang Deng
- Published: 2026-10-29
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2610.39417v1) | [pdf](https://arxiv.org/pdf/2610.39417v1)

## Abstract

Large language models (LLMs) have shown strong performance on software engineering (SE) tasks, driving the need for high-quality datasets for reliable training and evaluation. SWE-bench-style datasets (SWE datasets) are widely used to evaluate LLM-based coding agents on real-world software issues, where task clarity and test coverage directly affect whether instances are solvable and verifiable. However, quality issues persist in existing SWE datasets, and manual annotation is costly and labor-intensive, motivating LLM-based annotation. Existing approaches typically rely on static, overly general rubrics, limiting their ability to handle diverse and nuanced scenarios and often yielding high false positive rates. In contrast, human annotators draw on accumulated experience to make context-aware judgments. Inspired by this, we propose ExLabel, an LLM-based, self-evolving, experience-guided assistant for task clarity and test coverage assessment in SWE datasets. ExLabel maintains an evolving experience bank that distills cross-instance knowledge into stable yet adaptive judgment criteria and reuses relevant experience to guide the assessment of new instances. For systematic evaluation, we construct SWE-TQ, a new benchmark spanning eight programming languages, by cleaning human annotations from SWE-bench and Multi-SWE-bench. Experiments with three backbone LLMs show that ExLabel achieves the best F1 across all settings, with relative improvements of 44.2%/49.9% and 24.0%/18.4% over the best baseline for task clarity and test coverage assessment on the Python/Multilingual subsets, respectively. Moreover, a coding model fine-tuned on SWE-rebench data filtered by ExLabel resolves 66.2% of issues on SWE-bench Verified, outperforming the model trained on data filtered by the best baseline by 14.5%.
