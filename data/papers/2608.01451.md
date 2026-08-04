# Doc2CI: A Multi-Service Study of CI Configuration Generation Using Large Language Models

- arXiv ID: `2608.01451v1`
- Authors: Taher A. Ghaleb
- Published: 2026-08-02
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.01451v1) | [pdf](https://arxiv.org/pdf/2608.01451v1)

## Abstract

Adopting Continuous Integration (CI) often requires writing YAML configurations that are error-prone and challenging to maintain. Despite increasing LLM use in software engineering, their ability to generate CI configurations from natural language across services and model families remains unclear. This paper presents a large empirical study on using LLMs to generate CI configurations. We introduce DOC2CI, a benchmark of 3,363 description-to-YAML pairs collected from the official documentation of four CI services, and evaluate 14 open-weight models from 7B-34B parameters together with GPT-4o and GPT-4.1, producing over 53,000 configurations. We assess both reference alignment and schema validity to determine whether the generated configurations are structurally valid. We further develop a failure taxonomy from a manual analysis of 385 configurations and examine why LLMs disagree. Across models and services, exact reference reproduction never exceeds 3.1%, and while 97% of outputs parse as YAML, only 71% satisfy service schemas. Larger models improve structural validity, but code specialization provides no consistent advantage over comparable general models. Model differences are driven largely by output completeness: for the same request, some models generate the expected fragment while others produce a full workflow. Finally, a training-free schema-guided repair method improves schema validity to 94%, while fine-tuning improves similarity to documentation but reduces standalone validity. This suggests that similarity and validity are distinct objectives for CI generation and motivate schema-aware evaluation and tooling for LLM-based configuration generation.
