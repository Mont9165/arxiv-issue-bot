# Bug-Report-Driven Fault Localization: Industrial Benchmarking and Lesson Learned at ABB Robotics

- arXiv ID: `2604.25700v1`
- Authors: Pernilla Hall, Anton Ununger, Riccardo Rubei, Alessio Bucaioni
- Published: 2026-04-28
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2604.25700v1) | [pdf](https://arxiv.org/pdf/2604.25700v1)

## Abstract

Software quality assurance remains a major challenge in industrial environments, where large-scale and long-lived systems inevitably accumulate defects. Identifying the location of a fault is often time-consuming and costly, particularly during maintenance phases when developers must rely primarily on textual bug reports rather than complete runtime or code-level context. In this study, we investigated if artificial intelligence can support fault localization using only the natural-language content of bug reports. By relying only on textual information, our approach requires no access to source code, execution traces, or static analysis artifacts, making it directly deployable within existing industrial maintenance workflows. We framed fault localization as a supervised text classification problem and evaluated three traditional machine learning models (Logistic Regression, Support Vector Machine, and Random Forest) and two fine-tuned transformer-based language models (RoBERTa-Base and Distil-RoBERTa). Our evaluation used proprietary data from ABB Robotics in Sweden, comprising five years of resolved industrial bug reports, each linked to its verified code fix. This setting allowed us to assess model effectiveness under realistic industrial constraints.
  Our results showed that traditional models using term frequency-inverse document features consistently outperformed the fine-tuned language models on this dataset, while data augmentation improved Random Forest performance. These findings challenge the assumption that transformer-based models universally outperform classical approaches in industrial contexts with domain-specific data. We demonstrated that historical bug reports can be systematically used for text-based, artificial intelligence-assisted fault localization, providing a scalable, low-cost, and empirically grounded complement to common debugging practices in industry.
