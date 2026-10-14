# Fail-Aware and Explainable Test Oracle Prediction

- arXiv ID: `2607.11342v1`
- Authors: Yue Zhao, Binish Tanveer, Jelena Zdravkovic
- Published: 2026-07-13
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.11342v1) | [pdf](https://arxiv.org/pdf/2607.11342v1)

## Abstract

Despite their central role in fault detection, test oracles remain challenging to construct effectively. Recent learning based methods address this challenge by automatically generating test assertions, yet even if syntactically correct, they are often ineffective in revealing bugs. Rather than generating assertions, this study explores a different approach by training a model to directly predict whether a given test prefix passes or fails. We present FOCAL, an emerging code LLM-based discriminative oracle predictor. It learns from labeled pairs of test prefixes and methods under test, employs losses that emphasize failing cases during training, and grounds its predictions in statement level behavioral evidence. Compared with the baseline method SEER, we substantially improve performance on failing cases for unseen projects and provide richer explanations. A preliminary evaluation on fault-detection benchmarks and automated test-generation artifacts shows that our approach is highly accurate within its training distribution and substantially improves failure detection on previously unseen projects where prior discriminative oracles collapse. Moreover, the highlighted statements are supported by behavioral explanation checks. These early results suggest that fail-aware discriminative oracle prediction can complement existing approaches such as fuzzing, search-based testing, and LLM-based test generation. These techniques produce test prefixes at scale but often lack fault oriented oracles. In future work, FOCAL could take generated test prefixes and attach fault-aware predicted oracles to them, turning high-volume input generation into executable tests that are more likely to expose semantic failures.
