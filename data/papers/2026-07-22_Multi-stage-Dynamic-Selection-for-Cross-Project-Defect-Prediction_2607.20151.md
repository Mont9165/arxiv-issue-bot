# Multi-stage Dynamic Selection for Cross-Project Defect Prediction

- arXiv ID: `2607.20151v1`
- Authors: Juscimara G. Avelino, Juscelino S. A. Junior, George D. C. Cavalcanti, Rafael M. O. Cruz
- Published: 2026-07-22
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2607.20151v1) | [pdf](https://arxiv.org/pdf/2607.20151v1)

## Abstract

Cross-Project Defect Prediction (CPDP) involves building models using data from external projects, called training projects, to predict modules from the target project. However, traditional CPDP methods suffer from the distribution shift between training and target projects that affects the model's performance. This paper proposes a novel CPDP framework that addresses this issue by proposing a two-stage multiple classifier system (MCS) selection scheme: one working at the project level and another at the module level. In the first stage, the framework evaluates multiple possible MCS configurations to find one that covers and generalizes well across multiple training projects. Consequently, the proposal is likely to obtain a diverse set of classifiers, each specialized in tackling software modules with distinct characteristics. The second selection stage operates at test time, selecting the most competent classifiers to predict each new module in the target project. Unlike previous approaches that apply the same classifiers to the entire target project, the proposed framework performs module-level model selection. This way, the system is more robust to changes in distributions between training and target projects because the selected set of classifiers is module-dependent. Our experimental results using 82 projects from four different CPDP benchmark datasets demonstrate that the proposed approach outperforms the state-of-the-art CPDP methods in most scenarios. The code, dataset, and further details about the proposed method are publicly available at https://github.com/jsaj/Multi_DES.
