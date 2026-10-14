# A Unified Model for Cross-Domain Clone Detection via Model Merging

- arXiv ID: `2608.04215v1`
- Authors: Palash R. Roy, Banani Roy, Kevin A. Schneider, Chanchal K. Roy
- Published: 2026-08-04
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2608.04215v1) | [pdf](https://arxiv.org/pdf/2608.04215v1)

## Abstract

The growing diversity of code clone types, from syntactic copies to cross-language semantic clones to AI-generated duplicates, has created a fragmentation crisis in clone detection. Current deep learning detectors are domain specialists that degrade significantly outside their training distribution, with F1 drops exceeding 70% across domains. Deploying multiple specialized models is impractical, yet training a single cross-domain detector requires simultaneous access to all training data. To address this, we investigate model merging, a family of post-hoc techniques that operate solely on trained checkpoints. We evaluate parameter merging with five task-vector methods, architecture merging via greedy layer stitching, and cross-tokenizer alignment across four code models, three benchmarks, and twelve configurations. Same-base TIES merging creates effective cross-domain detectors, validated across two model families and three random seeds, reaching 0.865 combined F1 on UniXcoder, 93% of multi-task performance without any training data at the merging step. WUDI achieves the highest in-distribution combined F1 at 0.899, but TIES generalizes better to unseen AI-generated clones, making it our recommended method. Cross-base merging yields only marginal and high-variance gains across all five methods, indicating that task vector compatibility through a shared pre-trained base is the binding factor for effective merging. Merged detectors also outperform zero-shot code LLMs on GPTCloneBench at lower inference cost and generalize up to 4x better than multi-task training to unseen AI-generated clones, suggesting a trade-off between in-domain performance and OOD robustness. This work provides one of the first systematic empirical studies of model merging for software engineering and a practical recipe for building cross-domain clone detectors.
