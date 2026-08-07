# LiveEvalBench: Toward Open-World Evaluation for Web Generation

- arXiv ID: `2608.03689v1`
- Authors: Yiyao Wang, Zhen Wen, Yinghao Tang, Yixiao Fu, Lin Yuan, Xiaolau Zhang, Jun Zhou, Wei Chen
- Published: 2026-08-04
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.03689v1) | [pdf](https://arxiv.org/pdf/2608.03689v1)

## Abstract

Large language models are increasingly capable of synthesizing executable frontend projects, yet existing benchmarks still treat web generation as a static evaluation problem. We argue that frontend artifacts demand a different paradigm: they are interactive rather than static, admit diverse yet equally valid implementations, and evolve faster than rigid pipelines can accommodate. To address these gaps, we present LiveEvalBench, an automated framework that reformulates web-generation evaluation as an agentic, adaptive, and extensible process. LiveEvalBench instantiates evaluation as a collaborative review workflow, in which a Build Engineer, a Code Engineer, and a UI Tester collectively gather evidence across the full lifecycle of a frontend project, from deployment and code inspection to browser-based interaction. To handle implementation diversity, an adaptive protocol couples shared rubrics for cross-model comparability with implementation-grounded criteria tailored to each artifact. The framework further supports incremental integration of new evaluator roles and assessment dimensions without pipeline redesign. Experiments across diverse real-world web-generation scenarios show that LiveEvalBench aligns closely with human expert judgment and provides fine-grained insights into frontier models' web generation capabilities. Code is available at https://github.com/wyysteelhead/LiveEvalBench
