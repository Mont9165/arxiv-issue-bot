# EVOLVE: Efficient Learned Volume Compression with Variable-Rate Encoding on a Cross-Domain Database

- arXiv ID: `2607.18187v1`
- Authors: Kaiyuan Tang, Maizhe Yang, Chaoli Wang
- Published: 2026-07-20
- Primary category: `cs.GR`
- Categories: `cs.GR`, `cs.DB`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2607.18187v1) | [pdf](https://arxiv.org/pdf/2607.18187v1)

## Abstract

Large-scale scientific simulations generate volumetric data at rates that far outpace advances in storage and network bandwidth, making effective lossy compression increasingly critical. However, conventional compressors often struggle to preserve fine structural details at high compression ratios (CRs), and implicit neural representations (INRs) require costly per-volume optimization and produce models with fixed CRs. To respond, we present EVOLVE, an autoencoder (AE)-based volume-compression framework that targets high CRs for offline compression, with three key contributions. First, we construct a large-scale cross-domain database of 6,376 volumes from 21 scientific simulations, curated via perceptual hashing to ensure diversity, enabling the optimized model to extract features that generalize across volumes within the covered scientific simulation domains. Second, we reexamine the design space of AE-based compressors and incorporate several macro- and micro-designs into a vanilla AE to develop EVOLVE, which substantially improves the expressive power and compression capability. Third, we develop a learnable gain mechanism with a three-stage training strategy to enable variable-rate encoding, allowing a single model to support continuous CR adjustment at inference time. Experiments on multiple unseen scientific simulation datasets demonstrate that EVOLVE achieves substantially higher CRs than conventional compressors at comparable reconstruction quality, while delivering compression speeds that are orders of magnitude faster than INR-based methods, highlighting its promise as a strong alternative for compressing scientific data. The code, model weights, and results are available on our project page at https://evolve-vis.github.io.
