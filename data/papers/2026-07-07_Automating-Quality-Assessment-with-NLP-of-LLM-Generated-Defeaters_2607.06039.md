# Automating Quality Assessment with NLP of LLM-Generated Defeaters

- arXiv ID: `2607.06039v1`
- Authors: Tihomir Rohlinger, Daniel Ratiu, Stefan Wagner
- Published: 2026-07-07
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.06039v1) | [pdf](https://arxiv.org/pdf/2607.06039v1)

## Abstract

High-integrity systems, such as autonomous vehicle fleets and large-scale energy infrastructures, rely on structured assurance cases to justify safety claims. To remain valid under evolving operational conditions, such cases must be examined against potential challenges, known as defeaters. While large language models (LLMs) can support the scalable generation of candidate defeaters, assessing their quality remains largely manual and subjective process. This paper presents an automated approach for supporting the assessment of LLM-generated defeaters using natural language processing techniques. The method combines structural features from assurance case graphs with semantic embeddings and meta-classifiers trained on expert-assessed defeater annotations. We evaluate the approach through two case studies in the automotive and energy domains. The results show substantial human reviewer dissensus, with Cohen's kappa values below 0.442, highlighting the difficulty of consistent manual assessment. Against this background, the proposed classifiers achieve an average F1-score of 0.84 in validation and show improved alignment with individual expert ratings. The findings suggest that automated assessment can help reduce subjective variance and provide scalable decision support for assurance case review, while leaving final judgment to domain experts.
