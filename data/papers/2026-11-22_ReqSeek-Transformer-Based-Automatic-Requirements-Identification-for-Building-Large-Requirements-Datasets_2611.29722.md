# ReqSeek: Transformer-Based Automatic Requirements Identification for Building Large Requirements Datasets

- arXiv ID: `2611.29722v1`
- Authors: Mohammad Kasra Habib,  Umm-e-Habiba, Daniel Graziotin, Stefan Wagner
- Published: 2026-11-22
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2611.29722v1) | [pdf](https://arxiv.org/pdf/2611.29722v1)

## Abstract

Large, diverse, and high-quality datasets are significant for advancing AI in requirements engineering, yet automated identification of requirements from Software Requirement Specifications (SRS) remains a challenge. Automatic Requirements Identification (ARI) methods demonstrate limited generalization to unseen documents across heterogeneous SRSs. This work presents ReqSeek, a transformer-based, domain-agnostic ARI model for recognizing ISO 29148-style requirements in SRS documents, supporting dataset construction. We curated the Automatic Requirements Identification Dataset (ARID), comprising 2,396 training instances from 23 heterogeneous SRSs, and fine-tuned four transformer architectures. RoBERTa was selected as the base model for ReqSeek and achieved 95% precision, recall, F1, and F0.89 on the held-out evaluation set. Exploratory human-model benchmarking showed performance comparable to humans while requiring substantially less prediction time than manual annotation. Post-hoc evaluation on out-of-domain (OoD) SRSs provided evidence of requirement identification beyond ARID. Robustness analysis demonstrated ReqSeek's insensitivity to minor linguistic variations while maintaining sensitivity to major ISO 29148-style violations. We applied ReqSeek to construct the Software Requirements Dataset (SwaRD), identifying 10,201 ISO 29148-style requirements from 231 industrial SRSs. SwaRD aligns with textual and semantic properties of human-curated datasets while exceeding them in scale and domain diversity. Our results suggest that transformer-based ARI can provide precise and generalizable requirements identification.
