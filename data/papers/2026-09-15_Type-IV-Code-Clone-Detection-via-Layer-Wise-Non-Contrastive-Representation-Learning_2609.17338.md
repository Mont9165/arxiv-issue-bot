# Type-IV Code Clone Detection via Layer-Wise Non-Contrastive Representation Learning

- arXiv ID: `2609.17338v1`
- Authors: Luciano Marchezan, Kevin Delcourt, Eugene Syriani, Houari Sahraoui
- Published: 2026-09-15
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2609.17338v1) | [pdf](https://arxiv.org/pdf/2609.17338v1)

## Abstract

Software clones are fragments of code that are similar or functionally equivalent to each other. They pose significant challenges for maintenance, refactoring, and bug detection. Detecting Type-IV clones, which are semantically equivalent but may differ syntactically, is particularly difficult for traditional token- or syntax-based methods. Recent machine learning approaches rely on contrastive learning, which requires careful negative sampling and can introduce bias. In this paper, we propose LWVIC4Code, a non-contrastive representation learning approach specifically designed for Type-IV clone detection. Building on the Variance-Invariance-Covariance Regularization (VICReg) framework and prior layer-wise VICReg training, LWVIC4Code introduces cross-layer consistency regularization and depth-dependent layer weighting to progressively refine semantic information across transformer layers, producing robust and discriminative code representations. We conduct an empirical study comparing LWVIC4Code against a contrastive learning baseline and zero-shot large language models on Python (Kamino) and multi-language (GPTCloneBench) datasets. Results show that LWVIC4Code achieves competitive or superior performance without negative samples, benefits from layer-wise supervision, and generalizes effectively from Python to other languages, particularly Java and C#. These results demonstrate that non-contrastive, layer-wise representation learning is a promising direction for robust semantic code clone detection.
