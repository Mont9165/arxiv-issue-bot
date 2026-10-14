# How Well Do LLMs Generate Taxonomies in the SE Domain? A Multi-perspective Evaluation Framework

- arXiv ID: `2608.01592v1`
- Authors: Sota Nakashima, Yuta Ishimoto, Masanari Kondo, Tao Xiao, Yasutaka Kamei
- Published: 2026-08-03
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.01592v1) | [pdf](https://arxiv.org/pdf/2608.01592v1)

## Abstract

Taxonomies provide a shared conceptual framework for organizing heterogeneous observations in software engineering (SE) research. Manually constructing such taxonomies is labor-intensive and requires annotators with expertise in the SE domain. While advances in Large Language Models (LLMs) have led to the emergence of automated taxonomy generation methods outside the SE domain, their applicability to technically complex SE artifacts remains unclear. In this experience paper, we present the first comprehensive empirical evaluation of how state-of-the-art automated methods perform on SE artifacts through a multi-perspective evaluation framework, including taxonomy quality, alignment with taxonomies defined by human experts, reliability under independent annotation, and efficiency. To support this evaluation, we systematically collect seven SE papers with publicly available artifacts and human-defined taxonomies, and conduct experiments using two automated methods (TnT-LLM and CLIMB) with five state-of-the-art LLMs. Our evaluation reveals a clear trade-off: TnT-LLM constructs high-quality taxonomies comparable to human-defined ones but incurs substantially higher cost and runtime and tends to generate overly complex taxonomies, whereas CLIMB is 15--40$\times$ faster and 8--49$\times$ cheaper but tends to score lower on quality when technical inference beyond surface-level similarity is required. These findings suggest that TnT-LLM and CLIMB can be used in practical situations in the SE domain, while researchers should first assess the complexity of the generated taxonomies and their cost using a subset of the target data to decide whether to use automated methods or human experts. Our work represents a first step toward a systematic understanding of automated taxonomy generation in SE, offering actionable insights for future research and practice.
