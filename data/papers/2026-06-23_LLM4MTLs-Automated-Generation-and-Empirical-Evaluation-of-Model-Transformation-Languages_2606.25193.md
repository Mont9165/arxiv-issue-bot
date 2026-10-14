# LLM4MTLs: Automated Generation and Empirical Evaluation of Model Transformation Languages

- arXiv ID: `2606.25193v1`
- Authors: Bowen Jiang, Nathan Hagel, Haowei Cheng, Benedikt Jutz, Arne Lange, Weixing Zhang, Rahul Sharma, Ralf Reussner, Anne Koziolek
- Published: 2026-06-23
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.25193v1) | [pdf](https://arxiv.org/pdf/2606.25193v1)

## Abstract

Model transformation languages (MTLs) are domain-specific languages for transforming models conforming to a given metamodel into other models, including textual models such as source code. Developing correct model transformations is challenging, requiring both language-specific and domain knowledge, and motivating the use of large language models (LLMs) for MTL code generation. However, due to limited training data and executable examples, LLM-generated MTL code is often not syntactically valid or semantically usable out of the box. This paper presents LLM4MTLs, an automated workflow for constructing and comparing prompting strategies for LLM-generated MTL code, together with an evaluation suite and an empirical evaluation. The workflow systematically explores prompt constructions combining few-shot prompting, grammar prompting, and helper method inclusion, and evaluates them using syntactic and semantic metrics. We construct an evaluation suite spanning four MTLs (ATL, ETL, QVTo, and the Reactions language) with executable reference scripts and manually written test suites, and evaluate across three LLMs. We find that few-shot prompting consistently improves syntactic quality across all four MTLs while gains in semantic correctness are uneven and language-dependent. For ATL, Pass@1 remains unchanged across all strategies and models, indicating that few-shot prompting improves surface-level syntax more readily than deep transformation semantics. Grammar prompting stabilizes code generation when combined with few-shot examples, but in isolation it can be ineffective or even counterproductive for certain model-language combinations. Including helper methods as a complementary amplifier can also be beneficial. Finally, LLM choice influences syntactic correctness and similarity for certain MTLs, particularly ETL and QVTo, while its influence on semantic correctness remains limited.
