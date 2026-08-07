# Causal Disentanglement for Full-Reference Image Quality Assessment

- arXiv ID: `2604.21654v1`
- Authors: Zhen Zhang, Jielei Chu, Tian Zhang, Weide Liu, Fengmao Lv, Tianrui Li, Jun Cheng, Yuming Fang
- Published: 2026-04-23
- Primary category: `cs.CV`
- Categories: `cs.CV`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2604.21654v1) | [pdf](https://arxiv.org/pdf/2604.21654v1)

## Abstract

Existing deep network-based full-reference image quality assessment (FR-IQA) models typically work by performing pairwise comparisons of deep features from the reference and distorted images. In this paper, we approach this problem from a different perspective and propose a novel FR-IQA paradigm based on causal inference and decoupled representation learning. Unlike typical feature comparison-based FR-IQA models, our approach formulates degradation estimation as a causal disentanglement process guided by intervention on latent representations. We first decouple degradation and content representations by exploiting the content invariance between the reference and distorted images. Second, inspired by the human visual masking effect, we design a masking module to model the causal relationship between image content and degradation features, thereby extracting content-influenced degradation features from distorted images. Finally, quality scores are predicted from these degradation features using either supervised regression or label-free dimensionality reduction. Extensive experiments demonstrate that our method achieves highly competitive performance on standard IQA benchmarks across fully supervised, few-label, and label-free settings. Furthermore, we evaluate the approach on diverse non-standard natural image domains with scarce data, including underwater, radiographic, medical, neutron, and screen-content images. Benefiting from its ability to perform scenario-specific training and prediction without labeled IQA data, our method exhibits superior cross-domain generalization compared to existing training-free FR-IQA models.
