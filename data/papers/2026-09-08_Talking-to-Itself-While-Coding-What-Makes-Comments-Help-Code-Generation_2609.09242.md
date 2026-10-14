# Talking to Itself While Coding: What Makes Comments Help Code Generation?

- arXiv ID: `2609.09242v1`
- Authors: Dangfeng Pan, Zhensu Sun, Cenyuan Zhang, David Lo, Xiaoning Du
- Published: 2026-09-08
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.09242v1) | [pdf](https://arxiv.org/pdf/2609.09242v1)

## Abstract

Large Language Models (LLMs) often generate natural-language comments while writing code, and these comments become part of the context used to generate the code that follows. However, it remains unclear which properties of comments affect code-generation performance. We study this question through observational analyses and controlled interventions. On LiveCodeBench, neither comment frequency nor broad comment intent reliably predicts pass@1. We then prefill weaker recipient models with comment blocks written by stronger source models, allowing us to separate comment surface form from the solution content they convey. Comments from source solutions that pass the tests raise recipient pass@1 by 17.2% on average. In contrast, comments describing failed solutions provide no reliable gain, while comments written for a different problem reduce pass@1 by 20.8%. Finally, across a wide range of models and prompt variants, most recipient models show no significant recovery of the external-comment gain, and the best case recovers only 24%. These results show that comments help code generation not merely because they are comments, but because they can provide correct solution content that prompting cannot reliably elicit.
