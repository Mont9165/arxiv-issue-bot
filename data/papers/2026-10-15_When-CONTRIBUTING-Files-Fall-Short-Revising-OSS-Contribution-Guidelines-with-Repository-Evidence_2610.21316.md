# When CONTRIBUTING Files Fall Short: Revising OSS Contribution Guidelines with Repository Evidence

- arXiv ID: `2610.21316v1`
- Authors: Kai Zheng, XinGuo Zhou, Xin Tan
- Published: 2026-10-15
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.21316v1) | [pdf](https://arxiv.org/pdf/2610.21316v1)

## Abstract

Contribution guidelines help newcomers participate in open-source software projects, yet often contain incomplete or outdated information. Existing studies characterize newcomers' information needs and documentation gaps, but revising these guidelines requires recovering and validating project-specific knowledge from scattered sources. We present ContribAlign, a framework for automatically revising CONTRIBUTING files through category-guided evidence integration. A qualitative analysis yields a taxonomy of 30 fine-grained guidance types across six contribution categories. ContribAlign uses a classifier to diagnose coverage of the six categories in the original guidance, then uses the taxonomy to collect and organize project-specific evidence. It filters detected conflicts and uses a large language model to generate category-level revisions. The classifier achieves a weighted F1 score of 0.764, improving on the existing classifier by 0.156, while the verifier detects factual conflicts with 97.3% precision and 91.5% estimated recall. Human evaluation shows that ContribAlign achieves the highest overall quality among the original guidelines and three baselines, with significant improvements in usefulness, beginner-friendliness, and completeness. These results suggest that ContribAlign can help maintain more accurate and useful contribution guidelines.
