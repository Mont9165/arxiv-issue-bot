# Probing Privacy Leaks in LLM-based Code Generation via Test Generation

- arXiv ID: `2605.15248v1`
- Authors: Yifei Ge, Zhenpeng Chen, Weisong Sun, Yuchen Chen, Chunrong Fang, Juan Zhai, Xiaofang Zhang, Xia Feng, Yang Liu, Zhenyu Chen
- Published: 2026-05-14
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2605.15248v1) | [pdf](https://arxiv.org/pdf/2605.15248v1)

## Abstract

The widespread availability of large-scale code datasets has fueled the rapid development of large language models (LLMs) for code-related tasks. These datasets may include sensitive personally identifiable information (PII), which can lead to privacy leakage when LLMs memorize and reproduce it. However, existing privacy-leakage detection methods rely on ad-hoc prompt construction (manually or automatically designed). Therefore, they do not adequately approximate the real-world contexts in which PII appears in code corpora, making it difficult to extract realistic privacy leakage. In this paper, we propose a pipeline that simulates practical privacy-related code generation scenarios and adopts a test-driven strategy to elicit the memorized information from the generated test cases. We further introduce an automatically constructed privacy feature library that replaces manual prompt engineering by providing realistic templates and examples to guide test case generation. Large-scale experiments on 5 widely used LLMs show that our pipeline exposes more confirmed privacy leakage, achieving a 2.56 times increase in detected leakage compared to existing baselines.
