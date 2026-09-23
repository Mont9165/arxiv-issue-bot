# Confidence-Guided Cross-Modal Knowledge Transfer for Multimodal Anomaly Detection in Microservice Systems

- arXiv ID: `2609.25856v1`
- Authors: Peipeng Wang, Xiuguo Zhang, Lihua Zhang, Zhiying Cao, Jingchun Zhou, Zheng Li
- Published: 2026-09-22
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.25856v1) | [pdf](https://arxiv.org/pdf/2609.25856v1)

## Abstract

Accurate anomaly detection is essential for reliable and secure operations of microservice systems. While an increasing number of studies have shifted from unimodal modeling to multimodal interaction and fusion, effectively leveraging reliable cross-modal information remains challenging. The challenge primarily stems from two aspects. Firstly, different modalities are influenced by factors like load fluctuations, leading to dynamically changing reliability. Secondly, multimodal data exhibit heterogeneity in both structure and semantics. Therefore, we propose a confidence-guided Cross-Modal knowledge Transfer method for multimodal Anomaly Detection (CMT-AD). It jointly models metrics and logs within a unified deep clustering framework and estimates modality reliability through the soft clustering distributions, where clustering uncertainty is quantified into confidence scores. Guided by these confidence scores, the model actively analyzes the contributions of each modality in cross-modal interactions and supplements low-confidence modalities with knowledge from high-confidence ones. To further mitigate cross-modal heterogeneity, we introduce a gated intermediate modality and design structural and semantic consistency constraints that align the original modalities with the intermediate modality to preserve similarity structures and semantic distributions across modalities. Furthermore, intra-modal and cross-modal regularization terms are incorporated to enhance cluster compactness and mitigate negative transfer. We evaluated CMT-AD on three large-scale datasets, and the results demonstrate that CMT-AD outperforms state-of-the-art approaches and achieves an F1-score higher than 0.9.
