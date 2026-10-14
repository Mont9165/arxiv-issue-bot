# A Toolkit for Detecting Spurious Correlations in Speech Datasets

- arXiv ID: `2604.26676v1`
- Authors: Lara Gauder, Pablo Riera, Andrea Slachevsky, Gonzalo Forno, Adolfo M. García, Luciana Ferrer
- Published: 2026-04-29
- Primary category: `cs.SD`
- Categories: `cs.SD`, `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2604.26676v1) | [pdf](https://arxiv.org/pdf/2604.26676v1)

## Abstract

We introduce a toolkit for uncovering spurious correlations between recording characteristics and target class in speech datasets. Spurious correlations may arise due to heterogeneous recording conditions, a common scenario for health-related datasets. When present both in the training and test data, these correlations result in an overestimation of the system performance -- a dangerous situation, specially in high-stakes application where systems are required to satisfy minimum performance requirements. Our toolkit implements a diagnostic method based on the detection of the target class using only the non-speech regions in the audio. Better than chance performance at this task indicates that information about the target class can be extracted from the non-speech regions, flagging the presence of spurious correlations. The toolkit is publicly available for research use.
