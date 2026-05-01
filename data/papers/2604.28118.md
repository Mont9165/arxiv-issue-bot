# DEFault++: Automated Fault Detection, Categorization, and Diagnosis for Transformer Architectures

- arXiv ID: `2604.28118v1`
- Authors: Sigma Jahan, Saurabh Singh Rajput, Tushar Sharma, Mohammad Masudur Rahman
- Published: 2026-04-30
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2604.28118v1) | [pdf](https://arxiv.org/pdf/2604.28118v1)

## Abstract

Transformer models are widely deployed in critical AI applications, yet faults in their attention mechanisms, projections, and other internal components often degrade behavior silently without raising runtime errors. Existing fault diagnosis techniques often target generic deep neural networks and cannot identify which transformer component is responsible for an observed symptom. In this article, we present DEFault++, a hierarchical learning-based diagnostic technique that operates at three level of abstraction: it detects whether a fault is present, classifies it into one of 12 transformer-specific fault categories (covering both attention-internal mechanisms and surrounding architectural components), and identifies the underlying root cause from up to 45 mechanisms. To facilitate both training and evaluation, we construct DEFault-bench, a benchmark of 3,739 labeled instances obtained through systematic mutation testing. These instances are created across seven transformer models and nine downstream tasks using DEForm, a transformer-specific mutation technique we developed for this purpose. DEFault++ measures runtime behavior at the level of individual transformer components. It organizes these measurements through a Fault Propagation Graph (FPG) derived from the transformer architecture. It then produces an interpretable diagnosis using prototype matching combined with supervised contrastive learning. On DEFault-bench, DEFault++ exceeds an AUROC of 0.96 for detection and a Macro-F1 of 0.85 for both categorization and root-cause diagnosis on encoder and decoder architectures. In a developer study with 21 practitioners, the accuracy of choosing correct repair actions increased from 57.1% without support to 83.3% when using DEFault++.
