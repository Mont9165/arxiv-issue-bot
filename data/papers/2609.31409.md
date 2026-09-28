# Context-Aware Functional Modeling for Android Third-Party Library Detection

- arXiv ID: `2609.31409v1`
- Authors: Dihao Fan, Jian Zhang, Yasai Shi, Chuan Luo, Xudong Liu, Yang Liu, Chunming Hu, Xu Wang
- Published: 2026-09-25
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.31409v1) | [pdf](https://arxiv.org/pdf/2609.31409v1)

## Abstract

Third-party libraries (TPLs) are widely used in Android apps, but their reuse can introduce security risks and interfere with downstream program analyses. Existing Android TPL detection approaches face two key limitations: their hand-crafted features are fragile under aggressive code transformations, and their whole-library matching strategies are ineffective when apps retain only part of a TPL.
  In this paper, we propose LibFan, a learning-based Android TPL detection approach based on context-aware functional modeling. It realizes this modeling through two complementary components: context-aware contrastive learning at the method level and functional partitioning at the library level. At the method level, it learns semantic representations through contrastive training while incorporating outgoing call relationships and class-level context, improving robustness to obfuscation, shrinking, and optimization. At the library level, it partitions each TPL into functionally coherent units and determines library presence using the best-matching partition, thereby accommodating partial library reuse. To evaluate LibFan, we construct a new benchmark comprising 200 apps and 46 vulnerable TPLs, with each app compiled under four transformation configurations. Under the most challenging R8 full mode, LibFan achieves F1 scores of 81.3% at the library level and 47.6% at the version level, representing relative improvements of 64.9% and 35.6% over the state of the art, respectively.
