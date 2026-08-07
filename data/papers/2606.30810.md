# Towards Knowledge Alignment in Code LLMs: Contrastive Unlearning for Evolving APIs

- arXiv ID: `2606.30810v1`
- Authors: Huy Q. Tran, Dang H. Vu, Tuyen N. Dinh, Anh H. D. Nguyen, Anh N. H. Vu, Anh M. T. Bui, Phuong T. Nguyen
- Published: 2026-06-29
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.30810v1) | [pdf](https://arxiv.org/pdf/2606.30810v1)

## Abstract

Large Language Models (LLMs) have recently achieved strong performance in code generation. However, due to knowledge cut-off and the rapid evolution of software libraries, they often generate deprecated API usages that lead to unreliable and incompatible code. Existing fine-tuning methods lack selectivity when only a small portion of model knowledge requires modification. Recent model-level approaches, such as machine unlearning and model editing, offer a promising direction for modifying parametric knowledge. However, their use for deprecated API mitigation remains largely unexplored. Moreover, existing methods primarily suppress outdated APIs, but do not explicitly steer models toward correct replacements, often leading to mismatched or incomplete generations. To address this limitation, we developed CURE, a contrastive unlearning approach that shifts unlearning from purely suppressing outdated knowledge to explicitly promoting correct API replacements. Concretely, CURE jointly discourages deprecated APIs while encouraging their valid alternatives, enabling more reliable adaptation to evolving software libraries. The experiments on recent deprecated API benchmark dataset show that CURE not only reduces deprecated API usage but also improves correct API replacement, while preserving general code generation performance. CURE substantially outperforms two SOTA baselines with respect to different quality metrics. These findings highlight the importance of combining suppression with replacement when adapting LLMs to evolving software ecosystems.
