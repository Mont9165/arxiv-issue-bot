# Realistic Counterfactual Explanations via Denial Constraints

- arXiv ID: `2608.26335v1`
- Authors: Avia Asael, Nave Frost, Amir Gilad, Daniel Deutch
- Published: 2026-08-26
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.26335v1) | [pdf](https://arxiv.org/pdf/2608.26335v1)

## Abstract

In the realm of Explainable AI, classification results are often explained via counterfactuals (CFs for short), which are (ideally small) perturbations to an instance that lead to a change of classification label. Such CFs may serve as explanations for the prediction, pinpointing the features that were important. Existing explainability solutions typically aim at minimizing the distance of CFs from the original instance so that they are specific to it, and/or maximizing the diversity of CFs to cover multiple facets of the reasons underlying the prediction. In this paper, we note that in pursuing these aims, state-of-the-art explainability solutions may (and often do) yield counterfactual explanations that do not correspond to realistic instances. This limits their applicability and usefulness in practice. To remedy this, we combine ideas from Explainable AI with ideas from data management. Specifically, we capture realism of CFs via logical constraints that hold with respect to a dataset of examples (e.g., training set); the class of such constraints that we focus on is that of denial constraints, extensively studied in the context of relational databases. Algorithmically, we then combine explainable AI solutions to yield CFs, with ideas from data cleaning that we adapt to this unique setting, to transform CFs into realistic ones. Extensive experiments across four datasets validate that our solutions achieve realism with relatively minor compromise in terms of distance and diversity. They further validate that the dedicated optimizations that we have developed to speed up the search for CFs are indeed highly effective.
